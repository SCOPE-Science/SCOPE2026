# Scientific review: a signed macroscopic correlation law for Pareto-reset exclusion

## Correctness — PASS

For every \(\alpha>1\), the equilibrium age density of a Pareto renewal process is normalized and independent of the cutoff after rescaling. The ordinary symmetric exclusion process has an exact discrete-heat one-point equation. The two-site connected-correlation equation has a negative source only when the dual particles are adjacent. The reflection formula for the two-particle gap and heat-kernel estimates yield a uniform \(O((1+\log(1+t))/\sqrt{1+t})\) bound on the conditional pair covariance. This is sufficient to pass to the stationary-renewal mixture and rigorously obtain the displayed covariance kernel. The derivative of the error-function profile and a two-copy covariance identity establish strict signs for every pair of different scaled sites. Negative conditional pair covariance also supplies a uniform block-average variance bound, giving the stated \(L^2\) macroscopic profile convergence. The actual standalone Python program passed 70 deterministic checks, including duality and numerical sign evaluations; those finite tests support but do not replace the proofs.

## Originality — PASS, with qualification

The closest original work is Mishra and Basu, arXiv:2211.14120 (2022), whose stationary age mixture and density/current calculations are acknowledged. The 2019 single-Poisson-reset exclusion paper does not derive this Pareto, equal-time correlation kernel. The 2020 dichotomous-Poisson-reset exclusion paper examines spatial correlations on finite rings but explicitly lacks an analytic general pair correlation, and does not determine this infinite-step diffusive rescaling limit. Biroli et al., arXiv:2211.00563, explain known common-clock correlations in independent Brownian gases, not in an exclusion process. Santra and Singh, arXiv:2311.04097, treat a different random-average process. The exact conditional covariance decay, macroscopic Pareto kernel, and strict sign classification have not been located in these relevant primary sources or the queried mathematical result records. A broader hydrodynamic or mixture theorem might contain an equivalent specialization; priority remains subject to independent literature review. Failure to retrieve an identical statement is not, by itself, evidence of novelty.

## Scientific value — PASS

The original power-law resetting literature derives one-point density and particle-current statistics, and the adjacent dichotomous-reset literature expressly identifies spatial correlation analysis as nontrivial. The result answers the natural missing density-fluctuation question with a complete macroscopic covariance kernel, distinguishes exclusion-induced anticorrelations from the renewal-clock contribution, and proves a strict sign reversal on the same side of the reset front. It additionally proves non-self-averaging of the full macroscopic profile in the stationary regime. These qualitative and exact fluctuation consequences are not mere changes of notation, and the scaling \(\sqrt R\) is dictated by the diffusive front width, not an arbitrary numerical slice.

## Closest evidence and limits

- Mishra and Basu (2022), https://arxiv.org/abs/2211.14120, Sections 2–4 and 7; renewal equation (13) and step density profile.
- Sadekar and Basu (2020), https://arxiv.org/abs/2004.00951, Section 5.3, especially equations (77)–(89); finite-ring dichotomous-reset pair correlations.
- Basu, Kundu, and Pal (2019), https://arxiv.org/abs/1906.11801, Sections II–IV; single-Poisson-reset density and current results.
- Biroli et al. (2022), https://arxiv.org/abs/2211.00563, equations (4)–(6); known common-age correlations in a noninteracting resetting Brownian gas.

The theorem is restricted to positive finite-mean Pareto shape \(\alpha>1\), deterministic step resets, ordinary symmetric exclusion, and the infinite-lattice diffusive spatial scaling. It does not supply small-scale corrections or finite-ring crossover laws. Abstract-only inspection of related random-average-process work leaves a modest residual coverage risk.

Self-review: passed. Independent audit: not yet performed.
