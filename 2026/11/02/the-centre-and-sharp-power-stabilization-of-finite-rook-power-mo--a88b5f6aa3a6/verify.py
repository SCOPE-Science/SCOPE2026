"""Exact finite checks of the centre formula for power monoids of rook monoids.
No external dependencies. Run: python verify.py
"""
from itertools import combinations, permutations


def monoid(n):
    elems=[]
    for k in range(n+1):
        for domain in combinations(range(n),k):
            for image in permutations(range(n),k):
                f=[-1]*n
                for x,y in zip(domain,image):
                    f[x]=y
                elems.append(tuple(f))
    return elems


def compose(f,g):
    """Apply f then g."""
    return tuple(g[f[x]] if f[x] >= 0 else -1 for x in range(len(f)))


def rank_idempotent_blocks(elems):
    n=len(elems[0])
    return [frozenset(i for i,f in enumerate(elems)
            if sum(y>=0 for y in f)==k and all(y<0 or y==x for x,y in enumerate(f)))
            for k in range(n+1)]


def rank_product(n,A,B):
    return frozenset(t for a in A for b in B
            for t in range(max(0,a+b-n),min(a,b)+1))


def direct_center_checks(n, exhaustive=False):
    elems=monoid(n)
    ix={a:i for i,a in enumerate(elems)}
    mult=[[ix[compose(a,b)] for b in elems] for a in elems]
    blocks=rank_idempotent_blocks(elems)
    assert len(elems)==sum(__import__('math').comb(n,k)**2*__import__('math').factorial(k) for k in range(n+1))
    actual_centers=[]
    candidates=[]
    for mask in range(1,1<<(n+1)):
        bits=[r for r in range(n+1) if mask>>r&1]
        A=frozenset().union(*(blocks[r] for r in bits))
        assert all({mult[a][b] for a in A}=={mult[b][a] for a in A} for b in range(len(elems)))
        candidates.append(A)
    assert len(candidates)==2**(n+1)-1
    if exhaustive:
        for mask in range(1,1<<len(elems)):
            A=[i for i in range(len(elems)) if mask>>i&1]
            if all({mult[a][b] for a in A}=={mult[b][a] for a in A} for b in range(len(elems))):
                actual_centers.append(frozenset(A))
        assert set(actual_centers)==set(candidates)
    # Compare direct product against all products of rank-index descriptions.
    for maskA in range(1,1<<(n+1)):
        rA=[r for r in range(n+1) if maskA>>r&1]
        A=frozenset().union(*(blocks[r] for r in rA))
        for maskB in range(1,1<<(n+1)):
            rB=[r for r in range(n+1) if maskB>>r&1]
            B=frozenset().union(*(blocks[r] for r in rB))
            expect=frozenset().union(*(blocks[r] for r in rank_product(n,rA,rB)))
            direct=frozenset(mult[a][b] for a in A for b in B)
            assert direct==expect
    idem=sum(rank_product(n,[r for r in range(n+1) if mask>>r&1],[r for r in range(n+1) if mask>>r&1])==
             frozenset(r for r in range(n+1) if mask>>r&1) for mask in range(1,1<<(n+1)))
    assert idem==2*n+1
    for mask in range(1,1<<(n+1)):
        A=frozenset(r for r in range(n+1) if mask>>r&1)
        power=A
        for _ in range(1,n):
            power=rank_product(n,power,A)
        assert rank_product(n,power,A)==power
    if n>=2:
        A=frozenset([n-1]); power=A
        for _ in range(1,n-1):
            power=rank_product(n,power,A)
        assert rank_product(n,power,A)!=power
    print(f'n={n}: elements={len(elems)}, central_candidates={len(candidates)}, '
          f'central_idempotents={idem}, exponent={n}, exhaustive={exhaustive}, verified')


def arithmetic_checks(nmax=9):
    for n in range(1,nmax+1):
        sets=[frozenset(r for r in range(n+1) if mask>>r&1)
              for mask in range(1,1<<(n+1))]
        assert len(sets)==2**(n+1)-1
        assert sum(rank_product(n,A,A)==A for A in sets)==2*n+1
        for A in sets:
            P=A
            for _ in range(1,n):
                P=rank_product(n,P,A)
            assert rank_product(n,P,A)==P
        if n>1:
            A=frozenset([n-1]); P=A
            for _ in range(1,n-1):
                P=rank_product(n,P,A)
            assert rank_product(n,P,A)!=P
    print(f'rank-index exact arithmetic verified for n=1..{nmax}')


if __name__=='__main__':
    direct_center_checks(1,exhaustive=True)
    direct_center_checks(2,exhaustive=True)
    direct_center_checks(3,exhaustive=False)
    arithmetic_checks()
    print('VERIFY_OK')
