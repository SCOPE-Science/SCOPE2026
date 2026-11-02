# Two sign lines in honeycomb perfect-matching homology

## Finding
Let \(H\) be the honeycomb graph dual to the unit triangular cells of a regular hexagon of side length two in the triangular lattice. Let \(X=\mathcal M_p(H)\) be the simplicial complex on graph edges whose facets are the perfect matchings. Its planar symmetry group \(D_6=\langle r,s\mid r^6=s^2=1,\;srs=r^{-1}\rangle\) acts simplicially; \(r\) is rotation by \(60^\circ\), and \(s\) is the reflection that interchanges the two lattice basis directions.

Define one-dimensional rational characters by
\[
\alpha(r)=1,\quad\alpha(s)=-1,\qquad
\beta(r)=-1,\quad\beta(s)=1.
\]
Then, as rational \(D_6\)-modules,
\[
\boxed{\widetilde H_3(X;\mathbb Q)\cong\alpha\oplus\beta,\qquad
\widetilde H_j(X;\mathbb Q)=0\quad(j\ne3).}
\]
In fact \(X\simeq S^3\vee S^3\) integrally. Thus the rotation characters at \(r^k\), for \(k=0,\ldots,5\), are \((2,0,2,0,2,0)\), while the reflection characters at \(sr^k\) are \((0,-2,0,-2,0,-2)\).

For each subgroup \(K\le D_6\), \(\widetilde H_3(X/K;\mathbb Q)\) is the invariant part \((\alpha\oplus\beta)^K\) and all other reduced rational homology vanishes. In particular, its dimensions are \(0\) for \(D_6\), \(1\) for \(\langle r\rangle\), \(2\) for \(\langle r^2\rangle\), \(1\) for \(\langle s\rangle\), and \(0\) for \(\langle sr\rangle\). The full dihedral quotient is rationally acyclic, but the rotation quotient retains one three-dimensional rational homology class.

## Assumptions and scope
Work with the standard triangular-lattice basis \(u=(1,0)\), \(v=(1/2,\sqrt3/2)\). In integer axial coordinates set
\[
P=\{(i,j)\in\mathbb Z^2:\ |i|\le2,\ |j|\le2,\ |i+j|\le2\}.
\]
The triangular cells are the three-element subsets of \(P\) of the forms \(\{(i,j),(i+1,j),(i,j+1)\}\) and \(\{(i+1,j+1),(i+1,j),(i,j+1)\}\). The vertices of \(H\) are these cells, with two vertices adjacent exactly if their cells share two lattice points. This fixes an unambiguous 24-vertex, 30-edge graph, the standard \(2\times2\times2\) honeycomb dual. A face of \(X\) is an edge set contained in at least one perfect matching of \(H\); empty face included only when using reduced chains. The group acts by coordinate transformations \(r(i,j)=(-j,i+j)\) and \(s(i,j)=(j,i)\). We use the induced permutation on graph edges and its oriented-simplicial action, not an unsigned permutation of simplex generators.

## Proof
**Finite topological certificate.** Enumerate perfect matchings recursively: for the least uncovered graph vertex, choose in turn each incident edge to another uncovered vertex and remove both endpoints. There are exactly \(20\) distinct perfect matchings, each of size \(12\). Enumerating all of their subsets gives exactly \(66,369\) nonempty faces, with face counts by cardinality \(1,\ldots,12\):
\[
(30,357,1966,6069,11892,15807,14688,9612,4368,1320,240,20).
\]
On the nonempty face poset, process all \(30\) graph edges in lexicographic edge-index order. For each edge \(e\), match every currently unmatched face \(F\) not containing \(e\) with \(F\cup\{e\}\), if both faces are still unmatched. This yields \(33,183\) pairs and precisely three critical faces, of dimensions \(0,3,3\). Orient matched Hasse covers from the smaller face to the larger one, and all other covers downward. Complete topological sorting of the resulting directed graph visits all \(66,369\) faces and its \(420,294\) directed covers: the matching is acyclic. Forman's discrete Morse theorem therefore gives a CW model with one \(0\)-cell and two \(3\)-cells, without any \(1\)- or \(2\)-cells; their attaching maps are constant. Hence \(X\simeq S^3\vee S^3\). The accompanying independent executable certificate reconstructs the complete poset and verifies all counts and acyclicity; these are exhaustive finite statements, not samples.

**Equivariant calculation.** Fix any symmetry \(g\in D_6\), let \(p_g\) be its permutation of the \(30\) graph edges, and let \(F=\{e_1<\cdots<e_q\}\) range over the nonempty faces. The signed simplicial chain trace contributed by \(F\) is zero unless \(p_g(F)=F\); otherwise it is the sign of the permutation \((p_g(e_1),\ldots,p_g(e_q))\), multiplied by \((-1)^{q-1}\) in the alternating sum. The reduced Lefschetz number is therefore exactly
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne F\in X\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(p_g|_F).
\]
(The \(-1\) subtracts the empty face.) Exhaustive signed face enumeration gives the following values, with each row indexed by \(k=0,\ldots,5\):

| Symmetry | Number of setwise fixed nonempty faces | Reduced Lefschetz value | Homology trace |
| --- | --- | --- | --- |
| \(r^k\) | \((66369,3,57,231,57,3)\) | \((-2,0,-2,0,-2,0)\) | \((2,0,2,0,2,0)\) |
| \(sr^k\) | \((239,961,239,961,239,961)\) | \((0,2,0,2,0,2)\) | \((0,-2,0,-2,0,-2)\) |

The executable certificate independently computes each reduced Lefschetz number in two ways: (i) iterating every face and testing setwise invariance with its exact orientation sign, and (ii) enumerating unions of edge cycles inside each perfect matching. Both produce the listed values for all twelve symmetries. Since the only reduced rational homology group is in dimension three, \(\operatorname{tr}(g|\widetilde H_3)=-\widetilde L(g)\).

The characters of \(\alpha\) and \(\beta\) add to these twelve traces. Characters determine rational representations of finite groups in characteristic zero, so \(\widetilde H_3(X;\mathbb Q)\cong\alpha\oplus\beta\). For any finite subgroup, transfer/averaging over \(\mathbb Q\) identifies quotient homology with homology invariants, proving every quotient statement.

## Verification
Run `python3 certificate.py` using Python 3.10 or newer. The sole output signature is `HONEYCOMB_222_DIHEDRAL_EXACT_OK`, followed by full cardinality, matching-acyclicity, symmetry-character, and subgroup-invariant summaries. The script uses only the standard library. It constructs the triangular graph and all perfect matchings from scratch; it does not import a precomputed face list, a saved permutation, or an existing homology package. Its acyclicity check visits the complete finite directed Hasse graph, and it cross-checks signed Lefschetz numbers by independent facewise and orbitwise methods. The rational-module and quotient deductions from these finite certificates are proved above.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega proved the nonequivariant homotopy type \(\mathcal M_p(H_{2\times2\times2})\simeq S^3\vee S^3\) (Theorem 17, 2022 preprint; published 2023). That topological classification is prior art and is **not** a new claim here. The new claim is the entire natural \(D_6\)-representation on its third rational homology, including the inequivalent characters of the two sphere generators and the resulting subgroup-quotient rational homology. The cited paper's Section 4 and Appendix A supply a homotopy computation and complete matching descriptions but do not supply this representation or signed symmetry traces.

Chandrakar and Singh study perfect-matching complexes of polygonal **line** tilings and two-row Cartesian grids, rather than this two-dimensional hexagonal patch. More generally, counting reflection-symmetric or rotationally symmetric lozenge tilings counts fixed *facets*, not signed setwise-fixed faces of all dimensions, so such counts alone do not imply this equivariant homology theorem. The result applies to this specific regular side-two hexagon; no family-wide conclusion is asserted.

## Limitations
The theorem concerns ordinary rational homology representations, not Bredon equivariant homology, integral representation-lattice splittings, or the equivariant homotopy type of \(X\). Rational acyclicity of the full quotient does not assert contractibility or integral acyclicity. The finite certificate is exhaustive for exactly this graph, not for hexagonal regions of other side lengths. Literature checks cannot rule out equivalent unindexed results; independent external audit has not been performed.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first public September 6, 2022), Section 4, Theorem 17, Appendix A; *Electronic Journal of Combinatorics* **30** (2023), P2.45. https://arxiv.org/abs/2209.02803
2. H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1 (July 8, 2024). https://arxiv.org/abs/2407.05809
3. R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* **134** (1998), 90–145. Standard discrete Morse matching theorem.
