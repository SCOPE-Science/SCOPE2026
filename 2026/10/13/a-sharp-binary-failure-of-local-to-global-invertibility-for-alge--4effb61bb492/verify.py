#!/usr/bin/env python3
import itertools

def mat_bits(x, n):
    return [[(x >> (i*n+j)) & 1 for j in range(n)] for i in range(n)]

def rank2(M):
    A=[row[:] for row in M]
    nrows=len(A); ncols=len(A[0]) if A else 0
    r=0
    for c in range(ncols):
        piv=next((i for i in range(r,nrows) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(nrows):
            if i!=r and A[i][c]:
                A[i]=[a^b for a,b in zip(A[i],A[r])]
        r+=1
    return r

def apply(x, v, n):
    M=mat_bits(x,n)
    return tuple(sum(M[i][j]*v[j] for j in range(n)) & 1 for i in range(n))

def span(gens):
    S={0}
    for g in gens:
        S |= {x^g for x in list(S)}
    return frozenset(S)

def all_subspaces(dim_ambient):
    # Breadth-first generation is exact and duplicate-safe.
    universe=list(range(1<<dim_ambient))
    seen={frozenset({0})}
    frontier=[frozenset({0})]
    while frontier:
        E=frontier.pop()
        for g in universe[1:]:
            if g in E:
                continue
            F=span(list(E)+[g])
            if F not in seen:
                seen.add(F)
                frontier.append(F)
    return seen

def ref_contains(E,T,n):
    vecs=list(itertools.product((0,1), repeat=n))
    return all(any(apply(A,v,n)==apply(T,v,n) for A in E) for v in vecs)

def identity_bits(n):
    return sum(1 << (i*n+i) for i in range(n))

# The explicit three-dimensional space E in M_3(F_2).
A = 1 << 3
B = (1 << 0) | (1 << 4) | (1 << 5)
C = (1 << 4) | (1 << 8)
E = span([A,B,C])
assert len(E)==8

# Every member is singular.
assert all(rank2(mat_bits(T,3)) < 3 for T in E)

# Exact reflexive hull by direct definition.
Ref = frozenset(T for T in range(1<<9) if ref_contains(E,T,3))
I = identity_bits(3)
assert Ref == E | frozenset(T ^ I for T in E)
assert len(Ref)==16
inv_ref = sorted(T for T in Ref if rank2(mat_bits(T,3))==3)
assert inv_ref == sorted([I, I ^ A])
assert I in Ref and I not in E

# Sharpness over F_2 in ambient dimensions 1 and 2:
# exhaust every linear subspace of End(F_2^n).
counts={}
for n in (1,2):
    subs=all_subspaces(n*n)
    bad=[]
    I_n=identity_bits(n)
    for S in subs:
        if ref_contains(S,I_n,n) and all(rank2(mat_bits(T,n))<n for T in S):
            bad.append(S)
    counts[n]=(len(subs),len(bad))
    assert not bad

print("VERIFY_OK")
print("E_size=8")
print("Ref_size=16")
print("Ref_invertibles=2")
print("ambient_n1_subspaces=%d counterexamples=%d" % counts[1])
print("ambient_n2_subspaces=%d counterexamples=%d" % counts[2])
