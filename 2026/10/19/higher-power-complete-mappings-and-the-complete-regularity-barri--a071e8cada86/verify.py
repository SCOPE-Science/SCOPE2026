"""Exhaustive finite checks of higher-power complete mappings (stdlib only)."""
from itertools import permutations, product
from math import gcd

def group_table(moduli):
    elems=list(product(*(range(m) for m in moduli)))
    idx={v:i for i,v in enumerate(elems)}
    return [[idx[tuple((x+y)%m for x,y,m in zip(a,b,moduli))]
             for b in elems] for a in elems]

def brandt2():
    # Zero plus matrix units (i,j), i,j in {0,1}.
    elems=[None]+list(product(range(2),repeat=2))
    table=[]
    for a in elems:
        row=[]
        for b in elems:
            z=(a[0],b[1]) if a is not None and b is not None and a[1]==b[0] else None
            row.append(elems.index(z))
        table.append(row)
    return table

def inv2():
    # Empty, four rank-one partial bijections, identity and swap.
    maps=[(-1,-1)]+[(j,-1) for j in (0,1)]+[(-1,j) for j in (0,1)]+[(0,1),(1,0)]
    def compose(a,b):
        return tuple(-1 if b[i]==-1 else a[b[i]] for i in range(2))
    return [[maps.index(compose(a,b)) for b in maps] for a in maps]

def zero_extension(tab):
    n=len(tab)
    return [[0]*(n+1)]+[[0]+[1+v for v in row] for row in tab]

def check_associative(tab):
    n=len(tab)
    assert all(tab[tab[a][b]][c]==tab[a][tab[b][c]]
               for a in range(n) for b in range(n) for c in range(n))

def count_kcomplete(tab,k):
    n=len(tab)
    powk=[]
    for x in range(n):
        y=x
        for _ in range(k-1):
            y=tab[y][x]
        powk.append(y)
    count=0
    for p in permutations(range(n)):
        seen=0
        for x in range(n):
            y=tab[x][powk[p[x]]]
            bit=1<<y
            if seen & bit:
                break
            seen |=bit
        else:
            count+=1
    return count

def cyclic_sylow2_not_singleton(moduli):
    # For products of cyclic groups, 2-Sylow is cyclic iff
    # exactly one factor has even order (nontrivial case).
    return sum(m%2==0 for m in moduli)!=1

cases=[('C2',(2,)),('C3',(3,)),('C4',(4,)),('C5',(5,)),
       ('C6',(6,)),('V4',(2,2)),('C2xC4',(2,4)),
       ('C3xC3',(3,3))]
run_count=0
for name,mods in cases:
    tab=group_table(mods)
    check_associative(tab)
    for k in (2,3,4):
        if len(tab)>6 and k==4:
            continue
        actual=count_kcomplete(tab,k)>0
        expected=(k%2==0 or cyclic_sylow2_not_singleton(mods))
        assert actual==expected,(name,k,actual,expected)
        run_count+=1
for name,tab,clifford,mods in [
    ('Brandt2',brandt2(),False,None),
    ('I2',inv2(),False,None),
    ('C2+zero',zero_extension(group_table((2,))),True,(2,)),
    ('C3+zero',zero_extension(group_table((3,))),True,(3,)),
    ('V4+zero',zero_extension(group_table((2,2))),True,(2,2))
]:
    check_associative(tab)
    for k in (2,3,4):
        if len(tab)>5 and k==4:
            continue
        actual=count_kcomplete(tab,k)>0
        expected=bool(clifford and (k%2==0 or cyclic_sylow2_not_singleton(mods)))
        assert actual==expected,(name,k,actual,expected)
        run_count+=1
# General finite-semigroup boundary: completely regular rectangular bands pass;
# a nilpotent two-element semigroup does not.
for name,tab,expected in [
    ('rectangular-band-2x2',[[2*(a//2)+(b%2) for b in range(4)] for a in range(4)],True),
    ('left-zero-3',[[a for b in range(3)] for a in range(3)],True),
    ('nilpotent-pair',[[0,0],[0,0]],False)
]:
    check_associative(tab)
    for k in (2,3):
        actual=count_kcomplete(tab,k)>0
        assert actual==expected,(name,k,actual,expected)
        run_count+=1
# The ordinary complete-mapping case can differ sharply at k=1.
assert count_kcomplete(brandt2(),1)>0 and count_kcomplete(brandt2(),2)==0
print('VERIFY_OK',run_count,'exhaustive semigroup/exponent tests; Brandt k=1 contrast')
