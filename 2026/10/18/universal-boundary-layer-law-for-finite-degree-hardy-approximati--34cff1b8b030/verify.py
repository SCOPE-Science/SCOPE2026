#!/usr/bin/env python3
"""Reproduce exact H4 coefficients and boundary-layer numerics (requires mpmath)."""
import math
import mpmath as mp
mp.mp.dps=65

def H4(a,u,v):
    return 1+4*u*u+4*v*v+u**4+v**4+4*u*u*v*v-4*u*u*v+4*a*u+4*a*u**3+8*a*u*v*v+2*a*a*u*u+4*a*a*u*u*v

def baseline4(a): return 6-8*a+2*a*a

def main():
    c=(mp.mpf(2)/3)**(mp.mpf(1)/3)
    target=18*c**4
    print('H4: limiting polynomial coefficients c=(2/3)^(1/3)=',mp.nstr(c,22))
    print('H4: predicted improvement coefficient =',mp.nstr(target,22))
    for exponent in (2,3,4,5,6,9,12):
        eps=mp.mpf(10)**(-exponent); a=1-eps; delta=eps**(mp.mpf(1)/3)
        f=lambda u,v:mp.diff(lambda t:H4(a,t,v),u)
        g=lambda u,v:mp.diff(lambda t:H4(a,u,t),v)
        u,v=mp.findroot((f,g),(-1+c*delta,c*delta),tol=mp.mpf('1e-55'))
        base=baseline4(a); loss=H4(a,u,v)
        uc=(u+1)/delta;vc=v/delta;rc=(base-loss)/eps**(mp.mpf(4)/3)
        print('eps=1e-%d'%exponent,'q0 increment/scale=',mp.nstr(uc,13),'q1/scale=',mp.nstr(vc,13),'improvement/scale=',mp.nstr(rc,13))
        assert loss<=base and abs(uc-c)<mp.mpf('.15') and abs(vc-c)<mp.mpf('.30')
        if exponent==12:
            assert abs(uc-c)<mp.mpf('.00012') and abs(vc-c)<mp.mpf('.00012') and abs(rc-target)<mp.mpf('.005')
    print('Exact polynomial baseline sixth-moment checks:')
    m=3
    def baseline_even(a):
        return sum(math.comb(m,j)*math.comb(m,k)*(-a)**abs(j-k) for j in range(m+1) for k in range(m+1))
    for eps in (mp.mpf('0.01'),mp.mpf('0.0001'),mp.mpf('0.000001')):
        print('eps=',mp.nstr(eps,9),'baseline6/eps=',mp.nstr(baseline_even(1-eps)/eps,15))
        assert abs(baseline_even(1-eps)/eps-12)<mp.mpf('.25')
    print('Numerical checks passed. These checks support, but do not replace, the analytical proof.')
if __name__=='__main__':main()
