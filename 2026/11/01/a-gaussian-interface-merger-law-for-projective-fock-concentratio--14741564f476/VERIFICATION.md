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

The normalizations in RESULT.md are fixed by the probability Gaussian measure and the normalized monomial basis. The exact spectrum uses a beta density with shapes \(k+1\) and \(n-k+1\), which has total shape \(n+2\) and binomial count parameter \(n+1\). This one-unit offset is essential. The independent interval-copy identity was checked by exact rational enumeration for small degrees, not inferred from asymptotic numerical agreement.

Run `python3 checks.py`. The implementation uses the Python standard library, including exact fractions for finite checks and a stable modal recursion for higher-degree binomial probabilities. It verifies the exact trace, the beta–binomial identity, the interval symmetry-difference expectation, and a selection of finite-width and large-width numerical limits; those checks cannot substitute for the proof of convergence in RESULT.md.

The analytic proof verifies both the finite-\(c\) normal interval limit and the separate infinite-\(c\) regime. It treats arbitrarily chosen sequences of endpoints satisfying the written hypotheses, not only the centered parameterization used in the numerical examples. There is no claim of an explicit finite-degree error rate. No external independent audit or proof certification has been performed.
