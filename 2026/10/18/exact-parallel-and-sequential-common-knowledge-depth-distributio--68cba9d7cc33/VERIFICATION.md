---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For two distinguished S5 partitions with cells of size <=2, represent nontrivial equivalence classes as two partial matchings. Their union decomposes uniquely into singleton vertices, alternating r-paths and doubled/even 2j-cycles. Event-uniform E^d reaches precisely graph-distance d balls, yielding component depths r-1 and j. The ordered relation K_R K_S has directed reachability increments R then S, giving diameter ceil(r/2) on paths and ceil(j/2) on 2j-cycles (including doubled 2-cycle). Taking P equal to the complement of a not-yet-reached vertex proves necessity for all events. Labeled component counts are 1, r!, (2j-1)! and exponential formula with the corresponding cutoffs yields both cumulative EGFs; differences yield exact histograms. Spanning paths give n! maximal parallel frames for n>=3; perfect-matchings-only case deletes paths/singletons. Independent literal enumeration of all ordered involution pairs n=1..6 reproduced all cumulative coefficients and both depth distributions, including n=6 parallel (1,855,1920,1560,720,720) and sequential (1,1215,3120,1440). Original verify.py source inspected; finite enumeration corroborates, does not replace component proof.

## originality

PASS

Lugo's explicit 2009 component EGF already supplies the colored-involution combinatorial species and all component weights; Aumann/Barwise and Humml–Schröder supply known common-knowledge reachability. These ingredients are credited. The remaining claim joins two particular uniform modal-iteration diameters to component-size cutoffs and derives separate exact distributions; the two histograms do not appear as results of the inspected prior theorem, although they are relatively accessible deductions once the new modal cutoffs are recognized. Best-of-knowledge not priority certification.

## value

PASS

Depth to common-knowledge stabilization is a natural exact event-uniform modal invariant. The distinction between simultaneous E and ordered sequential K_R K_S exposes genuine directional distance asymmetry. Full all-n labeled histograms, extremal frames and fixed-point-free subfamily can be used as finite epistemic-model benchmarks; more than a random single instance, while the classical matching decomposition itself is not new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
