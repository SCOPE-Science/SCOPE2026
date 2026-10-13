"""Exact checks for the fair-rally, side-out, win-by-two probability law.

Python 3 standard library only. Analytic arguments appear in RESULT.md.
"""
from fractions import Fraction as F

# Serving states in cyclic order: A1, A2, B1, B2.
Q = [[F((8, 4, 2, 1)[(j - i) % 4], 15) for j in range(4)]
     for i in range(4)]

# Exact deuce continuation values for score differences -1, 0, +1.
deuce = [
    [F(22, 43), F(14, 43), F(11, 86), F(11, 43)],
    [F(30, 43), F(45, 86), F(13, 43), F(41, 86)],
    [F(75, 86), F(32, 43), F(21, 43), F(29, 43)],
]

def verify_deuce():
    count = 0
    for i, d in enumerate((-1, 0, 1)):
        for s in range(4):
            rhs = F(0)
            for t in range(4):
                dd = d + (1 if t < 2 else -1)
                continuation = F(1) if dd == 2 else (F(0) if dd == -2 else deuce[dd + 1][t])
                rhs += Q[s][t] * continuation
            assert rhs == deuce[i][s], (i, s, rhs)
            count += 1
    return count

# Dictionary-polynomial operations with pairs of nonnegative degrees.
def add(*polys):
    ans = {}
    for poly in polys:
        for monomial, value in poly.items():
            ans[monomial] = ans.get(monomial, F(0)) + value
    return {k:v for k,v in ans.items() if v}

def scale(p, c):
    return {k: v*c for k,v in p.items() if v*c}

def mul(a, b):
    out = {}
    for (i,j), v in a.items():
        for (k,l), w in b.items():
            key = (i+k,j+l)
            out[key] = out.get(key,F(0)) + v*w
    return {k:v for k,v in out.items() if v}

one = {(0,0):F(1)}
x = {(1,0):F(1)}
y = {(0,1):F(1)}
den = add(scale(one,5),scale(x,-2),scale(y,-2),mul(x,y))
D = [scale(x,-1),add(scale(one,5),scale(y,-2)),y,add(scale(x,2),scale(one,-5))]

def verify_green():
    weights = [x,x,y,y]
    for t in range(4):
        lhs = D[t]
        for s in range(4):
            lhs = add(lhs,scale(mul(D[s],weights[t]),-Q[s][t]))
        rhs = scale(den,(1 if t == 1 else -1 if t == 3 else 0))
        assert lhs == rhs,(t,lhs,rhs)
    a = [sum(Q[s][t] for t in (0,1)) for s in range(4)]
    assert add(*(scale(D[s],a[s]) for s in range(4))) == add(one,scale(y,-1))
    assert add(*(scale(D[s],deuce[1][s]) for s in range(4))) == scale(add(scale(x,11),scale(y,-32),scale(one,10)),F(1,43))
    return 6

def legendre_at_three_fifths(m):
    if m == 0: return F(1)
    if m == 1: return F(3,5)
    prev, now = F(1), F(3,5)
    for k in range(1,m):
        prev,now = now,F((2*k+1)*F(3,5)*now-k*prev,k+1)
    return now

def direct_dp(n):
    table = [[None for _ in range(n)] for _ in range(n)]
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if i == n-1 and j == n-1:
                table[i][j] = deuce[1][:]
                continue
            row = []
            for s in range(4):
                ans=F(0)
                for t in range(4):
                    if t<2:
                        val = F(1) if i+1>=n and i+1-j>=2 else table[i+1][j][t]
                    else:
                        val = F(0) if j+1>=n and j+1-i>=2 else table[i][j+1][t]
                    ans += Q[s][t]*val
                row.append(ans)
            table[i][j] = row
    # Starting A2 versus B2, with the *same fixed team A*.
    return table[0][0][1]-table[0][0][3]

def formula(n):
    return (75*legendre_at_three_fifths(n-1)+55*legendre_at_three_fifths(n-2))/(86*5**n)

def run():
    checked_deuce=verify_deuce()
    checked_green=verify_green()
    comparisons = 0
    signs=[]
    for n in range(2,32):
        d = direct_dp(n)
        f = formula(n)
        assert d == f,(n,d,f)
        comparisons += 1
        if n in (11,15):
            signs.append((n,float(f)))
    # The Legendre normalization and diagonal initial coefficients.
    for m in range(2,32):
        a,b,c_leg=(legendre_at_three_fifths(m-2),legendre_at_three_fifths(m-1),legendre_at_three_fifths(m))
        assert m*c_leg == (2*m-1)*F(3,5)*b-(m-1)*a
    print('PASS exact deuce states:',checked_deuce)
    print('PASS polynomial Green identities:',checked_green)
    print('PASS independent rational game DP comparisons:',comparisons)
    print('PASS fixed-angle Legendre recurrence through degree 31')
    print('Sample first-serve effects:',signs)

if __name__=='__main__': run()
