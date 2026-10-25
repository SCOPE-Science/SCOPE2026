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

The proof in `RESULT.md` is uniform for all integers \(k\ge1\). The only external mathematical identity used is the standard correspondence characterization \(2d_{\mathrm{GH}}=\inf_R\operatorname{dis}R\), stated explicitly in the cited primary papers.

From the directory holding the embedded files, run `python check_round_polygon.py` using Python 3 and its standard library. It checks the exact \(k\)-step correspondence distortion for each integer \(1\le k\le100\), and exhaustively enumerates all subsets with \(k+1\) elements when \(1\le k\le4\) to test the circular packing lemma. The script was executed successfully before packaging and its output reproduced the expected success messages.

The enumerations are finite sanity checks. They do not establish the theorem for all \(k\); the complete proof is the analytic packing lemma plus the interval-by-interval correspondence distortion calculation. No independent external audit or software proof assistant verification was performed.
