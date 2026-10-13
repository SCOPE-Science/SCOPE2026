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

# Reproducibility checks and limitations

The analytic check substitutes \(\theta=p\lambda\) into the two published mass functions and probability generating functions, obtaining literal equality for each integer count and every allowed parameter. The rational generating function has a unique double pole at \(1+\lambda\), with coefficient \(\lambda^2/(\alpha+1)\), proving uniqueness of the two effective parameters. A derivative along the constant-ratio curve yields a zero score direction and a singular three-parameter marginal information matrix.

The self-contained `check_epql.py` checker uses exact rational arithmetic with Python 3's standard library. It was run against the packaged source. It passed 284 exact PMF/PGF/rescaling equalities, and verified the example's \(5/9\) zero probability and normalized generating function at one.

A separate exact symbolic manipulation of the printed equations returned PMF ratio one, PGF difference zero, and zero directional log-likelihood derivative. Exact numerical tests only examine finitely many inputs; the universal conclusions come from the proof in `RESULT.md`, not the tests. The result concerns only the unrestricted marginal family, not independent observations of thinning inputs, known external exposures, or jointly observed bivariate counts.
