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

The primary theorem was checked from the full text together with the Douglas lemma it cites. The source defines the optimal lower bound by
\[
A=\sup\{\lambda>0:\lambda KK^*\le S_\Lambda\}.
\]
Therefore
\[
\inf\{\mu>0:KK^*\le\mu S_\Lambda\}=A^{-1},
\]
not \(A\).

For every \(K\)-dual,
\[
K=T_\Lambda T_\Gamma^*,
\]
so
\[
KK^*
=T_\Lambda T_\Gamma^*T_\Gamma T_\Lambda^*
\le
\|T_\Gamma\|^2S_\Lambda.
\]
This proves \(\|T_\Gamma\|^2\ge A^{-1}\). Douglas factorization supplies a reduced factor with squared norm exactly \(A^{-1}\).

The scalar counterexample uses \(\Lambda_1=2I\). Its frame energy is \(4\|f\|^2\), hence \(A=4\), while duality forces \(\Gamma_1=I/2\) and gives \(\|T_\Gamma\|^2=1/4\).

For the nonuniqueness counterexample, direct multiplication gives
\[
S_F=\operatorname{diag}(2,4)
\]
and
\[
S_{G_t}=\operatorname{diag}\left(\frac12,\frac14+2t^2\right).
\]
The reconstruction identity
\[
\sum_{j=1}^3\langle x,g_j(t)\rangle f_j=x
\]
holds for every \(x\in\mathbb C^2\) and every real \(t\). Thus every \(G_t\) is a dual, and all \(|t|\le1/(2\sqrt2)\) satisfy
\[
\|T_{G_t}\|^2=\frac12=A^{-1}.
\]
The symbolic outer-product computation was replayed from the explicit vectors; no floating-point calculation is needed.

For \(t=0\), the dual analysis range is contained in
\[
R(T_F^*)=\{(a,a,b):a,b\in\mathbb C\},
\]
while for \(t\ne0\), \(T_{G_t}^*e_2\) has first two coordinates \(t\) and \(-t\). This verifies that the reduced-range condition singles out the Douglas solution although the minimum operator norm does not.
