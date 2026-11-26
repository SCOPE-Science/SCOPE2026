---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The connected incidence graph has a unique bipartition up to swap. A side-preserving point permutation preserves the third point on every line, hence XOR after extending it by zero; the induced automorphisms are GL(3,2) of order 168. Orthogonal complementation for the nondegenerate F_2 pairing supplies the side-swapping polarity and hence 336 maps in total. A proper restricted-growth word encodes each unlabeled partition once; its distinguishing criterion tests pointwise fixation of the classes, not the residual class permutations allowed in an orbit stabilizer. Fresh bounded adjacency-backtracking replay at /workspace/branches/e46d8460-f74c-4b6c-b62c-6d574a6821d2/heawood_check.py, with independent_check.json in that directory, found 336 graph automorphisms, 1/350/29610 proper partitions into 2/3/4 classes, none distinguishing below four, and 13,692 distinguishing four-class partitions. Each gives 24 color namings, hence 328,608 fixed-palette colorings. The orbit census is 51 with sizes 56,84,112 and 168 (16),336 (32). All 51 frozen orbit rows matched, including canonical representatives, profiles, counts and class-permutation stabilizer data. Stabilizers act faithfully on the four classes because the kernel would preserve each named class; the exceptional orders 6,4,3 follow from 336 divided by orbit size. These are exact finite graph claims, not a formula for general incidence graphs.

## originality

PASS

The supported distinct contribution is the exact census of the optimal proper distinguishing color partitions of the Heawood graph and their orbits. The existence of a proper distinguishing four-coloring and the graph-coloring framework are already established and not treated as new.

## value

PASS

The Heawood graph is the natural highly symmetric Fano incidence graph, and the least proper palette is a canonical threshold. A complete classification of its optimal symmetry-breaking colorings records nonuniform stabilizers invisible to existence, and the reproducible representative set gives precise examples for further use. The orbit distribution is not an arbitrary parameter slice or a check of a known chromatic-polynomial value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
