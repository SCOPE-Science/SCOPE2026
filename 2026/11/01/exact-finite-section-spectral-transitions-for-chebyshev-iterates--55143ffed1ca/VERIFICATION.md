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

The reproducible checks were executed using `python verify.py` with NumPy. Output:

```
PASS: 1392 finite spectral/cutoff/discrepancy cases;
PASS: 7 independent Chebyshev quadrature cases;
PASS: 8 exact logistic-iterate resolution thresholds.
These checks are finite corroboration; the general claims require the written proof.
```

The direct matrices were assembled from the independent Chebyshev trigonometric product identity, while predicted spectra were assembled from the residue-class block decomposition. For seven parameter pairs, a separate midpoint cosine quadrature gave an additional matrix-construction cross-check. The finite CDF comparisons covered multiple block sizes and both parities. The infinite-rank, arbitrary-degree, and asymptotic results are proved in RESULT.md; finite tests are not completeness certificates or independent validation. Numerical double precision was used for the matrix and eigenvalue comparisons, while the paper gives exact algebraic formulas.
