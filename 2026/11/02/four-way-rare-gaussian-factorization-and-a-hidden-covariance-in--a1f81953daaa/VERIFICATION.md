---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Conditioning on K=k distinct selected cards gives a uniform k-set and independent uniform permutation of the selected labels as the prefix, with sorted unselected suffix; J has exact tail-maximum hypergeometric law and U falling factorial moments (|S∩[k]|)_ell/(k)_ell. For k/n→alpha these give independent Poi(alpha) and Geom(alpha) uniformly in central k. Uniform-permutation Eulerian descents obey CLT with variance k/12; forcing ell fixed positions and deleting/relabeling them changes descents by at most 3ell, yielding mixed factorial-characteristic-factorization independent of rare counts. The occupancy conditional bivariate local CLT produces independent H with tau²=e^-c-(1+c)e^-2c; A=(K-1)/2+√n G+o_P(√n), D=A+boundary with |boundary|<=1. Unscaled covariance requires a different calculation: E[F|K=k]=k/n+(n-k)/(k+1), Cov(U,A|K=k)=(1-k)/(n(n-1)), Cov(J,A|K=k)=0; bounded endpoint term covariance tends 0 by geometric/UI bounds; delta method gives 1/2 tau²(1-alpha^-2). Independent exhaustive finite selected-set checker for n=3..7 validated conditional covariance and boundary identities; these checks are not the asymptotic proof.

## originality

PASS

Clay 2026 already supplies uniform-prefix coupling, marginal fixed-point Poisson–geometric limit, marginal Eulerian/occupancy Gaussian central limits; these must not be claimed original. The joint four-variable asymptotic independence and nonzero negative order-one unnormalized covariance are additional dependence statements not implied by marginals or uniform-stationary permutation endpoint covariance. Accessible original paper did not state either joint result.

## value

PASS

A fully joint local-time shuffle theorem distinguishes asymptotic independence at sqrt(n) scales from a persistent order-one negative covariance at unscaled scales; the exact covariance constant is a natural dependence invariant invisible from the already known separate limit laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
