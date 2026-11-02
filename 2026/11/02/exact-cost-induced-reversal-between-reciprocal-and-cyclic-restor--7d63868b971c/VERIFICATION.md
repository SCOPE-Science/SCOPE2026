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
# Reproducible checks

Run `python3 verify_corridor.py` with Python >= 3.9. It relies only on the standard library.

The supplied program compares the characteristic cubic with independently expanded exact \(3\times3\) determinants for rational parameters and verifies the fixed-budget anchor algebra. It bisects the positive cubic root for finite rational parameter grids and checks the strict directional order and endpoint spectral formulas, including exact critical-budget instances and exact rational examples. The recorded pass counts from the source file execution were 13,440 determinant checks, 2,688 anchor checks, 384 sampled monotonicity/endpoint cases, 845 critical/target-budget checks, and the illustrative rational equalities.

The proof of the universal statement uses the single-positive-root sign change and the exact shared anchor. Finite grid checks supplement that proof but cannot establish all-parameter universal quantification. The public documents have not undergone independent audit, and none is claimed.
