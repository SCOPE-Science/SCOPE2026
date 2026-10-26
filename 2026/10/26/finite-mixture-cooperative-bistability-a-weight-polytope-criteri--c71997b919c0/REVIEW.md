# Scientific review

## Correctness — PASS
The payoff response is the finite weighted average of the published class-wise geometric-return payoff differences. Its second derivative is nonnegative throughout the physical interval and strictly positive whenever a genuinely nonlinear class has positive weight. The proof establishes the root ceiling, exact necessary-and-sufficient endpoint slope criterion, full stability sign pattern, mixing-weight feasibility criterion, and positive quadratic onset coefficient, including the rational three-order example. `verify.py` passed 1,555 exact-arithmetic consistency assertions. None of the finite checks is treated as proof for arbitrary mixture size.

## Originality — PASS, subject to priority risk
The closest primary work is Llabrés et al. (2026), Sections III.2 and Appendix A, which treats two interaction orders and displays a pairwise/triplewise bifurcation diagram. Peña (2012) analyzes variable group sizes under a common nonlinear rule; Zhu et al. (2024) treats stochastic synergy versus discounting at fixed group size. Archetti (2018) develops general Bernstein analysis rather than this mixture's explicit linear-weight feasibility and quadratic onset coefficient. A search for implications, aliases and stronger results did not identify a result simultaneously treating arbitrarily many classes with independent nonlinearities, the exact weight halfspaces, and the quadratic boundary coefficient. The underlying convexity and Taylor arguments are standard; independent derivation and unindexed-literature risks remain.

## Mathematical value — PASS
In empirically heterogeneous group interactions, mixing two orders is a restrictive idealization. The result states exactly which probability mixes can support an attracting active population *and* a stable all-cooperative population, shows this mechanism cannot create more complicated interior fixed-point multiplicity as interaction types proliferate, and quantifies the smallness of the resulting benefit-to-cost window near the critical mixture boundary. The strict rational three-order example demonstrates that the quadratic law is realized in a genuinely multi-order model, rather than merely a formal limiting expansion of pairwise/triplewise dynamics.

## Limits
The result is restricted to the specified finite exogenous class mixture, the common benefit-to-cost ratio, the deterministic well-mixed replicator equation, and strict (nondegenerate) bifurcation inequalities. It neither establishes structured-population dynamics nor asserts novelty beyond the inspected literature. No independent scientific audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
