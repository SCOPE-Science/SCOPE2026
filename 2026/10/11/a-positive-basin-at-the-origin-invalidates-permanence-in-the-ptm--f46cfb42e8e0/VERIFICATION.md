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

The printed update map was checked directly. At the origin its Jacobian is lower triangular,
\[
DT(0)=
\begin{pmatrix}
0&0&0\\
\rho_2&0&0\\
\alpha&1-\alpha&\alpha_0
\end{pmatrix},
\]
so the discrete multipliers are \(0,0,\alpha_0\).

For the explicit admissible point
\[
(\rho_1,\rho_2,\alpha,\alpha_0)=\left(2,1,\frac12,\frac12\right)
\]
and \(V=3H+P+G<1/16\), positivity and \(\tanh P\le P\) give
\[
H'\le\frac18H,\qquad P'\le H,\qquad
G'=\frac12G+\frac12H+\frac12P.
\]
Thus
\[
V'\le\frac{15}{8}H+\frac12P+\frac12G
\le\frac34V.
\]
This is an infinite-time proof because the same inequality makes the neighborhood forward invariant and can be iterated for every \(n\).

The bundled `verify.py` replays the rational coefficient inequalities and the triangular Jacobian structure using only the Python standard library. It does not use a finite orbit simulation as a substitute for proof.

Limits: no global basin classification is asserted; no claim is made for altered models with feedback from \(G\) into \(H\) or \(P\).
