#!/usr/bin/env python3
import itertools, math
alpha=0.2; r=2.75; mu=0.002; N=3
states=list(itertools.product((0,1), repeat=N))
idx={x:i for i,x in enumerate(states)}
partners={0:(1,2),1:(0,2),2:(0,1)}
d2=2; d3=1; qstar=1/3
def benefit(x,g):
    S=sum(x)
    return 3*alpha*r*(x[0]*x[1]*x[2] if g is None else (S/3)**g)
def payoff(x,i,g):
    p=sum((r/2)*(x[i]+x[j])-x[i] for j in partners[i])
    return (p+benefit(x,g)-x[i])/(d2+d3)
def fermi(a,b): return 1/(1+math.exp(a-b))
def kernel(g):
    P=[[0.0]*8 for _ in range(8)]
    for a,x in enumerate(states):
        for i in range(3):
            for j in partners[i]:
                w=fermi(payoff(x,i,g),payoff(x,j,g)); sel=1/6
                for z,pz in ((x[j],w),(x[i],1-w)):
                    for out,pm in ((z,1-mu),(1-z,mu)):
                        y=list(x); y[i]=out
                        P[a][idx[tuple(y)]] += sel*pz*pm
    for row in P: assert abs(sum(row)-1)<1e-12
    return P
def rowtv(P,Q):
    return max(0.5*sum(abs(a-b) for a,b in zip(x,y)) for x,y in zip(P,Q))
for bits in states:
    S=sum(bits); prod=bits[0]*bits[1]*bits[2]
    for g in (0.5,1,2,5,10,20):
        e=abs((S/3)**g-prod)
        assert e <= (2/3)**g+1e-15
        if S==2: assert abs(e-(2/3)**g)<1e-15
Pinf=kernel(None)
prev=None
for g in (2,5,10,20):
    tv=rowtv(kernel(g),Pinf)
    bound=1.5*alpha*r*qstar*(2/3)**g
    assert tv <= bound+1e-12
    prev=tv
assert prev < 1e-4
print("VERIFY_OK")
