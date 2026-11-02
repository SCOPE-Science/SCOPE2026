#!/usr/bin/env python3
"""Independent finite verification of binary bireversible Mealy enumerations.

Run: python3 verify.py
Python standard library only.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, gcd


def is_bireversible_direct(a, b, swap_mask):
    # Test invertibility and reversibility of the inverse transducer
    # by direct incoming-edge enumeration for each output letter.
    n = len(a)
    if len(set(a)) != n or len(set(b)) != n:
        return False
    for output in (0, 1):
        targets = set()
        for q in range(n):
            inp = output ^ ((swap_mask >> q) & 1)
            targets.add((a if inp == 0 else b)[q])
        if len(targets) != n:
            return False
    return True


def connected_direct(a, b):
    reachable = {0}
    todo = [0]
    while todo:
        q = todo.pop()
        for dest in (a[q], b[q]):
            if dest not in reachable:
                reachable.add(dest)
                todo.append(dest)
    return len(reachable) == len(a)


def canonical(a, b, swap_mask, relabels):
    n = len(a)
    best = None
    for p in relabels:
        aa = [0] * n
        bb = [0] * n
        mask = 0
        for q in range(n):
            j = p[q]
            aa[j] = p[a[q]]
            bb[j] = p[b[q]]
            mask |= ((swap_mask >> q) & 1) << j
        t = (tuple(aa), tuple(bb), mask)
        if best is None or t < best:
            best = t
    return best


@lru_cache(None)
def partitions(n, maximum=None):
    if maximum is None:
        maximum = n
    if n == 0:
        return ((),)
    return tuple((i,) + suffix for i in range(min(maximum,n), 0, -1)
                 for suffix in partitions(n-i, i))


def u_orbits(n):
    # Closed Burnside partition formula, indexed by swap count.
    result = Counter()
    for blocks in partitions(n):
        m = Counter(blocks)
        row = Counter({0:1})
        for ell, multiplicity in m.items():
            factor = ell ** multiplicity * factorial(multiplicity)
            new = Counter()
            for k, ways in row.items():
                for j in range(multiplicity+1):
                    new[k+ell*j] += ways * factor
            row = new
        result.update(row)
    return result


def labelled_connected_table(nmax):
    # Component containing the smallest label: direct integer recurrence.
    all_by_n = [Counter({0:1})]
    con_by_n = [Counter()]
    for n in range(1,nmax+1):
        alln = Counter({k:factorial(n)**2 for k in range(n+1)})
        conn = Counter(alln)
        for j in range(1,n):
            ways = comb(n-1,j-1)
            for r,v in con_by_n[j].items():
                for t,w in all_by_n[n-j].items():
                    conn[r+t] -= ways*v*w
        assert all(v >= 0 for v in conn.values())
        all_by_n.append(alln)
        con_by_n.append(conn)
    return con_by_n


def mobius(n):
    factors = []
    t = n
    p = 2
    while p*p <= t:
        if t%p == 0:
            t//=p
            if t%p == 0:
                return 0
            factors.append(p)
        p+=1
    if t>1:
        factors.append(t)
    return -1 if len(factors)%2 else 1


def unlabelled_connected_table(nmax):
    # Independent algebraic extraction of connected isomorphism classes:
    # log U(z,t) followed by multivariate Möbius inversion.
    u = [Counter({0:1})]+[u_orbits(n) for n in range(1,nmax+1)]
    logu = [Counter() for _ in range(nmax+1)]
    for n in range(1,nmax+1):
        row = Counter({k:Fraction(v) for k,v in u[n].items()})
        for j in range(1,n):
            for r,v in logu[j].items():
                for t,w in u[n-j].items():
                    row[r+t] -= Fraction(j,n)*v*w
        logu[n]=row
    conn = [Counter() for _ in range(nmax+1)]
    for n in range(1,nmax+1):
        for k in range(n+1):
            val = sum(Fraction(mobius(d),d)*logu[n//d][k//d]
                      for d in range(1,n+1) if n%d==0 and k%d==0)
            assert val.denominator == 1 and val >= 0, (n,k,val)
            conn[n][k] = int(val)
    return conn


def run():
    cc = labelled_connected_table(12)
    vv = unlabelled_connected_table(10)
    expected_total_connected = [2,8,88,1776,55488,2446080]
    expected_unlabelled = [2,10,38,188,950,6214,45718,396796]
    expected_conn_unlabelled = [2,7,20,94,472,3550,28496,268507]
    for n in range(1,9):
        assert sum(u_orbits(n).values()) == expected_unlabelled[n-1]
        assert sum(vv[n].values()) == expected_conn_unlabelled[n-1]
    for n in range(1,7):
        assert sum(cc[n].values()) == expected_total_connected[n-1]
    print('FORMAL_CHECK_OK labeled_connected n=1..12; unlabelled_connected n=1..10')
    # Direct enumeration uses the definition of inverse-reversibility,
    # rather than the derived cycle-normalization condition.
    for n in range(1,6):
        perms = list(permutations(range(n)))
        allcounts=Counter()
        conncounts=Counter()
        # Canonicalize independently under *state relabelings only* through n=4.
        unique_all=[set() for _ in range(n+1)] if n<=4 else None
        unique_con=[set() for _ in range(n+1)] if n<=4 else None
        for a in perms:
            for b in perms:
                co=connected_direct(a,b)
                for mask in range(1<<n):
                    if not is_bireversible_direct(a,b,mask):
                        continue
                    k=mask.bit_count()
                    allcounts[k]+=1
                    if co: conncounts[k]+=1
                    if n<=4:
                        key=canonical(a,b,mask,perms)
                        unique_all[k].add(key)
                        if co: unique_con[k].add(key)
        assert all(allcounts[k]==factorial(n)**2 for k in range(n+1))
        assert conncounts==cc[n], (n,conncounts,cc[n])
        if n<=4:
            assert Counter({k:len(s) for k,s in enumerate(unique_all)}) == u_orbits(n)
            assert Counter({k:len(s) for k,s in enumerate(unique_con)}) == vv[n]
        if n==2:
            # Compare the independently documented GAP state+alphabet equivalence
            # to the stricter state-only relation of the theorem.
            both = set()
            for a in perms:
                for b in perms:
                    for mask in range(1<<n):
                        if is_bireversible_direct(a,b,mask):
                            both.add(min(canonical(a,b,mask,perms),
                                         canonical(b,a,mask,perms)))
            assert len(both) == 8
            print('GAP_CONVENTION_OK n=2 classes_up_to_state_and_alphabet=8')
        print('DIRECT_OK n=%d labeled=%d connected=%d isomorphism=%s' %
              (n,sum(allcounts.values()),sum(conncounts.values()),
               'checked' if n<=4 else 'not_exhausted'))
    print('FIRST_COUNTS n | all_labeled | connected_labeled | all_unlabeled | connected_unlabeled')
    for n in range(1,9):
        print('%d | %d | %d | %d | %d' % (n,(n+1)*factorial(n)**2,
             sum(cc[n].values()),sum(u_orbits(n).values()),sum(vv[n].values())))
    print('VERIFY_OK')

if __name__=='__main__': run()
