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

Define
\[
Ue_{2n}=e_n,\qquad Ue_{2n-1}=0.
\]
Then
\[
U^*e_n=e_{2n},
\qquad
UU^*=I,
\]
so \(U\) is a surjective coisometry.

For
\[
D(x_n)=(n x_n),
\qquad
\operatorname{Dom}(D)=\{x:(n x_n)\in\ell^2\},
\]
the graph is closed. Interlacing that graph into the odd and even coordinates gives the closed subspace
\[
W=
\left\{
\sum_{n\ge1}(n x_ne_{2n-1}+x_ne_{2n}):
x\in\operatorname{Dom}(D)
\right\}.
\]
Directly,
\[
UW=\operatorname{Dom}(D).
\]
The vector
\[
(1/n)_{n\ge1}
\]
lies in \(\ell^2\) but not in \(\operatorname{Dom}(D)\), while its finite truncations lie in the domain and converge to it. Thus \(UW\) is nonclosed.

With \(K=I\), \(W_1=W\), \(W_2=H\), \(\Lambda_1=\pi_W\), \(\Lambda_2=I\), and unit weights,
\[
\|\pi_Wf\|^2+\|f\|^2
\]
lies between \(\|f\|^2\) and \(2\|f\|^2\). Hence the input family satisfies the source definition.

For the exact boundary, a surjective \(U\) factors through the quotient \(q:H\to H/N(U)\) as a Banach-space isomorphism after quotienting. Therefore \(UW\) is closed exactly when \(q(W)\) is closed, which is equivalent to
\[
q^{-1}(q(W))=W+N(U)
\]
being closed.

The target full text was checked at the definition requiring closed subspaces, the lemma using \(\pi_{\overline{TW}}\), and the theorem proof using \(\pi_{UW_j}\). No numerical approximation or finite-search inference is used.
