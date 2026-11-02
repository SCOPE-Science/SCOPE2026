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

# Verification scope

The reproducible independent finite calculation is `verify.py`, which uses Python's standard library and prints `VERIFY_OK: sections/graded generators/leading cancellations/lower bound` after confirming the first ninety graded degrees, the necessary low-degree multiplication injectivity, and both explicit coefficients. The proof for all degrees is the semigroup induction in `RESULT.md`, not a bounded experiment. Analytic existence of the formal function lifts and the associated graded description are supplied by the primary source's theorems and lemmas; no computer script checks an infinite analytic assertion. An external independent audit has not been performed.
