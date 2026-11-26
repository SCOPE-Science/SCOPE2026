# Propagation speed and one-slide choices among minimum Desargues monitoring sets

## Finding

In the twenty-vertex Desargues graph, initialize ordinary power domination at round zero by observing the closed neighborhood of a minimum monitoring set. The minimum sets with sorted pair-distance profile \((3,3,4)\) finish in two additional synchronous forcing rounds, and those with profile \((2,3,5)\) finish in three. Each of the two types has 120 sets. From **every** minimum set, exactly two legal token slides preserve its propagation time and exactly two change it. In particular, imposing a two-round deadline leaves exactly two local slide choices per feasible state, rather than the four available if only eventual observation is required.

In the full relocation graphs of minimum sets, the faster type has fewer token-jump neighbors (13 rather than 17) and greater token-slide eccentricity (8 rather than 7). The degrees and eccentricities of the full graphs are known; the distinction here is how propagation speed relates to them and how a speed constraint changes the available local moves.

## Assumptions and scope

The vertices of the Desargues graph are all two- and three-element subsets of \(\{1,2,3,4,5\}\). Different vertices are adjacent if their sets are related by inclusion. Encode each subset by its integer mask in which bit zero denotes symbol one. For a seed \(S\), observe \(N[S]\) at round zero. In each later round, every observed vertex with exactly one unobserved neighbor observes that neighbor; the tests use the observed set at the start of the round. A monitoring set is minimum by cardinality. A token jump replaces one vertex by an unselected vertex; a token slide additionally requires adjacency of the exchanged vertices. Both moves here must end at another minimum set. All distances used for input profiles are base-graph distances; slide eccentricity is measured in the full slide graph on minimum sets, not in the subgraph constrained by a deadline.

## Proof

Use the established minimum-set census for the Desargues graph [1]. It identifies precisely the triples of profiles \((2,3,5)\) and \((3,3,4)\), each a single 120-set orbit under label permutations and complementation. The mask triples \((3,14,17)\) and \((7,10,17)\) have these respective profiles. The synchronous process, adjacency, and profiles are invariant under these automorphisms, so timing and local moves can be checked on these representatives.

For timing, the following table lists the newly observed masks in each round, including the full initialization set in round zero. A dash means that all vertices have already been observed.

| Seed | Round zero | Round one | Round two | Round three |
|---|---|---|---|---|
| \((3,14,17)\) | 3, 6, 7, 10, 11, 12, 14, 17, 19, 21, 25 | 5, 9, 18, 22, 26 | 13, 20, 24 | 28 |
| \((7,10,17)\) | 3, 5, 6, 7, 10, 11, 14, 17, 19, 21, 25, 26 | 9, 12, 13, 18, 20, 22 | 24, 28 | — |

Each positive-round entry is obtained by taking the union of the singleton sets \(N(v)\setminus A\) over masks \(v\) already in the observed set \(A\). Two masks are adjacent exactly when they differ in one bit. This checks that the slower seed is not complete after round two and the faster one is not complete after round one. Applying all available forces is fastest: if the observed set is larger, a force available in the smaller set either still applies or its target is already observed.

For slides, each representative has nine candidate ordered replacements since none of the selected vertices are adjacent and each has three neighbors. The table gives the candidates classified by the resulting triple's distance profile. A pair \(u\to v\) denotes the deletion of \(u\) and insertion of \(v\). The two first columns of replacements are the only legal ones by the minimum-set census.

| Seed | Time-preserving | Time-changing | Other candidates: resulting profile |
|---|---|---|---|
| \((3,14,17)\) | \(3\to7,\ 3\to11\) | \(17\to21,\ 17\to25\) | \(3\to19:(1,4,5);\ 14\to6,\ 14\to10:(2,2,4);\ 14\to12:(2,4,4);\ 17\to19:(1,3,4)\) |
| \((7,10,17)\) | \(10\to26,\ 17\to25\) | \(10\to14,\ 17\to21\) | \(7\to3:(2,2,4);\ 7\to5,\ 7\to6:(2,4,4);\ 10\to11,\ 17\to19:(2,3,3)\) |

The entries can be checked directly: for masks of the same size, the distance is 0 for identical masks, 2 if they differ in two bits, and 4 otherwise. For different sizes, the distance is their Hamming distance (1, 3 or 5). Indeed, the Hamming distance is a lower bound, and one may successively toggle bits that differ from the target by alternating deletions and insertions as needed to stay in sizes two and three. This attains the lower bound, also for masks of the same size. The two preserving and two changing moves therefore hold at every state by transitivity. Equivalently, there are 120 undirected slides within each speed class and 240 between them. Combining the timing result with the full-graph jump degrees and slide eccentricities in [1] gives the stated trade-off.

## Verification

The timing table is a direct singleton-neighbor calculation after initialization. The slide table tests each of the three neighbors of each selected mask in both representatives and uses three Hamming distances per resulting triple. The complete minimum-set census and the full-graph eccentricities and jump degrees are taken from [1]. The bundled programs also reproduce that baseline; they are not needed to check the two new tables given the census.

## Relationship to prior work and limitations

The minimum-set cardinality, both size-120 orbits and their distance profiles, and the full token-slide graph metrics and token-jump degrees are already stated in [1]. That result also describes antipodal pairs. They are not claimed here as new. The exact forcing times and the split of local slide choices by whether they preserve the forcing time are the focus here. Barrera and Ferrero [2] give general bounds for power domination on generalized Petersen graphs; Bjorkman et al. [3] give the general reconfiguration setting. These calculations apply only to the Desargues graph and the stated initialization convention. In particular, the result does not determine the global connected components of the deadline-restricted slide graph. No worldwide priority is asserted.

## References

1. *Two symmetry types and a unique antipodal pairing in Desargues power-domination relocation*. [Resultary record 9829d0d5cf3e](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-symmetry-types-and-a-unique-antipodal-pairing-in-desargues-p--9829d0d5cf3e/RESULT.md).
2. R. Barrera and D. Ferrero, *Power domination in cylinders, tori, and generalized Petersen graphs*, Networks 58 (2011), 43–49. DOI: `10.1002/net.20413`.
3. *Power Domination Reconfiguration*, La Matematica. DOI: `10.1007/s44007-025-00187-5`.
