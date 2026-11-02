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

The Alexander dual of the ordinary 3-cut complex is exactly the complex K_p of subsets whose every triple induces a connected C_{4p}^p graph. Independently reconstructed K_2 with f-cardinalities (8,28,32,10), verified all 20 specified elementary free-face removals, and checked the residual connected closed triangulated surface has f=(8,18,12), circular vertex links and Euler characteristic 2, hence K_2≃S². Rotation by one fixes no nonempty face, giving its degree -1 by Lefschetz. The alternating singleton/(p-1)-vertex 8-block quotients and sections are weak graph homomorphisms; source-edge and section checks were independently verified for 2<=p<=35, while the symbolic distance threshold >p for jumps across 3 blocks proves every p>=2. Relative offsets t=s, t=s-1 and all others respectively give identity, odd rotation and parity-simplex maps, hence deg(Q_s E_t)=δ_{st}-δ_{t,s-1}. Independently computed 338349 complete signed simplicial Lefschetz degrees for all s,t and 2<=p<=100 (including 5049 of each ±1), matching the formula. The principal (p-1)x(p-1) minor is unit triangular, giving a split Z^{p-1} in H_2(K_p;Z), and combinatorial Alexander duality+UCT give a split Z^{p-1} in reduced H_{4p-5}(Δ_3(C_{4p}^p);Z). Since Δ is pure of dimension 4p-4, this nonzero lower homology obstructs shellability. Finite calculations corroborate but do not replace the symbolic all-p proof; p=2 boundary included.

## originality

PASS

Best-of-knowledge comparison of the same critical n=4p ordinary 3-cut cycle-power family with established shellability ranges, prior explicit conjecture, special-case tables and published findings finds no established implication of a uniform integrally split next-to-top rank p-1 summand. The 2024 conjecture would imply stronger exact topology if proved, but is not a theorem. The 2026 proved range is disjoint. Unindexed equivalent proofs remain a residual risk.

## value

PASS

A recent explicit conjecture predicted that the critical n=4p three-cut complexes should be non-shellable and have wedge topology. This theorem settles the non-shellability implication uniformly for the natural infinite family p>=2, with an integral primitive direct-summand mechanism rather than merely finite ranks. The exact splitting is a reusable structural obstruction; it is not just a table recomputation or arbitrary slice. It does not claim the stronger conjectured homotopy type or entire Betti group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
