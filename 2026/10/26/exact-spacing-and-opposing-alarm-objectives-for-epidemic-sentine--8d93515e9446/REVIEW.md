# Scientific assessment

## Correctness — PASS

The finding supplies one coherent theorem, simultaneously specifying the exact no-alarm probability, strictly convex gap statistic, equal-gap optimizer, concentrated-gap worst case, placement-invariant mean, and the exact opposite two-monitor corroboration ordering. Every quantifier is explicit: integer \(n\ge3\), integer \(1\le k<n\), and real \(0<p<1\). Uniform seeding includes monitor vertices. The two bordering gap routes are edge-disjoint, so their failure probabilities multiply. The strict second difference \((\ell+2)p^{\ell+1}(1-p)^2\) is positive for every admissible parameter. Discrete exchanges establish both extremal equality cases. Component reachability proves the mean formula independently, and \(X\in\{0,1,2\}\) supplies the two-monitor duality. The bounded enumerator agrees with the proof on all checked finite instances; the proof, not enumeration, establishes universal scope.

## Originality — PASS, subject to remaining literature risk

Closest inspected primary work is Leskovec et al. (2007), an all-network outbreak-detection framework with submodularity and near-optimal algorithms. It covers the general *objective type* and should not be described as unrelated. Its accessible 29-page report's placement sections and theorem statements do not give the exact gap-by-gap cycle probability, strict all-parameter extremal equality cases, or corroboration reversal. Kiss et al. (2005) concern contact tracing dynamics, Miller (2008) optimizes over infectivity/susceptibility distributions, and Christakis and Fowler (2010) study friendship sensors and early flu detection; none of the inspected material establishes the particular exact cycle claims. Exact placement on paths, in accessible earlier results, has different topology, source support, and monitor count; it does not imply this cyclic \(k\)-sensor theorem. The searches and full-text comparison are evidence of a literature gap, not mathematical proof of global novelty. An equivalent result under reliability coverage or cyclic facility-location language remains possible and warrants independent checking.

## Mathematical value — PASS

The finding provides a natural complete optimization theorem rather than a parameter-substitution calculation. It resolves *all* ring sizes, sensor budgets and interior edge-transmission parameters without numeric optimization, characterizes every optimal and worst placement, and identifies a real surveillance design tension: moving two monitors apart improves the probability of at least one detection but reduces the probability that both witness the same outbreak. Placement-invariance of expected alarm volume shows why an expectation-only monitoring metric cannot see this difference. The explicit six-site rational example makes the distinction concrete. No claim is made for broader epidemic models.

## Scientific limitations and closest literature

The precise graph, uniform all-vertex seeding, independent undirected bond model, passive monitors, and eventual detection are essential. An unexamined equivalent result in older exact cycle-coverage theory remains a bibliographic risk, as does any uninspected result with stronger assumptions that specialize to this setting. Neither the small-instance verifier nor a database search proves novelty or independence.

Self-review: passed. Independent audit: not yet performed.
