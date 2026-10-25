from math import comb

N, R = 8, 3
ball_size = sum(comb(N, k) for k in range(R + 1))
assert ball_size == 93
assert sum(comb(9, k) for k in range(5)) == 256
assert sum(k * comb(9, k) for k in range(5)) == 837
assert 9 * ball_size == 837
assert sum(comb(7, k) for k in range(3)) == 29

def intersection(d: int) -> int:
    """Intersection size of two radius-three balls whose centers differ in d places."""
    total = 0
    for a in range(d + 1):
        for b in range(N - d + 1):
            if a + b <= R and d - a + b <= R:
                total += comb(d, a) * comb(N - d, b)
    return total

table = [intersection(d) for d in range(N + 1)]
assert table == [93, 58, 58, 38, 38, 20, 20, 0, 0]
assert 29 not in table
print("ball_size=93")
print("signature_count=256; minimum_total_weight=837")
print("forced_pairwise_intersection=29")
print("intersection_table=", table)
print("PASS: no nine-query separating family exists by the stated obstruction")

