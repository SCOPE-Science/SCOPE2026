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

The universal proof uses only the following identities from the motivating source:
\[
AX=0,\quad FX=I_k,\quad FG=0,\quad GE=0,\quad YA=0,\quad YE=I_k,
\]
\[
AG+EY=I_n,\qquad GA+XF=I_n.
\]
Together with the source's direct sums, they give \(\psi^{-1}T_D\phi=A_0\oplus D\) by one substitution. The kernel and cokernel statements are therefore exact module statements, not numerical experiments.

For generalized inverses, symbolic multiplication gives
\[
T_D(G+XHY)T_D=A+E(DHD)F
\]
and
\[
(G+XHY)T_D(G+XHY)=G+X(HDH)Y.
\]
The converse uses
\[
YT_D=DF,\qquad T_DX=ED.
\]
Hence an inner inverse of \(T_D\) produces one of \(D\) through \(FQE\).

`verify_structured_defect.py` is a supplementary exact-arithmetic replay. It works over \(\mathbb F_3\) in a canonical \(5\)-by-\(5\) instance, exhausts all \(81\) matrices in \(M_2(\mathbb F_3)\), and verifies factorization, rank transfer, reflexive-inverse transfer, and the converse inner-inverse construction. `verification_structured_defect.log` ends with `CHECK_OK`.

The finite replay does not certify the universal ring statement; the displayed algebraic identities do. The result does not address weaker hypotheses where either source or target splitting can fail.
