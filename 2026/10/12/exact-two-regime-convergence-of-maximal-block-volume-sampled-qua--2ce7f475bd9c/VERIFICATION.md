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

Jacobi complementary minors give label probabilities p_i=G_ii/tr(G); exact minimization fixes x_i and yields x^+=x_i Ge_i/G_ii. The second-moment transition Q_{ji}=p_j G_ij^2/G_ii^2 is diagonal-similar to K_ij=G_ij^2/(tr(G) sqrt(G_ii G_jj)); Schur positivity and Perron comparison prove r in (0,1), the positive all-coordinate start guarantees positive leading coefficient even when K reducible. A zero inverse-Hessian offdiagonal yields a positive-probability annihilating adjacent label pair almost surely; if all entries nonzero, telescoped scale ratios and finite-state ergodic SLLN yield gamma=sum p_i p_j log|C_ij|, negative since SPD strict correlations. Independently tested 2240 rational/numerical path-update identities over 40 SPD matrices; no finite test substituted for spectral/SLLN proofs.

## originality

PASS

Published volume-sampling schemes supply block selection and objective-contraction bounds; the actual maximal proper-block pathwise multiplier chain, its exact Hadamard-square annealed factor and quenched/absorption dichotomy are not consequences of those bounds without substantial reduction. Best-of-knowledge novel though a matrix-product/Markov additive derivation could predate it.

## value

PASS

This quantifies two different natural notions of convergence for a real determinant-volume optimization algorithm and gives a sharp inverse-Hessian structural criterion for finite termination, neither merely a routine estimator bound nor an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
