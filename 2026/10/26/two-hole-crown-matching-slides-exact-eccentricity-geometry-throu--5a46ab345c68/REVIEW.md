# Self-review

## Correctness — PASS

The object is fixed-label deficiency-two matchings in \(\operatorname{Cr}_n\); its moves share an endpoint with the removed edge and retain cardinality. The explicit completion to a derangement on \(n+1\) symbols is invertible and converts each edge slide to a restricted swap of two images. This establishes the all-order enumerator, degree distribution, and parity bipartition with unequal parts. The \(S_n\)-orbit classification by the cycle containing the distinguished symbol, together with exhaustive BFS from one representative of each orbit, makes the finite eccentricity and distance classification mathematically exhaustive. Two independently organized implementations use different state representations and produce byte-for-byte equal detailed outputs for every order three through eight, including 133,496 states at the largest order. Critical assumptions and stopping boundaries are explicit: no extrapolation to order nine or beyond.

## Originality — PASS with residual publication-priority uncertainty

The general connectivity of token sliding below maximum independence size on connected claw-free line graphs follows from Bonsma–Kamiński–Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs* (2014), and is **not** newly claimed. Bousquet–Hatanaka–Ito–Mühlenthaler (2018) develop general shortest matching-reconfiguration results primarily under token jumping, not the exact crown token-slide metric. Avis–Hoang (2022) discusses general structural properties and bounds for token sliding, with no crown-specific diameter table. The OEIS derangement count is fully credited. The proposed new claim is the exact finite radius, diameter, orbit eccentricity and all-pairs distances through eight crown sizes, not the classical state count or generic connectivity. Exact earlier crown-specialized computations outside indexed literature remain possible.

## Mathematical value — PASS

For a natural family of one-edge-short-of-perfect matchings in a standard bipartite graph, this determines the complete local-motion metric up through the first 133,496-state case. The sharp even-versus-odd eccentricity split is mathematical structure, not just a vertex count: in even tested sizes, exactly the higher-degree states (coincident hole indices) form the center; odd tested sizes are self-centered. The complete all-pairs distance census and 15-orbit certification at order eight form a reproducible benchmark for extending the proposed pattern. The all-order parity imbalance additionally shows that these reachable solution spaces admit no Hamilton path. That elementary consequence is not presented as sufficient by itself to justify value.

## Closest literature and limitations

The exact finite cutoff is \(n=8\); an all-order diameter identity remains unproved, and unpublished computational tables could overlap. The matching-size convention is explicitly disambiguated from the usual term near-perfect. The verified two-implementation census does not constitute an independent external audit.

Self-review: passed. Independent audit: not yet performed.
