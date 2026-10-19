# The click-component size and symmetry spectrum of acyclic Petersen orientations

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent precisely when the subsets are disjoint. Let \(\mathcal C(P)\) have as vertices **all acyclic orientations** of the fifteen undirected edges of \(P\); two orientations are adjacent when one is obtained from the other by reversing **all three edges incident to a vertex that is a source or a sink**. This is the undirected source-to-sink (click) equivalence graph, with source clicks and their inverse sink clicks represented by the same edge.

The graph \(\mathcal C(P)\) has exactly \(16{,}680\) vertices, \(28{,}140\) edges and \(704\) connected components. Its complete component distribution and component metrics are:

| Component order | Number of components | Edges per component | Radius | Diameter | Orbits under the natural \(S_5\) action |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 66 | 20 | 150 | 5 | 6 | 1 of size 20 |
| 50 | 24 | 105 | 5 | 6 | 1 of size 24 |
| 38 | 60 | 73 | 5 | 6 | 1 of size 60 |
| 28 | 120 | 49 | 5 | 6 | 1 of size 120 |
| 22 | 120 | 34 | 5 | 5 | 1 of size 120 |
| 21 | 120 | 33 | 5 | 5 | **2 of size 60** |
| 16 | 120 | 22 | 5 | 5 | 1 of size 120 |
| 12 | 120 | 14 | 5 | 5 | 1 of size 120 |

In particular, **every component has radius exactly five**, its diameter is either five or six, and the component set has exactly nine orbits under the natural \(S_5\) symmetry. Complementing every directed edge preserves the click graph; this global orientation-reversal involution interchanges the two inequivalent \(S_5\)-orbits of 21-vertex components and preserves each of the other seven orbits setwise. There are consequently eight component-isomorphism types, distinguished by their orders.

The previously established relation between click classes and the Tutte/chromatic polynomial already determines the **number** of components; the assertion here is the finer complete distribution of their cardinalities, symmetry orbits and shortest-path radii/diameters, not a new general class-counting theorem.

## Assumptions and scope

Every one of the \(2^{15}\) possible edge orientations is considered when testing acyclicity. An orientation is acyclic exactly when its directed graph has no directed cycle. A source has every incident arc directed outward; a sink has every incident arc directed inward. The click operation is allowed only at those vertices; other subsets of incident edges may not be reversed. Isolated components of the flip graph are not introduced by restricting the allowed orientations. Distances, radii and diameters are ordinary undirected graph distances **within** each component. The group \(S_5\) acts by relabeling the underlying five symbols, and orientation reversal reverses every directed edge.

The theorem is exact for this one graph; no assertion is made about the class-size spectrum or radii of arbitrary graphs, or about arbitrary individual-edge flips.

## Proof

**1. Complete finite state space.** Order the ten two-subsets lexicographically. Order each of the fifteen unordered edges by its two increasing vertex indices. Encode an orientation by an integer \(s\in\{0,\ldots,2^{15}-1\}\): bit \(k\) specifies whether the \(k\)-th edge points from its smaller-index endpoint to its larger-index endpoint or in the reverse direction. The program `verify_click_petersen.py` iterates through the entire stated range. Kahn topological elimination and an independently coded depth-first directed-cycle test agree on each orientation. Exactly \(16{,}680\) pass both tests. Independently, the chromatic subset expansion
\[
\chi_P(q)=\sum_{F\subseteq E(P)}(-1)^{|F|}q^{k(F)}
\]
with \(k(F)\) the number of connected components of the spanning subgraph \((V(P),F)\), gives \(\chi_P(-1)=16{,}680\) and \([q]\chi_P(q)=-704\). These are independent checks on the state enumeration and the known click-class count formula, respectively; they are not substitutes for the structural computation below.

**2. Exact adjacency and component partition.** For each acyclic \(s\), inspect each of the ten vertices and verify that all three incident arcs point either inward or outward. Only then flip the corresponding three bits to obtain the neighbor \(t\). The resulting neighbor is tested against the enumerated acyclic states; each adjacency is checked to be symmetric. The undirected edge sum is exactly \(28{,}140\). Exhaustive breadth-first search from the least unvisited orientation gives 704 disjoint components and the stated component-size multiplicities. Their weighted size sum is \(16{,}680\) and the weighted edge sum is \(28{,}140\).

**3. Independent cycle-signature check.** Choose the lexicographically first spanning tree of \(P\) by scanning edges and adjoining each edge that does not create a tree cycle. Its six excluded chords define six oriented fundamental cycles. For each acyclic orientation compute the six integer sums of edge-orientation signs, with signs reversed when the cycle traverses an edge against its fixed reference direction. The independent signature grouping has exactly 704 nonempty groups, and every group equals exactly one component found in Step 2. The underlying completeness of cycle-circulation signatures for click equivalence is classical (Macauley and Mortveit, Theorem 4.1, citing Pretzel); the equality here is also checked exhaustively for all states without assuming that theorem for the finite partition.

**4. Symmetry orbits.** Enumerate all 120 permutations of the five symbols. Each relabels the ten two-subsets and permutes the fifteen edges, reversing an edge bit when the reordered endpoints change their canonical order. For every component representative, apply all 120 induced transformations and look up the component containing its image. This partitions all 704 components into nine orbits, grouped by order as in the final column. Each orbit's members are checked to have the same order, edge count, radius and diameter. Complementing all fifteen bits is an automorphism of \(\mathcal C(P)\) and maps the two 60-element orbits of 21-vertex components to each other. The other seven orbits are invariant as sets. Thus components of equal order are all mutually isomorphic (via \(S_5\) and, in the order-21 case, reversal); components of different orders cannot be isomorphic.

**5. Metric certification.** For each of the \(16{,}680\) acyclic orientations, run breadth-first search **inside its complete component** and record its maximum shortest-path distance to any vertex there. Taking the minimum and maximum of these eccentricities separately for each component gives the radius and diameter. Every computed component radius is five. The exact diameters and all edge counts agree within each of the nine verified symmetry orbits. The table contains the full range of cases, not a sample or a random test.

Together Steps 1–5 prove every numerical and symmetry assertion, conditional only on the transparent finite algorithms and executable exhaustive loops supplied in this package. No finite sample is extrapolated to an infinite family.

## Verification

Run `python3 verify_click_petersen.py` in a standard Python 3 environment; it uses no nonstandard packages, network access or external data. The script contains both acyclicity tests, the chromatic-polynomial independent check, the adjacency and component construction, the fundamental-cycle signature partition, all 120 symmetry actions, the global reversal map and exhaustive eccentricity calculations. The exact deterministic output is embedded as `verification_output.txt`, ending with `VERIFY_OK`. The checks cover every one of the \(2^{15}\) edge orientations and all components.

## Relationship to prior work

Macauley and Mortveit established the click-equivalence construction, its relationship with Coxeter elements, the general equality \(\kappa(G)=T_G(1,0)\), and the completeness of cycle-signature invariants. In particular, the number \(704\) is available in principle from known general results together with the Petersen chromatic polynomial. Those theorems give neither the eight exact component orders and multiplicities nor their nine orbits under the natural \(S_5\) action nor this component-radius and diameter spectrum.

A published general result entitled *A complete cycle-anchor invariant and geodesic formula for graph flexes* gives connectivity and exact distance formulas for **all** graph orientations under source/sink flexes. Its acyclic specialization includes the click operation studied here and thus logically covers the **method** of distance calculation; it does not state or tabulate the Petersen component census, symmetry orbit splitting or uniform radius. This finite classification is not represented as a new general distance theorem. Related results on acyclic-orientation reconfiguration for complete graphs and certain complete multipartite graphs concern different underlying graphs.

## Limitations

This is an exhaustive, reproducible **finite graph classification**, not a theorem about all cubic graphs. Its originality is the Petersen-specific spectrum, component metrics and symmetry action; the definition of a click, the number of classes from the Tutte polynomial, and general cycle-signature and geodesic formulas are previous mathematics. An unindexed earlier table or an unpublished exhaustive computation could have the same precise data. Independent expert validation and independent reproduction beyond the included executable mathematical checks have not been performed.

## References

1. Matthew Macauley and Henning S. Mortveit, *Equivalences on Acyclic Orientations*, arXiv:0709.0291, first public version 3 September 2007; especially the definitions of the click graph and its component equivalence.
2. Matthew Macauley and Henning S. Mortveit, *On Enumeration of Conjugacy Classes of Coxeter Elements*, arXiv:0711.1140 (2007), *Proceedings of the American Mathematical Society* **136** (2008), 4157–4165.
3. Matthew Macauley and Henning S. Mortveit, *Posets from Admissible Coxeter Sequences*, arXiv:0910.4376 (2009), *Electronic Journal of Combinatorics* **18** (2011), R197, Theorem 4.1.
4. *A complete cycle-anchor invariant and geodesic formula for graph flexes*, published mathematical research record `adc90e8a9935` (11 October 2026), full mathematical statement and proof inspected.
5. Herbert S. Wilf, *Generatingfunctionology*, for the standard subgraph expansion of the chromatic polynomial; the finite implementation is directly included here.
