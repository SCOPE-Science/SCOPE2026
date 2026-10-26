#!/usr/bin/env python3
"""Reproduce the wheel majority periodic-point census by two independent routes."""
from collections import defaultdict
from math import comb


def next_state(n, state):
    """Direct adjacency-majority updates; rim i uses i-1,i+1,hub."""
    hub = (state >> n) & 1
    ring = state & ((1 << n) - 1)
    rim_ones = ring.bit_count()
    new_hub = (rim_ones * 2 > n) or (rim_ones * 2 == n and hub)
    out = int(new_hub) << n
    for i in range(n):
        neighborhood = hub + ((ring >> ((i-1) % n)) & 1) + ((ring >> ((i+1) % n)) & 1)
        out |= int(neighborhood >= 2) << i
    return out


def count_by_brute_force(n):
    fixed, flipping, same_hub = 0, 0, 0
    for state in range(1 << (n+1)):
        successor = next_state(n, state)
        if next_state(n, successor) != state:
            continue
        if state == successor:
            fixed += 1
        elif ((state >> n) & 1) != ((successor >> n) & 1):
            flipping += 1
        else:
            same_hub += 1
    return fixed, flipping, same_hub


def no_isolated_one_runs_cycle(length):
    """Independent enumeration of the step-two graph's binary strings."""
    counts = defaultdict(int)
    for word in range(1 << length):
        bits = [(word >> i) & 1 for i in range(length)]
        if any(bits[i] and not (bits[(i-1) % length] or bits[(i+1) % length]) for i in range(length)):
            continue
        ones = sum(bits)
        one_edges = sum(bits[i] * bits[(i+1) % length] for i in range(length))
        counts[(ones, one_edges)] += 1
    return dict(counts)


def run_polynomial(length):
    """Cyclic positive 1-run lengths >=2 and positive 0-run lengths."""
    counts = defaultdict(int)
    counts[(0,0)] = 1
    counts[(length,length)] = 1
    for runs in range(1, length//3+1):
        for ones in range(2*runs, length-runs+1):
            numerator = length * comb(ones-runs-1,runs-1) * comb(length-ones-1,runs-1)
            assert numerator % runs == 0
            counts[(ones,ones-runs)] += numerator // runs
    return dict(counts)


def convolution(left,right):
    counts = defaultdict(int)
    for (a,b),x in left.items():
        for (c,d),y in right.items():
            counts[(a+c,b+d)] += x*y
    return dict(counts)


def formula(n):
    P = run_polynomial(n) if n % 2 else convolution(run_polynomial(n//2),run_polynomial(n//2))
    B = sum(v for (a,b),v in P.items() if 2*a>n and 2*b<n)
    return (2,2*B,4 if n%2==0 else 0),B


def verify():
    for length in range(2,15):
        assert no_isolated_one_runs_cycle(length) == run_polynomial(length), length
    values = []
    evaluated = 0
    for n in range(4,17):
        predicted,B = formula(n)
        actual = count_by_brute_force(n)
        assert predicted==actual,(n,predicted,actual)
        values.append((n,B,actual))
        evaluated += 1 << (n+1)
    for n,B,tup in values:
        print('rim=%d hub-flipping-two-cycle-orbits=%d periodic=(fixed=%d,flip-states=%d,fixed-hub-2cycle-states=%d)'%(n,B,*tup))
    print('OK: independently compared cyclic-run enumerators (lengths 2..14), %d complete wheel configurations for n=4..16.' % evaluated)

if __name__ == '__main__':
    verify()
