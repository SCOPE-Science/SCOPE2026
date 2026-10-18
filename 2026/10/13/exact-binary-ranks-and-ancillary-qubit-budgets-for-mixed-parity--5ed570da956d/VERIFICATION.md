---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For d≥2, q_i≥2 and both parity classes represented, A over F₂ of the Cartesian product of loopless complete graphs equals (d mod 2)I+Σ J_i. For odd q_i, J_i is projector; parity sectors contribute multiplicity (P+(-1)^d R)/2. For even q_i, J_i²=0 and rank one, their tensor sum D has D²=0, and each rank-two Jordan factor is contractible; only tensor product of (q_i−2)-dimensional trivial homology components survives, dimension H, yielding dim ker D=(Q+H)/2. Product formula dim ker A=(Q+H)(P+(-1)^dR)/4 follows. Direct GF₂ Gaussian elimination for 210 mixed-parity tuples with q_i∈2..5 and d∈2..4, N≤160, agrees with formula; not an infinite proof. For fully oriented edges, B+Bᵀ=A and Riera–Parker–Stănică Lemma4.1 gives e=rank(A)/2, independent orientation. Connected graph alternating binary adjacency rank even; denominator integral even at q_even=2.

## originality

PASS

Riera–Parker–Stănică already proves the general half-commutator-rank to ancilla identity. Fish–Key–Mwambene already determines homogeneous Hamming adjacency binary rank. This work evaluates heterogeneous mixed-parity Cartesian complete-graph products by an even-Jordan-factor homology calculation, not implied by homogeneous q. Closely related Fish–Key–Mwambene 2023 Cartesian product code paper available in excerpt, incomplete full text; no general exact theorem found. General modular Kronecker-sum algebra could encode equivalent formulas, retained as important risk.

## value

PASS

Closed uniform binary rank for heterogeneous Hamming boxes is a natural graph-code invariant beyond known homogeneous case and gives precise orientation-independent minimal stabilizer ancilla budget for every fully directed realization. Nonstandard odd/even tensor-complex argument handles q_even=2 and arbitrarily many coordinates; this is a reusable structural result rather than mere substitution into a quantum formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
