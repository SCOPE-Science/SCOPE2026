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
# Reproduction and scope of checks

The finite-dimensional rank and real-analytic arguments are proved in `RESULT.md` and require no external computation. The accompanying `verify_finite_difference.py` may be run using Python 3 and SymPy from its own directory; a successful run prints `FINITE_DIFFERENCE_RELATION_EXACT_TESTS_OK`.

The script checks the bidegree identities exactly for all \(1\le k\le6\) and \(1\le j\le k\), and checks strict positive finite differences at selected larger even exponents. Non-even numerical cases are diagnostic only. The theorem for all \(k\ge1\) and all real \(1<p<\infty\) follows from the analytic proof, not finite enumeration.

The reviewed result treats the defining numerical-range dichotomy as prior input, limits novelty to the coefficient and dimension classification plus the exponent-phase family, and explicitly retains access risks for two older sources. Independent audit has not been performed.
