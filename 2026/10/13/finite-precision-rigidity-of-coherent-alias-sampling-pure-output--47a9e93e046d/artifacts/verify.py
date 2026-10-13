"""Independent finite verification of the b-bit retained-garbage alias theorem."""
from itertools import product
from fractions import Fraction


def actual_gram(alias, keep, B):
    """Trace the explicitly enumerated compare/swap branches by garbage key."""
    L=len(alias)
    garbage={}
    for j in range(L):
        for sigma in range(B):
            flag=int(sigma>=keep[j])
            address=alias[j] if flag else j
            other=j if flag else alias[j]
            key=(other,keep[j],sigma,flag)
            vector=garbage.setdefault(key,[0]*L)
            vector[address]+=1
    gram=[[0]*L for _ in range(L)]
    for vec in garbage.values():
        for i in range(L):
            for k in range(L):
                gram[i][k]+=vec[i]*vec[k]
    return gram


def formula_gram(alias,keep,B):
    L=len(alias)
    result=[[0]*L for _ in range(L)]
    groups={}
    for j,(a,t) in enumerate(zip(alias,keep)):
        result[a][a]+=B-t
        groups.setdefault((a,t),[]).append(j)
    for (a,t),fiber in groups.items():
        for i in fiber:
            for k in fiber:
                result[i][k]+=t
    return result


def rank_one_psd_integer(A):
    # A is positive semidefinite with positive trace. Rank one iff every
    # principal 2x2 minor vanishes; for a positive Gram matrix this is exact.
    L=len(A)
    return all(A[i][i]*A[j][j]==A[i][j]*A[j][i]
               for i in range(L) for j in range(i+1,L))


def criterion_pure(alias,keep):
    return any(all(a==c for a in alias)
               and all(keep[j]==0 for j in range(len(alias)) if j!=c)
               for c in range(len(alias)))


def criterion_uniform(alias,keep):
    L=len(alias)
    return sorted(alias)==list(range(L)) and all(keep[j]==keep[alias[j]] for j in range(L))


def check(L,B):
    count=0
    for alias in product(range(L),repeat=L):
        for keep in product(range(B),repeat=L):
            A=actual_gram(alias,keep,B)
            assert A==formula_gram(alias,keep,B)
            assert sum(A[i][i] for i in range(L))==L*B
            pure=rank_one_psd_integer(A)
            assert pure==criterion_pure(alias,keep)
            uniform=all(A[i][i]==B for i in range(L))
            assert uniform==criterion_uniform(alias,keep)
            if uniform:
                assert all(A[i][j]==(B if i==j else 0)
                           for i in range(L) for j in range(L))
                # Exact fidelity to coherent uniform target: sum(A)/(L^2 B)
                # and trace distance from I/L to pure uniform = 1-1/L.
                assert sum(map(sum,A))==L*B
                assert Fraction(sum(map(sum,A)),L*L*B)==Fraction(1,L)
            count+=1
    return count

# Strict b-bit cases, with L and B true powers of two.
checks=check(2,2)+check(2,4)+check(4,2)+check(4,4)
assert checks>0

# A full-keep value B is outside the specified b-bit convention.
# With all thresholds equal B and all aliases identical, every input is
# unexchanged, all garbage keys coincide, and the address is pure |+>.
L,B=4,4
outside=actual_gram((0,)*L,(B,)*L,B)
assert outside==[[B]*L for _ in range(L)]
assert rank_one_psd_integer(outside)

# Some nonuniform tables can have nonzero off-diagonal coherence;
# the all-table claim does NOT assert that every result is diagonal.
assert any(actual_gram((0,0),(1,1),2)[i][j]>0 for i in range(2) for j in range(2) if i!=j)
print('VERIFY_OK',checks)
