---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Weighted edge-difference coordinates give an isometric identification of the little max-norm space with c_0(T) and of the sum-norm space with C direct-sum_1 c_0(T*). Conjugating M_psi produces an explicit row supported on the root, the ancestor chain and the current coordinate. Its dual norm is exactly |psi(v)|+c_v|Delta psi(v)|(1+H_c(v)) for the max model and max{c_v|Delta psi(v)|, |psi(v)|+c_v|Delta psi(v)|H_c(v)} for the sum model. Local finiteness makes finite-level coordinate projections finite rank, giving the matching upper bound; for every compact K, the non-root coordinate rows e_v^*K tend to zero in norm, giving the reverse bound. The c_v=1 and c_v=|v| specializations follow directly. No finite experiment is used as an infinite proof.

## originality

PASS

The closest complete primary source, Allen--Colonna--Easley (2013), explicitly says it provides estimates for the essential norm and proves max{A(psi),B(psi)} <= ||M_psi||_e <= A(psi)+B(psi); it does not state the exact row-limsup formula. The 2026 graph generalization likewise advertises essential-norm estimates rather than this equality, and Resultary did not return an earlier exact formula. The exact c_0 coordinate computation therefore survives the implication comparison. Older unavailable graph/tree sources remain a named risk rather than novelty evidence.

## value

PASS

The essential norm is a natural operator invariant already explicitly bounded in the prior literature. Replacing a known two-sided gap by an exact formula, and doing so for arbitrary positive edge weights, is a motivated structural result with direct compactness and perturbation consequences. Its short c_0 proof does not make the exact invariant a routine known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
