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
# Reproducibility and proof boundaries

Run `python verify.py` from the directory containing the package. The script uses the Python standard library only; it independently computes grounded full-product Kirchhoff inverses and compressed base-graph resolvents over rational numbers.

Observed output:
```
Compressed exact-rational all connected labeled graphs n<=4: 129 PASS
Direct full-graph Kirchhoff vs compressed resolvent: 18 PASS
Sharp K2 identities m=4..64, and failure at m=3: PASS
All fixed-graph large-clique checks: PASS
```

The universal edge-resistance bound and the exact norm inequality follow algebraically from the Kronecker Laplacian decomposition, inverse positive-semidefinite order, and the column identity. The asymptotic statement follows from finite-dimensional resolvent convergence. The computation tests sample cases and sharpness formulas only; it is neither exhaustive for unbounded graph size nor a substitute for proof.

The original electrical-products paper of Bollobás–Brightwell (1997) could be inspected only through its abstract. No independent mathematical audit is included.
