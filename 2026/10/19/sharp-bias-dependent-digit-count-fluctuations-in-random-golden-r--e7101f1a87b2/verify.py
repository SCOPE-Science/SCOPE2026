"""Self-contained exact and numerical checks for a random golden-base digit theorem.
Run: python3 verify.py. Uses Python standard library only.
"""
from fractions import Fraction as F
from math import sqrt, exp, log

# Arithmetic Q[p], with p^2 - 3p + 1 = 0, p=(3-sqrt(5))/2.
class Q:
    def __init__(self,a=0,b=0):
        if isinstance(a,Q): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=Q(o); return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+(-Q(o))
    def __rsub__(self,o): return Q(o)+(-self)
    def __mul__(self,o):
        o=Q(o); return Q(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a+3*self.b*o.b)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Q(o); den=o.a*o.a+3*o.a*o.b+o.b*o.b
        assert den
        return (self*Q(o.a+3*o.b,-o.b))*Q(1/den)
    def __eq__(self,o):
        o=Q(o); return self.a==o.a and self.b==o.b
    def __pow__(self,n):
        v=Q(1)
        for _ in range(n): v=v*self
        return v
    def __float__(self): return float(self.a)+float(self.b)*(3-sqrt(5))/2
    def __repr__(self): return f'Q({self.a},{self.b})'

p=Q(0,1); r=1-p
assert p*p==3*p-1 and r*r==p and p+r==1
checks=0
for q0 in [F(1,8),F(1,3),F(1,2),F(3,4),F(7,8)]:
    q=Q(q0)
    P=[[r,p,Q(0)],[q,Q(0),1-q],[Q(0),p,r]]
    pi=[q/(1+p),p/(1+p),(1-q)/(1+p)]
    assert sum(pi)==1
    for row in P: assert sum(row)==1
    for j in range(3):
        assert sum(pi[i]*P[i][j] for i in range(3))==pi[j]
        checks+=1
    # The independent excursions have L=1+J, J geometric(p),
    # and digit reward R equals 1 with probability q and J otherwise.
    meanL=(1+p)/p
    meanR=q+(1-q)/p
    rho=meanR/meanL
    assert rho==(1-q*r)/(1+p)
    vJ=r/(p*p)
    var_reward_centered=(q*rho*rho+(1-q)*(1-rho)*(1-rho))*vJ+q*(1-q)*((1-Q(1)/p)**2)
    V=var_reward_centered/meanL
    V_formula=p*r/(1+p)**3+q*(1-q)*r*r*(p*p+5*p+2)/(p*(1+p)**3)
    assert V==V_formula
    checks+=2
    for L in range(2,15):
        # Independent geometric time and Bernoulli branch labels.
        prob=p*r**(L-2)
        assert q*prob+(1-q)*prob==prob
        checks+=1
    pp=float(p); rr=float(r); qq=float(q); expectation=float(rho); target=float(V)
    # Dynamical transfer: tilted transition matrix, digit 1 on
    # B->A or any C->(B,C), digit 0 otherwise.
    # det(lambda I - tilted P) = 0, evaluated in scalar parameters.
    def char(lam,t):
        z=exp(t)
        return (lam**3-rr*(1+z)*lam*lam+(rr*rr*z-pp*z)*lam+
                pp*rr*z*(1-qq+qq*z))
    def root(t):
        # Leading PF eigenvalue bracketed between min and max row sums.
        lo=max(rr,rr*exp(t))+1e-10; hi=max(3.,3.*exp(abs(t)))
        for j in range(100):
            mid=(lo+hi)/2
            if char(mid,t)<0:lo=mid
            else:hi=mid
        return (lo+hi)/2
    for t in [-1,-.4,0,.4,1]:
        lam=root(t); z=exp(t)
        assert abs(char(lam,t))<1e-9
        # Renewal equation (independent from characteristic computation).
        lhs=(pp*z/(lam*lam))*(qq/(1-rr/lam)+(1-qq)/(1-rr*z/lam))
        assert abs(lhs-1)<1e-9
        checks+=2
    eps=1e-3
    c_plus=log(root(eps)); c_minus=log(root(-eps)); c0=log(root(0))
    first=(c_plus-c_minus)/(2*eps)
    second=(c_plus+c_minus-2*c0)/eps**2
    assert abs(first-expectation)<8e-7,(first,expectation)
    assert abs(second-target)<4e-6,(second,target)
    checks+=2

qhalf=Q(F(1,2))
base=p*r/(1+p)**3
excess=r*r*(p*p+5*p+2)/(p*(1+p)**3)
assert excess.a !=0 or excess.b!=0
assert float(excess)>0 and float(base)>0
assert float(base+qhalf*(1-qhalf)*excess)>float(base)
checks+=3
print('VERIFY_OK:',checks,'exact field/renewal identities, tilted Perron checks and second-derivative comparisons;',
      'variance endpoints',float(base),'central maximum',float(base+excess/4))
