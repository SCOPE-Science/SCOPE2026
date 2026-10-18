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

# Verification notes

## Analytic checks

The bivariate recurrence is an identity of finite formal probability-generating polynomials, with no analytic continuation or unproved cancellation. The covariance formula uses orthogonality of conditional-mean-zero innovations, and strict positivity follows from two available parent depths at every vertex \(i\ge3\). In the total-variation upper bound, the independent Bernoulli sum has a unimodal convolution mass function, and Fourier inversion yields the explicit \(V^{-1/2}\) maximum-mass bound. In the lower bound, Fourier domination and a third-moment estimate prove a uniform local central limit theorem at finitely many central lattice offsets. The threshold test is in \([0,1]\), so its covariance discrepancy is a valid total-variation lower bound. The power-weight boundary follows from explicit Bernoulli-parameter sums.

## Standalone finite certificate

Run `python3 verify_depth_dependence.py` using Python 3 and its standard library. The program enumerates all parent maps for seven-vertex trees with four different strictly positive weight vectors. For all applicable labeled vertex pairs, it independently constructs the exact rational bivariate law and the predicted Bernoulli convolution, verifies covariance invariance, and verifies normalization. An actual execution completed successfully: `PASS: 120 exact rational assertions across 4 weight cases`.

## Scope of verification

The exact finite checks do not certify the infinite local central limit theorem, asymptotic total-variation rate, or novelty; those depend on the supplied mathematical arguments and literature comparisons. No independent external validation has been performed. The first public source date was checked against the arXiv initial submission record of 2026-09-30, rather than a later revision or document date.
