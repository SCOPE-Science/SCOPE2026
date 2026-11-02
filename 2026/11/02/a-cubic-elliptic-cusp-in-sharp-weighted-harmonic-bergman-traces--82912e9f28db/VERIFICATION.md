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

The proof uses exact normalized weighted Bergman monomial norms, a spectral gap for the first circular harmonic, operator-norm analytic perturbation of a compact trace form, and Fourier selection rules up to cubic order. These are infinite-dimensional arguments; finite checks are supplemental.

Reproduce the algebra by running `python3 checker.py` in the directory containing this document. The script is self-contained and requires only Python's standard library. It verifies 70 exact rational identities, including the critical quadratic coefficient for nine rational positive values of \(\beta=\alpha+1\), plus the cubic \(9/16\) coefficient at \(\alpha=2\). The tests do not exhaust all real weights or certify operator-norm perturbation theory.

Limitations: the expansions hold for fixed \(\alpha>-1\) and radii in the stated open interval with sufficiently small real eccentricity. The full finite-eccentricity optimum, other spectral regimes, and independent validation are not established.
