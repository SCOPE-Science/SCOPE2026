"""Exact finite-field enumeration for the exceptional quadratic sign classes.

Run with Python 3, no third-party libraries. Exhaustive projective enumeration
and a second, unnormalized enumeration must agree on every coefficient triple.
"""
from itertools import product

EXPECTED = {
    19: ((1,1,7),(1,2,7),(1,2,11),(1,3,1),(1,3,11),
         (1,7,1),(1,11,11),(1,14,1),(1,14,7)),
    31: ((1,6,1),(1,7,12),(1,29,13)),
}

def prime_divisors(n):
    out = []
    for p in range(2,n+1):
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        if n==1: break
    return out

def primitive_roots(p):
    return tuple(g for g in range(1,p)
                 if all(pow(g, (p-1)//r, p) != 1
                        for r in prime_divisors(p-1)))

def norm(a,b,c,p):
    for t in (a,b,c):
        if t%p: return (a*pow(t,-1,p)%p,b*pow(t,-1,p)%p,c*pow(t,-1,p)%p)
    raise ValueError('zero triple has no projective class')

def valid(a,b,c,p):
    return (a%p!=0 or c%p!=0) and (b*b-4*a*c)%p!=0

def bad(a,b,c,p,roots,squares):
    has_positive = has_negative = False
    for g in roots:
        z = (a*g*g+b*g+c)%p
        if z:
            if z in squares: has_positive=True
            else: has_negative=True
        if has_positive and has_negative: return False
    return True

def run():
    for p, expected in EXPECTED.items():
        roots=primitive_roots(p)
        squares={x*x%p for x in range(1,p)}
        assert len(roots) == (6 if p==19 else 8)
        # First approach: choose unique projective normal forms.
        canonical = [(1,b,c) for b,c in product(range(p),repeat=2)]
        canonical += [(0,1,c) for c in range(p)]
        canonical += [(0,0,1)]
        assert len(canonical)==p*p+p+1
        qualifying=[r for r in canonical if valid(*r,p)]
        found=tuple(sorted(r for r in qualifying if bad(*r,p,roots,squares)))
        assert found == tuple(sorted(expected)), (p,found)
        # Second approach: enumerate ALL coefficient triples, no normalization,
        # test their quadratic symbols, then normalize only at the end.
        second=set()
        positives=negatives=zeros=0
        for a,b,c in product(range(p),repeat=3):
            if not valid(a,b,c,p): continue
            if bad(a,b,c,p,roots,squares):
                second.add(norm(a,b,c,p))
        assert second == set(found)
        assert len(found)*(p-1) == sum(
            1 for a,b,c in product(range(p),repeat=3)
            if valid(a,b,c,p) and bad(a,b,c,p,roots,squares))
        print('CERTIFIED',p,'primitive_roots',roots,'admissible_classes',len(qualifying),
              'exceptional_classes',len(found),'listed',found)
if __name__=='__main__': run()
