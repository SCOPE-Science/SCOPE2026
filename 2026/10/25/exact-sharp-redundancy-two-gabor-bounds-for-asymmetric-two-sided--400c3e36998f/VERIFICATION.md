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

# Mathematical verification

The main result follows analytically by unitary Zak decomposition of the redundancy-two frame operator, a strict scalar convexity argument in its frequency coordinate, and a single positive-root quadratic in the spatial coordinate. All hypotheses are \(a,b>0\), fixed translation step \(1\), modulation step \(1/2\), and the continuous window specified in `RESULT.md`. Absolute convergence of the two geometric series follows from \(e^{-a},e^{-b}\in(0,1)\); the positive Gram determinant establishes a strictly positive lower bound.

The attached `check_asymmetric_exponential_gabor.py` can be executed with Python 3 and no third-party modules. It checks 64 positive parameter pairs, both extremal formula values against direct Zak evaluation, a finite \(21\times41\) Zak grid for every pair, and 49 exact rational identities. Observed output:

```
CHECK_OK: 64 two-parameter grids; 49 exact rational determinant/end-fiber checks
```

Finite checks do not prove global optimality over the infinite Zak torus; only the exact analysis does. The earlier symmetric exponential frame-bound theorem and qualitative totally-positive frame-set results are separate prior work. Complete historical priority, especially an inaccessible 1996 paper, and any independent audit remain unperformed.
