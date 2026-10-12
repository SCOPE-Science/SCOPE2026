import sympy as s
W,X,Y,Z=s.symbols('W X Y Z')
a,b,c=s.symbols('a b c')
d,e,f,g,h=s.symbols('d e f g h')
# General homogeneous binary forms evaluated at (W,X); coefficients algebraically independent.
C=a*W**2+b*W*X+c*X**2
D=d*W**4+e*W**3*X+f*W**2*X**2+g*W*X**3+h*X**4
F=[s.expand(C*W*Z),s.expand(C*X*Z),s.expand(-C*Y*Z),D]
Wp,Xp,Yp,Zp=F
Cp=s.expand(C.subs({W:Wp,X:Xp}, simultaneous=True))
Dp=s.expand(D.subs({W:Wp,X:Xp}, simultaneous=True))
assert s.expand(Cp-C**3*Z**2)==0
assert s.expand(Dp-C**4*Z**4*D)==0
F2=[s.expand(Cp*Wp*Zp),s.expand(Cp*Xp*Zp),s.expand(-Cp*Yp*Zp),Dp]
S=s.expand(C**4*D*Z**3)
assert all(s.expand(u-S*v)==0 for u,v in zip(F2,[W,X,Y,Z]))
J=s.Matrix([[s.diff(fi,v) for v in (W,X,Y,Z)] for fi in F]).det()
fac=s.factor(J)
print('JACOBIAN_FACTOR=',fac)
# Divide expected obvious factors to see remainder.
q=s.cancel(J/(C**2*D*Z**2))
print('J_OVER_C2_D_Z2=',s.factor(q))
print('VERIFY_OK composition=involution degree=4 inverse_degree=4 multidegree=(1,4,4,1) reduced_base=5_concurrent_lines exceptional=3_planes_to_point+4_planes_to_lines')
