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

# Reproducibility and logical checks

Run `python verify_area.py` with Python 3, without external packages. The implementation makes only integer comparisons. It explores all four child quadrants of every undecided dyadic square, and exits only after the square has been certified wholly inside, wholly outside, or the fixed terminal resolution has been reached. The terminal unknown area contributes to the upper bound, not to the lower bound; this is an exhaustive enclosure of area rather than discrete point sampling.

For \((n,k)=(3,1),(4,1),(5,1),(5,2),(6,1),(6,2)\) the respective proved area numerators (lower,upper) over denominator \(65536\) are \((126966,129888)\), \((138338,140672)\), \((149516,151682)\), \((125242,128836)\), \((158192,160260)\), and \((126966,129888)\). Every test assertion passed. In addition, inspect the exact polar computation giving \(2\) for each balanced even degree and the exact unit-disk computation giving \(\pi\) for each unmixed multiplicity.

The arithmetic enclosures prove only the listed six cases and those justified separately by reflection and positive integer powers. They are not extrapolated as numerical evidence for uncomputed cases. No independent audit has been performed.
