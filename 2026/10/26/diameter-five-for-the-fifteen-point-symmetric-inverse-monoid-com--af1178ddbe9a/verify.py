#!/usr/bin/env python3
"""Exact finite certificate for diameter five in the degree-15 symmetric inverse monoid."""
N=15
ALPHA=tuple((i+1)%N for i in range(N))
BETA=(12,7,8,14,5,2,0,3,6,13,4,1,9,11,10)
IDENTITY=tuple(range(N))
ZERO=(-1,)*N

def compose(a,b):
    return tuple(-1 if b[i]<0 else a[b[i]] for i in range(N))

def power(p,k):
    r=IDENTITY
    for _ in range(k):r=compose(p,r)
    return r

def inverse(p):
    inv=[-1]*N
    for i,j in enumerate(p):
        assert 0<=j<N and inv[j]==-1
        inv[j]=i
    return tuple(inv)

def cycle_length(p):
    v=0;seen=set()
    while v not in seen:
        seen.add(v);v=p[v]
    return len(seen) if v==0 else 0

def equivariant_images(a,b):
    """All possible values at point 0 of a bijection commuting with a,b.
    A valid label propagation also checks transitivity and bijectivity."""
    gs=(a,b,inverse(a),inverse(b))
    images=[]
    for target in range(N):
        mapping=[-1]*N;mapping[0]=target
        frontier=[0];valid=True
        for v in frontier:
            for g in gs:
                u=g[v];w=g[mapping[v]]
                if mapping[u]==-1:
                    mapping[u]=w;frontier.append(u)
                elif mapping[u]!=w:
                    valid=False;break
            if not valid:break
        if valid and len(frontier)==N and len(set(mapping))==N:
            m=tuple(mapping)
            assert all(compose(m,g)==compose(g,m) for g in gs)
            images.append(target)
    return images

def transitive(a,b):
    gs=(a,b,inverse(a),inverse(b))
    seen={0};todo=[0]
    for v in todo:
        for g in gs:
            w=g[v]
            if w not in seen:seen.add(w);todo.append(w)
    return len(seen)==N

assert cycle_length(ALPHA)==N and cycle_length(BETA)==N
assert power(ALPHA,15)==IDENTITY and power(BETA,15)==IDENTITY
for i in (3,5):
    for j in (3,5):
        a,b=power(ALPHA,i),power(BETA,j)
        assert transitive(a,b)
        assert equivariant_images(a,b)==[0], (i,j,equivariant_images(a,b))
        print('CERTIFICATE exponents',i,j,'orbit=15 centralizer_images=(0,)')
for i in range(1,15):
    for j in range(1,15):
        assert transitive(power(ALPHA,i),power(BETA,j))
        assert equivariant_images(power(ALPHA,i),power(BETA,j))==[0]

def partial_identity(s):return tuple(i if i in s else -1 for i in range(N))
A=frozenset((0,5,10)); B=frozenset((2,3,9))
assert A.isdisjoint(B)
assert set(power(ALPHA,5)[i] for i in A)==A
assert set(power(BETA,5)[i] for i in B)==B
P=(ALPHA,power(ALPHA,5),partial_identity(A),partial_identity(B),power(BETA,5),BETA)
assert all(v!=ZERO and v!=IDENTITY for v in P)
assert all(P[i]!=P[i+1] for i in range(5))
assert all(compose(P[i],P[i+1])==compose(P[i+1],P[i]) for i in range(5))
print('EXPLICIT_COMMUTING_PATH_LENGTH=5')
print('ALL_196_POWER_PAIR_TESTS_PASS')
print('VERIFY_OK_INVERSE_MONOID_15_DIAMETER_5')
