"""Finite independent tests for Hamming closed-ball concept-lattice symmetry.
Run with Python 3.9+ and the standard library only.
Finite tests are not substitutes for the symbolic automorphism-group proof.
"""
from itertools import product, permutations
from math import factorial, comb


def context(d, q):
    points = list(product(range(q), repeat=d))
    neighborhoods = [frozenset(y for y in points if sum(a != b for a,b in zip(x,y)) <= 1) for x in points]
    return points, neighborhoods


def closed_intents(d,q):
    points, balls = context(d,q)
    universe = frozenset(points)
    closed = {frozenset(), universe}
    for a in balls:
        for b in balls:
            closed.add(a & b)
    # singleton is a triple intersection for every d>=2, q>=2
    for i in range(len(balls)):
        for j in range(i):
            ab = balls[i] & balls[j]
            for k in range(j):
                closed.add(ab & balls[k])
    for x in points:
        closed.add(frozenset([x]))
    # check actual fixed points, not merely assumed structural list
    for A in closed:
        derived = universe
        for B in balls:
            if A <= B:
                derived &= B
        assert derived == A, (d,q,A)
    return closed


def predicted_intents(d,q):
    points,balls = context(d,q)
    out = {frozenset(),frozenset(points)}
    out.update(map(frozenset,balls))
    out.update(frozenset([x]) for x in points)
    for i in range(d):
        for x in points:
            out.add(frozenset(y for y in points if all(x[j]==y[j] for j in range(d) if j!=i)))
    for i,x in enumerate(points):
        for y in points[:i]:
            if sum(a!=b for a,b in zip(x,y))==2:
                out.add(frozenset((x,y)))
    return out


def full_automorphisms_bruteforce(d,q):
    points, balls = context(d,q)
    n = len(points)
    enc = [sum(1 << points.index(y) for y in B) for B in balls]
    enc_set = frozenset(enc)
    total = 0
    for perm in permutations(range(n)):
        if all(sum(1 << perm[i] for i in range(n) if bit & (1 << i)) in enc_set for bit in enc):
            total += 1
    return total


def even_lift_symmetries(d):
    points, balls = context(d,2)
    pt_id = {v:i for i,v in enumerate(points)}
    ball_codes = {frozenset(pt_id[y] for y in B) for B in balls}
    n=d+1
    even = [t for t in product(range(2), repeat=n) if sum(t)%2==0]
    parity = lambda y: sum(y)%2
    lifted = {tuple(y)+(parity(y),):i for i,y in enumerate(points)}
    count = 0
    for perm in permutations(range(n)):
        for shift in even:
            image = []
            for y in points:
                e = tuple(y)+(parity(y),)
                transformed = tuple(e[perm[j]] ^ shift[j] for j in range(n))
                image.append(lifted[transformed])
            if {frozenset(image[i] for i in B) for B in ball_codes} != ball_codes:
                raise AssertionError((d,perm,shift))
            count += 1
    return count


def run():
    examined=0
    for d,q in [(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(2,4)]:
        X = closed_intents(d,q)
        Y = predicted_intents(d,q)
        assert X==Y, (d,q,len(X),len(Y),len(X-Y),len(Y-X))
        N=q**d
        expected=2+2*N+d*q**(d-1)+N*comb(d,2)*(q-1)**2//2
        # When q=2, coordinate lines coincide with dist-2 pairs in sizes but not sets.
        assert len(X)==expected,(d,q,len(X),expected)
        examined += len(X)
    actual={}
    for d,q in [(2,2),(3,2),(2,3)]:
        count=full_automorphisms_bruteforce(d,q)
        expected=(2**d*factorial(d+1)) if q==2 else factorial(q)**d*factorial(d)
        assert count==expected,(d,q,count,expected)
        actual[(d,q)]=count
    generated={d:even_lift_symmetries(d) for d in range(2,5)}
    assert generated=={2:24,3:192,4:1920}
    print('VERIFY_OK closed_intents_total=%d exhaustive_ball_perm_counts=%s binary_parity_generated=%s' % (examined,actual,generated))

if __name__=='__main__':
    run()
