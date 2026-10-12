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

The reported proof uses exact endpoint expansions, an explicit uniform derivative bound and complete tree-index extremal arguments. Reproduce the finite check using `python3 verify.py` (Python standard library only). The executed result was:

```text
VERIFY_OK labeled_trees=1437 sizes=4..6 endpoint_order_and_both_taylor_coefficients=exact quartic_difference=exact
```

The checker exhausts all labeled trees through six vertices and all their bond configurations. The statements for arbitrary order follow from the mathematical proof, not from the finite check. No stochastic simulation, independent replication, or external certification has been performed. The 2020 directly relevant path/star paper was available only in abstract form; the resulting literature-comparison risk is disclosed in the review.
