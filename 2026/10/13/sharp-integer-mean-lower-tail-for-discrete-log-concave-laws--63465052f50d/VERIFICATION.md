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
# Verification

The proof is analytic. The critical checks are:

1. For the truncated geometric law on \(\{0,\ldots,n\}\), differentiation with respect to \(\theta=\log r\) gives \(d\mu_n(e^\theta)/d\theta=\operatorname{Var}(Y)>0\).
2. At \(r=k/(k+1)\), the corresponding infinite geometric law has mean \(k\), and truncation at \(n>2k\) strictly lowers that mean.
3. As \(r\uparrow1\), the truncated law becomes uniform and its mean tends to \(n/2>k\); hence the integer-mean parameter exists uniquely.
4. For fixed \(k\), comparison with every fixed \(s>k/(k+1)\) proves \(r_{k,n}\to k/(k+1)\).
5. The exact tail formula
\[
 r_{k,n}^{\,k}\frac{1-r_{k,n}^{\,n-k+1}}{1-r_{k,n}^{\,n+1}}
\]
then tends to \((k/(k+1))^k\).
6. Reversal \(X=n-Y\) preserves log-affinity, makes the mean \(n-k\), and identifies the tail with \(\{X\le\mathbb E[X]\}\).
7. The elementary limit \((1+1/k)^{-k}\to e^{-1}\), combined with the published lower bound, gives the exact infimum.

The bundled `verify.py` solves representative mean equations by bisection, checks the resulting means and tail probabilities, and confirms convergence numerically. It does not prove the all-parameter theorem or the literature comparison.
