#!/usr/bin/env python3
"""Reproducible rational one-step identities and numerical asymptotic spot checks."""
from fractions import Fraction as Q

K=Q(1); alpha=Q(1); gamma=Q(1); mu=Q(1)
k=alpha+gamma+mu; beta=k/K; h=Q(1,4)
S=Q(7,10); I=Q(1,5); R=Q(1,10)
assert 0<S and 0<I and 0<R and S+I+R<=K and k==beta*K

def step(s,i,r):
    tau=h/(1+h*(k+beta*i))
    return (s+tau*(-beta*s*i+mu*(K-s)),
            i+tau*(beta*s-k)*i,
            r+tau*(alpha*i-mu*r))

for j in range(8):
    sn,inn,rn=step(S,I,R)
    tau=h/(1+h*(k+beta*I))
    x=K-S
    assert sn>0 and inn>0 and rn>0 and sn+inn+rn<=K
    assert inn==I*(1-beta*tau*x)
    assert K-sn==(1-mu*tau)*x+beta*tau*S*I
    assert Q(1)/inn-Q(1)/I == beta*tau*(x/I)/(1-beta*tau*x)
    S,I,R=sn,inn,rn

# Floating-point long-horizon corroboration is not the infinite-time proof.
s,i,r=.7,.2,.1
nmax=1000000
for n in range(1,nmax+1):
    tau=.25/(1+.25*(3+3*i))
    sn=s+tau*(-3*s*i+1-s)
    inn=i+tau*(3*s-3)*i
    rn=r+tau*(i-r)
    s,i,r=sn,inn,rn
assert abs(nmax*i-7/9)<0.0002
assert abs(nmax*.25*i-7/36)<0.00005
assert abs((1-s)/i-3)<0.0001
print("VERIFY_OK")
