# Token-sliding occupancy spectrum of the Desargues graph

## Finding

Let \(D\) be the twenty-vertex Desargues graph. The vertices of \(\mathrm{TS}_k(D)\) are the independent \(k\)-subsets of \(D\), and its edges are the legal slides of one token along an edge of \(D\). The complete component census is as follows, with \(a\,(b)\) denoting \(b\) components of order \(a\).

| \(k\) | Independent sets | Sliding edges | Component orders (multiplicities) |
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

The first loss of connectivity is at \(k=4\). The ten isolated states are the stars \(S_{x,s}\) defined below. At \(k=5\) the ten smaller components are each the one-subdivision of \(K_4\); at \(k=7,8\) every four-vertex component is a claw.

All nonsingleton components have the following radii and diameters. Singleton components have radius and diameter zero.

| \(k\) | Order | Radius | Diameter |
|---:|---:|---:|---:|
| 1 | 20 | 5 | 5 |
| 2 | 160 | 5 | 7 |
| 3 | 660 | 8 | 9 |
| 4 | 1500 | 8 | 10 |
| 5 | 1824 | 9 | 10 |
| 5 | 10 | 3 | 4 |
| 6 | 970 | 8 | 10 |
| 6 | 33 | 4 | 5 |
| 7 | 38 | 4 | 6 |
| 7 | 4 | 1 | 2 |
| 8 | 4 | 1 | 2 |

## Assumptions and scope

Label the twenty vertices \((s,p)\), with \(s\in\{0,1\}\) and \(p\in\binom{\{0,1,2,3,4\}}{2}\). Edges join opposite sides whose two-subsets are disjoint. A slide replaces one occupied vertex by an unoccupied neighbor, and the resulting set must still be independent. Tokens are indistinguishable; the states are actual vertex subsets, not automorphism orbits. This graph is the usual incidence graph between two- and three-subsets of a five-set after complementing the three-subsets. The included checker verifies a vertex bijection to the rim, spokes and inner-star presentation \(GP(10,3)\).

## Proof

**Exhaustive state and move census.** The spokes in the generalized Petersen presentation form a perfect matching, so an independent set contains at most ten vertices. The checker enumerates each \(k\)-subset once for \(1\le k\le10\) and discards those containing both endpoints of any host edge. The two independent ten-sets are the two bipartition sides. For a state represented by a bit mask, toggle the two endpoints of each host edge. If the result lies in the same independent size layer, exactly one endpoint was occupied, and this is a legal slide; conversely each legal slide is such a toggle. The checker also counts slide edges by inspecting each unordered pair of states for symmetric difference equal to a host edge mask. Components are found by breadth-first search. From every vertex of each nonsingleton component, a fresh breadth-first search finds every distance, hence that vertex's eccentricity. Minimizing and maximizing these eccentricities gives the radius and diameter, respectively. The checker asserts the full census, the agreement of all radius–diameter pairs at each fixed occupancy and component order, and every entry of both tables.

**Frozen stars.** Fix \(x\) and side \(s\), and let \(S_{x,s}\) contain all four vertices on side \(s\) whose two-subset contains \(x\). Every possible slide target for a member of \(S_{x,s}\) is adjacent to two star members, since its label avoids \(x\) and excludes two of the four possible partners for \(x\). Thus no such slide is legal, and this remains true after adding a fifth token. The checker finds that the ten stars are all the isolated states at \(k=4\).

**Subdivided tetrahedra and claws.** A fifth token added to a fixed star has ten allowed positions: six same-side two-subsets avoiding \(x\) and four opposite-side two-subsets containing \(x\). Each same-side vertex is adjacent to exactly two of the four opposite-side vertices, and these six pairs comprise the edges of \(K_4\). The slide graph of the fifth token is therefore the one-subdivision of \(K_4\). A five-set cannot contain two distinct stars, whose union has at least seven vertices. This gives ten distinct components, exactly the smaller ones at \(k=5\). The exhaustive search also checks the incidence geometry of these components and the degree sequence \((3,1,1,1)\) of every four-vertex component at \(k=7,8\).

## Verification

Run `python3 verify.py` with the Python 3 standard library. It prints both census and metric data, finishing with `ALL_CHECKS_OK` only after matching every table entry and checking the stated small-component shapes.

## Relationship to prior work and limitations

The independent-set counts are the known face vector of the Desargues independence complex; the contribution here is the full slide graph component and metric census. The separate calculation for minimum independent dominating sets concerns a restricted 100-state induced subgraph, not the full 1320-state graph at occupancy six. The Hamiltonicity of bipartite Kneser graphs describes the host graph, not multi-token configurations. The Desargues graph is not claw-free, so claw-free reconfiguration results do not apply. The computation is exhaustive for this one natural graph, not a reconfiguration classification for larger bipartite Kneser or generalized Petersen graphs. No claim is made that larger components of the same order are necessarily isomorphic.

## References

1. P. Bonsma, M. Kamiński and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359.
2. T. Mütze and P. Su, *Bipartite Kneser graphs are Hamiltonian*, arXiv:1503.09175, Combinatorica 37 (2017), 1207–1219.
3. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, Graphs and Combinatorics 39 (2023), article 59.
4. *The Desargues independence complex is \(S^4\vee\bigvee^5 S^5\)*, [indexed result](https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563).
5. [Indexed result on minimum independent domination on the Desargues graph](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-minimum-independent-domination-on-the-desargues-graph-has-five-d--cf69f6b23fb8).
