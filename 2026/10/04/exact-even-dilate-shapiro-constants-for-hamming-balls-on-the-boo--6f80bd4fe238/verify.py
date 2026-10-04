import math

def popcount(x):
    return x.bit_count()

def verify_case(d, r):
    radius = min(2*r, d)
    points = list(range(1 << d))
    ball = [x for x in points if popcount(x) <= radius]
    even = [x for x in ball if popcount(x) % 2 == 0]
    odd = [x for x in ball if popcount(x) % 2 == 1]
    E, O = len(even), len(odd)

    assert E == sum(math.comb(d,w) for w in range(radius+1) if w % 2 == 0)
    assert O == sum(math.comb(d,w) for w in range(radius+1) if w % 2 == 1)
    assert O <= d*E

    for xi in points:
        j = popcount(xi)
        coeff = sum(1 if popcount(xi & x) % 2 == 0 else -1 for x in ball)
        rhs_num = d*E + O*(d - 2*j)
        assert d*coeff <= rhs_num
        if xi != 0:
            assert coeff <= E - O

    # Exact extremizer f = indicator of the even-parity subgroup.
    denominator = sum(1 for x in points if popcount(x) <= 1 and popcount(x) % 2 == 0)
    numerator = sum(1 for x in ball if popcount(x) % 2 == 0)
    assert denominator == 1
    assert numerator == E

    # Its Walsh transform is nonnegative.
    for xi in points:
        ft = sum(
            (1 if popcount(x) % 2 == 0 else 0)
            * (1 if popcount(xi & x) % 2 == 0 else -1)
            for x in points
        )
        assert ft >= 0

count = 0
for d in range(1, 11):
    for r in range(1, 7):
        verify_case(d, r)
        count += 1

print(f"CASES={count}")
print("VERIFY_OK")
