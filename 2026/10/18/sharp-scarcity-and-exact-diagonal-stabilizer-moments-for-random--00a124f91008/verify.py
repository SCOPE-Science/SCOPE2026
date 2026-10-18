"""Independent small-field checks for diagonal automorphisms of perfect evolution algebras.

Run: python verify.py
The exhaustive tests form independent finite witnesses, not a proof of asymptotics.
"""
from itertools import product, permutations
from math import factorial, prod, comb, gcd


def field(q):
    if q in (4,8):
        add = lambda a, b: a ^ b
        deg = {4:2,8:3}[q]
        poly = {4:7,8:11}[q]
        def mul(a,b):
            v = 0
            for j in range(deg):
                if (b >> j)&1: v ^= a << j
            while v >=q:
                v ^= poly << (v.bit_length()-deg-1)
            return v
    else:
        add = lambda a,b:(a+b)%q
        mul = lambda a,b:(a*b)%q
    return add,mul


def det(M,q,add,mul):
    n = len(M)
    def sign_product(a,perm):
        v=1
        for i in range(n): v=mul(v,a[i][perm[i]])
        return v
    res=0
    for perm in permutations(range(n)):
        y=sign_product(M,perm)
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        if inv%2:
            y=(-y)%q if q not in (4,8) else y
        res=add(res,y)
    return res


def gl(k,q):
    return prod(q**k-q**i for i in range(k))


def square_orbits(q,mul):
    seen={1}; ans=[]
    for a in range(2,q):
        if a in seen:continue
        cur=a; seq=[]
        while cur not in seen and cur not in seq:
            seq.append(cur); cur=mul(cur,cur)
        if cur==a:
            ans.append(tuple(seq));seen.update(seq)
        # Other elements outside cycles cannot occur in invertible stabilized matrices.
    return ans


def formula_fixedsum(n,q,mul):
    cycles=square_orbits(q,mul)
    total=0
    def search(i, rem, den, factor):
        nonlocal total
        if i==len(cycles):
            s=n-rem
            total+=factorial(n)//(factorial(rem)*den)*factor*gl(rem,q)
            return
        l=len(cycles[i]);m=0
        while m*l<=rem:
            search(i+1,rem-m*l,den*factorial(m)**l,factor*gl(m,q)**l)
            m+=1
    search(0,n,1,1)
    return total


def brute(q,n):
    add,mul=field(q)
    scalars=list(range(1,q))
    diagonals=list(product(scalars,repeat=n))
    sq=[tuple(mul(t,t) for t in d) for d in diagonals]
    invertible=0;fixedsum=0; nontrivial=0
    dist={}
    for entries in product(range(q),repeat=n*n):
        M=[entries[i*n:(i+1)*n] for i in range(n)]
        if det(M,q,add,mul)==0:continue
        invertible+=1
        nn=0
        for d,dsq in zip(diagonals,sq):
            if all(M[i][j]==0 or d[j]==dsq[i] for i in range(n) for j in range(n)):
                nn+=1
        dist[nn]=dist.get(nn,0)+1
        fixedsum+=nn
        if nn>1:nontrivial+=1
    assert invertible==gl(n,q),(q,n,invertible,gl(n,q))
    assert fixedsum==formula_fixedsum(n,q,mul),(q,n,fixedsum,formula_fixedsum(n,q,mul))
    print(f'q={q} n={n} GL={invertible} sum_diagonal_group_sizes={fixedsum} nontrivial={nontrivial} distribution={dict(sorted(dist.items()))}')
    if (q,n) in [(4,2),(4,3),(7,2)]:
        r=2
        expected=comb(n,r)*factorial(r-1)*(q-1)**r*gl(n-r,q)
        assert nontrivial==expected,(q,n,nontrivial,expected)
    if q in (2,3,5): assert nontrivial==0

if __name__=='__main__':
    for q,n in [(2,3),(3,3),(4,2),(4,3),(5,2),(7,2)]:
        brute(q,n)
    add,mul=field(8)
    M=((0,1,0),(0,0,1),(1,0,0))
    assert det(M,8,add,mul)!=0
    # The smallest allowed squaring orbit for F_8 has length 3; its cycle realizes all 7 scalings.
    scalings=[d for d in product(range(1,8),repeat=3) if all(M[i][j]==0 or d[j]==mul(d[i],d[i]) for i in range(3) for j in range(3))]
    assert len(scalings)==7
    assert all(not any(d!=tuple([1,1]) for d in product(range(1,8),repeat=2) if all(P[i][j]==0 or d[j]==mul(d[i],d[i]) for i in range(2) for j in range(2))) for P in [((1,0),(0,1)),((0,1),(1,0))])
    print('q=8 n=3 cyclic witness has 7 diagonal symmetries; dimension-2 witnesses have 1')
    print('VERIFY_OK: six exhaustive finite-field GL ensembles, fixed-group moment and rarity counts plus F_8 witness')
