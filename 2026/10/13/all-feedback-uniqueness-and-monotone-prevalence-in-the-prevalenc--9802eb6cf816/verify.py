import sympy as sp
I,h=sp.symbols('I h', positive=True)
mu,beta,alpha,delta,gamma=sp.symbols('mu beta alpha delta gamma', positive=True)
sigma=sp.symbols('sigma', real=True)
t=sp.symbols('t', nonnegative=True)
Delta=beta*I*(mu+sigma*delta*h)+(mu+delta*h)*(mu+gamma*h)
R=alpha*I*(beta*I+mu+gamma*h)/Delta
C=alpha*I*delta*h/Delta
H=alpha*(beta*I+mu+h*(gamma+(1-sigma)*delta))/Delta
assert sp.simplify((1+0)*delta*h*R-beta*C*I-mu*C-gamma*h*C)==0
assert sp.simplify((1-sigma)*beta*C*I+alpha*I-mu*R-delta*h*R)==0
assert sp.simplify(R+(1-sigma)*C-I*H)==0
# Along h=1+epsilon I, epsilon=(h-1)/I.
Phi=I*(1+H)
dPhi=sp.diff(Phi,I)+sp.diff(Phi,h)*(h-1)/I
A0=(I**2*beta**2*(mu+delta*sigma)
    +2*I*beta*(delta*gamma+delta*mu+gamma*mu+mu**2)
    +delta**2*(gamma+mu)*(1-sigma)+delta*gamma**2
    +delta*gamma*mu*(3-sigma)+delta*mu**2*(2-sigma)
    +gamma**2*mu+2*gamma*mu**2+mu**3)
B1=(I*beta*(delta*gamma+delta*mu*(1-sigma)+gamma*mu)
    +delta**2*(gamma+mu)*(1-sigma)+delta*gamma**2
    +delta*gamma*mu*(2-sigma)+delta*mu**2*(1-sigma)
    +gamma**2*mu+gamma*mu**2)
B2=(delta**2*(gamma+mu)*(1-sigma)+delta*gamma**2
    +delta*gamma*mu*(1-sigma)+gamma**2*mu)
claimed=1+alpha*(A0+2*(h-1)*B1+(h-1)**2*B2)/Delta**2
assert sp.simplify(dPhi-claimed)==0
Q=(sigma*beta**2*I**2+2*beta*gamma*h*I+2*sigma*beta*mu*I
   +(1-sigma)*delta*gamma*h**2+gamma**2*h**2+2*gamma*mu*h+sigma*mu**2)
assert sp.simplify(sp.diff(H,h)+alpha*delta*Q/Delta**2)==0
print('VERIFY_OK')
