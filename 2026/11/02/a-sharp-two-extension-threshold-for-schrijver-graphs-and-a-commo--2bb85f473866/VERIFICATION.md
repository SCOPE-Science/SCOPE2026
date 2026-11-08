---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For 2r<=n<=4r−2, alternating disjoint stable r-sets A,B have no common neighbor because their complement is a path of n−2r ground-cycle vertices with independence number <=r−1. For n>=4r−1, every proper ground-cycle subset induces paths and has independence number >=ceil(size/2); the explicit constructions in RESULT.md produce disjoint-to-both, mixed and meeting-both stable r-sets distinct from anchors, including r=2 edge cases. Three-pebble back-and-forth uses 2-e.c. to preserve two-anchor adjacency and equality forever, hence unrestricted-depth counting-free FO3 equivalence to Rado. Schrijver chromatic theorem gives 2r+1 at n=4r−1. Independent full-pair four-pattern enumerations verified the predicted cutoff for r=2,n=4..10 and r=3,n=6..14, but finite enumeration is corroboration only.

## originality

PASS

Best-of-knowledge originality for the precise final theorem only, with known component results explicitly excluded from novelty and named inaccessible-source risks; relevant indexed findings and primary literature were compared by implication.

## value

PASS

An exact sharp local extension threshold for an important chromatic-extremal graph family is a natural infinite classification. The consequence that unbounded chromatic number coexists with the fixed unrestricted-quantifier-depth three-variable theory of the Rado graph is a substantive finite-model-theoretic interaction, not a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
