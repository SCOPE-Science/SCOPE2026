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

Tensor identity A_H=A_G⊗J_2 has rank r over every field, even characteristic 2, so dim E²=r and quotient dimension c=2N-r. A nonzero ideal contains some square e_i²; multiplying by adjacent e_j propagates e_j² along every connected symmetric edge, proving E²⊆I. Conversely any subspace I⊇E² is an ideal because E·E⊆E². Counts equal 1+Σ_j [c j]_q, with lower bound q^(floor(N²/4)) from graph subspaces. Real adjacency eigenvalues of H are 2λ_i(G) plus N zeros, yielding h(H)≥h0²/(2d) via standard Cheeger inequalities. K4 blowup has h=3, rank_F5=4, c=4 and 1121 ideals; s_i=e_i0+e_i1 and t_i=e_i0-e_i1 form a natural basis over F5 with proper basic E². Independent computation directly enumerated 8-vertex Cheeger cuts, matrix rank, all Gaussian counts and cross-products of these natural basis vectors; finite tests corroborate the uniform proofs.

## originality

PASS

Giacomelli arXiv:2605.12672v1 Theorem 3.8 actually asserts symmetric expander evolution algebras are simple, using a connectivity-to-ideal-simplicity step that fails for singular structure matrices. The present explicit connected regular expander counterfamily, full quotient-ideal lattice and eight-vertex BASIC ideal witness mathematically contradict that claim. Earlier papers on evolution ideals and subspaces containing E² supply the background lattice mechanism, which is not claimed as original. The specific robust counterfamily and exact quadratic finite-field ideal entropy were not present in the full target article or retrieved related findings.

## value

PASS

This is a motivated counterexample to a stated 2026 simplicity theorem in the same graph/evolution algebra setting, strengthened to bounded-degree uniform expander families and exact quadratic ideal-abundance asymptotics. The explicit proper basic ideal addresses possible definitional objections. Such a correction is a substantive mathematical boundary with immediate interpretive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
