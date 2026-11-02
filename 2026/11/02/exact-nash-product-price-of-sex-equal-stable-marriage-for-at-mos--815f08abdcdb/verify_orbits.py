"""Independent orbit-weighted verifier for six-person strict stable marriage.

Generate all label and side-swap symmetry orbits, evaluate one representative
per orbit, and recover the exact distribution by weighting orbit sizes.
"""
from itertools import permutations,product
from collections import Counter
from fractions import Fraction
from math import prod

N=3
ORDERS=tuple(permutations(range(N)))
LABELS=tuple(permutations(range(N)))

def relabel(profile, male_labels, female_labels):
    new_m=[None]*N;new_w=[None]*N
    for i in range(N):
        new_m[male_labels[i]]=tuple(female_labels[j] for j in profile[i])
    for j in range(N):
        new_w[female_labels[j]]=tuple(male_labels[i] for i in profile[N+j])
    return tuple(new_m+new_w)

def orbit(profile):
    result=set()
    swap=profile[N:]+profile[:N]
    for base in (profile,swap):
        for a in LABELS:
            for b in LABELS:
                result.add(relabel(base,a,b))
    return result

def ratio(profile):
    candidates=[]
    for assignment in ORDERS:
        partners=[assignment.index(w) for w in range(N)]
        # List-position checking, without precomputed ranking matrices.
        if any(profile[i].index(w)<profile[i].index(assignment[i])
               and profile[N+w].index(i)<profile[N+w].index(partners[w])
               for i in range(N) for w in range(N) if w!=assignment[i]):
            continue
        m=sum(profile[i].index(assignment[i]) for i in range(N))
        f=sum(profile[N+w].index(partners[w]) for w in range(N))
        p=prod(N-profile[i].index(assignment[i]) for i in range(N))
        p*=prod(N-profile[N+w].index(partners[w]) for w in range(N))
        candidates.append((abs(m-f),p))
    assert candidates
    bestgap=min(d for d,p in candidates)
    return Fraction(max(p for d,p in candidates),
                    max(p for d,p in candidates if d==bestgap))

def main():
    unseen=set(product(ORDERS,repeat=2*N))
    dist=Counter();orbits=Counter();maxorbit=[]
    while unseen:
        example=min(unseen)
        cls=orbit(example)
        assert cls<=unseen
        unseen.difference_update(cls)
        value=ratio(example)
        dist[value]+=len(cls)
        orbits[value]+=1
        if value==Fraction(9,4):maxorbit.append((len(cls),example))
    expected={Fraction(1):44136, Fraction(9,8):504, Fraction(3,2):1728,
              Fraction(2):144, Fraction(9,4):144}
    assert dist==expected
    assert sum(orbits.values())==669
    assert sum(dist.values())==46656
    print('orbit_count',sum(orbits.values()), 'orbit_histogram',dict(orbits))
    print('maximizer_orbits',maxorbit)
    print('VERIFY_ORBITS_OK profiles=46656 orbits=669 max_ratio=9/4')

if __name__=='__main__': main()
