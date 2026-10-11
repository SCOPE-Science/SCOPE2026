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
The proof was reconstructed from the defining formulas rather than from the convergence statement alone.

Checks performed:
- The paired-direction construction and normalization of \(U\) were matched to Lemmas 2.1--2.2.
- The dual relation \(V_i=(U_{i+1}-U_i)/[U_i,U_{i+1}]\) and its reverse relation to \(U\) were matched to Section 2.2.
- The central equidistant \(M_i=(P_i+P_{i+n})/2\), the edge coefficients, the half-sums, and the involute formula were matched to equations (3.1), (3.5), (3.14), and (4.1).
- The convergence premise used to prove \(A_U^k\to0\) was checked against Theorem 5.1.
- The open question asking for a direct method was checked immediately after Theorem 5.1.
- `verify.py` was run with exact rational arithmetic and returned `VERIFY_OK`.

The checker validates a representative nontrivial case and the indexing identities. It is not an exhaustive proof over all polygons; generality comes from the symbolic argument in `RESULT.md`.

Scientific limit: the result is specific to the Craizer--Martini constant-width Minkowski involute. It does not assert that this central point equals a classical Steiner or affine center.
