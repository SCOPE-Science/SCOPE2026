# Independent mathematical audit

## correctness

PASS

Independently derived the Poisson-to-two-Bernoulli density ratios r_0=e^s(1-p)(1-q)<1, r_1=e^s(1-s+Delta), r_2=e^s(1-Delta/s), with s=p+q and 2pq=s(s-Delta). Feasible Delta<=s<=2Delta, with endpoints corresponding respectively to (Delta,0) and (Delta,Delta). At fixed Delta derivative of r1 is e^s(Delta-s)<=0, while derivative of r2 is e^s(1-Delta/s+Delta/s^2)>0. The global envelope is therefore max(e^Delta,e^(2Delta)/2), with crossover Delta=log2 and equality family exactly as claimed, including both at the crossover. Strict comparison with 1/(1-Delta) follows by log-convexity for first branch and decreasing (1-Delta)e^(2Delta) above log2. Independent grid of 2,499 parameter pairs showed at most 8.9e-16 floating overshoot; analytic derivative proof, not grid, covers the continuum and boundaries p=0/q=0.

## originality

PASS

The exact heterogeneous fixed-Delta envelope and log-two endpoint switch were not found in the inspected 2019/2020 original conjecture or 2021 homogeneous binomial density-ratio theorem. Prior homogeneous formulas give the candidate endpoints, but proving all interior heterogeneous pairs are dominated requires the monotone-in-s identity. Best-of-knowledge original complete natural two-Bernoulli layer; older 2005 relative-error paper remains a specific residual equivalence risk.

## value

PASS

This solves a natural complete smallest heterogeneous case of a specifically stated density-ratio conjecture, finding the exact extremizer and nontrivial log2 symmetry-breaking boundary. Those facts control sharp approximation error for a meaningful two-summand Poisson-binomial class and are not a mere generic calculus exercise when the fixed-Delta optimization and two competing masses are taken together.

The dated certificate retains the supplied scientific assessment, sources and limitations.
