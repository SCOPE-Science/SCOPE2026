---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For Rademacher signs the one-node Rayleigh-log output is deterministic and squared bias 4 log^2 cosh u. For uniform sphere, log(kappa cos²θ+sin²θ) has absolute Fourier expansion: mean log c and variance 2Li_2(t²), yielding M_S=16 log²cosh(u/2)+8Li_2(x). The difference/8 H(x) has derivative N(x)/(1-x²), with N increasing strictly from -1 to 2log2; H initially decreases, then increases to +infinity, so exactly one interior zero. Independently evaluated x*=0.77780968432523010353 and kappa*=254.07878454108627389 with high precision, and checked risk ordering. κ=1 both exact; sphere is normalized Gaussian direction, not ordinary Gaussian.

## originality

PASS

General randomized trace/Lanczos frameworks cover Gaussian and sign probes and sometimes sphere concentration, but do not state the norm-matched 2D one-node exact risk crossover and uniqueness. It is a narrow explicit theorem, not a claim that Lanczos, Fourier log series, or probe distributions are new.

## value

PASS

At the simplest nontrivial one-matrix-vector-product budget, deterministic zero-variance sign probes may have *greater* total squared risk than random sphere probes due to quadrature bias; the unique κ frontier is a meaningful warning against variance-only probe comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
