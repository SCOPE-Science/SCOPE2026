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
# Verification and limits
The analytic proof in `RESULT.md` verifies all quantifiers and the three expansion coefficients using a uniform Rosser--Schoenfeld bound, the effective prime number theorem and Mertens product, and explicitly chosen primorial counterexamples. The strict inequalities for both types of threshold follow by bracketing with any fixed positive epsilon. No conjectured exact equality is presumed.

The auxiliary `artifacts/check_bracket.py` uses standard-library floating-point arithmetic solely to check the algebraic inversion bracket for a few levels; it is not an exhaustive search and is not the proof. Results are subject to rounding but have margins far exceeding machine precision. Independent audit has not been performed.
