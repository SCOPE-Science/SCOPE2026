---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A spanning tree's rim path components each contain exactly one selected spoke. Thus each positive-length inter-spoke gap has precisely one rim deletion, including the single-spoke case. A hub triangle with exactly two selected edges provides two distinct swaps and no swap is counted twice, since the insertion determines a unique fundamental cycle. In a gap of length 1 there is one active triangle; for g≥2 exactly two choices of deleted edge activate one triangle and the g−2 others activate two. Marking a spoke gives the factor r/m for labelled wheels, without any periodicity adjustment. Taking the formal logarithm gives the stated polynomial; evaluation and differentiation at z=1 give the Lucas count and the edge count (the derivative reduces to r[x^r](x+x³)/(1−3x+x²)). The minimum is attained only for one spoke with an adjacent deletion, the maximum only for all spokes since every gap of length g>1 contributes less than g, and any nontrivial rim component offers a swap increasing the spoke count. Independently enumerating actual fundamental paths agrees for r=3,…,8 with a coefficient recurrence based on the logarithmic derivative; in particular A_3=6z+9z²+z³ with the rim-only triangle excluded.

## originality

PASS

The known wheel tree count and the use of cyclic gap decompositions are not distinct contributions. The supported distinct claim is the full degree distribution for hub-triangle fundamental exchanges and its exact exchange invariants. The closest checked catalog and primary sources do not give this statistic or imply it without the activity refinement.

## value

PASS

The restriction to triangular fundamental cycles is natural on wheels, whose hub triangles give uniform local supports. The full law measures available local reconfiguration moves at every state, distinguishes bottleneck degrees from average degree, and supplies exact counts useful for analyzing local dynamics. The connectedness proof establishes sufficiency of those supports. This is not justified by the classical total number of states alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
