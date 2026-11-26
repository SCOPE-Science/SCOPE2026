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

The 13-by-13 incidence constraints require at least four members on each side. Incidence and pair counts for a four-point blocking set force a full line, whose four disjoint triples of singleton-signature lines would require at least eight selected lines. Duality handles the reverse split. For a five-point blocking set the corresponding counts give a_3+3a_4=3; two distinct three-secants would cover all five points, precluding a third, so a full line is forced. Dually the line side consists of a full pencil and one extra line. The four pairs of lines with a duplicated singleton signature force q to lie off the full line with q≠p, and the extra line must resolve the pair at x=pq∩ℓ. Conversely the line signatures are then separated; on the point side, t singles out one of the two remaining points of each other pencil line, and qx has just one outside point other than q. Different shores have disjoint nonempty signatures. Under a one-vertex exchange the full line and pencil cannot change because two distinct ones would require seven elements in a six-element union; the unchanged side then fixes x. The two independent choices of p and t thus yield a square for each of 13×9×4 triples. An independent affine-plane implementation checked all possible splits through size ten, and reconstructed all swaps by common nine-element subsets, including checking that no cross-shore swap appears. It found exactly the 1,872 states and 468 four-vertex components of degree two.

## originality

PASS

Readable prior statements and the closest Resultary records concern different invariants. Even the matches to 1,872 and 468 count different objects. The minimum and the exchange structure for ordinary locating-total domination were not found in the bounded comparison. No claim of exhaustive priority is made.

## value

PASS

The small natural incidence graph is a clean case where domination and location impose different constraints. The classification converts these constraints into an explicit geometric label and shows that optimal swaps preserve it, revealing severe reconfiguration disconnectivity that the minimum cardinality alone would not detect. The exact exceptional combinatorics provide a useful test case for reconfiguration questions on other incidence graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
