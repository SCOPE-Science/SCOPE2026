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
The all-dimensional mathematical proof is in `RESULT.md`.

The critical checks are:
- The exact half-integral vertex lemma implies that for a clique, all and only half-indicator supports of cardinality at least three can appear as fractional vertices; integral vertices are zero or a singleton indicator.
- For a center \(t\mathbf1\), the squared distances to zero, a unit vector, and a half-support indicator of size \(k\) are respectively
  \[
  nt^2,\qquad nt^2+1-2t,\qquad nt^2+k(1/4-t).
  \]
- At \(t=1/n\), the unit-vector-centered simplex ball contains the fractional vertices exactly for integers \(3\le n\le6\).
- At \(t=(n-4)/(4(n-2))\) for integers \(n\ge7\), the unit-vector and full-half distances are equal, and the distances of every smaller half-support layer are strictly less.
- The contact combination weights for \(n\ge7\) are \(a_n=n/(2(n-2)^2)\) on each unit vector and \(b_n=(n^2-8n+8)/(2(n-2)^2)\) on the full-half vertex. Both are positive, sum to one over the contact multiset, and yield the center.
- Weighted squared-distance averaging proves global minimality and uniqueness for arbitrary translated centers.
- Exact algebra gives the integer-to-fractional squared-radius gap and its asymptotic behavior.

`verify.py` independently enumerates the half-indicator vertex types for \(3\le n\le12\), checks all distance and contact formulas, confirms the barycentric weights with rational arithmetic, and solves the full epigraph minimum enclosing ball numerically for \(3\le n\le8\). Finite experiments corroborate the symbolic proof and are not infinite certification or an originality assessment.
