# Mixed-dimensional integral homotopy of the truncated-tetrahedral two-independence complex

## Finding
Let \(T\) be the twelve-vertex graph of the truncated tetrahedron. Its two-independence complex \(\operatorname{Ind}_2(T)\), formed by the vertex subsets whose induced connected components contain at most two vertices, has the **integral homotopy type**
\[
\boxed{\operatorname{Ind}_2(T)\simeq \bigvee^{3}S^{3}\vee\bigvee^{3}S^{4}.}
\]
The complex has 65 maximal faces: three of dimension three and 62 of dimension five. In particular, it is nonpure; its nonzero fourth homology lies in a dimension not occupied by any maximal face. These facts also obstruct nonpure shellability in the usual Björner--Wachs sense.

## Assumptions and scope
The graph is constructed from the tetrahedron with vertex set \(\{0,1,2,3\}\). Its twelve vertices are the ordered pairs \((a,b)\) with distinct entries. Distinct \((a,b)\) and \((c,d)\) are adjacent if \(a=c\), or if \((c,d)=(b,a)\). This is the standard truncated-tetrahedral graph: it has four disjoint triangular groups of three vertices and six reversal edges, for 18 edges total. For reproducible bitmasks, sort the twelve ordered pairs lexicographically and index them from zero.

For any vertex subset \(U\), the induced graph \(T[U]\) has connected components of size at most two if and only if it has maximum degree at most one. We include the empty face in augmented combinatorial calculations. The claimed wedge equivalence is an ordinary integral homotopy equivalence; it does not assert an equivariant homotopy type or a theorem for other truncated polyhedra.

## Proof
**Finite face model.** For each mask \(U\) of the twelve vertices, test that every vertex in \(U\) has at most one neighbor in \(U\). Exhaustive enumeration of all \(4096\) masks gives \(864\) admissible faces including the empty face, with nonempty face vector \((12,66,192,303,228,62)\) in dimensions zero through five. Exactly three facets have dimension three and 62 have dimension five.

**Acyclic discrete-Morse matching.** Apply successive toggles on currently unmatched faces in the vertex order
\[
(7,4,1,3,8,5,9,11,6,0,10,2).
\]
At each stage, pair an unmatched face omitting the current vertex with its one-vertex augmentation if that augmentation is also unmatched. This produces 429 augmented matched pairs and leaves three critical three-faces, with bitmasks \(540,1122,2313\), and three critical four-faces, with bitmasks \(2101,2164,3153\). The augmented empty face is paired with a singleton: removing that pair when passing to the ordinary nonempty face poset yields 428 pairs and one critical vertex in addition to those six higher-dimensional cells. Direct all 3432 ordinary face-poset covering relations from coface to face and reverse the matching covers. A complete topological sort visits every one of the 863 nonempty faces; the matching is therefore acyclic.

**Integral Morse attaching degrees.** Orient every face by its increasing vertex order. For a dimension-three face paired as the lower face with a four-face, solve its matching equation in the integral boundary of that four-face, substituting recursively along the acyclic matching graph. Faces paired as upper faces with two-faces project to zero, while critical three-faces project to their basis elements. Applying this reduction to the oriented boundaries of the three critical four-faces gives, in the displayed critical-face orders, the exact integer matrix
\[
\partial^{\mathrm{Morse}}_4=
\begin{pmatrix}0&0&0\0&0&0\0&0&0\end{pmatrix}.
\]
These entries are signed **integer** gradient-path sums, not numerical estimates or mod-two reductions. The attached standard-library checker supplies the complete deterministic rules and verifies the arithmetic.

**Homotopy deduction.** Forman's theorem supplies a CW homotopy model having one zero-cell, three three-cells and three four-cells, and no other cells. Its three-skeleton is \(\bigvee^{3}S^3\). The Hurewicz map \(\pi_3(\bigvee^{3}S^3)\to H_3(\bigvee^{3}S^3;\mathbb Z)\) is an isomorphism. Since every four-cell attaching degree is zero, all three attaching maps are nullhomotopic. This gives precisely the displayed wedge of three three-spheres and three four-spheres. The nonpure-shellability observation follows because homology of a nonpure shellable complex is a wedge of spheres with dimensions among the facet dimensions, whereas the present complex has dimension-four homology but no dimension-four facet.

## Verification
Run `python3 truncated_tetrahedron_ind2_verify.py` using only the Python standard library. It reconstructs the graph from oriented tetrahedron edges; evaluates every vertex mask; checks 429 augmented matching pairs; checks every directed Hasse cover and absence of directed cycles; calculates all nine entries of the exact integral Morse boundary; and independently computes ordinary simplicial boundary ranks over \(\mathbb F_2\). The success marker is `TRUNCATED_TETRAHEDRON_IND2_INTEGRAL_MORSE_OK`. The finite-field reduced Betti ranks are three in dimension three and three in dimension four, and zero otherwise. The integer gradient calculation, not finite-field agreement, establishes the full integral homotopy classification.

## Relationship to prior work
Deshpande and Singh's foundational higher-independence paper (first posted January 15, 2020) treats complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees. It does not cover the truncated tetrahedron. Chordal-graph higher-independence theorems also do not apply: this graph has an induced six-cycle on the bitmask vertices \(0,1,3,4,6,7\). Existing exact calculations for the **same graph** concern its ordinary edge-matching complex, three-cut complex, and graph-metric Čech or Vietoris--Rips nerves. These differ from the present vertex-subset two-independence complex, including in their ground sets or face conditions; their homotopy statements do not imply this one. Papers on dissociation numbers investigate maximum cardinalities of degree-one induced vertex sets rather than the homotopy type of the entire complex. Targeted literature and mathematical-record comparisons did not identify a dominating theorem or equivalent calculation.

## Limitations
The claim is restricted to the twelve-vertex truncated-tetrahedral graph at cutoff two. There is no assertion about an entire family of polyhedral graphs, equivariant integral representations, integral maps between filtration stages, or priority over inaccessible and unindexed work. The exact finite certificate has been checked here; independent external review has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first public January 15, 2020, https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863, first public June 21, 2021, https://arxiv.org/abs/2106.10863.
3. F. Bock, J. Pardey, L. D. Penso, and D. Rautenbach, *Relating the Independence Number and the Dissociation Number*, Journal of Graph Theory 104 (2023), DOI:10.1002/jgt.22965.
4. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, publicly available exact mathematical calculation, October 2026; comparison concerns the ordinary **edge-matching** complex, not this two-independence complex.
5. *Three-cut complexes of four-cycle-free graphs with triangles*, publicly available exact mathematical calculation, October 2026; comparison concerns the distinct three-cut construction.
