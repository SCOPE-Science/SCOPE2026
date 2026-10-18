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

# Computational and proof verification

Run `python3 verify.py` with Python 3 and its standard library. The script independently constructs the full rooted-tree endomorphism monoid by selecting a local map from each \(b\)-point child set and propagating it along the tree, then checks \(F(F(v))=F(v)\) for every vertex. Its resulting actual rank histograms are compared with a separate recurrence over retained labeled image subtrees. The five exhaustive parameter pairs are \((2,1),(2,2),(2,3),(3,1),(3,2)\), totaling \(547{,}920\) actual morphisms. All coefficients and the image counts agree; additional recurrence checks include \((2,4)\) and \((4,1)\). Successful execution ends `ALL_EXACT_CHECKS_PASSED`.

The general theorem relies on the written proof: fixed-point subtrees are full-height and prefix-closed; subtree maps factor independently through child choices; the multiset recurrence counts each image separately; and interval overlap establishes every possible rank. The finite checker is not an infinite-parameter proof or an independent mathematical audit. The prior general wreath-product theorem covers scalar total idempotent counts in principle, but not the full all-level rank refinement established here.
