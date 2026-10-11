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
The proof certificate is `verify_recurrence.py`. It uses only the Python standard library and exact integer Laurent-polynomial arithmetic.

It reconstructs the fourteen noncrossing-pairing basis of \(TL_4\), checks diagram concatenation with loop factor \(\delta=-A^2-A^{-2}\), forms
\[
B=\rho(\sigma_1\sigma_3\sigma_2^4),\qquad S=\rho(\sigma_1\sigma_3),
\]
constructs the factorized degree-six polynomial \(P_A\), and verifies the full state identity
\[
P_A(B)S=0.
\]
This identity is stronger than checking finitely many closed braids and implies the recurrence for every \(t\ge0\).

The verifier also checks the normalization values
\[
F_0=-A^8-A^4
\]
and
\[
F_1=-A^{14}-3A^6+A^2-4A^{-2}+2A^{-6}-3A^{-10}+A^{-14}-A^{-18}.
\]

Expected replay output:

`VERIFY_OK basis=14 block_terms=8 tail_terms=4 annihilator_degree=6 state_identity=true F0_terms=2 F1_terms=8`

Unproved limits: minimal recurrence order, asymptotic root dominance, coefficient-sign laws, and Khovanov-to-Jones cancellation are not asserted.
