#!/usr/bin/env python3
import json
from itertools import product, combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = json.loads((ROOT / "certificates.json").read_text(encoding="utf-8"))
WORDS = ["".join(p) for p in product("01", repeat=6)]


def pal_dup_descendants(word, ell=2):
    out = set()
    for i in range(len(word) - ell + 1):
        block = word[i:i + ell]
        out.add(word[:i + ell] + block[::-1] + word[i + ell:])
    return out


def pal_del_descendants(word, ell=2):
    out = set()
    for i in range(len(word) - 2 * ell + 1):
        window = word[i:i + 2 * ell]
        left = window[:ell]
        if window[ell:] == left[::-1]:
            out.add(word[:i + ell] + word[i + 2 * ell:])
    return out


def conflict_edges(desc):
    direct = set()
    for a, b in combinations(WORDS, 2):
        if desc(a) & desc(b):
            direct.add((a, b))

    by_output = {}
    for w in WORDS:
        for y in desc(w):
            by_output.setdefault(y, []).append(w)
    inverse = set()
    for parents in by_output.values():
        for a, b in combinations(sorted(set(parents)), 2):
            inverse.add((a, b))
    assert direct == inverse
    return direct


def check_independent(code, edges):
    code = list(code)
    assert len(code) == len(set(code))
    assert all(w in WORDS for w in code)
    edge_set = set(edges)
    for a, b in combinations(sorted(code), 2):
        assert (a, b) not in edge_set


def check_pair_partition(pairs, edges, expected_unmatched):
    seen = set()
    for pair in pairs:
        assert len(pair) == 2
        a, b = sorted(pair)
        assert (a, b) in edges
        assert a not in seen and b not in seen
        seen.update((a, b))
    assert len(WORDS) - len(seen) == expected_unmatched


def check_deletion_partition(triangles, pairs, edges):
    seen = set()
    for tri in triangles:
        assert len(tri) == 3
        assert len(set(tri)) == 3
        for w in tri:
            assert w not in seen
        for a, b in combinations(sorted(tri), 2):
            assert (a, b) in edges
        seen.update(tri)
    for pair in pairs:
        assert len(pair) == 2
        a, b = sorted(pair)
        assert (a, b) in edges
        assert a not in seen and b not in seen
        seen.update((a, b))
    singletons = set(WORDS) - seen
    assert len(triangles) == 8
    assert len(pairs) == 6
    assert len(singletons) == 28
    return singletons


def main():
    assert CERT["word_length"] == 6
    assert CERT["duplication_length"] == 2
    dup_edges = conflict_edges(pal_dup_descendants)
    del_edges = conflict_edges(pal_del_descendants)
    assert len(dup_edges) == 56
    assert len(del_edges) == 34

    cdup = CERT["duplication_lower_witness"]
    cdel = CERT["deletion_lower_witness"]
    assert len(cdup) == 40
    assert len(cdel) == 42
    check_independent(cdup, dup_edges)
    check_independent(cdel, del_edges)

    dup_pairs = CERT["duplication_upper_pairs"]
    assert len(dup_pairs) == 24
    check_pair_partition(dup_pairs, dup_edges, expected_unmatched=16)
    # Each independent set uses at most one endpoint of every certified pair,
    # plus at most all 16 unmatched vertices: alpha <= 24 + 16 = 40.
    dup_upper = len(dup_pairs) + 16
    assert dup_upper == 40

    del_singletons = check_deletion_partition(
        CERT["deletion_upper_triangles"],
        CERT["deletion_upper_pairs"],
        del_edges,
    )
    # The listed cliques together with the remaining singleton vertices form
    # a partition; an independent set meets every clique in at most one vertex.
    del_upper = (
        len(CERT["deletion_upper_triangles"])
        + len(CERT["deletion_upper_pairs"])
        + len(del_singletons)
    )
    assert del_upper == 42

    print("WORDS=64")
    print("DUP_CONFLICT_EDGES=56")
    print("DEL_CONFLICT_EDGES=34")
    print("DUP_LOWER=40 DUP_UPPER=40")
    print("DEL_LOWER=42 DEL_UPPER=42")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
