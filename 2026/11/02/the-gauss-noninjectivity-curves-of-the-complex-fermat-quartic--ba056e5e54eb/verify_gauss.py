"""Exact finite-field and pattern checks of Fermat-quartic Gauss-fibre geometry.
Run: python3 verify_gauss.py. Only integer modular arithmetic is used.
"""
from itertools import product,combinations
from collections import defaultdict,Counter

# Pattern enumeration in (mu_3)^4/mu_3, represented by exponents starting at 0.
patterns=Counter()
for v in product(range(3),repeat=3):
    a=(0,)+v
    sizes=sorted(Counter(a).values(),reverse=True)
    patterns[tuple(sizes)]+=1
assert patterns=={(4,):1,(3,1):8,(2,2):6,(2,1,1):12}
print('CUBIC_PATTERN_COUNTS_OK',dict(patterns))

def points_projective(q):
    for first in range(4):
        for tail in product(range(q),repeat=3-first):
            yield (0,)*first+(1,)+tail

def gauss(x,q):
    return tuple(pow(a,3,q) for a in x)

def support(x,q):
    s=[pow(a,4,q) for a in x]
    line=all(x) and any((s[i]+s[j])%q==0 and (s[k]+s[l])%q==0
             for (i,j),(k,l) in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))])
    # omega is a fixed nontrivial cube root in Fq. Rational support of the 48 smooth quartic sections.
    omega=next(w for w in range(2,q) if pow(w,3,q)==1)
    quartic=any(s[j] and s[k] and (s[j]-w*s[k])%q==0
      for j,k in combinations(range(4),2) for w in (omega,pow(omega,2,q)))
    return line,quartic

for q in (13,37,73):
    fib=defaultdict(list)
    n=0
    for x in points_projective(q):
        if sum(pow(a,4,q) for a in x)%q:continue
        n+=1
        fib[gauss(x,q)].append(x)
    h=Counter(map(len,fib.values()))
    assert max(h)>=2, (q,h)
    actual=0; exceptional_triple=0; exceptional_double=0
    for y,points in fib.items():
        for x in points:
            is_line,is_quartic=support(x,q)
            is_mult=len(points)>1
            assert is_mult==(is_line or is_quartic), (q,x,len(points),is_line,is_quartic)
            if len(points)==3 and not is_line: exceptional_triple+=1
            if len(points)==2 and not is_quartic: exceptional_double+=1
            if is_mult:actual+=1
    print('FERMAT_GAUSS_EXHAUSTIVE',q,'surface_points',n,'fiber_sizes',dict(h),'multiple_points',actual,'special_triples',exceptional_triple,'special_doubles',exceptional_double)
print('FERMAT_GAUSS_FIBRE_13_37_73_AND_PATTERN_CHECK_OK')
