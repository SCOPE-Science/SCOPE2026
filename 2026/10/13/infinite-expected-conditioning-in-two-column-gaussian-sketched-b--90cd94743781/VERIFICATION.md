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

# Verification and reproducibility

Run `python verify.py` with Python 3 (standard library only). The checker reports `VERIFY_OK: 986 exact Schur-complement and triangular-Gram tests; 25 density quadratures; 48 near-breakdown witnesses` on the provided script. It exercises exact rational identities for the algorithm's two unnormalized sketched residual columns, confirms the determinant-based condition-number lower bound, checks the Gaussian gamma-convolution coefficient against an independently integrated density, and constructs rational near-breakdown sequences.

The algebraic proof establishes all parameter quantifiers: every integer sketch size \(s\ge2\), every \(n\ge3\), every nonparallel unit input pair for the first-pivot moment threshold, and every moment order \(r\ge1\) for the fixed two-column conditioning counterexample. Integrability of inverse powers follows from local density asymptotics. The \(1/t\) probability lower tail rests on positivity of a smooth multivariate Gaussian density and a local transversal coordinate, not numerical sampling. The random sketch is unconditioned and exact arithmetic is assumed; no finite experiment is treated as an infinite proof or an independent audit.
