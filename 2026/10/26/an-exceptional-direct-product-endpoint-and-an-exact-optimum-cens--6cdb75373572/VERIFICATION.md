---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Independently enumerated all 3^(rs) {0,1,2}-labelings with adjacency and all three defining conditions directly for (r,s)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4). Returned (minimum,count)=(4,1),(6,25),(7,24),(8,40),(8,108),(10,96), respectively. Full proof: independent zero sets must be rows/columns (or matched two-point pair at r=2), weight=rs−|Z|+|T|; a complete zero row cannot be defended by one 2; for r≥3 only (s−1,1) and (s,2) attain optimal weight, and defenders in different columns plus total-positive condition enumerate both. On K2×Kn one-sided zeros require two positive vertices, while matched cross-zero pairs contribute only at n=3; resulting all-weight crown formula follows by disjoint zero-set partition. The exact finite enumeration is corroboration, universal proof is combinatorial.

## originality

PASS

PASS: 2022 source Theorem 3.5 actually states s(r−1)+2 for all 2≤r≤s; its r=2 witness leaves all positive vertices in one independent row and thus violates total-positive axiom. Earlier 2019 C6 value=6 is explicitly credited. Corrected infinite r=2 scalar, entire optimizer census and complete crown polynomial are not implied by the old scalar; distinct Roman variants use different axioms.

## value

PASS

PASS: Repairs an incorrect infinite boundary family in an established published theorem and supplies all minimizing configurations plus an entire crown all-weight generating function. These are natural structural/extremal invariants that a researcher using the published scalar needs, not a tiny gain or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
