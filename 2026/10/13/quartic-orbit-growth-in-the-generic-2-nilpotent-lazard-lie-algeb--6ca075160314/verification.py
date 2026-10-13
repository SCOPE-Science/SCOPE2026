from itertools import combinations, product
from math import comb


def gaussian_binom(n,k,q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num *= q**(n-i)-1
        den *= q**(k-i)-1
    return num//den


def galois(n,q):
    return sum(gaussian_binom(n,k,q) for k in range(n+1))


def rref_subspaces(n,q):
    """Enumerate each subspace of F_q^n once, as an RREF row basis."""
    yield tuple()
    for r in range(1,n+1):
        for pivots in combinations(range(n),r):
            pivot_set = set(pivots)
            free_positions=[]
            for i,p in enumerate(pivots):
                for j in range(p+1,n):
                    if j not in pivot_set:
                        free_positions.append((i,j))
            for vals in product(range(q), repeat=len(free_positions)):
                rows=[[0]*n for _ in range(r)]
                for i,p in enumerate(pivots):
                    rows[i][p]=1
                for (i,j),v in zip(free_positions, vals):
                    rows[i][j]=v
                yield tuple(tuple(row) for row in rows)


def reduce_mod(v, basis, q):
    v=list(v)
    for row in basis:
        p=next(i for i,x in enumerate(row) if x%q)
        c=v[p]%q
        if c:
            v=[(x-c*y)%q for x,y in zip(v,row)]
    return tuple(v)


def signature_from_kernel(m, K, q):
    sig=[]
    for j in range(m):
        e=[0]*m; e[j]=1
        sig.append(reduce_mod(e,K,q))
    return tuple(sig)

checks=0
# Independent enumeration of all subspaces for modest dimensions.
for q,maxn in [(2,6),(3,4)]:
    for n in range(maxn+1):
        count=sum(1 for _ in rref_subspaces(n,q))
        assert count == galois(n,q), (q,n,count,galois(n,q))
        checks += 1

# Kernel/signature classification on exterior-square dimensions for n<=4 over F2.
for n in range(1,5):
    m=comb(n,2)
    sigs=set()
    kernels=0
    for K in rref_subspaces(m,2):
        kernels += 1
        sig=signature_from_kernel(m,K,2)
        sigs.add(sig)
        # recover K by testing which ambient vectors map to 0 in the quotient
        recovered=[]
        for v in product(range(2), repeat=m):
            image=[0]*m
            for coeff, basis_image in zip(v, sig):
                if coeff:
                    image=[(x+coeff*y)%2 for x,y in zip(image,basis_image)]
            if tuple(image)==(0,)*m:
                recovered.append(v)
        expected=[v for v in product(range(2), repeat=m) if reduce_mod(v,K,2)==(0,)*m]
        assert recovered==expected
    assert kernels==galois(m,2)
    assert len(sigs)==kernels
    checks += 3

# Elementary asymptotic bounds used in the proof.
for q in (2,3,4,5):
    for s in range(1,25):
        G=galois(s,q)
        lo=q**(s*s//4)
        hi=(s+1)*q**(s*s//4+s)
        assert lo <= G <= hi, (q,s,G,lo,hi)
        checks += 1

print('q=2 natural-stratum counts n=1..6:', [galois(comb(n,2),2) for n in range(1,7)])
print('q=3 natural-stratum counts n=1..5:', [galois(comb(n,2),3) for n in range(1,6)])
print('checks:', checks)
print('VERIFY_OK')
