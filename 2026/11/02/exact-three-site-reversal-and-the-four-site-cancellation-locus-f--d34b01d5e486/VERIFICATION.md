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

# Verification

Run `python verify.py` with Python 3 and `sympy>=1.13`.

The verifier passed **378 exact symbolic/rational assertions**, of which **120** are independent full-configuration Markov stationary solves for randomly selected rational departure rates and rational fields across the three principal particle sectors. It explicitly verifies the three-site and four-site directed matrix-tree numerator/denominator identities, the strict algebraic symmetry classifier, the second-order coefficient, and two exact four-site witnesses. Random sampling checks normalization and nonnegative invariant weights as a diagnostic; universal positivity follows from irreducibility and the finite directed tree theorem.

All claims of exact rational identities are derived analytically by determinant expansion in `RESULT.md`; the symbolic executable independently reproduces those identities. The independently constructed full occupation-state generators cross-check signs and jump normalization. The script does not enumerate all positive real parameters and cannot establish universal facts by finite tests.

The proof does not establish uniqueness of any thermodynamic-limit response, a classification at two particles on four sites, or a priority/certification result. The scientific report has only a self-review; independent audit was not performed.
