---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Assaf et al. Cor.5.8 identifies connected closed oriented surface components indexed by Lagrangian planes and wedge labels modulo ± and glued only along vertices, with disjoint one-/two-simplices, so top homology is direct sum of signed orientation lines. There are (p+1)(p²+1) Lagrangians and (p-1)/2 labels each. The action is transitive via symplectic basis extension; stabilizer determinant ±1. An integral lift with det ±1 acts on symmetric-square surface orientation with sign det(A)^3=det(A), giving Ind_H^G epsilon. Fixed labels imply determinant ±1 and sign; transvection-fixed Lagrangians are precisely p+1 containing its axis; a ± symplectic split involution fixes (p+1)² mixed lines with sign -1. Cyclic C_p multiplicities follow from character averaging; Frobenius reciprocity kills full invariants. Independently enumerated 40 Lagrangians for p=3 and 156 for p=5 and checked transvection/involution fixed-plane counts and traces. Finite p checks corroborate but do not prove all-prime theorem.

## originality

PASS

The major geometric decomposition and dimensions are already explicit in Assaf et al. (arXiv:2609.14895). The inspected paper treats rank/Betti computations, including a different signed Steinberg module in H¹, but does not compute this signed Sp4-equivariant top-link character, subgroup traces, or invariant multiplicities. Older Igusa boundary ordinary cohomology may encode related representations, yet distinct dual-complex weight-zero summand needs careful comparison. Best-of-knowledge PASS with explicit equivalence-priority risk.

## value

PASS

The equivariant H² character is a structural refinement of a natural tropical Siegel moduli-space invariant, separating orientation-sensitive symplectic involutions and giving complete closed-form transvection restrictions. Negative involution trace distinguishes it sharply from unsigned permutation counts. Not a trivial Betti-number rename.

The dated certificate retains the supplied scientific assessment, sources and limitations.
