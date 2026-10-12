#!/usr/bin/env python3
import sympy as sp
A,mu,mu1,mu2,gamma,delta,m = sp.symbols("A mu mu1 mu2 gamma delta m", positive=True)
bstar,fp = sp.symbols("bstar fp", positive=True)
aH=m+mu+mu2
h=sp.simplify(delta/aH)
r=sp.simplify((gamma+m*h)/mu)
d=sp.simplify((mu1+mu2*h)/mu)
K=sp.simplify(bstar*(1+h+r)+d*fp)
lam=sp.symbols("lam")
J=sp.Matrix([[-mu,-mu1,-mu2,0],[0,0,0,0],[0,delta,-aH,0],[0,gamma,m,-mu]])
char=sp.factor(J.charpoly(lam).as_expr())
assert sp.simplify(char-lam*(lam+mu)**2*(lam+aH))==0
qH,qR,qz,u=sp.symbols("qH qR qz u")
assert sp.simplify((delta-aH*qH)-u*qH-(delta-(aH+u)*qH))==0
assert sp.simplify((gamma+m*qH-mu*qR)-u*qR-(gamma+m*qH-(mu+u)*qR))==0
assert sp.simplify((mu1+mu2*qH-mu*qz)-u*qz-(mu1+mu2*qH-(mu+u)*qz))==0

from scipy.integrate import solve_ivp
mu_v=1.0; mu1_v=0.2; mu2_v=0.3; gamma_v=0.4; delta_v=0.5; m_v=0.7
Ns=10.0; Av=mu_v*Ns; bv=0.08
cv=gamma_v+delta_v+mu_v+mu1_v
Bv=cv*(1+bv*Ns)/Ns
def beta(N): return Bv/(1+bv*N)
def rhs(t,y):
    N,I,H,R=y
    S=N-I-H-R
    return [Av-mu_v*N-mu1_v*I-mu2_v*H,
            beta(N)*S*I-cv*I,
            delta_v*I-(m_v+mu_v+mu2_v)*H,
            gamma_v*I+m_v*H-mu_v*R]
aHv=m_v+mu_v+mu2_v
hv=delta_v/aHv
rv=(gamma_v+m_v*hv)/mu_v
dv=(mu1_v+mu2_v*hv)/mu_v
bst=beta(Ns)
fpv=Bv/(1+bv*Ns)**2
Kv=bst*(1+hv+rv)+dv*fpv
sol=solve_ivp(rhs,(0,2e5),[9.5,0.05,0.01,0.01],rtol=2e-10,atol=1e-12,max_step=50.0)
N,I,H,R=sol.y[:,-1]; t=sol.t[-1]
vals=[t*I,t*H,t*R,t*(Ns-N)]
targets=[1/Kv,hv/Kv,rv/Kv,dv/Kv]
for got,target in zip(vals,targets):
    assert abs(got-target)/max(1.0,abs(target))<0.015
print("VERIFY_OK")
print("characteristic",char)
print("K_numeric",Kv)
print("scaled_state",vals)
print("target_state",targets)
