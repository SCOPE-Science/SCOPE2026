---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The package contains the standalone standard-library Python program `verify.py` and the complete 34-pattern certificate `PATTERNS.tsv` in the same directory. Run `python3 verify.py` from that directory. It generates all 52 partitions of five labels, checks all 2,704 ordered pairs and 1,153 admissible row/column partition pairs, obtains 34 nonisomorphic patterns, and validates the certificate line by line.

For each pattern it checks the distance-equalizer condition through complementary five-bit signatures in compressed representative grids. The reduction is exact for all board sizes at least five: a possible violating pair uses at most two unused row coordinates and at most two unused column coordinates. Thus the nine pairs of side lengths in the set \(\{5,6,7\}\times\{5,6,7\}\) exhaust every distinct possibility for this five-cell problem, not merely selected small samples. The program asserts the full nine-type classification and computes the row/column-preserving automorphism sizes by explicit permutations, obtaining the closed formula.

A separate routine reconstructs the rook-graph distance condition directly and checks every five-element subset for the boards \(5\times5\), \(5\times6\), and \(6\times6\). The resulting counts are 8430, 17076 and 36720. Additional exact orbit-formula evaluations give 31087 for \(5\times7\) and 152145 for \(7\times7\). The established lower bound of five landmarks is taken from the cited 2026 primary paper; the novel classification proof concerns every five-cell set.

The certificate has 34 distinct rows with the canonical masks, occupancy dimensions, automorphism orders, board-dependent validity flags, and an explicit failing exterior pair for each pattern failing at \(5\times5\). All tests use exact integer operations. No random sampling, numerical tolerance, or external package is required.

Independent audit: not performed. The finite certificate is an exact computation supported by a mathematical reduction, not an independent formal proof checker or an external certification.
