# Integral homotopy and affine homology character of the Paley-19 out-neighborhood complex

## Finding
Let \(T\) be the quadratic-residue tournament with vertex set \(\mathbb F_{19}\) and \(u\longrightarrow v\) if and only if \(v-u\) is a nonzero square modulo \(19\). Its ordinary directed **out-neighborhood** complex \(X=\overrightarrow{\mathcal N}(T)\) is defined by the condition that a finite nonempty vertex set is a simplex if all of its vertices have one common incoming arc from some vertex of \(T\). Then the following is an integral homotopy equivalence:
\[
X\simeq S^2\vee\bigvee^{78}S^3.
\]
Under the natural order-\(171\) affine group \(G=\mathbb F_{19}\rtimes Q\), where \(Q\subset\mathbb F_{19}^{\times}\) is the group of nine squares, the rational reduced second-homology character is identically \(1\). The rational reduced third-homology character is \(78\) on the identity, \(2\) on the eighteen nonidentity translations, \(-3\) on the thirty-eight elements with multiplier of order three, and \(0\) on the remaining 114 elements. Consequently
\[
\dim_{\mathbb Q}\widetilde H_2(X;\mathbb Q)^G=1,
\qquad \dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)^G=0.
\]

## Assumptions and scope
This theorem concerns one specific directed tournament, not its underlying complete graph, and the *out*-neighborhood complex, not the directed flag complex or an ordinary graph-neighborhood complex. Vertex residues are represented by \(0,1,\ldots,18\). The outgoing square set is
\[Q=\{1,4,5,6,7,9,11,16,17\}.\]
Its nineteen maximal simplices are \(v+Q\), one for each \(v\in\mathbb F_{19}\), each with nine vertices. The affine group acts by \(x\mapsto ax+b\), with \(a\in Q\) and \(b\in\mathbb F_{19}\). The representation statement is over \(\mathbb Q\); no equivariant splitting of the wedge is asserted.

## Proof
**1. Exhaustive finite model.** A simplex is exactly a subset of one of the nineteen translated square sets. Enumerating their submasks gives \(8247\) faces including the empty face. Independently scanning all \(2^{19}\) vertex subsets and testing for an outgoing-neighborhood witness yields exactly the same face set. The nonempty face counts in dimensions \(0\) through \(8\) are respectively
\[
(19,171,969,2223,2394,1596,684,171,19).
\]
The difference-set check also verifies that each pair of distinct maximal faces intersects in four vertices.

**2. A complete acyclic matching.** Represent a face by its nineteen-bit integer mask. Starting with all nonempty faces unmatched, visit vertices \(0,1,\ldots,18\). At each vertex, process currently unmatched faces in increasing order of (cardinality, integer mask); when both a face not containing the vertex and its union with that vertex remain unmatched, pair them and remove both. This pairs exactly \(4080\) edges of the face-poset Hasse diagram. Reverse the orientation of precisely these matched incidences, orienting every other incidence from a higher-dimensional face toward a lower-dimensional one. A complete topological-sort test visits all \(8246\) nonempty faces through all \(40014\) incidences, so this directed graph is acyclic, not merely sampled. Exactly one critical zero-cell, four critical two-cells and eighty-one critical three-cells remain, and there are no other critical cells. Forman's discrete Morse theorem therefore gives a homotopy-equivalent CW model with precisely those cell counts.

**3. Integral attaching degrees.** Orient every simplex by increasing vertex order, and use signed simplicial boundaries. Follow gradient paths through the matched triangle–tetrahedron pairs to express the boundary of each critical three-cell as an integral combination of the four critical two-cells. This produces an exact \(4\times81\) integer Morse boundary matrix \(B\), with rows indexed by the lexicographically increasing critical two-cell bitmasks and columns by the critical three-cell bitmasks. Every column \(c\) satisfies
\[c_0-2c_1-c_2+c_3=0,\]
so \(\operatorname{rank}_{\mathbb Q}B\le3\). The minor using rows \(0,1,2\) and columns \(0,1,4\) has determinant \(-1\), establishing \(\operatorname{rank}B=3\) and proving that its three nonzero Smith factors are units. The verifier computes all these entries by signed gradient recursion, checks every column relation, and explicitly evaluates this minor. There are no critical one-cells, so the CW two-skeleton is a bouquet of four two-spheres, and its three-cell attaching maps lie in \(\pi_2\) of that bouquet, canonically \(\mathbb Z^4\). Integral unimodular changes of bases for the two- and three-cells, realized through homotopy equivalences and cellular slides, reduce the attaching map to three unit attachments and seventy-eight null attachments. Cancelling the three unit pairs yields exactly one two-sphere and seventy-eight three-spheres. This proves the displayed integral homotopy type (not merely rational or mod-two homology).

**4. Affine character.** The order-\(171\) group preserves each face because multiplication by a square permutes \(Q\). Its action on \(\widetilde H_2(X;\mathbb Q)\cong\mathbb Q\) is a one-dimensional rational representation; the odd order forces it to be trivial. For every one of the \(171\) permutations \(g\), compute the signed simplicial Lefschetz number by summing \((-1)^{\dim \sigma}\) times the sign of the induced vertex permutation over all nonempty simplices \(\sigma\) fixed as sets. The Lefschetz identity then reads
\[L(g)=1+1-\operatorname{tr}\bigl(g\mid\widetilde H_3(X;\mathbb Q)\bigr).\]
The complete signed face calculation yields the stated four character values and multiplicities. Average the third-homology traces over the group:
\[
\frac{78+18(2)+38(-3)+114(0)}{171}=0.
\]
The second-homology invariant rank is one, as asserted.

## Verification
Run `python3 checks/paley19_neighborhood_verifier.py` with Python 3 and no third-party dependencies. The complete expected standard output is `checks/verification_output.txt`. The checker independently constructs every face in two ways, verifies the full directed acyclicity of the specified matching, computes the exact integral Morse boundary and its unimodular minor, independently computes all mod-two simplicial boundary ranks, and checks every affine permutation and signed Lefschetz trace. The independent mod-two calculation gives reduced Betti numbers \(1\) in dimension \(2\), \(78\) in dimension \(3\), and \(0\) otherwise. The finite certificate and the topological reduction together prove the integral homotopy statement; mod-two ranks alone would not suffice.

## Relationship to prior work
Dochtermann and Singh (first public version 24 August 2021) define directed neighborhood complexes, identify their connection with directed-edge Hom complexes, and prove general results on their homology; no explicit Paley-19 out-neighborhood homotopy or affine character is stated in the inspected version. Govc, Levi and Smith study *directed flag* (tournaplex) constructions, where faces are governed by transitivity rather than sharing an incoming neighbor. Published computations of the Paley-19 directed flag complex and its affine character likewise concern this distinct simplicial complex and do not imply the present homotopy or character. The already known Paley-11 out-neighborhood calculation concerns a different ground field and does not imply the nineteen-vertex case. Searches of related terminology and numerical signatures disclosed no equivalent theorem, but absence from indexed sources cannot establish absolute priority.

## Limitations
The theorem is restricted to the stated nineteen-vertex tournament and its natural affine subgroup, not necessarily the entire combinatorial automorphism group. It establishes a nonequivariant integral homotopy equivalence and the rational action on homology; it does **not** produce an equivariant wedge decomposition, calculate higher homotopy groups, or classify all doubly regular tournaments. Mathematical novelty remains subject to independent literature verification and any unindexed earlier calculation.

## References
- A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948v1 (first public 2021-08-24), https://arxiv.org/abs/2108.10948 .
- D. Govc, R. Levi and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, https://doi.org/10.1007/s41468-021-00068-0 (2021); comparison of distinct simplicial constructions.
