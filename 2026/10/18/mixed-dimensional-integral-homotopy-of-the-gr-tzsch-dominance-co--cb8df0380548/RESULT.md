# Mixed-dimensional integral homotopy of the Grötzsch dominance complex

## Finding
Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, obtained by the ordinary Mycielski construction on the five-cycle. Let \(\mathcal D(G)\) be its dominance complex: a vertex subset is a face exactly when its complement is a dominating set of \(G\). Then
\[
\boxed{\mathcal D(\mu(C_5))\simeq S^5\vee S^6\vee S^6.}
\]
Consequently its only nonzero reduced integral homology groups are \(\widetilde H_5\cong\mathbb Z\) and \(\widetilde H_6\cong\mathbb Z^2\). The complex is nonpure (its facets have dimensions five, six, and seven), yet has an explicit integral mixed-dimensional sphere-wedge homotopy type. This is a computation for the canonical smallest triangle-free four-chromatic graph, not a formula for arbitrary Mycielskians.

## Assumptions and scope
Use labeled vertices \(0,\ldots,10\). The original five-cycle is on \(0,\ldots,4\); the clone of vertex \(i\) is \(5+i\), for \(0\le i\le4\); vertex \(10\) is the apex. With cycle indices modulo five, edges are \(\{i,i+1\}\), \(\{5+i,i-1\}\), \(\{5+i,i+1\}\), and \(\{5+i,10\}\) for all \(0\le i\le4\), giving exactly 20 distinct undirected edges. A set \(U\) dominates if \(\bigcup_{u\in U}N_G[u]=V(G)\). Thus \(\mathcal D(G)=\{\sigma\subseteq V(G):V(G)\setminus\sigma\text{ dominates }G\}\).

Vertices of a face are encoded by the integer mask \(\sum_{i\in\sigma}2^i\) in the standalone verifier. This is a complete finite determination for one explicitly defined graph. All homology statements have integral coefficients. No conclusion for later Mycielski iterations, deletions, or other eleven-vertex graphs is asserted.

## Proof
**Complete face generation.** For each vertex \(i\), form the bitmask \(N_G[i]\) of its closed neighborhood. A complement \(V(G)\setminus\sigma\) dominates precisely when the bitwise union of its vertex-neighborhood masks equals the eleven-bit full mask. The complete search over all \(2^{11}\) subsets gives 1,435 faces including the empty face. The nonempty face-vector in dimensions zero through seven is
\[
(11,55,165,325,422,331,120,5).
\]
The maximal-face inventory is one facet of dimension five, 85 of dimension six and five of dimension seven. Each admitted face has every subface admitted; the verifier checks this directly.

**A complete acyclic matching.** Work first with the augmented face poset (including the empty face). Visit vertices in this fixed order:
\[
(9,4,5,0,6,3,1,7,8,2,10).
\]
For each visited vertex \(v\), pair each currently unmatched face not containing \(v\) with its union with \(\{v\}\) if both are still unmatched. Remove pairs immediately, using increasing integer-mask order within a stage. This gives 716 pairs and leaves precisely three unmatched face masks: 415, 1071, 1510, respectively of simplicial dimensions six, five, six. The first pair is the empty face with the singleton \(\{9\}\). Discard only this augmented pair and retain that singleton as an ordinary critical vertex. There are then 715 ordinary pairs and four critical cells with dimensions \(0,5,6,6\).

Orient all cover edges in the nonempty-face Hasse diagram downward, except that matched cover edges point upward. The complete diagram has 1,434 vertices and 6,881 arrows; indegree-zero elimination visits all 1,434 vertices. The matching is therefore acyclic, not merely an experimentally plausible sequence. Forman's discrete Morse theorem yields a CW complex with one critical zero-cell, one five-cell and two six-cells.

**Integral attaching maps.** The only potentially nonzero Morse differential joins the critical six-cells to the five-cell. With the standard increasing-vertex orientation \(\partial[v_0,\ldots,v_k]=\sum_j(-1)^j[v_0,\ldots,\widehat v_j,\ldots,v_k]\), eliminate the 715 matched face pairs over \(\mathbb Z\). Let \(p(s)\) be the projection of an oriented five-face onto the unique critical five-face: it is one on critical mask 1071, zero on any five-face paired downward, and, if \(s\) is paired upward to a six-face \(h=s\cup\{v\}\), the relation \(\partial h=0\) gives
\[
p(s)=-\varepsilon(h,s)\sum_{t\subset h,\ |t|=6,\ t\ne s}\varepsilon(h,t)p(t),
\]
where \(\varepsilon(h,t)\in\{-1,1\}\) is the oriented simplicial incidence. The acyclic matching guarantees recursive termination. The projections of the signed ordinary boundaries of critical masks 415 and 1510 are both exactly zero. Thus the integral Morse boundary matrix is \((0\ \ 0)\).

The CW five-skeleton is a single five-sphere, because there are no cells in dimensions one through four. The homotopy classes of attaching maps of its six-cells are in \(\pi_5(S^5)\cong\mathbb Z\), and are determined by their degrees. Since the two integral cellular boundary coefficients are zero, both attaching maps are nullhomotopic. The Morse CW model is therefore homotopy equivalent to \(S^5\vee S^6\vee S^6\), proving the statement, including integral torsion-freeness.

## Verification
Both supplied Python programs are standalone standard-library scripts. Run `python3 evidence/verify_morse.py` and `python3 evidence/verify_incidence.py` after extracting the embedded files. The first rebuilds the graph, enumerates all 1,435 faces, checks all 715 ordinary matching pairs, verifies acyclicity by complete Hasse-diagram topological sort, and recomputes the **signed integer** Morse boundary. The second independently constructs a symmetric adjacency matrix, enumerates all 91 minimal dominating sets and their complementary facets, regenerates every simplex, and calculates full simplicial boundary ranks over both \(\mathbb F_2\) and \(\mathbb F_3\). Its unreduced mod-two Betti vector is \((1,0,0,0,0,1,2,0)\), and the mod-three ranks agree. Recorded exact outputs are included. The finite-field calculations are corroboration; the integral Morse boundary and acyclicity establish the integral homotopy type.

## Relationship to prior work
Matsushita and Wakatsuki (arXiv:2312.02639, first public 2023-12-05) establish \(\mathcal D(G)^\vee=\mathcal N(\overline G)\), give connectivity and related methods, and compute specified grid families; their paper does not provide the homotopy classification of \(\mathcal D(\mu(C_5))\). The complement and Alexander duality equivalence was explicitly checked here: it changes the formulation but does not make this fixed graph computation a formal corollary of the general duality theorem alone.

Taylan (arXiv:1501.06754) develops matching methods for nonflag complexes and establishes the sphere homotopy type of dominance complexes of chordal graphs; \(\mu(C_5)\) is nonchordal and its mixed-dimensional result is not covered. Previously documented topological calculations for the Grötzsch *matching complex* use edge sets as vertices and concern \(\operatorname{Ind}(L(\mu(C_5)))\), rather than the vertex-set dominance complex here. Likewise, formulas for open-neighborhood complexes of high-girth graphs do not apply to the dense complement \(\overline{\mu(C_5)}\) needed for combinatorial Alexander duality. The stated homotopy type and two adjacent-degree homology generators are not implied by these results.

## Limitations
This is a single canonical graph, not an infinite family or classification of all triangle-free four-chromatic graphs. The proof supplies a reproducible exact finite acyclic matching and integral attaching map calculation, rather than a closed combinatorial formula for arbitrary Mycielski constructions or an equivariant integral module. Exhaustive enumeration of one graph does not prove global novelty; an unindexed calculation of this same dominance complex, or of the Alexander-dual neighborhood complex with sufficient integral information, remains a residual literature risk. Independent mathematical validation is not claimed.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first public 2023-12-05); accessible revised full text https://arxiv.org/html/2312.02639v2.
2. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type Of Devoid Complexes Of Graphs*, arXiv:1501.06754v1 (2015), https://arxiv.org/html/1501.06754v1.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. J. Mycielski, *Sur le coloriage des graphes*, Colloquium Mathematicum 3 (1955), 161–162.
