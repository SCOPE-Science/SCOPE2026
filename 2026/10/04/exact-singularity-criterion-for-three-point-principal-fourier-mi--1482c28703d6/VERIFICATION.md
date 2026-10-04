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

The proof was reconstructed from the determinant of a translated principal submatrix and checked at each algebraic branch. The critical identities are:

\[
\det F_N[\{0,a,b\}]=(\omega^{a^2}-1)(\omega^{b^2}-1)-(\omega^{ab}-1)^2,
\]

and, after the nonzero-right-side phase argument gives \(N\mid(b-a)^2\),

\[
( X-1)(XR^2-1)-(XR-1)^2=-X(R-1)^2.
\]

The standalone script `verify_three_point_principal.py` uses integer polynomial arithmetic to construct \(\Phi_N\), reduce determinant powers exactly modulo \(\Phi_N\), and compare determinant vanishing against three independently coded forms of the criterion. Running it prints:

`MAX_N 120`

`NORMALIZED_TRIPLES 280840`

`SINGULAR_NORMALIZED_TRIPLES 2602`

`SQUAREFREE_MODULI 73`

`VERIFY_OK`

The computation covers every normalized three-point set for \(3\le N\le120\). It does not prove the infinite theorem; the proof is the symbolic argument in `RESULT.md`. No claim is made for nonprincipal minors or for principal minors of order at least four.
