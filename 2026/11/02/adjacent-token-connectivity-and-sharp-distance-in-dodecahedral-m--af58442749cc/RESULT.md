# Adjacent-token connectivity and sharp distance in dodecahedral minimum feedback sets

## Finding
Let \(D=GP(10,2)\) be the dodecahedral graph, and let \(\mathcal S\) comprise its minimum feedback vertex sets. Define the *adjacent-token-slide graph* \(T(D)\) on \(\mathcal S\) by joining distinct \(S,S'\) exactly if \(S'=S-\{x\}+\{y\}\) with \(xy\in E(D)\) and \(x\in S\), \(y\notin S\). Each intermediate set must itself be a minimum feedback vertex set.

**Theorem.** The adjacent-token-slide graph \(T(D)\) is connected, with \(2520\) vertices and \(8880\) edges. Its radius is \(8\), its diameter is \(10\), and its exact eccentricity multiplicities are
\[
\#\{S\in\mathcal S:\operatorname{ecc}_{T(D)}(S)=d\}=\begin{cases}
120,&d=8,\\2340,&d=9,\\60,&d=10,\\0,&\text{otherwise}.
\end{cases}
\]
Thus any two minimum feedback vertex sets are related by at most ten **adjacent** token slides, and some pair needs ten. The \(660\) minimum sets inducing no edge and the \(1860\) minimum sets inducing one edge each span connected induced subgraphs of \(T(D)\). Within the two strata there are respectively \(1620\) and \(4140\) sliding edges, and \(3120\) additional edges cross the strata.

The minimum size \(6\), number \(2520\), two stratum cardinalities, and prior unrestricted token-jump results are background facts rather than new claims. The finding concerns *local adjacency-constrained mobility and its exact distance classification*.

## Assumptions and scope
The simple graph \(D\) has outer vertices \(u_i\), inner vertices \(v_i\), indexed by \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) (all indices modulo ten). Hence \(D\) has \(20\) vertices, \(30\) edges and degree \(3\). A feedback vertex set \(S\) is a vertex subset for which the induced graph \(D-S\) is acyclic. The exchange relation requires both the removed and inserted vertices to be joined by an edge of \(D\); arbitrary one-vertex exchanges do **not** qualify. The reported distances are shortest-path distances in the finite undirected graph \(T(D)\), not the original dodecahedral graph.

## Proof
**Minimum-size bound and state-space completeness.** For any feedback vertex set \(S\) of size \(k<20\), let \(e(S)\) denote the number of graph edges with both ends in \(S\). Cubic regularity implies that the induced complement has exactly \(30-3k+e(S)\) edges. Being a forest on \(20-k\) vertices, it can have at most \(19-k\) edges. Therefore \(11+e(S)\le2k\), giving \(k\ge6\). The enumeration below finds size-six sets, establishing \(\tau(D)=6\). For every such optimum \(e(S)\le1\). Moreover its complement is a forest with exactly \(2-e(S)\) components.

**Exhaustive enumeration.** The accompanying `verify.py` examines every one of the \(\binom{20}{6}=38760\) subsets of size six. For each it tests acyclicity of \(D-S\) with a disjoint-set union algorithm: inserting an edge whose endpoints are already in the same component is equivalent to finding a cycle. This yields precisely \(2520\) admissible masks, partitioned by \(e(S)\) into \(660\) and \(1860\) cases. The exhaustive construction is finite; no assumption about a symmetry orbit or sample is used.

**Complete slide graph.** For each admissible mask the verifier tries every selected vertex \(x\) and every neighbor \(y\notin S\) of \(x\). It retains the resulting mask exactly when that mask occurs in the exhaustive admissible-set dictionary. Because every legal slide has a unique removed vertex and unique inserted vertex, this produces every undirected edge of \(T(D)\) without omission. It finds \(8880\) distinct edges, including \(1620\) internal to the zero-edge stratum, \(4140\) internal to the one-edge stratum, and \(3120\) crossing edges. A complete connected-component search finds one component in the full graph and one component inside each stratum. Breadth-first search from **every** one of the \(2520\) states yields exactly the eccentricity histogram displayed in the theorem. Consequently the radius is eight, diameter ten, and both extrema are attained.

**Separate implementation.** The supplied `verify_alt.cpp` starts from a different 20-vertex dodecahedron edge list and checks an explicit bijection to the generalized Petersen presentation. It independently tests acyclicity by repeatedly pruning vertices of remaining degree zero or one. It then examines all unordered pairs of admissible six-vertex masks and recognizes a slide by a symmetric difference of two vertices whose corresponding graph vertices are adjacent. It obtains the same slide-edge and type counts, whole-graph connectivity, and all-source eccentricities, using independent graph construction and transition detection. The internal-stratum connectivity is checked explicitly by the first verifier.

## Verification
From a directory containing the supplied files, run `python3 verify.py` and `g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. Both were executed after construction, and both asserted that the slide graph has \(2520\) vertices, \(8880\) edges, one connected component, radius \(8\), diameter \(10\), and eccentricity multiplicities \((120,2340,60)\) at distances \((8,9,10)\). For comparison only, both reconstruct the **unrestricted** one-vertex-replacement graph with \(23940\) edges and uniform eccentricity six; those latter properties are not part of the present novelty claim. The entire finite search space is processed exactly, without randomized estimates or numerical floating-point calculations.

## Relationship to prior work
Kelly and Liu's 2016 investigations of induced forests and feedback vertex sets in low-degree, large-girth graphs motivate the dodecahedron as a natural extremal example; those papers concern optimum size, not adjacent-token-slide geometry. Existing dodecahedral finite censuses already determine the \(2520\) optimum configurations and their two component-count strata; their counts are reused, not newly claimed. The known unrestricted one-vertex-exchange graph of these same configurations has \(23940\) edges and diameter \(6\), whereas the adjacency-constrained graph here has only \(8880\) edges and diameter \(10\). This is a strict change of adjacency relation, not a numerical reformulation of the earlier metric. Bousquet, Hommelsheim, Kobayashi, Mühlenthaler and Suzuki analyze unrestricted feedback-vertex-set exchanges in planar graphs of maximum degree at most three, whereas this theorem requires the exchanged vertices themselves to be adjacent. That general unrestricted-connectivity result does not imply local token-sliding connectivity or the exact metrics here.

## Limitations
The result is a proved finite statement about this one graph. It does not establish a uniform sliding-connectivity theorem for other cubic graphs, generalized Petersen graphs, or arbitrary planar graphs. Exhaustive reproducible computation proves the exact numerical classification but does not supply a short conceptual formula for the distances. Novelty is assessed against inspected sources and available previous finite results, not asserted as a guarantee against unindexed literature. The full text of the closest 2023 reconfiguration paper was not accessible in this examination; its accessible statements concern unrestricted exchanges.

## References
- T. Kelly and C.-H. Liu, *Size of the Largest Induced Forest in Subcubic Graphs of Girth at least Four and Five*, arXiv:1603.03855, first public version 2016-03-12. https://arxiv.org/abs/1603.03855
- T. Kelly and C.-H. Liu, *Minimum Size of Feedback Vertex Sets of Planar Graphs of Girth at least Five*, arXiv:1603.04559, first public version 2016-03-15. https://arxiv.org/abs/1603.04559
- N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, and A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science (2023), article 114188, DOI:10.1016/j.tcs.2023.114188.
