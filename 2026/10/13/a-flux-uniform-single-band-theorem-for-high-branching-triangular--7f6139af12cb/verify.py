"""Standalone exact consistency checks for triangular-block adjacency resolvents.

The proof of the all-parameter theorem is analytical; this script checks
finite rational specializations and the first return moments only.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict


def cubic_disc(a, b, c, d):
    return b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d


def D(m, c, E):
    return (E**4+2*(m-1)*c*E**3+(m*m-12*m+9)*E**2
            -18*m*(m-1)*c*E-(2*m-3)**3-27*(m-1)**2*c*c)


def poly_convolve(a, b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def formal_series_recip(a, n):
    assert a[0] == 1
    b=[1]
    for k in range(1,n+1):
        b.append(-sum(a[i]*b[k-i] for i in range(1,min(k,len(a)-1)+1)))
    return b


def exact_moments(n):
    # A 3-triangle-per-vertex cactus is Cayley(F_2, {a,b,ab} +/-).
    def mul(w,gen):
        w=list(w)
        for ch in gen:
            if w and w[-1]==-ch: w.pop()
            else: w.append(ch)
        return tuple(w)
    gens=[(1,),(-1,),(2,),(-2,),(1,2),(-2,-1)]
    current={():1}
    out=[1]
    for _ in range(n):
        nxt=defaultdict(int)
        for word,count in current.items():
            for gen in gens: nxt[mul(word,gen)]+=count
        out.append(nxt.get((),0))
        current=nxt
    return out


def cavity_moments(N):
    # u=1/z and Y=y/z=1+sum_{k>=2} a_k u^k.
    # y=z-(m-1)*2(y+c)/(y*y-1), at m=3,c=1.
    # Solve coefficientwise in u via formal power series to avoid numeric roots.
    m=3; c=1
    A=[F(1)]+[F(0)]*(N+4)
    def mul(a,b):
        return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(N+5)]
    # Y^3 - Y^2 +(2m-3)*u^2*Y + u^2 +2(m-1)c*u^3=0.
    # Coeff at u^k of Y^3-Y^2 is a_k (because 3-2=1).
    for k in range(1,N+3):
        aa=mul(A,A); aaa=mul(aa,A)
        rem=aaa[k]-aa[k] + (2*m-3)*(A[k-2] if k>=2 else 0)
        rem += F(1) if k==2 else 0
        rem += F(2*(m-1)*c) if k==3 else 0
        A[k]=-rem
    # Root resolvent G= u /(Y -2m*u^2*(Y+c*u)/(Y^2-u^2)).
    # Equivalently G=u*(Y^2-u^2)/(Y^3-3*u^2*Y-2*c*u^3).
    yy=mul(A,A); yyy=mul(yy,A)
    num=[yy[k]-(1 if k==2 else 0) for k in range(N+4)]
    den=[yyy[k]-3*(A[k-2] if k>=2 else 0)-(2*c if k==3 else 0) for k in range(N+4)]
    inv=formal_series_recip(den,N)
    gg=poly_convolve(num[:N+1],inv)[:N+1]
    return [int(x) if x.denominator==1 else x for x in gg]


def main():
    for m in range(3,12):
        for c in [F(-1),F(-3,4),F(-1,3),F(0),F(1,5),F(2,3),F(1)]:
            for E in [F(-11,2),F(-1),F(0),F(2,7),F(3),F(9)]:
                # y^3-E y^2+(2m-3)y+E+2(m-1)c.
                disc=cubic_disc(1,-E,2*m-3,E+2*(m-1)*c)
                assert disc == 4*D(m,c,E)
        for E in [F(-2),F(0),F(5)]:
            # Factorization for zero flux angle c=1:
            # P=(y+1)*(y^2-(E+1)y+E+2m-2).
            q=[E+2*m-2,-E-1,1]
            p=poly_convolve([1,1],q)
            assert p==[E+2*m-2,2*m-3,-E,1]
    walks=exact_moments(8)
    formal=cavity_moments(8)
    assert walks==formal, (walks,formal)
    assert walks==[1,0,6,6,66,150,954,3150,16290]
    print('VERIFY_OK m=3..11 rational_cubic_discriminants factorization F2_return_moments_0..8')

if __name__=='__main__': main()
