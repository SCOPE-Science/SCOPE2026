# The Dürer two-independence complex is a mixed-dimensional sphere wedge

## Finding
For the twelve-vertex Dürer graph \(D=GP(6,2)\), the two-independence complex has the exact **integral homotopy type**
\[
\boxed{\operatorname{Ind}_2(D)\simeq\bigvee^{3}S^3\vee S^4.}
\]
In particular, reduced integral homology is free of rank \(3\) in degree \(3\), free of rank \(1\) in degree \(4\), and zero in all other degrees. This is a mixed-dimensional sphere wedge on a canonical cubic polyhedral graph. The underlying complex has dimension \(5\); this finding is a homotopy classification, not a claim that the simplicial complex is a four-dimensional manifold.

## Assumptions and scope
The graph is defined on twelve labeled vertices \(u_0,\ldots,u_5,v_0,\ldots,v_5\), with indices modulo \(6\). Its undirected edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for \(0\le i<6\). This is the generalized Petersen graph \(GP(6,2)\), also known as the Dürer graph. For any finite simple graph \(G\), \(\operatorname{Ind}_2(G)\) has a simplex for each vertex subset whose induced connected components have at most two vertices.

Set the machine vertex labels \(0,\ldots,5\) equal to \(u_0,\ldots,u_5\) and \(6,\ldots,11\) equal to \(v_0,\ldots,v_5\). A subset is encoded by the integer whose binary positions are its vertices. Empty faces are included in the abstract complex but omitted from the nonempty face poset for ordinary discrete Morse matching. The claim concerns the indicated graph and threshold exactly, not a general formula for all generalized Petersen graphs.

## Proof
**1. Finite face characterization.** A vertex set lies in \(\operatorname{Ind}_2(D)\) precisely when it contains no three-element set whose induced subgraph is connected. For three distinct vertices, connectivity is equivalent to the presence of at least two edges among them. This gives an independent forbidden-triple characterization that the accompanying verifier compares against a connected-component flood fill for every one of the \(2^{12}\) vertex subsets. There are exactly \(32\) forbidden triples and \(809\) nonempty simplices. The face numbers in dimensions \(0\) through \(5\) are
\[
(12,66,188,285,204,54).
\]

**2. Explicit acyclic face-poset matching.** Apply consecutive element-toggle matchings using the fixed vertex order
\[
(2,11,10,0,6,8,7,1,5,9,3,4).
\]
At each step, match every still-unmatched pair of nonempty faces \(\sigma\subset\sigma\cup\{v\}\) when both exist. The order gives \(402\) pairs, leaving precisely one critical zero-cell (mask \(4\)), the three critical three-cells (masks \(210,585,1313\)), and one critical four-cell (mask \(866\)). Specifically, the critical three-cells are the subsets \(\{1,4,6,7\}\), \(\{0,3,6,9\}\), and \(\{0,5,8,10\}\); the critical four-cell is \(\{1,5,6,8,9\}\). The matching is acyclic: the verifier constructs the full directed Hasse graph, directs matched covers upward and all other covers downward, and topologically sorts its \(809\) vertices and \(3180\) directed cover relations without residue. This finite acyclicity check is exhaustive, not a random test. The matching therefore yields a CW model with precisely the five indicated cells.

**3. Integral attaching degree.** Orient each simplex in ascending vertex-label order. For a matched lower three-simplex \(\sigma\) paired with a four-simplex \(\tau\), the coefficient of \(\sigma\) in \(\partial\tau\) is \(\pm1\). Recursively eliminate such matched lower three-simplices from the boundary of the critical four-simplex, replacing a coefficient on \(\sigma\) using the signed relation \(\partial\tau\). Discard degree-three cells matched as upper cells with degree-two partners, and retain critical three-cells. Acyclicity makes this integral gradient-path recursion finite. Its exact output is the zero vector on all three critical three-cells; in particular the signed Morse differential from the critical four-cell is \((0,0,0)\). The package's `verification.py` implements and checks this calculation from the graph and matching rather than reading a precomputed boundary matrix.

**4. Upgrade from homology to homotopy.** The discrete-Morse CW complex has one zero-cell, three three-cells, and one four-cell, with no one- or two-cells. Its three-skeleton is therefore \(S^3\vee S^3\vee S^3\). The Hurewicz map from its third homotopy group to its third integral homology group is an isomorphism. The attaching map of the lone four-cell represents an element of \(\pi_3(S^3\vee S^3\vee S^3)\cong\mathbb Z^3\), and this element is the vector of integral Morse attaching degrees just calculated. As that vector is zero, the attaching map is nullhomotopic. Hence the four-cell splits as another wedge summand \(S^4\), proving the displayed integral homotopy equivalence.

## Verification
Run `python3 verification.py` with a standard Python 3 interpreter; no external packages or network access are required. The checker independently enumerates connected-component admissibility and forbidden-triple admissibility over all \(4096\) masks, verifies all face numbers, rebuilds the \(402\) matching pairs and all \(3180\) face covers, exhaustively verifies acyclicity, computes the signed integer Morse differential, and independently calculates every mod-two simplicial boundary rank. The boundary ranks in dimensions one through five are \((11,55,133,149,54)\), consistent with reduced Betti ranks \((0,0,0,3,1,0)\) in dimensions zero through five. Mod-two homology is a corroborating check; integral homotopy follows from the acyclic matching and **integer** attaching-degree calculation.

## Relationship to prior work
Deshpande and Singh (2020) develop the theory of higher-independence complexes and give complete homotopy results for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees. The present cubic graph is none of these families; their general element-matching method is a tool used here, not an existing classification of this graph. Deshpande, Shukla, and Singh (2020) show that for a chordal graph the dimension of every sphere appearing in an \(r\)-independence wedge is of the form \(rj-1\). The Dürer graph has a chordless outer six-cycle and is not chordal. Its **even-dimensional** \(S^4\) summand at threshold two therefore highlights a phenomenon outside that theorem's hypotheses. Abdelmalek and collaborators (2021) extend results on shellability and vertex decomposability of higher-independence complexes for trees and caterpillars, not this graph.

Targeted comparisons included the aliases \(GP(6,2)\), Dürer graph, connected-triple hypergraph independence, and two-independence complex, along with relevant published research records. Closest indexed results concern the Petersen two-independence complex and ordinary independence complexes of other generalized Petersen graphs; they do not imply the stated mixed-dimensional homotopy type. No equivalent classification was identified in the examined material, but a finite search does not establish priority or rule out unindexed equivalent work.

## Limitations
Only the one explicitly specified graph and threshold are classified. No integral equivariant module, persistence inclusion map, or general theorem for \(GP(n,k)\) is asserted. The finite proof certifies all simplices and all Morse gradient incidences for this specific twelve-vertex graph, not an infinite family. Unindexed previous computations and inaccessible literature remain possible originality risks. Independent mathematical audit has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first public version 2020-01-15), Sections 2–4, especially the element matching and classified graph families. https://arxiv.org/abs/2001.05448
2. P. Deshpande, S. Shukla, and A. Singh, *Distance r-Domination Number and r-Independence Complexes of Graphs*, arXiv:2001.06775 (first public version 2020-01-19), Theorem 3 on chordal graphs. https://arxiv.org/abs/2001.06775
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (first public version 2021-06-21). https://arxiv.org/abs/2106.10863
