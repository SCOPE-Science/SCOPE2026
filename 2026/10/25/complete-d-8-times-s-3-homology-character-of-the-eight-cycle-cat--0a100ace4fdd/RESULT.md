# Complete \(D_8\times S_3\) homology character of the eight-cycle categorical product

## Finding

Let \(X=\operatorname{Ind}(C_8\times K_3)\) with the **categorical** graph product. Under the natural coordinate action of \(D_8\times S_3\), its only nonzero reduced rational homology modules are
\[
\widetilde H_4(X;\mathbb Q)\cong\alpha\boxtimes\varepsilon,\qquad
\widetilde H_5(X;\mathbb Q)\cong\beta\boxtimes(\varepsilon\otimes P).
\]
Here \(\varepsilon\) is the sign representation of \(S_3\), \(P\) is its three-color permutation representation, and the one-dimensional characters of \(D_8\) satisfy \(\alpha(r)=\alpha(s)=-1\), \(\beta(r)=-1\), \(\beta(s)=1\).

For \(g=(r^a s^b,\sigma)\), \(0\le a<8\), \(b\in\{0,1\}\), the complete degree-separated homology characters are
\[
\chi_4(g)=(-1)^{a+b}\operatorname{sgn}(\sigma),\qquad
\chi_5(g)=(-1)^a\operatorname{sgn}(\sigma)|\operatorname{Fix}(\sigma)|.
\]
In particular, \(X\simeq S^4\vee\bigvee^3S^5\), and the full symmetry group fixes no nonzero positive-degree reduced rational homology class.

## Assumptions and scope

The undirected graph has vertex set \(V=\mathbb Z/8\mathbb Z\times\{0,1,2\}\). Distinct vertices \((i,c)\) and \((j,d)\) are adjacent exactly when \(i-j\equiv\pm1\pmod8\) and \(c\ne d\). The independence complex contains all subsets without such an edge. The dihedral generators act by \(r(i,c)=(i+1,c)\), \(s(i,c)=(-i,c)\); \(\sigma\in S_3\) acts by \((i,c)\mapsto(i,\sigma(c))\). These operations commute. The displayed representations are over \(\mathbb Q\); the nonequivariant homotopy statement is integral.

## Proof

The following is a finite exact certificate whose public standalone verifier reconstructs every object without external data. Encode vertex \((i,c)\) by the bit \(3i+c\), and an independent set by its 24-bit mask. There are precisely 18,722 faces including the empty face. Their face-dimension counts, starting with the empty face in degree \(-1\), are
\[
(1,24,228,1112,3042,4848,4652,2880,1305,472,132,24,2).
\]

Apply the staged simplicial matching in the verifier: at each pivot, pair each remaining face not containing that pivot with its one-vertex extension, provided both remain unmatched. The pivot list, in order, is
```
(21, 8, 7, 12, 13, 5, 18, 1, 6, 22, 2, 10, 19, 15, 14, 11, 3, 4, 0, 16, 20, 23, 9, 17)
```
This pairs 9,358 face pairs, leaving exactly two critical 4-faces and four critical 5-faces. Reverse every matched covering relation in the entire face poset. The supplied checker constructs all 104,592 directed Hasse edges and confirms acyclicity by a topological ordering that visits all 18,722 face nodes. Therefore the reduced simplicial chain complex admits the indicated integral Morse reduction, with no omitted critical dimensions.

Writing the two critical four-cells as the ordered basis and the four critical five-cells in the verifier's order, the exact integral Morse differential is
\[
\partial_5=\begin{pmatrix}-1&0&0&1\\-1&0&0&1\end{pmatrix}.
\]
The differential has a unit entry and Smith rank one. The resulting reduced integral homology is free of ranks one in degree four and three in degree five, and zero otherwise. The Morse CW structure has only 4- and 5-dimensional positive cells; because attaching maps from 4-spheres to a wedge of two 4-spheres are classified by their degrees, the primitive rank-one attaching map cancels a 4/5 cell pair up to homotopy. Hence \(X\simeq S^4\vee\bigvee^3S^5\).

To determine the actions in each degree, the checker constructs an integral algebraic-Morse projection from all simplicial chains to the six critical-cell generators. It lifts representatives of the critical cells integrally and checks the boundary of the proposed degree-four and degree-five homology cycles vanishes in the original simplicial chains. The primitive relation among the degree-four critical generators is the diagonal vector. A basis of the degree-five cycles in critical coordinates is \((e_0+e_3,e_1,e_2)\). For every one of the 96 elements \((r^a s^b,\sigma)\), act on the lifted cycles as signed oriented simplicial chains and project back. The resulting integer traces on homology are exactly the two character formulas above.

The characters identify the representations, because characteristic zero representations of finite groups are semisimple and have unique irreducible-character decompositions. Separately, an orientation-aware enumeration of every simplex fixed setwise by each group element computes the reduced simplicial Lefschetz number independently and agrees with \(\chi_4-\chi_5\) in all 96 cases. Since \(r\) acts as negative identity in both degrees, neither module admits a full-group invariant vector.

## Verification

Run `python3 c8k3_symmetry_verify.py` from the directory containing that file. It uses only the Python standard library. The verifier asserts the complete simplex count and face vector, all 9,358 matching pairs, no directed cycle in the entire reversed matching Hasse graph, the exact integral Morse differential, primitive integral cycle lifts, and every one of the 96 predicted degree-separated traces. A second signed fixed-simplex computation checks every reduced Lefschetz trace without using the Morse action matrices. Successful execution ends with `C8_K3_EQUIVARIANT_HOMOLOGY_VERIFIED 18722 9358 6 96 boundary_rank_1 H4_1 H5_3`.

The proof is a complete finite, exact integer certificate for this specific 24-vertex complex; no random sampling, floating-point approximations, or extrapolation to larger graphs is involved.

## Relationship to prior work

Antolín Camarena and Carnero Bravo, arXiv:2307.12401, establish homotopy classifications for several categorical graph products and describe the unresolved/mixed-dimensional phenomena when the cycle length is not a multiple of three. Their discussion identifies the eight-cycle three-color example as having free homology in two adjacent dimensions. The present result does **not** claim the existence of those two degrees as new; it determines the previously unspecified separate rational homology representations under the full 96-element natural symmetry group.

Goyal, Shukla and Singh, arXiv:1905.06926, give related independence-complex results and a staged matching method. That mathematical technique does not provide the symmetry-character classification of this graph. The full graph, scale, group action and degree-separated character statements are essential distinctions from ordinary Betti counts, cyclic symmetry on other graph complexes, and nonequivariant results for other categorical products.

## Limitations

The representation is asserted over \(\mathbb Q\), not as a classification of integral group lattices. It concerns precisely \(C_8\times K_3\); neither arbitrary cycle lengths nor arbitrary color counts are covered. The certificate's finite nature is complete for its stated complex but proves no general all-parameter identity. Mathematical originality is assessed against located literature and accessible mathematical-result records, not guaranteed against unindexed equivalents. An independent audit has not been performed.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first public 23 July 2023, https://arxiv.org/abs/2307.12401.
2. S. Goyal, S. Shukla and A. Singh, *Homotopy type of the independence complex of a categorical product of graphs*, arXiv:1905.06926, https://arxiv.org/abs/1905.06926.
