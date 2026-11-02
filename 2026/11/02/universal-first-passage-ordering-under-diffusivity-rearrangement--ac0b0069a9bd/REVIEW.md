# Review: Universal first-passage ordering under diffusivity rearrangement and renewal resetting

## Correctness — PASS

The theorem has one precise mathematical object: a one-dimensional optical-pullback diffusion with an absorbing left endpoint, a reflecting right endpoint, an independent iid positive renewal reset clock and a prescribed equimeasurable spatial diffusivity histogram. The coefficient bounds make the optical map strictly increasing and invertible even for measurable media. The material inventory fixes the full optical length; it leaves only the prefix optical distance from the target to the fixed launch site variable.

The rearrangement bound is sharp by layer-cake inequalities. Its stochastic extension follows from the explicit monotone and nonexpansive one-sided Skorokhod reflection map, with the same Brownian driving path and reset intervals in every comparison. Every attempted cycle has positive absorption probability; almost-sure completion needs no waiting-time moments. Sliding a sorted optical profile through its full permissible range yields every intermediate law continuously. Strict inequality for distinct optical positions follows by a no-reset Brownian-path event of positive probability. The standalone checker passes 66,696 finite tests, including independent Poisson-transform diagnostics. The infinite-dimensional claims rest on the written proof, not on sampling.

## Originality — PASS, with residual priority risk

The closest source is Menon Jr. and Anteneodo, *Random search with resetting in heterogeneous environments*, arXiv:2408.04726v1 (first public 2024-08-08), whose section III.1 Eq. (19) explicitly gives the optical transform and a closed **mean** first-passage time for Poisson resetting. The monotone Poisson mean and its optical normalization are consequently prior deductions, **not** new contributions. That paper discusses arrival-time distributions as future work. The assessed addition is the *full* stochastic ordering of completion-time laws under every common independent renewal-reset protocol, the sharp simultaneous material-arrangement optimum and the realization of the complete set of possible laws.

Pal and Prasad, arXiv:1812.03009 (2018), provide a renewal survival treatment for homogeneous diffusion with two absorbing interval ends; sections II and the appendices were examined. Linn and Lawley's 2023 work covers broad resetting distributions in a high-reset asymptotic regime. Barbini and Giuggioli's 2024 lattice heterogeneous setting involves a different reset mechanism; the complete text was not inspected, so it remains a source-access uncertainty. Searches for optical-coordinate, rearrangement, equimeasurable medium, survival dominance, and general renewal equivalents found no directly covering statement. **Residual risk:** a broader unindexed comparison or rearrangement theorem may already imply the claimed classification. Negative search results alone are not certification of novelty.

## Mathematical value — PASS

A fixed physical distribution of diffusivities models a fixed inventory of transport materials. The problem of where to place this inventory to optimize first-arrival times is physically natural. Rather than minimizing one computed average or choosing a resetting rate, the theorem identifies a common design that minimizes every monotone completion-time performance criterion across **all independent renewal resetting protocols**. It also classifies the exact continuum of attainable distributions. This is a structural optimization result and not a parameter substitution or a recomputed mean table.

## Boundaries and verification

The optical-coordinate interpretation is essential for nonsmooth diffusivities; other interface prescriptions can yield different results. Resetting must be independent of the search path, spatial profile and individual arrival history, with the same launch/reset position and physical material histogram. The model does not address finite-time density estimation or multiple absorbers. The finite checker tests only representative arrangements and Brownian-path samples; it is not an exhaustive or independent scientific proof. A separate publication-priority review is advisable.

Self-review: passed. Independent audit: not yet performed.
