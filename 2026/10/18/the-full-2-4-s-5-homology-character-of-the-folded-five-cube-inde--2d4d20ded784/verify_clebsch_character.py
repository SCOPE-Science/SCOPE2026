"""Exact character and homology checks for the folded-five-cube independence complex.

Only the Python 3 standard library is needed. All integer calculations exhaust the
finite graph, all 1920 affine automorphisms, and all independent vertex sets.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations

DIRECTIONS = (1, 2, 4, 8, 15)
N = 16
NEIGHBORS = [sum(1 << (x ^ d) for d in DIRECTIONS) for x in range(N)]
ALPHAS = tuple(15 ^ (1 << i) for i in range(4)) + (15,)

def bitdot(a, b):
    return (a & b).bit_count() & 1

def parity_of_perm(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def independent(m):
    return all(not (NEIGHBORS[x] & m) for x in range(N) if (m >> x) & 1)

def enumerate_faces():
    return [m for m in range(1 << N) if independent(m)]

def rank_f2(vectors):
    basis = {}
    for x in vectors:
        while x:
            p = x.bit_length() - 1
            if p in basis: x ^= basis[p]
            else: basis[p] = x; break
    return len(basis)

def boundary_ranks(faces):
    by_size = [[m for m in faces if m.bit_count() == k] for k in range(6)]
    ranks=[]
    for k in range(2,6):
        ix={m:i for i,m in enumerate(by_size[k-1])}
        columns=[]
        for m in by_size[k]:
            v=0;left=m
            while left:
                low=left & -left;left-=low
                v ^= 1 << ix[m ^ low]
            columns.append(v)
        ranks.append(rank_f2(columns))
    # simplicial reduced complex has C_0 -> C_{-1}; connected 1-skeleton:
    return ranks

def induced_perm_of_vertices(p,t):
    images=[0]*N
    for x in range(N):
        y=t
        for i in range(4):
            if (x >> i)&1: y ^= DIRECTIONS[p[i]]
        images[x]=y
    return images

def direct_signed_euler(g,faces):
    total=0
    for mask in faces:
        vertices=[i for i in range(N) if (mask >> i)&1]
        images=[g[i] for i in vertices]
        if sum(1<<y for y in images) != mask: continue
        total += (-1)**len(vertices) * parity_of_perm(images)
    return total

def orbit_signed_euler(g):
    visited=set(); cycles=[]
    for x in range(N):
        if x in visited: continue
        orbit=[];y=x
        while y not in visited:
            visited.add(y);orbit.append(y);y=g[y]
        m=sum(1<<v for v in orbit)
        if independent(m):cycles.append(m)
    neigh=[]
    for m in cycles:
        nb=0
        for v in range(N):
            if (m >> v)&1: nb |= NEIGHBORS[v]
        neigh.append(nb)
    o=len(cycles)
    collision=[sum((1<<j) for j in range(o) if j!=i and (neigh[i]&cycles[j])) for i in range(o)]
    @lru_cache(None)
    def rec(active):
        if not active:return 1
        b=active & -active;i=b.bit_length()-1
        # An included independent vertex orbit contributes -1, regardless of its length.
        return rec(active^b)-rec(active &~(b|collision[i]))
    return rec((1<<o)-1)

def predicted(p,t):
    eps=parity_of_perm(p)
    fixed=[i for i in range(5) if p[i]==i]
    std=len(fixed)-1
    monomial=sum((-1)**bitdot(ALPHAS[i],t) for i in fixed)
    return eps*(std+monomial),eps*std,eps*monomial

def main():
    faces=enumerate_faces()
    f=Counter(m.bit_count() for m in faces)
    assert f == Counter({0:1,1:16,2:80,3:160,4:120,5:16}),f
    ranks=boundary_ranks(faces)
    assert ranks == [15,65,95,16],ranks
    assert len(faces)==393
    # Mod-two nonzero minors provide lower bounds on characteristic-zero ranks.
    # Since successive boundaries compose to zero, the boundary dimensions
    # force all of these ranks to be identical over Q.
    counts=[16,80,160,120,16]
    assert ranks[0]==counts[0]-1
    assert ranks[1]==counts[1]-ranks[0]
    assert ranks[2]==counts[2]-ranks[1]
    assert ranks[3]==counts[4]
    betti3=counts[3]-ranks[2]-ranks[3]
    assert betti3==9
    assert len({tuple(induced_perm_of_vertices(p,t)) for p in permutations(range(5)) for t in range(16)})==1920
    # Every automorphism fixing 0 permutes its five neighbours, and each other
    # vertex is a unique sum of two distinct connection directions.
    assert len({DIRECTIONS[i]^DIRECTIONS[j] for i,j in combinations(range(5),2)})==10
    groupchars=[];four=[];five=[];tc=[]; class_examples={}
    for p in permutations(range(5)):
        for t in range(16):
            g=induced_perm_of_vertices(p,t)
            assert sorted(g)==list(range(16))
            assert all(((NEIGHBORS[g[x]] >> g[x^d]) & 1) for x in range(N) for d in DIRECTIONS)
            value,part4,part5=predicted(p,t)
            assert direct_signed_euler(g,faces)==value,(p,t,value)
            assert orbit_signed_euler(g)==value,(p,t,value)
            groupchars.append(value);four.append(part4);five.append(part5)
            if p==tuple(range(5)):tc.append(value)
    assert Counter(groupchars)==Counter({9:1,5:10,3:80,1:865,-1:884,-3:60,-5:20})
    assert sum(x for x in groupchars)==0
    assert sum(x*x for x in groupchars)==3840
    assert sum(a*a for a in four)==1920
    assert sum(b*b for b in five)==1920
    assert sum(a*b for a,b in zip(four,five))==0
    assert sum(tc)==64
    assert tc == [9,1,1,5,1,5,5,5,1,5,5,5,5,5,5,1]
    print('PASS: degree-five folded cube, 393 faces, face-size counts',dict(sorted(f.items())))
    print('PASS: mod-two boundary ranks',ranks,'and exact rational reduced H_3 dimension',betti3)
    print('PASS: all 1920 graph automorphisms, signed-face and orbit Lefschetz character')
    print('PASS: exact character histogram',dict(sorted(Counter(groupchars).items())))
    print('PASS: orthogonal absolutely irreducible constituents of ranks 4 and 5')
    print('PASS: T-invariants dimension 4, G-invariants dimension 0')

if __name__=='__main__': main()
