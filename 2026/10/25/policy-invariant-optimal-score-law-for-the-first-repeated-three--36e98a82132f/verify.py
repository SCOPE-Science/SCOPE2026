"""Exact exhaustive certificate for yes/no card guessing on two copies of three types."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction

TYPES = 3
COPIES = 2
N = TYPES * COPIES

def all_words(counts, prefix=()):
    if sum(counts) == 0:
        yield prefix
        return
    for label, count in enumerate(counts):
        if count:
            nxt = list(counts)
            nxt[label] -= 1
            yield from all_words(tuple(nxt), prefix + (label,))

words = tuple(all_words((COPIES,) * TYPES))
assert len(words) == 90 and len(set(words)) == 90
full = (1 << len(words)) - 1
at = tuple(tuple(sum(1 << j for j,w in enumerate(words) if w[t] == g)
                 for g in range(TYPES)) for t in range(N))

@lru_cache(None)
def solve(mask, step):
    """(optimal unnormalized first moment, componentwise minimum and
    maximum score polynomial over all mean-optimal policies)."""
    if step == N:
        unit = (mask.bit_count(),)
        return (0, unit, unit)
    options = []
    for guess in range(TYPES):
        yes = mask & at[step][guess]
        no = mask ^ yes
        byes, lyes, uyes = solve(yes, step + 1)
        bno, lno, uno = solve(no, step + 1)
        mean = yes.bit_count() + byes + bno
        low = tuple(([0] + list(lyes))[j] + (list(lno) + [0])[j]
                    for j in range(N - step + 1))
        high = tuple(([0] + list(uyes))[j] + (list(uno) + [0])[j]
                     for j in range(N - step + 1))
        options.append((mean, low, high, guess))
    optimum = max(x[0] for x in options)
    eligible = [x for x in options if x[0] == optimum]
    return (optimum,
            tuple(min(x[1][j] for x in eligible) for j in range(N - step + 1)),
            tuple(max(x[2][j] for x in eligible) for j in range(N - step + 1)))

value, minimum, maximum = solve(full, 0)
assert (value, minimum, maximum) == (271,
    (0, 0, 33, 30, 21, 5, 1), (0, 0, 33, 30, 21, 5, 1))
assert sum(minimum) == 90
assert sum(i*c for i,c in enumerate(minimum)) == value
assert solve.cache_info().currsize == 11867

# Independent forward simulation of one policy chosen lexicographically among
# exact Bellman-optimal actions for each actual possible full deck.
def chosen_action(mask, step):
    first_moment = solve(mask, step)[0]
    for g in range(TYPES):
        yes = mask & at[step][g]
        no = mask ^ yes
        current = yes.bit_count() + solve(yes, step+1)[0] + solve(no, step+1)[0]
        if current == first_moment:
            return g
    raise AssertionError('no admissible Bellman action')

observed = Counter()
for word in words:
    mask = full
    hits = 0
    for step in range(N):
        guess = chosen_action(mask, step)
        correct = word[step] == guess
        hits += correct
        mask = (mask & at[step][guess]) if correct else (mask ^ (mask & at[step][guess]))
        assert mask
    observed[hits] += 1
assert tuple(observed[i] for i in range(N+1)) == minimum
assert Fraction(sum(i*observed[i] for i in range(N+1)),90) == Fraction(271,90)
assert Fraction(sum(i*i*observed[i] for i in range(N+1)),90)-Fraction(271,90)**2 == Fraction(7469,8100)
print('DECKS=90 STATES=11867 OPTIMAL_MEAN=271/90')
print('ALL_MEAN_OPTIMAL_POLICIES_SAME_SCORE_DISTRIBUTION=',minimum)
print('SAMPLE_OPTIMAL_POLICY_FORWARD_ENUMERATION=',tuple(observed[i] for i in range(N+1)))
print('OPTIMAL_SCORE_VARIANCE=7469/8100')
print('VERIFY_OK')
