"""Independent constructive enumerator for complementary-prism optima.
Run: python3 verify_structural.py > constructive_certificate.tsv
Only standard Python libraries are required. Output is deterministic.
"""
from itertools import combinations
from collections import deque,Counter

def opt_path(m):
    r=(m+2)//3
    for comb in combinations(range(m),r):
        x=set(comb)
        if any(i+1 in x for i in x):continue
        if all(any(abs(i-j)<=1 for j in x) for i in range(m)):
            yield comb

def opt_prism(n):
    seen=set()
    for j in range(n):
        for cc in opt_path(n-5):
            a={((j-1)%n),((j+1)%n)}|{(j+3+t)%n for t in cc}
            seen.add(sum(1<<x for x in a)|(1<<(n+j)))
        for cc in opt_path(n-2):
            a={(j+2+t)%n for t in cc}
            seen.add(sum(1<<x for x in a)|(1<<(n+j))|(1<<(n+(j+1)%n)))
    return sorted(seen)

def adjacent(u,v,n):
    if u<n and v<n:return (u-v)%n in (1,n-1)
    if u>=n and v>=n:return (u-v)%n not in (0,1,n-1)
    return u%n==v%n

def get_graph(n,sets):
    where={v:i for i,v in enumerate(sets)}
    A=[set() for _ in sets];B=[set() for _ in sets]
    for i,s in enumerate(sets):
        used=[u for u in range(2*n) if s>>u&1]
        free=[u for u in range(2*n) if not s>>u&1]
        for u in used:
            for v in free:
                j=where.get(s^(1<<u)^(1<<v))
                if j is not None and i<j:
                    B[i].add(j);B[j].add(i)
                    if adjacent(u,v,n):A[i].add(j);A[j].add(i)
    return A,B

def component_sizes(A):
    seen=set(); lengths=[]
    for i in range(len(A)):
        if i in seen:continue
        q=[i];seen.add(i)
        for v in q:
            for w in A[v]:
                if w not in seen:seen.add(w);q.append(w)
        lengths.append(len(q))
    return dict(sorted(Counter(lengths).items()))

def cf(x,letter):return ''.join(f'{letter}{k}:{v},' for k,v in x.items())

for n in range(5,13):
    sets=opt_prism(n)
    A,B=get_graph(n,sets)
    exp=(2*n if n%3==2 else n*(n//3)**2 if n%3==0 else n*(2*(n//3)+1))
    assert len(sets)==exp
    assert (sum(map(len,A))==0 if n%3==2 else component_sizes(A)=={exp:1})
    print(f'SUMMARY\t{n}\t{n//3+2}\t{len(sets)}\t{sum(map(len,B))//2}\t{sum(map(len,A))//2}\t{cf(component_sizes(A),"S")}\t{cf(component_sizes(B),"J")}')
    for s in sets:print(f'SET\t{n}\t{s}')
# Checks well beyond the brute-force range without printing large certificates.
for n in range(13,22):
    ss=opt_prism(n)
    exp=(2*n if n%3==2 else n*(n//3)**2 if n%3==0 else n*(2*(n//3)+1))
    assert len(ss)==exp
    A,B=get_graph(n,ss)
    assert (sum(map(len,B))==0 if n%3==2 else component_sizes(A)=={exp:1})
print('EXTENDED_CHECKS\t13..21\tpassed')
