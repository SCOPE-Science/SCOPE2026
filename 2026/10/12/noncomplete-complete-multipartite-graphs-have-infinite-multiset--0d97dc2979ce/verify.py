#!/usr/bin/env python3
from itertools import combinations_with_replacement

def rgs_partitions(n):
    a=[0]*n
    def rec(pos,mx):
        if pos==n:
            yield tuple(a); return
        for x in range(mx+2):
            a[pos]=x
            yield from rec(pos+1,max(mx,x))
    a[0]=0
    yield from rec(1,0)

def compositions_nondec(total, parts, lo=1):
    def rec(rem,k,last,prefix):
        if k==0:
            if rem==0: yield tuple(prefix)
            return
        for x in range(last, rem+1):
            if rem-x < (k-1)*x: break
            yield from rec(rem-x,k-1,x,prefix+[x])
    yield from rec(total,parts,lo,[])

def codes_for_partition(sizes,rgs):
    cls=[]
    for i,s in enumerate(sizes): cls += [i]*s
    N=len(cls); k=max(rgs)+1
    blocks=[[v for v,b in enumerate(rgs) if b==j] for j in range(k)]
    reps=[]
    for v in range(N):
        rep=[]
        for B in blocks:
            if v in B: d=0
            elif any(cls[x]!=cls[v] for x in B): d=1
            else: d=2
            rep.append(d)
        reps.append(tuple(sorted(rep)))
    return reps

def structural_formula(sizes,rgs):
    cls=[]
    for i,s in enumerate(sizes): cls += [i]*s
    k=max(rgs)+1
    blocks=[[v for v,b in enumerate(rgs) if b==j] for j in range(k)]
    pure=[0]*len(sizes)
    for B in blocks:
        kinds={cls[v] for v in B}
        if len(kinds)==1: pure[next(iter(kinds))]+=1
    formula=[]
    for v,c in enumerate(cls):
        B=blocks[rgs[v]]
        own_pure=all(cls[x]==c for x in B)
        q=pure[c]-(1 if own_pure else 0)
        formula.append(tuple([0]+[1]*(k-1-q)+[2]*q))
    return formula

def main():
    graph_profiles=0; partitions=0; formula_checks=0
    # Exhaust every complete multipartite type through order 7 and every set partition.
    for N in range(2,8):
        for r in range(2,N+1):
            for sizes in compositions_nondec(N,r):
                graph_profiles += 1
                found=False
                for p in rgs_partitions(N):
                    partitions += 1
                    actual=codes_for_partition(sizes,p)
                    form=structural_formula(sizes,p)
                    assert actual==form,(sizes,p,actual,form)
                    formula_checks += N
                    if len(set(actual))==N:
                        found=True; break
                assert not found,('unexpected resolving partition',sizes)
    print('ALL CHECKS PASSED; graph_profiles=%d; set_partitions=%d; vertex_formula_checks=%d; order_range=2..7' % (graph_profiles,partitions,formula_checks))

if __name__=='__main__': main()
