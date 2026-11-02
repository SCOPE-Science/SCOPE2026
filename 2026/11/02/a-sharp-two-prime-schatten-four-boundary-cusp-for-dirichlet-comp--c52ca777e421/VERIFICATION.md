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

# Reproducibility and verification

Run `python check_schatten4.py` with the package's SciPy dependency. The program compares exact Bessel coefficient sums with direct truncated-series expansions, integrates a second representation of the diagonal profile, and verifies the equal-amplitude constant. This is a finite supplementary check and **not** a proof of the infinite-index and boundary limits.

The analytic verification chain is: the monomial Gram identity, the Schatten-four double trace, a differentiable sum-to-integral correction based on harmonic-number asymptotics, Gaussian diagonal concentration, and three Abelian regimes. The steps and quantifiers are given in `RESULT.md`. No computer-assisted exhaustive infinite certificate or independent audit is claimed.
