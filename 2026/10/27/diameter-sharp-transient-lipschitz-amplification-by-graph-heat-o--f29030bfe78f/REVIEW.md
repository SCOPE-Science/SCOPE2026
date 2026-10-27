# Scientific review: diameter-sharp heat Lipschitz amplification

## Correctness — PASS
The proof reconstructs the Markov coupling upper estimate and strict finite-graph nonattainment, then specifies the rooted even/odd diameter trees, one-Lipschitz potentials, independent forward/backward Poisson clock representation, explicit finite branching error, and limit as branching grows. The proof handles both parities and every integer diameter at least two, for real or complex inputs. Its infinite claim rests on a Poisson-tail estimate, not on finite enumeration. The standalone verification script passed 64 finite quotient checks and 12 full-graph implementation comparisons.

## Originality — PASS (best available comparison)
Primary literature and actual semantic database searches were compared by implication rather than matching titles. Frank–Kovařík use continuous-edge metric trees; Bauer and collaborators study curvature-dimension heat gradients; Keller and collaborators give fixed-graph short-time asymptotics; Münch–Wojciechowski connect heat Lipschitz bounds to Wasserstein transport and curvature. None of the inspected relevant sections asserts an optimal fixed-diameter, all-graph envelope together with near-saturating trees in every diameter. The previously available balanced double-star computation covers diameter three, but not arbitrary diameters or the finite-graph strictness classification. The originalities of unindexed equivalents and inaccessible historical generations remain unverified.

## Mathematical value — PASS
For a finite Markov semigroup on a graph, positivity trivially bounds oscillation, but does not predict whether this is the best possible universal local-gradient bound. The finding determines the exact best bound using only graph diameter, shows that even trees asymptotically realize the full diameter at a vanishing heat time, and separates a sharp supremum over graphs from nonattainment on every finite graph. This informs graph-heat stability and Wasserstein amplification independently of individual spectral calculations.

## Closest literature and limits
The closest same-object historical finding is the diameter-three balanced-double-star formula (item `630448cd-1a9f-40db-a756-804046ff0031`). The semigroup/transport equivalence in arXiv:1712.00875 is relevant but does not dominate the sharp extremal diameter assertion. Literature search is not a novelty proof; no unindexed coverage is excluded. The result is specific to unit-rate combinatorial heat on finite unweighted graphs, with diameter fixed before the branching limit. It does not supply the exact time-norm of a particular graph, a uniform growing-diameter limit, or an independent certification.

Self-review: passed. Independent audit: not yet performed.
