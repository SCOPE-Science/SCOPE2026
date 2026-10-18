"""Exact checks for a two-mode projected RK4 oscillator classification."""
import sympy as sp
import numpy as np

x,h,w1,w2=sp.symbols('x h w1 w2',positive=True,real=True)
R=lambda z:1+z+z**2/2+z**3/6+z**4/24
Q=lambda x:1+x**6*(x**2-8)/576
assert sp.simplify(sp.expand(R(sp.I*x)*R(-sp.I*x))-Q(x))==0
H2=8*(w2**6-w1**6)/(w2**8-w1**8)
assert sp.simplify(Q(w2*sp.sqrt(H2))-Q(w1*sp.sqrt(H2)))==0
assert sp.simplify((Q(w2*h)-Q(w1*h))/h**6-(w2**8-w1**8)*(h**2-H2)/576)==0
# Prove positivity algebraically via sum-of-squares decomposition.
assert sp.factor(Q(x)-((x**4/24-x**2/2+1)**2+(x-x**3/6)**2))==0
# Critical example with distinct oscillators.
H2ex=sp.simplify(H2.subs({w1:1,w2:2}))
assert H2ex==sp.Rational(168,85)
assert sp.factor(Q(sp.sqrt(H2ex))-Q(2*sp.sqrt(H2ex)))==0
assert Q(sp.sqrt(H2ex))==sp.Rational(47985841,52200625)
J=np.array([[0.,-1.],[1.,0.]])
A=np.zeros((4,4)); A[:2,:2]=J;A[2:,2:]=2*J

def rk4_stage(u, h):
    k1=A@u; k2=A@(u+h*k1/2)
    k3=A@(u+h*k2/2);k4=A@(u+h*k3)
    y=u+h*(k1+2*k2+2*k3+k4)/6
    return y,np.stack((k1,k2,k3,k4),axis=1)

def projected(u, h):
    if np.linalg.norm(u)==0:return u
    pred,stage=rk4_stage(u,h)
    return pred*np.linalg.norm(u)/np.linalg.norm(pred)

# Verify direct RK4 stages, rank and radial QO projection, amplitude-ratio dynamics.
rng=np.random.default_rng(42)
assertions=0
for hnum in [0.4,float(sp.sqrt(H2ex)),1.5,2.0,4.0]:
    u=rng.normal(size=4)
    _,stage=rk4_stage(u,hnum)
    assert np.linalg.matrix_rank(stage)==4
    for n in range(15):
        before=(np.linalg.norm(u[:2])**2,np.linalg.norm(u[2:])**2)
        uu=projected(u,hnum)
        after=(np.linalg.norm(uu[:2])**2,np.linalg.norm(uu[2:])**2)
        assert np.isclose(sum(before),sum(after),rtol=2.e-13)
        q1=float(Q(sp.Float(hnum)));q2=float(Q(sp.Float(2*hnum)))
        assert np.isclose(after[1]/after[0],before[1]/before[0]*q2/q1,rtol=1.e-11)
        u=uu;assertions+=2
# In canonical actions, angle shifts are independent of amplitudes;
# the action Jacobian is identity only at Q1=Q2.
a,b,c,d=sp.symbols('a b c d',positive=True)
S=a+b;D=c*a+d*b
T=sp.Matrix([S*c*a/D,S*d*b/D]);Y=sp.Matrix([a,b])
Jac=sp.factor(T.jacobian(Y).det())
assert sp.simplify(Jac-c*d*S**2/D**2)==0
assert sp.simplify(T[0]+T[1]-S)==0
# A point with a=b gives nonunit Jacobian when c != d, except if cd relation?
assert sp.factor(Jac.subs({a:1,b:1})-1)==-(c-d)**2/(c+d)**2
print('PASS: exact RK4 modulus, sharp crossover, nonvanishing predictor, stage span checks,')
print('      150 direct one-step energy and ratio checks, symplecticity obstruction.')
print('Example H_star^2 =',H2ex,'; common mode power =',Q(sp.sqrt(H2ex)))
print('Action Jacobian =',Jac)
print('checks:',assertions,'direct comparisons plus 9 exact identities')
# The full-stage determinant identity establishes exact span, independently of
# floating-point rank calculations.
p,q,r,s,nu,mu=sp.symbols('p q r s nu mu',real=True)
Aex=sp.diag(nu*sp.Matrix([[0,-1],[1,0]]),mu*sp.Matrix([[0,-1],[1,0]]))
vex=sp.Matrix([p,q,r,s])
t1=Aex*vex;t2=Aex*(vex+h*t1/2)
t3=Aex*(vex+h*t2/2);t4=Aex*(vex+h*t3)
Dt=sp.factor(sp.Matrix.hstack(t1,t2,t3,t4).det())
want=(h**6/32)*nu**3*mu**3*(mu**2-nu**2)**2*(p*p+q*q)*(r*r+s*s)
assert sp.simplify(Dt-want)==0
print('Exact stage determinant =',Dt)
