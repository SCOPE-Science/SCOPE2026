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

The complete proof is given in `RESULT.md`. Executing `python3 verify.py` from the same directory independently checks the finite small-market cases and the four-pair witness with exact rational arithmetic. The exhaustive test traverses all \((n!)^{2n}\) labeled strict preference profiles for \(n=1,2,3\), all \(n!\) candidate perfect matchings, and every potentially blocking pair. It verifies the complete weak-order comparison, not just equality of optimal objective values, and independently checks the two exact witness matchings. For \(n\leq3\) the theorem has a separate structural proof; the check is corroboration, not an inference from sampling.

The validity is confined to complete strict one-to-one markets and positive Borda rank utilities, as stated. No claim of third-party validation is made.
