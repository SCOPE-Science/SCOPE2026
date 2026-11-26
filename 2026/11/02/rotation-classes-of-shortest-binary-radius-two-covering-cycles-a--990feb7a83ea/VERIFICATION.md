---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Coverage is the complete union of the n-bit Hamming balls of radius two about the cyclic windows, including wraparound at L<n. Both frozen C++ listings test this predicate and traverse the stated finite domains; they were inspected, not executed. Independently, from /workspace/branches run python3 audit4.py /workspace/source/2026/11/02/rotation-classes-of-shortest-binary-radius-two-covering-cycles-a--990feb7a83ea (NumPy; replay output audit4.out). The independent search compares every L-bit integer with every cyclic rotation before testing one representative per orbit. It constructs repeated-word windows, checks coverage by removing targets differing at zero, one or two positions, and sums the first-return rotation periods to recover the indexed counts. It matches all 44 length rows and every field of all 14 orbit rows, with zeros for every shorter length. The minima, indexed counts and orbit totals are (10,110,11), (14,28,2), (20,20,1). Full periods also follow from minimality: otherwise the shorter period supplies the same circular windows. The sole order-nine representative is the given 20-bit string; its complement and reverse were tested directly among its rotations. This is exhaustive only for the specified orders, radius and bounded lengths.

## originality

PASS

The supported distinct claim is the complete shortest-cycle census modulo rotation (not the minima or a new order-nine example). The closest available primary table and appendix give the minima and witnesses, and a generic lower bound; they do not give the number of orbits. No exact or dominating census was found in the checked sources. This is a bounded assessment rather than a guarantee of priority.

## value

PASS

For optimal cyclic covering sequences, counting all designs up to rotation is a natural classification beyond minimum length and construction. These are three consecutive benchmark orders from the foundational table, not arbitrary isolated examples. The exact census tells a researcher when another shortest design can be sought, establishes optimal-design rigidity at order nine, and supplies all canonical inputs at the two nearby orders. Its finite scope does not diminish those uses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
