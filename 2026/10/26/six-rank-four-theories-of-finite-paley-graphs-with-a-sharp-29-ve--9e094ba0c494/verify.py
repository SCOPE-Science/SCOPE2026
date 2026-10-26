#!/usr/bin/env python3
"""Exact rank-four Paley graph types and explicit separation certificates.

All arithmetic is in Z/pZ or (Z/pZ)[u]/(u*u-2), with p=3 or 5
in the quadratic cases. No third-party modules required.
"""
from itertools import combinations, product, permutations

ORDERS = (5, 9, 13, 17, 25, 29)


def graph(q):
    if q in (9,25):
        p = 3 if q==9 else 5
        elements = [(a,b) for a in range(p) for b in range(p)]
        index = {t:i for i,t in enumerate(elements)}
        def add(x,y):
            a,b=elements[x];c,d=elements[y]
            return index[((a+c)%p,(b+d)%p)]
        def neg(x):
            a,b=elements[x]
            return index[((-a)%p,(-b)%p)]
        def mul(x,y):
            a,b=elements[x];c,d=elements[y]
            return index[((a*c+2*b*d)%p,(a*d+b*c)%p)]
    else:
        p=q
        def add(x,y):return (x+y)%p
        def neg(x):return (-x)%p
        def mul(x,y):return (x*y)%p
    zero=0
    squares={mul(a,a) for a in range(q) if a!=zero}
    adj=tuple(tuple(int(x!=y and add(x,neg(y)) in squares) for y in range(q)) for x in range(q))
    assert len(squares)==(q-1)//2
    assert all(adj[x][y]==adj[y][x] for x in range(q) for y in range(q))
    return adj


def rank_four_type(a):
    """Exact recursive logical rank (4-k) types of ordered k-tuples.

    For a tuple, its atomic diagram and the set of types of one-point
    extensions determine every remaining first-order formula; this is
    an exact finite-structure recurrence, not a sample of formulas.
    """
    n=len(a)
    typ3={}
    for x,y,z in product(range(n),repeat=3):
        t=(x,y,z)
        atomic=(x==y,x==z,y==z,a[x][y],a[x][z],a[y][z])
        mask=0
        for w in range(n):
            if w in t:continue
            mask |=1<<(a[w][x]+2*a[w][y]+4*a[w][z])
        typ3[t]=(atomic,mask)
    typ2={}
    for x,y in product(range(n),repeat=2):
        typ2[(x,y)]=((x==y,a[x][y]),frozenset(typ3[(x,y,z)] for z in range(n)))
    typ1={x:frozenset(typ2[(x,y)] for y in range(n)) for x in range(n)}
    return frozenset(typ1.values())


def three_ec(a):
    n=len(a)
    for x,y,z in combinations(range(n),3):
        seen=0
        for w in range(n):
            if w in (x,y,z):continue
            seen |= 1 << (a[w][x]+2*a[w][y]+4*a[w][z])
        if seen!=255:return False
    return True


def test_formulas(a):
    n=len(a)
    T=D=U=K=False
    for x,y,z in combinations(range(n),3):
        edge_count=a[x][y]+a[x][z]+a[y][z]
        if edge_count==3:T=True
        if edge_count==1:
            if not any(w not in (x,y,z) and not (a[w][x] or a[w][y] or a[w][z]) for w in range(n)):
                U=True
    for x,y,z,w in combinations(range(n),4):
        e=sum(a[u][v] for u,v in combinations((x,y,z,w),2))
        if e==5:D=True
        if e==6:K=True
    return (T,D,U,K,three_ec(a))


def c_tables():
    for q in (13,17):
        a=graph(q)
        candidates=[c for c in range(2,q) if not a[c][0] and not a[c][1]]
        counts={c:sum(not(a[w][0] or a[w][1] or a[w][c]) for w in range(q) if w not in (0,1,c)) for c in candidates}
        print('ONE_EDGE',q,counts)
        assert counts==({6:1,7:0,8:1} if q==13 else {6:2,7:1,11:1,12:2})
    # In F_25 our indexing is a*5+b for a+b*u and u*u=2.
    a=graph(25)
    assert all(a[u][v] for u,v in combinations((0,5,10,15),2))
    assert a[0][5] and a[0][17] and a[5][17]
    assert all(not (a[w][0] and a[w][5] and a[w][17]) for w in range(25) if w not in (0,5,17))
    a=graph(13)
    assert a[0][1] and a[0][4] and a[0][10] and a[1][4] and a[1][10] and not a[4][10]
    print('DIRECT_CERTIFICATES_OK')


def induced_four_age(a):
    # Canonical adjacency bitmask under all 24 relabellings of four vertices.
    reps=set()
    for vertices in combinations(range(len(a)),4):
        best=min(sum(a[vertices[perm[i]]][vertices[perm[j]]] << k
                     for k,(i,j) in enumerate(combinations(range(4),2)))
                 for perm in permutations(range(4)))
        reps.add(best)
    return frozenset(reps)


def main():
    c_tables()
    matrices={q:graph(q) for q in ORDERS}
    types={q:rank_four_type(a) for q,a in matrices.items()}
    assert len(set(types.values()))==6
    expected={
        5:(False,False,True,False,False),
        9:(True,False,True,False,False),
        13:(True,True,True,False,False),
        17:(True,True,False,False,False),
        25:(True,True,False,True,False),
        29:(True,True,False,True,True),
    }
    for q,a in matrices.items():
        actual=test_formulas(a)
        print('PAL',q,'rank4type_distinct=',sum(types[q]!=types[t] for t in ORDERS),'bits=', ''.join(map(lambda b:str(int(b)),actual)))
        assert actual==expected[q]
    ages={q:induced_four_age(matrices[q]) for q in (13,17,25,29)}
    assert ages[13]==ages[17] and ages[25]==ages[29]
    print('FOUR_AGES_OK', len(ages[13]), len(ages[25]))
    assert three_ec(matrices[29])
    print('VERIFY_OK six_rank_four_classes=True optimal_representative_order=29')


if __name__=='__main__':main()
