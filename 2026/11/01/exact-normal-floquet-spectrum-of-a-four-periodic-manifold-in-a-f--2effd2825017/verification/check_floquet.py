"""Exact symbolic reconstruction of the 20-dimensional logarithmic return derivative.
Run with: python verification/check_floquet.py (requires SymPy).
"""
import sympy as S
p = S.symbols('p', positive=True)
T = S.zeros(20)
for component in range(4):
    for lag in range(4):
        T[5*component+lag,5*component+lag+1] = 1
# History order for each component: times n-4,...,n.
for u in range(4):
    forward = [((u,-3),1),(((u+1)%4,-4),1),(((u+1)%4,0),-1)]
    product = [(u,-3),((u+1)%4,-4),((u+2)%4,-1),((u+3)%4,-2)]
    for (v,lag), coefficient in forward + [(a,p-1) for a in product]:
        T[5*u+4,5*v+lag+4] += coefficient
J = T**4
lam = S.Symbol('lambda')
expected_one = (lam-1)**12 * (lam-p**2)**8
expected_step = (lam-1)**3*(lam+1)**3*(lam**2+1)**3*(lam**2-p)**2*(lam**2+p)**2
assert S.expand(T.charpoly(lam).as_expr()-expected_step) == 0
print('FOURIER_CHARACTERISTIC_PASS')
assert S.expand(J.charpoly(lam).as_expr()-expected_one) == 0
print('RETURN_SPECTRUM_PASS')
assert S.simplify((J-S.eye(20))*(J-p**2*S.eye(20))) == S.zeros(20)
print('SEMISIMPLICITY_IDENTITY_PASS')
assert S.simplify(S.trace(J) - (12+8*p**2)) == 0
assert (J.subs(p,2)-S.eye(20)).rank() == 8
print('MULTIPLICITIES_AND_ORIGINAL_PARAMETER_PASS')
assert (J.subs(p,S.Rational(1,2))-S.Rational(1,4)*S.eye(20)).rank() == 12
print('ATTRACTING_PARAMETER_PASS')
