# Scientific review

## Correctness — PASS

Both stage equations reduce algebraically to the same scalar multiplier. The change of variable from a uniform stage fraction gives an exactly normalized density with moving endpoints. Leibniz differentiation gives the moment derivative for every positive exponent. Its sign establishes the order-independent unique minimum; beta-integral and Fatou limits establish exactly one crossing of moment one. Strict power-mean inequality orders all moment cutoffs. Uniform exponential-log moment bounds, the known negative logarithmic mean, and endpoint Laplace concentration give the two distinct asymptotics. A separate executable check reconstructs the algorithms and cross-checks the numerical values. The argument is not based on a finite sample in place of an infinite proof.

## Originality — PASS, with residual risk

The April 2024 Bochacik–Przybyłowicz original gives the common scalar multiplier, mean-square cutoff (its Fact 4), and almost-sure stability (its Fact 7). The October 2024 full preprint still explicitly proposes general moment-stability regions as future work. Neither supplied source states a universal minimizer for all \(p>0\), a strictly nested sequence of arbitrary-order cutoffs, nor the endpoint laws. The 2025 journal preview retains mean-square / asymptotic / probability stability as its three named notions but does not expose the full publication text. General stochastic \(\theta\)-methods study moment stability for different random recursions; the precise transformed density and moment frontiers here are not implied merely by that methodology. Priority outside the inspected works cannot be guaranteed.

## Mathematical value — PASS

This is a full one-parameter family of sharp stability cutoffs for the actual two randomized implicit schemes. It resolves an explicit further-analysis direction from the originating work on the natural scalar Dahlquist stability test, quantifies all positive moments rather than only the previously analyzed second moment, and identifies the nontrivial divergence between rare-event moment growth and almost-sure decay. Both extreme-order asymptotics specify where the effective stability window sits, including a logarithmically divergent low-order window. The result is more than a single numerical threshold.

## Closest literature and limitations

Source: Bochacik and Przybyłowicz, arXiv:2404.19059v1, 29 April 2024, Section 3, Facts 4 and 7; revised open author manuscript from October 2024; and Bochacik, Przybyłowicz, Stępień, BIT Numerical Mathematics (2025), DOI 10.1007/s10543-024-01050-9. Related p-th moment stability of stochastic \(\theta\)-methods is represented by Higham (2000) and Mao (2015), but those concern different stochastic-equation updates. Remaining priority risk: a potentially equivalent analysis outside the retrieved primary works and the inaccessible complete 2025 journal version. Mathematically the theorem does not classify the complex stability plane or coupled systems.

Self-review: passed. Independent audit: not yet performed.
