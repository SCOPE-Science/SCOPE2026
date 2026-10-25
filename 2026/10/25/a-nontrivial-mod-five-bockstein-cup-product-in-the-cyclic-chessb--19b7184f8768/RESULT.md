# A nontrivial mod-five Bockstein cup product in the cyclic chessboard quotient

## Finding
Let \(\Delta_{4,5}\) denote the ordinary chessboard complex: a \(k-1\)-simplex is a placement of \(k\) nonattacking rooks in four indexed rows and five indexed columns. The cyclic group \(C_5\) acts by incrementing all column coordinates modulo five. For its quotient \(Y=|\Delta_{4,5}|/C_5\),
\[
(H_0,H_1,H_2,H_3)(Y;\mathbb Z)
\cong(\mathbb Z,\mathbb Z/5,\mathbb Z^4,\mathbb Z),
\]
and higher homology vanishes. The four-dimensional vector of cellular ranks is \((4,24,48,24)\) in dimensions zero to three.

Let \(u\in H^1(Y;\mathbb F_5)\) evaluate on an oriented edge of rows \(i<j\), occupied in columns \(a,b\), as \(b-a\pmod5\). The integral Bockstein \(\beta_{\mathbb Z}u\in H^2(Y;\mathbb Z)\) has exact order five. For the primitive fundamental three-cycle \(z\) specified below,
\[
\left\langle u\smile\overline{\beta_{\mathbb Z}u},z\right\rangle
=2\in\mathbb F_5.
\]
In particular, this cup product is nonzero. The space therefore cannot be homotopy equivalent to \(M(\mathbb Z/5,1)\vee\bigvee^4 S^2\vee S^3\), despite their matching integral homology groups.

## Assumptions and scope
Rows are \(0,1,2,3\), columns are \(0,1,2,3,4\), and each face is ordered by increasing row. The action \(j\mapsto j+1\pmod5\) fixes no nonempty simplex: a face fixed by a nonidentity fifth-order column shift would contain a complete five-element orbit of rooks with equal row, impossible. Thus the action is free on the realization. The quotient is a \(\Delta\)-complex (with distinct cells potentially sharing the same vertex set), **not** the abstract simplicial complex obtained by forgetting this multiplicity. All chain complexes here are of this quotient \(\Delta\)-complex.

## Proof
**Quotient chains.** A \(k\)-rook face is specified by a \(k\)-subset of rows and an injection into the columns. There are \(\binom4k(5)_k\) such faces, and every column-shift orbit has cardinality five. Hence the orbit-cell counts for \(k=1,2,3,4\) are \(4,24,48,24\). Order cells by their row coordinates. For each orbit, choose the lexicographically smallest shifted face as representative. The signed boundary of an oriented face \(f=(v_0,\ldots,v_k)\) is the sum \(\sum_{j=0}^{k}(-1)^j(f\setminus v_j)\) projected to orbit representatives. Since column shifts preserve the row order, there is no additional orientation character.

Write the resulting integer matrices as \(D_1,D_2,D_3\), with shapes \(4\times24\), \(24\times48\), and \(48\times24\). Exact Smith reduction gives their complete nonzero diagonal factors:
\[
D_1:(1,1,1),\qquad
D_2:(\underbrace{1,\ldots,1}_{20},5),\qquad
D_3:(\underbrace{1,\ldots,1}_{23}).
\]
Both products \(D_1D_2\) and \(D_2D_3\) are zero. As \(\operatorname{im}D_1\) is free, the order-five torsion of \(\operatorname{coker}D_2\) is exactly the torsion of \(H_1\). The free ranks are obtained from \((3,21,23)\) for the boundary ranks. The unit Smith factors of \(D_3\) make its image primitive; thus the rank-four group \(H_2=\ker D_2/\operatorname{im}D_3\) is torsion-free. Finally \(H_3=\ker D_3\cong\mathbb Z\).

**Integral orientation cycle.** For a top face \(f=((0,c_0),(1,c_1),(2,c_2),(3,c_3))\), let \(c_*\) be its unique missing column. Give its orbit representative the coefficient \(\varepsilon(f)\), the sign of the permutation \((c_0,c_1,c_2,c_3,c_*)\) of \((0,1,2,3,4)\). A column shift is a five-cycle, hence an even permutation, so \(\varepsilon\) is orbit-independent. The chain \(z=\sum_{[f]}\varepsilon(f)[f]\) has zero boundary: the two incident top cells on any codimension-one face have opposite signs. Since every coefficient is \(\pm1\) and \(\ker D_3\) has rank one, \(z\) is a primitive generator.

**Explicit Bockstein and cup.** On an edge with increasing rows, choose the integer lift \(U(v_i,v_j)\in\{0,1,2,3,4\}\) of the difference of its column coordinates. For every ordered triangle \((v_0,v_1,v_2)\), the integer
\[
B(v_0,v_1,v_2)=\frac{U(v_1,v_2)-U(v_0,v_2)+U(v_0,v_1)}5
\]
is well-defined because the numerator is divisible by five. It is an integer two-cocycle representing \(\beta_{\mathbb Z}u\). The Alexander–Whitney cup representative of \(u\smile\overline{\beta_{\mathbb Z}u}\) on a tetrahedron is \(U(v_0,v_1)B(v_1,v_2,v_3)\pmod5\). Summing over the 24 orbit representatives gives the exact integer
\[
\sum_{[f]}\varepsilon(f)\,U(v_0,v_1)B(v_1,v_2,v_3)=2,
\]
so the evaluation modulo five is nonzero. The nonzero class \(u\) cannot lift to integral degree-one cohomology because \(H^1(Y;\mathbb Z)=0\); hence its integral Bockstein is an order-five generator of the torsion summand of \(H^2(Y;\mathbb Z)\). On the indicated wedge comparison space, every degree-three cup of this form vanishes (the Moore summand is two-dimensional and cross-summand products vanish), giving the asserted obstruction.

## Verification
The complete reproducible script `verify.py` generates every cell orbit, all three signed integer boundary matrices, their exact Smith diagonals, the top orientation cycle, and the Bockstein cup. Run it with Python 3 and SymPy via `python verify.py`; it terminates with `PASS` if and only if all asserted finite checks hold. The quotient chain differential and the integer cup representative are specified above independently of any external data file.

## Relationship to prior work
The identification of the punctured four-by-five chessboard complex with a 20-cusped principal-congruence hyperbolic manifold is **previously known**, as documented by Goerner (2011, Sections 1.2.2 and 1.13), and its link-complement context appears in Baker–Goerner–Reid (2018). The topology and connectivity of ordinary chessboard complexes, including the torus vertex links, are also established in earlier and subsequent work, including the exposition by Jojić et al. (2020). The 2019 technical report focuses on principal-congruence links and peripheral homology of different manifolds. None of the inspected sections supplies this particular orbit-cell Smith complex or the nonzero Bockstein cup product on its four-vertex cyclic quotient. In particular, the homology of a higher-symmetry quotient or of the unquotiented link complement does not itself imply the stated cohomology multiplication.

## Limitations
This is a statement about the **singular-vertex compactification** \(Y\), not a claim that the four vertices have manifold neighborhoods. Each link is the usual three-by-four chessboard torus; deleting the four quotient vertices gives a cusped three-manifold. No complete cohomology ring beyond the specified product, and no uniqueness among finite-index manifold covers, is claimed. Exact computational certificates establish this finite object's invariants but do not demonstrate absence of equivalent results in unindexed literature.

## References
1. M. D. Baker, M. Goerner and A. W. Reid, *All principal congruence link groups*, arXiv:1802.01275 (first public version 2018-02-05); primary classification 57M25. https://arxiv.org/abs/1802.01275
2. M. D. Baker, M. Goerner and A. W. Reid, *Technical Report: All Principal Congruence Link Groups*, arXiv:1902.04722 (2019), especially Section 7. https://arxiv.org/abs/1902.04722
3. M. Goerner, *Regular Tessellation Link Complements*, doctoral thesis (2011), Sections 1.2.2 and 1.13. https://www.unhyperbolic.org/research/matthias_goerner_thesis_print.pdf
4. D. Jojić et al., *Generalized chessboard complexes and discrete Morse theory*, arXiv:2003.04018 (2020), Section 2.1. https://arxiv.org/abs/2003.04018
