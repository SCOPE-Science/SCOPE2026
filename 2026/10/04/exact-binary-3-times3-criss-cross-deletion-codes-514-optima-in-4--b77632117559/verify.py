#!/usr/bin/env python3
import csv
import os
import sys
from collections import Counter
from functools import lru_cache

N = 3

def bit(x, r, c):
    return (x >> (N * N - 1 - (N * r + c))) & 1

def deletion_outcome_loops(x, deleted_row, deleted_col):
    y = 0
    for r in range(N):
        if r == deleted_row:
            continue
        for c in range(N):
            if c == deleted_col:
                continue
            y = (y << 1) | bit(x, r, c)
    return y

def deletion_outcome_strings(x, deleted_row, deleted_col):
    s = f"{x:09b}"
    rows = [s[3*r:3*r+3] for r in range(3)]
    rows.pop(deleted_row)
    reduced = "".join(row[:deleted_col] + row[deleted_col+1:] for row in rows)
    return int(reduced, 2)

def deletion_ball_mask(x):
    a = {deletion_outcome_loops(x, r, c) for r in range(3) for c in range(3)}
    b = {deletion_outcome_strings(x, r, c) for r in range(3) for c in range(3)}
    if a != b:
        raise AssertionError("independent deletion implementations disagree")
    mask = 0
    for y in a:
        mask |= 1 << y
    return mask

def transform(x, reverse_rows, reverse_cols, transpose, complement):
    a = [[bit(x, r, c) for c in range(3)] for r in range(3)]
    if reverse_rows:
        a = list(reversed(a))
    if reverse_cols:
        a = [list(reversed(row)) for row in a]
    if transpose:
        a = [list(row) for row in zip(*a)]
    if complement:
        a = [[1-z for z in row] for row in a]
    y = 0
    for row in a:
        for z in row:
            y = (y << 1) | z
    return y

def matrix_string(x):
    s = f"{x:09b}"
    return "/".join((s[:3], s[3:6], s[6:9]))

def build_census():
    balls = [deletion_ball_mask(x) for x in range(512)]
    ball_hist = Counter(m.bit_count() for m in balls)
    if ball_hist != Counter({1:2, 2:16, 3:28, 4:60, 5:102, 6:152, 7:86, 8:64, 9:2}):
        raise AssertionError("deletion-ball histogram mismatch")

    unique_balls = tuple(set(balls))
    @lru_cache(maxsize=None)
    def pack(available):
        best = 0
        for b in unique_balls:
            if b & ~available == 0:
                best = max(best, 1 + pack(available ^ b))
        return best
    packing_number = pack((1 << 16) - 1)
    if packing_number != 4:
        raise AssertionError("set-packing maximum mismatch")

    adj = [0] * 512
    for i in range(512):
        for j in range(i+1, 512):
            if balls[i] & balls[j] == 0:
                adj[i] |= 1 << j
                adj[j] |= 1 << i

    cliques = []
    for i in range(512):
        pi = adj[i] & ~((1 << (i+1)) - 1)
        t = pi
        while t:
            lb = t & -t
            j = lb.bit_length() - 1
            t -= lb
            pij = pi & adj[j] & ~((1 << (j+1)) - 1)
            u = pij
            while u:
                lb2 = u & -u
                k = lb2.bit_length() - 1
                u -= lb2
                pijk = pij & adj[k] & ~((1 << (k+1)) - 1)
                z = pijk
                while z:
                    lb3 = z & -z
                    ell = lb3.bit_length() - 1
                    z -= lb3
                    cliques.append((i, j, k, ell))
    if len(cliques) != 514:
        raise AssertionError("four-code census mismatch")

    maps = []
    seen = set()
    for rr in (0, 1):
        for rc in (0, 1):
            for tr in (0, 1):
                for cp in (0, 1):
                    mp = tuple(transform(x, rr, rc, tr, cp) for x in range(512))
                    if mp not in seen:
                        seen.add(mp)
                        maps.append(mp)
    if len(maps) != 16:
        raise AssertionError("symmetry-group size mismatch")

    for mp in maps:
        for i in range(512):
            ti = mp[i]
            for j in range(i+1, 512):
                lhs = bool((adj[i] >> j) & 1)
                rhs = bool((adj[ti] >> mp[j]) & 1)
                if lhs != rhs:
                    raise AssertionError("claimed symmetry does not preserve compatibility")

    clique_set = set(cliques)
    orbits = {}
    for code in cliques:
        images = {tuple(sorted(mp[v] for v in code)) for mp in maps}
        if not images <= clique_set:
            raise AssertionError("symmetry image left optimum set")
        canonical = min(images)
        if canonical in orbits and orbits[canonical] != images:
            raise AssertionError("orbit inconsistency")
        orbits[canonical] = images
    if len(orbits) != 46:
        raise AssertionError("orbit count mismatch")
    orbit_hist = Counter(len(v) for v in orbits.values())
    if orbit_hist != Counter({2:1, 4:4, 8:20, 16:21}):
        raise AssertionError("orbit-size distribution mismatch")
    if sum(len(v) for v in orbits.values()) != 514:
        raise AssertionError("orbits do not partition the optima")

    rows = []
    for idx, (canonical, orbit) in enumerate(sorted(orbits.items()), 1):
        rows.append({
            "class": str(idx),
            "orbit_size": str(len(orbit)),
            "canonical_code": ";".join(matrix_string(v) for v in canonical),
            "deletion_ball_sizes": ";".join(map(str, sorted(balls[v].bit_count() for v in canonical))),
            "weights": ";".join(map(str, sorted(v.bit_count() for v in canonical))),
        })
    return balls, rows, orbit_hist, pack.cache_info()

def write_csv(path, rows):
    fields = ["class", "orbit_size", "canonical_code", "deletion_ball_sizes", "weights"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def main():
    balls, rows, orbit_hist, cache_info = build_census()
    here = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(here, "classes.csv")
    if "--emit-classes" in sys.argv:
        write_csv(csv_path, rows)
    if not os.path.exists(csv_path):
        raise AssertionError("classes.csv is missing")
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        stored = list(csv.DictReader(f))
    if stored != rows:
        raise AssertionError("classes.csv does not match recomputed census")
    witness = [0b000000000, 0b000011101, 0b011011011, 0b110101000]
    for i in range(4):
        for j in range(i+1, 4):
            if balls[witness[i]] & balls[witness[j]]:
                raise AssertionError("stored witness is not a code")
    print("maximum_cardinality=4")
    print("optimal_labeled_codes=514")
    print("symmetry_classes=46")
    print("orbit_size_distribution=2:1,4:4,8:20,16:21")
    print("deletion_ball_size_distribution=1:2,2:16,3:28,4:60,5:102,6:152,7:86,8:64,9:2")
    print(f"set_packing_dp_states={cache_info.currsize}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
