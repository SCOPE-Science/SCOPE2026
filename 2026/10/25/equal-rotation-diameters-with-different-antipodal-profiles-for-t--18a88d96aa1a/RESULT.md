# Equal rotation diameters with different antipodal profiles for the cube and Wagner graph

## Finding

Let \(Q_3\) be the graph on \(\{0,\ldots,7\}\) with edges between integers whose binary expansions differ in one position. Let \(M_8\) be the Wagner graph on \(\mathbb Z/8\mathbb Z\), with edges between \(i\) and \(i+1\) or \(i+4\), read modulo \(8\). For a connected graph \(G\), let \(\mathcal R(G)\) be the graph of its rooted elimination trees (equivalently, of its maximal proper tubings), with edges given by single tree rotations (equivalently, single tubing flips).

Both rotation graphs have radius \(17\) and diameter \(20\), but have different eccentricity and distance profiles:

| Invariant | \(\mathcal R(Q_3)\) | \(\mathcal R(M_8)\) |
|---|---:|---:|
| Elimination trees | 16,752 | 17,568 |
| Rotation edges | 58,632 | 61,488 |
| Base-graph automorphisms | 48 | 16 |
| Orbits of elimination trees | 355 | 1,098 |
| Rotation-graph radius | 17 | 17 |
| Rotation-graph diameter | 20 | 20 |
| Trees of eccentricity 17 | 1,368 | 976 |
| Trees of eccentricity 18 | 8,280 | 5,536 |
| Trees of eccentricity 19 | 6,336 | 10,800 |
| Trees of eccentricity 20 | 768 | 256 |
| Unordered pairs at distance 20 | 624 | 168 |

For \(Q_3\), 343 elimination-tree orbits have size 48 and 12 have size 24. For \(M_8\), all 1,098 orbits have size 16. In both graphs exactly 16 orbits consist of eccentricity-20 trees, yet their numbers of such trees are in the ratio three to one.

The complete unordered distinct-pair distance distributions, with rows indexed by exact shortest rotation distance, are:

| Distance | \(Q_3\) | \(M_8\) |
|---:|---:|---:|
| 1 | 58,632 | 61,488 |
| 2 | 230,712 | 241,824 |
| 3 | 653,904 | 685,152 |
| 4 | 1,488,696 | 1,559,056 |
| 5 | 2,890,800 | 3,028,464 |
| 6 | 4,967,280 | 5,207,440 |
| 7 | 7,701,408 | 8,089,664 |
| 8 | 10,887,384 | 11,479,368 |
| 9 | 14,100,984 | 14,957,024 |
| 10 | 16,745,640 | 17,918,640 |
| 11 | 18,179,424 | 19,692,096 |
| 12 | 17,940,888 | 19,737,008 |
| 13 | 15,963,096 | 17,885,520 |
| 14 | 12,638,352 | 14,472,144 |
| 15 | 8,638,488 | 10,188,936 |
| 16 | 4,806,864 | 5,908,024 |
| 17 | 1,941,288 | 2,528,288 |
| 18 | 437,856 | 620,288 |
| 19 | 34,056 | 47,936 |
| 20 | 624 | 168 |
| **Total** | **140,306,376** | **154,308,528** |

## Assumptions and scope

Graphs are finite, simple, undirected, and vertex-labeled exactly as above. An elimination tree of a connected induced subgraph on a vertex set \(S\) is obtained by choosing a root \(v\in S\), removing \(v\), and recursively choosing an elimination tree for each connected component. Child order is immaterial. Each nonroot vertex defines a tube consisting of the vertices in its descendant subtree. An edge of \(\mathcal R(G)\) swaps the parent-child choices along one elimination-tree edge with the usual induced-component reattachments. Graph distance counts individual rotations, not arbitrary permutations or simultaneous rotations. Eccentricity is the maximum shortest-path distance to another elimination tree. The comparison is confined to the two specific eight-vertex base graphs, not to all cubic graphs.

## Proof

**Completeness of states.** For every nonempty induced vertex set \(S\), the recursion tries every root \(v\in S\) and every product of elimination trees on the connected components of \(G[S\setminus\{v\}]\). Every elimination tree has exactly one such root and a unique choice on each component, so the recursion lists all states without duplication. Its proper descendant tubes are connected and pairwise nested or disjoint nonadjacent. Conversely, each maximal proper tubing has a spine with singleton vertex labels, recovering its unique elimination tree; the standard tubing–spine correspondence is stated in [1]. Thus this recursion enumerates the complete vertex set of the rotation graph.

**Completeness of moves.** Each maximal proper tubing has exactly seven tubes. Delete each of the seven tubes in turn and index the remaining six-tube collection, called a ridge. Every ridge encountered has exactly two completions among the enumerated maximal tubings. Connecting those completions therefore constructs every tubing flip and no other edge, by the defining flip relation [1]. The verifier independently recovers a parent array from each tubing and rotates each of its seven parent-child edges. When rotating parent \(u\) below child \(v\), a former child subtree of \(v\) is transferred to \(u\) exactly when that subtree contains a vertex adjacent to \(u\) in the base graph. The resulting neighbor set agrees with the ridge construction at every state. This independently checks the equivalence of the two edge descriptions [2,3].

**Shortest distances.** For each base graph, test all \(8!=40{,}320\) permutations of the vertex set and retain exactly those preserving all base edges. Apply each retained automorphism to the seven tubes of every state to identify full orbits. Breadth-first search from one representative of every orbit gives the exact distances to every state. Distances and eccentricities are invariant under the automorphism action, so multiplying each representative's ordered distance counts by its orbit size and dividing positive-distance counts by two gives the exact unordered-pair distribution. The resulting profiles are the displayed numbers. All breadth-first searches reach the entire relevant rotation graph, and the unordered-pair totals equal \(\binom{16752}{2}=140306376\) and \(\binom{17568}{2}=154308528\). Minimum and maximum eccentricity are respectively \(17\) and \(20\) in both graphs, proving the stated radii and diameters.

## Verification

Run the supplied standard-library Python program from the extracted directory:

`python3 verify_tubings.py`

It reconstructs both base graphs, generates all maximal tubings recursively, constructs the full ridge-adjacency graph, compares every one of its edges to an independently implemented parent-child rotation, enumerates the full base-graph automorphism groups, and performs orbit-weighted exhaustive breadth-first searches. It checks all stated counts, all eccentricities, and all 20 positive-distance pair multiplicities; a successful execution prints `VERIFY_OK`. The data above have additionally been checked by an all-source breadth-first-search implementation that independently enumerated each unordered pair without orbit weighting.

## Relationship to prior work

Manneville and Pilaud [1] supply the graph-tubing framework and general diameter bounds, namely \(\max(|E(G)|,2|V(G)|-20)\leq\operatorname{diam}(\mathcal R(G))\leq\binom{|V(G)|}{2}\), but not the two base-graph-specific distance distributions obtained here. Subsequent hardness [2] and fixed-parameter algorithmic [3] results address general distance computation rather than the full metric census of either eight-vertex cubic input. The exact eccentricity profile of the different eight-vertex input \(K_{4,4}\) is recorded in [4] but concerns a different graph. Its values do not imply those for \(M_8\) or \(Q_3\).

## Limitations

This is an exact finite computation with an explicit exhaustive verifier, not a structural formula for arbitrary cubic graphs or infinite graph families. No complexity improvement for the general rotation-distance problem is claimed. Previously unindexed calculations of these specific graph-associahedron metrics remain possible.

## References

[1] T. Manneville and V. Pilaud, *Graph properties of graph associahedra*, arXiv:1409.8114v1 (first public 2014-09-29), later Sém. Lothar. Combin. B73d (2015). https://arxiv.org/html/1409.8114v2

[2] T. Ito et al., *Hardness of Finding Combinatorial Shortest Paths on Graph Associahedra* (2023). https://arxiv.org/abs/2304.14782

[3] L. F. I. Cunha et al., *Computing Distances on Graph Associahedra is Fixed-parameter Tractable* (2025). https://arxiv.org/abs/2504.18338

[4] *The complete eccentricity profile of the balanced \(K_{4,4}\) graph associahedron*, published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-complete-eccentricity-profile-of-the-balanced-k-4-4-graph-as--c2821713101d
