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
The all-parameter proof is given in `RESULT.md`.

Critical checks:
- the polytope is
  \[
  I_{r,n}=\{x\in[0,1]^n:\sum_i x_i\le r\};
  \]
- every lower coordinate facet gives clearance \(c_i\);
- for \(r\ge2\), every upper coordinate facet gives clearance \(1-c_i\);
- the rank facet gives clearance
  \[
  \frac{r-\sum_i c_i}{\sqrt n};
  \]
- summing the lower-facet clearances and the rank-facet clearance yields the global inradius bound
  \[
  \rho\le\frac{r}{n+\sqrt n};
  \]
- opposite coordinate facets yield the global bound
  \[
  \rho\le\frac12;
  \]
- the displayed incenter reaches the smaller of these two bounds;
- a vertex of cardinality \(k\) has squared distance from \(t\mathbf1\)
  \[
  nt^2+k(1-2t);
  \]
- minimizing the maximum over \(0\le k\le r\) gives the outer threshold \(2r=n\).

`verify.py` checks every pair \(2\le n\le40\), \(1\le r<n\). It solves the full inradius linear program from the complete facet system, verifies every tangency phase, evaluates all Hamming-weight vertex layers, and independently minimizes the exact scalar outer objective. Finite computation is corroborative only and does not assess originality.
