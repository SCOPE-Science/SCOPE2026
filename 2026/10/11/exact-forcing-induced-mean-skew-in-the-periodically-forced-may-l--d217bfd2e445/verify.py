import sympy as s
X,Y,Z,A,c,e=s.symbols("X Y Z A c e", positive=True)
R=X+Y+Z
Q=c**2+c*e+e**2
L=3+c-e
E1=1-R-c*Y+e*Z+A
E2=1-R-c*Z+e*X
E3=1-R-c*X+e*Y
sol=s.solve([E1,E2,E3],[X,Y,Z],dict=True)[0]
assert s.simplify((sol[Y]-sol[X])-c*A/Q)==0
assert s.simplify((sol[X]-sol[Z])-e*A/Q)==0
assert s.simplify((sol[X]+sol[Y]+sol[Z])-(3+A)/L)==0
assert s.simplify((E2-E3)-(c*(X-Z)-e*(Y-X)))==0
assert s.simplify((E3-E1+A)-(c*(Y-X)+e*(Y-Z)))==0
# Inward signs on upper cube faces for 0<e<c<1 and nonnegative other coordinates:
# x=1: -(1+c)y + (e-1)z <= 0
# y=1: (e-1)x -(1+c)z <= 0
# z=1: (e-1)y -(1+c)x <= 0
print("Y_minus_X =", s.factor(sol[Y]-sol[X]))
print("X_minus_Z =", s.factor(sol[X]-sol[Z]))
print("sum =", s.factor(sol[X]+sol[Y]+sol[Z]))
print("VERIFY_OK")
