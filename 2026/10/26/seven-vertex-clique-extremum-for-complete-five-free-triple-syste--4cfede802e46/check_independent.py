"""Independent elementary enumeration and shape test for seven-vertex triple systems."""
from itertools import combinations
from math import comb
U=set(range(7))
tri=list(combinations(range(7),3))
four=list(combinations(range(7),4))
five=list(combinations(range(7),5))
# Dictionary of four- and five-set incidence masks, independently built.
sh4={tuple(x):sum(1<<j for j,q in enumerate(four) if set(x)<=set(q)) for x in tri}
sh5={tuple(x):sum(1<<j for j,q in enumerate(five) if set(x)<=set(q)) for x in tri}
assert sum(len([q for q in four if set(tri[0])<=set(q)]) for _ in range(1))==4

def statistics(family):
    q4=q5=0
    for t in family:
        q4|=sh4[t];q5|=sh5[t]
    return q4.bit_count(),q5.bit_count()==len(five)

# Exhaust every normalized family through seven missing triples.
min_score=10**9; winners=[]; covering_by_size={}
for k in range(1,8):
    covered=0
    for rest in combinations(tri[1:],k-1):
        family=(tri[0],)+rest
        shadow,is_cover=statistics(family)
        if not is_cover:continue
        covered+=1
        score=k+shadow
        if score<min_score: min_score=score;winners=[]
        if score==min_score:winners.append(family)
    covering_by_size[k]=covered
assert min_score==22
assert len(winners)==5
assert covering_by_size=={1:0,2:0,3:0,4:0,5:245,6:15300,7:235992}

def bipartite_family(A):
    B=U-set(A)
    return frozenset(t for t in tri if set(t)<=set(A) or set(t)<=B)
expect={bipartite_family(A) for A in combinations(range(7),3) if tri[0] in bipartite_family(A)}
assert {frozenset(fam) for fam in winners}==expect
assert len({bipartite_family(A) for A in combinations(range(7),3)})==35
for A in combinations(range(7),3):
    fam=bipartite_family(A)
    shadow,cover=statistics(fam)
    assert len(fam)==5 and cover and 99-len(fam)-shadow==77
print('PYTHON_CHECK_OK', 'normalized_optima',len(winners),'all_bipartite_templates',35,'score',min_score)
