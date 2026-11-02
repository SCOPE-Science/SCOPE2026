"""Exact finite tests for leaf-dominated random-majority dynamics.

Run with Python 3 standard library only. Finite checks supplement, not replace,
the theorem's all-order proof.
"""
from fractions import Fraction
from itertools import product
from math import comb


def instance(k, edges, leaves):
    assert k == len(leaves) and min(leaves) >= 1
    core = [[] for _ in range(k)]
    for u,v in edges:
        core[u].append(v)
        core[v].append(u)
    assert all(leaves[i] > len(core[i]) for i in range(k))
    groups = []
    neighbors = [list(t) for t in core]
    for i,t in enumerate(leaves):
        g=[]
        for _ in range(t):
            z=len(neighbors)
            neighbors.append([i])
            neighbors[i].append(z)
            g.append(z)
        groups.append(g)
    return core,groups,neighbors


def shift(s,groups):
    k=len(groups)
    a=s[:k]
    b=tuple(s[group[0]] for group in groups)
    return b+tuple(a[i] for i,group in enumerate(groups) for _ in group)


def coherent(s,groups):
    return all(len({s[z] for z in group})==1 for group in groups)


def step(s,neighbors):
    outcomes={():Fraction(1)}
    for group in neighbors:
        blue=sum(s[j] for j in group)
        if blue*2>len(group): options=[(1,Fraction(1))]
        elif blue*2<len(group): options=[(0,Fraction(1))]
        else: options=[(0,Fraction(1,2)),(1,Fraction(1,2))]
        outcomes={state+(v,):prob*q for state,prob in outcomes.items()
                  for v,q in options}
    assert sum(outcomes.values())==1
    return outcomes


def qprob(i,a,core,leaves,p):
    t=leaves[i]
    fixed=sum(a[j] for j in core[i])
    deg=t+len(core[i])
    total=Fraction(0)
    for j in range(t+1):
        b=fixed+j
        factor=Fraction(1) if b*2>deg else (Fraction(1,2) if b*2==deg else Fraction(0))
        total+=comb(t,j)*p**j*(1-p)**(t-j)*factor
    return total


def majority_binom(d,p):
    return sum((comb(d,j)*p**j*(1-p)**(d-j)
                *(Fraction(1) if 2*j>d else (Fraction(1,2) if 2*j==d else Fraction(0))))
               for j in range(d+1))


def canon(s,groups):
    t=shift(s,groups)
    return min(s,t)


def check(k,edges,leaves):
    core,groups,neighbors=instance(k,edges,leaves)
    n=len(neighbors)
    assert n<=12
    states=list(product((0,1),repeat=n))
    cstates=[s for s in states if coherent(s,groups)]
    assert len(cstates)==4**k
    fixed=sum(s==shift(s,groups) for s in cstates)
    assert fixed==2**k
    classes={canon(s,groups) for s in cstates}
    assert len(classes)==(4**k+2**k)//2
    comparisons=0
    distributions={p:{t:Fraction(0) for t in classes} for p in (Fraction(1,3),Fraction(2,3))}
    for s in states:
        transitions=step(s,neighbors)
        for x,pr in transitions.items():
            assert coherent(x,groups)
            assert step(x,neighbors)=={shift(x,groups):Fraction(1)}
            assert shift(shift(x,groups),groups)==x
            comparisons+=3
            for p,dist in distributions.items():
                weight=p**sum(s)*(1-p)**(n-sum(s))
                dist[canon(x,groups)]+=weight*pr
    for p,dist in distributions.items():
        w={}
        for a in product((0,1),repeat=k):
            qa=[qprob(i,a,core,leaves,p) for i in range(k)]
            for b in product((0,1),repeat=k):
                s=a+tuple(b[i] for i,group in enumerate(groups) for _ in group)
                pr=p**sum(a)*(1-p)**(k-sum(a))
                for i in range(k):
                    pr*=qa[i] if b[i] else 1-qa[i]
                key=canon(s,groups)
                w[key]=w.get(key,Fraction(0))+pr
        assert w==dist
        expected=sum(Fraction(sum(x)+sum(shift(x,groups)),2)*pr
                     for x,pr in dist.items())
        formula=sum(Fraction(leaves[i]+1,2)*
                    (p+majority_binom(leaves[i]+len(core[i]),p))
                    for i in range(k))
        assert expected==formula
        assert sum(dist.values())==1
        comparisons+=len(classes)+2
    return n,len(states),len(classes),comparisons


def main():
    instances=[
      (1,[],[1]),
      (1,[],[2]),
      (2,[(0,1)],[2,2]),
      (2,[(0,1)],[3,2]),
      (3,[(0,1),(1,2)],[2,3,2]),
      (3,[(0,1),(1,2),(2,0)],[3,3,3]),
    ]
    total=0
    for k,e,l in instances:
        r=check(k,e,l)
        print('PASS: core=%d edges=%s leaves=%s vertices=%d configurations=%d recurrent_classes=%d comparisons=%d'
              %(k,e,l,*r))
        total+=r[3]
    for r in range(1,9):
        for p in (Fraction(1,5),Fraction(1,2),Fraction(3,5),Fraction(4,5)):
            assert majority_binom(2*r,p)==majority_binom(2*r-1,p)
            delta=majority_binom(2*r+1,p)-majority_binom(2*r-1,p)
            assert delta==comb(2*r-1,r-1)*p**r*(1-p)**r*(2*p-1)
            total+=2
    print('PASS: total exact comparisons',total)

if __name__=='__main__': main()
