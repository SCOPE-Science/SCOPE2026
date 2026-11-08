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

## Reproduction

Execute `python verify_tail.py` with Python 3, NumPy and SciPy. The test source is included in full, as an ordinary numerical consistency checker rather than a certificate of an infinite-domain theorem. The recorded execution returned `PASS: 387 deterministic checks; exact stationary g=1,r=2 variances (X,Q)=(4/5,8/5), mgf cutoff 2.`

The mathematical proof in RESULT.md establishes all parameter quantifiers, the exact moment domain, divergence at the endpoints and the two-sided logarithmic tail limits. The tests independently compare the stated semigroup to a matrix exponential, the Gaussian innovation variances to covariance integrals, stationary moments to linear generator equations and embedded recursions, and finite-\(x\) Gaussian saddlepoint costs to the claimed limit. Finite checks cannot establish infinite tails, publication priority or independent validation.
