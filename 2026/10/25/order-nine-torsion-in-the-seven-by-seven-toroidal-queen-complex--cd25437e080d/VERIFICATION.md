---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For toroidal queens on F_7^2, nonattacking displacements are exactly nonzero (dx,dy) with dx,dy,dx±dy all nonzero. The invertible linear map (x,y)->(2x+3y)+(2x+y)omega with omega^2=3 identifies this legal-placement graph with Paley(49): the square norm condition equals nonattack. Exhaustively generate each clique/face once, giving f=(49,588,2156,2450,882,196,28), total 6349. A specified greedy order on 49 vertices pairs 3093 face inclusions; direct Hasse acyclicity check on 23226 incidences leaves critical cells 1 zero-, 21 two-, 141 three-dimensional. Exact signed Morse boundary 21×141 has 1055 nonzero entries. An independent integral Smith normal form gives 20 unit invariant factors and one 9, so reduced H2=Z/9, H3=Z^120 and all other groups vanish. This is a complete finite exhaustive mathematical certificate, not an infinite-family theorem. Independent check: Independently reconstructed all 6349 faces from the 49-board attack relation, the specified discrete Morse pairing, exhaustive directed Hasse DAG, and the signed Morse boundary via a separately written implementation. An independent SymPy exact-integer Smith normal form gave [1]*20+[9], confirming odd order-nine torsion; pairwise Paley correspondence was also verified in supplied package. Thus this run checked the crucial integer certificate, not only a log or mod-two ranks.

## originality

PASS

The Paley49 clique-complex alias was directly included in searches. Baker et al. classify certain maximal cliques in Paley square-order graphs; Cairns classifies toroidal queen placement feasibility. Neither a maximal clique classification nor a maximum number of queens determines the full oriented boundary matrix or its order-nine Smith factor. Paley17/29 computations are for different graphs and homology types. Priority remains qualified against unindexed clique-complex homology tables.

## value

PASS

This is a precise integral homology invariant for a natural toroidal-board/Paley graph complex; Z/9 is genuinely stronger than a mod-three Betti anomaly and invisible in Q and mod-two homology. A full small classical-object computation with certified prime-power torsion is a reusable benchmark for topological graph methods, even without a family-wide theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
