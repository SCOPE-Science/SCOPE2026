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

The analytic proof is in `RESULT.md`. It covers all real parameters \(0<x<y\le1\), \(0<w<1\), \(0<\lambda<1\) and \(p\ge0\), including both onset boundaries and the special algebraic value \(p=1-\lambda\) by continuity.

Running `python verify.py` in the directory containing the scientific documents checks the exact rational curve-number 40/50 benchmark, 2,400 independent evaluations of the fully wet weighted-gap formula, and 2,400 numerical root brackets with 96,000 interior/exterior sign tests. All checks passed in the originating environment. The program is standalone and deterministic, requiring Python 3 standard-library modules only.

Finite verification does not certify the universal result. The argument relies on strict monotonicity of the partial-onset ratio, the one-change sign pattern of the cubic, stage continuity, and the curvature calculation for the lower bound. No experimental watershed observations, uncertainty propagation, or broader-than-two-zone theorem are asserted.
