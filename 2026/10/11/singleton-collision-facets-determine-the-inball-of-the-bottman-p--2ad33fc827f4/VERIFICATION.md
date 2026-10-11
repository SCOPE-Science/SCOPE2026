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
- the affine coordinate sum is \(C=\binom n2\binom m2+\binom n2+\binom m2\);
- singleton interval facets have equation \(z_i=1\);
- a mixed facet with horizontal run statistic \(U\) and vertical run statistic \(V\) has offset \(U+V+UV\);
- after translation by \(\mathbf1\), every mixed offset is at most \(F(R,Q)\);
- the full translated mass equals \(F(n-1,m-1)\);
- the normalized density is strictly coordinatewise increasing for positive arguments and equals \(1/2\) on a coordinate axis;
- every nonsingleton facet is therefore strictly farther than the singleton radius;
- summing singleton distance inequalities gives the same radius as a global upper bound and forces the uniform center.

`verify.py` enumerates every horizontal and vertical collision subset for \(3\le m,n\le9\), decomposes them into maximal interval runs, rebuilds the source facet constants, and verifies the exact squared-distance inequalities with rational arithmetic. It does not replace the arbitrary-parameter proof and does not assess originality.
