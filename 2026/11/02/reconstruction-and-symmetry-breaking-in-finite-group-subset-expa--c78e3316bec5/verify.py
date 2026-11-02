#!/usr/bin/env python3
"""Independent finite checks for symmetries of Boolean and pointed group subset expansions."""
import itertools


def cyclic(n):
    return [[(i + j) % n for j in range(n)] for i in range(n)], 0


def klein():
    return [[i ^ j for j in range(4)] for i in range(4)], 0


def symmetric3():
    perms = list(itertools.permutations(range(3)))
    pos = {p: i for i, p in enumerate(perms)}
    mul = [[pos[tuple(p[q[t]] for t in range(3))] for q in perms] for p in perms]
    return mul, pos[(0, 1, 2)]


def aut_group(mul, e):
    n = len(mul)
    tail = [i for i in range(n) if i != e]
    for b in itertools.permutations(tail):
        p = list(range(n))
        p[e] = e
        for x,y in zip(tail,b):p[x]=y
        if all(p[mul[i][j]] == mul[p[i]][p[j]] for i in range(n) for j in range(n)):
            yield tuple(p)


def expansion(mul, e, pointed=False):
    n=len(mul)
    el=[]
    for mask in range(1 << n):
        for g in range(n):
            if not pointed or ((mask >> e)&1 and (mask >> g)&1):
                el.append((mask,g))
    pos={v:i for i,v in enumerate(el)}
    table=[]
    for a,g in el:
        row=[]
        for b,h in el:
            gb=0
            for i in range(n):
                if (b>>i)&1:gb|=1 << mul[g][i]
            row.append(pos[(a|gb,mul[g][h])])
        table.append(row)
    return el,pos,table


def induced_map(mul,e,el,pos,phi,t=None):
    n=len(mul)
    if t is None:t=e
    perm=[]
    for a,g in el:
        mask=0
        for x in range(n):
            if (a >> x)&1:mask|=1 << mul[phi[x]][t]
        perm.append(pos[(mask,phi[g])])
    return tuple(perm)


def respects(table,p):
    n=len(table)
    return all(p[table[i][j]] == table[p[i]][p[j]] for i in range(n) for j in range(n))


def brute_aut_count(table):
    n=len(table)
    assert n <= 8
    return sum(1 for p in itertools.permutations(range(n)) if respects(table,p))


def run():
    examples=[('C1', cyclic(1)),('C2', cyclic(2)),('C3', cyclic(3)),
              ('C4', cyclic(4)),('V4', klein()),('S3', symmetric3())]
    totals=[]
    for name,(mul,e) in examples:
        aps=list(aut_group(mul,e))
        n=len(mul)
        for pointed in [False,True]:
            el,pos,tab=expansion(mul,e,pointed)
            perms={induced_map(mul,e,el,pos,p,t)
                   for p in aps for t in ([e] if pointed else range(n))}
            assert len(perms) == len(aps)*(1 if pointed else n), (name,pointed)
            assert all(respects(tab,p) for p in perms), (name,pointed)
            if len(el)<=8:
                count=brute_aut_count(tab)
                assert count==len(perms), (name,pointed,count,len(perms))
            totals.append((name,'pointed' if pointed else 'full',len(el),len(perms)))
    for name,(mul,e) in examples:
        n=len(mul)
        el,pos,tab=expansion(mul,e,False)
        aps=list(aut_group(mul,e))
        # Inner conjugations by units are precisely the images of left translations.
        for t in range(n):
            unit=pos[(0,t)]
            tinv=next(x for x in range(n) if mul[t][x]==e and mul[x][t]==e)
            inverse_unit=pos[(0,tinv)]
            direct=tuple(tab[tab[unit][a]][inverse_unit] for a in range(len(el)))
            adt=tuple(mul[mul[t][x]][tinv] for x in range(n))
            assert direct==induced_map(mul,e,el,pos,adt,t),name
        # The distinct copies of the pointed expansion are indexed by the
        # singleton identity support to which each automorphism sends {e}.
        orbital=[]
        for t in range(n):
            itemset={i for i,(mask,g) in enumerate(el)
                     if (mask>>t)&1 and (mask>>mul[g][t])&1}
            orbital.append(frozenset(itemset))
        assert len(set(orbital))==n,name
        base=orbital[e]
        assert all(frozenset(p[i] for i in base)==orbital[t]
                   for t in range(n) for phi in aps
                   for p in [induced_map(mul,e,el,pos,phi,t)]),name
    for x in totals:print(*x,sep=' | ')
    print('VERIFY_OK')

if __name__=='__main__':run()
