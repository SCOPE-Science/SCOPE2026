---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Used natural reduced Swiatkowski chain model: at weight 4, degree-2 group U⊗U⊗Sym²(E) and two degree-one multiplication components U⊗Sym³(E), no degree-3 boundaries; U=ker(Q^k->Q). Decompose E=Q t⊕U. t² sector kernel zero, tU sector pair-symmetrization kernel Λ³U, pure Sym²U sector flip-split gives ker in Sym²U⊗Sym²U = Schur_(2,2)U and ker in Λ²U⊗Sym²U = Schur_(2,1,1)U by Littlewood–Richardson and nonzero multiplication on target Schur_(4) and Schur_(3,1). Pole swap exchanges the two local degree-one generators, hence action is -factor-flip: even Λ³U plus Schur_(2,1,1)U, odd Schur_(2,2)U. Edge variable stabilization from weight-three Λ³U realizes full even sector by Pieri; the odd subspace cannot be stabilized. Independently built exact reduced-complex boundary matrices and modular Gaussian ranks over 1000003 for k=3..6; even/odd dimensions (0,1),(4,6),(19,20),(55,50) match hook-content formulas. These finite-field checks corroborate, do not establish infinite-characteristic-zero theorem; algebraic kernel proof does. Exact Git source tree, RESULT and verification material inspected.

## originality

PASS

Best-of-knowledge, statement-and-implication comparison: inspected same-object primary results and relevant published records; literature access limits documented. Exact pole-odd summand is nonstabilized; earlier generator model is a method, not a theorem implying full decomposed module.

## value

PASS

Full symmetry-sensitive classification of a natural family of graph-braid configuration homology at fixed four particles; detects pole-odd module invisible to three-particle theta-class stabilization. Sharp distinction between geometric generators and new four-particle classes answers a motivated structure question, beyond mere rank recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
