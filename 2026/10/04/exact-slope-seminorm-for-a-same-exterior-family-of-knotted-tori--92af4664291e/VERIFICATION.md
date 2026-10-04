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

The proof was checked against the actual source statements used.

For Nifa's exterior, Proposition 2.3 gives
\[
\mu\mapsto\mu,\qquad \lambda\mapsto\lambda,\qquad s\mapsto\lambda^{-N},
\]
and the filling-coordinate calculation states
\[
\lambda_r\mapsto\lambda,\qquad s_r\mapsto\lambda^{-N}.
\]
Thus a tangent class \(a[\lambda_r]+b[s_r]\) represents \(\lambda^{a-Nb}\). The same proposition gives \(H_1(E_N)\cong\mathbb Z\langle\mu\rangle\), and Theorem 6.5 proves
\[
\operatorname{scl}(\lambda^N)=\frac{N-1}{2}.
\]
Its proof explicitly expresses \(\lambda\) as a commutator. Homogeneity of stable commutator length therefore gives
\[
\operatorname{scl}(\lambda^{a-Nb})=\frac{N-1}{2N}|a-Nb|.
\]

Liu--Ni--Sun--Wang's Definition 4.4 and Remark 4.5 were checked in the journal PDF. They identify their induced slope seminorm with stable commutator length and extend it uniquely to \(H_1(T^2;\mathbb R)\).

For a primitive integral slope \((a,b)\) with \(a-Nb=Nq\ne0\), Nifa's Lemma 6.6 and Theorem 6.5 give
\[
g_{\mathrm{sing}}=\operatorname{cl}(\lambda^{Nq})
=1+\left\lceil\frac{|q|(N-1)}2\right\rceil.
\]

The bundled arithmetic regression check reports:

`VERIFY_OK cases=75429 N=2..30 box=-25..25 kernel=true surgery_direction=true sublattice_genus=true`

This finite computation checks only arithmetic consequences over representative ranges. It is not used as evidence for the universal group-theoretic statements.

No independent audit has been performed.
