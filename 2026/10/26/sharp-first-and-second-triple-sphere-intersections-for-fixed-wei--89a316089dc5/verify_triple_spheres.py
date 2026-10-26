"""Exact independent checks of three-center equal-radius sphere intersection bounds.

Uses only the Python standard library. All arithmetic is integer-exact.
For a triple, translate the first center to zero and partition coordinates
into those where the other two centers have patterns 10, 01, 11, 00.
"""
from itertools import combinations
from math import comb


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def triple_count_by_profile(n, t, a, b, c):
    """Exact count for column profiles (10,01,11,00)=(a,b,c,n-a-b-c)."""
    d = n-a-b-c
    if min(a, b, c, d) < 0 or not (a+c and b+c and a+b):
        return 0
    if (a+c) % 2 or (b+c) % 2:
        return 0
    alpha, beta = (a+c)//2, (b+c)//2
    return sum(choose(c, h)*choose(a, alpha-h)*choose(b, beta-h)
               *choose(d, t-alpha-beta+h) for h in range(c+1))


def brute_count(n, t, y, z):
    ans = 0
    for pos in combinations(range(n), t):
        x = sum(1 << j for j in pos)
        ans += ((x ^ y).bit_count() == t and (x ^ z).bit_count() == t)
    return ans


def profile_from_centers(n, y, z):
    mask = (1 << n)-1
    a = (y & (~z) & mask).bit_count()
    b = (z & (~y) & mask).bit_count()
    c = (y & z).bit_count()
    return a,b,c


def check():
    profile_count = 0
    exhaustive_types = 0
    for t in range(2, 6):
        for n in range(4*t, 4*t+5):
            high = choose(n-2, t-1)
            runner = 4*choose(n-4, t-2)
            assert 0 < runner < high
            top_types, runner_types = set(), set()
            for a in range(n+1):
                for b in range(n-a+1):
                    for c in range(n-a-b+1):
                        v = triple_count_by_profile(n, t, a, b, c)
                        if v == high: top_types.add((a,b,c))
                        if v == runner: runner_types.add((a,b,c))
                        assert v <= high
                        if sorted((a+b,a+c,b+c)) != [2,2,2]:
                            assert v <= runner, (n,t,a,b,c,v,runner)
                        elif v != high:
                            raise AssertionError((n,t,a,b,c,v,high))
                        if v == runner:
                            assert sorted((a+b,a+c,b+c)) == [2,2,4]
                        profile_count += 1
            assert top_types == {(1,1,1)}
            assert runner_types == {(0,2,2),(2,0,2),(2,2,0)}
            exhaustive_types += 1
    direct_count = 0
    for t in (2,3,4):
        n=4*t
        centers = [((1<<2)-1,(1<<1)|(1<<2)),
                   ((1<<2)-1,((1<<2)-1)<<2),
                   (0b1111,0b0011),
                   (0b110011, 0b101010),
                   (0b111111, 0b101010)]
        for y,z in centers:
            if max(y,z) >= 1<<n:continue
            a,b,c=profile_from_centers(n,y,z)
            independent=brute_count(n,t,y,z)
            formula=triple_count_by_profile(n,t,a,b,c)
            assert independent==formula, (n,t,y,z,independent,formula)
            direct_count+=1
    print('TRIPLE_SPHERE_VERIFY_OK')
    print('complete parameter grids:',exhaustive_types)
    print('center-profile evaluations:',profile_count)
    print('independent direct word enumerations:',direct_count)
    print('n=12, t=3: maximum={}, runner-up={}'.format(choose(10,2),4*choose(8,1)))

if __name__ == '__main__':
    check()
