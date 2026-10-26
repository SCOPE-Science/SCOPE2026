#!/usr/bin/env python3
"""Reproduce and verify the n=5 nested-Hilbert initial-complex shelling.

Uses only the Python standard library. Run from this directory with:
    python verify.py
"""
from itertools import combinations
import json
from pathlib import Path

N = 5
ROOT = Path(__file__).resolve().parent
CERTIFICATE = ROOT / "data" / "shelling_order.json"
VERTICES = tuple((i, j) for i in range(1, N + 2) for j in range(1, N + 1))
VERTEX_SET = frozenset(VERTICES)

# The squarefree supports x_h, y_h, z_h from the published construction.
GENERATORS = []
for h in range(2, N + 2):
    GENERATORS.append(
        {(i, N + 2 - i) for i in range(2, h)}
        | {(i, N + 3 - i) for i in range(h + 1, N + 2)}
    )
for h in range(2, N + 2):
    GENERATORS.append(
        {(i, N + 1 - i) for i in range(1, h)}
        | {(i, N + 2 - i) for i in range(h + 1, N + 2)}
    )
for h in range(3, N + 2):
    GENERATORS.append(
        {(i, N + 3 - i) for i in range(3, h)}
        | {(i, N + 2 - i) for i in range(h, N + 2)}
        | {(i, N + 4 - i) for i in range(h + 1, N + 2)}
    )


def is_hitting_set(candidate):
    return all(candidate & generator for generator in GENERATORS)


def is_minimal_hitting_set(candidate):
    return is_hitting_set(candidate) and all(
        not is_hitting_set(candidate - {vertex}) for vertex in candidate
    )


def enumerate_c_facets():
    """Enumerate all minimal size-four hitting sets of the 14 generators."""
    return sorted(
        (frozenset(subset) for subset in combinations(VERTICES, 4)
         if is_minimal_hitting_set(set(subset))),
        key=lambda c: tuple(sorted(c)),
    )



def enumerate_minimal_transversals():
    """Complete transversal recursion; it does not assume covers have size four."""
    family = {frozenset()}
    for generator in GENERATORS:
        candidates = set()
        for cover in family:
            if cover & generator:
                candidates.add(cover)
            else:
                candidates.update(cover | {vertex} for vertex in generator)
        family = {
            cover for cover in candidates
            if not any(other < cover for other in candidates)
        }
    return family


def deterministic_shelling(c_facets):
    """Find a deterministic order using the shelling criterion on complements."""
    count = len(c_facets)

    def valid_next(j, order):
        current = c_facets[j]
        external_vertices = set()
        for k in order:
            earlier = c_facets[k]
            if len(current | earlier) == 5:
                external_vertices.update(earlier - current)
        return all(
            (c_facets[i] - current) & external_vertices
            for i in order
        )

    def score_candidate(j, order, unused):
        extended = order + [j]
        return sum(valid_next(q, extended) for q in unused if q != j)

    order = [0]
    unused = set(range(1, count))
    while unused:
        valid = [j for j in sorted(unused) if valid_next(j, order)]
        if not valid:
            raise AssertionError(f"deterministic shelling search stalled at {len(order)} facets")
        scores = [(score_candidate(j, order, unused), j) for j in valid]
        best_score = max(score for score, _ in scores)
        chosen = min(j for score, j in scores if score == best_score)
        order.append(chosen)
        unused.remove(chosen)
    return order


def verify_shelling_order(c_facets, order):
    """Check the pure shelling criterion directly on facets F=V\\C."""
    facets = [VERTEX_SET - c for c in c_facets]
    assert len(order) == len(facets)
    assert len(set(order)) == len(facets)
    for position, j in enumerate(order):
        if position == 0:
            continue
        current = facets[j]
        for earlier_index in order[:position]:
            intersection = facets[earlier_index] & current
            witnessed = any(
                len(facets[k] & current) == len(current) - 1
                and intersection <= (facets[k] & current)
                for k in order[:position]
            )
            if not witnessed:
                raise AssertionError(
                    f"shelling criterion failed at position={position + 1}, "
                    f"earlier facet={earlier_index + 1}, current facet={j + 1}"
                )


def main():
    assert len(VERTICES) == 30
    assert len(GENERATORS) == 14
    assert all(1 <= min(i for i, _ in g) and max(i for i, _ in g) <= 6 for g in GENERATORS)
    assert all(1 <= min(j for _, j in g) and max(j for _, j in g) <= 5 for g in GENERATORS)

    c_facets = enumerate_c_facets()
    all_minimal_covers = enumerate_minimal_transversals()
    assert len(all_minimal_covers) == 130, f"expected 130 minimal covers, got {len(all_minimal_covers)}"
    assert all(len(c) == 4 for c in all_minimal_covers), "a minimal cover has size other than four"
    assert set(c_facets) == all_minimal_covers, "4-subset enumeration and full transversal recursion disagree"
    assert len(c_facets) == 130

    order = deterministic_shelling(c_facets)
    certificate = [
        [[i, j] for i, j in sorted(c_facets[index])]
        for index in order
    ]
    if CERTIFICATE.exists():
        stored = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        assert stored == certificate, "stored shelling order differs from deterministic reconstruction"
    else:
        CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
        CERTIFICATE.write_text(json.dumps(certificate, separators=(",", ":")) + "\n", encoding="utf-8")

    verify_shelling_order(c_facets, order)
    print("vertices=30")
    print("generators=14")
    print("4-subsets_examined=27405")
    print("minimal_hitting_sets=130")
    print("minimal_hitting_set_sizes=[4]")
    print("4-subset_enumeration_matches_full_transversal_recursion=PASS")
    print("facet_size=26")
    print("shelling_order_length=130")
    print("direct_facet_shelling_check=PASS")
    print("certificate=" + str(CERTIFICATE.relative_to(ROOT)))


if __name__ == "__main__":
    main()
