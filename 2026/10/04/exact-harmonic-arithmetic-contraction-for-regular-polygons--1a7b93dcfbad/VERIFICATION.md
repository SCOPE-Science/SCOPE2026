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

For odd \(n\), normalize the regular polygon to circumradius \(1\) and put
\[
r=\cos(\pi/n),\qquad c=\cos(\pi/(2n)).
\]
The proof establishes the exact identities
\[
P_n^{\circ}=r^{-1}(-P_n),
\qquad
H_n=rA_n^{\circ}.
\]
The arithmetic symmetrization \(A_n\) is a regular \(2n\)-gon of circumradius \(c\), hence inradius \(c^2\). Its polar therefore has circumradius \(c^{-2}\) and is rotated by half a sector. The harmonic symmetrization has circumradius \(rc^{-2}\). Comparing this with the arithmetic side distance \(c^2\) gives
\[
\beta_n=rc^{-4}
=\frac{4s_n}{(s_n+1)^2}.
\]
Opposite contacts give equality of supporting-strip widths, so translation cannot improve the factor.

The embedded `verify.py` was replayed from its actual package path before packaging. It constructs regular polygons directly from their vertices, forms the arithmetic mean as the convex hull of all half-differences, computes polars from supporting edges, reconstructs the harmonic mean, and evaluates the containment factor from the target halfspaces. It checks every \(3\le n\le51\) and returns:

`VERIFY_OK regular polygon harmonic-arithmetic contraction n=3..51`

For odd \(n\), the replay also checks the predicted \(2n\)-vertex structure and circumradii and reproduces the published reverse factor \((s_n+1)/2\).

The finite replay is not an exhaustive proof for all \(n\); the infinite theorem is supplied by the exact regular-polygon geometry above.
