"""Exact-arithmetic checks for Pell-triple factorization presentations.

Run with Python 3.10+: python pell_catenary_verify.py
Checks are finite corroboration, not a proof of the universal theorem.
"""
from math import gcd
from collections import deque


def pell(u, top):
    P = [0, 1]
    for _ in range(2, top + 1):
        P.append(u * P[-1] + P[-2])
    return P


def all_factors(n, a, b, c):
    for z in range(n // c + 1):
        for y in range((n - z * c) // b + 1):
            rem = n - y * b - z * c
            if rem % a == 0:
                yield (rem // a, y, z)


def transforms(q, Q, r, b):
    return [((0,q,0),(1,0,1)),
            ((b-Q,0,0),(0,r,Q)),
            ((0,0,Q+1),(b-Q-1,q-r,0))]


def connected_with_moves(factors, moves):
    group = set(factors)
    if not group:
        return True
    reached = {factors[0]}
    todo = deque([factors[0]])
    while todo:
        f = todo.popleft()
        for m1,m2 in moves:
            for lhs,rhs in ((m1,m2),(m2,m1)):
                if all(f[j] >= lhs[j] for j in range(3)):
                    g = tuple(f[j]-lhs[j]+rhs[j] for j in range(3))
                    if g in group and g not in reached:
                        reached.add(g);todo.append(g)
    return len(reached) == len(factors)


def check(u, i, exhaustive=False):
    P = pell(u, i+4)
    a,b,c = P[i], P[i+2], P[i+4]
    q = u*u+2
    Q,r = divmod(a,q)
    assert i >= 5 and i%2 == 1
    assert a>q and b>2*a and gcd(a,b)==1 and c == q*b-a
    assert r in (1,q-1)
    assert (r == 1) == (i%8 in (1,7))
    moves = transforms(q,Q,r,b)
    for lhs,rhs in moves:
        assert sum(lhs[j]*v for j,v in enumerate((a,b,c))) == sum(rhs[j]*v for j,v in enumerate((a,b,c)))
    betti = [q*b, (b-Q)*a, (Q+1)*c]
    assert len(set(betti)) == 3
    checked_fibers = 0
    for n,(lhs,rhs) in zip(betti,moves):
        if n < 10**6:
            fact = set(all_factors(n,a,b,c))
            assert fact == {lhs,rhs}, (u,i,n,fact,lhs,rhs)
            checked_fibers += 1
    D = b-Q+q-r-1
    assert D == max(max(map(sum,p)) for p in moves)
    # Minimality and exhaustive presentation checks on the small instance:
    if exhaustive:
        for n in range(1201):
            fac = list(all_factors(n,a,b,c))
            assert connected_with_moves(fac,moves), (u,i,n,fac)
    return (u,i,a,b,c,q,Q,r,D,checked_fibers)


def main():
    checks = 0
    fibers = 0
    for u in range(1,9):
        for i in range(5,20,2):
            result = check(u,i,exhaustive=(u,i) in {(1,5),(1,7),(2,5)})
            checks += 1
            fibers += result[-1]
            if u <= 3 and i <= 9:
                print(result)
    print('PASS',checks,'parameter samples;',fibers,'directly enumerated critical fibers; 3 exhaustive ranges 0..1200')

if __name__ == '__main__':
    main()
