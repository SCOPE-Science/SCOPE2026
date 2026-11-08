# Scientific review: a cubical bridge geometry for subdivided stars

## Correctness — PASS

The proof classifies every independent set with \(m-1\) tokens by center occupancy and checks every original-tree edge. Cube states have exactly one missing arm; each bridge state has the center and all but two leaves. The only inter-cube switches use one-hot cube corners and a degree-two bridge. An explicitly defined target potential is globally \(1\)-Lipschitz; direct routes attain it. The three pair types are bounded for the diameter. The bound \(2m\) is attained by states differing in precisely two leaves. Both standalone implementations enumerate original independent sets and legal slides independently; Python checked \(m=3,4,5,6,7\), and C++17 checked \(m=3,4,5,6,7,8,9\), including all ordered-pair distances.

## Originality — PASS, qualified

Demaine et al. (arXiv:1406.6576) supply tree reachability and polynomial-length sequences. Hoang, Khorramian and Uehara (arXiv:1806.08291) **already solve the shortest-sequence algorithmic problem for all spiders**; it would be incorrect to present that capability as new. Avis and Hoang (arXiv:2203.16861) study general token-sliding graph structure. The actual assessed contribution is the *complete* uniform depth-two spider reconfiguration graph (isometric cubes joined over all pairs), its symbolic metric and sharp global diameter. These statements are not given in the inspected relevant parts of those primary texts. Search of indexed published research records found no statement equivalent to the full conclusion, but prior unindexed work could exist. Full priority confirmation requires broader independent literature review.

## Value — PASS

There is a motivated global metric gap beyond generic polynomial-time reachability: the exact graph of feasible configurations and worst-case shortest route remain nontrivial even for symmetric spiders. The full isomorphism exposes the central bottleneck as a subdivided \(K_m\) bridge network grafted onto \(m\) high-dimensional cubes. The sharp diametral pair has symmetric difference two but requires \(2m\) legal slides, quantifying a substantial structural detour in a natural family. This is an infinite-family classification, not a parameter renaming or isolated finite count.

## Limitations and comparison risk

The theorem is limited to size \(m-1\) independent sets on uniformly subdivided \(m\)-arm stars, \(m\ge3\), under token sliding. Finite programs are corroboration, not infinity proofs. Some literature establishes stronger *algorithmic* coverage; no new shortest-sequence algorithm for generic spiders is claimed. Indexed search and relevant accessible primary text do not guarantee uniqueness. No independent scholarly audit has been performed.

Self-review: passed. Independent audit: not yet performed.
