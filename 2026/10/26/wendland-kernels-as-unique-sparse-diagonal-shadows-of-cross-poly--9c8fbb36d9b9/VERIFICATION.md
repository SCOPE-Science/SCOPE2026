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

Let E_1,...,E_(d+1) be i.i.d. Exp(1), S=sum E_i, ε_i independent signs, X_i=ε_iE_i/S. Gamma–Dirichlet independence shows X has uniform normalized volume on B_1^d and S is independent of Y=sum_{i≤k}X_i. Since ε_iE_i are independent symmetric exponential/Laplace variables with characteristic function (1+t²)^(-1), SY has characteristic function (1+t²)^(-k) and even moments E[Y^(2n)]=(2n)!(k)_n/[n!(d+1)_(2n)]; odd moments vanish by sign symmetry. For W_k=I^(k-1)(1-r)^k, I f(r)=∫_r^1u f(u)du, repeated Fubini gives ∫_0^1r^m W_k(r)dr=B(m+2k-1,k+1)/prod_{j=0}^{k-2}(m+2j+1). Dividing m=2n by m=0 yields (2n)!(k)_n/[n!(3k)_(2n)]. At d=3k-1 every moment of two compactly supported symmetric probability laws agrees; polynomial density in C[-1,1] proves equality of measures and continuous density representatives p_k(y)=W_k(|y|)/(2∫W_k). For fixed k unit-weight coordinates and any d≥k, equality of second moments forces (d+1)(d+2)=3k(3k+1), strictly increasing and hence d=3k-1. Using d+1=3k exponentials and k independent signs yields the exact sampler. All statements hold for every integer k≥1, no multivariate/all-convex-bodies claim.

## originality

PASS

Best-of-knowledge original probability identity joining the entire family of one-dimensional normalized Wendland functions with sparse unit-weight coordinate sums of uniformly sampled cross-polytopes, plus a rigid ambient dimension and exact sampler. Wendland 1995 defines radial profile and positivity; Fields–Ismail hypergeometric positivity covers transforms; Bell provides crosspolytope volume/Fourier background. Those known results are credited and do not, in inspected material, express this specific all-order pushforward or its dimension uniqueness. Original Wendland full text and possible older probability-shadow representations inaccessible: significant residual historical priority risk, not an automatic O failure.

## value

PASS

The result realizes an established, natural hierarchy of compactly supported basis kernels as exact one-dimensional probability densities of a second natural geometric hierarchy, uniform cross-polytopes. Matching of *every* moment for all k, the rigid d=3k-1 dimension fingerprint, and a direct rejection-free sampler are a structurally useful translation between radial-basis and convex-probability models. A future researcher can exploit the precise distribution/normalization rather than just positivity or a few low-order tabulations. No novel positive-definiteness theorem or uniqueness over arbitrary convex bodies is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
