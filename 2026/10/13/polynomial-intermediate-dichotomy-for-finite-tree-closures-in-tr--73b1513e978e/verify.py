#!/usr/bin/env python3
"""Finite exact regression for colored tree-plan tree-closed type growth.

This program only verifies finite cases; the unbounded growth dichotomy is
proved mathematically in the accompanying text.
"""
from collections import defaultdict, Counter
from itertools import combinations_with_replacement, product
from math import comb


def descendants(plan, sigma):
    return [p for p in plan if p[:len(sigma)] == sigma]


def children(plan, sigma):
    return [p for p in plan if len(p) == len(sigma)+1 and p[:-1] == sigma]


def multiply(a,b,L):
    c=[0]*(L+1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b[:L+1-i]):
            c[i+j]+=x*y
    return c


def plethysm(a,L):
    out=[1]+[0]*L
    for k in range(1,L+1):
        if not a[k]: continue
        d=[0]*(L+1)
        for j in range(L//k+1):
            d[j*k]=comb(a[k]+j-1,j)
        out=multiply(out,d,L)
    return out


def power_series(plan,L):
    cache={}
    def F(sigma):
        if sigma in cache: return cache[sigma]
        out=[0,1]+[0]*(L-1)
        for tau in children(plan,sigma):
            part=F(tau)
            if plan[tau]=='I': part=plethysm(part,L)
            out=multiply(out,part,L)
        cache[sigma]=out
        return out
    return F(())


def closed_antichain(plan):
    infs=[s for s,lab in plan.items() if lab=='I']
    return all(not(a!=b and (a[:len(b)]==b or b[:len(a)]==a)) for a in infs for b in infs)


def antichain_formula(plan,L):
    root_fixed=sum(1 for s in plan if all(plan[s[:j]]=='1' for j in range(len(s)+1)))
    out=[0]*(L+1)
    if root_fixed<=L: out[root_fixed]=1
    for s,lab in plan.items():
        if lab!='I': continue
        size=len(descendants(plan,s))
        factor=[int(k%size==0) for k in range(L+1)]
        out=multiply(out,factor,L)
    return out


def instantiated_tree(plan,K):
    nodes={():()}
    # actual vertex path stores (plan-edge index, tag) steps
    for sigma in sorted(plan,key=len):
        for vertex,path in list(nodes.items()):
            if path!=sigma: continue
            for tau in children(plan,sigma):
                for tag in (range(K) if plan[tau]=='I' else ('*',)):
                    child=vertex+((tau[-1],tag),)
                    nodes[child]=tau
    return nodes


def closure(selected,nodes,plan):
    S={()}
    for v in selected:
        for j in range(len(v)+1):
            S.add(v[:j])
    changed=True
    while changed:
        changed=False
        for v in tuple(S):
            for child in nodes:
                if child[:-1]==v and len(child)==len(v)+1 and plan[nodes[child]]=='1' and child not in S:
                    S.add(child);changed=True
    return frozenset(S)


def canonical(S,nodes):
    def sub(v):
        bylabel=defaultdict(list)
        for u in S:
            if u[:-1]==v and len(u)==len(v)+1:
                bylabel[nodes[u]].append(sub(u))
        return (nodes[v],tuple((lab,tuple(sorted(bylabel[lab]))) for lab in sorted(bylabel)))
    return sub(())


def direct_types(plan,K):
    nodes=instantiated_tree(plan,K)
    infinity=[v for v,s in nodes.items() if plan[s]=='I']
    if len(infinity)>18:
        raise ValueError('finite verifier needs small instances')
    counts=defaultdict(set)
    for mask in range(1<<len(infinity)):
        selected=[v for i,v in enumerate(infinity) if mask>>i&1]
        S=closure(selected,nodes,plan)
        counts[len(S)].add(canonical(S,nodes))
    return {n:len(types) for n,types in counts.items()},len(nodes),1<<len(infinity)


def bounded_canonical_counts(plan,K):
    cache={}
    def F(sigma):
        if sigma in cache:return cache[sigma]
        childtypes=[]
        for tau in children(plan,sigma):
            shapes=F(tau)
            if plan[tau]=='1':
                childtypes.append([(x,) for x in shapes])
            else:
                childtypes.append([x for m in range(K+1) for x in combinations_with_replacement(shapes,m)])
        T=set()
        for combo in product(*childtypes):
            x=tuple(sorted(y for branch in combo for y in branch))
            size=1+sum(y[0] for y in x)
            key=(sigma,tuple(y[1] for y in x))
            T.add((size,key))
        cache[sigma]=sorted(T,key=repr)
        return cache[sigma]
    return Counter(n for n,_ in F(()))


def plan_from_string(edges, inf_paths):
    plan={(): '1'}
    for p in edges:
        assert p and all(p[:i] in plan for i in range(1,len(p)))
        plan[p]='I' if p in inf_paths else '1'
    return plan


def main():
    L=30; assertions=0
    plans=[
       plan_from_string([(0,)],{(0,)}),
       plan_from_string([(0,),(0,0)],{(0,),(0,0)}),
       plan_from_string([(0,),(0,0),(1,)],{(0,),(1,)}),
       plan_from_string([(0,),(0,0),(1,),(1,0)],{(0,),(1,)}),
       plan_from_string([(0,),(0,0),(0,0,0)],{(0,),(0,0,0)}),
       plan_from_string([(0,),(0,0),(0,1)],{(0,),(0,0),(0,1)}),
       plan_from_string([(0,),(0,0),(0,0,0),(1,)],{(0,),(0,0,0),(1,)})
    ]
    total_direct=0
    for plan in plans:
        coeff=power_series(plan,L)
        assert coeff[0]==0;assert coeff[1]>=0; assertions+=2
        direct,nodecount,examined=direct_types(plan,2)
        total_direct+=examined
        bounded=bounded_canonical_counts(plan,2)
        assert direct==dict(bounded),(plan,direct,bounded); assertions+=1
        if closed_antichain(plan):
            antichain=antichain_formula(plan,L)
            assert coeff==antichain,(plan,coeff,antichain);assertions+=L+1
        for n,c in bounded.items():
            # Infinite generic must have at least as many types.
            assert c<=coeff[n],(plan,n,c,coeff[n]);assertions+=1
    # Exhaust every increasing-parent encoding of a rooted tree with up to
    # six plan nodes, and every infinity/one labelling of nonroot nodes.
    total_plans=0; antichain_plans=0
    for nn in range(1,7):
        parent_lists=product(*(range(i) for i in range(1,nn)))
        for parents in parent_lists:
            positions=[()]
            nextchild=defaultdict(int)
            for par in parents:
                prefix=positions[par]; i=nextchild[prefix];nextchild[prefix]+=1
                positions.append(prefix+(i,))
            for bits in range(1<<(nn-1)):
                plan={v:('I' if bits>>(j-1)&1 else '1') for j,v in enumerate(positions) if j>0}
                plan[()]='1'
                cf=power_series(plan,15)
                assert cf[0]==0 and cf[1]>=0
                assertions+=2;total_plans+=1
                if closed_antichain(plan):
                    assert cf==antichain_formula(plan,15),(plan,cf)
                    assertions+=16;antichain_plans+=1
    # Euler's generalized-pentagonal recurrence is independent of the
    # multiset recurrence and uses only the Python standard library.
    partitions=[0]*L;partitions[0]=1
    for n in range(1,L):
        t=0
        for j in range(1,n+1):
            for k in (j*(3*j-1)//2,j*(3*j+1)//2):
                if k<=n: t+=(1 if j%2 else -1)*partitions[n-k]
        partitions[n]=t
    two=power_series(plans[1],L)
    for n in range(1,L+1):
        assert two[n]==partitions[n-1];assertions+=1
    print(f'VERIFY_OK {assertions} exact assertions; {total_direct} labelled finite-node selections screened; '+
          f'{len(plans)} tree-plan shapes compared by direct isomorphism invariants; '+
          f'{total_plans} exhaustive small plans incl. {antichain_plans} antichain plans')

if __name__=='__main__':main()
