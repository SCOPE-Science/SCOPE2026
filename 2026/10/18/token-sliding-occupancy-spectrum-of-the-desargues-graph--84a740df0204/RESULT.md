# Token-sliding occupancy spectrum of the Desargues graph

## Finding

Let \(D\) be the twenty-vertex Desargues graph. For each integer \(1\le k\le10\), let \(\mathrm{TS}_k(D)\) be the graph whose vertices are the independent \(k\)-subsets of \(D\), with adjacency when one token is slid along an edge of \(D\) while independence is preserved. The following is the exact complete component census. In the fourth column, `a (b)` means \(b\) distinct components, each with \(a\) vertices.

| \(k\) | Independent sets | Sliding edges | Connected-component sizes (multiplicities) |
|---:|---:|---:|---|
| 1 | 20 | 30 | 20 (1) |
| 2 | 160 | 420 | 160 (1) |
| 3 | 660 | 2220 | 660 (1) |
| 4 | 1510 | 5580 | 1500 (1), 1 (10) |
| 5 | 1924 | 6870 | 1824 (1), 10 (10) |
| 6 | 1320 | 3840 | 970 (1), 33 (10), 1 (20) |
| 7 | 480 | 780 | 38 (10), 4 (20), 1 (20) |
| 8 | 115 | 60 | 4 (20), 1 (35) |
| 9 | 20 | 0 | 1 (20) |
| 10 | 2 | 0 | 1 (2) |

In particular, the **first loss of connectivity occurs at \(k=4\)**: precisely ten independent four-sets are immobile. In the canonical bipartite two-subset realization of \(D\), these are exactly the two-sided stars \(S_{x,s}\), consisting of the four two-subsets containing a fixed \(x\in[5]\) on one fixed side \(s\in\{0,1\}\). At \(k=5\) the ten nonlarge components are **each the one-subdivision of \(K_4\)**; at \(k=7\) and \(k=8\), every four-vertex component is a claw \(K_{1,3}\).

The exact radii and diameters of the nontrivial components, grouped by component order, are:

| \(k\) | Component order | Radius | Diameter |
|---:|---:|---:|---:|
| 4 | 1500 | 8 | 10 |
| 5 | 1824 | 9 | 10 |
| 5 | 10 | 3 | 4 |
| 6 | 970 | 8 | 10 |
| 6 | 33 | 4 | 5 |
| 7 | 38 | 4 | 6 |
| 7 | 4 | 1 | 2 |
| 8 | 4 | 1 | 2 |

All components of the same listed order have the same pair of metrics. Singleton components have radius and diameter zero. This statement is finite, exact and specific to \(D\); it makes no claim for arbitrary generalized Petersen or bipartite Kneser graphs.

## Assumptions and scope

Let \(\mathcal P=\binom{[5]}2\), where \([5]=\{0,1,2,3,4\}\). Label the vertices of \(D\) by \((s,p)\in\{0,1\}\times\mathcal P\). There is an edge between \((0,p)\) and \((1,q)\) exactly when \(p\cap q=\varnothing\); there are no same-side edges. The graph has twenty vertices and thirty edges, and its canonical correspondence with \(GP(10,3)\) is checked by an explicit vertex bijection in `verify.py`. The two-side description is also obtained by complementing the three-subsets in the usual incidence model \(H(5,2)\).

An independent set is a vertex set containing no graph edge. A sliding move replaces exactly one occupied vertex \(u\) by a neighboring, unoccupied vertex \(v\), provided the resulting set remains independent; token labels do not matter. Token jumping, token addition/removal, and recoloring are *not* permitted. For two independent \(k\)-sets \(I,J\), adjacency is equivalent to the three conditions \(|I\setminus J|=|J\setminus I|=1\), writing \(I\setminus J=\{u\}\) and \(J\setminus I=\{v\}\), and \(uv\in E(D)\). Components count labeled vertex subsets, not automorphism orbits.

## Proof

**Graph identification.** The stated disjointness rule has precisely thirty edges and every vertex has degree three. In the verifier, the explicit permutation `TO_GP` sends these thirty edges bijectively to the rim, spoke, and inner-star edges of the generalized Petersen presentation \(GP(10,3)\). This proves the identification rather than assuming it from a name.

**Exhaustive state space.** Represent each subset by a twenty-bit integer. The first generator recursively branches on the lowest remaining vertex: exclude it, or include it and remove all its neighbors from the available set. These mutually exclusive choices exhaust independent subsets without repetitions. The second generator independently selects each of the \(2^{10}\) subsets \(U\) on the first side, computes the prohibited neighbor positions \(N(U)\) on the second side, and selects every subset of the remaining second-side vertices. Thus both algorithms enumerate all independent sets, and they give exactly the same \(6212\) bit masks, including the empty set. The independence number is \(10\), with exactly two independent ten-sets (the two bipartition sides). Their nonempty cardinality counts are the second column of the first table. These independent-set counts alone have appeared in published independence-complex computations and are not the asserted novelty.

**Complete move and component enumeration.** For each occupancy \(k\), the first move generator tests every occupied \(u\) and each of its three neighbors \(v\), allowing a replacement exactly when the other \(k-1\) selected vertices have no edge to \(v\). Independently, the second move generator tests every unordered pair of enumerated \(k\)-subsets, retaining exactly those with symmetric difference of size two whose exchanged vertices are adjacent in \(D\). The two edge lists coincide exactly for every \(k\). Breadth-first traversal and an independent disjoint-set union computation return identical connected-component sizes. The total state and edge counts and component multiplicities are then those in the first table. Finally, complete breadth-first search from **every** vertex of every nonsingleton component computes every eccentricity and hence all radii and diameters in the second table. Thus no incomplete finite sample or heuristic graph exploration enters any asserted count or metric; `verify.py` performs all tests from the defining data and checks the displayed answers.

**The ten frozen stars.** For a fixed \(x\) and side \(s\), the set \(S_{x,s}\) consists of the four labels \((s,\{x,y\})\) with \(y\ne x\). Any vertex on the opposite side adjacent to a member of this star is adjacent to **two** members, because its label is a two-subset avoiding \(x\), leaving precisely two star labels disjoint from it. Sliding one token to that target therefore leaves another token adjacent to the target, so no move is legal. There are ten such stars. The exhaustive degree-zero check at \(k=4\) proves there are no other frozen independent four-sets; the remaining 1500 states form one component.

**The ten subdivided tetrahedra at occupancy five.** Adding tokens cannot make a member of \(S_{x,s}\) movable. Exactly ten vertices outside a frozen star are both unoccupied and nonadjacent to it: six same-side two-subsets not containing \(x\), and four opposite-side two-subsets containing \(x\). Their induced graph is the one-subdivision of \(K_4\): the four opposite-side vertices have degree three, and each same-side vertex has degree two and joins a distinct pair of those four. Thus the ten valid fifth-token positions, with star held fixed, form a ten-vertex token-sliding component isomorphic to that subdivided \(K_4\). No independent five-set contains two distinct four-token stars, because the union of two same-side stars has seven vertices, while opposite-side stars have eight vertices in their union. Hence these ten components are distinct. The exhaustive census verifies that the other 1824 five-sets form exactly one further component.

**Other component shapes.** The verifier checks the degree sequence and incidence pattern of every ten-vertex component at occupancy five, and directly checks degree sequence \((3,1,1,1)\) of every four-vertex component at occupancies seven and eight. No claim is made that all larger components share an isomorphism type merely because they share cardinality.

## Verification

Run `python3 verify.py` with the Python 3 standard library, without network access or input files. It reconstructs the graph and its explicit generalized-Petersen isomorphism, enumerates independent sets by two independent constructions, enumerates sliding edges by two independent tests, verifies all component counts by breadth-first search and union–find, checks the geometric frozen-star classification, the subdivided-\(K_4\) and claw components, and computes every required shortest-path eccentricity. Every asserted numerical result is an explicit assertion in the checker, and the final completion marker is `ALL_CHECKS_OK`.

## Relationship to prior work

Bonsma, Kamiński and Wrochna (2014) study independent-set reconfiguration under token sliding and jumping on **claw-free** graphs. The Desargues graph is cubic and bipartite, and every neighborhood forms an induced claw, so their graph-class theorem does not directly apply. Mütze and Su (2015) prove Hamiltonicity for bipartite Kneser graphs, including the host \(H(5,2)\); a Hamilton cycle through the twenty underlying vertices does not imply connectivity or component counts of configurations of multiple nonadjacent tokens. Avis and Hoang (2022) develop general structural results for \(\mathrm{TS}_k(G)\) but do not determine the occupancy spectrum or exact components of the Desargues instance.

Published independence-complex calculations for the Desargues graph already give its full independent-set face vector \((20,160,660,1510,1924,1320,480,115,20,2)\) and its topological invariants. Those static counts do **not** give the token-sliding edge relation, component multiplicities, geometric frozen classes, or reconfiguration distances. Published Desargues matching-complex homology and graph-metric Vietoris–Rips results concern different constructions. The claimed contribution is restricted to the **entire token-sliding component structure and its derived geometry and distances**, not a new count of independent sets or a new Hamiltonicity assertion.

## Limitations

The proof is an exhaustive exact computation for one twenty-vertex graph, supported by a short independently cross-checked program; it is not a structural recurrence covering larger bipartite Kneser graphs. The frozen-star and subdivided-tetrahedron phenomena have direct arguments, but the remaining component counts, connectivity statements, and diameters rely on the complete finite search. Relevant full-text searches found no previously published exact token-sliding census of this instance, but inaccessible, unindexed, or unpublished computations remain a genuine originality risk. The checker documents finite computation, with no claim of a closed-form family-level theorem.

## References

1. P. Bonsma, M. Kamiński and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1, publicly submitted 2014-03-03; Algorithm Theory—SWAT 2014.
2. T. Mütze and P. Su, *Bipartite Kneser graphs are Hamiltonian*, arXiv:1503.09175v1, publicly submitted 2015-03-31; Combinatorica 37 (2017), 1207–1219.
3. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861v1, publicly submitted 2022-03-31; Graphs and Combinatorics 39 (2023), article 59.
4. *The Desargues independence complex is \(S^4\vee\bigvee^5 S^5\)*, published `RESULT.md` at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563.
5. *Complete graph-metric Vietoris–Rips filtration of the Desargues configuration*, published `RESULT.md` at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-desargues--7d9e11af611c.
