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

The proof of the infinite interval family and damping-density asymptotic is in `RESULT.md`. The reproducibility artifact `verify.py` runs with ordinary Python 3 and the standard library; execute `python3 verify.py` in the same directory. It numerically brackets the turning-point and imaginary-eigenvalue roots, checks the first twelve disjoint intervals and full-dimensional sink inequalities, and checks scaled interval widths at large indices. The computation is *not* an exhaustive enumeration and is not used as an infinite proof. Boundary nonlinear stability, nonsynchronous dynamics and publication priority remain outside this verification.

Self-review: passed. Independent audit: not yet performed.
