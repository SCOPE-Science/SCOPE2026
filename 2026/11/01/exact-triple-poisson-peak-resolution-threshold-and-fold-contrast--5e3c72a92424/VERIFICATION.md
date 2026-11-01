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

To reproduce the computer-backed identities, extract `CHECK.py` and run `python CHECK.py` with Python 3.10 or later; no third-party dependency is required. It verifies the two-variable rational-function derivative numerator identity by exact sparse polynomial arithmetic, the exact collision factorization, and illustrative rational-parameter minimum signs. The observed success message is `CHECK_OK: exact two-variable derivative identity, exact critical factorization, strict-minimum root controls`.

Independent hand-algebra checks also gave \(\partial_sV_s'(1/\sqrt2,1/2)=-2\sqrt2\), \(\partial_x^2V_s'(1/\sqrt2,1/2)=-18\sqrt2\), \(\partial_y^2Q_{1/2}(1/2)=36\), and \(\partial_sQ_{1/2}(1/2)=8\). These are the local coefficients needed for the fold law. The continuum positive-root census, stationary-point classifications, and asymptotic-error bounds rely on the written analytic proof, not the finite checker. Historical originality remains open to independent literature verification. No independent audit is claimed.
