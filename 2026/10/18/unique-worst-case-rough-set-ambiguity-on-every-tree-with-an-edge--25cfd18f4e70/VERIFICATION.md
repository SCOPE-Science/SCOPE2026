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

# Reproducibility and limitations

Run `python3 verify.py` with a standard Python 3 installation; no external packages, data files, or network access are required. The checker enumerates every Prüfer sequence for tree orders 2 through 7, giving exactly 18,248 labeled trees, and explicitly examines every vertex subset in each case. It computes both approximation operators from closed neighborhoods, groups each realized rough observation's inverse fiber by the number of cut edges, independently enumerates tree edge covers, and confirms all polynomial coefficients. It checks the strict maximal-fiber assertion and a separate bottom-up edge-cover dynamic program.

It further tests 600 pseudorandom labeled trees with a recorded fixed seed (150 each of orders 8, 9, 10, and 11). The recorded successful output is:

```
LABELED_TREES 2 1
LABELED_TREES 3 3
LABELED_TREES 4 16
LABELED_TREES 5 125
LABELED_TREES 6 1296
LABELED_TREES 7 16807
VERIFY_OK exhaustive_labeled_trees= 18248 individual_rough_fibers= 1462212 central_colorings= 189520 sampled_larger_trees= 600 edge_cover_polynomial=PASS fiber_shift_dominance=PASS unique_maximum=PASS tree_dp=PASS
```

These finite tests neither exhaust all trees nor certify originality. Correctness for arbitrary finite tree order relies on the explicit graph-cut and injection proof in `RESULT.md`. Independent external audit has not been performed.
