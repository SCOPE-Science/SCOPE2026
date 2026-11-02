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

# Verification performed

The independent-of-formula symbolic construction in `verify_dual.py` uses sparse polynomials over the polynomial ring with coefficient field \(\mathbb F_2\), with four dual coordinates and ten independent quadric coefficients. It reconstructs the eleven nonzero universal monomials of \(G\), verifies their total coordinate degree twelve, checks all four exact partial derivatives, the four nonzero coordinate-plane restrictions, the orders four along all six coordinate lines, the orders eight at all four vertices, and the substitution identity \(G(C(x))=P(x)^8(P(x)+Q(x)^2)\). All assertions passed.

For the example \(Q=\sum_i x_i^2+\sum_{i<j}x_ix_j\) over \(\mathbb F_4\), the checker exhausts \(85\) projective ambient points, finds twelve primal singular points, and finds eighteen points of each torus surface, mutually identified by the Cremona map. It also exhaustively checks the boundary support of the dual in that finite field. Standard output was:

```text
CHAR2_DUAL_CREMONA_DEGREE12_SIX_QUADRUPLE_EDGES_FOUR_OCTUPLE_VERTICES_PASS
universal_terms 11 projective_F4_points 85 F4_nodes 12 torus_X_points 18 torus_dual_points 18
```

All-family claims rest on the explicit universal algebraic proof in `RESULT.md`; a finite-field census alone does not establish them. The symbolic checker is a consistency check of algebraic identities, not an external or independent mathematical audit. No normalization, conductor or full Jacobian singular scheme was computed or certified.
