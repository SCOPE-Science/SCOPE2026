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

A standalone Python 3 exact verifier is provided as `verify_ap_runs.py`. Run from the artifact directory:

```
python verify_ap_runs.py --max-n 13
```

Observed output on the packaged copy: `PASS: 806 exact assertions (n through 13).`

The verifier enumerates complete fixed-cardinality sample spaces for \(4\le n\le13\), computes the arithmetic-progression count and occupied adjacency count for every sample, and independently constructs every progression/adjacent-pair intersection. It verifies the covariance against the complete hypergeometric overlap sum and the endpoint-interpolated expression. It checks integer identities for the positive endpoint coefficients, signs, and the three-run nonmonotone conditional-regression example.

For the **all-size** conclusion, inspect the proof in RESULT.md: exactly three overlap classes determine the covariance; after removing the positive progression-inclusion probability, the remaining function of sample size is a quadratic with root at full occupancy; dividing by the missing-vertex count gives an affine function whose two endpoint values are explicitly positive. The singular \(n=\ell+1\) case is counted separately. No finite program run by itself proves these claims for arbitrarily large parameters. The model is not extended to arbitrary hypergraphs, cyclic progressions, nonuniform weights or stochastic domination. No independent audit has been performed.
