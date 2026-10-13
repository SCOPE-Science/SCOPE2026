#!/usr/bin/env python3
"""Exhaustive verification of a two-colour signed-burning reachability theorem.
Runs on the unsigned complete multipartite graph; switching equivariance is
verified independently for every gauge of each small graph.
"""
from itertools import product
from collections import deque

def edges(parts):
    vpart=[i for i,z in enumerate(parts) for _ in range(z)]
    n=len(vpart)
    return [[j for j in range(n) if vpart[j]!=vpart[i]] for i in range(n)],vpart

def burn_step(s,neighbors,signs):
    # Spread from the previous burned state simultaneously.
    n=len(s);out=list(s)
    for v in range(n):
        if s[v]:continue
        total=sum(s[u]*signs[v][u] for u in neighbors[v])
        if total:out[v]=1 if total>0 else -1
    return tuple(out)

def all_terminal(neighbors,signs):
    n=len(neighbors)
    seen={(0,)*n};stack=[(0,)*n];terminal=set()
    while stack:
        s=stack.pop();t=burn_step(s,neighbors,signs)
        if 0 not in t:
            terminal.add(t);continue
        for v in range(n):
            if not t[v]:
                for c in (-1,1):
                    x=tuple(c if i==v else t[i] for i in range(n))
                    if x not in seen:seen.add(x);stack.append(x)
    return terminal

def claimed_code(part_of,gauge):
    n=len(part_of);E={i for i in range(n) if part_of.count(part_of[i])>=2}
    base=set()
    for c in (-1,1):
        for v in [-1]+sorted(E):
            base.add(tuple(gauge[i]*(-c if i==v else c) for i in range(n)))
    return base,E

def dist(x,y):return sum(a!=b for a,b in zip(x,y))

def claimed_radius(n,m,s):
    if m==0:return n//2
    if n%2==0:return n//2-1
    t=(n-1)//2
    return t if s>=t else t-1

def partitions(n,minimum=1):
    def rec(k,remaining,acc):
        if k==0:
            if remaining==0:yield tuple(acc)
            return
        for z in range(minimum,remaining-k*minimum+2):
            yield from rec(k-1,remaining-z,acc+[z])
    for k in range(3,n+1):
        yield from rec(k,n,[])

def main():
    cases=gauges=terminal_counts=0
    for n in range(3,8):
        for parts in partitions(n):
            neighbors,p=edges(parts)
            gauge0=(1,)*n
            base,E=claimed_code(p,gauge0)
            direct=all_terminal(neighbors,[[1]*n for _ in range(n)])
            assert direct==base,(parts,direct^base)
            assert len(base)==2+2*len(E),(parts,len(base))
            radius=max(min(dist(t,c) for c in base) for t in product((-1,1),repeat=n))
            assert radius==claimed_radius(n,len(E),n-len(E)),(parts,radius)
            for g in product((-1,1),repeat=n-1):
                gauge=(1,)+g
                signature=[[gauge[u]*gauge[v] for u in range(n)] for v in range(n)]
                observed=all_terminal(neighbors,signature)
                predicted,E2=claimed_code(p,gauge)
                assert observed==predicted,(parts,gauge,observed^predicted)
                a=sum(x==1 for x in gauge);b=n-a
                formula=max([a,b]+([a+1] if any(gauge[v]==-1 for v in E) else [])+([b+1] if any(gauge[v]==1 for v in E) else []))
                actual=max(max(sum(v==1 for v in w),sum(v==-1 for v in w)) for w in observed)
                assert formula==actual,(parts,gauge,formula,actual)
                gauges+=1;terminal_counts+=len(observed)
            cases+=1
    print('PASS balanced complete multipartite unsigned-code, covering-radius and switched-code verifier')
    print('all ordered multipartite profiles 3<=N<=7:',cases)
    print('switching signatures independently exhausted:',gauges)
    print('terminal profiles verified:',terminal_counts)
    print('follows by universal proof; finite checks are non-proofs of unbounded claim')
if __name__=='__main__':main()
