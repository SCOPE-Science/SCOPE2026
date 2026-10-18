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

Run `python verify.py` using Python 3.9 or later (standard library only). This enumerates complete multinomial occupancy vectors exactly with `fractions.Fraction`, rather than sampling. It cross-checks the pair-collision covariance against the independently evaluated conditional-difference identity for five explicit positive probability vectors, sample sizes 2–9, every convex hinge, every exact-frequency score, and two affine scores. The uniform-frequency quadratic sign and singleton threshold are also checked. The run succeeded with 520 exact-rational checks and 180 strict positive convex-hinge checks.

The analytical argument in `RESULT.md` establishes the claim for arbitrary parameter sizes; finite computational checks cannot establish a universal theorem. No external or independent audit was conducted. The proof does not establish priority relative to all historical occupancy results.
