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

For
\[
Q=b^{-2}I-(b^{-2}-a^{-2})e_1e_1^{\mathsf T},
\]
the compression to a subspace \(E\) is
\[
Q|_E
=
b^{-2}I_E-(b^{-2}-a^{-2})(P_Ee_1)(P_Ee_1)^{\mathsf T}.
\]
Therefore its least eigenvalue is
\[
b^{-2}-(b^{-2}-a^{-2})\|P_Ee_1\|^2.
\]

If \(E\) is Haar-uniform of codimension \(n\), then
\[
T=\|P_{E^\perp}e_1\|^2
\sim
\operatorname{Beta}\!\left(\frac n2,\frac{N-n}{2}\right),
\]
so
\[
R_n^{-2}=a^{-2}+(b^{-2}-a^{-2})T.
\]
This is the complete analytic proof of the random-radius law.

The bundled checker performs four supplementary replays:

1. It constructs deterministic pseudorandom Haar subspaces by QR factorization and compares the smallest compressed eigenvalue with the rank-one formula.
2. It checks the exact beta mean and variance
\[
\mathbb ET=\frac nN,
\qquad
\operatorname{Var}(T)=\frac{2n(N-n)}{N^2(N+2)}.
\]
3. It numerically integrates the beta density for selected moments and compares with the hypergeometric expression.
4. It compares the beta-tail probability with the direct threshold transformation for several \((N,n,a/b,C)\) choices.

The computations are not used to infer any infinite or all-dimensional statement. The proof above supplies the quantifiers for every \(N\ge2\), \(1\le n<N\), and \(a>b>0\).

No claim is made for joint section eigenvalue laws beyond the one-spike case.
