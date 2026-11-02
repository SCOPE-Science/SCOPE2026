"""Exact combinatorial checks of the binary-prefix ternary BWT splice construction."""
from collections import Counter
from math import gcd


def is_prime(p):
    if p < 2:
        return False
    return all(p % d for d in range(2, int(p**0.5) + 1))


def two_primitive(p):
    if not is_prime(p):
        return False
    if p == 2:
        return False
    x, seen = 1, set()
    for _ in range(p - 1):
        if x in seen:
            return False
        seen.add(x)
        x = (2*x) % p
    return x == 1 and len(seen) == p - 1


def stable_permutation(L):
    counts = Counter(L)
    first = {}
    s = 0
    for ch in sorted(counts):
        first[ch] = s
        s += counts[ch]
    used = Counter()
    ans = []
    for ch in L:
        ans.append(first[ch] + used[ch])
        used[ch] += 1
    return ans


def is_single_cycle(pi):
    n = len(pi)
    if sorted(pi) != list(range(n)):
        return False
    visited = set()
    k = 0
    while k not in visited:
        visited.add(k)
        k = pi[k]
    return k == 0 and len(visited) == n


def inverse_bwt_single_cycle(L, pi):
    row = 0
    out = []
    for _ in L:
        out.append(L[row])
        row = pi[row]
    assert row == 0
    return ''.join(out[::-1])


def cyclic_bwt(t):
    return ''.join(s[-1] for s in sorted(t[i:]+t[:i] for i in range(len(t))))


def verify(p, kind, inverse=True):
    assert p % 8 == 5 and two_primitive(p)
    r = (p-5)//2
    L = '10'*r + ('1012021' if kind == 2 else '10120121')
    n = len(L)
    assert n == p+kind
    assert all(a != b for a, b in zip(L, L[1:])), (p,kind)
    pi = stable_permutation(L)
    assert is_single_cycle(pi), (p,kind)
    inv2 = pow(2, -1, p)
    f = lambda i: (inv2 * ((i-1)%p)) % p
    assert all(pi[i] == f(i) for i in range(p-2)), (p,kind,'ordinary edges')
    if kind == 2:
        assert (pi[p-2], pi[p], pi[p+1], pi[p-1]) == (p, p+1, p-1, r+1)
        assert Counter(L) == Counter({'0':r+2, '1':r+3, '2':2})
    else:
        assert (pi[p-2], pi[p+1], pi[p+2], pi[p], pi[p-1]) == (p+1,p+2,p,p-1,r+1)
        assert Counter(L) == Counter({'0':r+2,'1':r+4,'2':2})
    F = ''.join(sorted(L))
    agree = [sum(L[j]==F[j] for j in range(len(L)) if F[j]==c) for c in '012']
    assert agree == ([r//2+1, r//2+1, 1] if kind==2 else [r//2+1, r//2+2, 1]), (p,kind,agree)
    dist = sum(a!=b for a,b in zip(L,F))
    assert dist == (p+3)//2, (p,kind,dist)
    if inverse:
        t = inverse_bwt_single_cycle(L, pi)
        assert len({t[i:]+t[:i] for i in range(n)}) == n, (p,kind)
        assert cyclic_bwt(t) == L, (p,kind,'BWT reconstruction')
        assert sum(t[i] != t[(i+1)%n] for i in range(n)) == dist, (p,kind,'cyclic run identity')
    return n, dist


if __name__ == '__main__':
    tested = []
    for p in range(5, 2000, 8):
        if two_primitive(p):
            tested.append(p)
            for kind in (2,3):
                verify(p, kind, inverse=p <= 181)
    print('PASS: checked',len(tested),'eligible primes up to 2000, two lengths each')
    print('Primes:',tested)
    print('PASS: stable permutation, single-cycle, edge splice, block agreements, sharp distance for all')
    print('PASS: independently reconstructed primitive necklace, cyclic BWT, and run counts for primes <=181')
    print('Representative lengths:', [(p, verify(p,2)[0], verify(p,3)[0]) for p in (5,13,29,37,53,61,101,149,173,181) if two_primitive(p)])
