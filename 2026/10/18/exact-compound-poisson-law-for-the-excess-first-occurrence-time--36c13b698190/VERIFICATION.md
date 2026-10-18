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

# Verification
Run `python3 word_wait_checker.py` using Python's standard library. The checker constructs prefix automata, evaluates characteristic-polynomial coefficients from Newton's identities and traces, compares with exact first-hitting probabilities, checks trace nonnegativity, and independently enumerates short words. It reports 498 tested patterns, 7968 coefficient identities, 7470 nonnegative traces and 365 brute comparisons. All are finite checks.

The general assertion follows independently from the four proof steps in `RESULT.md`: an upper-Hessenberg cofactor identity, uniform geometric absorption, the matrix trace logarithm and positivity of every trace term. No claim about arbitrary finite-state phase-type laws, multiple targets or Markov-generated strings is made. Independent audit has not been performed.
