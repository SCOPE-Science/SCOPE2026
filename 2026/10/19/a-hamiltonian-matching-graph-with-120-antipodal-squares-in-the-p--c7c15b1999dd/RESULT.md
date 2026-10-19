# A Hamiltonian matching graph with 120 antipodal squares in the Petersen line graph

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. Its line graph \(G=L(P)\) has fifteen vertices, one for each edge of \(P\), and thirty edges. The graph \(\mathcal M(G)\) has one vertex for each maximum matching of \(G\), with two matching-states adjacent exactly when one of the seven selected edges is exchanged for a different edge and the result remains a maximum matching. Then \(\mathcal M(G)\) has 480 states and 960 edges, is connected, 4-regular and Hamiltonian, and has radius and diameter both nine. Each state has precisely two other states at distance nine. The graph of all distance-nine pairs is a disjoint union of 120 cycles \(C_4\); within each such four-cycle, the matchings have the same exposed vertex in \(G\).

The natural five-symbol action of \(S_5\) partitions all 480 states into six orbits with sizes 60, 60, 60, 60, 120 and 120. Among unordered distinct state-pairs the counts at distances \(1,\ldots,9\) are 960, 2400, 6120, 13080, 23310, 32730, 26550, 9330 and 480 respectively. The shortest-path length can exceed the set-exchange lower bound \(|M\setminus N|\) by zero, one, two or three moves, with respective pair counts 81120, 32340, 900 and 600.

## Assumptions and scope

Everything concerns the single explicit undirected graph \(G=L(KG(5,2))\). Vertices of \(P\) are the ten two-element subsets of \(\{0,1,2,3,4\}\), with adjacency given by disjointness. Distinct edges of \(P\) yield adjacent vertices of \(G\) if they share an endpoint. A matching is a set of pairwise vertex-disjoint edges of \(G\); 'maximum' means greatest cardinality, not inclusion-maximal. Every matching-state contains exactly seven edges and exposes exactly one of the fifteen vertices of \(G\). Two states are neighbors iff \(|M\setminus N|=|N\setminus M|=1\). The distance-nine auxiliary graph is defined on all 480 matching-states, with an edge exactly for pairs at reconfiguration distance nine. This is not the different perfect-matching graph where adjacency requires a Hamiltonian union, nor a flip graph that allows temporary loss of matching size.

## Proof

The independent exact enumeration procedures `build_A` and `build_B` in `check.py` agree and yield 480 near-perfect matchings. `build_A` fixes the unique exposed vertex, recursively pairs the least remaining vertex with each available neighbor and visits all possible pairings. `build_B` checks each of the \(\binom{30}{7}\) edge subsets of \(G\), admitting a subset iff all fourteen endpoints are distinct. This exhausts all size-seven matchings. Because \(G\) has fifteen vertices, seven is the maximal possible size. The two enumerations agree as sets and give 32 states per exposed vertex.

From a size-seven matching with exposed vertex \(u\), replacing the matching edge incident with any neighbor \(v\) of \(u\) by \(uv\) is a legal exchange. Conversely, any valid single-edge exchange must match the formerly exposed vertex, so this generates all neighbors. Since \(G\) is four-regular, each state has precisely four distinct neighbors. The second adjacency construction independently compares all \(\binom{480}{2}\) state-pairs for one-edge symmetric difference, confirming all 960 undirected edges and symmetry of the adjacency relation.

Breadth-first search from each of the 480 states constructs every finite distance. It reaches every state and gives eccentricity nine at every source. An independent sparse-matrix shortest-path algorithm reproduces all 230400 ordered pair distances. The distance-nine graph is constructed from the resulting distance matrix, then exhaustively traversed; it has 120 components of four vertices, each two-regular, hence 120 disjoint \(C_4\). Each component's four matching-states expose the same vertex. Pair-count distributions follow by summing distances over unordered state-pairs. For symmetry, each of the 120 permutations of the five underlying symbols is mapped to a permutation of the fifteen vertices of \(G\), checked to preserve the state-graph adjacency, and used to partition states into orbits. Finally `hamcycle.txt` gives a complete cycle certificate as 480 distinct sorted-state indices: `check.py` verifies that every consecutive index including the last-to-first link is an edge. This proves Hamiltonicity, not just the existence of a long path.

## Verification

With Python 3 and SciPy installed, run `python check.py` in the directory containing `check.py` and `hamcycle.txt`. The script enumerates all states, reconstructs both edge lists, computes and independently cross-checks distances, validates all enumerations and geometric classifications, and verifies the explicit cycle. It concludes `VERIFY_OK`; exact captured stdout appears in `check_output.txt`. The state-index convention is the deterministic sorting of frozensets of seven graph edges performed in `check.py`; the cycle certificate references exactly this order. The check is an exhaustive finite computation, not an extrapolation to other graphs.

## Relationship to prior work

Jones, Roehm and Schultz introduced matching graphs and their metric; Eroh and Schultz established broader structural results about such matching graphs, including forbidden induced configurations and examples from even cycles. The definition here is exactly their one-edge-exchange adjacency; neither the definition nor the general existence of matching graphs is new. The inspected original Jones–Roehm–Schultz paper contains no instance-specific classification of \(L(P)\). The accessible Eroh–Schultz abstract does not describe the specific Petersen-line-graph state metric or Hamiltonian certificate, but its full paper was inaccessible, so possible coverage cannot be excluded conclusively. General independent-set token-sliding and matching reconfiguration literature studies different graphs, less constrained intermediate matchings, or alternate moves; results under those models do not imply this exact finite distance spectrum. Published research-record and mathematical-literature searches for the exact graph, aliases, reconfiguration rule, and numerical parameters did not identify an equivalent claim. A failed search is not a proof of global novelty.

## Limitations

This theorem is specific to \(L(P)\), not to all line graphs or general matching graphs. Hamiltonicity is witnessed by an explicit machine-checkable finite cycle, not a general constructive Gray-code algorithm. No independent external audit has been performed. A potentially relevant complete paper by Eroh and Schultz was not available for full-text comparison; there is residual originality risk, including unpublished or unindexed tables.

## References

- D. M. Jones, D. J. Roehm, M. Schultz, *On Matchings in Graphs*, Ars Combinatoria 50 (1998), 65–79. https://combinatorialpress.com/ars-articles/volume-050-ars-articles/on-matchings-in-graphs/
- L. Eroh, M. Schultz, *Matching Graphs*, Journal of Graph Theory 29 (1998), 73–86, DOI 10.1002/(SICI)1097-0118(199810)29:2<73::AID-JGT3>3.0.CO;2-9. https://doi.org/10.1002/(SICI)1097-0118(199810)29:2%3C73::AID-JGT3%3E3.0.CO;2-9
- G. Chartrand, H. Hevia, E. B. Jarrett, M. Schultz, *Subgraph distances in graphs defined by edge transfers*, Discrete Mathematics 170 (1997), 63–79. https://doi.org/10.1016/0012-365X(95)00357-3
- T. Ito et al., *On the Complexity of Reconfiguration Problems*, 2010. https://arxiv.org/abs/1004.1948
- D. Avis, D. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861. https://arxiv.org/abs/2203.16861
