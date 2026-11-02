"""Reproduce exact symbolic and finite-state checks for dyadic-depth fluctuations.
Public science-only verification; requires Python 3, SymPy and NumPy.
"""
import sympy as sp
import numpy as np

p,z,n=sp.symbols('p z n',positive=True)
q=1-p
d=2*p-1
pi=sp.factor(d/((2-z)*(p-q*z)))
assert sp.simplify(pi.subs(z,1)-1)==0
pi0=sp.simplify(pi.subs(z,0))
assert sp.simplify(pi0-d/(2*p))==0
# The transition pgf at depth zero is q*z+p/(2-z), and from k>=1 it is p*z^(k-1)+q*z^(k+1).
assert sp.simplify(pi- (p*(pi-pi0)/z+q*z*pi+p*pi0/(2-z)))==0
M={0:sp.Integer(1)}
f=pi
for k in range(1,4):
    f=sp.factor(z*sp.diff(f,z))
    M[k]=sp.factor(f.subs(z,1))
mu=sp.factor(p/d)
assert sp.simplify(M[1]-mu)==0
h=n*(n-1)/(2*d)
assert sp.simplify(h-(p*h.subs(n,n-1)+q*h.subs(n,n+1))-(n-mu))==0
# At zero, the geometric reinjection J has E[J(J-1)]=2 and contraction goes to depth 1.
assert sp.simplify(-p*(2/(2*d))+mu)==0
Eh=sp.factor((M[2]-M[1])/(2*d))
Enh=sp.factor((M[3]-M[2])/(2*d))
Egh=sp.factor(Enh-mu*Eh)
var=sp.factor(M[2]-mu**2)
sigma=sp.factor(2*Egh-var)
claimed=(2+5*d**2+24*d**3-7*d**4)/(4*d**4)
assert sp.simplify(sigma-claimed)==0
assert sp.simplify(var-(1+7*d**2)/(4*d**2))==0
assert sp.limit(d**4*sigma,p,sp.Rational(1,2),dir='+')==sp.Rational(1,2)
assert sp.limit(d**2*sigma/var,p,sp.Rational(1,2),dir='+')==2
assert sp.simplify(sigma.subs(p,1)-6)==0

# Independent finite-state Green--Kubo checks: tail truncated at Kmax,
# each finite lag sum computed from exact transition probabilities and stationary masses.
for pv,Kmax,lags,relative_tol in [(0.6,240,700,0.02),(0.75,120,220,0.005),(0.95,90,110,0.005),(1.,90,90,0.005)]:
    qv=1-pv;dv=2*pv-1
    depths=np.arange(Kmax+1)
    # pi coefficients are convolution of Geom(1/2) and Geom(d/p).
    w=np.zeros(Kmax+1)
    for j in range(Kmax+1):
        w[j]=sum((.5**(k+1))*(dv/pv)*(qv/pv)**(j-k) for k in range(j+1))
    w=w/w.sum()
    g=depths - np.dot(w,depths)
    transition=np.zeros((Kmax+1,Kmax+1))
    transition[0,:]=pv*(.5**(depths+1))
    transition[0,1]+=qv
    for j in range(1,Kmax):
        transition[j,j-1]=pv
        transition[j,j+1]=qv
    transition[Kmax,Kmax-1]=1
    # Near truncation numerical tail negligible at tested sizes.
    transition[0,0]+=1-transition[0,:].sum()
    C0=np.dot(w,g*g)
    u=g.copy(); cum=C0
    for i in range(1,lags+1):
        u=transition@u
        cum+=2*np.dot(w*g,u)
    val=float(sigma.subs(p,sp.Rational(str(pv))))
    assert abs(cum-val)/val<relative_tol,(pv,cum,val)
    print(f'p={pv}: summed covariances={cum:.10g}, exact={val:.10g}')
print('PASS: exact stationary PGF, Poisson equation, cubic moments, CLT variance, critical exponents, and finite-lag covariance checks')
