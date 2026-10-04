#!/usr/bin/env python3
from math import comb


def matchings(xs):
    xs=tuple(xs)
    if not xs:
        yield ()
        return
    a=xs[0]
    for i in range(1,len(xs)):
        b=xs[i]
        rest=xs[1:i]+xs[i+1:]
        for tail in matchings(rest):
            yield ((a,b),)+tail


def endpoint_perm(N, typ, k):
    if typ=='r':
        return tuple((i+k)%N for i in range(N))
    return tuple((k-i)%N for i in range(N))


def gap_image(N, typ, k, i):
    # gap i is the clockwise arc from i to i+1. Reflections reverse it.
    if typ=='r':
        return (i+k)%N
    return (k-i-1)%N


def stabilizer(M):
    N=2*len(M)
    pairs=[frozenset(p) for p in M]
    G=[]
    for typ in ('r','s'):
        for k in range(N):
            p=endpoint_perm(N,typ,k)
            if all(frozenset((p[a],p[b]))==pair for (a,b),pair in zip(M,pairs)):
                G.append((typ,k))
    return G


def extension_orbits(M):
    N=2*len(M)
    G=stabilizer(M)
    placements={(i,j) for i in range(N) for j in range(i,N)}
    unseen=set(placements)
    count=0
    while unseen:
        x=min(unseen)
        orb=set()
        for typ,k in G:
            a,b=x
            y=tuple(sorted((gap_image(N,typ,k,a),gap_image(N,typ,k,b))))
            orb.add(y)
        unseen-=orb
        count+=1
    return count

max_nonalg=[]
max_full=[]
for m in range(1,7):
    best=-1
    for M in matchings(range(2*m)):
        best=max(best,extension_orbits(M))
    max_nonalg.append(best)
    max_full.append(best+m)
    if m>=3:
        adjacent=tuple((2*i,2*i+1) for i in range(m))
        assert len(stabilizer(adjacent))==1
        assert extension_orbits(adjacent)==comb(2*m+1,2)

assert max_nonalg == [2,7,21,36,55,78], max_nonalg
assert max_full == [3,9,24,40,60,84], max_full
for m in range(3,7):
    assert max_full[m-1] == 2*m*(m+1)

print('max nonalgebraic:', max_nonalg)
print('f_M(m), m=1..6:', max_full)
print('VERIFY_OK')
