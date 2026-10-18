"""Exact exhaustive finite proof for height-two dimension-two posets of size at most ten.
No external dependencies; all comparisons use integer tuples and backtracking.
"""
from itertools import permutations
from collections import defaultdict,Counter
from math import comb

def av123(n):
    family=[()]
    for value in range(n):
        nxt=[]
        for p in family:
            # Inserting the new maximum must precede the first increasing pair.
            first=next((j+1 for j in range(len(p)-1) if p[j]<p[j+1]),len(p))
            for i in range(first+1):nxt.append(p[:i]+(value,)+p[i:])
        family=nxt
    return family

def rows(p):
    return tuple(sum(1<<j for j in range(i+1,len(p)) if p[i]<p[j]) for i in range(len(p)))

def refine_all(objects,n):
    # All graphs share the same palette at every round, without hash shortcuts.
    # Label 0 is the uniform initial colour.
    data=[]
    for r in objects:
        dn=tuple(tuple(j for j in range(n) if (r[j]>>i)&1) for i in range(n))
        up=tuple(tuple(j for j in range(n) if (r[i]>>j)&1) for i in range(n))
        data.append((dn,up))
    colours=[(0,)*n for _ in objects]
    for _ in range(n):
        palette={};out=[]
        for (dn,up),c in zip(data,colours):
            nxt=[]
            for i in range(n):
                key=(c[i], tuple(sorted(c[j] for j in dn[i])),tuple(sorted(c[j] for j in up[i])))
                if key not in palette:palette[key]=len(palette)
                nxt.append(palette[key])
            out.append(tuple(nxt))
        colours=out
    return colours

def are_isomorphic(r,s,c1,c2):
    n=len(r)
    if sorted(c1)!=sorted(c2):return False
    # backtrack inside corresponding refinement classes
    B=defaultdict(list)
    for j,c in enumerate(c2):B[c].append(j)
    order=sorted(range(n), key=lambda i:len(B[c1[i]]))
    f={};used=set()
    def search(t):
        if t==n:return True
        i=order[t]
        for j in B[c1[i]]:
            if j in used:continue
            if any(bool(r[i]&(1<<k))!=bool(s[j]&(1<<z)) or
                   bool(r[k]&(1<<i))!=bool(s[z]&(1<<j)) for k,z in f.items()):continue
            f[i]=j;used.add(j)
            if search(t+1):return True
            del f[i];used.remove(j)
        return False
    return search(0)

def main():
    result=[]
    for n in range(1,11):
        ps=av123(n)
        assert len(ps)==comb(2*n,n)//(n+1),(n,len(ps))
        rr=[rows(p) for p in ps]
        col=refine_all(rr,n)
        buck=defaultdict(list)
        for i,c in enumerate(col):buck[tuple(sorted(c))].append(i)
        # A bucket is a single order-isomorphism type iff every representative
        # can be explicitly mapped to its first member, exactly checked.
        for group in buck.values():
            r0=rr[group[0]];c0=col[group[0]]
            for t in group[1:]:
                assert are_isomorphic(r0,rr[t],c0,col[t]), ('collision',n,ps[group[0]],ps[t])
        result.append((n,len(ps),len(buck)))
        print(n,len(ps),len(buck),flush=True)
    assert [b for _,_,b in result]==[1,2,4,9,21,55,151,447,1389,4502]
    print('PASS: every equal round-n directed-counting fingerprint is isomorphic through n=10; n=10 has 4502 global types')
if __name__=='__main__':main()
