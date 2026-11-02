# Independent mathematical audit

## correctness

PASS

For iid cycles with Exp(1) run/rest marginals and fresh fair run signs, stationary same-run sampling yields E[W0 Ws]=v² E[(U-s)+]/E(U+V)=v² exp(-|s|)/2, so the full lag-MSD v²(t−1+exp(−t)) is unchanged by pairing. The analytic regenerative characteristic exponent solves E[exp(−lambda(U+V))cosh(kvU)]=1: the k⁴ coefficient has 24B=v⁴/E(T)[E(U⁴)−6 E(U²)/E(T) E(U²T)+3(E(U²)/E(T))² E(T²)]. With both margins Exp(1), comonotone pairing gives cumulant rate −12v⁴, countermonotone pairing gives (π²+12ζ(3)−24)v⁴/2, and the Bernoulli pairing mixture is affine, crossing once at θ=24/(π²+12ζ(3)). Exact logarithmic beta integrals E(UV)=2−ζ(2), E(U²V)=6−2ζ(2)−2ζ(3) give the endpoint constants. Independent direct high-precision integration confirms the two endpoint coefficients and θ≈0.98788656624871, and the rational bound π>157/50 plus five zeta-series terms establishes strict positivity. Renewal analyticity/nonarithmetic finite exponential moments justify differentiation of leading log-MGF through fourth order; unfinished boundary cycles do not alter rates. The supplementary finite root checks cannot prove this infinite-time theorem.

## originality

PASS

Datta/Beta/Großmann arXiv:2406.15277 develop renewal-theoretic velocity correlations and diffusivity with run/turn marginal laws, not the evaluated within-cycle copula fourth-cumulant sign reversal. Santra/Olsen/Gupta arXiv:2408.16643 develop fourth cumulants for phase switching but use separately generated phase sojourn kernels rather than these paired within-cycle couplings. Niemann/Kantz 2008 treats the broader general class of coupled CTRW multipoint functions, so the renewal transform is not new; its full text was not inspected and implicit coverage remains possible. Resultary's direct semantic search found neighboring stationary renewal correlation results, not this exact joint equality/sign boundary. The precise comparison concerns the evaluated counterexample, not ownership of the general renewal method; no absence-of-index proof of novelty is claimed.

## value

PASS

This natural statistical-identifiability construction shows that entire mean-square displacement and full stationary velocity autocorrelation fail to distinguish models whose asymptotic excess-kurtosis sign differs. Its one-parameter sharp threshold is a motivated nontrivial higher-order transport invariant. The critical mixing rate describes a concrete boundary rather than arbitrary parameter tuning; it does not assert finite-time kurtosis signs or estimation power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
