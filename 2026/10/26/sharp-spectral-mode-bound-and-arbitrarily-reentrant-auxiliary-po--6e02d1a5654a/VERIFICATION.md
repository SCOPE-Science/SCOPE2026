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

Execute `python verify.py` using Python 3.10 or newer; the checker uses only the standard library and exact fractions. It verifies coefficient interpolation and rational identities for dimension one through seven, all 79 sampled rational stepsizes, sign alternation, and an independent direct solution of the original two-coordinate backward-Euler equations.

The two-dimensional example evaluates to \(r^+(1/2)=16/545>0\), \(r^+(3/2)=-16/8303<0\), and \(r^+(3)=8/1715>0\). Its nonlinear energy has global minimum \(31/320\).

These computational checks do not exhaust all dimensions or stepsizes; the full theorem follows from the pole-residue argument, degree bound, and positive quadratic realization given in `RESULT.md`.
