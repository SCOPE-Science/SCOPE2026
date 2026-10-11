#!/usr/bin/env python3
from itertools import combinations


def faces_edges(n,k):
    faces=set()
    for i in range(n):
        faces.add(frozenset((i,(i+k)%n,(i+k+1)%n)))
        faces.add(frozenset((i,(i+1)%n,(i+k+1)%n)))
    edges=set()
    for f in faces:
        a=tuple(f)
        for x,y in combinations(a,2):
            edges.add(frozenset((x,y)))
    return faces,edges


def empty_triangles(n,k):
    faces,edges=faces_edges(n,k)
    nbr={v:set() for v in range(n)}
    for e in edges:
        x,y=tuple(e); nbr[x].add(y); nbr[y].add(x)
    tris=set()
    for v in range(n):
        N=sorted(nbr[v])
        for a,b in combinations(N,2):
            if frozenset((a,b)) in edges:
                tris.add(frozenset((v,a,b)))
    return tris-faces


def predicted(n,k):
    return (
        n*int(k==2)
        +(n//3)*int(n==3*k)
        +(n//3)*int(n==3*(k+1))
        +n*int(n==3*k+1)
        +n*int(n==3*k+2)
        +n*int(n==2*k+3)
    )

# Direct exhaustive check over a substantial parameter rectangle.
tested=0
first_flag=None
for n in range(7,181):
    for k in range(2,(n-3)//2+1):
        got=len(empty_triangles(n,k))
        want=predicted(n,k)
        assert got==want,(n,k,got,want)
        if got==0 and first_flag is None:
            first_flag=(n,k)
        tested += 1
assert first_flag==(13,3), first_flag

# The symbolic proof reduces a graph triangle to three signed steps in
# D={+-1,+-k,+-(k+1)}.  Under 2<=k<=floor((n-3)/2), a zero-sum
# relation besides 1+k=(k+1) is only 1+1=k (k=2); an n-sum must have
# all signs positive, and only the six multisets below can reach n.
# We verify the displayed contribution sizes directly on every
# parameter instance in the same range by constructing each family.
def fams(n,k):
    out=[]
    if k==2:
        out.append({frozenset((i,(i+1)%n,(i+2)%n)) for i in range(n)})
    if n==3*k:
        out.append({frozenset((i,(i+k)%n,(i+2*k)%n)) for i in range(n)})
    if n==3*(k+1):
        c=k+1
        out.append({frozenset((i,(i+c)%n,(i+2*c)%n)) for i in range(n)})
    if n==3*k+1:
        # cyclic steps k,k,k+1
        out.append({frozenset((i,(i+k)%n,(i+2*k)%n)) for i in range(n)})
    if n==3*k+2:
        c=k+1
        # cyclic steps k,c,c
        out.append({frozenset((i,(i+k)%n,(i+k+c)%n)) for i in range(n)})
    if n==2*k+3:
        c=k+1
        # cyclic steps 1,c,c
        out.append({frozenset((i,(i+1)%n,(i+1+c)%n)) for i in range(n)})
    return out

for n in range(7,181):
    for k in range(2,(n-3)//2+1):
        fs=fams(n,k)
        union=set().union(*fs) if fs else set()
        # Distinct relation types contribute disjoint triangle families.
        assert sum(map(len,fs))==len(union),(n,k,[len(x) for x in fs])
        assert union==empty_triangles(n,k),(n,k,len(union),len(empty_triangles(n,k)))

print(f"VERIFY_OK parameters={tested} range=n7..180 first_flag=13,3 exact_formula=yes relation_families=yes")
