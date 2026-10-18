---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Every code vertex lies in exactly four closed neighborhoods; among 24 distinct nonempty closed-neighborhood signatures at most k are singleton, so 4k>=k+2(24-k), i.e. k>=10. Independent C++ direct signature enumeration of all C(24,10)=1,961,256 and C(24,11)=2,496,144 candidates gives zero size-ten codes and exactly 384 size-eleven codes; monotonicity eliminates sizes below 10. Independent NetworkX construction from the LCF sequence and exact isomorphism enumeration gives 32 graph automorphisms, all checked as bijections preserving incidences; orbit partition of all 384 codes gives 13 disjoint orbits of sizes 16 twice and 32 eleven times and reproduces all 13 listed representatives. This exhausts the only finite candidate layers needed for minimum, rather than sampling.

## originality

PASS

The original graph order/girth, symmetry group and stronger identifying-code existence literature are antecedents. None of the compared statements provides both the exact minimum ordinary identifying-code multiplicity 384 and full 13-orbit representative classification, although the 2008 directly relevant titled Laihonen paper could not be inspected beyond available abstract.

## value

PASS

The McGee graph is the canonical extremal cubic (3,7)-cage; identifying codes are a natural sensor/location-discrimination invariant. The exact minimum, full 384 optimum multiplicity and 13 symmetry classes provide an independently usable complete classification of optimal configurations and distinguish multiple geometry types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
