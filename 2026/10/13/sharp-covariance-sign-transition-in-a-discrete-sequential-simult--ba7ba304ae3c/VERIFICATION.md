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

# Verification record

The exact geometric joint law is derived analytically in `RESULT.md`. The finite checker `checker.py` is standalone and was run as `python3 checker.py` using Python standard-library arithmetic. It returned PASS for six combinations of sequential-shock, simultaneous-shock, and orientation probabilities; checked normalized truncated joint mass; and compared direct finite joint-PMF covariance summation against the infinite-support closed-form covariance. The same checker tested the sharp critical tied-failure probability under three orientation settings, near-critical positive and negative signs, and a positive-only parameter regime. In all cases its tolerance conditions passed.

Independent checks include direct probabilities for both tied and separated failures, independent summation of first and second moments, and evaluation of the exact transition roots. The example \(r=0.9\), \(\theta=1/2\) yielded critical tied-failure mass \(0.5755710991019481\) and common-shock probability \(0.5496502702061786\). Numerical sums are truncated and cannot prove claims over the entire parameter space; that role belongs to the geometric-series factorization and strictly monotone quadratic in the proof. No external audit, formal verification, or third-party replication is claimed.
