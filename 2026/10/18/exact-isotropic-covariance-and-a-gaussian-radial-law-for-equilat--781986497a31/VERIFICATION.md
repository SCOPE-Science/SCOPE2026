---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Verified sign-chamber Jacobi density sqrt(n)R^{n-2}/((k-1)!(n-k-1)!) and total volume sqrt(n)binom(2n-2,n-1)/(n-1)!. Exact rational independent binomial moment checks through n=24 show E[1/(K+1)]=(2n-1)/(n(n+1)) and Cov=4(2n-1)/(n(n+1)^2)I_H. Proof couples Dirichlet weights to exponential ratios Q_k and delta-method CLT with variance 4; independent hypergeometric K/n->1/2, radial R=U^(1/(n-1)), gives normalized Gaussian variance one. Finite symbolic checks support, not prove asymptotic. Euclidean zero-sum metric normalization is essential.

## originality

PASS

PASS with prior geometry credited: Alexander et al already give exact equilateral Lipschitz-free volume using chambers; the new assertion is bulk covariance, isotropic constant, exact sampler law and Gaussian radial CLT, neither entailed by a scalar volume formula nor identified in Kipp normality literature.

## value

PASS

Natural exact bulk invariant for a central family of Lipschitz-free unit balls; supplies a useful exact uniform sampler, precise affine-invariant isotropic constant, and quantitative thin-shell fluctuation universality beyond known volume.

The dated certificate retains the supplied scientific assessment, sources and limitations.
