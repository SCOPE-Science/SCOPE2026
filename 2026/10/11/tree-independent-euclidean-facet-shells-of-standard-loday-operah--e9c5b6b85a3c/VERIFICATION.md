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
The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative only.

Critical checks:
- a tree in \(\mathrm{PT}_n\) has \(n-1\) internal edges;
- a connected \(s\)-edge nest has \(s+1\) induced internal vertices;
- the standard-weight affine total is \(\binom n2\);
- the corresponding facet height is \(\binom{s+1}{2}\);
- the intrinsic projected normal has squared norm \(s(n-1-s)/(n-1)\);
- the exact center-to-facet distance is \(\frac12\sqrt{(n-1)s(n-1-s)}\);
- its minimum is attained exactly at \(s=1\) or \(s=n-2\);
- singleton facets yield the same radius as a universal upper bound and force the uniform center at equality.

`verify.py` checks the closed formula for \(3\le n\le200\). It also enumerates all labeled trees through \(n=6\), every nonempty proper connected edge subset, and verifies the source support constant, exact squared distance, and tangent-cardinality classification. It does not replace the arbitrary-rank proof and does not assess originality.
