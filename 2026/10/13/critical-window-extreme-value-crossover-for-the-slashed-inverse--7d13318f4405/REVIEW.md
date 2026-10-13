# Scientific review

## Correctness — PASS

From the inverse-Rayleigh density and an independent Beta distribution, conditioning gives the exact normalized survival integral. Change of variables and integration by parts yield the upper incomplete-gamma representation. Splitting the kernel at one isolates \(L\Phi(w)\); differentiable domination for the remainder gives \(-\gamma_{\mathrm E}\) and a uniform \(O(L^{-1})\) term. A direct expansion for \(q_n=2+2\kappa/\log n\) supplies both the limiting Fréchet exponent and the \(\log\log n/\log n\) finite-size term. The checker independently compares exact survival values to conditional integration and checks boundary convergence. This is an analytic theorem; a finite test is not its proof. The assertion is limited to positive scale, sufficiently large arguments and row sizes, and bounded critical-window parameters.

## Originality — PASS, with residual risk

The July 2026 primary article's Section 2 and Proposition 8 establish the distribution and discuss pointwise regular variation. Previously available fixed-parameter tail classifications resolve the two sides and the critical logarithm but have no uniform moving-parameter statement. The present two-term crossover and the finite-size extreme-value law require interchanging limits along \(q=q(z)\) and controlling the nonuniform singular kernel. The 2007 product-tail theory concerns fixed products and does not state this triangular-array coefficient; the 2023 inverse-Weibull mixture uses a bounded multiplier rather than reciprocal-beta amplification. Mathematically related work may be unindexed, so a first-ever-priority claim is not warranted.

## Value — PASS

The boundary between the two competing tail exponents is a natural calibration regime for a heavy-tailed lifetime model. Near this boundary, fixed-parameter power laws do not reveal the correct normalization for an increasing sample, whereas the theorem gives a continuous interpolation \(\Phi(\kappa)\) and a quantitative logarithmic drift. The explicit correction is relevant to diagnosing slow finite-sample convergence of extreme quantiles. The result does not quantify arbitrary-parameter hazard shapes or prove non-asymptotic risk guarantees.

## Closest literature and limitations

Gómez et al. (2026), DOI 10.3934/math.2026938, is the directly relevant model source. Denisov and Zwart (2007), DOI 10.1239/jap/1197908822, is the general fixed-law product-tail comparison. Almuhayfith et al. (2023), DOI 10.1038/s41598-023-47313-3, is a related but different inverse-Weibull mixture. The theorem's asymptotic uniformity is only on specified compact ranges; unindexed priority and external scientific validation remain open.

Self-review: passed. Independent audit: not yet performed.
