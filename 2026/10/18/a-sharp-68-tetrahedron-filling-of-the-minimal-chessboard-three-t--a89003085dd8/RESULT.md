# A sharp 68-tetrahedron filling of the minimal chessboard three-torsion sphere

## Finding
Let \(K=\mathcal M(K_{5,5})\) be the chessboard complex whose vertices \(e_{r,c}\), indexed by \(0\le r,c\le4\), are squares of a five-by-five board and whose faces are placements of mutually nonattacking rooks. Define the oriented simplicial two-cycle
\[
z=(e_{0,0}-e_{0,1})\star(e_{1,2}-e_{1,3})\star(e_{2,4}-e_{3,4}),
\]
where \(\star\) denotes the signed join of reduced zero-chains. The fundamental cycle has eight triangular faces, each with coefficient \(\pm1\), and represents an element of exact order three in integral second homology. Its optimal real-coefficient simplicial filling satisfies
\[
\boxed{\min\{\|w\|_1:w\in C_3(K;\mathbb R),\ \partial_3w=3z\}=68.}
\]
An integral filling supported on 68 distinct tetrahedra attains the minimum, so the minimum over integral three-chains also equals 68. This equality holds for every oriented fundamental cycle, up to sign, of every induced octahedral two-sphere on six vertices in \(K\); the 1800 such spheres form one orbit under row and column permutations and transposition.

## Assumptions and scope
Use the unaugmented simplicial chain groups over the indicated coefficient ring. Orient every face by increasing vertex index \(5r+c\), order all oriented faces lexicographically, and use \(\partial[v_0,\ldots,v_d]=\sum_{i=0}^d(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_d]\). The norm \(\|w\|_1\) is the sum of the absolute values of its coefficients in the oriented tetrahedron basis. Each factor \(e_a-e_b\) is a reduced zero-cycle; their join is oriented with its three vertices in factor order and reoriented with the corresponding permutation sign. The minimum is over **all** real three-chains, without positivity, support, or integrality restrictions. There are 25 vertices, 200 edges, 600 triangles, 600 tetrahedra, and 120 four-simplices.

## Proof
**Order-three claim.** The octahedral join has eight signed triangular terms, and its simplicial boundary vanishes by the Leibniz rule or direct expansion. The certificate `CERTIFICATE.json` gives a three-chain \(w\) with exactly 68 signed coefficients in \(\{+1,-1\}\); the standalone program `VERIFY.py` reconstructs all 600 oriented tetrahedron boundaries and verifies the exact integer identity \(\partial_3w=3z\). To exclude \(z\) being a boundary, it row-reduces the integer boundary matrix modulo three and obtains rank 423. Reduction of \(z\) against the resulting column basis has a nonzero remainder; hence \(z\notin\operatorname{im}(\partial_3\otimes\mathbb F_3)\), and in particular \(z\) is not an integral boundary. Therefore \([z]\) has order exactly three.

**Upper bound.** Each of the 68 tetrahedral coefficients of \(w\) has magnitude one. Thus \(\partial_3w=3z\) and \(\|w\|_1=68\), proving the real and integral minima are at most 68.

**Lower bound.** The certificate also gives a rational two-cochain \(y\) as a sparse list of integer numerators divided by three. Exact arithmetic verifies that its coboundary, evaluated on every one of the 600 oriented tetrahedra, has absolute value at most one, with equality attained, and that \(\langle y,3z\rangle=68\). Therefore for every **real** three-chain \(v\) satisfying \(\partial_3v=3z\),
\[
68=\langle y,\partial_3v\rangle=\langle\delta y,v\rangle\le\|\delta y\|_\infty\,\|v\|_1\le\|v\|_1.
\]
The upper and lower bounds coincide. This dual argument applies to arbitrary signed real coefficients, so a hidden fractional improvement is impossible. The exact checker verifies the critical inequalities from rational integers, not from floating-point optimization output.

**All six-vertex octahedral spheres.** Two incompatible rooks occupy the same row or column. A six-element induced rook complex is the octahedral boundary exactly when its conflict graph is a perfect matching. Among these, there are 900 with two row-conflict pairs and one column-conflict pair; 900 have the dual pattern. For the first pattern choose the column used by its column-conflict pair (five choices), the two row-conflict rows (\(\binom52\) choices), the column-conflict pair’s two rows from the three remaining rows (\(\binom32\) choices), and the two nonconflict columns in the first row-conflict row from the remaining four columns (\(\binom42\) choices); the second row-conflict row must use the other two columns. The product is \(5\binom52\binom32\binom42=900\). Exhaustive independent enumeration confirms the 900+900 count. The row-permutation group, column-permutation group, and row-column interchange act transitively on these pair-patterns. Each symmetry induces a signed permutation of oriented simplex bases, commuting with boundary and preserving their \(\ell_1\) norms. It maps \(z\) to one of the two possible orientations of the octahedral fundamental class, so each such cycle has the same sharp value 68.

## Verification
With Python 3 standard library, place `VERIFY.py` and `CERTIFICATE.json` together and run `python3 VERIFY.py`. The program checks orientation and boundary-composition identities, reconstructs the eight-term cycle, verifies the 68-term integer primal filling, verifies each dual inequality using exact integers and the exact pairing 68, confirms nonboundary status modulo three, and exhaustively enumerates the induced octahedral spheres. The face vector is \((25,200,600,600,120)\); the exact modular boundary rank is 423. It prints `THREE_TIMES_CYCLE_PRIMAL_AREA_68 DUAL_LOWER_BOUND_68 EXACT` upon success. Both certificates are included, not merely output logs.

## Relationship to prior work
Shareshian and Wachs, *Torsion in the Matching Complex and Chessboard Complex* (initial arXiv submission 3 September 2004), Section 5.1, Theorem 5.4, establish the order-three homology generator using three factors of reduced zero-cycles of the indicated row/column form. The generator and its order are **not claimed as new**. Jonsson, *On the 3-Torsion Part of the Homology of the Chessboard Complex*, Theorem 3.1, establishes the same \(\mathbb Z/3\) homology group without computer assistance. Neither inspected theorem specifies the minimum \(\ell_1\) norm of a simplicial three-chain filling three times that cycle. The quantitative sharp equality 68 is the contribution here. A different computation concerning a torsion one-cycle in the matching complex of a complete seven-vertex graph does not imply the three-dimensional filling norm in this chessboard complex.

## Limitations
The theorem concerns the specified finite chessboard complex, the canonical octahedral generator and its images under symmetries, and the simplicial \(\ell_1\) norm relative to the displayed triangulation. It does not classify all optimal filling chains, establish larger-board asymptotic inequalities, or assert publication priority over inaccessible or unindexed equivalent calculations. Integral torsion and the sharp norm are independently checked by finite exact certificates; no extrapolation to infinite complexes is made. The primary-literature comparison is limited to the indicated inspected results and targeted text passages.

## References
- J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (3 September 2004), Section 5.1, Theorem 5.4. https://arxiv.org/abs/math/0409054
- J. Jonsson, *On the 3-Torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644v1 (26 March 2012), Theorem 3.1. https://arxiv.org/abs/1203.5644
