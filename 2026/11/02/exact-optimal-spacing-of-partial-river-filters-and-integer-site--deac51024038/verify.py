#!/usr/bin/env python3
"""Exact arithmetic tests for uniform-source river purification spacing."""
from fractions import Fraction as F
from itertools import combinations
from math import prod

checks=0

def add(condition, message):
    global checks
    assert condition, message
    checks+=1

# Continuous identity and sharp optimum for rational efficiency, length, filter count.
def integrated(L, eta, ts):
    rho=1-eta
    c=F(0); prev=F(0); exposure=F(0)
    for t in list(ts)+[L]:
        h=t-prev
        exposure+=c*h+h*h/2
        c+=h
        prev=t
        if t!=L:
            c*=rho
    return exposure,c

for L in [F(1),F(2),F(7,3)]:
 for k in range(1,18):
  for eta in [F(1),F(1,2),F(1,7),F(2,3),F(9,10)]:
   D=2+(k-1)*eta
   ts=[L*(1+j*eta)/D for j in range(k)]
   E,v=integrated(L,eta,ts)
   add(E==L*L*(2-eta)/(2*D),('continuous minimum',L,k,eta))
   add(v==L*(2-eta)/D,('outflow',L,k,eta))
   u=[L/D]*k
   add(v+eta*sum(u)==L,('mass',L,k,eta))
   add(2*E==v*v+eta*(2-eta)*sum(t*t for t in u),('energy',L,k,eta))

# Distinct integer-site point treatments, evaluated from first principles.
def discharge_exposure(n,eta,a,b):
    c=F(0); total=F(0)
    for i in range(1,n+1):
        c+=1
        if i in (a,b):
            c*=1-eta
        total+=c
    return total

def score(n,eta,a,b):
    N=n+1
    s=a+b;d=b-a
    return (2-eta)*(s-N)**2+(2+eta)*(d-eta*N/(2+eta))**2

for n in range(2,14):
 N=n+1
 effs={F(1),F(1,2),F(1,3),F(2,3),F(1,7),F(6,7),F(99,100),F(1,100)}
 for d in range(1,n-1):
    if (d-N)%2==0:
      t=F(2*(d+1),N-d)
    else:
      t=F(2*d,N-d-1)
    if F(0)<t<=F(1):
      effs.update([t])
      if t>F(1,10000):effs.add(t-F(1,10000))
      if t<F(9999,10000):effs.add(t+F(1,10000))
 for eta in effs:
    if not (F(0)<eta<=F(1)):continue
    vals={(a,b):discharge_exposure(n,eta,a,b) for a,b in combinations(range(1,n+1),2)}
    best=min(vals.values()); opts={p for p,v in vals.items() if v==best}
    # Continuous completion must order the complete discrete objective.
    ss={(a,b):score(n,eta,a,b) for a,b in vals}
    add(opts=={p for p,s in ss.items() if s==min(ss.values())},('square-equivalence',n,eta))
    for (a,b),E in vals.items():
        N=n+1
        saved=n*N/F(2)-E
        predicted=eta*(a*(N-a)+b*(N-b)-eta*a*(N-b))
        add(saved==predicted,('discrete identity',n,eta,a,b))
    tau=[]
    for d in range(1,n-1):
        val=F(2*(d+1),N-d) if (d-N)%2==0 else F(2*d,N-d-1)
        tau.append(val)
    add(all(tau[i]<tau[i+1] for i in range(len(tau)-1)),('ordered threshold',n))
    predicted_d={1+sum(t<eta for t in tau)}
    predicted_d.update(d+1 for d,t in enumerate(tau,1) if t==eta)
    add(predicted_d=={b-a for a,b in opts},('staircase',n,eta,predicted_d,opts))
    for a,b in opts:
        d=b-a;s=a+b
        add(abs(s-N)==((d-N)&1),('centering',n,eta,a,b))
print('PASS',checks,'exact-rational assertions')
