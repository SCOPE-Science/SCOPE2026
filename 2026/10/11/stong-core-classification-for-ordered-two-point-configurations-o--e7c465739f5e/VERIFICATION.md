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

The theorem is verified primarily by an all-parameter proof from strict upper and lower sets. For a mixed point \((a_i,b_j)\), the strict lower set has exactly \(p-1\) incomparable points and the strict upper set has exactly \(q-1\) incomparable points. The dual mixed type has the same cardinalities. Same-level points have explicit incomparable witnesses, so no hidden beat cases remain.

`artifacts/verify.py` is a finite independent replay of the definitions, not a substitute for the proof. It reconstructs the product-order configuration space for all \(49\) pairs \(2\le p,q\le8\), enumerates beat points directly, executes the claimed deletion sequences, identifies the final complete height-two remainder, and verifies that the remainder is beat-point-free. The recorded output is:

`VERIFY_OK cases=49 range=2..8 theorem=beat_classification_and_core_formula
samples=2x2:12->4;2x5:42->22;3x3:30->30;3x6:72->72;5x2:42->22;6x6:132->132`

Limits: the script checks only the displayed finite parameter box. The proof establishes all \(p,q\ge2\). No independent audit has been performed.
