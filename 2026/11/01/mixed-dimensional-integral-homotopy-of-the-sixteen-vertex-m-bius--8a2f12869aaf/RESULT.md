# Mixed-dimensional integral homotopy of the sixteen-vertex Möbius-ladder matching complex

## Finding
Let \(G\) have vertex set \(\mathbb Z/16\mathbb Z\), cycle edges \(\{i,i+1\}\) for each residue \(i\), and eight antipodal edges \(\{i,i+8\}\), for \(0\le i<8\). Let \(\mathcal M(G)\) denote the **ordinary matching complex**: its vertices are the 24 graph edges, and a simplex is any collection of pairwise vertex-disjoint graph edges, whether or not it extends to a perfect matching. Then
\[
|\mathcal M(G)|\simeq \bigvee^{2}S^{4}\ \vee\ \bigvee^{4}S^{5}.
\]
Thus its only nonzero reduced integral homology groups are \(\widetilde H_4\cong\mathbb Z^2\) and \(\widetilde H_5\cong\mathbb Z^4\). This is a homotopy classification, not an inference from modular homology.

## Assumptions and scope
All graphs are finite and simple. The cycle and antipodal edges in the first paragraph uniquely specify \(G\), sometimes called the eight-rung Möbius ladder or circulant \(\operatorname{Ci}_{16}(1,8)\). Every matching, including one not contained in a perfect matching, is allowed. Spheres are unbased unless used in the standard one-point wedge, and all claimed homotopy equivalences are nonequivariant. No statement is made for other ladder lengths or for the perfect-matching subcomplex.

## Proof
Order the 24 graph edges lexicographically by their sorted endpoint pairs, with indices \(0,\ldots,23\). Encode a simplex by its edge-indicator integer \(f\), whose \(j\)th bit is one precisely when the \(j\)th graph edge is present. Two graph edges conflict when they share an endpoint. Starting with the empty face, insert edges in ascending index order only when no conflict occurs. This constructs all simplices; the result has **11,393 nonempty simplices** and face vector by dimensions \(0\) through \(7\):
\[
(24,228,1096,2834,3880,2588,696,47).
\]

Use the following index order for a sequence of elementary *face-poset toggle matchings*:

`[11,5,22,13,20,7,17,12,3,4,1,0,18,19,8,6,2,10,16,21,14,23,9,15]`.

For each index \(j\) and each currently unmatched nonempty simplex \(f\) in increasing integer order, if \(j\notin f\) and both \(f\) and \(f\cup\{j\}\) are still unmatched, match this pair and remove both from consideration. This pairs exactly **5,690** simplex pairs and leaves 13 critical simplices: one vertex, five four-simplices and seven five-simplices. The critical face integer masks in increasing order are

`[2048,49985,69968,594064,2105680,2114324,2146625,2367620,2376204,2425601,8422209,8921232,8950792]`.

For acyclicity, orient the full nonempty-face Hasse diagram downward except reverse each of the matched incidences. Its 55,256 codimension-one incidences admit a complete topological sort (all 11,393 vertices are removed); therefore the matching is acyclic and Forman's discrete-Morse theorem gives a homotopy-equivalent CW complex with the asserted critical-cell counts.

Use increasing edge-index orientation on all simplices. The simplicial incidence of a codimension-one face obtained by removing the \(r\)th selected edge (zero-indexed) is \((-1)^r\). To calculate the Morse differential, eliminate matched pairs by signed gradient-path reduction. For a four-simplex \(f\) paired upward to a five-simplex \(u\), the coefficient of \(f\) in \(\partial u\) is a unit \(c=\pm1\), and its reduction is \(-c\) times the reductions of all the other boundary faces of \(u\), with their simplicial signs. A four-simplex paired downward to a three-simplex has zero projection; a critical four-simplex projects to itself. The directed-acyclicity check ensures the recursion terminates. In increasing integer order of critical face masks within each dimension, the resulting integer boundary \(C_5\to C_4\) is the **exact** matrix
\[
B=\begin{pmatrix}
0&0&0&0&0&0&0\\
-1&-1&-1&0&0&0&0\\
1&-1&1&0&0&0&0\\
0&0&0&-1&0&1&0\\
-1&0&-1&-1&0&1&0
\end{pmatrix}.
\]

Every four-by-four minor of \(B\) is zero. The three-by-three minor on zero-indexed rows \((1,3,4)\) and columns \((0,1,3)\) has determinant \(-1\). Thus \(B\) has rank three and three unit Smith invariant factors. The Morse CW complex has only one zero-cell, five four-cells, and seven five-cells. Its four-skeleton is a wedge of five four-spheres. By the Hurewicz theorem, the homotopy classes of the five-cell attaching maps \(S^4\to\bigvee^5 S^4\) are determined by their integer degree columns. Unimodular changes of the four-sphere basis and five-cell generators transform \(B\) into a rank-three diagonal identity block and zero remainder. The three unit attachments cancel three four/five-cell pairs (cellular cancellation or elementary homotopy cofiber reduction), leaving two freely wedged four-spheres and four five-cells attached trivially. This proves the displayed homotopy type over \(\mathbb Z\).

## Verification
The accompanying stand-alone `verify.py` (Python 3 standard library only) reconstructs the 24 edges and 11,393 simplices; checks every simplex directly for disjoint edge endpoints; verifies the full face vector, every one of the 5,690 matching pairs and all thirteen critical masks; enumerates 55,256 face incidences and globally verifies acyclicity; computes the full signed five-by-seven Morse differential by recursive integral gradient reduction; checks every four-by-four minor vanishes and an explicit three-by-three minor is a unit; and independently reduces the original simplicial boundary matrices over \(\mathbb F_2\) to confirm the two homology ranks. Run `python3 verify.py` from any directory; no external input is needed.

## Relationship to prior work
Agarwal and Basak, arXiv:2608.30601, first publicly posted 31 August 2026, classify the **graph independence complex** and **perfect-matching subcomplex** for the entire Möbius-ladder family. Their Main Theorem 1 gives \(\mathcal M_p(M_{16})\simeq S^3\vee S^3\), where every face must extend to a perfect matching. The ordinary matching complex here is the independence complex of the *line graph* of \(M_{16}\), not the independence complex of \(M_{16}\) itself, and includes all nonextendible matchings. Neither theorem in that paper yields the mixed four/five-dimensional homotopy type above. Moreover, **Problem 26** in that paper explicitly names the ordinary matching complex of Möbius-ladder graphs as a future homotopy-type problem. This theorem resolves a natural sixteen-vertex instance of that open direction, without purporting to solve its uniform-family form. Matching-polynomial recurrences likewise determine simplex counts but not integral attaching maps or the homotopy type. A contextual search of related ordinary and perfect matching-complex results found no statement implying this one; see the originality comparisons in `AUDIT.json` for scope and residual uncertainty.

## Limitations
This is a complete finite theorem for one specified graph, without a claim of a uniform recurrence, an equivariant homology representation, or a classification for all Möbius ladders. The computational certificate is exhaustive, but its correctness has not been independently audited by a separate researcher; numerical homology alone would not support the homotopy conclusion. Equivalent work outside the searched accessible literature remains possible.

## References
- Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first version 31 August 2026, revised 14 September 2026. https://arxiv.org/abs/2608.30601
- Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145; the acyclic-matching/CW reduction used here.
- Allen Hatcher, *Algebraic Topology*, Cambridge University Press (2002), Sections 0 and 4; homotopy cofibers, cellular attachments and the Hurewicz theorem.
