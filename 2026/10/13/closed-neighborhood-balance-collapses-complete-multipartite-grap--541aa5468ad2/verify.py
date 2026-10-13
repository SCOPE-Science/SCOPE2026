from itertools import product
from math import factorial


def vertices(parts):
    out=[]
    for i,n in enumerate(parts):
        out += [(i,j) for j in range(n)]
    return out


def valid(parts,k,colors):
    V=vertices(parts)
    if set(colors)!=set(range(k)):
        return False
    idx={v:i for i,v in enumerate(V)}
    for v in V:
        pi=v[0]
        counts=[0]*k
        for u in V:
            if u==v or u[0]!=pi:
                counts[colors[idx[u]]]+=1
        if len(set(counts))!=1:
            return False
    return True


def predicted(parts,k):
    n=sum(parts)
    if not all(x==1 for x in parts) or n%k:
        return 0
    m=n//k
    return factorial(n)//(factorial(m)**k)

profiles=0
assignments=0
valids=0
max_order=8
for r in range(2,6):
    for parts in product(range(1,4), repeat=r):
        if tuple(sorted(parts, reverse=True))!=parts:
            continue
        n=sum(parts)
        if n>max_order:
            continue
        profiles+=1
        for k in range(2,min(4,n)+1):
            got=0
            for colors in product(range(k), repeat=n):
                assignments+=1
                if valid(parts,k,colors):
                    got+=1
            valids+=got
            want=predicted(parts,k)
            assert got==want,(parts,k,got,want)
print(f"ALL CHECKS PASSED; profiles={profiles}; assignments={assignments}; valid_colorings={valids}; max_order={max_order}; k_range=2..4")
