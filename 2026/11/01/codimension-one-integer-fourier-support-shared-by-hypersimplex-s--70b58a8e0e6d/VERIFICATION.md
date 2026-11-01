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

Run `python check_hypersimplex.py` with Python 3, NumPy and SciPy available. The accompanying checker re-evaluates the binomial identity for \(3\le n\le23\), counts collision sets in several finite boxes independently, performs direct numerical integration for \(n=3,4\) without residues, and checks the first nontrivial hypersimplex instances \(n=5\), \(s=2,3\) by deterministic quasi-Monte Carlo integration. The actual run reported `PASS: 552 exact combinatorial checks and 11 direct numerical integrals`.

The infinite result does **not** follow from these checks. The necessary analytic steps are the sliced-cube Laplace transform, simple/double pole partial fractions, a finite alternating-binomial identity, and hyperplane-arrangement counting, all given in `RESULT.md`. No assertion is made for Fourier support at frequencies with two or more collisions or for arbitrary real frequencies. No independent external audit has been performed.
