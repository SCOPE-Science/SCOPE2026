#!/usr/bin/env python3
"""Supplementary exact-rational checks of the stated radial moment-gap identities."""
from fractions import Fraction as F
from math import factorial

def gamma_moments(beta, n=12):
    return [F(factorial(k+beta)) for k in range(n+1)]

def annulus_moments(d, n=12):
    return [((1+d)**(k+1)-(1-d)**(k+1))/F(k+1) for k in range(n+1)]

def mixture_moments(n=12):
    return [F(factorial(k)+factorial(k+3)) for k in range(n+1)]

def poly_norm_squared(coefs, m):
    return sum((F(c)*F(c))*m[k] for k,c in enumerate(coefs))

def test(m, R=None):
    checks=0
    s=m[1]/m[0]
    delta=1-m[1]*m[1]/(m[0]*m[2])
    assert 0<delta<1; checks+=1
    for n in range(2,len(m)):
        assert s*m[n-1]/m[n] <= 1-delta
        checks+=1
    for a in (F(0),F(1,3),F(2,3),-F(1,4)):
        # For g=z(z+conj(a)*R), f=z(a*z+R): exact positive coefficient gap.
        deficit=(1-a*a)*(m[2]-s*m[1])
        target=(1-a*a)*delta*m[2]
        assert deficit==target
        checks+=1
    if R is not None:
        assert R*R==s
        for a in (F(0),F(1,3),F(-1,4)):
            # Test the exact two-polynomial witness via both moment norms.
            g=[F(0),a*R,F(1)]
            f=[F(0),R,a]
            assert poly_norm_squared(g,m)-poly_norm_squared(f,m)==(1-a*a)*delta*m[2]
            checks+=1
            # Nonconstant polynomial multiplier h: g=(z+a*R)h, f=(a*z+R)h.
            for h in ([F(1),F(2)],[F(1,2),F(-3,4),F(2,3)]):
                gg=[F(0)]*(len(h)+1);ff=[F(0)]*(len(h)+1)
                for j,c in enumerate(h):
                    gg[j]+=a*R*c;gg[j+1]+=c
                    ff[j]+=R*c;ff[j+1]+=a*c
                deficit=poly_norm_squared(gg,m)-poly_norm_squared(ff,m)
                rhs=(1-a*a)*sum((m[j+1]-s*m[j])*h[j]*h[j] for j in range(len(h)))
                gap=(1-a*a)*delta*sum(m[j+1]*h[j]*h[j] for j in range(1,len(h)))
                assert deficit==rhs and deficit>=gap
                checks+=2
    return checks

checks=0
for beta in (0,3,10):
    checks+=test(gamma_moments(beta), F(1) if beta==0 else (F(2) if beta==3 else None))
for d in (F(1,3),F(1,2),F(2,3)):
    m=annulus_moments(d)
    assert 1-m[1]*m[1]/(m[0]*m[2])==d*d/(3+d*d)
    checks+=1+test(m,F(1))
checks+=test(mixture_moments())
print('CHECK_OK',checks)
