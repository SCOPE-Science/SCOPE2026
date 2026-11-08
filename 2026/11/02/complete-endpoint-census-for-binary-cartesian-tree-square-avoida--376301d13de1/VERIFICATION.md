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

Prefix-closure gives an exhaustive recurrence: a new forbidden Cartesian-tree-equivalent adjacent pair must end at the appended bit. Literal leftmost-minimum ordered Cartesian tree recursion precisely implements the predicate, and a separate parent-distance equality test checks it using a different representation. An independent fresh complete breadth-first enumeration of all valid binary prefixes through n=30 gives |F_26..30|=156,107,56,20,0; the 20 distinct endpoints share mask 110--11010--1101010--110101-- and have ordered-list SHA256 fa7a68bf7155a80ca632847616541706160392ee2d4492e90c3310f1787da79a. The explicit eight-pattern partition accounts for all 20. F30 empty and prefix closure exclude all larger lengths; computational proof is exact finite enumeration, not random sampling.

## originality

PASS

PASS, substantial historical-priority risk: maximum length 29 and Cartesian-tree equivalence are prior, while the complete count and fixed-coordinate endpoint classification are not implied by inspected statements; most relevant 2026 primary full text inaccessible despite lawful attempts, so no whole-document noncoverage claim.

## value

PASS

The full set of extremizers at an independently known natural sharp avoidability cutoff is motivated endpoint data, revealing 21 fixed positions and exact nonuniqueness of 20 words. This is a meaningful finite classification without pretending to solve larger alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
