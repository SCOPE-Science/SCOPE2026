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
# Verification

The proof in `RESULT.md` is the analytic evidence for arbitrary input graphs. The script `artifacts/verify.py` provides independent finite corroboration rather than an external certification.

It constructs the central graph from each original graph's edges, lists all nonempty vertex subsets, tests independence and domination directly from central-graph adjacency, and computes the full bivariate table indexed by total selected size and selected original count. A separate routine computes the claimed bivariate polynomial from vertex degrees, degree-one neighbors, and degree sums on original edges. The tables agree coefficientwise.

The range is all \(88\) connected triangle-free unlabeled graphs of original orders \(3\) through \(7\) in NetworkX `graph_atlas_g`. The run examines \(3,098,568\) nonempty subset candidates, verifies the minimum count and total count, and compares the two six-vertex spiders with the stated polynomials.

Executed with Python 3 and NetworkX `3.6.1`. Replay command from the extracted package root:

```sh
python -m pip install -r artifacts/requirements.txt
python artifacts/verify.py
```

Expected output, also embedded in `artifacts/verification_output.txt`:

`ALL CHECKS PASSED; connected_triangle_free_atlas_graphs=88; subsets_examined=3098568; original_orders=3..7; bivariate_polynomials=yes; minimum_counts=yes; spider_profiles=2`

This finite test cannot establish a theorem for arbitrary order; the bidirectional three-template argument is the proof. No independent audit has been performed.
