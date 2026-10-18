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

# Verification of the arctangent volume law

Run `python VERIFY_VOLUME.py` in an environment with SymPy, NumPy, and SciPy. The script independently computes exact rational volumes by iterated integral operators for dimensions 1 through 12, and by enumerated rational vertices plus a convex-hull triangulation for dimensions 1 through 5; it checks twelve Taylor coefficients, eight cotangent-derivative lattice coefficients, and the leading eigenfunction's normalization. The program reports `ALL EXACT SQUARED-PATH LIPSCHITZ VOLUME CHECKS PASSED` after every assertion succeeds.

The finite checks **cannot** establish a formula for arbitrarily large dimensions; that assertion rests on the explicit resolvent ODE, the classical cotangent partial fraction and absolute coefficient extraction in the accompanying proof. The computational facet choice uses numerical triangulation, but its vertices and determinant volumes are evaluated over exact rationals. No independent audit has yet been conducted.
