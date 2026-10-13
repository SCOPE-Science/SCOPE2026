def wt(x):
    return x.bit_count()


def span2(a, b):
    return (0, a, b, a ^ b)


def subspaces2(n):
    seen = set()
    for a in range(1, 1 << n):
        for b in range(a + 1, 1 << n):
            S = tuple(sorted(span2(a, b)))
            if len(set(S)) == 4:
                seen.add(S)
    return sorted(seen)


def is_doubly_even(code):
    return all(wt(c) % 4 == 0 for c in code)


def d2_for_dimension_two(code):
    # Every nonzero word belongs to the unique two-dimensional subcode.
    return wt(code[1] | code[2] | code[3])


def generalized_covering_radius_two(code, n):
    # Directly evaluate max_X min_Y column-support weight of X-Y,
    # with X an arbitrary ordered pair of ambient binary words and
    # Y an ordered pair of codewords.
    code_pairs = [(u, v) for u in code for v in code]
    radius = 0
    for x in range(1 << n):
        for y in range(1 << n):
            best = min(wt((x ^ u) | (y ^ v)) for u, v in code_pairs)
            radius = max(radius, best)
    return radius


def check_small_codes():
    for n in (4, 5, 6, 7):
        spaces = subspaces2(n)
        de = [C for C in spaces if is_doubly_even(C)]
        pairs = set()
        for C in de:
            d = d2_for_dimension_two(C)
            r = generalized_covering_radius_two(C, n)
            assert d <= 2 * r
            assert (d - 2) // 2 <= r - 1
            pairs.add((d, r))
        print(f"n={n} subspaces2={len(spaces)} doubly_even={len(de)} pairs={sorted(pairs)}")


def check_parity_lemma():
    for a in range(21):
        for b in range(21):
            for c in range(21):
                if (a + c) % 4 == 0 and (b + c) % 4 == 0 and (a + b) % 4 == 0:
                    assert a % 2 == 0 and b % 2 == 0 and c % 2 == 0
    print("PARITY_OK")


if __name__ == "__main__":
    check_small_codes()
    check_parity_lemma()
    print("VERIFY_OK")
