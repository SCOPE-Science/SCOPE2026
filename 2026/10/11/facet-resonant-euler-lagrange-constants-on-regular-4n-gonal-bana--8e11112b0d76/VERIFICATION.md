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
The global upper bound is analytic. For the inradius-one regular \(N\)-gon with \(N=4n\),
\[
\|z\|_N\le\|z\|_2\le R\|z\|_N,
\qquad
R=\sec\!\left(\frac{\pi}{N}\right).
\]
The Euclidean coefficient transform satisfies
\[
\|\lambda x+\mu y\|_2^2+\|\mu x-\lambda y\|_2^2
=
(\lambda^2+\mu^2)(\|x\|_2^2+\|y\|_2^2),
\]
so
\[
L_{\mathrm{YJ}}(\lambda,\mu,X_N)\le R^2.
\]

For the balanced ratio, adjacent vertices symmetric about one facet normal have sum and difference on perpendicular facet-normal rays.

For the unbalanced resonances, put
\[
\alpha=\frac{\pi}{N},
\qquad
\phi=(2k+1)\alpha,
\qquad
(\lambda,\mu)=(\cos\phi,\sin\phi).
\]
A vertex and its quarter-turn are sent to directions
\[
2(k+1)\alpha
\quad\text{and}\quad
2(k+1-n)\alpha,
\]
which are both facet-normal directions. Each transformed vector has Euclidean and polygonal norm \(R\), giving equality.

`verify.py` reconstructs representative polygon norms and checks all stated resonance configurations for \(1\le n\le30\), including the octagonal and dodecagonal closed forms. These finite checks are reproducibility aids only and are not used to justify the infinite quantifiers.

No independent audit or independent validation has been performed.
