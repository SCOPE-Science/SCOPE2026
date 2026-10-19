---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The source `artifacts/verify.py` uses only Python 3 standard library operations and can be run as `python3 artifacts/verify.py`. The exact expected output is in `artifacts/verify_output.txt`; the program terminates with `VERIFY_OK` after all assertions.

Actual checks: order of the field element, two minimal polynomials and the binary BCH generator; dimension-18 dual basis; full \(262144\)-element dual Gray-code census; Krawtchouk/MacWilliams coefficients through weight six; all triple-syndrome collisions and \(876\) distinct weight-six supports; divisibility by the BCH generator for all of them; orbits under \(657\) affine coordinate transformations; two orbit representative Euclidean gcds and ranks of all their cyclic shifts; gcd recheck on every weight-six support; complete \(2628\)-pair incidence and \(73\)-coordinate replication checks.

The weight-six count can be checked independently by the dual MacWilliams sum and by pairwise-disjoint triple syndrome equalities. The geometric orbit and pair-count claims are verified by both a two-representative proof and an exhaustive reconstructed-population diagnostic. The finite program is not an infinite-family proof.

No independent audit, external certification, or independent validator is asserted.
