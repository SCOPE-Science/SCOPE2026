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

Fresh exhaustive enumeration of every two- and three-pair profile and every perfect matching independently reproduces the stated relation counts and stable-count marginal. For the 144 disjoint profiles, a separate canonicalization under independent relabelings of men and women together with side exchange yields exactly two equivalence classes, each containing 72 labeled profiles. Every disjoint profile has two stable matchings realizing the opposite objective pairs (2,3) and (3,2), consistent with the claimed conflict geometry.

## originality

PASS

The defining literature puts minimum regret and sex-equality in the same exact optimization framework, but it does not classify their joint optimum sets on the smallest markets. The closest complete small-instance paper does not tabulate either this pair of criteria or the two disjoint symmetry classes. Independent exhaustive replay confirms both the relation census and the two size-72 orbits.

## value

PASS

Minimum regret protects the worst-off participant while sex-equality balances aggregate dissatisfaction across sides. Their first incompatible market size is a natural fairness boundary; the full census and orbit decomposition explain all first conflicts rather than selecting an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
