---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational and analytic verification

The analytic proof establishes the claim for all integers \(k\ge2\), \(m_j\ge2\), all strictly positive prices and budgets. A finite verifier is provided to catch normalization and algebraic mistakes; it is not an exhaustive infinite-case proof.

Run `python3 verify.py` with Python 3 and only its standard library. The checker performs exactly 480 assertions, including 96 direct exact-rational Kirchhoff-index calculations from independently inverted grounded Laplacians, exact phase-boundary derivative comparisons, and five examples checking feasibility, the precise optimum, positive and inactive internal edges, and full-graph inverse calculations. Its observed result was `PASS: 480 independent assertions; exact rational inverses and optimality identities`.

The most important manual identities are \(A_j+C_j=m_j(N-1)\), \(f_j'(t)=b_jA_j-(a_j-b_j)C_j/t^2\), and the equality condition in \(\sum_jF_j/E_j\ge(\sum_j\sqrt{F_j})^2/B\). The proof explicitly treats zero peripheral weights and the equality price threshold. No computer algebra, finite enumeration, empirical eigenvalue sample or numerical optimization is relied upon for the infinite-family conclusion.

The source-based novelty check was limited to identifiable, accessible literature; the full text of a 2024 windmill-index paper could not be obtained. Independent mathematical validation remains unperformed.
