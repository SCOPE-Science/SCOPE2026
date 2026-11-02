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

Run `python3 verify_subdivision_clique.py` in an environment with NumPy available. The script reconstructs each actual full-subdivision adjacency matrix and computes return probabilities from spectral projectors, not from the closed formulas alone. It checks clique orders \(3\le n\le16\), both site types, and all 771 connected labeled simple graphs with \(2\le n\le5\) to compare the subdivision identity against an independently diagonalized signless Laplacian.

Observed output:

```
PASS: 14 independent adjacency-matrix diagonalizations; exact spectra and all vertex return values match.
PASS: general subdivision identity for all 771 connected simple graphs on 2–5 vertices.
```

The proof in `RESULT.md` verifies every graph/order analytically, including degeneracies, graph bipartiteness and kernel multiplicity. Finite numerical calculations do not certify an infinite statement; eigendecomposition grouping and floating tolerance affect only corroborating checks. Independent audit and independent validation have not been performed.
