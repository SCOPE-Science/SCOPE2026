---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently reconstructed the proof. The determinant factorization makes the estimator conditionally unbiased and the Gaussian quadratic-form variance is twice the squared Frobenius norm of log M. Almost surely ker(U^T) in the spike block has dimension (r-ell)_+ and gives exactly that many forced eigenvalues 1+t in a reducing subspace. In its orthogonal complement substituting c=U^+a into the Nyström residual variational formula bounds the residual by (1+||VU^+||^2)I; the inverse congruence is contractive since P>=I and preserves the complement. The remaining eigenvalues lie in [1,2+||VU^+||^2]. The least positive singular value of U dominates that of a square Gaussian subblock by Gram matrix monotonicity. Its inverse norm has a half moment by the adjugate bound, Hölder exponents 3 and 3/2 and the QR chi-product negative determinant moment of order 3/4, including a final chi with one degree of freedom. Independence of U and V and log^2(2+z^2)=O(1+z^(1/2)) give the contrast-uniform expected bound including the square case ell=r. This yields the exact diverging coefficient and both directions of the threshold.

## originality

PASS

The exact two-dimensional predecessor is credited as overlapping and stronger in its own case. The supported distinct result is the all-multiplicity Gaussian-sketch threshold, with a bounded remainder and a zero-oversampling boundary. No examined benchmark or broader theorem supplies that result.

## value

PASS

The benchmark isolates exactly how many sketch directions are needed to prevent contrast-driven one-probe variance, even when ordinary square Gaussian inverse moments are too strong to use. The logarithmic observable permits a sharp conclusion at the no-excess-sketch boundary, and the exact coefficient distinguishes failure to capture the spike subspace from bounded error on the remainder. This is more than reproducing the dimension-two example or the ideal spectral benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
