# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/sharp-lag-one-spectral-envelopes-reversible-chain-variance--530e5145f9f6`  
Assigned and audited source tree: `6277f9a35d81226ffe65d014c4153b21a5cd8bd5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `5e7eccbe868b7bc11b55ab0198d527de028f730d`  
Disposition: **passed**

## Correctness

**independently_supported**. The spectral-envelope theorem is correct. For a positive reversible kernel, the centered observable's normalized spectral measure is a probability measure on [0,beta] and rho is its first moment. Jensen applied to x^k gives rho_k>=rho^k, while x^k<=beta^{k-1}x gives the upper envelope. The finite-sample mean-variance identity has nonnegative lag weights, so these simultaneous bounds give the exact finite-n interval. For asymptotic variance, g(x)=(1+x)/(1-x) is convex; Jensen gives the lower endpoint and the chord through 0,beta gives 1+2rho/(1-beta). The two-state refresh chain and its product with a zero-eigenvalue coordinate realize the endpoint spectral measures; adding independent coordinates realizes convex mixtures. Sending beta to one with fixed rho proves finite-n sharpness and unbounded IAT when no spectral ceiling is available.

## Originality

**qualified_supported_moment_extremal_packaging**. Reversible-chain spectral representations, variance bounding, and the Hausdorff-moment structure of autocovariances are classical or established prior work; Berg-Song in particular explicitly use the moment sequence viewpoint for estimation. Targeted searches did not locate the combined fixed-lag-one sharp theorem: simultaneous autocorrelation envelopes, finite-sample and asymptotic variance identification intervals, common finite-state extremizers, and the AR(1) factor as the minimum IAT under positivity. Since the proof becomes a short one-moment convexity problem once the spectral representation is exposed, equivalent moment-problem or operator-theoretic formulations remain a real attribution risk. Originality is therefore accepted only for the complete MCMC-oriented sharp packaging and finite-state attainability statement.

## Scientific value

**meaningful_exact_identification_region**. The theorem turns lag-one correlation plus an optional spectral ceiling into exact worst-case variance/ESS ranges at finite and asymptotic sample sizes, and clarifies that the familiar AR(1) plug-in is a best-case lower endpoint rather than a generic reconstruction under positivity.

## Independent checks

- Re-derived both autocorrelation envelopes directly from the one-moment spectral problem.
- Checked the finite-sample variance weights and the convex chord bound for asymptotic variance.
- Verified the two-state refresh-kernel and product constructions produce the claimed endpoint spectral measures.
- Checked that beta approaching one preserves finite-state irreducibility/aperiodicity for each beta<1 while the IAT diverges.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/sharp-lag-one-spectral-envelopes-reversible-chain-variance--530e5145f9f6
- https://doi.org/10.1214/ss/1177011137
- https://arxiv.org/abs/0806.2747
- https://arxiv.org/abs/1102.2171
- https://doi.org/10.1214/23-AOS2335
- https://arxiv.org/abs/2408.04155
## Limitations

- The lower envelopes require nonnegative observable spectrum (for example a positive reversible kernel), not reversibility alone.
- The spectral ceiling may be observable-specific and is treated as known.
- The result is deterministic conditional on rho and beta and does not analyze estimation error.
- Equivalent classical one-moment extremal results may exist outside MCMC terminology.
