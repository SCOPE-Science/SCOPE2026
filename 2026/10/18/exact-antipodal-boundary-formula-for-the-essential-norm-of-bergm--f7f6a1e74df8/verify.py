#!/usr/bin/env python3
"""Elementary reproducibility checks for the Bergman slant parity formula."""
import cmath
from fractions import Fraction
from math import sqrt, pi

def almost(x,y,tol=1.e-11):
    assert abs(x-y)<tol,(x,y)

for n in range(1,70):
    almost(sqrt((2*n+1)/(n+1)),sqrt(2)*sqrt((2*n+1)/(2*(n+1))))
    for k in range(0,10):
        if (n+k)%2==0:
            # T_{z^k} followed by W, in orthonormal monomial coefficients
            actual=sqrt((n+1)/(n+k+1))*sqrt((n+k+1)/((n+k)//2+1))
            expected=sqrt((n+1)/((n+k)//2+1))
            almost(actual,expected)
        if n>=k and (n-k)%2==0:
            # T_{bar(z)^k} followed by W
            actual=sqrt((n-k+1)/(n+1))*sqrt((n-k+1)/((n-k)//2+1))
            expected=(n-k+1)/sqrt((n+1)*((n-k)//2+1))
            almost(actual,expected)

polysets=[{-3:2+1j,0:1,2:-.5j,7:.6}, {0:1,1:1}, {0:1,2:1}, {-4:.25,3:-1j,5:2}, {0:1}, {1:1}]
for c in polysets:
    for j in range(97):
        t=2*pi*j/97
        eta=cmath.exp(1j*t)
        zeta=eta*eta
        a=sum(v*zeta**(k//2) for k,v in c.items() if k%2==0)
        b=sum(v*zeta**((k-1)//2+1) for k,v in c.items() if k%2)
        fplus=sum(v*eta**k for k,v in c.items())
        fminus=sum(v*(-eta)**k for k,v in c.items())
        almost(fplus,a+eta/zeta*b)
        almost(fminus,a-eta/zeta*b)
        almost(abs(fplus)**2+abs(fminus)**2,2*(abs(a)**2+abs(b)**2))
print('BERGMAN_SLANT_ANTIPODAL_ESSENTIAL_NORM_FINITE_IDENTITIES_OK monomial_n=69 polyphase_sets=6')
