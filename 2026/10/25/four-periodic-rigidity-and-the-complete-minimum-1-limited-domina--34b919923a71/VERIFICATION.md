---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For n>=3 the 2n-vertex Möbius ladder is cubic. Double-count D-to-complement edges to get |D|>=n. With rung counts x zero, y singleton, z full, |D|=n+z-x. The three-neighbor local rules exclude mixed zero and singleton blocks when |D|<=n+1; the remaining singleton/full case forces one full rung and yields 2n configurations, while zero/full cyclic run lengths 1..2 for zeros and >=2 for fulls force 0033 periodicity or a unique defect. These give gamma=n for n divisible by 4 and gamma=n+1 otherwise, with exact counts 4,2n,3n. Independent direct labeled-vertex exhaustive enumeration for all n=3..9 reproduces 9,4,15,12,21,4,27 minima. The finite enumeration cannot prove the unbounded classification.

## originality

PASS

A complete structural optimizer classification on the twisted Möbius ladder and exact labeled minima count survives comparison with general half-order matching-cut bounds and other cubic graph families. Graph is not the Cartesian prism. Recent cubic 1-limited domination work reports Goldberg, Blanuša and flower snark applications, not the inspected Möbius family. Historical priority remains qualified for unindexed cubic circulant literature.

## value

PASS

The exact minimum and every labeled optimizer of a natural infinite family of cubic graphs are determined by a surprising modulus-four defect; this is motivated by sharp limited domination and extremal matching cuts, not a reparameterized general bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
