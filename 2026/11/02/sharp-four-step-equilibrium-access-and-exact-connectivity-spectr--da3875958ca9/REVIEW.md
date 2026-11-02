# Self-review

## Correctness — PASS

The proof fixes a pure-equilibrium cube vertex and uses the three Hamming-distance layers to give every profile a strict best-response path to *some* equilibrium of length at most four; this is valid even if other equilibria exist. The displayed twelve arcs form precisely one orientation of every cube edge and yield a forced four-step shortest route from profile \(2\) to the unique sink \(4\). Inclusion–exclusion, using the independent sets of the cube, gives \(3134\) orientations with at least one sink. The complete integer enumeration and independent breadth-first/Floyd–Warshall checks yield the distance histogram \((258,644,1512,720)\) and \(2492\) connected orientations. The package includes and successfully replays the actual verification program. These finite checks do not purport to prove a larger-player theorem.

## Originality — PASS, subject to source-access uncertainty

The 2011/2013 Fabrikant–Jaggard–Schapira weak-acyclicity theorem for strict two-by-two-by-two games is known and expressly excluded as a novelty claim. That existence theorem supplies no numeric sharp distance, distribution, or exact count of connected orientations. The complete primary text of Johnston–Savery–Scott–Tarbush, including its Appendix H, reports approximate simulations and asymptotic results rather than this exact three-player census or universal four-step bound. The fully accessible Heinrich et al. 2023 article discusses stochastic/clockwork activations and asymptotic convergence instead. Searches for exact counts, dimension-three oriented-cube shortest paths, and stronger coverage in published research records and primary literature did not find the same formula. The potentially relevant 1993 Bollobás–Gotsman–Shamir paper was accessible only at abstract level; an undocumented earlier tabulation is an explicit residual priority risk, not something silently treated as inspected.

## Mathematical value — PASS

The length-four bound answers a precise worst-case accessibility-time question at the smallest multi-player binary scale where best-response cycles can coexist with a pure equilibrium. The exact count and distance spectrum turn a motivating small-game simulation question into an exhaustive conditional probability law, separating existence, distance and strong connectivity. This is not a rephrasing of weak acyclicity: the latter asserts some finite path without its sharp universal length, distribution of maximum distances, or every-equilibrium reachability frequency. The calculation is natural for benchmark testing of adaptive equilibrium methods, while making no claim about actual convergence times under exogenous playing sequences.

## Closest literature and limits

Main comparison: Johnston et al., arXiv:2309.10609 (2023), especially §3 and Appendix H. Essential known special case: Fabrikant et al., arXiv:1108.2092, Lemma 4.6 (2011 preprint). Other comparison: Heinrich et al., DOI 10.1007/s00182-023-00837-4 (2023). Access-limited risk: Bollobás et al., DOI 10.1007/BF02784059 (1993), abstract only. The result concerns independently oriented best-response comparisons for exactly three labeled binary players and existential improvement paths, not arbitrary update schedules.

Self-review: passed. Independent audit: not yet performed.
