# Review: Fixed-index low-bandwidth spectra for arbitrary two-window Fourier concentration

## Correctness — PASS
The exact dilation identity \(K_t=tT_t^*T_t\) is valid for measurable positive-measure bounded windows. The unique lowest-degree term in the exterior-power determinant expansion is the Vandermonde tensor, with normalization set by the Gram--Hankel quotients \(h_j(D)\). Taking consecutive exterior singular-norm ratios yields \(\lambda_n(t)\sim (2\pi)^{2n}h_n(E)h_n(F)t^{2n+1}/(n!)^2\). Exterior singular-vector convergence and nested rank projections recover the individual orthogonal-polynomial eigenmodes. The argument is for each fixed index only; exact rational moment and quadrature tests at disconnected windows independently check signs and leading coefficients.

## Originality — PASS, subject to historical-priority limitations
Marceca--Romero--Speckbacher (arxiv:2301.11685) treat two-domain eigenvalue counting rather than this small-dilation all-mode coefficient law. Israel--Mayeli (arxiv:2301.09616) treat higher-dimensional spectral distributions with expanding windows. Bonami--Jaming--Karoui (arxiv:1804.01257) treat nonasymptotic classical single-interval bounds. The accessible prior principal-eigenvalue moment expansion does not cover higher fixed indices and independently irregular frequency windows; a finite Hankel-transform small-bandwidth law pertains to a distinct radial operator. Indexed-result queries for orthogonal-polynomial eigenmode limits, Hankel moment determinant coefficients and exact fixed-index small-bandwidth Fourier spectra identified no covering statement. An unindexed older analytic-kernel treatment might still establish an equivalent theorem; arxiv:2006.00427 was considered at the abstract level only, not inspected in full.

## Mathematical value — PASS
Individual concentration eigenvalues across disconnected observation and frequency sets are not determined by counting estimates or principal-only moment expansions. The theorem identifies all fixed-mode leading constants and the strong-limit maximizing mode shapes, for a continuum of irregular domains without smoothness assumptions. This is a motivated, nonroutine exact spectral asymptotic for a natural two-domain Fourier concentration operator; it does not assert a general growing-index theory or a finite-bandwidth closed form.

## Reproducibility and limitations
The accompanying checker computes exact rational moments and finite-quadrature singular spectra for independently disconnected windows. These finite tests check normalization only; the infinite-dimensional limit is proved analytically. Priority remains uncertain in unindexed historical treatments. Independent validation has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
