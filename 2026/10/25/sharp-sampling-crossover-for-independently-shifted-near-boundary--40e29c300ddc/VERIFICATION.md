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

# Verification of numerical identities and limits

The exact analytic proof is provided in `RESULT.md`. Execute `python3 VERIFIER.py` from the same directory using Python 3 standard libraries only. The script has been executed with 475 passing checks and tests multiple-node Fourier aliasing, numerical integration of first and second moments, Poisson-kernel quantiles, critical Laplace transforms, variance asymptotics, and seeded averages. In the proof, dominated convergence and a triangular-array Lindeberg estimate establish the infinite-sample statements; no finite numerical test replaces those arguments.

The first qualifying public source is arXiv:2212.11476v1, dated 2022-12-22. Numerical studies and limit demonstrations assume independent random shifts for each complete grid evaluation, not reuse of a common shift. Source priority remains subject to independent checking, and no independent audit has been performed.
