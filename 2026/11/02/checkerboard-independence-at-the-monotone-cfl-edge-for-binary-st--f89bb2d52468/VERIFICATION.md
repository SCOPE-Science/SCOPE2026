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

The matrix B=(1-2h)I+hA_path is nonnegative for 0<h<=1/2 and positive Perron vector w_i=sin(pi i/(m+1)) has 0<rho=1-2h+2h cos(pi/(m+1))<1. Common-uniform coupling contracts weighted Hamming distance; finite-state existence, uniqueness, geometric convergence follow. At stationarity Es=0, C=BCB+D with diagonal D>=0; boundary D11>0. The positive path series Σ B^t D(B^t)^T proves all off-diagonal signs and parity zeros at h=1/2. Two-step transition kernel then splits by parity, and uniqueness for P² proves full block independence. For m=2 exact two-spin stationary moment q satisfies q=2h(1-2h)+((1-2h)^2+h^2)q, hence covariance formula. Independently computed 2-site Markov transition and stationary covariance at h=1/6,1/2,3/5 and checked endpoint case. These finite checks do not establish all m.

## originality

PASS

The claimed object is a coarse fixed-binary lattice Bernoulli quantization, not IEEE stochastic rounding; Croci and Giles analyze floating-point heat-solver error propagation, not stationary joint binary laws. No located published specialist result gives this precise finite-reservoir block-independence and two-cell sign reversal. Synchronous noisy-voter similarities make broader covariance and sublattice factorization precedents a residual historical risk.

## value

PASS

The numerical-stability boundary h=1/2 acquires a nontrivial stochastic stationary independence structure and m=2 changes correlation sign while deterministic Euler is still spectrally stable. This is a meaningful structural contrast between monotone CFL positivity and numerical stochastic dependence, not a routine moment calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
