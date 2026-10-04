from fractions import Fraction
from itertools import combinations, product

W = {
    "0000": Fraction(3,5), "0001": Fraction(2,5), "0011": Fraction(1,5), "0111": Fraction(2,5),
    "1000": Fraction(2,5), "1100": Fraction(1,5), "1110": Fraction(2,5), "1111": Fraction(3,5),
}
C = ["000000", "000001", "011100", "100110", "101111", "110001", "111111"]

def subsequences_after_two_deletions(x):
    out=set()
    for d in combinations(range(6),2):
        out.add(''.join(x[i] for i in range(6) if i not in d))
    return out

# Upper-bound certificate: exact arithmetic over all 64 ambient words.
min_lhs=None
for bits in product('01', repeat=6):
    x=''.join(bits)
    lhs=sum((W.get(y,Fraction(0)) for y in subsequences_after_two_deletions(x)), Fraction(0))
    if x in ("000000","111111"):
        lhs += Fraction(2,5)
    assert lhs >= 1, (x,lhs)
    min_lhs = lhs if min_lhs is None or lhs < min_lhs else min_lhs

assert sum(W.values(), Fraction(0)) == Fraction(16,5)
upper = 2*sum(W.values(), Fraction(0)) + 2*Fraction(2,5)
assert upper == Fraction(36,5)
assert upper < 8

# Lower-bound witness: every received length-four word belongs to at most two codewords.
mult={}
for x in C:
    for y in subsequences_after_two_deletions(x):
        mult[y]=mult.get(y,0)+1
assert max(mult.values(), default=0) <= 2
assert len(C) == 7
print("VERIFY_OK")
print("minimum_pointwise_lhs", min_lhs)
print("fractional_upper", upper)
print("witness_size", len(C))
print("max_received_multiplicity", max(mult.values()))
