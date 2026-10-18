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

# Verification of the copula singular-mass identity

The mathematical proof in `RESULT.md` is analytic: it derives clipping boundaries, conditional jump sizes, and the planar density, and integrates singular graph masses. The standard-library-only companion `verify_copula_decomposition.py` provides supplementary reproducibility checks, not a replacement for the proof.

Run `python3 verify_copula_decomposition.py`. The checked script prints `PASS: 20814 supplementary exact-rational and numerical checks` and gives the singular fraction at absolute correlation one half as `0.462098120373297`.

For nine rational values of the absolute parameter and 99 rational conditional locations, checks include exact clipping boundaries, atom positivity, rational jump-weight identities, and numerical matching at clip intersections. Additional numerical quadratures check continuous conditional density plus both atoms sums to one, the nonnegative mixed-derivative bound on the clipped strip, and the integrated graph masses. Numerical tolerances are embedded in the script; the proof supplies all exact universal quantifiers. No Monte Carlo approximation, independent audit, or external certification is claimed.
