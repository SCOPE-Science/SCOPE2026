#!/usr/bin/env python3
"""Exact finite-state tests for sector classification and stationary transport."""
from fractions import Fraction
from math import comb, gcd
from itertools import product
from collections import defaultdict

def strongly_connected_components(nodes, edges):
    visited=set(); finish=[]
    def forward(u):
        visited.add(u)
        for v in edges[u]:
            if v not in visited: forward(v)
        finish.append(u)
    for u in nodes:
        if u not in visited: forward(u)
    backwards={u:[] for u in nodes}
    for u in nodes:
        for v in edges[u]:backwards[v].append(u)
    visited.clear()
    groups=[]
    def reverse(u,group):
        visited.add(u);group.add(u)
        for v in backwards[u]:
            if v not in visited:reverse(v,group)
    for u in reversed(finish):
        if u not in visited:
            group=set();reverse(u,group);groups.append(group)
    return groups

def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in compositions(total-a,n-1):
                yield (a,)+tail

def weight(h):
    return {3:Fraction(2),4:Fraction(3),5:Fraction(5,2)}.get(h+1,Fraction(1))

def transitions(state, N,L,I,rs,ls):
    z,h = state
    for i in range(N):
        j=(i-1)%N
        if h[i]>=I and rs:
            hh=list(h);hh[i]-=I;hh[j]+=I
            yield ( ((z+I)%L if i==0 else z,tuple(hh)), rs*weight(h[i]-I)/weight(h[i]), I )
        if h[j]>=I and ls:
            hh=list(h);hh[j]-=I;hh[i]+=I
            yield ( ((z-I)%L if i==0 else z,tuple(hh)), ls*weight(h[j]-I)/weight(h[j]),-I )

def sector(s,L,I):
    z,h=s; rr=tuple(v%I for v in h)
    Q=(sum(h)-sum(rr))//I
    return (rr, Q, z if Q==0 else z%gcd(L,I))

def Zcoeff(rr,Q,I):
    if Q<0:return Fraction(0)
    val=Fraction(0)
    for q in compositions(Q,len(rr)):
        p=Fraction(1)
        for r,qi in zip(rr,q):
            p*=weight(r+I*qi)
        val+=p
    return val

def verify(N,L,I,rs,ls):
    H=L-N
    states=[(z,h) for z in range(L) for h in compositions(H,N)]
    edges={s:set() for s in states}
    rates={}
    for s in states:
        tr=list(transitions(s,N,L,I,rs,ls))
        rates[s]=tr
        for dst,rate,_ in tr: edges[s].add(dst)
    byclass=defaultdict(set)
    for s in states:byclass[sector(s,L,I)].add(s)
    components=strongly_connected_components(states,edges)
    assert {frozenset(c) for c in components}=={frozenset(c) for c in byclass.values()},("SCC",N,L,I)
    for label,ss in byclass.items():
        rr,Q,_=label
        if Q==0:
            assert len(ss)==1
        else:
            assert len(ss)==L//gcd(I,L)*comb(Q+N-1,N-1)
        pi={s: __import__('math').prod(weight(h) for h in s[1]) for s in ss}
        part=sum(pi.values(),Fraction(0))
        for s in ss:
            outgoing=sum((pi[s]*rate for _,rate,_ in rates[s]),Fraction(0))
            incoming=sum((pi[src]*rate for src in ss for dst,rate,_ in rates[src] if dst==s),Fraction(0))
            assert incoming==outgoing,("balance",N,L,I,s,incoming,outgoing)
        expected=Fraction(N*I,L)*(rs-ls)*Zcoeff(rr,Q-1,I)/Zcoeff(rr,Q,I)
        direct=sum((pi[s]*rate*sgn/L for s in ss for _,rate,sgn in rates[s]),Fraction(0))/part
        assert direct==expected,("current",N,L,I,label,direct,expected)
    return len(states),len(byclass)

def main():
    cases=states=classes=0
    for N in range(2,5):
      for L in range(N+1,11):
       for I in range(1,min(4,L)):
        for rs,ls in [(Fraction(1),Fraction(0)),(Fraction(3,2),Fraction(1,2)),(Fraction(0),Fraction(1))]:
            a,b=verify(N,L,I,rs,ls)
            cases+=1;states+=a;classes+=b
    print(f"PASS: {cases} finite generators, {states} states examined, {classes} class balances and exact current identities")
    N,L,I=3,6,2
    frozen=(0,(1,1,1)); active=(0,(2,1,0))
    print("Coexistence:",sector(frozen,L,I),"current=0;",sector(active,L,I),
          "current=",Fraction(N*I,L)*Zcoeff((0,1,0),0,I)/Zcoeff((0,1,0),1,I))
if __name__=="__main__":main()
