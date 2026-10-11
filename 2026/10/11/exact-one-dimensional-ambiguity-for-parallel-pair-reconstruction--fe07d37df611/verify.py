import sympy as sp
X,Y=sp.symbols("X Y")
a,b,c,r,s,t,alpha,beta=sp.symbols("a b c r s t alpha beta")
F=(Y-alpha)*(Y-beta)
H=a*X**2+b*X*Y+c*Y**2+r*X+s*Y+t
J=sp.expand(sp.diff(F,X)*sp.diff(H,Y)-sp.diff(F,Y)*sp.diff(H,X))
expected=-(2*Y-alpha-beta)*(2*a*X+b*Y+r)
assert sp.expand(J-expected)==0

# Kernel coefficient conditions over the generic coefficient ring.
poly=sp.Poly(sp.expand(J),X,Y)
coeffs=poly.coeffs()
# Substituting a=b=r=0 annihilates J.
assert sp.expand(J.subs({a:0,b:0,r:0}))==0
# Any cY^2+sY+t decomposes in span{1,F,Y}.
A=sp.expand(t-c*alpha*beta)
B=c
C=sp.expand(s+c*(alpha+beta))
assert sp.expand((c*Y**2+s*Y+t)-(A+B*F+C*Y))==0

# Example 7.6.
F0=Y**2-1
Gp=X**2-1
Gt=4*X**2-Y**2+6*Y-9
def jac(P,Q):
    return sp.expand(sp.diff(P,X)*sp.diff(Q,Y)-sp.diff(P,Y)*sp.diff(Q,X))
assert jac(F0,Gp)==-4*X*Y
assert jac(F0,Gt)==-16*X*Y
D=sp.expand(Gt/sp.Integer(4)-Gp)
assert sp.expand(D-(-sp.Rational(3,2)-sp.Rational(1,4)*F0+sp.Rational(3,2)*Y))==0
print("VERIFY_OK")
print("parallel_kernel_basis=1,F,Y")
print("example_defect=3/2")
