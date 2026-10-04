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

The verifier reconstructs the affine curve
\[
1+x^2+y^2+z^2=0,
\qquad
1+2x^2+3y^2+4z^2=0
\]
and its embedded tangent bundle using
\[
xu+yv+zw=0,
\qquad
2xu+3yv+4zw=0.
\]

It intersects this surface in \(\mathbf A^6\) with
\[
-2x+y+3z+3u+3v-3w-1=0,
\qquad
-3x+3z+2w=0.
\]
Exact lexicographic Gröbner-basis computation over \(\mathbf Q\) returns leading monomials
\[
x,\ y,\ z,\ u,\ v,\ w^{12}.
\]
The quotient therefore has length \(12\). The univariate eliminant is checked to be squarefree, proving that these are \(12\) distinct complex intersection points.

The script also checks the degree \(4\) and genus \(1\) of a smooth \((2,2)\) complete intersection, computes the general apparent-double-point count
\[
\frac{(4-1)(4-2)}2-1=2,
\]
and verifies that the published secant-corrected upper bound evaluates to \(12\).

The replay output ends in `VERIFY_OK`.
