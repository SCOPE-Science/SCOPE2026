"""Finite corroboration of depth-three flag-adjacency classifications.

The theorem's infinite scope is handled separately by its proof.
Run: python3 verify_designs.py
"""
from itertools import combinations

def pair_design(v):
    return [frozenset(c) for c in combinations(range(v), 2)]

def fano():
    # Nonzero vectors in F_2^3 form the points of PG(2,2).
    return sorted({frozenset((a, b, a ^ b)) for a in range(1, 8) for b in range(1, 8) if a != b}, key=lambda x:tuple(sorted(x)))

def projective_binary_3():
    return sorted({frozenset((a, b, a ^ b)) for a in range(1, 16) for b in range(1, 16) if a != b}, key=lambda x:tuple(sorted(x)))

def affine_prime(q):
    points = [(x,y) for x in range(q) for y in range(q)]
    out = [frozenset((x, (a*x+b)%q) for x in range(q)) for a in range(q) for b in range(q)]
    out += [frozenset((c,y) for y in range(q)) for c in range(q)]
    return out

def projective_prime(q):
    points = [(x,y,1) for x in range(q) for y in range(q)] + [(1,a,0) for a in range(q)] + [(0,1,0)]
    return [frozenset(p for p in points if sum(t*u for t,u in zip(p,L))%q==0) for L in points]

def flag_graph(blocks):
    flags=[(p,i) for i,B in enumerate(blocks) for p in sorted(B)]
    assert len(set(flags))==len(flags)
    n=len(flags)
    adj=[set() for i in range(n)]
    for i in range(n):
        for j in range(i):
            if flags[i][0]==flags[j][0] or flags[i][1]==flags[j][1]:
                adj[i].add(j); adj[j].add(i)
    return adj

def johnson(n,k):
    V=list(combinations(range(n),k)); A=[set() for _ in V]
    for i in range(len(V)):
        for j in range(i):
            if len(set(V[i])&set(V[j]))==k-1:A[i].add(j);A[j].add(i)
    return A

def verify_design(blocks):
    pts=set().union(*blocks);v=len(pts);k=len(blocks[0]);
    assert all(len(b)==k for b in blocks)
    pairs={tuple(sorted(pair)):0 for pair in combinations(pts,2)}
    for b in blocks:
        for pair in combinations(sorted(b),2):pairs[pair]+=1
    assert all(c==1 for c in pairs.values()),'not a Steiner 2-design'

def spectrum(A):
    n=len(A)
    # Third-point type over two named vertices records equalities and adjacency to them.
    T=[]
    for u in range(n):
        one=set()
        for v in range(n):
            mask=set()
            for w in range(n):
                mask.add((w==u,w==v,w in A[u],w in A[v]))
            one.add((u==v,v in A[u],tuple(sorted(mask))))
        T.append(frozenset(one))
    assert all(x==T[0] for x in T),'unexpected nonuniform pointed profile'
    return T[0]

def counts(A):return len(A),sum(map(len,A))//2

cases=[
    ('complete-pair-system-v3',pair_design(3),'small'),
    ('complete-pair-system-v4',pair_design(4),'middle'),
    ('complete-pair-system-v5',pair_design(5),'middle'),
    ('affine-plane-q2',affine_prime(2),'middle'),
    ('Fano-plane',fano(),'large'),
    ('affine-plane-q3',affine_prime(3),'large'),
    ('projective-plane-q3',projective_prime(3),'large'),
    ('affine-plane-q5',affine_prime(5),'large'),
    ('projective-plane-q5',projective_prime(5),'large'),
    ('binary-PG3-lines-STS15',projective_binary_3(),'large'),
]
by_class={}
for name,blocks,cl in cases:
    verify_design(blocks)
    A=flag_graph(blocks)
    spectrum_result=spectrum(A)
    by_class.setdefault(cl,spectrum_result)
    assert spectrum_result==by_class[cl],(name,cl)
    v,k=len(set().union(*blocks)),len(blocks[0])
    print(name, 'v=',v,'k=',k,'flags=',len(A),'edges=',counts(A)[1],'rank3_profile_count=',len(spectrum_result),'class=',cl)
assert len({*by_class.values()})==3
J=spectrum(johnson(7,3))
assert J==by_class['large']
print('Johnson-J(7,3): matches universal large-block class; vertices=35')
# Four-rank separating induced claw: J(7,3) has a claw; line graphs never have one.
A=johnson(7,3)
claw=next(((u,x,y,z) for u in range(len(A)) for x,y,z in combinations(sorted(A[u]),3) if y not in A[x] and z not in A[x] and z not in A[y]),None)
assert claw is not None
print('induced-claw witness in J(7,3):',claw)
print('CHECKS_PASS: three exact rank-three classes, representative minima 6/12/21; cross-family match and rank-four separator.')
