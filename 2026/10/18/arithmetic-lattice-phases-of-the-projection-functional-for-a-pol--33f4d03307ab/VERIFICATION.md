---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Regular-ring averaging is exact through Fourier degree four for n≥5. Writing R²=X²+Y² gives the unnormalized ring average 6R⁴+12R²Z²+Z⁴, and the weights give (R²+Z²)²/5 after the pole term. The diagonal second moments are 1/3 in every coordinate and the mixed moments vanish, so the normalized Gram is a rank-three projection. The absolute Gram is positive: the only potential zero ring entries require 2 cos(2πj/n)=−1/2, impossible for a rational algebraic integer. Perron uniqueness makes the positive eigenvector constant around the ring; in pole/normalized-ring coordinates the matrix is (1/2)[[1,1],[1,a_n]]. The signed ring average is one and the positive indices are 0 and ±1 through ±floor(nα). A geometric sum yields the stated a_n, including a_5=1+4√5/5 and a_6=8/3. As an independent check of the cusp asymptotic, put s={nα}, δ=1−2s. Rewrite a_n as −1+4α+2δ/n+(8/n)sin(θ+δπ/n)/sin(π/n). The n^−1 terms cancel since cos θ=−1/4; the n^−2 coefficient is 8π sin θ(1/6−δ²/2)=−4π√15 B_2(s). Taylor's remainder is uniform since |δ|≤1. Composing with Φ gives the asserted coefficient, and the density of the irrational phase yields both exact extremal subsequence limits. The frozen script was read, not executed; sampled moment and eigenvector checks do not establish the all-n formula or the remainder.

## originality

PASS

The supported result is the exact all-size value of the already defined fixed-frame functional on this design family, including its sharp irrational second-order phase. Neither the frame functional, the seven-point geometry class, the Perron method, nor Bernoulli quadrature is new. The inspected primary passages and related exact catalogue results concern different optimizations, observables, or kernels. The original Hu–Tang manuscript was not available in lawful full text, so independent comparison of its exact ring parameters is limited to the accessible D–L report.

## value

PASS

This is a concrete exact invariant of a natural family of weighted designs from projection-constant theory, extending the regular pentagonal and hexagonal ring examples. The sign-changing sharp n^−2 fluctuation shows why a single second-order constant cannot describe discretization to the continuous-ring benchmark. The exact finite values make the comparison possible without incorrectly treating this fixed-frame quantity as a global projection constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
