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

The analytical statements were checked against the exact monomial matrix, the standard gamma-ratio asymptotics, an \(L^1\) beta integral, the finite-variation Riemann-sum estimate, and the high- and low-index tail estimates in `RESULT.md`. The same proof controls the signed compact critical windows; the supercritical full-operator comparison is restricted to \(\varepsilon>0\).

Run `python3 verification_checker.py` in a standard Python 3 environment. The checker is self-contained and tests exact finite Bergman moment identities, gamma-beta normalization, matrix coefficients and three selected critical-window finite-section series. It does not establish asymptotic convergence or originality.

Independent mathematical and historical review have not been performed; the provenance of the borrowed matrix identity and the limitations on strong priority are explicitly described in `RESULT.md` and `REVIEW.md`.
