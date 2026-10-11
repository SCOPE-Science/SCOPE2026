---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

If every occupied image level contains at least two points, comparability forces each such target level to receive points from exactly one source level and every source level to occur; with equal source and target heights, monotonicity makes this assignment the identity, so the map is level-preserving and nonconstant on every level. Otherwise the image weak order has a singleton occupied level and its order complex is a cone, so the map factors through a contractible image and is null-homotopic. A levelwise nonconstant map acts nontrivially on top rational homology. Any pointwise-comparable map has the same action, hence is also levelwise nonconstant and level-preserving; comparability inside an antichain then forces equality. Fresh enumeration of the (2,2,2) case independently gives 446 maps and exactly nine components, one of size 438 and eight singletons.

## originality

PASS

Published nearby results determine the top-homology test, unequal-source/target same-height maps, and the height-two self-map case, but none implies the h-at-least-three self-map null-component theorem. The audited image lemma adds the missing implication from failure of levelwise nonconstancy to a contractible image, and this plus homology rigidity yields the full self-homotopy set.

## value

PASS

The result gives the complete self-homotopy monoid-set cardinality and component structure for a standard finite-pseudosphere family, strengthening the previously available top-homology test to an exact homotopy classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
