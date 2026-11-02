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

# Reproducible checks

Run `python3 verify_geodesic_edges.py` in the extracted package directory with Python 3.9 or later. Only Python's standard library is used.

The program separately computes canonical-edge membership traces using explicit permutations and a dynamic program whose state is the set of already-used coordinates plus the accumulated queried-edge mask. It compares the outputs for dimensions \(1\) through \(9\), exhaustively evaluates every canonical query support against the forbidden-pattern characterization for dimensions \(1\) through \(12\), and checks the exact VC formula. It also builds complete adaptive depth-\(d-1\) query trees for dimensions \(1\) through \(11\) and verifies the query answers and uniqueness of the terminal path witnesses.

Observed terminal marker:

```
ALL_ANTIPODAL_GEODESIC_EDGE_SHATTERING_CHECKS_PASS
```

The recorded run included an explicit adaptive tree with \(1024\) leaves in dimension \(11\). These are finite reproducibility checks. The proof of the theorem for all dimensions is in `RESULT.md`; a finite computation alone would not establish it. The publication-priority comparison remains incomplete and no independent scientific audit has been performed.
