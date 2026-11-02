"""Separate symplectic representation and exhaustive Bron--Kerbosch strong-matching census."""
from collections import Counter
from itertools import combinations

points = tuple(range(1, 16))
def skew(x,y):
    return ((x&1 != 0) * (y&2 != 0) + (x&2 != 0) * (y&1 != 0)
            + (x&4 != 0) * (y&8 != 0) + (x&8 != 0) * (y&4 != 0))%2
lines = tuple(sorted({frozenset((x,y,x^y)) for x in points for y in points
                      if x!=y and skew(x,y)==0}, key=lambda s:tuple(sorted(s))))
assert len(lines)==15
flags = [(p,l) for p in points for l in lines if p in l]
assert len(flags)==45
# Compatibility = no shared point/line and no cross-incidence.
N=[]
for i,(p,l) in enumerate(flags):
    m=0
    for j,(q,t) in enumerate(flags):
        if i!=j and p not in t and q not in l:
            m |= 1<<j
    N.append(m)

def bits(mask):
    while mask:
        low=mask & -mask
        yield low.bit_length()-1
        mask ^=low

sizes=Counter()
maxima=[]

def bronk(R,P,X):
    if P==0 and X==0:
        sizes[R.bit_count()]+=1
        if R.bit_count()>=9:
            maxima.append(R)
        return
    PX=P|X
    if PX:
        pivot=max(bits(PX), key=lambda u:(P&N[u]).bit_count())
        choices=P & ~N[pivot]
    else:
        choices=P
    while choices:
        vbit=choices&-choices
        v=vbit.bit_length()-1
        bronk(R|vbit,P&N[v],X&N[v])
        P &= ~vbit
        X |= vbit
        choices &= ~vbit

bronk(0,(1<<45)-1,0)
assert sizes == Counter({5:3060,6:5520,7:360,9:10}),sizes
assert len(maxima)==10
assert all((x&y).bit_count()==1 for x,y in combinations(maxima,2))
assert Counter(v for m in maxima for v in bits(m)) == Counter({i:2 for i in range(45)})
print('SYMPLECTIC_BRON_KERBOSCH_PASS flags=45 maximal_matchings=8950 maxima=10')
print('maximal_sizes=',sorted(sizes.items()))
