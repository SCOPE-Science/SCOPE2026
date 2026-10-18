---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. Independently reconstructed the 15 vertices, 45 edges and 30 triangles directly from Datta–Upadhyay Example 7 with m=2,n=3. Every edge lies in two triangles. The 30 mod-two triangle equations have rank29, hence dim Z1=16; the 15 vertex stars have rank14, giving dim H1=2. Enumerated all 2^16=65,536 cocycles, exactly 4 classes of 2^14 representatives. The three nonzero class minima/counts are (5,1),(5,1),(10,1), not sampled. Alexander–Whitney cup squares of unique minima are respectively 1,1,0, invariant under coboundary; Wu identity <w1∪x,[K]>=<x²,[K]> uniquely identifies the weight10 class as w1. The two weight5 representatives have disjoint edge supports, their XOR is the unique weight10 representative, and both support simple 5-cycles on exactly the two Datta–Upadhyay exceptional 5-vertex carriers. Recomputed via independent bitset kernel/coboundary implementation /mnt/data/scope08_independent_20261015.py, not source logs.

## originality

PASS

PASS. Exact source Datta–Upadhyay Example 7 constructs Q5,3 and explicitly lists the two exceptional blocks for a local regularity test, but does not compute mod-two simplicial cohomology minima, minimizer uniqueness, cup-square strata, or w1. The new statement connects these known carriers to a specific intrinsic cohomological optimization problem; the original blocks alone cannot imply uniqueness over 65,536 cocycles. Searches for Q5,3/Klein bottle cosystolic/cup square aliases and related indexed records found other triangulations, not stronger coverage.

## value

PASS

PASS. On a natural degree-regular 15-vertex Klein-bottle triangulation, the complete cosystolic spectrum and cup-square stratification identify geometrically distinguished nonorientability carriers and w1 uniquely. This is a motivated exact natural invariant of a specific nontrivial simplicial complex, not a generic small finite enumeration; the 5+5=10 decomposition is structural. No general family formula is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
