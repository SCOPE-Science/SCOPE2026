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

# Exact-arithmetic verification and scientific limits

Run `python3 verify.py` with Python 3.10 or newer; no external libraries are required. The verifier calculates \(T(h)S_hT(h)^\top=S_h\), the covariance map on rank-one states, the perturbation matrix coefficient \(2h^2/(4-h^2)\), and, for two equiprobable rational steps, the characteristic polynomial \(64r^3-66r^2+49r-49\). It also enumerates every sample path at horizons \(0\) through \(8\) for two independent rational initial-state choices and compares the exact expected covariance with the iterated three-coordinate moment recurrence. Its executed output reports 107 passed exact-rational checks.

These checks confirm nontrivial algebra and finite-path consistency. They do not by themselves certify infinitely many iterations, the existence of positive-definite primal/dual eigenmatrices, strictness of determinant-root concavity, or novelty. Those mathematical steps are proved in `RESULT.md`; the decisive strict eigenvalue step uses the impossibility of a common positive invariant quadratic form for distinct step values. No independent audit has been performed.
