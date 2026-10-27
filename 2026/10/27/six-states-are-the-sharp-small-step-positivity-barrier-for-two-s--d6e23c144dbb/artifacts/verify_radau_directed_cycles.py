#!/usr/bin/env python3
"""Exact certificates for Radau IIA end-step positivity on directed CTMC cycles.

Run: python artifacts/verify_radau_directed_cycles.py
Requires SymPy. No floating-point claims are used to prove signs.
"""
from math import comb
import sympy as sp

h, z, t = sp.symbols('h z t')
r = (6+2*z)/(6-4*z+z*z)
coeffs = [sp.expand(sp.series(r, z, 0, 7).removeO()).coeff(z, j)
          for j in range(7)]
assert coeffs[:6] == [1,1,sp.Rational(1,2),sp.Rational(1,6),
                       sp.Rational(1,36),-sp.Rational(1,108)]
assert sp.solve(6-4*z+z*z,z) == [2-sp.sqrt(2)*sp.I, 2+sp.sqrt(2)*sp.I]

def cycle(n):
    P=sp.zeros(n)
    for i in range(n):
        P[i,(i+1)%n]=1
    Q=P-sp.eye(n)
    numerator=6*sp.eye(n)+2*h*Q
    denominator=6*sp.eye(n)-4*h*Q+h*h*Q*Q
    rows=[sp.cancel(x) for x in (denominator.inv()*numerator)[0,:]]
    base=sp.denom(rows[0])
    assert all(sp.simplify(sp.denom(x)-base)==0 for x in rows)
    numerators=[sp.expand(sp.fraction(x)[0]) for x in rows]
    assert all(sp.Poly(x,h).degree()<=2*n-2 for x in numerators)
    assert sp.simplify(sum(rows)-1)==0
    for i in range(n):
        for j in range(n):
            assert sp.simplify((denominator*denominator.inv()*numerator)[i,j]-numerator[i,j])==0
    return base,numerators

for n in range(2,7):
    den, nums=cycle(n)
    assert all(c>0 for c in sp.Poly(den,h).all_coeffs())
    if n<=5:
        for j,nu in enumerate(nums):
            coefficients=sp.Poly(nu,h).all_coeffs()
            assert all(c>=0 for c in coefficients)
            assert any(c>0 for c in coefficients)
            if j:
                assert sp.Poly(nu,h).terms()[-1][0][0]>=j
    if n==6:
        d_expected=(2*h*h+4*h+3)*(h**4+4*h**3+10*h*h+24*h+36)*\
                   (3*h**4+12*h**3+22*h*h+24*h+12)
        assert sp.expand(den-d_expected)==0
        p=h**5+15*h**4+60*h**3+90*h**2+36*h-12
        assert sp.expand(nums[5]-h**5*p)==0
        assert all(c>0 for c in sp.Poly(sp.diff(p,h),h).all_coeffs())
        assert p.subs(h,0)<0 and p.subs(h,1)>0
        for j in range(1,5):
            assert all(c>=0 for c in sp.Poly(nums[j],h).all_coeffs())
            assert nums[j] != 0
        # Nu_0 has two negative monomial coefficients. Exact positivity proof
        # on [0,1] is via all positive Bernstein coefficients of degree 10.
        nu0=sp.Poly(nums[0],h)
        asc=[nu0.nth(i) for i in range(11)]
        bernstein=[sum(asc[i]*sp.Rational(comb(k,i),comb(10,i))
                       for i in range(k+1)) for k in range(11)]
        assert all(c>0 for c in bernstein)
        assert bernstein == [sp.Integer(1296),sp.Rational(8424,5),
              sp.Rational(10968,5),sp.Rational(14297,5),
              sp.Rational(130552,35),sp.Rational(306616,63),
              sp.Rational(666497,105),sp.Rational(496103,60),
              sp.Rational(483569,45),sp.Rational(139181,10),sp.Integer(17945)]
        # Positivity on [1,infinity) by shifting h=1+t, all positive monomials.
        shifted=sp.Poly(sp.expand(nums[0].subs(h,1+t)),t)
        shifted_asc=[shifted.nth(i) for i in range(11)]
        assert shifted_asc == [17945,40269,38465,19230,4730,372,166,210,85,15,1]
        assert all(c>0 for c in shifted_asc)
        exact=sp.factor((nums[5]/den).subs(h,sp.Rational(1,10)))
        assert exact == -sp.Rational(743849,19268401151106)
        assert p.subs(h,sp.Rational(208608,1000000))<0
        assert p.subs(h,sp.Rational(208609,1000000))>0
        print('SIX_CYCLE_DENOMINATOR:',sp.factor(den))
        print('SIX_CYCLE_FIFTH_ENTRY:',sp.factor(nums[5]))
        print('SIX_CYCLE_EXACT_WITNESS:',exact)
        print('SIX_CYCLE_BERNSTEIN_DIAGONAL:',bernstein)
        print('SIX_CYCLE_SHIFTED_DIAGONAL:',shifted_asc)
    print('CYCLE_CERTIFIED:',n,'row classes',len(nums),'degree',sp.degree(den,h))
print('VERIFY_OK: 5 exact cycle systems; universal Taylor-prefix coefficients; '
      'all short-cycle positive numerator certificates; sixth-cycle unique-root '
      'and diagonal Bernstein/shift certificates; exact negative witness; stochasticity')
