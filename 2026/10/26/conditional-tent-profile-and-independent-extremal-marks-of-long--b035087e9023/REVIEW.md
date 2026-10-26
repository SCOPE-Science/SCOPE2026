# Self-review

## Correctness — PASS

The sole accepted scientific claim is the conditional marked long-gap theorem and its exact finite apex distribution in `RESULT.md`. Its proof reduces the gap event to a tilted unimodal-order-statistic model using the established valleys-of-first-arrivals lemma. The tilt \(g(S_L)g(S_R)\), the independent minimum-of-uniform moments and the finite apex weights are rederived without presuming the new claim. Their exact sum agrees with the 2026 gap probability, which is an independent normalization check. Conditional binomial and extreme-order-statistic limits give independent interior marks; uniform integrability follows from exact convergence of the nonnegative tilt expectations; the limit tilt turns independent exponentials into independent gamma variables. Finally, uniform fractions of those gamma endpoint minima give independent exponential endpoint arrival limits. Uniform order statistics give the tent law. All quantifiers refer to the specified local gap under iid arrival clocks. Exact arithmetic replay tests all lengths 1 through 100, all 5,050 marked weights and six selected endpoint moments. The finite checks support, but do not prove, the infinite limits.

## Originality — PASS, with uncertainty

The closest paper is M. Matijasevick, *Gaps between roots in ballistic deposition on a strip* (arXiv:2610.21094v1). Sections 2, 4 and 6 were read: it supplies the root/valley identification, a unimodality criterion, excursion probability kernels and unconditional gap-count limit laws. It does not state a conditional tent profile, a four-way jointly independent conditional mark limit, or exact peak-position weights. Mansour–Rastegar–Roitershtein (2019) addresses root counts; Billey–Burdzy–Sagan (2013) gives peak-set permutation enumeration. The latter results imply the unmarked normalization but not the continuous conditional mark law. Searches of relevant research records for valley gaps, conditional peak location, independent exponential endpoints and Gaussian/Gumbel marks found no covering statement. All those input results are credited as prior work. Residual historical risk: a general theorem on conditional random permutation mountains or order-statistic profiles might subsume the marked limit under different terminology; a failed search does not establish uniqueness.

## Mathematical value — PASS

The underlying 2026 paper identifies a Poisson regime for extremely rare long deposition-root gaps but characterizes gap *counts*, not the internal shape of a rare gap. The new theorem describes an entire conditional profile and four observables on three fluctuation scales, with explicit independent limiting distributions. The endpoint exponential rate is nontrivial: conditioning size-biases two endpoint-adjacent spacings from exponential to gamma before the valley clock is sampled. The exact finite peak-position law makes the asymptotic claim checkable and provides a finite-size localization statistic. The marked morphology has direct relevance to interpreting rare deposition gaps, rather than being an arbitrary parameter slice.

## Limitations and priority risks

The theorem addresses a specified oriented root gap, not the globally largest gap, and iid site-clock arrivals; no quantitative error rates are asserted. Classical binomial/Gumbel/order-statistic ingredients are not original. Full-text historical search cannot exclude a differently phrased conditional permutation-profile theorem. Independent human assessment of literature priority and mathematics remains outstanding.

Self-review: passed. Independent audit: not yet performed.
