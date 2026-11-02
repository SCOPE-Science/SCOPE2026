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

The claim is proved by two complementary arguments. A three-color local-column rigidity argument forces period three but contradicts the row-swap boundary. A four-color column construction works for every length. The complete number of named optimal colorings is a trace of a precisely defined 84-state integer matrix under an involution; its two 42-state characteristic polynomials give the exact rational generating function.

Reproduce the integer certificate with `python3 verify.py` from this package directory. This constructs all 84 states, all 384 directed transitions, the 42 row-swap orbit representatives, and both 42-by-42 blocks directly from the local PCF rules. The standard-library Faddeev–LeVerrier computation checks **all** coefficients of both claimed characteristic polynomials, not just their first few traces. The same script independently checks direct graph-edge assignments for lengths 3 and 4; both types of closure for the explicit four-color construction through length 300; and the twisted/untwisted trace correction through length 30. A successful run ends with `VERIFY_OK`.

The finite-width tests are corroboration, not proof for all lengths. The exact characteristic-polynomial calculation, trace identities, and the separate periodic construction provide the infinite argument. No independent external audit is claimed. The full text of the 2026 broad subcubic choosability source was not obtainable for a line-by-line novelty comparison; its theorem statement is recorded as a broader upper-bound result, not claimed as new here.
