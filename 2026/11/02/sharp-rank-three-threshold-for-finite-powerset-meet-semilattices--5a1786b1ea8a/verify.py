"""Exact finite Venn-cell logical-type certificates for intersection semilattices."""
from itertools import product
from functools import lru_cache

def atom(c):
    k = len(c).bit_length()-1
    support = [p for p,v in enumerate(c) if v]
    eq = tuple(all((p>>i&1)==(p>>j&1) for p in support)
               for i in range(k) for j in range(i+1,k))
    mt = tuple(all(((p>>i&1)&(p>>j&1))==(p>>h&1) for p in support)
               for i in range(k) for j in range(k) for h in range(k))
    return eq,mt

@lru_cache(None)
def typ(c,r):
    if not r:
        return atom(c)
    out = set()
    for x in product(*(range(v+1) for v in c)):
        v = tuple(c[i]-x[i] for i in range(len(c)))+tuple(x)
        out.add(typ(v,r-1))
    return frozenset(out)

# Each 4-or-more region allows every split with both truncated sizes <=2.
for c in range(4,9):
    patterns = {(min(x,2),min(c-x,2)) for x in range(c+1)}
    assert patterns == {(0,2),(1,2),(2,2),(2,1),(2,0)}

for b in range(5):
    assert typ((3,b),2)==typ((4,b),2)
    assert typ((b,3),2)==typ((b,4),2)

pointed = { (a,b):typ((a,b),2) for a in range(4) for b in range(4) }
assert len(set(pointed.values()))==16
roots = [typ((n,),3) for n in range(1,11)]
assert len(set(roots))==6
assert len(set(roots[:5]))==5
assert all(v==roots[5] for v in roots[5:])
print('PASS: exact 4+ split stabilization, ten pointed reductions, 16 distinct pointed types, six root theories')
