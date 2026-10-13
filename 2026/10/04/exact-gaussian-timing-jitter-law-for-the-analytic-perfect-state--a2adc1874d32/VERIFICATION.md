---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Christandl equation (15) verifies the normalization J_n=lambda sqrt(n(N-n))/2 and amplitude [-i sin(lambda t/2)]^(N-1). At t0+Xi, occupation probability is cos^(2m)(lambda Xi/2). Expanding the 2m-th cosine power gives the central binomial Fourier coefficients; the Gaussian characteristic function multiplies coefficient k by exp(-k^2 s^2/2), establishing the exact sum for all m>=1 and s>=0. Positive coefficients imply strict decrease for s>0, with endpoints 1 and 4^-m binom(2m,m). For s=c/sqrt(m), the pointwise log-cosine limit is -c^2 Z^2/4, with bounded integrand; dominated convergence gives (1+c^2/2)^-1/2. For fixed s>0, each central-binomial coefficient ratio tends to one and is bounded by one; the summable Gaussian weights and central-binomial asymptotic give the theta-series constant. Targets eta in (0,1) have a unique finite root only when eta exceeds the plateau; this holds eventually in m. Bracketing the strictly monotone limiting profile gives the stated target threshold without assuming unwarranted uniform convergence. Independent direct Gaussian integration agrees with the finite sum to about 2e-16 at four (m,s) pairs; this is supplemental numerical evidence, not an infinite proof.

## originality

PASS

Best-of-knowledge PASS restricted to the complete finite Gaussian average and its two sharp chain-length regimes. The engineered chain and amplitude are known. Kay-Kim-Tamon 2025 explicitly introduces general random readout-time averaging, so stochastic averaging itself is not novel; their full paper optimizes local sensitivity and other chain designs rather than stating the present Gaussian finite sum and theta-profile limits. The known inverse-square-root timing scale is also excluded from standalone novelty.

## value

PASS

Timing precision is explicitly motivated in both the older review and the 2025 stochastic receiver framework. The exact finite-chain occupation law converts a Gaussian standard-deviation specification into a performance quantity. Its shrinking-noise profile gives a target-dependent calibration constant, whereas fixed noise retains periodic-revival contributions through a theta series. Distinguishing these regimes provides information beyond a local curvature or deterministic window and is a natural useful exact fact of an established chain, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
