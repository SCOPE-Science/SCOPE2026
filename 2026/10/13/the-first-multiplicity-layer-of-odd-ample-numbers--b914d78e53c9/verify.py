from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import prod
import json

ODD_PRIMES = (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)


def partitions(n, max_part=None):
    """All integer partitions of n in weakly decreasing order, exactly once."""
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


@lru_cache(None)
def recursive_divisor_value(part):
    """a(n) for any n whose positive prime-exponent multiset is part."""
    part = tuple(x for x in part if x)
    if not part:
        return 1
    total = 1
    for sub in product(*(range(e+1) for e in part)):
        if sub == part:
            continue
        normalized = tuple(sorted((x for x in sub if x), reverse=True))
        total += recursive_divisor_value(normalized)
    return total


def minimum_odd_representative(part):
    """Least odd integer having exponent multiset part."""
    return prod(p**e for p,e in zip(ODD_PRIMES, part))


def direct_recursive_value(factorization):
    divisors = [1]
    for p, e in factorization:
        divisors = [d * p**j for d in divisors for j in range(e+1)]
    divisors.sort()
    values = {}
    for n in divisors:
        values[n] = 1 + sum(values[d] for d in divisors if d < n and n % d == 0)
    return values[divisors[-1]], len(divisors)


def main():
    maxima = []
    expected_counts = [1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,297]
    total_checked = 0
    for k in range(1, 18):
        rows = []
        for part in partitions(k):
            a = recursive_divisor_value(part)
            n = minimum_odd_representative(part)
            rows.append((part, a, n))
        assert len(rows) == expected_counts[k-1]
        total_checked += len(rows)
        best = max(rows, key=lambda t: Fraction(t[1], t[2]))
        part, a, n = best
        maxima.append({
            "Omega": k,
            "partition_count": len(rows),
            "max_ratio_partition": list(part),
            "a_value": a,
            "minimum_odd_representative": n,
            "comparison": "<" if a < n else "=" if a == n else ">",
        })
        if k <= 16:
            assert all(a0 <= n0 for _, a0, n0 in rows)
        print(f"Omega={k:2d} partitions={len(rows):3d} max={part} a={a} min_odd={n} cmp={'<' if a<n else '=' if a==n else '>'}")

    qualifying = []
    for part in partitions(17):
        a = recursive_divisor_value(part)
        n = minimum_odd_representative(part)
        if a > n:
            qualifying.append((n, part, a))
    qualifying.sort()

    expected = [
        (488462349375, (8,4,2,1,1,1), 523830280192),
        (1139745481875, (7,4,3,1,1,1), 1163507844992),
        (3093594879375, (7,4,2,1,1,1,1), 3210476052352),
    ]
    assert qualifying == expected

    N0, P0, A0 = qualifying[0]
    assert N0 == 3**8 * 5**4 * 7**2 * 11 * 13 * 17
    assert A0 - N0 == 35367930817

    source_example = 3**9 * 5**5 * 7**2 * 11 * 13
    assert source_example == 430996190625
    source_a = recursive_divisor_value((9,5,2,1,1))
    assert source_a == 436791402496 > source_example

    direct_n0, d0 = direct_recursive_value(((3,8),(5,4),(7,2),(11,1),(13,1),(17,1)))
    direct_src, ds = direct_recursive_value(((3,9),(5,5),(7,2),(11,1),(13,1)))
    assert (direct_n0, d0) == (A0, 1080)
    assert (direct_src, ds) == (source_a, 720)

    certificate = {
        "schema_version": 1,
        "theorem_boundary": 17,
        "partitions_checked_Omega_1_through_17": total_checked,
        "maxima_by_Omega": maxima,
        "qualifying_minimal_representatives_at_Omega_17": [
            {"n": n, "partition": list(part), "a_value": a}
            for n, part, a in qualifying
        ],
        "boundary_minimum": {"n": N0, "partition": list(P0), "a_value": A0, "excess": A0-N0},
        "source_smallest_odd_ample_check": {"n": source_example, "partition": [9,5,2,1,1], "a_value": source_a},
        "direct_divisor_recurrence_checks": {"boundary_divisor_count": d0, "boundary_a_value": direct_n0, "source_divisor_count": ds, "source_a_value": direct_src},
    }
    with open("partition_certificate.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(certificate, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    print("qualifying_Omega17=", qualifying)
    print("total_partitions_checked=", total_checked)
    print("direct_checks=", (direct_n0, d0), (direct_src, ds))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
