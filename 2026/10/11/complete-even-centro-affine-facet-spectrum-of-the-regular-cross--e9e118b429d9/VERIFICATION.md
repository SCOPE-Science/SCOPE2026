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

For the standard cross-polytope, the proof checks the following exact identities:
\[
\mathcal H^{n-1}(F)=\frac{\sqrt n}{(n-1)!},
\qquad
m=\frac1{(n-1)!},
\]
\[
\mathcal H^{n-2}(R)=\frac{\sqrt{n-1}}{(n-2)!},
\qquad
\sin\theta=\frac{2\sqrt{n-1}}n,
\qquad
c=\frac1{2(n-2)!},
\]
and therefore
\[
\frac cm=\frac{n-1}{2}.
\]

The facet graph is the Boolean cube. For every Walsh character of degree \(k\), exactly \(k\) coordinate flips reverse its sign, so the ordinary graph Laplacian eigenvalue is \(2k\). Multiplication by \(c/m\) gives the generalized eigenvalue \((n-1)k\). Antipodal inversion multiplies a degree-\(k\) Walsh character by \((-1)^k\), so the even space consists exactly of the even levels.

The bundled checker reconstructs this operator for \(2\le n\le8\) using exact rational arithmetic and verifies every Walsh eigen-equation, parity condition, and multiplicity. This finite replay is a consistency test; the all-dimensional proof is the symbolic argument above.

No claim is made about local minimality of the cross-polytope or spectra of arbitrary simplicial polytopes.
