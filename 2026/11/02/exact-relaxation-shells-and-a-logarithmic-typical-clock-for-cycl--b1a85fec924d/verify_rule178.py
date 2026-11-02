#!/usr/bin/env python3
"""Independent finite checks of exact first-periodic-entry counts for rule 178.

Requires Python 3 standard library only.  Not an infinite-size certificate;
the all-size assertions require the combinatorial proof in RESULT.md.
"""
from collections import Counter
from math import comb


def next_state(x, n):
    y = 0
    for i in range(n):
        l = (x >> ((i - 1) % n)) & 1
        c = (x >> i) & 1
        r = (x >> ((i + 1) % n)) & 1
        v = (l & r) if c else (l | r)
        y |= v << i
    return y


def wall_word(x, n):
    return [((x >> i) ^ (x >> ((i + 1) % n))) & 1 for i in range(n)]


def exact_time_from_walls(x, n):
    d = wall_word(x, n)
    walls = [i for i, v in enumerate(d) if v]
    if not walls:
        return 0
    return max((((walls[(j + 1) % len(walls)] - w - 1) % n) // 2)
               for j, w in enumerate(walls))


def finite_trajectory(x, n):
    seen = {}
    step = 0
    while x not in seen:
        seen[x] = step
        x = next_state(x, n)
        step += 1
    return seen[x], step - seen[x]


def bounded_compositions(k, m, width):
    # Coefficient of z^m in (1 + z + ... + z^width)^k.
    return sum(((-1) ** j) * comb(k, j) * comb(m - j*(width+1)+k-1, k-1)
               for j in range(min(k, m//(width+1)) + 1))


def cumulative(n, t):
    width = 2*t + 1
    total = 2  # Both constant fixed configurations.
    for k in range(2, n+1, 2):
        b = bounded_compositions(k, n-k, width)
        assert (n*b) % k == 0, (n,t,k,b)
        total += 2*((n*b)//k)
    return total


def lucas(n):
    a,b = 2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def cosine_twice(n):
    return 2 if n%3==0 else -1


def main():
    checked=0
    for n in range(3,18):
        shell=Counter()
        p2=0
        for x in range(1<<n):
            t,p=finite_trajectory(x,n)
            assert t==exact_time_from_walls(x,n), (n,x,t)
            assert p==(1 if x in (0,(1<<n)-1) else 2), (n,x,t,p)
            shell[t]+=1
            p2+=p==2 and t==0
            checked+=1
        maxt=(n-2)//2
        assert max(shell)==maxt
        assert shell[maxt]==(2*n if n%2==0 else 4*n) if maxt>0 else True
        assert sum(shell.values())==1<<n
        for t in range(maxt+1):
            assert sum(v for s,v in shell.items() if s<=t)==cumulative(n,t), (n,t,shell)
        assert p2 == lucas(n)+cosine_twice(n), (n,p2)
        print(f'n={n:2d}: periodic={cumulative(n,0):6d} maxT={maxt:2d} '
              f'terminal={shell[maxt]:6d} total={1<<n:6d}')
    print('RULE178_ALL_CHECKS_PASSED; enumerated_states=',checked)


if __name__=='__main__':
    main()
