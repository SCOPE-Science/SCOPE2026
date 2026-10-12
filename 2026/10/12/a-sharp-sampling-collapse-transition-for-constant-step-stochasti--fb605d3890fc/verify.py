#!/usr/bin/env python3
"""Reproduce exact identities and finite-time checks for the two-component scalar resolvent sampling calculation."""
from fractions import Fraction as Q
import sympy as sp

k,p=sp.symbols('k p',positive=True,real=True)
w1=k/(1+k); w2=sp.Rational(1,2)
W=p*w1+(1-p)*w2
S=p*(2*w1-w1*w1)+(1-p)*(2*w2-w2*w2)
star=1/(k+1)
mean=(1-p)*w2/W
variance=p*(1-p)*w1**2*w2**2/(W**2*S)
risk=sp.factor(variance+(mean-star)**2)
A=(k-1)*(k+3)*(k*k+4*k+5)
B=6*(k+1)**2*(k+3)
C=-3*(k+1)**4
P=A*p*p+B*p+C
Den1=k+1+(k-1)*p
Den2=(k*k+2*k-3)*p+3*(k+1)**2
assert sp.simplify(sp.diff(risk,p)-8*k*k*P/(Den1**2*Den2**2))==0
assert sp.factor(P.subs(p,1)) == -2*k*(k+2)*(k*k-2*k-7)
assert sp.simplify(P.subs(p,(k+1)/(k+3)) + 2*(k-1)*(k+1)**2*(k*k+4*k+2)/(k+3))==0
assert sp.simplify(risk.subs(p,1) - 1/(k+1)**2)==0
assert sp.simplify(risk.subs(p,0) - k*k/(k+1)**2)==0
assert sp.simplify(risk.subs(p,(k+1)/(k+3)) - k*k/((k+1)**2*(2*k+1)))==0
assert sp.simplify(risk.subs(k,1) - (8*p*p-8*p+3)/12)==0
assert sp.limit(k*k/(2*k+1),k,sp.oo)==sp.oo
assert sp.limit((k+1)*risk.subs(p,(k+1)/(k+3))/4,k,sp.oo)==sp.Rational(1,8)
assert sp.limit((k+1)*risk.subs(p,1)/4,k,sp.oo)==0
print('Symbolic: derivative, sign polynomial, boundaries, unbiased law, asymptotic objective limits verified.')

N=0
for kv in [1,2,4,9,17]:
    for pv in [Q(0), Q(1,5), Q(1,2), Q(4,5), Q(1)]:
        a=Q(1,kv+1); b=Q(1,2); t=Q(1,kv+1)
        # Track exact path probabilities; repeated states are merged.
        dist={Q(1,3):Q(1)}
        m=Q(1,3); s=m*m
        for j in range(9):
            em=sum(x*w for x,w in dist.items()); es=sum(x*x*w for x,w in dist.items())
            assert em==m and es==s, (kv,pv,j,em,es,m,s)
            N+=2
            new={}
            for x,weight in dist.items():
                for y,prob in ((a*x,pv),(b*x+(1-b),1-pv)):
                    new[y]=new.get(y,Q(0))+weight*prob
            dist={x:v for x,v in new.items() if v}
            m=pv*a*m+(1-pv)*(b*m+(1-b))
            s=pv*(a*a*s)+(1-pv)*(b*b*s+2*b*(1-b)*em+(1-b)**2)
        lim=sp.factor(risk.subs({k:kv,p:sp.Rational(pv.numerator,pv.denominator)}))
        assert lim>=0
print(f'Finite time: {N} exact path-versus-moment identity checks passed.')

for kv in [1,2,3,4,9,40]:
    Pk=sp.Poly(P.subs(k,kv),p)
    assert Pk.eval(0)<0
    if kv < (1+2*2**.5):
        assert Pk.eval(1)>0
        roots=[z for z in sp.nroots(Pk,maxsteps=100) if abs(float(sp.im(z)))<1e-11 and 0<float(sp.re(z))<1]
        assert len(roots)==1
        pm=float(sp.re(roots[0]))
    else:
        assert Pk.eval(1)<0
        pm=1.
    optimum=float(risk.subs({k:kv,p:pm}))
    for j in range(101):
        q=j/100
        assert optimum <= float(risk.subs({k:kv,p:q}))+1e-11,(kv,q,pm)
print('Optimality: unique switching frontier and six 101-point rational-grid diagnostics passed.')
