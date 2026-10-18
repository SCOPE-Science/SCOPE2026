"""Independent finite checks for length-two reverse-complement irreducible words."""
from itertools import product
from collections import defaultdict


def recurrence(q, end):
    vals = [1, q, q*q, q*q*q]
    for n in range(4, end + 1):
        injection = {4:q, 5:q}.get(n, 0)
        vals.append((q-1)*vals[n-1] + (q-2)*vals[n-2]
                    + (q-1)*vals[n-3] + injection)
    return vals


def automaton_dp(q, end):
    assert q >= 2 and q % 2 == 0
    vals = [1, q, q*q, q**3]
    states = {t:1 for t in product(range(q), repeat=3)}
    for n in range(4, end + 1):
        nxt = defaultdict(int)
        for (a,b,c), wt in states.items():
            for d in range(q):
                if a == (d ^ 1) and b == (c ^ 1):
                    continue
                nxt[(b,c,d)] += wt
        states = nxt
        vals.append(sum(states.values()))
    return vals


def direct_count(q, n):
    total = 0
    for word in product(range(q), repeat=n):
        if all(not (word[i] == (word[i+3] ^ 1)
                    and word[i+1] == (word[i+2] ^ 1))
               for i in range(n-3)):
            total += 1
    return total


def check_conjugacy(q, n):
    for word in product(range(q), repeat=n):
        rc = any(word[i] == (word[i+3] ^ 1)
                 and word[i+1] == (word[i+2] ^ 1)
                 for i in range(n-3))
        y = tuple(a ^ (i % 2) for i, a in enumerate(word))
        pal = any(y[i] == y[i+3] and y[i+1] == y[i+2]
                  for i in range(n-3))
        assert rc == pal, (q, word)


if __name__ == '__main__':
    for q, maximum in [(2,16), (4,8), (6,6), (8,5)]:
        pred = recurrence(q, 35)
        states = automaton_dp(q, 35)
        assert pred == states, (q, pred, states)
        for n in range(4, maximum+1):
            assert direct_count(q,n) == pred[n], (q,n,pred[n])
        check_conjugacy(q, min(maximum, 6))
        print('alphabet',q,'literal_through',maximum,
              'states_through',35,'initial_values',pred[:9])
    print('ALL_CHECKS_PASSED')
