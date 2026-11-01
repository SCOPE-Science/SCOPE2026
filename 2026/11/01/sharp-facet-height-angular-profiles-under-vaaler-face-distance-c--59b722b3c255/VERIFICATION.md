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

# Reproduction and limits

Execute `python3 verify.py` using Python 3's standard library; no network or downloaded data are needed. The script completes 2,082 exact-algebra and numerical checks: positivity and cumulative-sum optimality of the boundary Gaussian coefficients, a rational Abel-summation identity on ordered vectors, the planar closed integral formula, its strict fixed-height comparison, exact high-height gamma coefficients and normalization, the planar threshold kink, admissible trapezoid identity, and the truncated-cube radius sandwich.

The universal inequality is established by the analytic proof in `RESULT.md`, notably the pointwise cumulative-sum domination (10), the source-supported contraction inequality (14), and the facetwise cone-sector summation. The two geometric sharpness constructions are explicit. The checks do not independently validate all quantifiers; no formal proof assistant or external expert assessment was performed.

The source's original face-distance, contraction, and sector identities were inspected in the complete available article at arXiv:2609.27798v1, Sections 2–4. Karasev's related article was inspected at arXiv:2505.16247v3, Sections 1–3. Historical-priority and intermediate-dimensional geometric sharpness limits are stated in `RESULT.md`.
