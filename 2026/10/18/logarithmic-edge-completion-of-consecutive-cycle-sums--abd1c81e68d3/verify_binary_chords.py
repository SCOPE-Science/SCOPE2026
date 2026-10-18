"""Independent finite checks for binary-chord connected subset sums.

Run: python3 verify_binary_chords.py
"""
from collections import deque
import random


def chords(n):
    return [(n, 1 << j) for j in range(1, n.bit_length()) if (1 << j) <= n - 2]


def witness(n, target):
    if not 1 <= target <= n * (n + 1) // 2:
        raise ValueError('target outside allowed range')
    if target < n:
        return {target}
    if target == n * (n + 1) // 2:
        return set(range(1, n+1))
    # S_t = sum(t,...,n), with S_t <= target < S_(t-1).
    t = n
    while t > 2 and (n * (n + 1) - (t - 1) * t) // 2 + (t-1) <= target:
        t -= 1
    s = (n * (n + 1) - (t-1) * t) // 2
    if not s <= target < s + t - 1:
        raise AssertionError(('suffix mismatch', n, target, t, s))
    residue = target - s
    result = set(range(t,n+1))
    bit = 1
    while residue:
        if residue & 1:
            result.add(bit)
        residue >>= 1
        bit <<= 1
    return result


def check_witness(n, target):
    v = witness(n, target)
    assert sum(v) == target, (n,target,v)
    edges = {i: set() for i in v}
    for a,b in [(i,i+1) for i in range(1,n)] + [(1,n)] + chords(n):
        if a in v and b in v:
            edges[a].add(b)
            edges[b].add(a)
    seen = {next(iter(v))}
    queue = deque(seen)
    while queue:
        u = queue.popleft()
        for w in edges[u] - seen:
            seen.add(w)
            queue.append(w)
    assert seen == v, (n,target,v,seen)
    return True


def main():
    rng=random.Random(1729)
    cases=0
    for n in range(3,81):
        cs=chords(n)
        assert len(cs) <= max(0,(n-2).bit_length()-1)
        assert len(cs)==len(set(cs))
        for a,b in cs:
            assert 1<=b<=n-2 and b&(b-1)==0
            assert b!=1
        for target in range(1,n*(n+1)//2+1):
            check_witness(n,target)
            cases+=1
    samples=0
    for n in [81,97,128,129,255,256,257,500,1000,10000,65537]:
        targets={1,n,n+1,n+2,n*(n+1)//2-2,n*(n+1)//2-1,n*(n+1)//2}
        targets.update(rng.randint(1,n*(n+1)//2) for _ in range(80))
        for target in sorted(targets):
            check_witness(n,target)
            samples+=1
    print(f'PASS: {cases} exhaustive target instances for 3<=n<=80; {samples} large-n sampled instances; binary-chord count and connectedness verified')

if __name__=='__main__':
    main()
