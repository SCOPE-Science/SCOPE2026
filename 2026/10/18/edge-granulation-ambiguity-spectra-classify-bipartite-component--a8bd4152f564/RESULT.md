# Edge-granulation ambiguity spectra classify bipartite component orders

## Finding

**Theorem (complete ambiguity spectrum and inverse classification).** Let \(G=(V,E)\) be any finite simple undirected graph, including disconnected graphs and isolated vertices. For every \(X\subseteq V\), observe the two edge sets
\[
L_G(X)=\{e\in E:e\subseteq X\},\qquad U_G(X)=\{e\in E:e\cap X\ne\varnothing\},\qquad \rho_G(X)=(L_G(X),U_G(X)).
\]
Thus each edge is observed in one of three states: neither endpoint selected, exactly one selected, or both selected. The object measured here is this *two-sorted vertex-to-edge granulation*, not the same-universe equivalence-based Pawlak approximation.

Let \(s\) be the number of isolated vertices. Let \(v_1,\ldots,v_b\ge2\) be the orders of all connected **bipartite** components having an edge, repeated according to component multiplicity, and let \(u\) be the total number of vertices in nonbipartite components. For a realized observation \(Q\), put \(f(Q)=|\rho_G^{-1}(Q)|\), and define the unlabelled multiplicity enumerator by
\[
F_G(z)=\sum_{Q\in\operatorname{im}(\rho_G)}z^{\log_2 f(Q)}.
\]
Every fiber has power-of-two size, so this is a polynomial. It is exactly
\[
\boxed{F_G(z)=2^u z^s\prod_{i=1}^{b}\bigl(z+2^{v_i}-2\bigr).}
\]
Consequently the complete unlabelled multiset of observation-fiber sizes determines, without labels or knowledge of \(|V|\), **exactly** the triple
\[
\boxed{\bigl(s,\ u,\ \{\!\{v_1,\ldots,v_b\}\!\}\bigr).}
\]
Two finite simple graphs have the same unlabelled fiber-size multiset if and only if those triples agree. In particular, the spectrum determines every nontrivial bipartite component order and the total order of the nonbipartite part, but in general determines neither graph isomorphism nor the number or structure of nonbipartite components.

The number of distinct observations, maximum fiber size, number of maximum fibers, and output min-entropy under uniform vertex-subset sampling are respectively
\[
\boxed{|\operatorname{im}\rho_G|=2^u\prod_{i=1}^{b}(2^{v_i}-1),\quad \max_Q f(Q)=2^{s+b},\quad |\{Q:f(Q)=2^{s+b}\}|=2^u,}
\]
\[
\boxed{H_\infty(\rho_G(X))=|V|-s-b.}
\]
These formulas include all degenerate cases, with empty products interpreted as one.

## Assumptions and scope

A graph is finite, loopless and simple. Component orders and bipartiteness have their ordinary graph-theoretic meanings; an isolated vertex is excluded from the \(v_i\) list. The observer sees which original *edges* have zero, one, or two selected endpoints, rather than the original vertex set. The multiset of fiber cardinalities includes one entry for each realized observation, with repetitions even if different observations have equal fiber size. A nonbipartite component has an odd cycle, hence no proper binary vertex coloring. All logarithms in the enumerator are base two.

## Proof

**1. Edge-state decoding on a connected component.** For a vertex coloring \(x:V\to\{0,1\}\), the observed state on \(e=\{a,b\}\) is \(x(a)+x(b)\in\{0,1,2\}\). A state-zero edge forces both endpoint bits to zero; a state-two edge forces both bits to one; and a state-one edge forces its endpoint bits to be complementary.

Fix any *realized* observation on a connected component containing an edge. If an edge has state zero or two, it fixes at least one vertex bit, and connectivity propagates all remaining bits uniquely along paths: on an edge of state one the unknown endpoint is the complement of the known endpoint, while on an edge of state zero or two both bits are predetermined. Because the observation was realized, no consistency issue arises. Its fiber has cardinality one.

If every edge has state one, the consistent labelings are precisely the proper two-colorings. A connected nontrivial bipartite graph has exactly two of them, interchanged by global complementation; a connected nonbipartite graph has none. Hence every realized observation in a connected nonbipartite component is unique, giving \(2^v\) different singleton fibers for component order \(v\). In a connected bipartite component of order \(v\ge2\), there is precisely one double fiber, at the all-one edge-state observation. The remaining \(2^v-2\) vertex subsets give distinct singleton fibers.

**2. Disjoint-union factorization.** Distinct connected components have disjoint edge coordinates. Consequently their sets of observations form a Cartesian product, and the size of a global fiber is the product of its component fiber sizes. One isolated vertex contributes one empty-edge observation of size two, hence the factor \(z\). A nonbipartite component of order \(v\) contributes \(2^v\) singleton observations, hence the constant polynomial \(2^v\). A nontrivial bipartite component of order \(v\) contributes \(2^v-2\) singleton observations and one observation of size two, hence \(2^v-2+z\). Multiplication proves the displayed product formula and the fact that all fiber sizes are powers of two.

**3. Recovery and the if-and-only-if statement.** Every factor \(z+2^{v_i}-2\) has a strictly positive constant term. Therefore the lowest nonzero degree of \(F_G\) is \(s\). Its highest nonzero coefficient is \(2^u\), determining \(u\). Divide by \(2^u z^s\); the remaining monic polynomial has complex roots \(-(2^{v_i}-2)\), counted with multiplicity. Because \(v\mapsto 2^v-2\) is injective on integers \(v\ge2\), its root multiset determines precisely the unordered multiset of component orders \(\{\!\{v_i\}\!\}\). Conversely the triple determines the polynomial, so it determines the unlabelled fiber spectrum. Moreover \(F_G(2)=2^{|V|}\), since each realized fiber contributes its cardinality to this evaluation, so even the total graph order can be recovered from the spectrum.

**4. Other exact invariants.** Evaluating the polynomial at one counts the realized observations. Every bipartite factor contributes one degree-one choice, and every isolate contributes a fixed degree-one factor; hence the largest exponent of \(z\) is \(s+b\) and its coefficient is \(2^u\). Under uniform input \(X\), the largest output probability is \(2^{s+b-|V|}\), giving the min-entropy formula.

## Verification

The accompanying standalone Python program `verify_edge_observation.py` independently enumerates all vertex subsets, derives the two edge approximations as edge states, constructs every output fiber, and compares the full spectrum to the factorized formula. It exhaustively tests all \(33867\) finite simple graphs on at most six labeled vertices (the precise count is \(1+2+8+64+1024+32768=33867\)) and 750 reproducibly sampled graphs on seven through nine vertices, totaling \(34617\) graphs. Its recovery routine reconstructs \(s\), \(u\), and the bipartite component-order multiset from the unlabeled spectrum. It also tests the sharp rank-two boundary: a single three-vertex hyperedge has fiber sizes \(1,6,1\), rather than powers of two. The program uses only the Python standard library and may be executed with `python verify_edge_observation.py`.

## Relationship to prior work

Work on graphical rough approximations and rough hypergraphs supplies relevant frameworks for how lower and upper approximations interact with graph or hypergraph structures [1,2]. The present observation is defined explicitly as a **vertex-to-edge** incidence channel; it is not a theorem about equivalence-relation partitions of a graph and does not claim to subsume those frameworks. The graph-theoretic fact that connected bipartite graphs admit precisely two proper binary colorings is classical and is an ingredient, not a novel lemma. The asserted contribution is the complete unlabelled multiplicity polynomial for every graph and its exact inverse classification by component orders, which is not stated in the inspected relevant full text [2]. An accessible abstract of [1] was insufficient for a full-text exclusion; the possibility of an equivalent earlier formulation remains a limitation.

## Limitations

The spectrum **does not** recover the graph topology: all connected nonbipartite graphs on the same number of vertices have the same constant enumerator, and all connected bipartite graphs of equal order share the same linear enumerator. No assertion is made for hyperedges of size greater than two, weighted observations, noisy measurements, or higher-valued vertex labels. The finite verification is corroborative; the proof for all graph orders is the connectivity argument above. Publication priority and independent external validation have not been established.

## References

[1] T. Shaheen and J. G. Stell, *Graphical Partitions and Graphical Relations*, Fundamenta Informaticae 165 (2019), 75–98, DOI: 10.3233/FI-2019-1777; first published online 14 February 2019. https://doi.org/10.3233/FI-2019-1777

[2] M. Sarwar, *A Theoretical Investigation Based on the Rough Approximations of Hypergraphs*, Journal of Mathematics (2022), article 1540004, first published 7 March 2022. https://doi.org/10.1155/2022/1540004
