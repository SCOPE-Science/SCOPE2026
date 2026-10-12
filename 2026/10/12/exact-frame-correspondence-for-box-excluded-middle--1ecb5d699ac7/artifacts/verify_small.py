def is_poset(n, le):
    if any((i, i) not in le for i in range(n)):
        return False
    for i in range(n):
        for j in range(n):
            if i != j and (i, j) in le and (j, i) in le:
                return False
    for i, j in tuple(le):
        for k in range(n):
            if (j, k) in le and (i, k) not in le:
                return False
    return True

def base_ok(n, le, rel):
    return all((x, z) in rel for x, y in le for yy, z in rel if yy == y)

def exact_condition(n, le, rel):
    for x, y in le:
        for xx, z in rel:
            if xx == x and not any((y, u) in rel and (u, z) in le for u in range(n)):
                return False
    return True

def paper_BEM(n, le, rel):
    return all((y, z) in rel for x, y in le for xx, z in rel if xx == x)

def atomic_bem_valid(n, le, rel):
    for mask in range(1 << n):
        truth = {i for i in range(n) if (mask >> i) & 1}
        if any(i in truth and (i, j) in le and j not in truth for i in range(n) for j in range(n)):
            continue
        for x in range(n):
            box_x = all(z in truth for xx, z in rel if xx == x)
            if box_x:
                continue
            neg_box_x = True
            for y in range(n):
                if (x, y) in le:
                    box_y = all(z in truth for yy, z in rel if yy == y)
                    if box_y:
                        neg_box_x = False
                        break
            if not neg_box_x:
                return False
    return True

def main():
    expected = {1: (2, 0), 2: (34, 2), 3: (2942, 270)}
    for n in (1, 2, 3):
        pairs = [(i, j) for i in range(n) for j in range(n)]
        frames = 0
        strict = 0
        for le_bits in range(1 << (n * n)):
            le = {p for k, p in enumerate(pairs) if (le_bits >> k) & 1}
            if not is_poset(n, le):
                continue
            for r_bits in range(1 << (n * n)):
                rel = {p for k, p in enumerate(pairs) if (r_bits >> k) & 1}
                if not base_ok(n, le, rel):
                    continue
                frames += 1
                exact = exact_condition(n, le, rel)
                semantic = atomic_bem_valid(n, le, rel)
                assert exact == semantic
                if exact and not paper_BEM(n, le, rel):
                    strict += 1
        assert (frames, strict) == expected[n]
        print(f"n={n}: frames={frames}, exact_vs_atomic_mismatches=0, exact_not_BEM={strict}")

    n = 2
    le = {(0, 0), (1, 1), (0, 1)}
    rel = {(0, 0), (0, 1), (1, 0)}
    assert base_ok(n, le, rel)
    assert exact_condition(n, le, rel)
    assert atomic_bem_valid(n, le, rel)
    assert not paper_BEM(n, le, rel)
    print("two_point_witness=OK")

    n = 4
    le = {(i, i) for i in range(n)} | {(0, 1), (3, 2)}
    rel = {(0, 2), (0, 3), (1, 3)}
    assert base_ok(n, le, rel)
    assert exact_condition(n, le, rel)
    assert atomic_bem_valid(n, le, rel)
    assert not paper_BEM(n, le, rel)
    print("published_four_point_example=OK")

if __name__ == "__main__":
    main()
