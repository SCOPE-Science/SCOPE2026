"""Self-contained finite checks for shortest absent subsequences of constrained binary cycles.

Usage: python3 verify_rotations.py
Only Python's standard library is required.
"""
from itertools import product
from collections import Counter


def next_table(w):
    n = len(w)
    table = [[n, n] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        table[i] = table[i+1].copy()
        table[i][int(w[i])] = i
    return table


def contained(table, word, n):
    j = 0
    for c in word:
        p = table[j][int(c)]
        if p == n:
            return False
        j = p + 1
    return True


def actual_missing(w, length):
    table = next_table(w)
    return {''.join(t) for t in product('01', repeat=length)
            if not contained(table, t, len(w))}


def predicted_missing(w):
    m = w.count('1')
    assert m >= 2
    n = len(w)
    out = {'1' * (m + 1)}
    if w[0] == '1':
        out.add('0' + '1' * m)
        assert w[1] == '0'
        # The initial gap ends at the second one.
        z = w.find('1', 1) - 1
        if z == 1:
            out.add('00' + '1' * (m - 1))
    elif w[-1] == '1':
        out.add('1' * m + '0')
        assert w[-2] == '0'
        previous = w.rfind('1', 0, n-1)
        z = n - previous - 2
        if z == 1:
            out.add('1' * (m - 1) + '00')
    else:
        assert w[0] == '0' and w[-1] == '0'
    return out


def is_valid_gaps(g):
    return 2 in g and all(not (g[i] == 1 and g[(i + 1) % len(g)] == 1)
                            for i in range(len(g)))


def missing_count_dp(w, length):
    """Count absent strings using distinct greedy-embedding states, not enumeration."""
    n = len(w)
    tab = next_table(w)
    states = {0: 1}
    lost = 0
    for _ in range(length):
        nxt = {}
        missing_now = 2*lost
        for j, count in states.items():
            for bit in (0, 1):
                p = tab[j][bit]
                if p == n:
                    missing_now += count
                else:
                    nxt[p+1] = nxt.get(p+1, 0) + count
        states, lost = nxt, missing_now
    return lost


def main():
    tested_cycles = tested_roots = tested_strings = 0
    for m in range(2, 11):
        for g in product((1, 2), repeat=m):
            if not is_valid_gaps(g):
                continue
            circular = ''.join('1' + '0' * v for v in g)
            n = len(circular)
            roots = [circular[i:] + circular[:i] for i in range(n)]
            actual_profile = Counter()
            for w in roots:
                actual = actual_missing(w, m+1)
                predicted = predicted_missing(w)
                assert actual == predicted, (m, g, w, actual, predicted)
                assert missing_count_dp(w, m+1) == len(actual)
                actual_profile[len(actual)] += 1
                tested_roots += 1
                tested_strings += 2**(m+1)
            t = g.count(2)
            assert all(actual_profile[j] == v for j,v in ((1,t),(2,2*t),(3,2*(m-t)))), (m,g,actual_profile)
            tested_cycles += 1

    fib = ['0', '01']
    for i in range(2, 12):
        fib.append(fib[-1] + fib[-2])
    fib_checks = 0
    a,b = 0,1
    standard_fib = [0,1]
    for _ in range(13):
        standard_fib.append(standard_fib[-1] + standard_fib[-2])
    for k in range(3, 12):
        circular = fib[k]
        m = circular.count('1')
        n = len(circular)
        assert m == standard_fib[k]
        assert all(forbidden not in circular*3 for forbidden in ('11','000','10101'))
        histogram = Counter()
        for i in range(n):
            w = circular[i:] + circular[:i]
            count = missing_count_dp(w, m+1)
            assert count == len(predicted_missing(w)), (k,i,count)
            histogram[count] += 1
            fib_checks += 1
        assert dict(histogram) == {1:standard_fib[k-1],
                                   2:2*standard_fib[k-1],
                                   3:2*standard_fib[k-2]}, (k,histogram)
    print('VERIFY_OK', 'gap_cycles=', tested_cycles,
          'gap_roots=',tested_roots,'tested_length_m_plus_1_words=',tested_strings,
          'fibonacci_roots=',fib_checks)


if __name__ == '__main__':
    main()
