---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

On D_beta with squared monomial weight (k+1)^(1-beta), the normalized basis is e_k=(k+1)^((beta-1)/2)z^k. The exact operator matrix for P(z) f^(n)(exp[-eps]z) has finite shifts j-n and entry p_j eps^n k!/(k-n)! exp[-eps(k-n)]((k+1)/(k-n+j+1))^((beta-1)/2). Compared to P(S)S*^n D_eps, the residual is O(eps) in operator norm and contributes negligible eps-scaled Schatten-q mass for every q>0. Closed-walk moments of the slowly varying finite-band Gram matrix lead to the two-variable symbol g(x)|P(e^{i theta})|, g=x^n exp[-x]. Uniform small-singular-value control via q<p extends positive-threshold counting to every Schatten p>0, while localized plane waves establish the sharp spectral norm edge. Exact orthogonal monomial-column summation produces the Hilbert-Schmidt first correction eps^((2n)+1)||T_eps||^2 = [(2n)!/2^(2n+1)]A_P + eps[(2n-1)!/2^(2n)][n(n+beta)A_P-(beta-1)B_P]+o(eps). The finite-dimensional numerical tests separately corroborate the coefficient and are not a proof of infinite-rank asymptotics. Independently verified exact rational coefficients and numerically checked first-correction slopes for beta=0,1,3, n=1.

## originality

PASS

Best-of-knowledge based on actual source-tree proof inspection, prior claim/implication comparisons and the explicit coverage boundaries. A general second-order Szego/GLT trace expansion may cover the first Hilbert-Schmidt correction; this historical priority remains unexcluded.

## value

PASS

This is a natural sharp spectral invariant for differentiation combined with near-identity composition on a precisely normalized family of coefficient Dirichlet spaces, including all quasi-Schatten exponents. The bulk local-Toeplitz principle is known; the coupled polynomial symbol and first index-dependent Hilbert-Schmidt correction isolate information invisible to the leading law, providing a motivated nontrivial specialization. Scope fixes beta,n,P as eps->0 and no arbitrary symbols are asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
