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

# Checks and reproducibility

The standalone `verify_niven.py` uses only the Python standard library. Running `python verify_niven.py` independently constructs all small-base digit pairs, tests direct digit-sum divisibility, evaluates the exact multiplicative-order count formula, and checks the decimal grouped expression, rational constants, and 48-period minimality.

The infinite proof relies on two exact number-theoretic reductions and a closed finite arithmetic sum. Exhaustive finite regression is not offered as an infinite certificate. The 48-residue check proves *minimality* only because the proof separately bounds the remainder's period by 48. General originality and independent external validation are not certified.
