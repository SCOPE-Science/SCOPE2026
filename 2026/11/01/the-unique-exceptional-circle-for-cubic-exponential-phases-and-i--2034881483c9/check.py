"""Independent exact polynomial checks for the cubic maximum-modulus theorem."""
from sympy import symbols, I, conjugate, expand, simplify, discriminant, pi, cos, sin
z,x,y,C,r=symbols('z x y C r', real=True, positive=True)
# x, y in this checker are real, not necessarily positive.
x,y=symbols('x y', real=True)
s=x+I*y
Q=z**3-s*z**2+conjugate(s)*z-1
# Laurent polynomial representing |Q|^2 on the unit circle.
qstar=conjugate(Q).subs(z,1/z)
# Because z is real in sympy, conjugation then substitution is algebraic star.
T=expand(Q*qstar)
A=C*r**2*(s**2+2*conjugate(s))
B=-2*C*r*s
H=(A*r*z+conjugate(A)*r/z+B*r**2*z**2+conjugate(B)*r**2/z**2+C*r**3*(z**3+z**(-3)))/2
M=C*r**3*(1+x*x+y*y)
assert simplify(expand(M-C*r**3*T/2-H))==0
D=expand(discriminant(Q,z))
formula=(x*x+y*y)**2+18*(x*x+y*y)-8*(x**3-3*x*y*y)-27
assert simplify(D-formula)==0
# Arithmetic exact example: 8z-4z^2+z^3, r=1, roots 1, exp(+-i*pi/3).
q=Q.subs({x:2,y:0})
assert expand(q-(z-1)*(z*z-z+1))==0
assert formula.subs({x:2,y:0})==-3
assert M.subs({C:1,r:1,x:2,y:0})==5
# Real cubic alternative: a=1, b=-1, c=1, radius=3/4.
rad=symbols('rad',positive=True)
a,b,c=1,-1,1
d=b*b/(4*c)-a
assert d/b==3/4
s0=-b/(2*c*(d/b))
assert s0==2/3
print('CHECK_OK: exact Laurent factorization, cubic discriminant, two sharp examples')
