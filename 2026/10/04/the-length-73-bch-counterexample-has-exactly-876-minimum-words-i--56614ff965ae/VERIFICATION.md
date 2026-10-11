---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

I independently reran the exact finite-field/signature enumeration encoded by the inspected verifier: no normalized weight-5 support exists; all 62196 triples yield 8760 unordered disjoint equal-signature pairs; every six-support has multiplicity 10; hence there are 876 weight-6 supports. Canonical cyclic shifting gives exactly 12 free orbits of size 73. The BCH bound supplies d>=5, the exhaustive weight-5 exclusion gives d>=6, and the enumerated six-supports give d=6.

## originality

PASS

The recent source determines minimum distances for the BCH family and, according to the frozen package comparison, records the s=3 length-73 case only at minimum-distance level. Exact Resultary and web searches found no independent A6=876 or twelve-orbit statement.

## value

PASS

For an exceptional BCH counterexample singled out by current research, the exact minimum-word multiplicity and cyclic orbit structure are natural coding invariants relevant to error performance and structural classification. The complete finite census is not an arbitrary subset sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
