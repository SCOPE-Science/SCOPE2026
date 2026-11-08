---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Write t=a^n, c=b/(1-a), T_t=C_phi^n-P=f(c+t(z-c))-f(c). The trace-class Taylor expansion T_t=Σ_{m>=1}t^m q_m⊗h_m has q_m=(z-c)^m, h_m=z^m exp(z conjugate(c))/m!; Gaussian norm bounds yield term trace norms at most exp(|c|²/2+2|c| sqrt(m)), hence absolute trace norm convergence for |t|<1. The exterior jth power uniquely starts at t^(j(j+1)/2)(q_1∧...∧q_j)⊗(h_1∧...∧h_j), because no repeated indices survive; dividing consecutive products of singular values yields the product of successive Gram-Schmidt distances. The first pivot squared is d_j²=j!+|c|^(2j)/K_{j-1}(c,c), K=sum_{k=0}^{j-1}|c|^(2k)/k!; Weyl translation gives second pivot exp(|c|²/2)d_j/j!, so the sharp fixed-rank constant follows. Independent exact rational Gram determinant pivots at c=2/3 for j=1..5 confirm the closed expression, while asymptotic all-n proof uses trace class and exterior-power uniqueness. No rank j growing with n is claimed; c=0 exact diagonal case checked.

## originality

PASS

Best-of-knowledge originality: original claim adds the mathematically distinct sharp classification/quantitative invariant described in the four actual prior-implication checks; no dominating statement was identified in checked primary literature, with listed specific residual risks.

## value

PASS

Fixed-point projection subtraction is a natural but nonorthogonal refinement of convergence of compact affine Fock composition operators. The full fixed-rank singular/error hierarchy and explicit rank-dependent truncated-Poisson coefficients quantify convergence in best finite-rank approximations and expose behavior hidden by the norm convergence theorem; the result is not a routine simplification of uncorrected operator singular values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
