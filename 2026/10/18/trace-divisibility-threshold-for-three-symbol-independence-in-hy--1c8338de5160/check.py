"""Exact-arithmetic reproducibility checks for the quantized Anosov three-block law.

Use: python check.py. No external dependencies.
"""
from fractions import Fraction as Q
from math import gcd, log, isclose


def cut(poly, a, b, c):
    """Clip a rational polygon against a*x+b*y <= c."""
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp = a*p[0]+b*p[1]-c
        fq = a*q[0]+b*q[1]-c
        if fp <= 0:
            out.append(p)
        if (fp < 0 and fq > 0) or (fp > 0 and fq < 0):
            z = fp/(fp-fq)
            out.append((p[0]+z*(q[0]-p[0]),p[1]+z*(q[1]-p[1])))
        elif fp > 0 and fq == 0:
            out.append(q)
    return out


def shoelace(poly):
    if not poly:
        return Q(0)
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly, poly[1:]+poly[:1])))/2


def area(t, r):
    square = [(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    square = cut(square,Q(-1),Q(t),Q(r+1))
    square = cut(square,Q(1),Q(-t),Q(-r))
    return shoelace(square)


def p(t, r):
    if r in (-1,t-1):
        return Q(1,2*t)
    if 0 <= r <= t-2:
        return Q(1,t)
    return Q(0)


def w(t, q, residue):
    return sum((p(t,j) for j in range(-1,t) if j%q==residue), Q(0))


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]


def test():
    for t in range(3,31):
        assert sum((p(t,r) for r in range(-1,t)),Q(0)) == 1
        assert [area(t,r) for r in range(-1,t)] == [p(t,r) for r in range(-1,t)]
        for q in range(2,41):
            ww = [w(t,q,r) for r in range(q)]
            assert sum(ww,Q(0)) == 1
            assert (len(set(ww)) == 1) == (q==2 or t%q==0), (t,q,ww)
            if q >= t+1:
                expected = [Q(1,2*t)]*2 + [Q(1,t)]*(t-1)
                assert sorted(x for x in ww if x) == sorted(expected)
                H = -sum(float(x)*log(float(x)) for x in ww if x)
                assert isclose(H, log(t)+log(2)/t, rel_tol=1e-12)
    for t in range(3,21):
        A=[[t,-1],[1,0]]
        rows=[]
        B=[[1,0],[0,1]]
        for n in range(9):
            rows.append(B[0])
            B=matmul(B,A)
        for i in range(9):
            for j in range(i+1,9):
                assert rows[i][0]*rows[j][1]-rows[i][1]*rows[j][0] != 0
    print('VERIFY_OK: rational polygon integration, arithmetic threshold, entropy, and pairwise ranks')


if __name__=='__main__':
    test()
