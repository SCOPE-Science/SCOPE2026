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

The verified claim is:

Let \(E_m=\operatorname{span}\{e_1,\ldots,e_m\}\subset c_0\), \(Y=(\bigoplus_{m\ge1}E_m)_{\ell_1}\), and let \(Q:Y\to c_0\) be the summation quotient from Acuaviva's construction. Put \(Z=(\bigoplus_{m\ge1}E_m^*)_{c_0}\), so \(Y=Z^*\), and let \(P=J_Z^*:Y^{**}\to Y\) be the natural projection. For every isometric lifting \(S:c_0\to Y^{**}\) obtained by the weak-star ultralimit construction of Proposition 4.1 of arXiv:2607.12935v1, one has \(PS=0\). Consequently, for every \(x\in c_0\), \[\inf_{Qy=x}\|Sx-J_Yy\|_{Y^{**}}=2\|x\|_\infty.\] For every \(\varepsilon>0\), if \(Y_\varepsilon\) carries the norm \(\|y\|_\varepsilon=\max\{\varepsilon\|y\|_Y,\|Qy\|_\infty\}\), then \[\inf_{Qy=x}\|Sx-J_Yy\|_{Y_\varepsilon^{**}}=2\varepsilon\|x\|_\infty.\] Thus the factor \(M+1=2\) in the canonical lifting-to-fiber comparison used in Acuaviva's lower-bound mechanism is sharp for this summation quotient and this ultralimit lifting construction; no claim is made that the resulting global retraction lower bound is itself optimal.

The focal construction was checked at the level of its directed local liftings. For each fixed \(N\), moving to the tail whose finite-dimensional datum contains \(e_{N+1}\) forces the first support index past \(N\). Therefore the weak-star ultralimit annihilates every finitely supported vector of
\[
Z=\left(\bigoplus_{m\ge1}E_m^*\right)_{c_0},
\]
and density gives \(PS=0\).

The structural input was checked against the standard M-ideal reference: \(c_0\)-sums of M-embedded spaces are M-embedded, and for an M-embedded space the natural projection from the third dual onto the dual is an L-projection. Hence
\[
Y^{**}=J_Y(Y)\oplus_1\ker P.
\]
The focal paper supplies the isometry of \(S\), the norm-one quotient property of \(Q\), and the bidual formula for the renorming. These inputs give the exact two displayed distance formulas without approximation.

The result does not show that arbitrary liftings have the same profile and does not determine the global retraction constant. No finite computation, sampling argument, or numerical tolerance is used.
