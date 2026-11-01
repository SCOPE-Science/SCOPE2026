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
# Reproducibility

Run `python verification/check.py` with a standard Python 3 installation. No third-party packages or network access are required. It checks phase-Hessian determinants exactly for six finite amplitude vectors and computes deterministic midpoint estimates for \(M_{\varphi,1}(w_\epsilon)=J_\epsilon(0)-\log(A-\epsilon)\) for two and three unit-amplitude prime frequencies. The angular Jessen integral is exact as a mathematical expression; the quadrature is numerical.

The normalization \(\pi/T\), ordering of limits, multiplicities and fixed-parameter hypotheses are specified in RESULT.md. The proof relies on the analytic small-cap expansion, Jessen derivative identity and beta integration, not on quadrature or sampled zeros. Finite tests cannot exclude errors in the infinite-height theorem and do not supply independent validation.
