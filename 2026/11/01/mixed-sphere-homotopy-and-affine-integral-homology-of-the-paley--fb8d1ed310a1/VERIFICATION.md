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

# Reproducibility and limits

Run `python3 VERIFY.py` using Python 3 standard-library modules only. All displayed figures are calculated from an explicit thirteen-vertex quadratic-residue adjacency rule, without external data files. Compare the standard output to `VERIFY_OUTPUT.txt`; the final marker is `ALL_CHECKS_PASS`.

The checks include all vertex subsets (two distinct face predicates), maximal-face purity, a complete acyclic matching and all its Hasse incidences, oriented integral unit cancellations, the exact Morse boundary and a determinant-one-in-absolute-value minor, unreduced field boundary ranks over four primes, and all 78 signed group traces. Finite-field ranks corroborate the integral computation but do not establish the absence of torsion on their own; the integral unit-pivot and unit-minor argument is essential. The full homotopy equivalence and identification of the rank-two integer lattice with the Euclidean Eisenstein ring follow from mathematical theorems specified in the proof. Independent mathematical review has not been performed.
