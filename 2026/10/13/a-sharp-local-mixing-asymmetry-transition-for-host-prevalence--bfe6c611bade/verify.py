import sympy as sp

V,q,d=sp.symbols("V q d")
A,B=sp.symbols("A B")
a1=sp.Rational(1,2)+d
a2=sp.Rational(1,2)-d
s=(V-1)/(2*(V+1))
I1=s+A*d+B*d**2
I2=s-A*d+B*d**2

def local(I,a):
    return V/(2*a)*(a-I)/(a+I)*I-I

E1=local(I1,a1)+q*(-a2*I1+a1*I2)
E2=local(I2,a2)+q*(a2*I1-a1*I2)
D=V**2+2*V*q-1
N=V**3+2*V**2*q-V**2-4*V*q-V-2*q+1
A0=(V-1)*(V**2+2*V*q-2*V-1)/((V+1)*D)
B0=-4*V**2*N/((V+1)**2*D**2)

# The ansatz solves both equilibrium equations through second order.
for E in (E1,E2):
    z1=sp.factor(sp.cancel(sp.diff(E,d).subs(d,0).subs(A,A0)))
    z2=sp.factor(sp.cancel(sp.diff(E,d,2).subs(d,0).subs({A:A0,B:B0})))
    assert z1==0 and z2==0

# Exact curvature identities.
P=I1+I2
host2=sp.factor(sp.cancel(sp.diff(P,d,2).subs(d,0).subs(B,B0)))
assert sp.factor(sp.cancel(host2 + 16*V**2*N/((V+1)**2*D**2)))==0
Pv=sp.Rational(1,2)*(I1/(a1+I1)+I2/(a2+I2))
vec2=sp.factor(sp.cancel(sp.diff(Pv,d,2).subs(d,0).subs({A:A0,B:B0})))
assert sp.factor(sp.cancel(vec2-16*V*q/D**2))==0

# Transition factorization and monotonicity polynomial.
y=sp.symbols("y", positive=True)
assert sp.expand(N.subs(V,y+1)-(y**3+2*(1+q)*y**2-4*q))==0
assert sp.expand(sp.diff(y**3+2*(1+q)*y**2-4*q,y)-(3*y**2+4*(1+q)*y))==0

# Balanced Jacobian eigenvalues.
I,a=sp.symbols("I a")
f=local(I,a)
fp=sp.factor(sp.diff(f,I).subs({I:s,a:sp.Rational(1,2)}))
assert sp.factor(fp+(V-1)*(V+1)/(2*V))==0

print("VERIFY_OK")
