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

# Complete finite checks

Both checkers are standalone Python 3 standard-library scripts and were executed from their actual packaged paths:

```
python3 verify_coordinates.py > verification_coordinates.txt
python3 verify_arcs.py > verification_arcs.txt
```

Both output files are byte-for-byte equal and end in `VERIFY_OK`. The first program enumerates all \(3^9\) colour words, generates the twelve affine lines from \(\mathbb F_3^2\) direction vectors, and calculates all permissible point recolourings. The second independently enumerates every possible line-free bit mask, partitions points into three ordered arcs using a separately specified list of twelve triples, and derives transitions by moving a point between colour-class masks.

Each algorithm rebuilds the graph and breadth-first-searches from **each** of its \(3762\) vertices, giving full exact radius, diameter and connectivity rather than sampling. Both reconstruct the same canonically ordered vertex and edge sets, with SHA-256 digests `931e08d1d6167e59e0246e3747fbe8e4527e217a5aae4c5d898c742425bb1234` and `fda7d2573c23bb1a48c821fb4228c254fbd6fa5575728e8b1d5c7b33128d1ff9`. The reproduced counts are \(3762\) vertices, \(16848\) edges, degree counts \(162\) of eight and \(3600\) of nine, eccentricity counts \(3456\) of nine and \(306\) of ten, and radius nine/diameter ten.

The certificate does not establish any comparable result for larger affine planes and does not constitute an external independent scientific audit. The constructive pair of witnesses at distance ten is recorded in `RESULT.md`; shortest-distance nonexistence follows from the exhaustive breadth-first distance arrays, not merely the exhibited ten-move path.
