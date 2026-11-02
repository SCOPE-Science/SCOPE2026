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

Run `python3 check_six_season.py` in the directory containing `orbit_certificate.csv`. The checker uses only the Python standard library and exact rational arithmetic. It independently enumerates all \(720\) permutations, compresses them to \(60\) dihedral classes, verifies every row in the finite certificate, and proves all extremal integer-statistic statements by exhaustion. Direct matrix multiplication is compared against the analytical trace polynomial for every six-season word under four exact-rational parameter sets, including the critical boundary.

The **all-real-parameter** conclusion is supported by the cycle-matching trace identity, the finite exhaustive coefficient bounds, the common-determinant spectral-radius monotonicity, and the explicit sign of \(T_A-T_B\). Tests at finitely many biological parameter sets are supplementary only. The minimal-six assertion follows algebraically from the matching-polynomial degree for shorter cycles, not from numerical sampling. No external or independent scientific audit has been performed.
