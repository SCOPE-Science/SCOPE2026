# The rank-five seven-point hypersimplex factor-count gap

## Finding

For every complex symmetric \(7\times7\) matrix \(C=(c_{ij})\) satisfying \(c_{ii}=0\), \(c_{ij}\ne0\) for \(i\ne j\), and \(\operatorname{rank}C=5\), define
\[
N_5(C)=\#\{I\subseteq\{1,\ldots,7\}:|I|=5,\;\det C[I]\ne0\}.
\]
The exact spectrum is
\[
\boxed{\{N_5(C)\}=\{10,12,13,14,15,16,17,18,19,20,21\}.}
\]
In particular, the count \(11\) is impossible, and all the other integers between \(10\) and \(21\) occur. Furthermore, the thirteen possible loop/parallel-class patterns of the dual rank-two matroid are all realized by such matrices; these patterns yield exactly the eleven numerical values above.

For the scaled projective toric model of the second hypersimplex \(\Delta_{7,2}=\operatorname{conv}\{e_i+e_j:i<j\}\), the entries \(c_{ij}\) are its nonzero scaling parameters. The \(21\) determinants \(\det C[I]\), \(|I|=5\), are the indexed order-five principal-minor factors appearing in the principal \(A\)-determinant; thus this is a complete factor-nonvanishing-count classification on its rank-five scaling locus.

## Assumptions and scope

The base field is \(\mathbb C\) (the argument and rational examples also work over any field of characteristic zero admitting the stated symmetric factorization). Matrix rank is exactly five; every off-diagonal scaling is nonzero. A factor is **counted** when its evaluated determinant is nonzero; no claim is made about its irreducibility as a polynomial. Reordering the seven coordinates does not alter the count. Statements are set-theoretic, and refer only to principal minors of order five, not all factors or the maximum-likelihood degree.

## Proof

**Factorization.** Since \(C\) is symmetric of rank five over \(\mathbb C\), congruence diagonalization gives \(C=XBX^{\mathsf T}\), with \(X\) a \(7\times5\) matrix of column rank five and \(B\) a nonsingular symmetric \(5\times5\) matrix. For every five-subset \(I\),
\[
\det C[I]=\det(B)\,(\det X_I)^2.
\]
Hence the nonvanishing five-subsets are precisely the bases of the rank-five row matroid \(M\) of \(X\).

**Small circuits vanish.** For any three distinct indices, the principal determinant is \(2c_{ij}c_{jk}c_{ki}\), which is nonzero. Thus every triple of rows of \(X\) is independent, so \(M\) has no circuits of size at most three.

**Rank-two dual.** The dual matroid \(N=M^*\) has rank two on seven elements. Let \(\ell\) be its number of loops, \(t=7-\ell\) the number of nonloops, and \(a_1,\dots,a_s\) the positive sizes of its nonloop parallel classes (each class is a rank-one flat). The cocircuits of \(N\) are exactly the complements of a loop set together with one parallel class; their sizes are \(t-a_j\). Circuits of \(M\) are cocircuits of \(N\). Therefore
\[
t-a_j\ge4\quad (1\le j\le s), \qquad t\in\{5,6,7\},\qquad a_j\le t-4.
\]
Complementation bijects bases of \(M\) with bases of \(N\). A basis of rank-two \(N\) consists of a pair of nonloop elements from different classes, so
\[
N_5(C)=\binom{t}{2}-\sum_{j=1}^s\binom{a_j}{2}.
\]

**Exhaustive list of numerical possibilities.** There is only one allowed integer partition of \(t=5\), namely \((1,1,1,1,1)\), giving \(10\). For \(t=6\), the allowed partitions are \((2,2,2)\), \((2,2,1,1)\), \((2,1,1,1,1)\), and \((1,1,1,1,1,1)\), giving respectively \(12,13,14,15\). For \(t=7\), the allowed partitions are \((3,3,1)\), \((3,2,2)\), \((3,2,1,1)\), \((3,1,1,1,1)\), \((2,2,2,1)\), \((2,2,1,1,1)\), \((2,1,1,1,1,1)\), and \((1,1,1,1,1,1,1)\), giving respectively \(15,16,17,18,18,19,20,21\). This exhausts the partitions because the maximum part is respectively \(1,2,3\). It proves the upper inclusion and forbids \(11\).

**Realization and sharpness.** The companion `witnesses.json` supplies one explicit symmetric integer \(7\times7\) scaling matrix for each of the thirteen partitions. The dependency-free exact-arithmetic `verify.py` checks symmetry, the zero diagonal, all \(21\) nonzero off-diagonal entries, rank exactly five, all \(21\) order-five principal determinants, and the dual rank-two loop/parallel partition inferred independently from complementary bases. The checker also generates all admissible integer partitions and verifies none is omitted. Its success proves that every pattern and every listed number is attained. These finite certificates establish finite realizations, while the factorization/matroid argument proves the universal exclusion of all other counts.

## Verification

Run `python3 verify.py` in the directory containing `verify.py` and `witnesses.json` using Python 3. The calculation uses exact rational Gaussian elimination and determinant computations, not numerical tolerances, and prints `VERIFY_OK; 13 exact witnesses`. Each matrix is specified in full by rational integers; no external data or algebra system is needed. The universal part of the proof is symbolic and independent of the finite checks.

## Relationship to prior work

Clarke, Hoşten, Kushnerchuk and Oldekop identify the principal \(A\)-determinant of the second hypersimplex with a product of principal minors of its symmetric scaling matrix, and tabulate the special rank-three scaling giving the minimum ML degree through seven and eight coordinates. Their author-maintained companion table has a seven-coordinate entry, but not this rank-five order-five factor-count spectrum. Oldekop studies these factor nonvanishing patterns through delta-matroids and proves an ML-degree minimum through six coordinates. The present classification isolates the first larger-order rank-five slice; it is not a proof of an ML-degree bound, a formula for all discriminant factors, or a refinement of the published rank-three minimum construction.

## Limitations

No assertion is made for \(\operatorname{rank}C\ne5\), for vanishing off-diagonal coefficients, for the full principal \(A\)-determinant factor support, or for the ML degrees of the represented varieties. The combinatorial ceiling argument uses characteristic other than two; the explicit realizations are over \(\mathbb Q\) and hence apply over \(\mathbb C\). A scheme-theoretic description of the parameter strata is not provided. Independent external validation has not been performed.

## References

1. Janike Oldekop, *Euler Stratifications of Second Hypersimplices via Delta-matroids*, arXiv:2606.16482v1 (first public 15 June 2026). https://arxiv.org/abs/2606.16482
2. Oliver Clarke, Serkan Hoşten, Nataliia Kushnerchuk and Janike Oldekop, *Matroid Stratification of ML Degrees of Independence Models*, *Algebraic Statistics* 15 (2024), 199–223, DOI 10.2140/astat.2024.15.199. https://mathrepo.mis.mpg.de/MLDegreeStratification/index.html
