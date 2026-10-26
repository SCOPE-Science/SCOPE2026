# Scientific review

## Correctness — PASS

The payoff difference exactly matches the stochastic synergy/discounting equation of Zhu et al. after setting \(G=n+1\), \(r/G=\kappa\), and \(p_n=cL^{-n}\). For integer \(n\ge2\), the second derivative is strictly positive on the entire closed unit interval. The endpoint sign, a fixed interior negative point, and this convexity imply the exact eventual equilibrium counts and hyperbolic signs. The low-cooperation boundary follows from \(F_n(u/n)\to\kappa e^{-\delta u}-1\); the upper noncritical and critical layers use respectively \(x=x_L+z/n\) and \(x=1-z/n\). The critical-amplitude result requires a different test scale \(1-x=C(1-\delta)^n/n\), on which the normalized payoff tends to \(\kappa-\delta C/(1+\delta)\). These sign-bracket arguments, not finite simulations, establish the infinite-n theorem. Exact rational sign certificates bound the two illustrated roots. Limits assume fixed parameters and sufficiently large integer group sizes.

## Originality — PASS, with residual priority risk

Zhu et al., arXiv:2408.02042 (first posted 2024-08-04), already derive the game payoff and analyze finite-group coexistence and bistability, including the full-cooperation stability condition. None of that is claimed as new. The new claim is the simultaneous growing-group/exponentially rare synergy limit, its sharp \(L=1+\delta\) transition, the macroscopic basin surviving exponentially rare synergy, and a second exponentially thinner layer at the exact critical amplitude. Peña and Nöldeke (2018), DOI 10.1016/j.jtbi.2018.08.004, Section 4 covers some games with size-dependent gains, so such dependence in itself is not new; their benefit-sharing analysis does not imply this mixed nonlinear stochastic rarity limit. Peña (2012) studies fluctuating *group sizes*, while Li et al. (2014) study structured-network weak-selection effects, and Llabrés et al. (2026) deterministic mixtures of interaction orders. The closest accessible full sources and mathematics-indexed search records did not supply the asserted rare-synergy trichotomy, but failed retrieval/search never establishes absolute novelty.

## Value — PASS

Rare synergistic interactions are a natural question for cooperation theory. The theorem shows that an exponentially vanishing fraction of synergistic groups can preserve a finite all-cooperation basin if and only if the rarity base lies below a precise nonlinear amplification threshold. The boundary case has two qualitatively different rates, \(n^{-1}\) and \((1-\delta)^n/n\), not captured by finite-group phase diagrams. This is an interpretable finite-parameter population-level transition, not an arbitrary numerical slice or routine restatement of fixed-n endpoint signs.

## Limitations and closest literature

The result holds for homogeneous deterministic mean-field dynamics with \(r=(n+1)\kappa\), \(\kappa>1\), fixed \(\delta\in(0,1)\), \(s>0\), and \(p_n=cL^{-n}\). No stochastic fixation law, uniform finite-size error, heterogeneous network or fixed-benefit asymptotic is claimed. Literature checks cover the full motivating paper and accessible supplement, primary treatments of nonlinear/group-size public goods, and directly searched mathematical records; priority beyond these remains uncertain.

Self-review: passed. Independent audit: not yet performed.
