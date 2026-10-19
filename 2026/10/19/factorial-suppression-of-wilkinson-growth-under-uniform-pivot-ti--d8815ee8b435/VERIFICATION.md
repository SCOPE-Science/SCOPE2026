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

The accompanying `check.py` uses only standard-library exact rational arithmetic. It enumerates every legal maximum-absolute-value pivot choice for dimensions 2 through 9, retaining separately each Schur matrix and current maximum entry magnitude. The exact dynamic-programming masses sum to one at each step; the computed point probabilities, survival probabilities, and means agree with the analytical identities. The program printed `EXACT_CHECKS_OK 576` in the completed execution. Run `python3 check.py` from the extracted files.

The universal statements are proved via the leading-minor classification and Schur-complement formulas in `RESULT.md`. Enumeration to dimension 9 is a finite check, not a proof of a universal assertion. No independent audit or external mathematical validation has been performed.
