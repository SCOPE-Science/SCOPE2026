---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The arithmetic was independently reconstructed from the two Hirzebruch--Jung strings. Their determinants and tail determinants are \((73,66)\) and \((87,70)\), giving quotient types \(1/73(1,66)\) and \(1/87(1,70)\) and local canonical indices 73 and 87. Their least common multiple is 6351, so with \(K_X^2=1/6351\) the index-volume product is one. Solving the discrepancy linear systems gives exactly the vectors printed in RESULT.md. Substitution into Blache's correction formula using exact rational arithmetic yields integer plurigenera: zero for degrees 2 through 10, one at 11, no value above one through 97, and two at 98, with the listed degree-one-section set. The inspected verifier recomputes every rational step and every claimed degree; the finite computation is exhaustive for the explicitly bounded threshold claim.

## originality

PASS

Originality passes. Liu--Liu prove uniqueness of the rank-one stable surface at the minimal volume and use plurigenus inequalities/filters, while Alexeev--Liu provide the underlying surface construction and cyclic quotient data. The inspected current full Liu--Liu text does not state the global canonical index 6351, the equality between index times volume and one, or the first section thresholds 11 and 98; targeted text searches likewise did not locate those values as pluricanonical thresholds. Fresh Resultary search returned the audited theorem as the exact hit and no prior source with the same threshold computation.

## value

PASS

The surface is the unique rank-one stable surface at the sharp minimal volume, so its canonical Cartier index and first nonzero/positive-dimensional pluricanonical systems are natural intrinsic invariants. The calculation converts the classification basket into concrete canonical-section thresholds that are useful for understanding the canonical ring of the extremal surface, without claiming uncomputed base-point or birational thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
