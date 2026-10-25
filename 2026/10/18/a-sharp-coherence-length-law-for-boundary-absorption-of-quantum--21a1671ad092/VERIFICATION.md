---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: The cited half-line Lindblad sink resolvent yields a Parseval decomposition A_{n,K}=B_eta(c)+E_{n,eta}(c). Exterior term nonnegative and its polynomial numerator bounded by K gives E<=K/[2pi n(n-1)] uniformly in c and eta>0. The in-band factor 2 eta sin(k)/(1+eta²+2 eta sin(k)) is bounded pointwise by sin(k)/(1+sin(k)), with equality only at eta=1; any nonzero preparation polynomial is nonzero on positive measure, proving unique far-field loss and top Toeplitz eigenvalue Lambda_K. At eta=1 the full-circle scalar symbol sigma(k) has deficit satisfying x(k)/4 <=1-sigma(k)<=x(k)/4+x(k)^2/8 with x=|exp(ik)-i|². The Dirichlet path Laplacian gives smallest x-energy lambda_K=4sin²(pi/[2(K+1)]); the chirped sine ground-state packet yields exact x²-energy lambda_K²+[4/(K+1)]sin²(pi/(K+1)). Thus both explicit K bounds and Lambda_K=1-pi²/[4(K+1)²]+O(K^-3). Independent 2048-node Gauss-Legendre quadrature and Hermitian eigenvalues for K=1,2,3,5,10,20 verified lower/upper deficit bounds and K=1=1-2/pi,K=2=2/pi. The exact Green-function premise is sourced to Riberi and not claimed as independently proved from first principles; numeric finite K cannot prove asymptotics.

## originality

PASS

PASS qualified: Riberi 2026 original half-line sink model, Green function and single-site eventual absorption were inspected in a full HTML version including Appendix D. His localized one-site initial states correspond to K=1; the submitted arbitrary *coherent finite preparation window* optimization, Toeplitz K-by-K operator, uniform n finite-distance bound and sharp K^-2 locality penalty are not stated in those results. Classical extreme Toeplitz eigenvalue theorems may imply a similar leading spectral asymptotic, but the full quantum preparation and sink-optimization claim adds the physical structure and quantitative finite bounds.

## value

PASS

PASS: The amount of coherence/initial preparation bandwidth needed for near-perfect absorption is a natural quantum-transport invariant, and the sharp 1/(K+1)^2 loss with a finite-distance error provides a useful preparation-resource scaling law. Exact K=1,2 phase-control behavior and uniqueness of optimal coupling are physically motivated boundary results, not arbitrary Toeplitz number extraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
