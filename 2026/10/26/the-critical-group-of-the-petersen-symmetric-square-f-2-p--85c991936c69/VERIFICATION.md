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

The graph is exactly F_2(KG(5,2)): unordered pairs of distinct Kneser vertices joined by one legal token move. It has 45 configurations, 15 degree-4 and 30 degree-6 vertices, hence 120 edges. Deleting the last Laplacian row/column gives a concrete 44-by-44 integral matrix. Independently constructed the graph, computed its exact determinant 49253533675382566432014336000, and independently reduced that entire matrix over each prime-power ring for p=2,3,5,7,19. Local valuations were p2: 0^28,1^8,2^4,5^4; p3: 0^39,1^1,2^4; p5: 0^41,1^3; p7: 0^38,1^6; p19: 0^39,1^5. These align into the claimed invariant factors, their product equals the determinant, and the supplied full characteristic-polynomial computation is supported by the exact verifier source. The Smith reductions are exhaustive finite exact matrix calculations, not extrapolations. A separate conceptual derivation of each p-primary summand is not claimed.

## originality

PASS

The inspected token-graph literature supplies graph/spectral constructions and the inspected Kneser critical-group results describe the 10-vertex base KG(5,2), not the 45-vertex F_2(P). No actual matching Smith table or stronger theorem yielding these factors was identified. Published related Resultary records concern two-particle configuration homology or other Petersen complexes, not the critical group. This is a qualified best-of-knowledge conclusion, not priority certification.

## value

PASS

The two-token symmetric square of the Petersen graph is a canonical configuration graph with nontrivial irregularity; its sandpile group governs recurrent chip-firing classes. The exact noncyclic abelian group is a natural integral invariant not fixed by a Laplacian spectrum or spanning-tree number. A 44-dimensional fully reproducible integer Smith computation adds meaningful arithmetic information, although it proves no all-graph family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
