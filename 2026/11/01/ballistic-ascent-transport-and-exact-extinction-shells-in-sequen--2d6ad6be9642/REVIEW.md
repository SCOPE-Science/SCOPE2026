# Mathematical review

## Correctness — PASS

The all-order proof derives the exact one-sweep recurrence with the correct sequential data dependency and zero-valued open boundaries. It proves the shift of every \(01\) ascent and the special case of ascent-free nonzero states. The rightmost-ascent count gives exact, disjoint time shells covering all \(2^n\) states. Direct Python and independent bitwise C++ exhaustive runs match the formulas for all states through orders 15 and 20, respectively. The code is reproducible but not an all-order proof.

## Originality — PASS (qualified)

The 2011 bi-threshold source gives a long-cycle construction on cycles and branched trees, not a path absorption-time census. The interior local update is Rule 178, so the 2026 full-text Rule-178 investigation was specifically compared; it studies periodic rings and coverings of sequential orders rather than one left-to-right open path and its transient shells. Related exact-cycle and finite-tree assertions concern different graph classes and invariants. Actual semantic database queries on both terminology systems returned no covering formula. Novelty can never be certified from unsuccessful searches alone; equivalent unindexed work remains possible.

## Mathematical value — PASS

Open-path termination is a natural missing contrast to the long-period examples at the same hysteresis thresholds. The theorem gives a complete finite-size first-absorption-time distribution, a sharp \(n\)-sweep upper bound attained by a positive fraction of all states, and a limiting negative-binomial deficit law. The structural transport of ascent interfaces explains why extinction is typical but still nearly as late as possible, rather than merely supplying a numerical table or a routine period bound.

## Closest literature and limitations

- Kuhlman–Mortveit–Murrugarra–Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974: same local bi-threshold rule; periodic cycles and branched-tree examples.
- Donoso-Leiva–Goles–Ríos-Wilson–Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797: Rule 178 alias and ring-order covering result; different topology and assertion.
- Macauley–Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412: recurrence equivalence under update-order changes, not transient distributions.

The result assumes a fixed ascending update order, open endpoints and un-clipped threshold three for persistence, and a uniform random initial state for its limit law. The novelty finding is not exhaustive or independently certified.

Self-review: passed. Independent audit: not yet performed.
