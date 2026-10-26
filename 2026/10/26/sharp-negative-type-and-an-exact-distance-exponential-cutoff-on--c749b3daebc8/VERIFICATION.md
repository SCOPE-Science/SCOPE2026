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

Run `python3 verify_odd4.py` using Python 3 and no third-party packages. The replay returned `VERIFY_OK` and checked the \(35\)-vertex shortest-path metric, exact sector projectors, the Johnson-scheme coefficient rows, their ranks and multiplicities, the powered distance at exponent one, and the ordinary distance-exponential polynomial identities. The reported nonconstant sector dimensions are \(6,14,14\); ordinary-distance eigenvalues are \(-2,-7,2\); the endpoint Euclidean squared-distance dimension is \(20\), and the positive-cutoff distance-exponential rank is \(21\).

The general real-exponent classification is supported by the analytic sign and uniqueness argument in `RESULT.md`. Rational test points do not prove universal analytic inequalities, and the root decimal is a numerical display of the uniquely defined exact root. The source comparison used full text for the relevant sections of Sánchez (arXiv:1108.0451) and Aalipour et al. (arXiv:1509.01196), plus the relevant HTML section of Tanaka (arXiv:2208.11002); the novelty claim is bounded by that inspection and the specified searches. Independent external validation is not claimed.
