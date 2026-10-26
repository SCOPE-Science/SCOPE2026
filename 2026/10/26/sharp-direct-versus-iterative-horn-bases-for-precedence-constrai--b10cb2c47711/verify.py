"""Self-contained small-instance checks for strict-order comparison closures.

Public, self-contained; Python 3 standard library only.
"""
from itertools import permutations
from math import factorial, ceil, log2
from functools import reduce
import random


def graph(n):
    arcs = [(a,b) for a in range(n) for b in range(n) if a!=b]
    return arcs, {p:i for i,p in enumerate(arcs)}


def bitset(lst,idx):
    out=0
    for item in lst:out|=1<<idx[item]
    return out


def actual_closure(s,model_masks,full):
    compatible=[m for m in model_masks if s & ~m ==0]
    if not compatible:return full
    c=full
    for m in compatible:c&=m
    return c


def rules(n,direct):
    arcs,ix=graph(n)
    full=(1<<len(arcs))-1
    out={}
    # All directed simple paths of length >=2, or only length two
    for ell in (range(2,n) if direct else [2]):
        if ell>=n:continue
        for p in permutations(range(n),ell+1):
            premise=bitset(zip(p,p[1:]),ix)
            if direct:
                concl=bitset(((p[i],p[j]) for i in range(ell+1) for j in range(i+1,ell+1)),ix)
            else:
                concl=1<<ix[p[0],p[2]]
            out[premise]=out.get(premise,0)|concl
    # Cycles of length 2 through n-1 (direct); length 2 (iterative)
    for ell in (range(2,n) if direct else [2]):
        if ell>=n:continue
        for cycle in permutations(range(n),ell):
            if cycle[0]!=min(cycle):continue
            prem=bitset(((cycle[i],cycle[(i+1)%ell]) for i in range(ell)),ix)
            out[prem]=out.get(prem,0)|(full if direct or ell==2 else 0)
    return list(out.items())


def apply(s,rr):
    return s | reduce(lambda accum,rule: accum | (rule[1] if rule[0]&s==rule[0] else 0),rr,0)


def verify(n,all_cases,draws):
    arcs,ix=graph(n); full=(1<<len(arcs))-1
    perms=list(permutations(range(n)))
    models=[bitset(((p[i],p[j]) for i in range(n) for j in range(i+1,n)),ix) for p in perms]
    it=rules(n,False); dr=rules(n,True)
    if n>=3:
        assert len(it)==n*(n-1)*(n-2)+n*(n-1)//2,(n,len(it))
        expect=sum(factorial(n)//factorial(n-ell-1) for ell in range(2,n))+sum(factorial(n)//(ell*factorial(n-ell)) for ell in range(2,n))
        assert len(dr)==expect,(n,len(dr),expect)
    seq=list(range(1<<len(arcs))) if all_cases else [random.Random(n*123+i).getrandbits(len(arcs)) for i in range(draws)]
    maxround=0
    for s in seq:
        target=actual_closure(s,models,full)
        once=apply(s,dr)
        assert once==target,('direct failure',n,s,once,target)
        x=s
        for turn in range(n+4):
            if x==target:break
            xnew=apply(x,it)
            assert xnew!=x,('stalled',n,s,x,target)
            x=xnew
        assert x==target,('iterative failure',n,s)
        maxround=max(maxround,turn)
    assert maxround<=ceil(log2(n-1)),(n,maxround)
    cyc=bitset(((i,(i+1)%n) for i in range(n)),ix)
    x=cyc
    t=0
    while x!=full:
        x=apply(x,it);t+=1
        assert t<n+3
    assert t==ceil(log2(n-1)),(n,t)
    print('n',n,'model_count',len(models),'rule_counts_iter_direct',len(it),len(dr),'cases',len(seq),'largest_round',maxround,'cycle_rounds',t,'PASS')


def main():
    for n in (3,4):verify(n,True,0)
    verify(5,False,1024)
    for n in range(3,9):
        if n<6:continue
        rr=rules(n,False)
        arc,ix=graph(n);full=(1<<len(arc))-1
        cyc=bitset(((i,(i+1)%n) for i in range(n)),ix)
        t=0
        while cyc!=full:
            cyc=apply(cyc,rr);t+=1
            assert t<=n
        assert t==ceil(log2(n-1))
        print('n',n,'iterative_basis',len(rr),'cycle_rounds',t,'PASS')
    print('VERIFY_OK exact_closure=PASS optimal_basis_counts=PASS direct_one_round=PASS logarithmic_depth=PASS')

if __name__=='__main__':main()
