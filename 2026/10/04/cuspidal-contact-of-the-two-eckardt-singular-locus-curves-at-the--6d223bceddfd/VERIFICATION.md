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
The exact checker is `artifacts/verify.py`. It uses symbolic arithmetic over \(\mathbb Q\) to reconstruct the two centered Sylvester root patterns, calculate their elementary symmetric invariants, eliminate the normalization parameters, verify the two cusp ideals, and compute the sum ideal.

Expected output:

`VERIFY_OK`

The proof is characteristic-zero and the geometric statement is over \(\mathbb C\). The checker verifies the algebraic identities and zero-dimensional quotient length; the identification of these invariant coordinates with the local \(S_5\)-quotient is the standard reflection-invariant fact \(\mathbb C[\sum y_i=0]^{S_5}=\mathbb C[e_2,e_3,e_4,e_5]\).

No computation at the Fermat point is included or claimed.
