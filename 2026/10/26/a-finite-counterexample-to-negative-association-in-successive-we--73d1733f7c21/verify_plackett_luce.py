from fractions import Fraction
from itertools import permutations

WEIGHTS = (1, 34, 37, 1, 1)
K = 3
N = len(WEIGHTS)
TOTAL = sum(WEIGHTS)

# Exact Plackett-Luce probability of the ordered top-k sequence.
sequence_probabilities = {}
for order in permutations(range(N), K):
    remaining = TOTAL
    probability = Fraction(1, 1)
    for index in order:
        probability *= Fraction(WEIGHTS[index], remaining)
        remaining -= WEIGHTS[index]
    sequence_probabilities[order] = probability

assert sum(sequence_probabilities.values(), Fraction(0, 1)) == 1
marginals = []
for item in range(N):
    marginals.append(sum((p for order, p in sequence_probabilities.items() if item in order), Fraction(0, 1)))

def joint_inclusion(i, j):
    return sum((p for order, p in sequence_probabilities.items() if i in order and j in order), Fraction(0, 1))

p2 = marginals[1]
p3 = marginals[2]
p23 = joint_inclusion(1, 2)
cov = p23 - p2 * p3
assert p2 == Fraction(10761, 10804)
assert p3 == Fraction(113507, 113880)
assert p23 == Fraction(2091527, 2106780)
assert cov == Fraction(2941, 1230359520) > 0
print('ordered_sequences', len(sequence_probabilities))
print('normalization', sum(sequence_probabilities.values(), Fraction(0, 1)))
print('P(I_2=1)', p2)
print('P(I_3=1)', p3)
print('P(I_2=I_3=1)', p23)
print('Cov(I_2,I_3)', cov)
