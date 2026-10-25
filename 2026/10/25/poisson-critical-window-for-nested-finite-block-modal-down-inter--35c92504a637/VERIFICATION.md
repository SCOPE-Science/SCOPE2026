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
# Reproduction and scientific limits

Run `python3 checker.py` with Python 3 standard-library modules only. The checker independently generates all equal-block partitions in the listed small sizes, counts outputs from fixed-cardinality inputs, compares each count with the rational factorial-moment inversion law, and independently propagates every initial subset through each listed number of fresh independent partition steps. Each output is computed using exact `fractions.Fraction` arithmetic. Successful output ends in `ALL_CHECKS_OK`.

The proof of the growing-size limit is analytic: the conditional negative-covariance bound, the concentration induction, and the factorial-moment convergence are recorded in `RESULT.md`. No finite test establishes the asymptotic result. The conclusions do not extend to general random partitions, independent interpretations without equal block sizes, or satisfaction probabilities, and there has been no independent audit.
