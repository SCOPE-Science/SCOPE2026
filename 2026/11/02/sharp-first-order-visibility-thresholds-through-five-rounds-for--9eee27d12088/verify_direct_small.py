"""Unquotiented vertex-sequence enumeration through five moves (small graphs)."""
from functools import lru_cache
from itertools import combinations

def vertices(n):return tuple(frozenset(x) for k in (1,2) for x in combinations(range(n),k))
def adjacent(a,b):return (len(a),len(b)) in ((1,2),(2,1)) and (a<b or b<a)
@lru_cache(None)
def allmoves(n,seq,depth):
    atoms=tuple((a==b,adjacent(a,b)) for a in seq for b in seq)
    if depth==0:return atoms, frozenset()
    return atoms,frozenset(allmoves(n,seq+(new,),depth-1) for new in vertices(n))

def indexmoves(n,seq):
    used=set().union(*seq) if seq else set()
    old=sorted(used);fresh=[x for x in range(n) if x not in used][:2]
    moves=[frozenset((a,)) for a in old]
    if fresh:moves.append(frozenset((fresh[0],)))
    moves.extend(frozenset(x) for x in combinations(old,2))
    if fresh:moves.extend(frozenset((a,fresh[0])) for a in old)
    if len(fresh)==2:moves.append(frozenset(fresh))
    return tuple(moves)
@lru_cache(None)
def orbitmoves(n,seq,depth):
    atoms=tuple((a==b,adjacent(a,b)) for a in seq for b in seq)
    if depth==0:return atoms, frozenset()
    return atoms,frozenset(orbitmoves(n,seq+(new,),depth-1) for new in indexmoves(n,seq))

for n in range(1,5):
    raw=allmoves(n,(),5)
    orbit=orbitmoves(n,(),5)
    assert raw==orbit,(n,'not equal')
    print(f'n={n} raw_tuples={allmoves.cache_info().currsize} orbit_tuples={orbitmoves.cache_info().currsize} identical=True')
print('DIRECT_UNQUOTIENTED_PASS')
