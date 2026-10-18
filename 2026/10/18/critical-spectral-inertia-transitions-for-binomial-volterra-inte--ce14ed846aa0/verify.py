#!/usr/bin/env python3
"""Finite, reproducible checks for a Bergman Volterra commutator formula.
No finite computation is used as a substitute for the infinite-dimensional proof.
"""
import cmath
from fractions import Fraction
from math import sqrt

TESTS = 0

def check(condition, message):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(message)

def w(k, r):
    if k < 0:
        return 0.0
    return r * sqrt((k+1)/(k+r+1))/(k+r)

def diagonal(k, m, n, a, b):
    return abs(a)**2 * (w(k,m)**2 - (w(k-m,m)**2 if k>=m else 0)) + abs(b)**2 * (w(k,n)**2 - (w(k-n,n)**2 if k>=n else 0))

def upper(k, m, n, a, b):
    q=n-m
    return a*b.conjugate() * (w(k,n)*w(k+q,m) - (w(k-m,m)*w(k-m,n) if k>=m else 0))

def diagonal_exact(k,m,n,aa,bb):
    z=Fraction(0)
    for r,c in [(m,aa),(n,bb)]:
        z += c*c * Fraction(r*r*(k+1),(k+r)**2*(k+r+1))
        if k>=r:
            z -= c*c * Fraction(r*r*(k-r+1),k*k*(k+1))
    return z

def upper_magnitude_squared_exact(k,m,n,aa,bb):
    q=n-m
    p=Fraction((k+1)*(k+q+1),(k+n)**2*(k+n+1))
    if k>=m:
        p-=Fraction(k-m+1,k*(k+q))
    return Fraction(aa*aa*bb*bb*m*m*n*n,(k+1)*(k+q+1))*p*p

def direct_principal(size,m,n,a,b):
    length=size+n
    t=[[0j for _ in range(length)] for _ in range(length)]
    for k in range(length):
        if k+m<length:t[k+m][k]+=a*w(k,m)
        if k+n<length:t[k+n][k]+=b*w(k,n)
    return [[sum(t[u][i].conjugate()*t[u][j] for u in range(length)) -
             sum(t[i][u]*t[j][u].conjugate() for u in range(length))
             for j in range(size)] for i in range(size)]

for m,n in [(1,2),(1,3),(1,5),(2,3),(2,5),(3,5),(3,8)]:
    for a,b in [(1+0j,1+0j),(3+0j,1+0j),(1+2j,2-1j)]:
        size=15
        h=direct_principal(size,m,n,a,b)
        q=n-m
        for i in range(size):
            for j in range(size):
                target=(diagonal(i,m,n,a,b) if i==j else
                        upper(i,m,n,a,b) if j==i+q else
                        upper(j,m,n,a,b).conjugate() if i==j+q else 0)
                check(abs(h[i][j]-target)<4e-13,("matrix",m,n,a,b,i,j,h[i][j],target))

for m,n in [(1,2),(1,4),(2,3),(2,7),(4,9)]:
    for aa,bb in [(0,1),(1,0),(1,1),(2,3),(5,2)]:
        for k in range(max(m,n)+2,max(m,n)+15):
            check(abs(diagonal(k,m,n,complex(aa),complex(bb))-float(diagonal_exact(k,m,n,aa,bb)))<5e-14,
                  ("exact diagonal",m,n,k,aa,bb))
            check(abs(abs(upper(k,m,n,complex(aa),complex(bb)))**2 - float(upper_magnitude_squared_exact(k,m,n,aa,bb)))<2e-13,
                  ("exact offdiagonal",m,n,k,aa,bb))
        k=50000
        Q=m**3*aa**2+n**3*bb**2
        B=m*n*(m+n)*aa*bb
        d=float(diagonal_exact(k,m,n,aa,bb)*k**3)
        c2=float(upper_magnitude_squared_exact(k,m,n,aa,bb)*k**6)
        check(abs(d+2*Q)<(1+Q)*.012,("diagonal asymptotic",m,n,aa,bb,d,-2*Q))
        check(abs(sqrt(c2)-B)<(1+B)*.012,("offdiagonal asymptotic",m,n,aa,bb,sqrt(c2),B))

# Positivity/negativity of finite quadratic forms on distant disjoint blocks:
# in the mixed range there are positive blocks; beyond the two endpoints,
# eventually the diagonal strictly dominates the offdiagonal.
for m,n in [(1,2),(1,3),(2,3),(2,5)]:
    b=1+0j
    r=n/m
    a=complex((r+r*r)/2)
    Q=m**3*abs(a)**2+n**3
    B=m*n*(m+n)*abs(a)
    check(B>Q,("strict phase region",m,n))
    block=120
    k0=100000
    inds=[k0+i*(n-m) for i in range(block)]
    vec=[(-1)**i for i in range(block)]
    # c_k is negative with a,b positive; alternating signs make edges positive.
    quadratic=sum(diagonal(k,m,n,a,b) for k in inds)
    quadratic+=sum(2*(upper(k,m,n,a,b)*vec[i]*vec[i+1]).real for i,k in enumerate(inds[:-1]))
    check(quadratic>0,("positive block witness",m,n,quadratic))
    for a0 in [r*.5,r*r*1.5]:
        a=complex(a0)
        Q=m**3*abs(a)**2+n**3
        B=m*n*(m+n)*abs(a)
        check(Q>B,("finite-positive regime",m,n,a0))
        for k in [200000,300000,400000]:
            edge=abs(upper(k-(n-m),m,n,a,b))+abs(upper(k,m,n,a,b))
            check(diagonal(k,m,n,a,b)+edge<0,("strict negative diagonal dominance",m,n,a0,k))


# High-precision checks of the asymmetric critical edge.  These verify finite
# instances only; the theorem uses proved rational asymptotic coefficients.
from decimal import Decimal, localcontext

def dec_frac(f):
    return Decimal(f.numerator) / Decimal(f.denominator)

def exact_decimal_upper(k,m,n,a,b):
    q=n-m
    p=Fraction((k+1)*(k+q+1),(k+n)**2*(k+n+1))
    if k>=m:
        p-=Fraction(k-m+1,k*(k+q))
    return dec_frac(a*b*m*n)*dec_frac(p)/Decimal((k+1)*(k+q+1)).sqrt()

def exact_decimal_diag(k,m,n,a,b):
    return dec_frac(diagonal_exact(k,m,n,a,b))

with localcontext() as ctx:
    ctx.prec=65
    for m,n in [(1,2),(1,3),(2,3),(2,5)]:
        q=n-m
        for a in [Fraction(n,m),Fraction(n*n,m*m)]:
            b=Fraction(1)
            P=m**4*a*a+n**4*b*b
            W=2*(3*P-m*n*(m*m+4*m*n+n*n)*a*b)
            k=1000000
            V=exact_decimal_diag(k,m,n,a,b)-exact_decimal_upper(k-q,m,n,a,b)-exact_decimal_upper(k,m,n,a,b)
            check(abs(V*Decimal(k)**4-dec_frac(W)) < abs(dec_frac(W))/Decimal(10000),
                  ('critical potential expansion',m,n,a,V*Decimal(k)**4,W))
            check((W>0)==(a==Fraction(n,m)),('critical edge direction',m,n,a,W))
            if a==Fraction(n,m):
                # Hat functions produce genuine positive finite-dimensional
                # witnesses on a remote q-chain, including the lower edge.
                start, length=10000,1000
                vec=[Decimal(min(i+1,length-i)) for i in range(length)]
                energy=Decimal(0)
                for i,x in enumerate(vec):
                    k=start+i*q
                    potential=exact_decimal_diag(k,m,n,a,b)-exact_decimal_upper(k-q,m,n,a,b)-exact_decimal_upper(k,m,n,a,b)
                    energy+=potential*x*x
                for i in range(-1,length):
                    k=start+i*q
                    delta=(vec[i+1] if i+1<length else Decimal(0))-(vec[i] if i>=0 else Decimal(0))
                    energy+=exact_decimal_upper(k,m,n,a,b)*delta*delta
                check(energy>0,('lower-edge positive block',m,n,energy))

print("VERIFICATION_OK",TESTS)
