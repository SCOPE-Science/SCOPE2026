---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Geometric lower bound: if L<min(a+2,5), total horizontal and vertical gaps beside the a-square are each <2; reflections ensure left and bottom gaps <1. Every unit square must be wholly right or wholly above the large square. Each strip has width<2, so two unit projections across short direction overlap and projections along length must be disjoint; each strip holds <=4 units because L<5. With eight units, both assigned strips contain four; the rightmost top-assigned square has left coordinate >=3 and the uppermost right-assigned square has bottom >=3, while both lie in [a,L-1] along constrained axes. Since L<5, their horizontal and vertical unit projections overlap strictly, impossible. Separate L>=a+1 follows because otherwise both total coordinate gaps <1 and no unit square can be disjoint. Explicit three coordinate layouts attain the max/min formula including a=1,3,4. Independently checked 10 rational samples and all 360 pairwise closed-square nonoverlap relations; universal result rests on continuous geometric argument.

## originality

PASS

Recent Badger 7-square formula (2610.22622) and 8-square 23-strategy formula (2610.28504) explicitly have fewer positive squares; not a nine-square exact profile. Classical equal-unit n=9 packing s(9)=3 is only boundary a=1, not a dominating mixed-size theorem. No retrieved stronger two-size nine-square formula; best-of-knowledge originality with meaningful older/uncatalogued two-size packing risk.

## value

PASS

Nine-square two-size slice directly probes the first cardinality not covered by the newly exact arbitrary 8-square theorem. Its a-dependent three-phase optimum, including a constant container-size plateau 3<=a<=4, isolates a sharp eight-unit strip capacity obstruction for a canonical object/invariant instead of arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
