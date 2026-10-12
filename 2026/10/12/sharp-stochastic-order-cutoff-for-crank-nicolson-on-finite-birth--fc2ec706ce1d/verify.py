from fractions import Fraction as F
import sympy as S

def bd(birth,death):
    n=len(birth)+1
    Q=S.zeros(n)
    for i in range(n):
        if i<n-1:Q[i,i+1]=birth[i]
        if i>0:Q[i,i-1]=death[i-1]
        Q[i,i]=-sum(Q[i,j] for j in range(n) if j!=i)
    D=S.zeros(n-1,n)
    for i in range(n-1):D[i,i]=-1;D[i,i+1]=1
    H=S.zeros(n-1)
    for i in range(n-1):
        H[i,i]=-(birth[i]+death[i])
        if i<n-2:H[i,i+1]=birth[i+1]
        if i>0:H[i,i-1]=death[i-1]
    assert D*Q==H*D
    return Q,D,H

def cn(Q,h):
    n=Q.rows
    return (S.eye(n)-h*Q/2).inv()*(S.eye(n)+h*Q/2)

def edge(H,h):
    return 2*(S.eye(H.rows)-h*H/2).inv()-S.eye(H.rows)

Q1,D1,H1=bd([S.Integer(1),S.Integer(1)],[S.Integer(1),S.Integer(1)])
assert H1==S.Matrix([[-2,1],[1,-2]])
h1=S.Rational(3,2)
T1=cn(Q1,h1)
assert T1==S.Matrix([[S.Rational(31,91),S.Rational(6,13),S.Rational(18,91)],[S.Rational(6,13),S.Rational(1,13),S.Rational(6,13)],[S.Rational(18,91),S.Rational(6,13),S.Rational(31,91)]])
assert all(e>0 for e in T1)
assert T1*S.ones(3,1)==S.ones(3,1)
assert T1*S.Matrix([0,1,1])==S.Matrix([S.Rational(60,91),S.Rational(49,91),S.Rational(73,91)])
assert (D1*T1)==edge(H1,h1)*D1
assert edge(H1,h1)[0,0]<0
assert S.simplify(2/S.sqrt(3))<h1<S.Integer(2)

Q2,D2,H2=bd([S.Integer(1),S.Integer(3)],[S.Integer(3),S.Integer(1)])
assert H2==S.Matrix([[-4,3],[3,-4]])
h2=S.Rational(1,2)
T2=cn(Q2,h2)
assert T2==S.Matrix([[S.Rational(39,55),S.Rational(2,11),S.Rational(6,55)],[S.Rational(6,11),S.Rational(-1,11),S.Rational(6,11)],[S.Rational(6,55),S.Rational(2,11),S.Rational(39,55)]])
assert T2[1,1]==S.Rational(-1,11)
E2=edge(H2,h2)
assert E2==S.Matrix([[S.Rational(9,55),S.Rational(24,55)],[S.Rational(24,55),S.Rational(9,55)]])
assert all(e>=0 for e in E2)
assert (D2*T2)==E2*D2
assert S.Rational(2,5)<h2<2/S.sqrt(7)
assert T2*S.ones(3,1)==S.ones(3,1)

# General three-state threshold formula on exact rational rates.
for birth,death in [([S.Integer(1),S.Integer(1)],[S.Integer(1),S.Integer(1)]),([S.Integer(1),S.Integer(3)],[S.Integer(3),S.Integer(1)]),([S.Integer(2),S.Integer(5)],[S.Integer(1),S.Integer(4)])]:
    Q,D,H=bd(birth,death)
    a=-H[0,0];d=-H[1,1];b=H[0,1];c=H[1,0];Delta=a*d-b*c
    assert Delta>0
    hh=S.simplify(4/(abs(a-d)+S.sqrt((a+d)**2-4*b*c)))
    RR=(S.eye(2)-hh*H/2).inv()
    # One edge hits 1/2 exactly, the other no less than 1/2.
    assert any(S.simplify(RR[i,i]-S.Rational(1,2))==0 for i in range(2))
    assert all(float(S.N(RR[i,i]-S.Rational(1,2),40))>-1e-25 for i in range(2))

# Nonuniform 4-state birth-death indexing identity.
bd([S.Integer(2),S.Integer(7),S.Integer(3)],[S.Integer(5),S.Integer(1),S.Integer(4)])
print('VERIFY_OK')
