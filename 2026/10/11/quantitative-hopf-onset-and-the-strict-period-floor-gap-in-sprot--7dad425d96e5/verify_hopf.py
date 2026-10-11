"""Symbolic verification of the Sprott Q Hopf theorem.

Requires SymPy. No finite computation is used as an infinite-dynamics proof.
"""
import sympy as s

w,b=s.symbols('w b',positive=True,real=True)
L=s.symbols('L')
a=w**2
I=s.I
A=s.Matrix([[0,0,-1],[1,-1,0],[a,0,0]])
A_b=s.Matrix([[0,0,-1],[1,-1,0],[a,0,b]])
q=s.Matrix([1+I*w,1,a-I*w])
ell=s.Matrix([[1/(2*(1+I*w)),0,I/(2*w*(1+I*w))]])
B=lambda u,v:s.Matrix([0,0,2*u[1]*v[1]])
qs=s.conjugate(q)
assert s.simplify(A*q-I*w*q)==s.zeros(3,1)
assert s.simplify(ell*A-I*w*ell)==s.zeros(1,3)
assert s.simplify((ell*q)[0]-1)==0
assert s.simplify(A_b.charpoly(L).as_expr()-(L+1)*(L**2-b*L+a))==0
h11=A.inv()*B(q,qs)
h20=(2*I*w*s.eye(3)-A).inv()*B(q,q)
assert s.simplify(h11-s.Matrix([2/a,2/a,0]))==s.zeros(3,1)
assert s.simplify(h20[1]-2/(3*a*(1+2*I*w)))==0
G=(ell*(B(qs,h20)-2*B(q,h11)))[0]
ReG=s.factor(s.re(s.expand_complex(G)))
expected_reg=-2*(8*a+1)/(a*(a+1)*(4*a+1))
assert s.simplify(ReG-expected_reg)==0
l1=s.factor(ReG/(2*w))
assert s.simplify(l1+(8*a+1)/(w**3*(a+1)*(4*a+1)))==0

# Independent Fourier/Lindstedt balance for the equivalent scalar jerk equation.
c0=-1/(2*a)
c2=1/(12*a*(1+2*I*w))
beta=s.factor(2*s.re(s.expand_complex((c0+c2)/(-a+I*w))))
assert s.simplify(beta-(8*a+1)/(2*a*(a+1)*(4*a+1)))==0
assert s.simplify(1/beta-2*a*(a+1)*(4*a+1)/(8*a+1))==0
delta=s.factor(-s.im(s.expand_complex((c0+c2)/(-a+I*w))))
assert s.simplify(delta+(26*a+5)/(12*w**3*(a+1)*(4*a+1)))==0
assert s.simplify(-delta*w*(1+I*w)-beta*(-a+I*w)/2+c0+c2)==0
# The Sprott-S positive-height branch has the same critical jerk equation
# at its own Hopf parameter; parameter derivatives differ away from criticality.
bS=s.symbols('bS', positive=True, real=True)
assert s.simplify(2*a*s.sqrt(bS)-a).subs(bS,s.Rational(1,4))==0
frequency_slope=s.factor(delta/beta)
assert s.simplify(frequency_slope+(26*a+5)/(6*w*(8*a+1)))==0
period_relative_slope=s.factor(-frequency_slope/w)
assert s.simplify(period_relative_slope-(26*a+5)/(6*a*(8*a+1)))==0
period_floor_gap=s.factor(period_relative_slope-1/(2*a))
assert s.simplify(period_floor_gap-(a+1)/(3*a*(8*a+1)))==0

# Both equilibrium branches follow directly for a>0.
x,y,z=s.symbols('x y z',real=True)
f=s.Matrix([-z,x-y,a*x+y**2+b*z])
assert s.simplify(f.subs({x:0,y:0,z:0}))==s.zeros(3,1)
assert s.simplify(f.subs({x:-a,y:-a,z:0}))==s.zeros(3,1)
J=f.jacobian([x,y,z]); Jsecond=J.subs({x:-a,y:-a,z:0})
assert s.simplify(Jsecond.charpoly(L).as_expr().subs(L,0)+a)==0
print('PASS: characteristic factorization, dual eigenvectors, l1, independent harmonic balance, equilibria')
print('Re G21 =',ReG)
print('l1 =',l1)
print('b/(first-harmonic y amplitude)^2 =',beta)
print('period relative slope =',period_relative_slope)
print('period comparison slope =',period_floor_gap)
