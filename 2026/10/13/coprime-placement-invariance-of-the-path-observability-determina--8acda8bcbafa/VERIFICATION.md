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

# Reproducibility and scope of checks

Run `python3 checker.py` with Python 3 and no external dependencies. The checker uses exact rational numbers and Gaussian elimination to recompute every finite-horizon Gramian, determinant, and rank for \(2\le n\le8\), \(\alpha\in\{0,3/5,-1/3\}\), \(\beta\in\{1/5,-2/7\}\), \(H\in\{n,n+1,n+2\}\), and every sensor \(1\le j\le n\). The output is:

```
VERIFY_OK 630 exact-rational finite tests; 630 determinants; 630 ranks; n=4 trace contrast.
```

The check establishes agreement with the proposed formulas on those 630 instances, including the singular sensor ranks and determinant equality across all coprime nodes. It additionally verifies an exact four-state example with different traces but identical determinants. The all-dimensional proof rests on the distinct Dirichlet sine eigenvectors, a finite Vandermonde rank argument, the roots-of-unity sine product, endpoint Krylov triangularity, and the Cauchy identity for the stable infinite-horizon kernel. The symbolic argument—not the finite samples—establishes the universal quantifiers. The stable infinite-horizon product is not independently evaluated by this finite rational checker.

The source comparisons concern arXiv:1109.3556, arXiv:1308.1201, and arXiv:1306.2491, and the residual possibility of an equivalent result in other literature is retained. Independent auditing has not been performed.
