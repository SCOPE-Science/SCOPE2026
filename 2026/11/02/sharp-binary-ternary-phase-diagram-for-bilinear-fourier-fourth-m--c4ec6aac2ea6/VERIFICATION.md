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

The master fourth-moment identity was cross-checked by direct additive-character convolution in the standalone `checks/check_segre.py` script, without using the row-correlation formula for the direct calculation. The script also exhaustively enumerates labelled, normalized binary configurations for widths \(3\) through \(7\), and ternary configurations for widths \(3\) through \(5\), using exact integer arithmetic for all squared root-of-unity sums. Constructed equality arrays were checked for widths \(3\) through \(120\) in both alphabets. All 273 assertions passed under Python 3.

These finite calculations cannot prove the results for arbitrary width. That conclusion follows from the fully stated Walsh and root-of-unity count arguments. No independent mathematical audit, human certification, or formal proof-assistant verification has been performed. The count of normalized ternary optimizers is only claimed in the stated divisible-by-three case.
