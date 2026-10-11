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
- Proposition 3.8 of the primary source gives the exact two affine-sum equations and all bisubset facets.
- The restricted normal of \(x_i=1\) or \(y_i=1\) has norm \(\sqrt{(n-1)/n}\).
- Summing the coordinate-facet radius inequalities gives the claimed upper bound and forces the uniform center at equality.
- For a general bisubset, the projected-normal norm squared is \(Q/(2n)\) and the uniform-center slack is \(Q/4+w/n\).
- For \(w\ge1\), one has \(Q\ge2(n-1)\), and the distance is minimized exactly at \(w=1\), \(Q=2(n-1)\).
- For \(w=0\), one has \(Q\ge4(n-1)\), giving a strictly larger distance for \(n\ge3\).
- For \(n=2\), the four coordinate facets and two complementary-singleton facets give the radius-\(1\) incenter segment exactly.

`verify.py` checks every allowed cardinality pair for \(3\le n\le200\) using exact rational slack and squared-normal data, and separately checks the rank-two center interval. It does not replace the arbitrary-rank proof and does not assess originality.
