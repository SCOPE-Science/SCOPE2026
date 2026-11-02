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

Run `python3 verify.py` with `AP_PROFILE.csv` beside it. The program derives the fixed point bit vector from the base-four substitution, checks exact existence and impossibility by the one-carry equivalence, verifies every 1025 table row, checks an actual starting position for each maximal progression, and confirms all three unique prefix maxima. The expected terminal line begins `VERIFY_OK`.

The certificate concerns only differences at most 1025. Mathematical correctness of the one-carry lemma remains an ordinary subject for independent scientific review; it is documented in `RESULT.md`. No independent audit has been performed.
