"""Reproduce the exact matrix identities and positivity threshold.
Run: python verify.py (requires SymPy >= 1.10)."""
import sympy as s

q, r, p, u = s.symbols('q r p u', real=True)
R = s.Rational
I2 = s.eye(2)

def two_exp(x, weight):
    return s.Matrix([[1-weight*(1-x), weight*(1-x)],
                     [(1-weight)*(1-x), weight+(1-weight)*x]])

def three_A(x):
    return s.Matrix([[x, 1-x, 0],[0, 1, 0],[0, 0, 1]])

def three_B(x):
    return s.Matrix([[1, 0, 0],[0, x, 1-x],[0, 0, 1]])

# q=e^(-total_rate_A*h/4), r=e^(-total_rate_B*h/4).
X = two_exp(q**2,p)*two_exp(r**4,u)*two_exp(q**2,p)
W = two_exp(q,p)*two_exp(r**2,u)*two_exp(q,p)
Y = W**2
M = (4*Y-X)/3
coef_A = (1-q)*(q**2*r**4*(3*q-1)+4*q*r**2*(q+1)+3-q)/3
coef_B = q*(1-r**2)*(4*q**2*r**2-q*r**2-q+4)/3
assert s.simplify(M[0,1]-p*coef_A-u*coef_B)==0
assert s.simplify(M[1,0]-(1-p)*coef_A-(1-u)*coef_B)==0
assert s.simplify(s.det(X)-q**4*r**4)==0
assert s.simplify(s.det(Y)-q**4*r**4)==0
assert s.simplify(s.det(M)-q**4*r**4)==0
for integer in range(1,8):
    delayed = (4*Y**integer-X**integer)/3
    assert all(s.simplify(v)==0 for v in delayed-M**integer)

# q=e^(-lambda*h/4), equal rates on the three-state pure birth split.
Xs=three_A(q**2)*three_B(q**4)*three_A(q**2)
Ys=(three_A(q)*three_B(q**2)*three_A(q))**2
Ms=(4*Ys-Xs)/3
E01=q**2*(1-q**2)*(8*q-q**2-1)/3
E02=(1-q)**2*(1+q)*(-q**3+7*q**2+3*q+3)/3
assert s.simplify(Ms[0,1]-E01)==0
assert s.simplify(Ms[0,2]-E02)==0
assert all(s.simplify(v)==0 for v in Ms*s.ones(3,1)-s.ones(3,1))
assert s.simplify(Ms[0,0]-q**4)==0
assert s.simplify(Ms[1,1]-q**4)==0
assert s.simplify(Ms[1,2]-(1-q**4))==0
for integer in range(1,9):
    delayed=(4*Ys**integer-Xs**integer)/3
    assert s.simplify(delayed[0,1]-integer*q**(4*(integer-1))*E01)==0
    assert s.simplify(delayed[0,0]-q**(4*integer))==0
    assert s.simplify(delayed[1,1]-q**(4*integer))==0
    assert s.simplify(delayed[0,2]-(1-q**(4*integer)-integer*q**(4*(integer-1))*E01))==0
    assert all(s.simplify(v)==0 for v in delayed*s.ones(3,1)-s.ones(3,1))

qstar=4-s.sqrt(15)
assert s.simplify(qstar**2-8*qstar+1)==0
assert 0 < qstar.evalf() < 1
for qvalue in [s.Rational(1,10),s.Rational(1,5),s.Rational(1,2),s.Rational(9,10)]:
    for integer in [1,2,5,12]:
        numerator=(integer*q**(4*(integer-1))*E01).subs(q,qvalue)
        should_positive=qvalue>=qstar
        assert bool(numerator>0)==should_positive
print('VERIFY_OK 2-state exact delayed-power identity through p=7; 3-state identities through p=8; threshold signs')
