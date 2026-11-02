"""Independent finite checks of distance-intersection support, and Hamming formula."""
from itertools import product
from collections import deque

def hamming(d,q):
    V=list(product(range(q),repeat=d))
    D=[[sum(a!=b for a,b in zip(x,y)) for y in V] for x in V]
    return D

def triple_support(D):
    n=len(D); diameter=max(map(max,D))
    S={h:set() for h in range(diameter+1)}
    representative={}
    for x in range(n):
        for y in range(n):
            h=D[x][y]
            triple={(D[x][z],D[y][z]) for z in range(n)}
            if h in representative: assert representative[h]==triple, (h,representative[h],triple)
            else: representative[h]=triple
    return representative

def formula(d,q,h):
    out=set()
    # a of h disagreement sites choose x, b choose y, c choose neither;
    # e of d-h agreement sites choose a new symbol.
    for a in range(h+1):
        for b in range(h-a+1):
            c=h-a-b
            if c and q==2:continue
            for e in range(d-h+1):
                out.add((b+c+e,a+c+e))
    return out

results={}
for d in range(1,4):
    for q in (2,3,4):
        D=hamming(d,q)
        S=triple_support(D)
        for h, pairs in S.items(): assert pairs==formula(d,q,h),(d,q,h,pairs,formula(d,q,h))
        results[d,q]=S
        print(f'dimension={d} alphabet={q} vertices={len(D)} supports={[len(S[h]) for h in S]} verified')
    assert results[d,3]==results[d,4]
    assert results[d,2]!=results[d,3]
    print('three-variable support classes: binary distinct, all alphabet sizes >=3 match, d=',d)
# Independent symmetric-distance support identity on an example not of Hamming type: cycles.
for n in (5,6,7,8):
    D=[[min((i-j)%n,(j-i)%n) for j in range(n)] for i in range(n)]
    S=triple_support(D)
    print('cycle',n,'diameter',max(S),'total support triples',sum(map(len,S.values())))
print('ALL_CHECKS_PASS')
