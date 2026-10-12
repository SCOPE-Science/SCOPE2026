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

The proof is analytic. The accompanying checker performs three supplementary replays.

For every simple symmetric lattice walk of length at most \(16\), it exhaustively computes
\[
A_n=\sum_{k=1}^n\mathbf 1_{\{S_k>0\}}
\]
and \(S_n\), and verifies with exact rational arithmetic that
\[
\operatorname{Cov}(A_n,S_n)
=
\frac12\sum_{k=1}^n\mathbb E|S_k|.
\]
This check deliberately uses a lattice law with ties, demonstrating that the covariance identity itself does not require continuity.

For every \(1\le n\le200\), the checker verifies directly from
\[
p_{n,r}
=
4^{-n}\binom{2r}{r}\binom{2(n-r)}{n-r}
\]
that the probabilities sum to one and have mean \(n/2\) and variance \(n(n+1)/8\).

Finally, it evaluates the exact Gaussian correlation formula at increasing \(n\) and confirms convergence toward
\[
4/(3\sqrt{\pi}).
\]

These computations are not used as an infinite proof. The universal result follows from the exact mixed-moment reduction, the classical Sparre-Andersen law, and the central limit theorem with uniform integrability.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK lattice_paths=131070 covariance_checks=16 arcsine_normalizations=200 arcsine_means=200 arcsine_variances=200 gaussian_checks=5 last_corr=0.752254651282 target=0.752252778064`.
