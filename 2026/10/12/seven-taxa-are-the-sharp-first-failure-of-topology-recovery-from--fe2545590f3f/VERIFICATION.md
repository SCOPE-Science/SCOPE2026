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

Run `python3 verify_pd.py` with Python 3 and the standard library; no external files are required. The checker constructs every unordered rooted binary shape with one through seven tips by the exhaustive child-pair recursion, verifies published shape counts \((1,1,1,2,3,6,11)\), checks all supports through six are distinct, and identifies the unique duplicated support at seven. It then rebuilds the two height-annotated witness trees, verifies strictly positive lengths and four-unit root-to-tip distance, computes the full spectrum \((12,3,2,1,0,0)\), enumerates all \(2^7\) possible leaf subsets across all sample sizes without floating point, verifies the hypergeometric mean formula and its explicit triangular inverse, and independently evaluates all 21 unordered two-tip outcomes in each witness.

Expected passing marker: `VERIFY_OK`. Exact two-tip frequencies by rooted diversity \(5,6,7,8\) are \((1,4,4,12)\) and \((2,2,5,12)\); exact population variances are \(128/147\) and \(142/147\). The full curve is \((0,4,51/7,351/35,433/35,101/7,114/7,18)\). These finite checks verify the complete seven-tip witness and the fully enumerated lower-bound domain, not the claim for arbitrarily many tips. That part is established by the grafting proof in RESULT.md, and independent audit remains unperformed.
