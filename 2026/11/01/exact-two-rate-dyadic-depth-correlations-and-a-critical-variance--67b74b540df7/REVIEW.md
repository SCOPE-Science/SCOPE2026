# Scientific assessment

## Correctness — PASS

The proof directly derives the depth-chain transition kernel from affine uniform-cell dynamics and verifies the invariant geometric law. The two signed-row identities hold for every positive level and separately at the reinjection boundary, producing an exact covariance at every lag without a finite-state approximation. A quadratic solution of the countable Poisson equation proves the stationary martingale CLT; geometric stationary tails supply all moment conditions. Exact finite-time variance summation and a uniform Riemann-sum argument yield the near-critical crossover. The included SymPy checker independently verifies the delicate algebra, including the boundary and nontrivial finite examples. Scope is stationary, annealed, and \(0<q\leq1\).

## Originality — PASS within inspected evidence

The defining 2021 article's abstract and the same authors' accessible 2023 doctoral thesis were searched, and the thesis's complete model-and-density section was inspected, including its equations and proof of the density. The thesis's numerical correlation discussion concerns its different continuous-family map. Relevant literature searches addressed dyadic depth, leading-zero runs, renewal-chain covariance, random lazy doubling, and analogous exact Green–Kubo formulas. A separate existing calculation concerns the same map but studies covariance of the **bounded physical coordinate**; that result has a different transfer representation and does not determine the present unbounded dyadic-depth covariance, Poisson equation, or triangular critical crossover. Exact statement implication rather than wording was compared. Complete publisher article text was unavailable despite open-access attempts, so possible uninspected treatment remains a priority risk.

## Mathematical value — PASS

Dyadic depth measures logarithmic proximity to the fixed region where the identity branch induces long residence times. The exact two-rate covariance isolates the slow residence mode from a fast reset mode; the divergent integrated variance gives its critical time scale, and the finite-window transition resolves how the apparent \(N^2\) fluctuations cross to order \(N/q\). This is not a general-purpose Markov theorem restated with a parameter: it explicitly identifies a nontrivial observable for an established interval map, determines its complete covariance and makes the parameter/window transition quantitative. The source invariant density alone cannot recover these temporal results.

## Scope and priority risks

The stationary initial distribution and independent map choices are essential. No claim is made at the degenerate endpoint \(q=0\) or for fixed quenched histories. The inaccessible original article and unindexed prior calculations are publication-priority risks; no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
