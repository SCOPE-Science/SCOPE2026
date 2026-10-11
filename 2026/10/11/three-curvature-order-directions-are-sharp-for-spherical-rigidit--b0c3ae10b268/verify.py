import sympy as sp

I = sp.eye(3)
e1 = sp.Matrix([1,0,0])
e2 = sp.Matrix([sp.Rational(3,5), sp.Rational(4,5), 0])
s2 = sp.sqrt(2)
e3 = sp.Matrix([0,1/s2,1/s2])

def R(e):
    return sp.simplify(I - 2*e*e.T)

for e in (e1,e2,e3):
    assert sp.simplify((e.T*e)[0]-1) == 0
    Q = R(e)
    assert sp.simplify(Q.T*Q-I) == sp.zeros(3)
    assert sp.simplify(Q*Q-I) == sp.zeros(3)

R1,R2,R3 = R(e1),R(e2),R(e3)
P = sp.simplify(R2*R1)
target = sp.Matrix([
    [sp.Rational(-7,25), sp.Rational(-24,25), 0],
    [sp.Rational(24,25), sp.Rational(-7,25), 0],
    [0,0,1],
])
assert P == target
assert sp.simplify(P.T*P-I) == sp.zeros(3)
assert sp.det(P) == 1

z = sp.Matrix([0,0,1])
yneg = sp.Matrix([0,-1,0])
assert sp.simplify(R3*z-yneg) == sp.zeros(3,1)

# Half-angle data: cos(theta)=3/5, so cos(2theta)=-7/25 and sin(2theta)=24/25.
c = sp.Rational(3,5)
s = sp.Rational(4,5)
assert 2*c*c-1 == sp.Rational(-7,25)
assert 2*s*c == sp.Rational(24,25)

# The irrationality proof uses that 2*cos(theta)=6/5 is rational but not an integer.
assert sp.Rational(6,5).q != 1

print('VERIFY_OK')
print('reflection_product_exact=true')
print('dense_rotation_half_angle_data=true')
print('third_reflection_axis_map=true')
