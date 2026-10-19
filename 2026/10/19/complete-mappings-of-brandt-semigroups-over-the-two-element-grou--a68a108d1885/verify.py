"""Independent finite checks for complete mappings of Brandt semigroups over C2.
Public mathematical verification only; run with Python 3: python verify.py
"""
from itertools import permutations, product

def multiply(x, y):
    if x is None or y is None or x[2] != y[0]:
        return None
    return (x[0], (x[1] + y[1]) % 2, y[2])

def canonical_elements(n):
    return [None] + [(i, g, j) for i in range(n) for g in range(2) for j in range(n)]

def is_complete(mapping):
    source = set(mapping)
    if len(set(mapping.values())) != len(source):
        return False
    return {multiply(x, mapping[x]) for x in source} == source

def explicit(n):
    assert n % 2 == 0 and n >= 2
    t = n // 2
    def decode(z): return (z // t, z % t)
    def encode(a,u): return a * t + u
    mapping = {None: None}
    for i in range(n):
        a,u = decode(i)
        for j in range(n):
            b,v = decode(j)
            for g in range(2):
                mapping[(i,g,j)] = (j, (a+b+g)%2, encode(g,(u+v)%t))
    return mapping

def reduced_enumeration():
    pairs = [(i,g) for i in range(2) for g in range(2)]
    outputs = [(h,k) for h in range(2) for k in range(2)]
    perms = list(permutations(outputs))
    count = 0
    valid_first = 0
    follower_histogram = {}
    for P0 in perms:
        f0 = dict(zip(pairs,P0))
        if any(len({f0[(i,0)][1],f0[(i,1)][1]}) < 2 for i in range(2)):
            continue
        valid_first += 1
        followers = 0
        for P1 in perms:
            f1 = dict(zip(pairs,P1))
            mapping = {None:None}
            for i,g in pairs:
                for j,F in [(0,f0),(1,f1)]:
                    h,k = F[(i,g)]
                    mapping[(i,g,j)] = (j,h,k)
            if is_complete(mapping):
                count += 1
                followers += 1
        follower_histogram[followers] = follower_histogram.get(followers,0) + 1
    assert valid_first == 16
    assert follower_histogram == {2:16}
    assert count == 32
    return count, valid_first, follower_histogram

def full_permutation_enumeration():
    S=canonical_elements(2)
    T=S[1:]
    count=0
    for perm in permutations(T):
        alpha={None:None}
        alpha.update(zip(T,perm))
        if is_complete(alpha): count+=1
    assert count==32
    return count

if __name__ == '__main__':
    print('Reduced enumeration:',reduced_enumeration())
    print('Independent exhaustive 8! enumeration:',full_permutation_enumeration())
    for n in (2,4,6,8,10):
        f = explicit(n)
        assert set(f) == set(canonical_elements(n))
        assert is_complete(f)
        print('Explicit family checked n=',n,'size=',len(f))
    print('All checks PASS')
