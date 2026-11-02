---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For a cell of an m-by-n colouring array, the edge-neighbour count is m+n-2. In any two-colouring equal-half forces R_i+C_j=2x_ij; differences make every row/column sum constant for m,n>=3, yielding contradiction. For m=2 parity gives exact 2/3 dichotomy. Colour i+j modulo3 satisfies the ceiling criterion except exactly (3,4),(4,4),(4,5),(4,7) for small m+n; explicit valid 4x4 and 4x7 matrices cover two, and modulo4 covers 3x4/4x5. The actual 1704-byte C++17 exception checker enumerates canonical colour/column-permuted first rows, lexicographically nondecreasing remaining rows, all 3-colour row words, with sound monotone count pruning; compiled and executed successfully for both finite obstructions, reporting no full assignment and 931 / 59228 partial extensions. This exhausts symmetry classes; no timeout or random test is used for nonexistence.

## originality

PASS

Best-of-knowledge PASS for the full sharp K_mn classification, NOT the known K3,4 obstruction or the known minimum-degree>=5 upper bound. No inspected source implies the K4,5 exception or entire phase diagram.

## value

PASS

A complete exact phase diagram for a recently introduced natural edge-colouring invariant; the new low-degree K4,5 obstruction is nontrivial, unlike the already-covered min-degree>=5 upper bound. The thin K2,n parity transition, constructive 3-colour families and provably unique exceptional pairs give an independently useful classification, and the K4,5 case is relevant to the published low-degree boundary discussion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
