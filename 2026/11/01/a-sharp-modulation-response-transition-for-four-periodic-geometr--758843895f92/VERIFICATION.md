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

# Reproducible verification

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The included code symbolically reconstructs the differentiation identity for the geometric-vector test profile, the degree-eight half-line coefficient transform, three sign-chain certificates, the neutral-curve identity, and the strict derivative formulas. It also evaluates 90 directional numerical cases across six geometric damping parameters and tests the predicted critical-curve limits.

The universal mathematical conclusions follow from the analytic sign certificate, Descartes' rule, implicit differentiation, and the exact degenerate-root boundary expansion in `RESULT.md`. The finite computations do **not** substitute for those analytic steps or establish publication priority. They do not verify the exact numerical radius of the underlying operator, which is expressly outside the theorem.

The new contribution is the sensitivity phase diagram and its critical scaling, not optimizer existence or uniqueness. All reported testing uses the standalone source included with this package.
