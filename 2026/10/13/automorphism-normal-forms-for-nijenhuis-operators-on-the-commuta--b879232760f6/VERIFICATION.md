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
The bundled checker `artifacts/verify.py` reconstructs the associative product
\[
e_1e_2=e_2e_1=e_3
\]
and the Nijenhuis torsion.

It verifies symbolically that in characteristic different from \(2\) the solution set is the union
\[
\mathcal C_1\cup\mathcal C_2
\]
of the two affine \(5\)-spaces stated in `RESULT.md`.

For odd finite fields it constructs the full automorphism group and checks preservation of the multiplication.

Over \(\mathbf F_3\) and \(\mathbf F_5\), it computes every Nijenhuis conjugacy orbit and verifies that every orbit contains exactly one canonical representative from the displayed normal-form list. The orbit counts are
\[
39,\qquad105,
\]
equal to
\[
q(4q+1).
\]

It also checks the raw counts and rank profiles over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]

The checker returns `VERIFY_OK`.

Finite-field enumeration is replay evidence. The normal-form theorem is proved symbolically in `RESULT.md`.
