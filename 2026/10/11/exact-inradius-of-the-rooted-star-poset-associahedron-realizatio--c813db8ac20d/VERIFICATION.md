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
- the rooted-star proper tubes are exactly the root together with a nonempty proper leaf subset;
- Sack's \(\alpha_\tau\) becomes the corresponding leaf-difference subset sum;
- the full-tube equation fixes the root coordinate, so the difference-coordinate map is an isometry on the affine span;
- a \(k\)-leaf subset facet has projected normal norm \(\sqrt{k(n-1-k)/(n-1)}\);
- singleton facets give the global radius upper bound and force the uniform leaf-difference center;
- for every \(k\ge2\), the exact centered facet distance is strictly larger than the singleton distance;
- the closed radius simplifies to
\[
\frac{n^{2n}-(n-1)n^4}{\sqrt{(n-1)(n-2)}}.
\]

`verify.py` checks all subset cardinalities for \(3\le n\le200\) with exact rational comparisons after clearing the common square roots. It does not replace the arbitrary-rank proof and does not assess originality.
