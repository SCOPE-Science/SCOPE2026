---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The final claim is for exactly two fixed states, iid symmetric Beta(alpha,alpha) off-diagonal entries alpha>0, with Pi=V/(U+V), Lambda=1-U-V. The inverse (U,V)=(s(1-r),sr), s=1-Lambda, has Jacobian s and exact support max(0,1-1/s)<r<min(1,1/s) for 0<s<2. Thus the joint density is s^(2alpha-1)[r(1-r)(1-sr)(1-s+sr)]^(alpha-1)/B(alpha,alpha)^2. On s<1 at alpha=1 this is s, so r is uniform independent of s; for alpha≠1 its r=1/2 to 1/4 conditional-density odds vary with s, with exact bracket limits 4/3 and 16/9, proving the only-if. On s>1 moving positive conditional support makes independence impossible for all alpha. At alpha=1 the joint law is f(r,ell)=(1-ell) 1_D, eigenvalue density 1-|ell|, conditional variance 1/12 if ell>0 and (1+ell)^2/[12(1-ell)^2] if ell<0. Independently reran SymPy integrations: Var(Pi)=3/4-log2=0.05685281944 and Cov((Pi-1/2)^2,Lambda)=7/6-5log2/3=0.01142136573>0; marginal densities each integrate to 1/2. Exact constraints and measure-zero ell=0 are respected. These independent algebraic checks corroborate the self-contained analytic proof, not an appeal to logs or finite experiments.

## originality

PASS

Qualified best-of-knowledge: exact full sign-conditional independence iff alpha=1 and the associated random joint density/moments were not located in inspected same-ensemble and same-invariant primary literature. The deterministic support domain is already implied by Kirkland 2023 Theorem 4.1 and is not counted as new. Chafai provides independent uniform Dirichlet rows, a sufficient starting premise from which the alpha=1 law is a short calculation; this does not itself state the all-alpha iff law. Higher-dimensional circular-law results do not imply it. Residual priority risks explicitly retained.

## value

PASS

The stationary mass and nontrivial eigenvalue are the canonical two observables of equilibrium and mixing for a two-state stochastic matrix. Conditional independence under nonnegative spectral sign at exactly one symmetric Dirichlet prior, versus unavoidable dependence with negative sign, gives a complete natural classification of these coupled observables; the strict nonzero squared-balance/eigenvalue covariance illustrates dependence hidden from the ordinary covariance. Although the computations are short, the exact joint law and unique-alpha phase are a motivated distributional property rather than an arbitrary constant, renamed standard theorem, or mere numeric recomputation. No multi-state or broad universality consequence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
