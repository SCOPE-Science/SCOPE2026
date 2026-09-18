import sympy as sp

p = sp.Rational(7, 10)
c = sp.sqrt(p)
s = sp.sqrt(1-p)
U3 = sp.Matrix([
    [c/sp.sqrt(2), -1/sp.sqrt(2), s/sp.sqrt(2)],
    [c/sp.sqrt(2),  1/sp.sqrt(2), s/sp.sqrt(2)],
    [-s,             0,             c],
])
Sigma3 = sp.diag(10, 2, 1)
I3 = sp.eye(3)
assert sp.simplify(U3*U3.T - I3) == sp.zeros(3)

B3 = sp.simplify(U3*Sigma3*U3.T)
f3 = sp.simplify(sum(
    B3[i,j]**2/(B3[i,i]*B3[j,j])
    for i in range(3) for j in range(3)
))
rhs3 = sp.Rational(9)*sp.Rational(105, 169)
gap3 = sp.factor(f3-rhs3)
assert gap3 > 0

r = sp.symbols('r', integer=True, nonnegative=True)
n = r + 3
t = sp.Rational(105, 13)
S1 = 13 + r*t
S2 = 105 + r*t**2
rhsn = sp.factor(n**2*S2/S1**2)
fn = f3 + r
gapn = sp.factor(fn-rhsn)
assert sp.simplify(rhsn - 105*(r+3)**2/(169+105*r)) == 0
assert sp.simplify(gapn - 4*(10386273*r+475532)/(320013*(105*r+169))) == 0

f4 = sp.factor(f3+1)
rhs4 = sp.factor(rhsn.subs(r,1))
gap4 = sp.factor(gapn.subs(r,1))
assert gap4 > 0

# Algebra behind the exact n=2 upper bound.
a, b = sp.symbols('a b', positive=True)
rho2 = (a-b)**2/(a+b)**2
bound2 = sp.factor(2 + 2*rho2)
target2 = sp.factor(4*(a*a+b*b)/(a+b)**2)
assert sp.simplify(bound2-target2) == 0

print('U3*U3^T =')
print(U3*U3.T)
print('B3 = U3*diag(10,2,1)*U3^T =')
print(B3)
print('f3 =', f3)
print('conjectured_rhs_3 =', rhs3)
print('gap3 =', gap3)
print('all_n_rhs =', rhsn)
print('all_n_gap =', gapn)
print('f4 =', f4)
print('hadamard_value_4 =', rhs4)
print('gap4 =', gap4)
print('n2_bound_identity =', target2)
