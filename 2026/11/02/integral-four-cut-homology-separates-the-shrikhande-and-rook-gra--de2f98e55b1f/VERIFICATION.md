---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Reconstructed graph definitions (Shrikhande Cayley steps and rook equal-coordinate adjacency), ordinary disconnected-four-set facets and dual L=all subsets whose four-subsets are connected. Independent full 2^16-mask enumeration verifies dual f-vectors S (16,120,560,668,288,0) and rook (16,120,560,620,288,48), with connected 4-set counts 668/620 and mod-2 homology dual degrees S (65,2,12), rook (96,21). The actual evidence/verify.py source constructs acyclic Morse matchings, checks every oriented Hasse incidence, signed gradient-path Morse boundaries and integral unimodular unit-pivot reductions (nonzero ranks 4,6 for S and zero for rook); these are needed to exclude torsion, which independent mod-2 checks alone cannot do. Integral Alexander duality on 16 vertices shifts L^cohomology degree 13-i and UCT applies as integral groups are free. Nonzero lower-dimensional homology obstructs shellability of pure 11-complexes. This is a complete finite graph calculation, not an assertion about all strongly regular graphs.

## originality

PASS

The two primary cut-complex papers establish the general definition and other graph families, not these ordinary four-cut integral groups. The earlier SCOPE result is the rook THREE-cut homology and does not imply the four-cut calculation. An exact 16-vertex additive homology classification is provisionally original, not a claim that these two graphs were otherwise indistinguishable.

## value

PASS

Exact torsion-sensitive homology of two canonical strongly regular parameter twins is a natural finite but complete topological invariant. The degree-nine Shrikhande class distinguishes the four-cut constructions despite equal reduced Euler characteristic; confirms nonshellability and reveals graded structure rather than a routine sampled statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
