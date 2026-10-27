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

# Verification record

The result is proved by reducing the exact capped update to two affine branches and analyzing their switch, contraction factor, invariant reflection interval, and exact period-two orbit. The proof and branch inequalities are in `RESULT.md`; all quantifiers and boundary cases are restricted there.

The included `verify.py` uses only exact standard-library rational arithmetic to test the source-rule formula, the cycle equations, the critical reflection, and stability multipliers for selected examples. Running `python verify.py` produced `VERIFY_OK; exact fractions, both cycle orientations, critical band and stable/unstable examples`. Finite rational checks do not establish generality. No independent audit has been performed.
