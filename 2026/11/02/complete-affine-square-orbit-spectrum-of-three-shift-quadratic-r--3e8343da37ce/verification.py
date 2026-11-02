#!/usr/bin/env python3
"""Exact, dependency-free verification of three-shift quadratic covers."""
from itertools import combinations
CASES=((3,0,(1,)),(5,0,(5,5)),(7,0,(7,21)),(3,1,(6,6,36)),(11,0,(55,)),(13,0,(26,39)),(17,0,(68,)),(5,2,(100,)))

def arithmetic(p,k):
    q=p if k==0 else p*p
    def add(a,b):
        if k==0:return (a+b)%p
        return (((a//p+b//p)%p)*p+(a%p+b%p)%p)
    def mul(a,b):
        if k==0:return (a*b)%p
        return (((a//p*(b%p)+(a%p)*(b//p))%p)*p+((a%p)*(b%p)-k*(a//p)*(b//p))%p)
    return q,add,mul

def run():
    for p,k,expected in CASES:
        q,add,mul=arithmetic(p,k)
        # Integer p*i+j encodes the field element i*theta+j, theta^2=-k.
        # Both x^2+k are irreducible for (p,k)=(3,1),(5,2).
        assert k==0 or {(-k)%p not in {i*i%p for i in range(p)}}
        square={mul(x,x) for x in range(q)}
        assert len(square)==(q+1)//2
        units=sorted(square-{0})
        # First algorithm: direct-set unions; exhaustive enumeration of all C(q,3) sets.
        triples={a for a in combinations(range(q),3)
                 if set().union(*( {add(t,z) for z in square} for t in a))==set(range(q))}
        # Second, independent set-encoding check of the union criterion.
        masks=[sum(1<<add(t,z) for z in square) for t in range(q)]
        full=(1<<q)-1
        triples2={a for a in combinations(range(q),3)
                  if masks[a[0]]|masks[a[1]]|masks[a[2]]==full}
        assert triples==triples2
        unseen=triples.copy(); orbits=[]; orbit_reps=[]
        while unseen:
            representative=min(unseen)
            orbit={tuple(sorted(add(mul(t,s),b) for t in representative))
                   for b in range(q) for s in units}
            assert orbit<=triples
            assert orbit<=unseen
            unseen-=orbit
            orbits.append(len(orbit));orbit_reps.append(representative)
        assert tuple(sorted(orbits))==expected,(q,orbits,expected)
        assert sum(orbits)==len(triples)
        print(f'q={q}: triples={len(triples)}; orbit sizes={tuple(sorted(orbits))}; representatives={orbit_reps}')
    print('VERIFY_OK')

if __name__=='__main__':run()
