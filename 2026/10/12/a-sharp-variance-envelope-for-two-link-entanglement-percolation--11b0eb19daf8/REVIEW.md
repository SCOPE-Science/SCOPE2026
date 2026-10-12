# Scientific review
## Correctness — PASS
The full assertion is a scalar optimization over all probability measures on \([0,1]\) with mean \(1/2\) and a specified variance. The two moment constraints on the CDF are derived by layer-cake integration including atoms. Both candidate CDFs meet them exactly. The affine-clipping inequality expands the difference of quadratic objectives into a nonnegative square and another nonnegative sign-controlled integral, proving global minimality and uniqueness. The transition, endpoint cases and lattice crossing are derived exactly. Independently recomputed finite rational and random-discrete checks are reported in the verification document; they do not certify the infinite-law claim by enumeration.

## Originality — PASS, with residual priority risk
The motivating 2026 paper supplies the swapping rule, the general expected-minimum identity, and uniform/location-scale examples, but not a hard-support mean-and-variance extremal over all laws. The classical Gini mean-difference equivalence and general dispersion inequalities are acknowledged; they do not by themselves yield the physical-support endpoint-atom branch. Related 2025–2026 Wasserstein-constrained Gini optimization has different admissible laws and a reference-distribution constraint, and the inspected statements do not explicitly supply this compact-support extremal. A 2008 finite-interval Gini survey is relevant but inaccessible beyond its abstract; equivalent prior specializations are possible. No claim of complete global priority certainty is made.

## Value — PASS
The quantum link model has a natural bounded SCP parameter, so optimizers must respect \([0,1]\); unconstrained Gini-moment inequalities cannot capture the endpoint-atom phase for \(v>1/12\). The exact unique-law classification locates the physical breakdown of the ordinary uniform-extremizer picture, while the sharp triangular-lattice variance cutoff makes a falsifiable protocol-level guarantee without assuming a parametric probability family. The result does not purport to solve global LOCC optimality.

## Closest literature and limitations
The source's two-link rule, independence condition and integral formula are inputs, not discoveries; its numerical width crossover addresses a different comparison. The separate classical Gini program and the 2008 unavailable survey create residual priority risk. The proof covers arbitrary input SCP laws with mean exactly \(1/2\), but not correlated edges, general means, multi-hop outputs or all quantum protocols.

Self-review: passed. Independent audit: not yet performed.
