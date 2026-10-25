# A mixed-dimensional sphere wedge from the Paley tournament on 23 vertices

## Finding

Let \(P_{23}\) be the quadratic-residue tournament on \(\mathbb Z/23\mathbb Z\): the directed edge \(i\to j\) occurs exactly when \(j-i\) is a nonzero quadratic residue modulo \(23\). Its directed out-neighborhood simplicial complex \(K=\mathcal N^+(P_{23})\) has the integral homotopy type
\[
\boxed{K\simeq\left(\bigvee^{209}S^3\right)\vee S^4.}
\]
Consequently its only nonzero reduced integral homology groups are \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{209}\) and \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z\). This is a homotopy assertion, not merely a finite-field Betti-number computation.

## Assumptions and scope

The vertex set is \(V=\{0,1,\ldots,22\}\), all arithmetic being modulo \(23\). Put
\[
Q=\{1,2,3,4,6,8,9,12,13,16,18\}.
\]
The facets of \(K\) are exactly the 23 sets \(v+Q\), for \(v\in V\). A nonempty subset \(\sigma\subseteq V\) belongs to \(K\) exactly when \(\sigma\subseteq v+Q\) for some \(v\). In particular, \(K\) is the simplex-generated block complex of the cyclic Paley symmetric \(2\text{-}(23,11,5)\) design. The result concerns this exact tournament and its *out*-neighborhood complex, not the directed-flag complex and not the undirected Paley graph.

## Proof

**1. Exact finite complex and simplicial collapses.** Encode each nonempty face \(\sigma\) as \(b(\sigma)=\sum_{v\in\sigma}2^v\). For every facet, enumerate its nonempty submasks. Deduplication yields exactly \(42,297\) nonempty faces, with face counts in dimensions \(0\) through \(10\):
\[
(23,253,1771,6325,10373,10626,7590,3795,1265,253,23).
\]
Repeatedly choose the least bitmask that has exactly one immediate coface in the current complex and delete the face together with that coface. Uniqueness implies that the coface is maximal (otherwise the simplex property would supply another immediate coface). Every step is therefore an elementary simplicial collapse. This deterministic rule makes exactly \(19,184\) pairs and leaves a subcomplex \(L\) with \(3,929\) nonempty faces and face vector \((23,253,1180,1815,658)\) in dimensions \(0\) through \(4\). Thus \(K\simeq L\).

**2. Certified acyclic matching.** On the face poset of \(L\), process the vertices in the order
\[
(22,21,5,13,18,20,4,11,0,16,17,12,9,1,6,19,2,7,10,8,14,15,3).
\]
For each vertex \(v\), traverse currently unmatched faces in increasing bitmask order; pair every face not containing \(v\) with its union with \(\{v\}\), provided both are unmatched. Reverse all paired covering edges in the face-poset Hasse diagram and direct all other covering edges from the larger face to the smaller face. The entire resulting graph has \(3,929\) nodes and \(14,596\) arrows, and topological sorting visits all nodes. Hence there is no directed cycle: this is a valid integral discrete-Morse matching. Its critical-cell vector has exactly one zero-cell, 212 three-cells, and four four-cells, with no other critical cells. Forman's theorem gives a homotopy-equivalent CW complex \(M\) with that cell vector. Its three-skeleton is a wedge of 212 three-spheres.

**3. Integral four-cell attachments.** Give each simplex the increasing-vertex orientation. To compute the integral cellular map \(\partial_4^M\), replace each noncritical three-face paired with a four-face by the negative of the other oriented three-faces of its paired four-face, divided by its incidence coefficient (which is \(\pm1\)); a three-face paired with a two-face contributes zero. The acyclic matching ensures termination, and the calculation is carried out recursively in the attached verifier. The resulting \(212\times4\) integer matrix has columns \(c_0,c_1,c_2,c_3\) with the exact entrywise relation
\[
c_0-c_1-c_2+c_3=0.
\]
The rows indexed by the critical three-face bitmasks \(8724,133252,270360\), restricted to the first three columns, form the matrix
\[
\begin{pmatrix}0&-1&1\\-1&0&-1\\0&0&1\end{pmatrix},
\]
whose determinant is \(-1\). Thus the integer matrix has rank exactly three, and its nonzero Smith invariants are exactly \((1,1,1)\): rank is at most three by the column relation and at least three by the displayed unit minor; that minor also forces the product of the three Smith invariants to be one.

**4. Homotopy, not just homology.** Since the three-skeleton of \(M\) is \(\bigvee^{212}S^3\), the Hurewicz isomorphism identifies its third homotopy and homology groups with \(\mathbb Z^{212}\). Each four-cell attaching map is therefore determined up to homotopy by its degree column. Unimodular changes of bases of three- and four-cells reduce the attaching matrix to \(\operatorname{diag}(1,1,1,0)\), and are realized by homotopy equivalences/attaching-map slides. The three unit attaching maps cancel three pairs of adjacent cells, while the zero column supplies one four-sphere. Precisely \(212-3=209\) three-spheres remain, proving the claimed wedge decomposition.

## Verification

The supplied standalone `verify_paley23.py` uses only the Python standard library. Running `python verify_paley23.py` regenerates all faces directly from the 23 quadratic-residue translates; verifies every elementary collapse; constructs the complete matching; independently checks acyclicity by a topological sort of all Hasse arrows; computes the signed integral Morse differential; checks the four-column linear dependence and the unit determinant of the specified three-row minor. All the cited counts and matrix facts are asserted in executable code. The computation is exhaustive on this finite 23-vertex object and does not extrapolate from smaller instances.

## Relationship to prior work

Dochtermann and Singh introduced the out-neighborhood complex of a digraph and connected it to directed Hom complexes; their 2021 preprint studies general structural results, five-vertex tournaments, and explicit single-sphere examples. Their stated problem of realizing further tournament-neighborhood homotopy types motivates the present canonical mixed-dimensional example. Govc, Levi, and Smith study directed flag complexes and tournaplex filtrations, which are different constructions. Calculations of the directed *flag* complex for Paley tournaments of other orders do not imply this out-neighborhood calculation. The cyclic quadratic-residue translates are also the blocks of a classical symmetric design; its incidence parameters do not determine the above homotopy decomposition. Searches of the main paper, indexed mathematical results, and published literature found no statement implying the exact result for this complex.

## Limitations

The theorem concerns one natural finite tournament, not all Paley tournaments. The proof is an exhaustive, reproducible combinatorial certificate, not a symbolic formula uniformly in the field order. It does not determine the equivariant homology representation or the behavior of other design block complexes. A mathematically equivalent unindexed classification remains possible; no independent expert audit has been performed.

## References

1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, first posted 2021-08-24; especially Definition 4.1, Theorem 4.3, Proposition 4.11, Section 5, and the final open questions. https://arxiv.org/abs/2108.10948
2. D. Govc, R. Levi, and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, Journal of Applied and Computational Topology 5 (2021), 313–337, DOI:10.1007/s41468-021-00068-0. https://doi.org/10.1007/s41468-021-00068-0
