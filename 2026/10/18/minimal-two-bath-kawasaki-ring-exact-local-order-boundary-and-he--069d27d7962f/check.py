#!/usr/bin/env python3
"""Independently enumerate the four-spin two-reservoir Kawasaki model.

Use: python check.py
Requires Python 3.10+ and SymPy 1.12+.
All hopping attempts have rate one per bond before Metropolis acceptance.
"""
from itertools import combinations
from math import log
import sympy as S

p,q=S.symbols('p q',positive=True)
spins=[tuple(1 if j in A else -1 for j in range(4)) for A in combinations(range(4),2)]
where={x:i for i,x in enumerate(spins)}
D=p*(1+q)+3*q+q*q

def energy(s):
    return -sum(s[j]*s[(j+1)%4] for j in range(4))

def matrix():
    M=S.zeros(6,6)
    for i,s in enumerate(spins):
        for edge in range(4):
            b=(edge+1)%4
            if s[edge]==s[b]:
                continue
            t=list(s);t[edge],t[b]=t[b],t[edge]; t=tuple(t)
            delta=energy(t)-energy(s)
            assert delta in {-4,4}
            base=p if edge==0 else q
            rate=base if delta>0 else S.Integer(1)
            k=where[t]
            M[i,k]+=rate
            M[i,i]-=rate
    return M
Q=matrix()
a=(p+q)/(2*D)
b=q*(p+q)/(2*D)
c=q/D
pi=S.Matrix([[a,b,c,c,b,a]])
assert S.simplify(sum(pi)-1)==0
assert all(S.simplify(z)==0 for z in (pi*Q))

corr_hot=(p*(1-q)-q*(1+q))/D
corr_cold=(q*(1-q)-p*(1+q))/D
current=4*q*(p-q)/D  # heat absorbed from hot bath in units of J per unit time
for edge,expected in [(0,corr_hot),(1,corr_cold),(2,corr_hot),(3,corr_cold)]:
    got=sum(pi[0,i]*spins[i][edge]*spins[i][(edge+1)%4] for i in range(6))
    assert S.simplify(got-expected)==0

flow=0
for i,s in enumerate(spins):
    if s[0]==s[1]:
        continue
    t=list(s);t[0],t[1]=t[1],t[0];t=tuple(t)
    delta=energy(t)-energy(s)
    rate=p if delta>0 else S.Integer(1)
    flow+=pi[0,i]*rate*delta
assert S.simplify(flow-current)==0

assert S.simplify(S.diff(corr_hot,p)-4*q/D**2)==0
assert S.simplify(S.diff(current,p)-8*q*q*(2+q)/D**2)==0
assert S.simplify(corr_hot.subs(p,q)+q/(2+q))==0
assert S.simplify(corr_cold.subs(p,q)+q/(2+q))==0
assert S.simplify(corr_hot.subs(p,1)-(1-2*q-q*q)/(1+4*q+q*q))==0

# Exact rational comparisons with an independently solved six-state generator.
cases=0
for qq in [S.Rational(1,13),S.Rational(1,7),S.Rational(1,3),S.Rational(2,5),S.Rational(3,5),S.Rational(4,5)]:
    for pp in [qq,(qq+1)/2,S.Integer(1)]:
        G=Q.subs({q:qq,p:pp})
        A=G.T.copy(); A[5,:]=S.ones(1,6)
        rhs=S.zeros(6,1);rhs[5]=1
        v=A.inv()*rhs
        assert all(v[i]==pi[0,i].subs({p:pp,q:qq}) for i in range(6))
        f=0
        for i in range(6):
            for j in range(i+1,6):
                forward=float(v[i]*G[i,j])
                backward=float(v[j]*G[j,i])
                if forward and backward:
                    f+=(forward-backward)*log(forward/backward)
        expected=float((q*(p-q)*S.log(p/q)/D).subs({p:pp,q:qq}))
        assert abs(f-expected)<1e-11,(pp,qq,f,expected)
        cases+=1

# The minimum-sized zero-magnetization interacting periodic Ising sector has four sites.
# On n=3, each one-minority-spin configuration has identical exchange energy.
for n in [2,3]:
    for size in range(1,n):
        en=set()
        for occupied in combinations(range(n),size):
            bits=[1 if i in occupied else -1 for i in range(n)]
            en.add(-sum(bits[j]*bits[(j+1)%n] for j in range(n)))
        assert len(en)==1

assert S.simplify(S.diff((1-q)*(q*q+4*q+1)/(1-2*q-5*q*q),q) -
    (5*q**4+4*q**3+18*q*q+4*q+5)/(5*q*q+2*q-1)**2)==0

print('PASS: all 6 symbolic master equations; all 4 exact pair correlations; heat flux')
print('PASS: monotonicity and equilibrium identities; 18 independent rational stationary solves')
print('PASS: all 18 entropy-production evaluations; minimality for smaller cycles')
print('PASS: uniqueness derivative identity for the infinite-hot-bath entropy maximum')
