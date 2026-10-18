# The first one-point counting-refinement obstructions in distance-hereditary graphs

## Finding
Let \(G\) be a finite connected simple distance-hereditary graph, and let \(r\in V(G)\) be singled out by a unique initial colour. All other vertices initially have one common colour. Let \(\Pi(G,r)\) be the stable partition of ordinary synchronous one-dimensional counting colour refinement, and let \(\Omega(G,r)\) be the orbit partition of the stabilizer \(\operatorname{Aut}(G)_r\).

**Sharp finite classification.** For every such pair \((G,r)\) with \(|V(G)|\le 7\), \(\Pi(G,r)=\Omega(G,r)\). At \(|V(G)|=8\), precisely two nonisomorphic unrooted graphs admit a root for which this equality fails; in each of them the bad root is unique. They are
\[
G_1=K_1\vee (K_3\sqcup C_4),\qquad
G_2=K_1\vee\overline{(K_3\sqcup C_4)},
\]
with the added dominating vertex distinguished. Here \(\sqcup\) is disjoint union and \(\vee\) is graph join. In either rooted graph the stable colour classes have sizes \(1,7\), whereas its rooted automorphism orbits have sizes \(1,3,4\). The graphs have respectively \(14\) and \(21\) edges.

The numbers of connected distance-hereditary graph isomorphism classes on \(n=1,\ldots,8\) vertices are \(1,1,2,6,18,73,308,1484\). The corresponding numbers of isomorphism types admitting at least one bad distinguished root are \(0,0,0,0,0,0,0,2\). This also gives a sharp small-size obstruction to recovery of rooted automorphism orbits by unary two-variable counting types.

## Assumptions and scope
All graphs are finite, simple, undirected and connected. Distance-hereditary means that distances between vertices in each connected induced subgraph equal their distances in the original graph. Ordinary counting refinement replaces a vertex colour by its previous colour and the multiset of its neighbours' previous colours, until no cell splits. Exactly one designated vertex has a singleton initial colour. An automorphism must fix this vertex. No statement is made about multiple independently marked vertices, arbitrary other initial colours, or graphs of order at least nine.

## Proof
**Exhaustive generation.** The classical pendant/twin characterization of connected distance-hereditary graphs states that they are exactly the graphs built from a singleton by repeatedly adding a pendant vertex, a true twin, or a false twin, with connectedness retained. The inverse operation is removal of a pendant vertex or one member of a twin pair. Thus every graph on \(n>1\) vertices in the class has a removable last vertex and an \((n-1)\)-vertex member of the class; conversely, each of the three additions preserves distance heredity. It therefore suffices to construct all three extensions of every isomorphism type at the preceding order and deduplicate by actual graph isomorphism. Isomorphism hashing is used only to narrow comparisons, not as a uniqueness certificate.

**Exact orbit and colour decisions.** For each generated unrooted graph \(G\) and each of its vertices \(r\), compute the stable counting-refinement partition from the indicated initial colouring. Separately compute rooted automorphism orbit equivalence: either enumerate all root-preserving graph automorphisms or decide, for each pair of same-colour vertices \(u,v\), whether an isomorphism exists from \((G,r,u)\) to \((G,r,v)\). These are exact finite tests of the respective definitions. The self-contained code implements both approaches; each uses a complete search with no randomized shortcut. The completeness lemma above transfers the finite exhaustive calculation to every graph in the claimed domain.

The first verifier obtains \(1,1,2,6,18,73,308,1484\) types and finds exactly two failing eight-vertex types, one root in each. The independent verifier takes all connected distance-hereditary graphs of order at most seven directly from NetworkX's complete graph atlas, tests hereditary membership by reverse pendant/twin reductions, and constructs all eight-vertex successors. It recovers the same counts, exceptional types and pointed failures. A separate cross-check explicitly matches each independently generated witness with one of the two models by graph isomorphism.

**Explicit exceptional structures.** In \(G_1\), after marking the cone vertex, all other vertices have exactly two neighbours within their own seven-vertex set and one neighbour at the marked cone, so they have identical refinement signatures forever. The cone is unique and fixed; automorphisms preserve the two different-sized connected components \(K_3\) and \(C_4\). Their internal automorphism groups act transitively, giving rooted orbit sizes \(1,3,4\).

In \(G_2\), the induced seven-vertex graph is \(\overline{K_3\sqcup C_4}\), which is four-regular. Again refinement yields sizes \(1,7\). Since its complement has components \(K_3\) and \(C_4\), the rooted orbit sizes are \(1,3,4\). Both exceptional graphs are distance-hereditary: \(K_3\), \(C_4\), disjoint unions, complements and joins with a singleton are all cographs, a subclass of distance-hereditary graphs. These observations prove the failures without relying on graph enumeration for their existence.

## Verification
Run `python recursive_census.py`, `python atlas_census.py`, `python witness_analysis.py`, then `python cross_check.py` using Python and NetworkX 3.x. The exact source files and replayed outputs are embedded with this result. The first program independently enumerates rooted automorphism permutations; the second starts from a pre-existing complete unlabeled graph atlas and tests doubly pointed graph isomorphisms. Both classify exactly \(1484\) unrooted types at order eight. The third and fourth programs verify model structure and cross-check that independently enumerated exceptional graphs match the same two explicit isomorphism classes. The exhaustive finite theorem depends on the complete-construction justification and the exactness of these programs; it is not an extrapolation from sampled graphs.

## Relationship to prior work
Bandelt and Mulder introduced distance-hereditary graphs and their constructive pendant/twin characterization. Bahrani and Lumbroso (2016) discuss complete split decomposition and enumeration of related hereditary classes; the established connected distance-hereditary counts agree with independent reference tables. Arvind, Köbler, Rattan and Verbitsky (2015) set out colour refinement, rooted individualization and the distinct concepts of Tinhofer/refinable graphs. Their general inclusion results do not state the present eight-vertex rooted minimum or the two models. Gavrilyuk, Nedela and Ponomarenko (2020) prove that distance-hereditary graphs have Weisfeiler–Leman dimension two. A result for two-dimensional WL identification does not by itself determine the sharp one-dimensional single-individualization orbit partition cutoff computed here.

## Limitations
The uniqueness result is computationally exhaustive only through eight vertices. It does not assert that the two displayed graphs are the only obstructions at larger orders. The classification relies on correct execution of exact graph-isomorphism and atlas routines and the classical pendant/twin completeness theorem; no machine-independent formally verified proof artifact is claimed. More specialized prior work could cover the exact finite classification even though none was located among the inspected sources.

## References
- H.-J. Bandelt and H. M. Mulder, *Distance-hereditary graphs*, Journal of Combinatorial Theory B **41** (1986), 182–208, DOI: 10.1016/0095-8956(86)90043-2.
- V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255v3 (first posted 2015-02-04), https://arxiv.org/html/1502.01255v3.
- M. Bahrani and J. Lumbroso, *Enumerations, Forbidden Subgraph Characterizations, and the Split-Decomposition*, arXiv:1608.01465v1 (2016-08-04), https://arxiv.org/html/1608.01465v1.
- A. L. Gavrilyuk, R. Nedela and I. Ponomarenko, *The Weisfeiler–Leman dimension of distance-hereditary graphs*, arXiv:2005.11766 (2020-05-24), https://arxiv.org/abs/2005.11766.
- OEIS A277862, enumerating connected unlabeled distance-hereditary graphs, https://oeis.org/A277862.
