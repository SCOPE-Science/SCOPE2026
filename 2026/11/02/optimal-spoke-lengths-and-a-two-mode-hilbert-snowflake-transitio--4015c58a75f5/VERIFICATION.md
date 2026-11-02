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

# Verification of the weighted-wheel classification

Run `python verify.py` from the directory containing this document. The script needs Python 3 and NumPy; no downloaded data and no external network access are required. The replay for this result returned:

```
PASS standalone metric, quadratic form, spectral threshold, multiplicity and asymptotic checks: 10362
n=4: critical spoke length and optimal exponent: (0.7071067811865476, 2.0)
n=5: critical spoke length and optimal exponent: (0.8399793136490875, 1.8552059610742986)
```

The checker constructs every wheel from edge weights, runs Floyd–Warshall to compute all distances, forms independently the powered-distance matrices, diagonalizes their restrictions to the zero-sum hyperplane, and verifies agreement with the critical exponent and equality-space dimension. It covers integers \(4\le n\le16\), six spoke lengths per integer (including endpoints and the transition), and four random zero-mass quadratic-form comparisons per case. It also tests predicted large-rim expansions at four larger values using the analytic scalar formulas.

The finite replay is neither a computer-assisted all-dimensional proof nor an independent mathematical audit. The proof of the universal result is the complete mean/contrast decomposition, exact mode eigenvalues, strict scalar monotonicity, and explicit transition calculation in `RESULT.md`. No external verification or publication has been performed.
