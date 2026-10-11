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

# Verification and limits

The graph, edge-current observable and stationary variational domain are defined explicitly in `RESULT.md`. The weighted Perron eigenvector equations reduce exactly to \(\lambda^2-C\lambda-k=0\), and its Doob kernel satisfies \(C/\lambda+k/\lambda^2=1\). Direct differentiation yields \(m_k=2\sinh(t)/S_k(t)\), \(m'_k>0\) and \(P^{(4)}_k(0)=2(4k-9)/(9+4k)^{3/2}\). The heart of the global proof is the closed identity for \(F_{9/4}\), the coefficient formula \(a_n\), the inequality \(n a_{n+1}-(n+1)a_n>0\) and the consequent monotonicity of \(F_{9/4}/D\). This establishes the unique positive spinodal and coexistence roots for every integer \(k\geq3\), not just numerical cases.

Computational cross-checks, not substitutes for proof: symbolic expansion verified the hyperbolic \(F_{9/4}\) identity and the closed coefficient-difference identity; direct series coefficients through order eleven agree. Independent scalar bracketing gives for \(k=3\): \(\beta_s\approx2.27460002\), \(\beta_t\approx2.27861888\), \(\beta_c\approx2.29128785\), and coexistence current \(m\approx0.43392301\). Numerical checks also sampled \(k=0,1,2,4,8,20\) without contradiction. Rounding means these are *illustrations* only. The proof handles every nonnegative integer \(k\) and every nonnegative \(\beta\).

Limitations: the classification is not claimed for other graph topologies, external fields, nonquadratic interactions, nonstationary kernels or nonequilibrium entropy production. No independent audit was performed.
