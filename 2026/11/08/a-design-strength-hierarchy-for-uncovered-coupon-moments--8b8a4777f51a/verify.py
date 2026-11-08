"""Exact finite checks for the random-block uncovered-moment hierarchy.
No stochastic simulation is used. Requires Python >=3.9, standard library only.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb


def falling(v, r):
    z = 1
    for j in range(r):
        z *= v-j
    return z


def projective_plane(p):
    """Points and lines of PG(2,p) for prime p as 0-based index sets."""
    def canonical(x):
        pivot = next(z for z in x if z % p)
        return tuple((z * pow(pivot,-1,p)) % p for z in x)
    points = sorted({canonical(x) for x in product(range(p),repeat=3) if any(x)})
    lines = [frozenset(j for j,x in enumerate(points)
                       if sum(a*b for a,b in zip(x,w)) % p == 0)
             for w in points]
    assert len(points) == p*p+p+1
    assert len(lines) == len(set(lines)) == len(points)
    assert all(len(line) == p+1 for line in lines)
    return points, lines


def avoidance(v, blocks, probabilities, r):
    return [sum((weight for block,weight in zip(blocks, probabilities)
                 if block.isdisjoint(S)), Q(0))
            for S in combinations(range(v),r)]


def covered_inclusion(v, blocks, probabilities, j):
    return [sum((w for B,w in zip(blocks,probabilities) if set(J)<=B),Q(0))
            for J in combinations(range(v),j)]


def direct_moment(v,blocks,probabilities,t,r):
    total = Q(0)
    for idx in product(range(len(blocks)),repeat=t):
        union = set().union(*(blocks[i] for i in idx))
        probability = Q(1)
        for i in idx:
            probability *= probabilities[i]
        total += probability*falling(v-len(union),r)
    return total


def run():
    tested=0
    for v in range(4,8):
      for k in range(1,v):
        all_blocks = [frozenset(B) for B in combinations(range(v),k)]
        candidates = [
          ('full',all_blocks,[Q(1,len(all_blocks))]*len(all_blocks)),
          ('single',[all_blocks[0]],[Q(1)]),
          ('cyclic',[frozenset((i+j)%v for j in range(k)) for i in range(v)],[Q(1,v)]*v),
          ('biased',all_blocks,[Q(i+1, len(all_blocks)*(len(all_blocks)+1)//2) for i in range(len(all_blocks))]),
        ]
        for label,blocks,pr in candidates:
            assert sum(pr)==1
            for r in range(1,min(k,v-k)+1):
                av=avoidance(v,blocks,pr,r)
                full=Q(comb(v-r,k),comb(v,k))
                assert sum(av, Q(0))/len(av)==full
                tested+=1
                for t in (2,3):
                    got=falling(v,r)*sum((x**t for x in av),Q(0))/len(av)
                    base=falling(v,r)*full**t
                    assert got>=base
                    flat=all(x==full for x in av)
                    assert (got==base)==flat
                    tested+=1
                incl=covered_inclusion(v,blocks,pr,r)
                balanced=all(x==Q(comb(k,r),comb(v,r)) for x in incl)
                assert balanced == all(x==full for x in av)
                tested+=1
                if r==1:
                    moment1=falling(v,1)*sum(x**2 for x in av)/len(av)
                    assert moment1>=v*Q(v-k,v)**2
                    tested+=1
                if r<=2:
                    got2=falling(v,r)*sum((x*x for x in av),Q(0))/len(av)
                    via2=direct_moment(v,blocks,pr,2,r)
                    assert got2==via2
                    tested+=1

    for p in (2,3,5):
        points,lines=projective_plane(p)
        v=len(points);pr=[Q(1,v)]*v
        for r in (1,2,3):
            av=avoidance(v,lines,pr,r)
            a0=Q(comb(v-r,p+1),comb(v,p+1))
            if r<=2:
                assert all(a==a0 for a in av)
            else:
                lower=Q((p-1)**2-1,v)
                higher=Q((p-1)**2,v)
                f=Q(p-1,v-2)
                assert set(av)=={lower,higher}
                assert Q(av.count(lower),len(av))==f
                assert (f*lower+(1-f)*higher)==a0
                for t in (2,3,5):
                    target=falling(v,3)* (f*lower**t+(1-f)*higher**t-a0**t)
                    assert target>0
                    tested+=1
                gap=falling(v,3)*(f*lower**2+(1-f)*higher**2-a0**2)
                expected=Q(p**3*(p*p-1),v*(v-2))
                assert gap==expected
                print('q =',p,'exact two-draw third-factorial-moment gap =',gap)
            tested+=1
        if p in (2,3):
            for t in (2,3):
                formula=falling(v,3)*sum((a**t for a in avoidance(v,lines,pr,3)),Q(0))/comb(v,3)
                brute=direct_moment(v,lines,pr,t,3)
                assert formula==brute
                tested+=1

    print('PASS:',tested,'exact rational checks; finite sizes only')

if __name__=='__main__':
    run()
