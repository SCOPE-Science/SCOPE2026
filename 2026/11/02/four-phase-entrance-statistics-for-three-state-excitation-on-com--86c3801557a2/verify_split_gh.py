#!/usr/bin/env python3
"""Exact self-contained check for three-state Greenberg-Hastings on complete split graphs.
Only the mathematical rule, finite color-support automaton, and independent labelled evolution are used.
"""
from collections import defaultdict
from itertools import product

def mask_step(z):
    c, i = z
    ec = bool(c & 2)
    ei = bool(i & 2)
    def trans(mask, excite):
        out = 0
        for color in range(3):
            if mask & (1 << color):
                new = (color + 1) % 3 if color else int(excite)
                out |= 1 << new
        return out
    return trans(c, ec or ei), trans(i, ec)

def support_class(z):
    seen = {}
    cur = z
    while cur not in seen:
        seen[cur] = len(seen)
        cur = mask_step(cur)
    return seen[cur], len(seen) - seen[cur]

def monomial(z):
    c, i = z
    # Formal monomial exponents: x=U_2(m), y=U_2(n), u=U_3(m), v=U_3(n)
    a, b = c.bit_count(), i.bit_count()
    return (int(a == 2), int(b == 2), int(a == 3), int(b == 3))

def add_poly(out, term, coeff=1):
    out[term] += coeff

def form_coefficients():
    hist = defaultdict(lambda: defaultdict(int))
    rows = []
    for c in range(1, 8):
        for i in range(1, 8):
            z = (c, i)
            nxt = mask_step(z)
            t, cycle = support_class(z)
            # The unique singleton-mask fixed component is the zero state;
            # the full-mask fixed component has microscopic least period three.
            cyc_state = z
            for _ in range(t):
                cyc_state = mask_step(cyc_state)
            p = 1 if cyc_state == (1, 1) else 3
            assert cycle in (1, 3) and (cycle == 3 or cyc_state in ((1, 1), (7, 7)))
            hist[t, p][monomial(z)] += 1
            rows.append((c, i, nxt[0], nxt[1], t, p))
    return hist, rows

# Explicit polynomial expected coefficients; keys (t,period), values monomial->coefficient.
# x=2**m-2, y=2**n-2, u=3**m-3*2**m+3, v=3**n-3*2**n+3.
ONE=(0,0,0,0)
X=(1,0,0,0); Y=(0,1,0,0); U=(0,0,1,0); V=(0,0,0,1)
XY=(1,1,0,0); UV=(0,0,1,1); UY=(0,1,1,0); XV=(1,0,0,1)
EXPECTED={
 (0,1):{ONE:1},
 (0,3):{UV:1, UY:3, U:3, XY:3, X:3},
 (1,1):{XY:1, X:2, Y:2, ONE:3},
 (1,3):{XV:1, XY:1},
 (2,1):{V:1,XY:1,X:2,Y:3,ONE:3},
 (2,3):{XV:1,XY:1},
 (3,1):{V:1,XY:1,X:2,Y:2,ONE:2},
 (3,3):{XV:1,XY:1},
 (4,1):{V:1,Y:2},
}

def num_onto(k,n):
    if k == 1:return 1
    if k == 2:return 2**n-2
    if k == 3:return 3**n-3*(2**n)+3
    raise ValueError(k)

def expected_num(m,n):
    x,y=2**m-2,2**n-2
    u,v=3**m-3*2**m+3,3**n-3*2**n+3
    vals=(x,y,u,v)
    ans={}
    for k,poly in EXPECTED.items():
        ans[k]=sum(coeff * __import__('math').prod(vals[j]**power for j,power in enumerate(monom)) for monom,coeff in poly.items())
    return ans

def microscopic_step(state,m,n):
    # Explicit graph-neighborhood evaluation (not color-support transitions).
    out=[]
    for j,s in enumerate(state):
        if s == 1:out.append(2)
        elif s == 2:out.append(0)
        else:
            if j < m:
                excited=any(state[k] == 1 for k in range(m+n) if k != j)
            else:
                excited=any(state[k] == 1 for k in range(m))
            out.append(1 if excited else 0)
    return tuple(out)

def trajectory_class(state,m,n):
    states=[state]
    for _ in range(7):
        states.append(microscopic_step(states[-1],m,n))
    assert states[4] == states[7]
    for t in range(5):
        if states[t] == states[t+3]:
            return t, 1 if states[t] == states[t+1] else 3
    raise AssertionError('No entry by four updates')

def main():
    hist,rows=form_coefficients()
    hist={k:dict(v) for k,v in hist.items()}
    assert hist == EXPECTED, (hist,EXPECTED)
    assert len(rows)==49
    print('SUPPORT_CERTIFICATE_OK: 49 exact transitions; nine entry/period classes; all polynomial coefficients')
    tests=0; params=0; orbit_checks=0
    for m in range(1,8):
        for n in range(1,8):
            predicted=expected_num(m,n)
            assert sum(predicted.values()) == 3**(m+n)
            assert sum(v for (t,p),v in predicted.items() if p==1) == 3**(n+1)+3*(2**m-2)*(2**n)
            assert predicted[0,3] == (3**m-3*2**m+3)*3**n +3*(2**m-2)*(2**n-1)
            assert predicted[4,1] > 0 if n>=2 else predicted[4,1]==0
            params+=1
            if m+n>10:continue
            got=defaultdict(int)
            for s in product(range(3),repeat=m+n):
                k=trajectory_class(s,m,n)
                got[k]+=1
                tests+=1
            assert all(got[k]==predicted[k] for k in EXPECTED),(m,n,got,predicted)
            assert sum(got.values())==3**(m+n)
            orbit_checks+=1
    print('MICROSCOPIC_CHECK_OK: %d labelled configurations over %d graph sizes'%(tests,orbit_checks))
    print('FORMULA_CHECK_OK: %d graph-size pairs; extinction basin, period-three counts, sharp clock'%params)
    print('BASELINE: (m,n)=(2,1),(2,2),(3,2),(3,3)')
    for m,n in [(2,1),(2,2),(3,2),(3,3)]:
        pred=expected_num(m,n)
        print('%d,%d: %s'%(m,n,' '.join('%s:%s'%(k,pred[k]) for k in sorted(pred))))
    print('CERTIFICATE_ROWS_BEGIN')
    print('clique_mask,independent_mask,next_clique_mask,next_independent_mask,first_entry,least_period')
    for line in rows:print(','.join(map(str,line)))
    print('CERTIFICATE_ROWS_END')
if __name__=='__main__':main()
