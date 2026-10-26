#!/usr/bin/env python3
"""Direct finite-group tests for a derived-conjugacy medial quotient."""
from itertools import permutations, product
from math import gcd, factorial


def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
    v=[0]*len(a)
    for i,x in enumerate(a): v[x]=i
    return tuple(v)
def conj(x,y): return compose(compose(inverse(y),x),y)
def sign(a):
    count=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    return -1 if count%2 else 1

def quotient_orbits(elements, subgroup):
    pending=set(elements); blocks=[]
    while pending:
        x=next(iter(pending)); orbit={conj(x,h) for h in subgroup}
        assert orbit<=pending
        pending-=orbit; blocks.append(tuple(sorted(orbit)))
    return blocks

def check_medial(elements, blocks):
    classes={x:i for i,b in enumerate(blocks) for x in b}
    reps=[b[0] for b in blocks]; m=len(reps)
    tab=[[classes[conj(a,b)] for b in reps] for a in reps]
    for i,bi in enumerate(blocks):
        for j,bj in enumerate(blocks):
            answer=tab[i][j]
            for a in bi:
                for b in bj: assert classes[conj(a,b)]==answer
    for a,b,c,d in product(range(m),repeat=4):
        assert tab[tab[a][b]][tab[c][d]]==tab[tab[a][c]][tab[b][d]]
    return m

def partitions(n,max_part=None):
    if n==0:yield ()
    else:
        hi=n if max_part is None else min(n,max_part)
        for i in range(hi,0,-1):
            for tail in partitions(n-i,i):yield (i,)+tail

def check_automorphisms(elements,blocks):
    """Exhaustively count automorphisms of tiny quotient quandles."""
    idx={x:i for i,b in enumerate(blocks) for x in b}
    reps=[b[0] for b in blocks]
    tab=[[idx[conj(a,b)] for b in reps] for a in reps]
    count=0
    for perm in permutations(range(len(blocks))):
        if all(perm[tab[i][j]]==tab[perm[i]][perm[j]] for i in range(len(blocks)) for j in range(len(blocks))):
            count+=1
    return count

def symmetric_tests():
    rows=[]
    for n in range(2,7):
        group=list(permutations(range(n)))
        subgroup=[p for p in group if sign(p)==1]
        blocks=quotient_orbits(group,subgroup)
        p=sum(1 for _ in partitions(n))
        q=sum(1 for part in partitions(n) if all(x%2 for x in part) and len(part)==len(set(part)))
        assert len(blocks)==p+q,(n,len(blocks),p,q)
        assert check_medial(group,blocks)==p+q
        odd=sum(1 for lam in partitions(n) if (n-len(lam))%2==1)
        even_nonsplit=p-q-odd
        expected_aut=(2**q)*factorial(q)*factorial(odd)*factorial(even_nonsplit)
        if 3<=n<=5:
            assert check_automorphisms(group,blocks)==expected_aut,(n,expected_aut)
        rows.append((n,p,q,p+q,expected_aut))
    print('SYMMETRIC_OK',rows)

def dihedral(n):
    # (a,e) represents r^a s^e, s r s = r^-1.
    def mul(x,y):return ((x[0]+(-1 if x[1] else 1)*y[0])%n,x[1]^y[1])
    def inv(x):return ((-x[0] if not x[1] else x[0])%n,x[1])
    def cnj(x,y):return mul(mul(inv(y),x),y)
    group=list(product(range(n),range(2)))
    subgroup=[(2*j%n,0) for j in range(n)]
    blocks=[]; pending=set(group)
    while pending:
        v=next(iter(pending)); orbit={cnj(v,h) for h in subgroup}
        assert orbit<=pending
        pending-=orbit;blocks.append(tuple(sorted(orbit)))
    idx={x:i for i,b in enumerate(blocks) for x in b}
    reps=[b[0] for b in blocks]
    tab=[[idx[cnj(a,b)] for b in reps] for a in reps]
    for a,b in product(group,repeat=2):assert idx[cnj(a,b)]==tab[idx[a]][idx[b]]
    for a,b,c,d in product(range(len(blocks)),repeat=4):
        assert tab[tab[a][b]][tab[c][d]]==tab[tab[a][c]][tab[b][d]]
    assert len(blocks)==n+gcd(n,4)
    # Complete explicit operation on m rotation singleton orbits and g
    # reflection orbits. The latter are indexed by the exponent modulo g.
    g=gcd(n,4)
    for i in range(n):
        for b in range(n):
            assert idx[cnj((i,0),(b,0))]==idx[(i,0)]
        for j in range(g):
            assert idx[cnj((i,0),(j,1))]==idx[((-i)%n,0)]
    for j in range(g):
        for b in range(n):
            assert idx[cnj((j,1),(b,0))]==idx[((j-2*b)%n,1)]
        for k in range(g):
            assert idx[cnj((j,1),(k,1))]==idx[((2*k-j)%n,1)]
    assert sum(len(b)==1 for b in blocks)==n+(n if n==4 else 0) # for n>=3 only n=4 has fixed reflections
    return len(blocks)

def main():
    symmetric_tests()
    rows=[]
    for n in range(3,17):
        rows.append((n,dihedral(n)))
    print('DIHEDRAL_OK',rows)
    print('VERIFY_OK')
if __name__=='__main__':main()
