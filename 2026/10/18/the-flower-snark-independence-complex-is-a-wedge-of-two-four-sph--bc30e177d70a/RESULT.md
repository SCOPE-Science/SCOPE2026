# The flower-snark independence complex is a wedge of two four-spheres

## Finding

Let \(F_5\) be the twenty-vertex flower snark in the explicit edge presentation below, and let \(K=\operatorname{Ind}(F_5)\) be its ordinary independence complex, meaning that an edge-free set of graph vertices is a simplex. There is an integral homotopy equivalence
\[
K\simeq S^4\vee S^4.
\]
Moreover, the *entire* graph automorphism group is the dihedral group \(D_{10}\) of order twenty. If \(r\) is its distinguished order-ten rotation and \(s\) a reflection as defined below, then, as a rational representation,
\[
\widetilde H_4(K;\mathbb Q)\cong\mathbf 1\oplus\varepsilon,
\qquad\varepsilon(r)=-1,\quad\varepsilon(s)=+1.
\]
Equivalently, for each integer \(k\) with \(0\le k<10\),
\[
\operatorname{tr}\!\left(r^k\mid\widetilde H_4(K;\mathbb Q)\right)
=\operatorname{tr}\!\left(sr^k\mid\widetilde H_4(K;\mathbb Q)\right)
=1+(-1)^k.
\]
Thus the two-dimensional rational homology has exactly one line fixed by the entire graph-automorphism group. The reduced integral homology is free of rank two in degree four and vanishes in every other degree. The rational representation statement makes no assertion of an integral direct-sum splitting into characters.

## Assumptions and scope

The graph is defined for the single parameter \(n=5\), not for all odd flower-snark parameters. Index sets and all congruences in the following vertex presentation are literal. Put
\[
V(F_5)=\{a_i,b_i:0\le i<5\}\ \sqcup\ \{c_j:0\le j<10\}.
\]
Its thirty undirected edges are
\[
\{a_ib_i,a_ic_i,a_ic_{i+5},b_ib_{i+1\pmod5}:0\le i<5\}
\ \cup\ \{c_jc_{j+1\pmod{10}}:0\le j<10\}.
\]
An orientation of simplices is induced by the vertex order \(a_0,\ldots,a_4,b_0,\ldots,b_4,c_0,\ldots,c_9\). Define \(r\) by simultaneous rotation \(a_i\mapsto a_{i+1}\), \(b_i\mapsto b_{i+1}\), and \(c_j\mapsto c_{j+1}\) modulo five or ten, respectively. Define \(s\) by negating all the indices modulo their respective lengths. Their actions preserve the edge list and obey \(r^{10}=s^2=1\) and \(srs=r^{-1}\).

The graph presentation agrees with the flower-snark definition in Zheng–Lin–Yang–Yang (2008) and with the standard database encoding; the earliest day-verified public reference used to identify the graph is dated 2008-01-31. Isaacs's earlier foundational publication is from March 1975, but its available scanned source does not establish an exact calendar day; the 2008 date is **not** a claim of the graph's first discovery.

## Proof

**The graph and its symmetry.** The edge list has twenty vertices, thirty edges, and degree three at every vertex. The graph has no triangles (checked directly from the edge list), so every five-cycle is induced. Direct exhaustive inspection of five-element vertex subsets exhibits exactly one five-cycle, the \(b\)-cycle \(b_0b_1b_2b_3b_4b_0\). Any automorphism must act dihedrally on this unique cycle, allowing at most ten choices. Each \(b_i\) has exactly one neighbor off that cycle, namely \(a_i\), so the action on all \(a_i\) is then forced. The remaining \(c\)-vertices form a ten-cycle. Once the images of the \(a_i\) are prescribed, its only remaining freedom is to choose which of the pair \(c_i,c_{i+5}\) lies over one fixed \(a_i\). All choices at other indices are forced by adjacency around the \(c\)-cycle. Hence there are at most twenty automorphisms. The twenty distinct maps \(r^k\) and \(sr^k\), for \(0\le k<10\), all preserve the edges, giving the entire group \(D_{10}\).

**The finite independence complex.** Enumerate all masks \(m\) with \(1\le m<2^{20}\); retain exactly those containing no graph edge. The resulting simplex counts in dimensions \(0,1,\ldots,8\) are, respectively,
\[
(20,160,660,1510,1923,1310,450,75,5),
\]
for 6,113 nonempty simplices. The enumeration is exhaustive because it tests all possible vertex subsets. The necessary recursion and edge checks are reproduced in `verify_flower_snark.py`.

**Acyclic discrete Morse reduction.** Number the vertices \(0\) through \(19\) in the displayed order. Start with every nonempty simplex unmatched. In successive rounds \(v=0,\ldots,19\), scan all simplices in increasing binary-mask order, pairing an unmatched simplex that does not contain \(v\) with its unmatched one-vertex extension obtained by adding \(v\), whenever both are available. Remove each pair immediately. This explicit combinatorial vector field has 3,054 pairs and exactly five critical faces: one vertex, three four-simplices, and one five-simplex. The three critical four-simplex masks are \(140864,280736,534688\), and the critical five-simplex mask is \(696896\).

Reverse the matched arrows in the directed Hasse diagram and point every unmatched cover relation downward. The graph has 6,113 nodes and 29,610 directed cover relations. The reproduced topological-sort test removes every node, proving acyclicity. Forman's discrete Morse theorem therefore provides a homotopy-equivalent CW complex with one point, three four-cells, and one five-cell.

**Integral attaching coefficient.** Orient each simplex by increasing numbered vertices. Use the signed simplicial differential \(\partial[v_0,\ldots,v_p]=\sum_i(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_p]\). To compute the degree-four Morse projection, map every critical four-face to itself and every matched upper four-face to zero. If a four-face \(f\) is a matched lower face of a five-face \(u\), solve the boundary equation for \(f\): its projected value is the negative sum of the projections of the other four-faces of \(u\), divided by the incidence \(\langle\partial u,f\rangle\in\{1,-1\}\). The acyclic matching makes this recurrence well founded. The resulting one-by-three Morse boundary, ordered by the ascending masks above, is exactly
\[
\partial^{\mathrm{Morse}}_5=(1,0,-1).
\]
This is a primitive integral vector. Before attachment, the three four-cells form \(\bigvee^3 S^4\). Since \(\pi_4(\bigvee^3 S^4)\cong\mathbb Z^3\), the homotopy class of the five-cell attaching map is completely determined by its three degrees. A unimodular change of the four-sphere generators takes \((1,0,-1)\) to \((1,0,0)\), and the corresponding five-cell kills exactly one sphere. Consequently the Morse CW complex, and hence \(K\), is homotopy equivalent to \(S^4\vee S^4\). This also proves the claimed complete integral homology without a torsion assumption.

**Character of the full symmetry action.** For a simplicial automorphism \(g\), the reduced Lefschetz number is the alternating signed count of its fixed oriented simplices, including the empty augmented simplex with contribution \(-1\):
\[
\widetilde L(g)= -1+\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}(-1)^{\dim\sigma}\operatorname{sgn}(g\text{ on the ordered vertices of }\sigma).
\]
Because the reduced homology is concentrated in even degree four, \(\widetilde L(g)\) is the trace on that homology. Exhaustive signed fixed-face enumeration for all twenty automorphisms gives \(\widetilde L(r^k)=\widetilde L(sr^k)=2\) for even \(k\), and zero for odd \(k\). These are precisely the character values of \(\mathbf1\oplus\varepsilon\) with \(\varepsilon(r)=-1\) and \(\varepsilon(s)=1\); rational finite-group representations are determined by character.

## Verification

Run `python3 verify_flower_snark.py` using only Python 3 and the standard library. The program reconstructs all graph edges and all \(2^{20}\) vertex subsets; checks that its local graph is isomorphic to the standard Sage graph6 encoding; enumerates all 6,113 faces; constructs all 3,054 Morse pairs; checks acyclicity across all 29,610 Hasse covers; computes the signed primitive Morse differential; establishes the graph-automorphism bound; and enumerates all twenty Lefschetz traces. It exits successfully only if every asserted certificate and theorem-specific identity holds, printing `VERIFY_OK_FLOWER_SNARK_INDEPENDENCE_HOMOTOPY_AND_FULL_DIHEDRAL_CHARACTER`.

The complete code, rather than a detached log or partial face sample, is the finite certificate. The graph-complex computation is exhaustive for the **specified twenty-vertex graph**; it does not establish a theorem for all flower snarks.

## Relationship to prior work

Isaacs (1975) introduced the flower-snark construction in cubic graph coloring. Zheng–Lin–Yang–Yang (2008) give exactly the vertex-edge parametrization used here, with a theorem on crossing numbers rather than independence-complex homotopy. The Sage graph catalog supplies an independent canonical encoding of the same graph. Published computations on the independence complexes of other twenty-vertex cubic graphs (such as generalized Petersen and Desargues graphs) concern different graphs and do not imply the present result. General works on independence complexes and related cubic graph families do not, in the inspected material, give this specific homotopy classification or its full dihedral rational character. No assertion of priority follows merely from a negative database search.

## Limitations

The statement concerns only the first genuine twenty-vertex flower snark \(F_5\); there is no all-rank or general odd-parameter conclusion. The isomorphism of representations is rational, not a claim of an integral character splitting. The bibliographic comparison was limited to accessible literature, named-graph aliases, relevant computational records and inspected primary materials; an unindexed or inaccessible equivalent statement remains possible. The dated 2008 reference establishes a day-verified public *definition* of the exact graph but does not displace Isaacs's earlier month-and-year-dated work. No independent audit of the mathematics has been performed.

## References

1. R. Isaacs, *Infinite Families of Nontrivial Trivalent Graphs Which are Not Tait Colorable*, American Mathematical Monthly 82 (March 1975), 221–239. https://homepages.math.uic.edu/~kauffman/Isaacs.pdf
2. W. Zheng, X. Lin, Y. Yang and X. Yang, *The Crossing Number of Flower Snarks and Related Graphs*, Ars Combinatoria 86 (2008), 57–64; source date 2008-01-31. https://combinatorialpress.com/ars-articles/volume-086-ars-articles/the-crossing-number-of-flower-snarks-and-related-graphs/
3. SageMath, *Graph Generators: FlowerSnark* documentation and graph6 catalog. https://sagemath.gitlab.io/documentation/html/en/reference/graphs/sage/graphs/graph_generators.html
4. Goyal, Shukla and Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs* (2019), https://arxiv.org/abs/1905.06926 (abstract-level comparison only; no claim of exhaustive coverage).
