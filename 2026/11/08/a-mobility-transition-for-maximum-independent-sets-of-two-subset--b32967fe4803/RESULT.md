# A mobility transition for maximum independent sets of two-subset Kneser prisms

## Finding
For every integer \(n\ge3\), let \(H_n=\operatorname{KG}(n,2)\square K_2\). The prism has two copies of the graph on two-element subsets of \([n]\), with disjoint pairs adjacent inside each copy and the two copies of each pair joined by an edge. Let \(\mathcal R_n\) have maximum independent sets as vertices, adjacent when one chosen vertex is replaced by another, preserving independence and cardinality.

**Theorem.** The independence number satisfies
\[
\alpha(H_n)=\begin{cases}3,&n=3,\\6,&n=4,\\2n-3,&n\ge5.\end{cases}
\]
The exact optimum reconfiguration graph is
\[
\mathcal R_n\cong\begin{cases}
Q_3,&n=3,\\
8K_1,&n=4,\\
\mathcal B,&n=5,\\
n(n-1)K_2,&n\ge6,
\end{cases}
\]
where \(\mathcal B\) is the connected eighty-vertex graph constructed below: it has 140 edges, forty vertices of degree three, forty of degree four, and diameter nine. In particular, the number of maximum sets is \(8\), \(8\), \(80\), and \(2n(n-1)\) in the four cases, respectively. Token jumping and token sliding give precisely the same optimum reconfiguration graph.

## Assumptions and scope
All graph vertices are labeled: a prism vertex is \((A,\varepsilon)\) with \(A\in\binom{[n]}2\) and \(\varepsilon\in\{0,1\}\). Adjacency means either the same layer with disjoint ground pairs, or the same ground pair in opposite layers. Every maximum independent set has a pair of disjoint intersecting edge families \((F_0,F_1)\), where each \(F_\varepsilon\) is an intersecting family of two-element subsets. A single replacement removes one prism vertex and adds a different unselected one; all intermediate configurations are maximum independent sets.

## Proof
**Intersecting-pair lemma.** For \(n\ge5\), an intersecting family of two-element subsets with at least four members is contained in a unique star \(\mathcal S_i=\{ij:j\ne i\}\). Indeed, if a pairwise-intersecting family has no common ground label, take two members \(ab,ac\); a member avoiding \(a\) must be \(bc\). These three pairs form a triangle, and no fourth distinct pair meets all three. Thus an intersecting family has at most \(n-1\) members; equality for \(n\ge5\) is precisely a full star.

For \(n\ge5\), the two prism layers each contain at most \(n-1\) selected pairs. Both cannot attain \(n-1\), since distinct stars share their pair \(ij\), while identical stars overlap completely and the layers must be disjoint. Thus the total is at most \(2n-3\). This is attained by taking full \(\mathcal S_i\) in layer zero and \(\mathcal S_j\setminus\{ij\}\) in layer one, for \(i\ne j\), or reversing layers. Equality forces layer sizes \((n-1,n-2)\) in some order. The full layer is the unique \(\mathcal S_i\); the other avoids \(i\) entirely because every pair containing \(i\) is already chosen.

For \(n\ge6\), the other layer contains \(n-2\ge4\) pairwise-intersecting ground pairs, hence is a partial star with center \(j\ne i\). There are exactly \(n-2\) available pairs of that star avoiding \(i\), so it is \(\mathcal S_j\setminus\{ij\}\). Distinct centers \((i,j)\) and choice of full layer give precisely \(2n(n-1)\) configurations. A one-replacement move cannot alter the center of the full star while retaining its \(n-1\ge5\) members, nor change the center of the \(n-2\ge4\)-member star within a layer. The only legal move transfers the ground pair \(ij\) from the full-star layer to the other, thereby exchanging which layer contains a full star. This pairs the two orientations at centers \((i,j)\) and \((j,i)\) into exactly \(n(n-1)\) disjoint edges.

For \(n=5\), each four-member layer is a full star centered at \(i\). The remaining three-member family avoids \(i\), so it is either one of the four three-edge stars on the other four labels, or one of the four triangles supported on three of those labels. For each choice of full layer (two choices) and center \(i\) (five choices) there are eight states, totaling 80. Within one such eight-state fiber, a legal exchange changes a three-star to a triangle containing its center: each three-star is adjacent to three triangles, and conversely. Thus the fiber is the crown graph \(K_{4,4}\) minus a perfect matching, having 12 edges. A three-star state also has exactly one inter-fiber move transferring the pair of the two star centers between layers; no triangle state permits an inter-fiber move. The fibers are connected, and their inter-fiber bridges connect all ten fibers because the centers \(i\ne j\) form a connected complete bipartite graph with the five matching edges deleted. Hence \(\mathcal B\) is connected, has \(10\cdot12+20=140\) edges, and has degree three at the forty triangle states and degree four at the forty three-star states. Its diameter is exactly nine, verified by complete breadth-first enumeration of all eighty explicitly characterized states in each of two independently implemented exhaustive checkers; the program files, outputs, and direct reconstruction details are embedded below.

For \(n=4\), \(\operatorname{KG}(4,2)\) consists of three independent edges, so its prism consists of three disjoint four-cycles. Each four-cycle has precisely two maximum independent sets (the opposite pairs), with no legal one-vertex replacement between them. The eight combinations are isolated. For \(n=3\), \(\operatorname{KG}(3,2)\) consists of three isolated vertices, so the prism is three disjoint edges. Every optimum picks one endpoint of each edge; the reconfiguration graph is the three-cube \(Q_3\).

Finally, for any graph, a maximum independent set is dominating. If replacing a selected vertex \(v\) by an unselected vertex \(w\) preserves maximum independence, then \(w\) was not adjacent to any vertex of the original set except \(v\), while domination requires at least one selected neighbor of \(w\). Therefore \(w\) is adjacent to \(v\). Thus every legal jump is a slide, as asserted.

## Verification
Two standalone implementations were executed from the actual package inputs. `prism_direct.py` independently builds each prism from the adjacency definition, examines every vertex-subset bitmask of the required optimum size for orders three through five, verifies each exchange really is a slide, computes all degrees/components and breadth-first distances, and obtains diameter nine at order five. `prism_check.py` separately enumerates intersecting families from the ground two-subsets, constructs compatible ordered layer pairs, and computes all optimum moves for orders five, six and seven. The outputs agree at order five and corroborate the uniform theorem at six and seven. Finite experiments do not prove the all-order component theorem; the star classification and exchange argument do.

## Relationship to prior work
The classical Erdős–Ko–Rado intersecting-family theorem gives the independent-set number and star extremizers for ordinary two-subset Kneser graphs, but does not directly give the prism's two-layer disjointness, optimal-state census, or mobility. The 2014 analysis by Bonsma, Kamiński and Wrochna develops the token sliding/jumping framework and records the general equivalence for maximum independent sets; this equivalence is prior art, not a new contribution. Das and Tran analyze Erdős–Ko–Rado stability and random subgraphs, not this Cartesian prism's optimum exchange graph. The novelty claimed here is solely the sharp four-regime reconfiguration classification, particularly the order-five connectivity versus the all-larger-order disjoint-edge decomposition. No absolute publication-priority certification is asserted.

## Limitations
The theorem concerns two-element Kneser graphs and only maximum independent sets under one-vertex exchanges; it asserts nothing for general \(k\)-uniform Kneser prisms or smaller independent sets. The nine-step diameter is established by finite exhaustive search on the twenty-vertex prism, not a closed symbolic distance formula. Some indexed and older publications might contain equivalent results despite searches. Independent external mathematical review remains unperformed.

## References
- P. Bonsma, M. Kamiński and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1, publicly posted 2014-03-03; full accessible HTML inspected, especially Sections 1–3 and Proposition 1.
- S. Das and T. Tran, *Removal and Stability for Erdős–Ko–Rado*, arXiv:1412.7885v1, publicly posted 2014-12-26; full accessible HTML inspected, particularly Sections 1 and 3. The original 1961 intersecting-family result is standard background.
