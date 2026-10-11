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

The source definition was checked directly in arXiv:2610.01196v1, Definition 3.3. The source’s hyperbolicity implication was checked against Theorem 4.5, its proof, Corollary 4.6, the finite-dimensional Corollary 4.8, and the surjective-Hilbert Theorem 4.13.

For the explicit witness \(T=\operatorname{diag}(1/2,2)\), let
\[
a_N^2=\frac{4^N-1}{4^N-4^{-N}},\qquad b_N^2=\frac{1-4^{-N}}{4^N-4^{-N}}.
\]
Direct algebra gives
\[
a_N^2+b_N^2=1,
\]
and
\[
4^{-N}a_N^2+4^Nb_N^2=1
\]
for every integer \(N\ge1\). Exact rational replay for \(1\le N\le7\) returned both identities exactly, not approximately.

For the general mixed-hyperbolic statement, the proof uses the source’s standard Riesz spectral splitting and its valid one-sided estimates on the two restrictions. The explicit normalized segment between a stable unit vector and an unstable unit vector is well defined because the spectral subspaces intersect only at zero. The intermediate value theorem then produces, for every sufficiently large time, a unit vector with image norm exactly \(1\). Thus the quantifier failure is exact and does not depend on numerics.

Limits: the complete if-and-only-if classification is asserted only in finite dimension. In general Banach spaces the result classifies the hyperbolic class and does not decide all nonhyperbolic operators. Only arXiv version v1 was inspected.
