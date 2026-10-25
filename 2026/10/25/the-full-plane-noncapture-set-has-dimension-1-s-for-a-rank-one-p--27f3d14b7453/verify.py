"""Exact rational checks supporting the exceptional-set dimension calculation.

Run: python verify_exceptional_dimension.py
The infinite Cantor and planar dimension conclusions require the analytic proof
in RESULT.md; these finite checks are not substitutes for that proof.
"""
from fractions import Fraction as Q
from itertools import product

B=Q(-13,16)
A=Q(-11,16)
Z=Q(13,16)
L=Q(-19,32)
R=Q(-3,16)


def F(p):
    x,y=p
    return (abs(x)-y-1, x-abs(y)+B)


def F_n(p,n):
    for _ in range(n): p=F(p)
    return p


def G(u):
    assert A<=u<=Z
    if u<=L: return 16*u+Q(165,16)
    if u<=R: return Z
    if u<=0: return -8*u-Q(11,16)
    return A


def T(p):
    x,y=p
    return (abs(x)-y-16,x-abs(y)-13)


def check():
    checks=0
    period=[(Q(-11,16),Q(-1,2))]
    for _ in range(5):period.append(F(period[-1]))
    assert len(set(period))==6 and F(period[-1])==period[0]
    checks+=2
    assert F_n((Q(-19,16),Q(-1)),5)==period[0]
    checks+=1
    p=(Q(13,16),Q(-1))
    assert F(p)==p
    checks+=1
    # In the two singular quadrant images, Y'-X'=3 and X'+Y'=-29.
    assert 16*p[1]-16*p[0]!=3 and 16*p[0]+16*p[1]!=-29
    checks+=2
    # For the invertible quadrants, solve preimages of (13,-16).
    # Q2 candidate (-16,-13) violates Y >= 0; Q4 candidate (13,-16) is p.
    assert Q(-13)<0 and T((13,-16))==(13,-16)
    checks+=2
    assert 16*A==-11 and 16*Z==13 and 16*L==Q(-19,2) and 16*R==-3
    checks+=4
    # Direct six-step iterates on a fine rational grid, including breakpoints.
    grid=[A+(Z-A)*Q(j,300) for j in range(301)]+[A,L,R,Q(0),Z]
    for u in grid:
        p0=(u,u+Q(3,16))
        v=G(u)
        assert F_n(p0,6)==(v,v+Q(3,16)),(u,F_n(p0,6),v)
        checks+=1
    # Every integer-grid state in Pi reaches the endpoint of the six-cycle.
    max_steps=0
    for k in range(-11,14):
        u=Q(k,16)
        assert F_n((u,u+Q(3,16)),6)==(G(u),G(u)+Q(3,16))
        checks+=1
        n=0
        while u!=A and n<10:
            u=G(u)
            n+=1
        assert u==A
        max_steps=max(n,max_steps)
        checks+=1
    assert max_steps<=3
    checks+=1
    # Exact scaling conjugacy on integer points, including branch boundaries.
    for x,y in product(range(-15,16),repeat=2):
        v=T((x,y))
        w=F((Q(x,16),Q(y,16)))
        assert v==(16*w[0],16*w[1])
        checks+=1
    # Branch slope and endpoint identities for the two inverse similarities.
    assert G(A)==A and G(L)==Z and G(R)==Z and G(0)==A
    assert L-A==(Z-A)/16 and 0-R==(Z-A)/8
    assert L<R
    checks+=3
    print('EXACT_RATIONAL_CHECKS_PASSED',checks)
    print('MAX_INTEGER_GRID_RETURN_ITERATES',max_steps)
    print('PERIOD_SIX',period)
    print('LEFT_RIGHT_INVERSE_RATIOS','1/16','1/8')


if __name__=='__main__': check()
