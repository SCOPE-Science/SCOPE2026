"""Finite exact checks accompanying the finite-word theorem.

Run: python3 verify.py
All calculations are integer-valued. These checks do not certify the asymptotic theorem.
"""
from collections import defaultdict
from itertools import product
from math import comb


def count_brackets_direct(m, n):
    """Check all labeled words via a stack, independently of the GF."""
    total = 0
    for symbols in product(range(2*m), repeat=n):
        stack = []
        valid = True
        for letter in symbols:
            if letter < m:
                stack.append(letter)
            elif stack:
                if stack.pop() != letter-m:
                    valid = False
                    break
        total += valid
    return total


def count_weighted_skeleton(m, n):
    """Count push-label choices and initial free pop-digit choices."""
    states = {(0, 0): 1}  # (current height of pop-minus-push, max height)
    for _ in range(n):
        nxt = defaultdict(int)
        for (s, maximum), count in states.items():
            nxt[(s-1, maximum)] += m*count  # m labeled pushes
            nxt[(s+1, max(maximum, s+1))] += count  # generic pop
        states = nxt
    return sum(count*m**maximum for (s, maximum), count in states.items())


def count_generating_function(m, length):
    """Extract coefficients of (1-g)/((1-(m+1)t)(1-mg)), g=t+mtg^2."""
    g = [0]*(length+1)
    for j in range((length-1)//2+1):
        g[2*j+1] = comb(2*j,j)//(j+1)*m**j
    d = [0]*(length+1)
    d[0] = 1
    for j in range(1,length+1):
        d[j] = -(m+1)*(j == 1) - m*g[j] + m*(m+1)*g[j-1]
    a = [0]*(length+1)
    for j in range(length+1):
        a[j] = (j == 0) - g[j] - sum(d[k]*a[j-k] for k in range(1,j+1))
    return a


def main():
    max_lengths = {2: 8, 3: 6, 4: 5}
    comparisons = 0
    for m, limit in max_lengths.items():
        values = count_generating_function(m, 12)
        for n in range(limit+1):
            direct = count_brackets_direct(m, n)
            weighted = count_weighted_skeleton(m, n)
            assert direct == weighted == values[n], (m,n,direct,weighted,values[n])
            comparisons += 1
        for n in range(13):
            assert count_weighted_skeleton(m, n) == values[n]
            comparisons += 1
        if m == 2:
            assert values[:11] == [1,4,14,48,160,528,1720,5568,17888,57216,182080]
    print('VERIFY_OK:', comparisons, 'integer equalities; m in 2..4')


if __name__ == '__main__':
    main()
