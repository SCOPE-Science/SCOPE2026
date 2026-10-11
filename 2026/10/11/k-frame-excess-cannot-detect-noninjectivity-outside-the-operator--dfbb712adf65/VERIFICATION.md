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

Let
\[
H=\operatorname{span}\{e_0\}\oplus\ell^2(\mathbb N),
\qquad
K=P_{\operatorname{span}\{e_0\}}.
\]
On the second summand, let
\[
Bf_1=0,
\qquad
Bf_{n+1}=f_n.
\]
Then \(B\) is onto and
\[
N(B)=\operatorname{span}\{f_1\}.
\]
Therefore
\[
U=I\oplus B
\]
is onto and noninjective.

Because \(U\) is block diagonal,
\[
UK=KU,
\]
and \(R(K)^\perp\) is invariant under \(U\).

For
\[
\Phi=\{e_0\},
\]
one has
\[
|\langle x,e_0\rangle|^2=\|K^*x\|^2
\]
for every \(x\), so \(\Phi\) is a Parseval \(K\)-frame. Its only atom is indispensable, hence
\[
E_K(\Phi)=0.
\]
Also
\[
P_{R(K)}\Phi=\Phi,
\qquad
U\Phi=\Phi.
\]
Thus
\[
E_K(\Phi)=E(UP_{R(K)}\Phi)=E_K(U\Phi)=0,
\]
while \(f_1\in N(U)\).

For the finite-excess repair, let \(\Psi\) be a frame for \(M=R(K)\), let \(T_\Psi\) be its onto synthesis operator, and let \(V=U|_M\), which is onto under the source hypotheses. The restriction
\[
T_\Psi:\ker(VT_\Psi)\to\ker V
\]
is onto and has kernel \(\ker T_\Psi\). Therefore
\[
0\to\ker T_\Psi\to\ker(VT_\Psi)\to\ker V\to0
\]
is exact. Taking dimensions in the finite-excess regime gives
\[
E(V\Psi)=E(\Psi)+\dim\ker V.
\]
Hence equal finite excesses are equivalent to
\[
N(U)\cap R(K)=\{0\}.
\]

The target article was inspected in the actual full text at the relevant Section 5 pages. The counterexample and repair use exact operator identities, not numerical evidence or finite approximation.
