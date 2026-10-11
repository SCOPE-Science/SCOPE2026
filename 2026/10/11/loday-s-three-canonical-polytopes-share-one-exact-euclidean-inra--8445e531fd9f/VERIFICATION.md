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
The theorem is proved symbolically in `RESULT.md`; finite checks are corroborative only.

Verified source premises:
- The three polytopes lie in the affine hyperplane \(\sum_i x_i=\binom{n+1}{2}\).
- The permutahedron uses all nonempty proper subset inequalities.
- Loday's associahedron retains exactly the interval inequalities.
- Loday's parallelepiped retains the prefix and suffix inequalities.
- The cited survey records that their vertex barycenters coincide.

Verified mathematical steps:
- Projection of a \(k\)-set indicator to the tangent space \(\mathbf1^\perp\) has squared norm \(k(n-k)/n\).
- At the common barycenter, the facet slack is \(k(n-k)/2\), so the distance is \(\frac12\sqrt{nk(n-k)}\).
- This quantity is minimized exactly at \(k=1\) or \(k=n-1\).
- Summing all singleton distance constraints gives the sharp upper bound and unique center for the permutahedron and associahedron.
- The endpoint parallel-facet pair gives the same sharp upper bound for the parallelepiped.
- Prefix sums are affine coordinates on the hyperplane, so the parallelepiped incenter locus is exactly the product of the intervals displayed in the finding.

`verify.py` checks these identities and the dimension/contact counts for \(2\le n\le30\).
