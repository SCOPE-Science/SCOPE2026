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

The proof is analytic and uses no finite numerical experiment.

For a degree-\(N\) symbol, direct basis multiplication gives
\[
H_{\overline\psi}z^j
=
\sum_{m=1}^{N-j}\overline{c_{m+j}}z^{-m}
\quad(0\le j<N),
\qquad
H_{\overline\psi}z^j=0
\quad(j\ge N).
\]
Hence the operator is finite rank and
\[
\operatorname{Ran}(H_{\overline\psi}^*H_{\overline\psi})
\subset
\operatorname{span}\{1,\ldots,z^{N-1}\}.
\]

Normalized Hardy kernels are weakly null at the boundary. Compactness therefore forces their Hankel images to vanish there, so any kernel attaining the nonzero operator norm is an interior kernel. Equality in the positive Rayleigh quotient makes that kernel an eigenvector of \(H^*H\); the finite polynomial range forces the center to be zero.

At \(k_0=1\), the top-eigenvector equations are the positive-lag autocorrelation equations
\[
\sum_{m=1}^{N-j}c_{m+j}\overline{c_m}=0.
\]
If \(r\) and \(s\) are the least and greatest occupied degrees with \(s>r\), the lag \(s-r\) leaves only
\[
c_s\overline{c_r},
\]
which is nonzero. Thus nonmonomial support is impossible.

For a monomial symbol, the basis action is a scalar multiple of a finite partial reversal and \(k_0\) attains the operator norm directly.

The verification establishes only the polynomial-symbol theorem and does not assess the broader open classification for general bounded or BMOA symbols.
