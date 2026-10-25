---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Because Y=D^(1/2)G has codimension one, its missing normal is proportional to D^(-1/2)g for Haar-spherical g in kernel(G^T); the PSD residual is D^(1/2)hh^T D^(1/2) of rank one with unique eigenvalue L=(sum g_i^2/lambda_i +g_r^2/epsilon)^-1. With t=g_r and q(u)=sum_(i<r)u_i^2/lambda_i, t has density c_r(1-t^2)^((r-3)/2) and L=[(1-t^2)q+t^2/epsilon]^-1. Dominated convergence yields subcritical s<1/2 moment epsilon^s E|t|^-2s; at s=1/2 integration over |t|~sqrt(epsilon) gives c_r sqrt(epsilon) log(1/epsilon); for s>1/2 the substitution t=sqrt(epsilon)v gives c_r B(1/2,s-1/2) sqrt(epsilon) E q^(1/2-s). Fixing y<min lambda_i makes tail event a shrinking band |t|<sqrt(epsilon) sqrt(1/y-q), giving the claimed tail coefficient. The uniform circle integral at r=2 evaluates exactly to sqrt(lambda epsilon). Independent 250,000-sample sphere tests for r=3, lambda_1=lambda_2=1 gave E[L]=.1480005 vs leading .1570796 at epsilon=.01 and E[L]=.0487985 vs .0496729 at epsilon=.001; ratios approach one. Analytic proof, not samples, establishes the claim.

## originality

PASS

Standard Nyström projector identity and Haar normal are not novel. Persson-Boullé-Kressner (2025) derive Gaussian Nyström norm guarantees with positive oversampling in the quoted principal theorems; their publisher page was accessible only through abstract/metadata, and arXiv full-text retrieval failed. Gittens-Mahoney (2016) provide deterministic and oversampled Gaussian bounds but no matching fixed rank-(r-1), one-small-eigenvalue exact spherical residual distribution and half-moment asymptotic in the inspected portions. Moment transition constants may be mechanically extractable from older angular-statistics integrals; no directly dominating exact theorem found, and this priority risk is retained.

## value

PASS

Unoversampled Nyström is a genuinely important difficult regime where leading expected-error bounds can be misleading: typical error is O(epsilon), but E[L] is O(sqrt(epsilon)), causing an epsilon^-1/2 expected approximation factor. The complete moment trichotomy identifies the rare-event mechanism and exactly delineates which error summaries can be extrapolated, supplying a nontrivial testing benchmark beyond a routine projector restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
