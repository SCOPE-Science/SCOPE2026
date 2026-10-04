from functools import lru_cache

# B_n is represented as the powerset of an n-element atom set; elements are bitmasks.
def cell_pattern(n, tup):
    pattern = 0
    for atom in range(n):
        sig = 0
        for i, x in enumerate(tup):
            if (x >> atom) & 1:
                sig |= 1 << i
        pattern |= 1 << sig
    return pattern

@lru_cache(None)
def duplicator_wins(n, m, left, right, rounds):
    # Equality of Boolean terms in selected elements is determined by which Venn cells are empty.
    if cell_pattern(n, left) != cell_pattern(m, right):
        return False
    if rounds == 0:
        return True

    for x in range(1 << n):
        if not any(duplicator_wins(n, m, left + (x,), right + (y,), rounds - 1)
                   for y in range(1 << m)):
            return False
    for y in range(1 << m):
        if not any(duplicator_wins(n, m, left + (x,), right + (y,), rounds - 1)
                   for x in range(1 << n)):
            return False
    return True

def predicted(n, m, q):
    return min(n, 1 << q) == min(m, 1 << q)

cases = 0
for n in range(1, 5):
    for m in range(1, 5):
        for q in range(4):
            got = duplicator_wins(n, m, (), (), q)
            want = predicted(n, m, q)
            assert got == want, (n, m, q, got, want)
            cases += 1

print(f"VERIFY_OK cases={cases} states={duplicator_wins.cache_info().currsize}")
