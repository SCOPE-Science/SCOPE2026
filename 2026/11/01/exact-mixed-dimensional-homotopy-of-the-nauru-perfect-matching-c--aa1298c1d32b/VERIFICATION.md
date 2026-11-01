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

# Finite verification

Run `python3 verify.py` in the directory containing `certificate.json`. The complete certificate contains 36 indexed graph edges, all 120 perfect-matching masks, all 108 unmatched-face masks, the complete signed matrices in degrees four and five, and exact determinant-one minor positions. The checker regenerates these inputs from the GP(12,5) definition before comparing every value.

The 346,822 face poset elements are exhaustively generated, with 173,357 paired incidences and 2,282,760 Hasse incidences inspected. The directed graph is topologically sorted to verify acyclicity. Exact rational elimination finds ranks 16 and 19; exact fraction-free determinant calculation establishes unit minors and all coefficients of the zero boundary composite are checked. No sampled calculation is substituted for an exhaustive assertion. A second matching, made by toggling in reverse edge order, yields mod-two ranks 5 and 18 and the same homology ranks.

`CHECK_LOG.txt` records one successful actual execution. The data and algorithm, not just this log, are the finite evidence. No independent external validation is claimed; all-parameter generalized Petersen statements are unproved and not asserted.
