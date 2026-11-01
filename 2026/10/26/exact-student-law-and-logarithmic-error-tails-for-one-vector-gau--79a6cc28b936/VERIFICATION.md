---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Independently reconstructed the one-vector sketched FOM formula (Sv)^dagger SAv and decomposed Av=alpha v+rho w with w orthogonal to v (SPD is more than necessary for this projection identity). For each of ell independent isotropic Gaussian rows, G=sqrt(ell)Sv and H=sqrt(ell)Sw are independent N(0,I_ell). The ratio (G^T H)/(G^T G)=Z/||G||, with Z independent N(0,1) and ||G||^2 chi-square(ell), is T_ell/sqrt(ell). Therefore Y=(lambda_hat-alpha)/rho has exactly normalized density c_ell(1+y^2)^(-(ell+1)/2), c_ell=Gamma((ell+1)/2)/(sqrt(pi)Gamma(ell/2)). Integrating the negative tail yields P(Y<-u)~c_ell u^(-ell)/ell; the deterministic exponential map changes u to (log R+O(1))/(t rho). Reverse triangle inequality bounds |error-approximation_norm| by the fixed finite true solution norm, proving the identical logarithmic tail constant for the actual error. The density has no finite negative-side exponential moments, giving every positive moment of approximation and error infinite (error controls half the norm beyond a fixed threshold). If rho=0, b is an eigenvector and the formula becomes exact a.s. All claims fix ell>=2<n and t>0 and condition on NO successful-embedding rejection. Independent script checked Gaussian-ratio normalization, explicit ell=2,3 constants and special-case limits; finite checks do not establish infinite-tail assertions.

## originality

PASS

The exact unconditioned shifted Student distribution and resulting logarithmic error-tail constant are not consequences of the qualitative outlier Ritz observation in the original sketched-FOM paper, nor of high-probability subspace-embedding error bounds. Palitta–Schweitzer–Simoncini analyze larger sketched Krylov approximants and outlier effects, not this precise all-positive-moment divergence for the one-column, unsafeguarded Gaussian scalar exponential. The Gaussian normal/chi ratio is classical, so originality resides only in its identification with this numerical method and its exact transformed-error implications. Equivalent random least-squares or one-vector regression results remain a real priority risk.

## value

PASS

For an established SPD matrix-function algorithm, a high-probability accurate approximation can nevertheless have an unbounded unconditional mean and every positive error moment, with a computable log-Pareto tail. The sharp constant distinguishes embedding-conditioned guarantees from unconditioned risk and supplies a precise mathematical reason to consider safeguarding or rejection, without asserting such procedures are proved here. This is a motivated numerical stability result, not merely a Student-law rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
