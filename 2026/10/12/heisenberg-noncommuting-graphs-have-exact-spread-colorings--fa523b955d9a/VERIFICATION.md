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
The proof is symbolic.

The packaged checker `artifacts/verify.py` works on the projective quotient of the Heisenberg graph. Each projective point corresponds to
\[
q(q-1)
\]
element-level vertices with identical neighborhoods and no edges among them.

For \(H_2(2)\), the checker constructs the \(15\)-vertex projective symplectic graph, exhaustively proves that no independent \(4\)-set exists, and verifies a five-part symplectic spread. Hence
\[
\alpha_{\mathrm{proj}}=3,\qquad\chi_{\mathrm{proj}}=5,
\]
which gives
\[
\alpha(\mathcal N(H_2(2)))=6,\qquad\chi(\mathcal N(H_2(2)))=5.
\]

For \(H_2(3)\), it constructs the \(40\)-vertex projective graph using the trace form on \(\mathbf F_9^2\), exhaustively proves that no independent \(5\)-set exists, and verifies a ten-part Desarguesian symplectic spread. Hence
\[
\alpha_{\mathrm{proj}}=4,\qquad\chi_{\mathrm{proj}}=10,
\]
which gives
\[
\alpha(\mathcal N(H_2(3)))=24,\qquad\chi(\mathcal N(H_2(3)))=10.
\]

It also checks that every maximum independent set in the \(\mathbf F_2\) test case spans a maximal totally isotropic subspace.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the all-\(q\), all-\(n\) theorem.
