---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The ordinary matching complex of the 3-by-10 vertex grid has 47 graph edges. Source verify_grid10.cpp exhaustively branches on each edge, removing incidences, and its greedy early-edge toggle has the usual acyclic alternating-path argument. Two complete, independent stored GF(2) critical-cell boundary matrices were read as actual source blobs, parsed and independently row-reduced with exact BigInt bitset elimination: ascending 122x393 rank120; descending 30x301 rank28; no malformed rows. Thus reduced H10 has dimension 2 and H9 dimension 273 in both matchings, with no other critical degrees. Independently, an edge-state matching DP counted 47,177,097 augmented faces and Euler sum 271, consistent with -273+2=-271. The finite certificate supports exactly P3-square-P10 mod-two homology; it proves neither integral freeness nor any larger width.

## originality

PASS

Best-of-knowledge first exact nonzero H10 result at n=10, an object directly adjacent to earlier computed widths 1 through 9 and a counterexample to the proposed all-width single-sphere-dimension pattern. Indexed matching complexes on other finite graphs do not imply this specific mod-two group.

## value

PASS

A complete exact natural grid-width threshold, n=10 immediately beyond published n<=9 computations, refutes the mathematically motivated all-width one-dimensional sphere-wedge pattern at the first open width. Mixed adjacent homology degrees are a substantive obstruction, not an arbitrary tiny-instance table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
