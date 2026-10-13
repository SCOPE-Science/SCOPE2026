from fractions import Fraction


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for a in range(max_part, 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def score(partition):
    value = Fraction(1, 1)
    for a in partition:
        value *= Fraction(a + 1, 2)
    return value


def predicted(m):
    if m == 1:
        return Fraction(1, 1), {(1,)}
    if m == 2:
        return Fraction(3, 2), {(2,)}
    if m == 5:
        return Fraction(3, 1), {(5,), (3, 2)}
    r = m % 3
    if r == 0:
        q = m // 3
        return Fraction(2**q, 1), {tuple([3] * q)}
    if r == 1:
        q = (m - 1) // 3
        return Fraction(5, 2) * 2**(q - 1), {tuple([4] + [3] * (q - 1))}
    q = (m - 2) // 3
    if q >= 2:
        return Fraction(25, 4) * 2**(q - 2), {tuple([4, 4] + [3] * (q - 2))}
    raise AssertionError("unhandled small case")


checked_partitions = 0
for m in range(1, 41):
    best = Fraction(0, 1)
    equality = set()
    for part in partitions(m):
        checked_partitions += 1
        value = score(part)
        if value > best:
            best = value
            equality = {part}
        elif value == best:
            equality.add(part)
    want_value, want_equality = predicted(m)
    assert best == want_value, (m, best, want_value)
    assert equality == want_equality, (m, equality, want_equality)

print(f"VERIFY_OK m_max=40 partitions_checked={checked_partitions} equality_layers=40")
