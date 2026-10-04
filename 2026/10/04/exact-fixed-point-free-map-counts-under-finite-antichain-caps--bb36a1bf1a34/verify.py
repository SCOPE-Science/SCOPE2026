#!/usr/bin/env python3
from itertools import product

def transitive_posets(n):
    # Enumerate all labeled partial orders by choosing, for each unordered pair,
    # either incomparable, i<j, or j<i; keep the transitive choices.
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for states in product((0,1,2), repeat=len(pairs)):
        le=[[False]*n for _ in range(n)]
        for i in range(n): le[i][i]=True
        ok=True
        for (i,j),s in zip(pairs,states):
            if s==1: le[i][j]=True
            elif s==2: le[j][i]=True
        # transitivity
        for k in range(n):
            for i in range(n):
                if le[i][k]:
                    for j in range(n):
                        if le[k][j] and not le[i][j]:
                            ok=False; break
                    if not ok: break
            if not ok: break
        if ok: yield le

def monotone_maps(le):
    n=len(le)
    for f in product(range(n), repeat=n):
        good=True
        for x in range(n):
            for y in range(n):
                if le[x][y] and not le[f[x]][f[y]]:
                    good=False; break
            if not good: break
        if good: yield f

def ordinal_cap(le,r):
    n=len(le); N=n+r
    out=[[False]*N for _ in range(N)]
    for i in range(N): out[i][i]=True
    for i in range(n):
        for j in range(n): out[i][j]=le[i][j]
    for i in range(n):
        for a in range(n,N): out[i][a]=True
    return out

def fpf_count(le):
    n=len(le)
    return sum(1 for f in monotone_maps(le) if all(f[i]!=i for i in range(n)))

def predicted(le,r):
    n=len(le); total=0
    for g in monotone_maps(le):
        if any(g[i]==i for i in range(n)): continue
        u=sum(all(le[g[x]][z] for x in range(n)) for z in range(n))
        total += (u+r-1)**r
    return total

def main():
    poset_counts={}
    tests=0
    map_checks=0
    for n,maxr in [(1,3),(2,3),(3,3),(4,2)]:
        pcs=0
        for le in transitive_posets(n):
            pcs+=1
            for r in range(2,maxr+1):
                got=fpf_count(ordinal_cap(le,r))
                want=predicted(le,r)
                assert got==want, (n,r,got,want,le)
                tests+=1
                map_checks += (n+r)**(n+r)
        poset_counts[n]=pcs
    assert poset_counts=={1:1,2:3,3:19,4:219}, poset_counts
    print('labeled_posets=' + ','.join(f'{n}:{poset_counts[n]}' for n in sorted(poset_counts)))
    print(f'theorem_instances={tests}')
    print(f'ambient_function_assignments_upper_bound={map_checks}')
    print('ranges=n<=4,r=2; n<=3,r=3')
    print('VERIFY_OK')
if __name__=='__main__': main()
