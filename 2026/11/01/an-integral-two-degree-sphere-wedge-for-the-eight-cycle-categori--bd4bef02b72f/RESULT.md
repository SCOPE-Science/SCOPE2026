# An integral two-degree sphere wedge for the eight-cycle categorical product with four colors

## Finding
Let \(C_8\) be the simple eight-cycle and \(K_4\) the complete graph on four vertices. For their **categorical** graph product \(G=C_8\times K_4\), the ordinary independence complex satisfies
\[
\boxed{|\operatorname{Ind}(G)|\simeq\bigvee^{3}S^4\ \vee\ \bigvee^{6}S^5.}
\]
Consequently, its reduced integral homology is \(\widetilde H_4\cong\mathbb Z^3\), \(\widetilde H_5\cong\mathbb Z^6\), and zero in every other degree. In particular no integral homology torsion or Moore summand occurs.

## Assumptions and scope
The vertex set is \((\mathbb Z/8\mathbb Z)\times\{0,1,2,3\}\), with an edge from \((i,a)\) to \((j,b)\) if and only if \(j=i\pm1\pmod8\) and \(a\ne b\). The independence complex contains every vertex subset without such an edge. It is **not** the Cartesian-product graph or a graph-Hom complex. Only this specific finite graph is classified. Integer orientations are induced by increasing vertex labels \(4i+a\); all homology uses integer coefficients unless otherwise indicated.

## Proof
**1. Complete finite complex.** A face is represented by a 32-bit integer. Starting with the empty face, process vertices in label order; for each new vertex adjoin it to every previously constructed face containing none of its neighbors. This is an induction on the vertex set, hence enumerates every independent set exactly once. It produces \(196227\) faces including the empty face and, in dimensions zero through fifteen, the face vector
\[
(32,400,2560,9400,21440,33040,37728,34488,26336,16896,8864,3648,1120,240,32,2).
\]
An independent transfer enumeration uses column subsets \(A_i\subseteq\{0,1,2,3\}\). Adjacent columns may both be nonempty precisely when each is the same singleton; otherwise at least one is empty. Exact cyclic transfer counting by selected size independently reproduces all seventeen cardinality counts, including the empty face.

**2. Certified acyclic matching.** Exclude the empty face. For each vertex label \(v=0,1,\ldots,31\) successively, pair every currently unpaired nonempty face \(\sigma\) avoiding \(v\) to \(\sigma\cup\{v\}\), provided the latter is a face and remains unpaired. Each pair is used once. Exactly \(98087\) pairs are constructed, leaving one critical zero-cell, \(24\) critical four-cells and \(27\) critical five-cells. To prove global acyclicity rather than merely observe the counts, orient **every** cover relation of the full nonempty-face Hasse graph upward if it belongs to the matching and downward otherwise. A complete topological sort processes all \(196226\) vertices of this graph and its \(1457216\) cover relations. Hence there is no closed gradient path. Forman's discrete-Morse theorem gives a CW model with precisely those critical cells.

**3. Integral Morse differential.** Let \(c_1,\ldots,c_{24}\) and \(d_1,\ldots,d_{27}\) enumerate the critical four- and five-cells by increasing bitmask. Orient a face \(\sigma=\{v_0<\cdots<v_k\}\) in this vertex order; deleting \(v_j\) has incidence \((-1)^j\). To compute the projection \(p\) of an oriented four-face into the critical four-cells, set \(p(c_i)=c_i\), set \(p(\sigma)=0\) when \(\sigma\) is the upper member of a matched three/four pair, and for a matched four/five pair \(\sigma\subset\tau\) use the exact reduction
\[
p(\sigma)=-[\tau:\sigma]^{-1}\sum_{\substack{\eta\subset\tau\\\dim\eta=4,\ \eta\ne\sigma}}[\tau:\eta]\,p(\eta).
\]
Acyclicity makes the recursion finite. Applying \(p\) to the oriented boundaries of the \(27\) critical five-cells yields the complete integer matrix \(D\in M_{24\times27}(\mathbb Z)\). Exact Smith normal form of \(D\) has \(21\) nonzero diagonal entries, every one equal to \(1\); the other entries are zero. Independently, exact rational elimination shows rank \(21\) and a selected \(21\times21\) minor has determinant \(-1\). Thus \(\ker D\cong\mathbb Z^6\) and \(\operatorname{coker}D\cong\mathbb Z^3\), with no torsion.

**4. From chains to homotopy.** The CW model has one zero-cell, no cells in dimensions one through three, \(24\) four-cells and \(27\) five-cells. Its four-skeleton is a wedge of \(24\) four-spheres. Its fourth homotopy group is canonically identified with its fourth homology by Hurewicz. Hence the homotopy classes of five-cell attaching maps are completely determined by their integer degree vectors, the columns of \(D\). Integral row/column changes and the unit Smith pivots correspond to changing sphere generators and canceling \(21\) four/five cell pairs up to homotopy. The remaining model is the wedge of \(3\) four-spheres and \(6\) five-spheres in the finding. The independently enumerated reduced Euler characteristic equals \(-3=3-6\).

## Verification
Run `python verify.py` with Python 3.10+ and SymPy available (`requirements.txt` specifies the dependency). The script reconstructs the graph, all independent faces, the separate cyclic-column transfer enumeration, every match, the entire directed cover graph, the signed integral Morse matrix, its Smith factors and a unimodular maximal minor. It asserts the exact numbers above, including the complete directed-graph topological sort. Output ends in `ALL_VERIFY_OK` on success. The finite computation is exhaustive for the stated graph; the argument does not extrapolate to larger graph products.

## Relationship to prior work
Carnero Bravo's 2025 paper *On independence complexes of graph products* develops homotopy calculations for path-factor categorical products, together with other graph products. Closing a path factor into an eight-cycle changes the adjacency constraints, and the paper's path-product formulas do not calculate the present complex. Antolín Camarena and Carnero Bravo's 2023/2024 *Homotopy type of the independence complex of some categorical products of graphs* is the most direct older comparison: its Theorem 3.18 (Theorem 23 in the accessible arXiv rendition) leaves, for cycle lengths congruent to two modulo three, possible sphere and Moore summands rather than computing this specific case. Its explicit sample list includes the eight-cycle with three colors, not the eight-cycle with four. The present result is a complete integral resolution at the first unlisted four-color example in that residue class. No claim of a general torsion-free theorem is made.

## Limitations
This proves one finite homotopy type, not an all-length or all-color formula. No general nonexistence of Moore spaces in other categorical products follows. An unindexed equivalent computation remains possible; independent mathematical validation has not been performed. The computational proof requires executing the complete included verifier or independently checking its stated discrete-Morse certificate.

## References
- A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, first posted 2025-05-09, https://arxiv.org/abs/2505.06457 .
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first posted 2023-07-23; *Homology, Homotopy and Applications* 26(2) (2024), 349–373, https://arxiv.org/abs/2307.12401 .
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Standard discrete-Morse theorem and integral Morse boundary.
