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

Run `python verify.py` with Python 3, NumPy, SymPy and SciPy installed. The script checks algebraic identities of the rank-one Green function and extremizer conditions, exact radical expansions, and independent finite-section matrix inversions.

The unbounded-lattice theorem does **not** follow merely from these computations. The universal sharp constant, attainment classification and global uniqueness rely on the resolvent Cauchy--Schwarz equality, the quadratic derivative sign argument, and the escape-to-infinity construction established in RESULT.md. Finite sections approximate the infinite Green kernel but do not certify an infinite maximum on their own.

Independent audit: not yet performed.
