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

The classification proof fixes a code edge by translation and uses the incompatibility of overlapping open neighbourhoods to force its remaining antipodal edge. The antipodal quotient and full edge-to-code correspondence then give the distance and partition formulas without unproved computational assumptions.

Reproducible finite checks (Python standard library):

```
python direct_certificate.py
python quotient_certificate.py
```

Expected passing lines:

```
DIRECT_Q4_OPEN_NEIGHBORHOOD_PASS 16 48 Counter({4: 72, 2: 48})
ANTIPODAL_QUOTIENT_K44_PASS 8 16 Counter({'distance_two': 72, 'adjacent': 48})
```

The first program exhaustively checks all \(\binom{16}{4}=1820\) possible four-vertex subsets, every legal pair of codes, each source's shortest-path distances and every four-code partition. The second uses quotient-graph algebra, rather than the first program's code enumeration, to reconstruct the structure and perfect-matchings census. Both were run successfully. Neither is an external, independent scholarly audit. The claim applies only to \(Q_4\); historical originality comparisons remain subject to inaccessible literature, notably the full Kwon–Lee (2014) article.
