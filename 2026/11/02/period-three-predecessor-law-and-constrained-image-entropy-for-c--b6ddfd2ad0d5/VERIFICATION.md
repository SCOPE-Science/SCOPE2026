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

# Reproduction and limits

Execute `python3 verify.py` in the directory containing this document. The script uses Python 3 standard library only. It builds direct Rule-22 output/preimage fibers from every binary input and compares the exact two-state matrix predictor on every cyclic-`00`-avoiding output for each length \(1\le n\le17\). The same tests count distinct reachable outputs and exactly-two-predecessor outputs. It separately checks coefficients of the rational generating series through degree 120. A complete replay prints `VERIFY_OK`; finite evidence does not replace the universal graph/determinant proof in `RESULT.md`.

The source material relevant to priority comparisons includes the full-text Rule-22 preimage analysis of Jen (1989), the explicit same growth constant in Voorhees (1997), the exactly-one dynamics work of Gravner and Griffeath (2010), and the Rule-22 subset/regular-language sections of Martínez et al. (2019). The exact cyclic constrained image formula is not claimed to have an independently certified priority status. The one-step image outside cyclic-`00` avoidance, multistep reachability, and reversal/rotation quotients remain outside scope.
