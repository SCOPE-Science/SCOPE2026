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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and its standard library. The checker enumerates every word over the relevant alphabet in each of four finite length ranges, independently builds distinct subsequences by iterative set expansion, tests the Lyndon rotation predicate, and weights source words by exact rational probabilities. It independently computes coefficients of the Möbius–geometric generating function using exact rational polynomial multiplication; all comparisons are exact.

Test cases: binary uniform through length 11 (4,095 source words), binary with probabilities (1/3,2/3) through length 10 (2,047), ternary uniform through length 8 (9,841), ternary (1/2,1/3,1/6) through length 8 (9,841): total 25,824 words. The checker additionally confirms published uniform finite-n values against nine asymptotic predictions (three alphabet sizes, three lengths) and evaluates three independent majorization examples. The success marker is `VERIFY_OK exhaustive_source_words=25824 bias_vectors=4 length_ranges=11,10,8,8 uniform_asymptotic_cases=9 strict_majorization_examples=3`.

Finite tests do not establish the full analytic singularity argument, monotonicity for all probability vectors, or originality. Those are separately proved/assessed in the result and scientific review. No independent audit or certification has been performed.
