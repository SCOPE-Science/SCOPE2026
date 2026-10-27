from fractions import Fraction as F
from itertools import product

# States are ordered (N, A); A is the sole accepting state.
P = {
    "a": ((F(1, 2), F(1, 2)), (F(1, 3), F(2, 3))),
    "b": ((F(1, 2), F(1, 2)), (F(1), F(0))),
    "c": ((F(0), F(1)), (F(2, 3), F(1, 3))),
}
pi = (F(1, 3), F(2, 3))

for letter, matrix in P.items():
    assert all(sum(row) == 1 for row in matrix), letter
    assert all(F(0) <= value <= F(1) for row in matrix for value in row), letter
assert sum(pi) == 1 and all(F(0) <= value <= F(1) for value in pi)

def acceptance(word):
    p_accept = pi[1]
    for letter in word:
        alpha = P[letter][0][1]
        beta = P[letter][1][1]
        p_accept = alpha + (beta - alpha) * p_accept
    return p_accept

words = ["".join(w) for w in product("abc", repeat=3)]
scores = {word: acceptance(word) for word in words}
target = "abc"
assert len(scores) == 27
assert scores[target] == F(47, 54)
competitors = {word: score for word, score in scores.items() if word != target}
max_competitor = max(competitors.values())
maximizers = [word for word, score in scores.items() if score == max(scores.values())]
assert max_competitor == F(23, 27)
assert [word for word, score in competitors.items() if score == max_competitor] == ["cbc"]
assert max(scores.values()) == scores[target]
assert scores[target] - max_competitor == F(1, 54)

# Independent exact table: rows are length-two prefixes; columns are final letters.
for prefix in ("aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"):
    print(prefix, *(str(scores[prefix + last]) for last in "abc"))
print("target=abc", scores[target])
print("max_competitor=cbc", max_competitor)
print("gap=", scores[target] - max_competitor)
print("VERIFY_OK")
