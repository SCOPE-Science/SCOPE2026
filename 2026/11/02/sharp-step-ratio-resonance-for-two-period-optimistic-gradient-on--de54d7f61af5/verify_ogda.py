"""Reproducible finite checks for the exact two-period OGDA stability theorem.

Run: python3 verify_ogda.py
The analytic proof, not this finite checker, establishes stability for all parameters.
"""
from fractions import Fraction as Q
from cmath import sqrt
from math import sqrt as rsqrt


def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def transfer(h):
    z = complex(h)
    return ((1-2j*z, 1j*z), (1, 0))


def monodromy(u, v):
    return mm(transfer(v), transfer(u))


def eigenvalues(u, v):
    r = float(u*v)
    tr = complex(1-4*u*v, -(u+v))
    d = sqrt(tr*tr+4*r)
    return ((tr+d)/2, (tr-d)/2)


def delta(u, v):
    r=u*v
    s=u+v
    return 3*r*(2-5*r)*(1+r)**2-s*s*(1-r)**2


def check():
    count=0
    vals=[Q(i,100) for i in (1,2,3,7,11,21,33,41,55,60,70)]
    for u in vals:
        for v in vals:
            M=monodromy(u,v)
            tr=M[0][0]+M[1][1]
            det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
            exact_tr=1-4*u*v-1j*float(u+v)
            assert abs(tr-exact_tr)<3e-14
            assert abs(det+float(u*v))<3e-14
            if u*v < 1 and delta(u,v) != 0:
                rho=max(abs(z) for z in eigenvalues(u,v))
                assert (rho<1)==(delta(u,v)>0), (u,v,rho)
            count += 1
    u,v=Q(1,100),Q(1,10)
    assert delta(u,v) == Q(-1215767223,200000000000)
    assert max(abs(z) for z in eigenvalues(u,v))>1
    count+=2
    for h in vals:
        # Delta for constant h factors with exact rational arithmetic.
        D=delta(h,h)
        factor=-h*h*(h*h+2)*(3*h*h-1)*(5*h*h+1)
        assert D==factor
        count+=1
    for a,b in [(1,1),(1,2),(1,3),(1,4),(1,5),(3,1),(4,1),(10,1)]:
        limit=6*a*b-(a+b)**2
        for den in (100,300,1000):
            u,v=Q(a,den),Q(b,den)
            assert (delta(u,v)>0)==(limit>0)
            count+=1
    critical=2+rsqrt(3)
    assert 3.7<critical<3.8
    for x in (1.01,2,3.5):
        assert (1+x)**2<6*x
    for x in (4,7):
        assert (1+x)**2>6*x
    print(f'VERIFY_OK {count} exact/finite stability and asymptotic checks')


if __name__=='__main__':
    check()
