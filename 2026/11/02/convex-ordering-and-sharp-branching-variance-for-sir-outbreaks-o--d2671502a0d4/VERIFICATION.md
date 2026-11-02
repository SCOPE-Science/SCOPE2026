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

# Verification performed

The exact-rational checker `verify_tree_variance.py` independently constructs finite probability-generating functions of final outbreak size, rather than reusing the two-path covariance proof. It enumerates every labelled tree represented by a Prüfer sequence on \(2\le n\le6\), every choice of root, and three transmission laws with two distinct means. It confirms the mean and variance identities, both index expressions, and the size bound for 25,428 tree/law/root comparisons. Output includes `PASS 25428 exact rooted tree/law comparisons`.

The separate `check_convex_order.py` checks the complete set of integer stop-loss inequalities \(\mathbb E[(N-k)_+]\) across two convex-ordered triplets of transmissibility laws on the same tree family. It verifies 117,088 exact-rational comparisons; output includes `CONVEX_ORDER_PASS 117088 stop-loss triplet checks`.

Run from the directory containing both files, with standard Python 3 only:

```sh
python verify_tree_variance.py
python check_convex_order.py
```

The computations are finite checks. The general theorem depends on the analytic unique-route pair formula, nonnegative mixed discrete convex differences, and a sharp counting bound. Independently established originality and scientific validation remain unperformed.
