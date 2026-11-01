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

# Reproducible finite checks and analytic scope

Run `python check.py` with `numpy` and `scipy` versions meeting `requirements.txt`. The checker reconstructs the finite Jacobi matrices from \(b_n=\sqrt{(n+1)/(n+\alpha+2)}\), tests weighted beta-moment ratios by exact rational arithmetic, tests the full boundary-inclusive energy identity, and compares numerical principal eigenpairs with the predicted Airy constants at several fixed weights and degrees. It also checks the distinct Hardy endpoint formula. The packaged checker completed 1922 finite supplementary assertions. The infinite \(N\to\infty\) theorem is justified by the explicit upper/lower form convergence proof in RESULT.md; finite computations alone cannot prove it.

Scientific limits: fixed \(\alpha>-1\); no uniform parameter convergence or certified computer-assisted infinite proof. The asymptotic coefficient, normalization, boundary conditions and exact weight formulas are defined in RESULT.md. Independent mathematical audit has not been performed.
