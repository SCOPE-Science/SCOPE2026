#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-three parabolic sixth-moment second variation.

Only Python's standard library is required. Computes independently by exhaustive
ordered pair/triple enumeration, without importing a proof-side fiber formula.
"""
from collections import defaultdict

POLYNOMIALS = {
    1: (0, 1),           # F_3
    2: (1, 0, 1),        # t^2+1
    3: (2, 2, 0, 1),     # t^3-t-1
    4: (1, 0, 1, 1, 1),  # t^4+t^3+t^2+1
}


def field(n):
    q = 3 ** n
    poly = POLYNOMIALS[n]
    digs = [tuple((z // 3 ** j) % 3 for j in range(n)) for z in range(q)]
    powers = [3 ** j for j in range(n)]

    def enc(a):
        return sum((v % 3) * powers[j] for j, v in enumerate(a))

    add = [[enc([x+y for x,y in zip(digs[i],digs[j])]) for j in range(q)] for i in range(q)]
    neg = [enc([-x for x in digs[i]]) for i in range(q)]
    mul = [[0]*q for _ in range(q)]
    for x in range(q):
        for y in range(q):
            conv = [0]*(2*n-1)
            for i,a in enumerate(digs[x]):
                for j,b in enumerate(digs[y]):
                    conv[i+j] += a*b
            for k in range(2*n-2,n-1,-1):
                coeff = conv[k] % 3
                for j in range(n):
                    conv[k-n+j] -= coeff * poly[j]
            mul[x][y] = enc(conv[:n])
    assert all(mul[i][j] != 0 for i in range(1,q) for j in range(1,q))
    return q,add,neg,mul


def check(n):
    q, add, neg, mul = field(n)
    sq = [mul[x][x] for x in range(q)]
    r2 = defaultdict(int)
    for a in range(q):
        for b in range(q):
            r2[(add[a][b],add[sq[a]][sq[b]])] += 1
    assert sum(v*v for v in r2.values()) == 2*q*q-q
    k01 = 0
    for (s,w), value in r2.items():
        sm1 = add[s][neg[1]]
        wm1 = add[w][neg[1]]
        k01 += value*r2.get((sm1,wm1),0)
    assert k01 == q*q

    fibers = defaultdict(list)
    for a in range(q):
        for b in range(q):
            s2, w2 = add[a][b],add[sq[a]][sq[b]]
            for c in range(q):
                fibers[(add[s2][c],add[w2][sq[c]])].append((a,b,c))
    reps = {key:len(val) for key,val in fibers.items()}
    for (s,w), v in reps.items():
        if s: assert v==q
        elif w==0: assert v==q
        else: assert v==2*q
    assert sum(v*v for v in reps.values()) == q**4+q**3-q**2
    for x,y,expected in [(0,0,q*q),(0,1,q*q+q)]:
        l = 0
        for z in range(q):
            s=add[add[x][y]][z]
            w=add[add[sq[x]][sq[y]]][sq[z]]
            l += reps[(s,w)]
        assert l==expected

    # Exact Taylor coefficients for a nonconstant mean-zero perturbation.
    h = [0]*q
    h[0],h[1] = 1,-1
    norm = sum(z*z for z in h)
    aa=0
    bc=0
    for key, triple_list in fibers.items():
        b=len(triple_list)
        first = sum(h[x]+h[y]+h[z] for x,y,z in triple_list)
        second = sum(h[x]*h[y]+h[x]*h[z]+h[y]*h[z]
                     for x,y,z in triple_list)
        aa += first*first
        bc += b*second
    assert aa==9*(q*q-q)*norm,(q,aa)
    assert bc==-3*q*norm,(q,bc)
    assert aa+2*bc==(9*q*q-15*q)*norm
    assert aa-2*bc==(9*q*q-3*q)*norm
    m0=sum(v*v for v in reps.values())
    # Integer numerator of the normalized Taylor coefficients, before division by q^4.
    hre = aa+2*bc-3*m0*norm//q
    him = aa-2*bc-3*m0*norm//q
    assert hre == -3*q*(q*q-2*q+4)*norm
    assert him == -3*q*q*(q-2)*norm
    print(f'q={q}: pairs={q*q}, triples={q**3}, fibers={len(fibers)}, '
          f'M0={m0}, K01={k01}, L01=({q*q},{q*q+q}), '
          f'Taylor integers=({hre},{him}) PASS')


if __name__=='__main__':
    for n in (1,2,3,4):
        check(n)
    print('All exact checks passed. Finite tests are not the unrestricted proof.')
