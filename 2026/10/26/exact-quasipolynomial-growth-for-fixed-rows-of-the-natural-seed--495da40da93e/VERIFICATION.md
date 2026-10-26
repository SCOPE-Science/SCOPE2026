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

# Reproducibility
Run `python3 verify.py` using Python 3 with only the standard library. It directly reproduces 1,980 row values across 11 generations and 180 start positions using integer gcd arithmetic, independently checks selected prime-adic reconstructions and the closed low-row examples, and checks high-spike invariance for 337 synthetic configurations. Successful output is `VERIFY_OK integer_cases 1980 synthetic_high_spike 337 rows 11 exact_examples_m2_m3 360`. These checks do not prove the theorem for unbounded generation or starting position; that follows from the symbolic induction in RESULT.md. The displayed period is an upper bound, not necessarily minimal.
