#!/usr/bin/env python3
"""Independent matrix-and-vector checks of a radical-cube-zero quiver commutator claim.
Only prime fields are used for exhaustive tests; the theorem covers all prime powers.
"""
from collections import Counter
from itertools import product
from random import Random


def rank_matrix(rows, cols, q):
    a = [list(row) for row in rows]
    pivot = 0
    for j in range(cols):
        ix = next((i for i in range(pivot, len(a)) if a[i][j] % q), None)
        if ix is None:
            continue
        a[pivot], a[ix] = a[ix], a[pivot]
        inv = pow(a[pivot][j], -1, q)
        a[pivot] = [v * inv % q for v in a[pivot]]
        for i in range(len(a)):
            if i != pivot and a[i][j]:
                mul = a[i][j]
                a[i] = [(v - mul*w) % q for v,w in zip(a[i],a[pivot])]
        pivot += 1
        if pivot == min(cols,len(a)): break
    return pivot


def graph_from_paths(arrows):
    m = len(arrows)
    paths = [(i,j) for i,(u,v) in enumerate(arrows)
             for j,(w,x) in enumerate(arrows) if v == w]
    g = [set() for _ in arrows]
    for i,j in paths:
        if i != j:
            g[i].add(j)
            g[j].add(i)
    return paths, g


def formula(q,arrows):
    m=len(arrows); paths,g=graph_from_paths(arrows)
    out=Counter()
    for mask in range(1<<m):
        S={i for i in range(m) if mask>>i&1}
        closed=S | {j for i in S for j in g[i]}
        rem=set(S)
        components=0
        while rem:
            components+=1
            seen={rem.pop()}
            while True:
                found={y for x in seen for y in g[x] if y in rem}
                if not found: break
                seen |=found
                rem-=found
        out[len(closed)-components]+=(q-1)**len(S)*q**len(paths)
    return out


def independent_matrix_enumeration(q,arrows):
    m=len(arrows); paths,_=graph_from_paths(arrows)
    hist=Counter()
    for alpha in product(range(q),repeat=m):
        rows=[]
        for e,f in paths:
            row=[0]*m
            row[e]= (row[e]-alpha[f])%q
            row[f]= (row[f]+alpha[e])%q
            rows.append(row)
        hist[rank_matrix(rows,m,q)]+=q**len(paths)
    return hist


def vector_pair_count(q,arrows):
    m=len(arrows);paths,_=graph_from_paths(arrows)
    count=0
    for v in product(range(q),repeat=2*m):
        a=v[:m];b=v[m:]
        if all((a[i]*b[j]-b[i]*a[j])%q==0 for i,j in paths):
            count+=1
    return count


def theoretical_pair_count(q,arrows):
    paths,g=graph_from_paths(arrows)
    m=len(arrows)
    total=0
    for mask in range(1<<m):
        S={i for i in range(m) if mask>>i&1}
        rem=set(S);c=0
        while rem:
            c+=1
            frontier={rem.pop()}
            while frontier:
                new={v for u in frontier for v in g[u] if v in rem}
                rem-=new;frontier=new
        total+=(q-1)**len(S)*(q+1)**c
    return total


def path_count_recurrence(q,m):
    f0,f1=1,q*q
    if m==0:return f0
    if m==1:return f1
    for k in range(2,m+1):
        f0,f1=f1,q*f1+q*(q-1)*f0
    return f1


def main():
    cases=[
        ('zero',[]),
        ('single_loop',[(0,0)]),
        ('double_loop',[(0,0),(0,0)]),
        ('two_cycle',[(0,1),(1,0)]),
        ('two_parallel',[(0,1),(0,1)]),
        ('fork',[(0,1),(1,2),(1,3)]),
        ('in_fork',[(0,2),(1,2),(2,3)]),
        ('three_cycle',[(0,1),(1,2),(2,0)]),
        ('star',[(0,1),(0,2),(0,3)]),
        ('zigzag',[(0,1),(2,1),(2,3),(4,3)]),
    ]
    for m in range(1,6):
        cases.append((f'linear_{m}',[(i,i+1) for i in range(m)]))
    for m in range(2,6):
        cases.append((f'cycle_{m}',[(i,(i+1)%m) for i in range(m)]))
    configs=0;elements=0;pairs=0
    for q in (2,3,5):
        for name,arr in cases:
            if q**len(arr)>3000: continue
            predicted=formula(q,arr)
            actual=independent_matrix_enumeration(q,arr)
            assert predicted==actual, (name,q,predicted,actual)
            configs+=1;elements+=q**len(arr)
            if q**(2*len(arr))<=10000:
                pair=vector_pair_count(q,arr)
                assert pair==theoretical_pair_count(q,arr), (name,q,pair)
                assert pair==sum(v*q**(len(arr)+len(graph_from_paths(arr)[0])-r) for r,v in actual.items())//q**(2*len(graph_from_paths(arr)[0]))
                pairs+=q**(2*len(arr))
    for q in (2,3,5):
        for m in range(0,8):
            arr=[(i,i+1) for i in range(m)]
            z=theoretical_pair_count(q,arr)
            assert z==path_count_recurrence(q,m),(q,m,z)
    for q in (2,3,5):
        for m in range(2,9):
            arr=[(i,(i+1)%m) for i in range(m)]
            s=theoretical_pair_count(q,arr)
            # The Lucas trace recurrence has initial traces 2,q.
            L0,L1=2,q
            if m>=2:
                for _ in range(2,m+1):
                    L0,L1=L1,q*L1+q*(q-1)*L0
            assert s==L1+q*(q-1)**m,(q,m,s,L1)
    print('ALL_RADICAL_CUBE_ZERO_COMMUTATOR_CHECKS_PASSED',configs,elements,pairs)
if __name__=='__main__':main()
