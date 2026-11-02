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

# Reproducible numerical verification

Run `python verify.py` with a Python 3 interpreter; no third-party libraries or external datasets are required.

The script enumerates every reduced-row-echelon subspace for each test configuration and checks the graph Lie bracket directly for all basis pairs. It constructs the predicted counts independently from induced-subgraph components, Gaussian binomials, and finite-field subspace-lattice inversion. It also independently enumerates all subspaces of full graph Lie algebras (including central edge basis elements), comparing the complete abelian-subalgebra dimension distributions with the central-lift prediction.

Observed result: `VERIFY_OK 158 quotient graph-field cases and 44 full-Lie-algebra cases; independent RREF-bracket enumeration vs connected-support Möbius and Gaussian formulas`. The quotient cases include all labelled simple graphs on at most four vertices over the prime fields of orders two and three, with additional characteristic-five cases. The full-Lie cases include both zero-edge and nonzero-edge graphs and both even and odd characteristics.

For the path on four vertices, the direct full-Lie counts for dimensions zero through seven are `1,127,747,771,155,5,0,0` over the binary field and `1,1093,9796,8932,859,7,0,0` over the ternary field. The same sequences are obtained from the closed formula.

These exhaustive finite calculations do not establish results for all graph sizes or extension fields; the complete proof in `RESULT.md` supplies that argument. No independent mathematical audit has been performed.
