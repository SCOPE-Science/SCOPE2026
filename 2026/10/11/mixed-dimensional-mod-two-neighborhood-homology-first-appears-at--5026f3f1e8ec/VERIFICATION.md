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
The bundled verifier reconstructs the triangular graphs and neighborhood complexes from definitions only. It exhaustively enumerates every simplex for \(3\le n\le7\), forms all simplicial boundary maps over \(\mathbf F_2\), computes exact ranks by binary Gaussian elimination, and derives the Betti vectors from chain dimensions and adjacent boundary ranks.

For \(T_7\), the checked face vector is \( (21,210,1190,3780,5187,4410,2520,945,210,21) \), and the boundary ranks are \( (20,190,1000,2534,2646,1764,756,189,21) \). These give reduced ranks \(246\) in degree \(3\) and \(7\) in degree \(4\).

The verifier also checks that \(T_3,T_4,T_5,T_6\) have reduced mod-two homology in exactly one degree and verifies the Euler characteristic from both the face vector and the Betti vector. No floating-point arithmetic, sampling, or incompleteness inference is used. A successful replay prints `VERIFY_OK`.
