---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the full directed strict refinement relation, the strict successor count is Bell(k)-1 and the strict predecessor count is the product of block Bell numbers minus one. Gluing two partitions at a shared point gives the injective and nonsurjective comparison Bell(p+q-1)>Bell(p)Bell(q) for p,q>=2, so repeated replacement of two nonsingleton sizes by (p+q-1,1) proves the unique maximizing one-nonsingleton size type. Round one identifies these witnesses, their sizes and their relation to the mark. For t<=b, the two pure witness families have round-two counts of one-step coarsenings strictly below the mark differing by (t-1)(b-a); these coarsenings have n-t>=3 blocks so none is accidentally the mark. For t>b the pure side is forced, and when b=1 the possible marked witness is already distinguished. In round three, pure two-point predecessor counts recover both positive mixed sizes using injectivity of binomial(s,2) on positive s; a mixed witness cannot equal a pure predecessor. For any nonwitness, all witnesses supported in a block count as strict predecessors. Their round-four counts give the binomial moments, whose missing low coefficients are k,a,b; translating variables recovers every block-profile multiplicity. The subgroup S_a times S_b is transitive on each profile and color invariance prohibits any further splitting or orbit fusion. Multiset enumeration and the labeled orbit count give the stated coefficient and class-size formulas. Independently generated all coarsenings directly for all 12 asymmetric pairs with a+b<=8, confirmed colors at round four and every class cardinality, including 57 and 97; no finite run is used to prove the round bound or its sharpness.

## originality

PASS

The supported increment is a uniform four-round upper bound for recovering the full ordered intersection profiles of an asymmetric named partition in the strict order. The closest published statements concern the unmarked relation or a different graph. Neither the standard profile counts nor the general logic-to-refinement correspondence is itself novel.

## value

PASS

This is a uniform depth bound independent of the Bell-sized domain for seeing a stabilizer's genuinely finer orbits. The side-orientation and moment-recovery steps explain how the mark changes the observable invariant, not simply the count of a few finite cases. It gives an explicit stopping depth for this natural family even though optimality is open within the record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
