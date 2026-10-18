# The two optimal power-monitoring orbits of the Desargues graph and their relocation geometry

## Finding
Let \(D=H(5,2)\) be the Desargues graph: its twenty vertices are the two- and three-element subsets of \(\{1,2,3,4,5\}\), and its edges join a two-set to a three-set exactly when the former is contained in the latter. Under ordinary power domination, the minimum monitoring-set size is \(\gamma_P(D)=3\). Its **240 minimum power-dominating triples** consist exactly of the two following intrinsic classes. Pairwise distances in the base graph are sorted to define the profile.

| Base-graph distance profile | Optimal triples | Additional synchronous forcing rounds | Token-jump degree | Token-slide eccentricity |
|---|---:|---:|---:|---:|
| \((2,3,5)\) | 120 | 3 | 17 | 7 |
| \((3,3,4)\) | 120 | 2 | 13 | 8 |

Each class is one orbit under the explicit \(S_5\times C_2\) action (permutations of the five symbols and subset complementation). On these minimum sets, a token jump may replace one selected vertex by any unselected vertex, while a token slide requires the exchanged vertices to be adjacent in \(D\). Both reconfiguration graphs are connected. The token-jump graph has 240 vertices, 1,800 edges, degree classes 120 of degree 17 and 120 of degree 13, and radius and diameter both 4. The token-slide graph has 240 vertices, 480 edges, is 4-regular and bipartite, and has radius 7 and diameter 8. Its 120 slower-monitoring triples have eccentricity 7; its 120 faster-monitoring triples have eccentricity 8. The token-slide edges consist of 120 within each class and 240 between the classes.

In particular, faster propagation is accompanied by fewer unrestricted single-replacement options and greater worst-case travel distance under local slides. This is an exact finite structural classification, not a claim about every generalized Petersen graph.

## Assumptions and scope
All graphs are finite, simple and undirected. A set \(S\subseteq V(D)\) power dominates if, starting with the observed set \(N[S]\), repeated color-change steps (an observed vertex with exactly one unobserved neighbor observes that neighbor) eventually observe every vertex. For *propagation time* here, the closed-neighborhood step is numbered zero and thereafter all available forces are performed simultaneously; the displayed time is the minimum number of these synchronous subsequent rounds. Distances of three vertices are the three ordinary shortest-path lengths between pairs. Minimum means minimum cardinality, not merely inclusion-minimal. All reconfiguration states are distinct unordered triples and a legal step must stay within the minimum power-dominating triples.

For self-contained reproduction, number the twenty subset labels by increasing five-bit characteristic-mask integer (bit zero represents symbol one). The exact graph, action and move rules are implemented in `desargues_pd_verify.py`. An independent program `desargues_pd_independent.py` constructs the isomorphic generalized Petersen graph \(\operatorname{GP}(10,3)\) and uses the original vertex-and-edge monitoring rules rather than the color-change closure.

## Proof
**Classification.** The maps that permute the five base symbols preserve subset inclusion. Complementation exchanges two- and three-subsets and also preserves the undirected incidence relation. Their 240 distinct compositions act by automorphisms. There are exactly \(\binom{20}{3}=1140\) three-element candidate sets. The explicit group partitions these into twelve disjoint orbits; the following table gives every orbit's size and its closed-neighborhood/forcing-round observed-vertex totals. The representatives are printed as five-bit subset masks, not vertex indices.

| Representative | Orbit size | Pairwise-distance profile | Observed totals (round zero first) | Feasible |
|---|---:|---|---|---|
| (3,5,6) | 20 | (2,2,2) | 10 | no |
| (3,5,7) | 60 | (1,1,2) | 8 | no |
| (3,5,9) | 40 | (2,2,2) | 9,12 | no |
| (3,6,9) | 120 | (2,2,4) | 10,12,15,16 | no |
| (3,7,9) | 240 | (1,2,3) | 9,12 | no |
| (6,7,9) | 120 | (1,3,4) | 10,14,16 | no |
| (7,9,10) | 120 | (2,3,3) | 11,15,16 | no |
| (7,11,12) | 60 | (2,3,3) | 11,16 | no |
| (6,9,17) | 60 | (2,4,4) | 11,12 | no |
| (7,10,17) | 120 | (3,3,4) | 12,18,20 | yes |
| (3,14,17) | 120 | (2,3,5) | 11,16,19,20 | yes |
| (6,14,17) | 60 | (1,4,5) | 10 | no |

Each representative's propagation is a deterministic application of the defining rule; automorphisms carry its observed-vertex sequence to the whole orbit. The table's disjoint orbit sizes total 1,140. Every set of zero, one or two vertices is infeasible by an exhaustive check of the \(1+20+190=211\) candidates using exactly the same rule. The two feasible orbits therefore prove the minimum cardinality and complete 240-state classification. Both accepted orbits have size 120, and their pair-distance profiles differ, so neither covers the other.

**Reconfiguration.** Exchange edges are formed explicitly between feasible triples \(S,T\) precisely when \(|S\triangle T|=2\); for sliding, the one deleted and one inserted vertex must additionally be an edge of \(D\). Exhaustive generation of the two edge lists yields 1,800 and 480 undirected edges respectively, with degree distributions as stated. The same 240 automorphisms preserve each adjacency relation and act transitively on each of the two types, so eccentricity and degree are constant within each type. Breadth-first search from one representative of each type gives the exact distance-level counts (number of states at distances zero, one, etc.):

| Move | Start profile | BFS level counts |
|---|---|---|
| Jump | (2,3,5) | 1,17,64,156,2 |
| Jump | (3,3,4) | 1,13,72,152,2 |
| Slide | (2,3,5) | 1,4,12,30,57,75,50,11 |
| Slide | (3,3,4) | 1,4,12,29,56,75,50,12,1 |

Each level sequence sums to 240, proving connectedness, and its final nonzero position proves the reported eccentricities; transitivity on each class then proves the radii and diameters over *all* states. To see bipartiteness of the slide graph without computation, color a triple by the parity of the number of selected two-subsets: each slide in the bipartite incidence graph exchanges a two-subset and a three-subset, changing this parity. Counting edge endpoints by both classes gives 120 intra-class edges for each class and 240 cross-class edges.

## Verification
Run `python3 desargues_pd_verify.py` using Python 3.9 or newer. It enumerates the complete explicit automorphism subgroup, independently verifies adjacency invariance, partitions all candidate triples into orbits, checks every orbit member's feasibility and speed, and constructs and searches both complete move graphs. Its output is included as `desargues_pd_verify.txt` and ends with `VERIFY_OK`. Run `python3 desargues_pd_independent.py`: it independently constructs all thirty edges of \(\operatorname{GP}(10,3)\), validates an explicit graph isomorphism to the subset-inclusion model, and uses the original *edge-monitoring* power-domination rules to recompute all minimum triples, both move graphs and every state's eccentricity. Its output is `desargues_pd_independent.txt` and ends with `INDEPENDENT_VERIFY_OK`. These are two computational methods in the same research package, not an external audit. Both programs use only the Python standard library. The finite enumeration is exhaustive because all 211 smaller sets and all 1,140 triples are visited.

## Relationship to prior work
Barrera and Ferrero (first online publication 18 October 2010) proved upper bounds for the power domination numbers of generalized Petersen graphs, including the general bound \(\gamma_P(\operatorname{GP}(m,k))\le k\). Their Section 5 does not classify the minimum triples, relocation graphs or distances of \(\operatorname{GP}(10,3)\). Benson et al. (arXiv 1510.02421, first public 8 October 2015) give general power-domination/zero-forcing relations but not these two optimal-placement orbit and movement classifications. *Power Domination Reconfiguration* (DOI 10.1007/s44007-025-00187-5) defines and studies token-jump power domination graphs and several special graph families; its studied families and general theorems do not entail the two explicit Desargues state graphs or their metrics. Prior work on token sliding for other graph-set properties has different feasibility constraints. Thus the claimed contribution is specifically the classification of all optimal triples, their propagation-time split, and both exact relocation geometries, not the underlying general move definitions or upper bounds.

## Limitations
The theorem is for the twenty-vertex Desargues graph only. The argument uses finite exhaustive orbit and shortest-path calculations, supplied in independently structured verification programs; no general formula for other bipartite Kneser or generalized Petersen graphs is asserted. The power-propagation times use the explicitly stated synchronous-round convention. Unindexed equivalent computations could exist; the literature comparison cannot prove global uniqueness. No external independent audit has been carried out.

## References
- R. Barrera and D. Ferrero, *Power domination in cylinders, tori, and generalized Petersen graphs*, Networks 58 (2011), 43–49. DOI: `10.1002/net.20413`; first published online 2010-10-18. Author-accessible full text: https://cpb-us-e1.wpmucdn.com/wp.txstate.edu/dist/1/556/files/2015/03/BarreraFerrero.pdf .
- K. F. Benson, D. Ferrero, M. Flagg, V. Furst, L. Hogben, V. Vasilevska and B. Wissman, *Power domination and zero forcing*, arXiv `1510.02421`, first posted 2015-10-08.
- *Power Domination Reconfiguration*, La Matematica, DOI: `10.1007/s44007-025-00187-5`, full text at https://link.springer.com/article/10.1007/s44007-025-00187-5 .
