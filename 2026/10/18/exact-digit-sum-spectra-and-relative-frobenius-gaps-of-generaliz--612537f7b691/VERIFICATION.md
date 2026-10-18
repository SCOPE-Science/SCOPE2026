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

# Mathematical verification

The universal proof is the three-stage argument in `RESULT.md`: reduction by cyclic carries, explicit inverse-carry construction, and a residue-class Frobenius computation. Each stage is valid over arbitrary integer bases and lengths in the stated domain.

`python3 verify.py` requires the standard Python 3 library only. A completed execution returned 34 selected modulus/base settings, 1518 exact residue-DP weight comparisons, and 1260 independently checked witness numbers, with no failed assertion. Exact reachability is computed by iterating finite sets of residues modulo the repunit, not by scanning a bounded multiplier; for each examined weight it therefore decides the finite-weight question exactly. Witnesses are checked with integer modular division and an independently computed positional digit sum.

The verifier checks only finite settings. Neither an infinite-domain mathematical audit nor independent validation has been performed. No statements beyond the exact spectrum and its relative gap consequences are claimed.
