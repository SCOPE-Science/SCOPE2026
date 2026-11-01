---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Orthogonal diagonalization of real symmetric negative-semidefinite factors reduces every spectral error to Cov(e^-aU,e^-bU) for U uniform on [0,1]. The symmetric double-integral gives nonnegative sign and zero exactly when a=0 or b=0. Cauchy–Schwarz bounds F(a,b) by max_t Var(e^-tU), attained only a=b=t*. Symbolic derivative 2t^3 W'(t)=e^-2t H(t) and sign-chain H triple-prime = -4e^t J(t) with J double-prime = (2t-1)e^t shows a single positive maximizing root; independent derivative and covariance checks give t*=3.24530448 and C*=0.0661398939754. Rank and dimension arbitrary but factors symmetric. Relative captured action tends zero for a=b→∞; fixed generators have h²/12 A⊗B leading error. Analytic argument, not grid, proves sharp global norm statement.

## originality

PASS

Best-of-knowledge comparison of the same final mathematical statement and direct implications, including exact-model primary sources, relevant general theorems and named residual priority risks. Absence of a matching search hit is not presented as proof of novelty. Caliari–Cassini Theorem 1 proves O(h²) direction-splitting for fixed generators, not uniform all-stiffness constant or equality set. Sylvester/quadrature methods recover phi-actions differently and do not imply sharp error for the uncorrected tensor product.

## value

PASS

Global sharp stiffness-independent operator bound, positivity, equality spectra, and failure of uniform relative accuracy are motivated numerical matrix-function questions. Constant has exact variational characterization and impact on two-direction tensor splitting beyond local O(h²) accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
