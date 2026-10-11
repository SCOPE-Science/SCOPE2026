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

The scientific check used the normalization \(R=[-A,A]\times[-B,B]\) with \(A\ge B>0\). Every center-passing line was assigned to one of two exhaustive classes according to which pair of opposite sides it meets.

For horizontal-side intersections at \((t,B)\) and \((-t,-B)\), reflection reduces to \(t\ge0\), and a single half contains a boundary pair separated by \(\sqrt{(A+t)^2+4B^2}\). This is minimized only at \(t=0\).

For vertical-side intersections at \((A,s)\) and \((-A,-s)\), reflection reduces to \(s\ge0\), and a half contains a boundary pair separated by \(\sqrt{4A^2+(B+s)^2}\). This is at least \(\sqrt{4A^2+B^2}\), which is at least the first-class optimum because \(A\ge B\). Equality with the global optimum can occur in this class only when \(A=B\) and \(s=0\).

The midpoint cut \(x=0\) yields a half-rectangle of dimensions \(A\) by \(2B\), so its diameter is exactly \(\sqrt{A^2+4B^2}\). Substituting \(A=L/2\) and \(B=H/2\) gives \(\sqrt{H^2+L^2/4}\).

The reduction from arbitrary bisections to a center-passing straight-line minimizer was checked in Cañete--Segura Gomis, arXiv:1803.00321, Proposition 3.1. The earlier equal-area reduction was checked in the 2004 conference version of *On fencing problems*, Theorem 2. No computation beyond these exact algebraic comparisons is needed.

Limit: the verification does not claim uniqueness among arbitrary curved bisections.
