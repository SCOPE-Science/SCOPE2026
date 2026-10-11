# Sharp fourth moment, stability, and Euclidean distortion of the seven-sign cubic Walsh chaos

## Finding
Let \(\varepsilon_1,\ldots,\varepsilon_7\) be independent uniform signs. Let \(\mathcal T=\{S\subseteq\{1,\ldots,7\}:|S|=3\}\), of cardinality \(35\), and put \(\chi_S(\varepsilon)=\prod_{i\in S}\varepsilon_i\). For every real array \(a=(a_S)_{S\in\mathcal T}\), define \(Q_a=\sum_{S\in\mathcal T}a_S\chi_S\) and \(B=\sum_{S\in\mathcal T}a_S^2\). Then
\[
\boxed{\mathbb E Q_a^4\leq \frac{97}{5}B^2-14\sum_{S\in\mathcal T}\left(a_S^2-\frac B{35}\right)^2.}
\]
In particular, the optimal real \(L^2\)-to-\(L^4\) comparison on this homogeneous level is \(\|Q_a\|_4\leq(97/5)^{1/4}\|Q_a\|_2\). Equality is attained by the constant positive coefficient array, and by its coordinate-sign transforms \(a_S=c\prod_{i\in S}\sigma_i\), with nonzero real \(c\) and signs \(\sigma_i\). The Banach--Mazur distance to the 35-dimensional real Hilbert space satisfies
\[
\boxed{d_{\mathrm{BM}}(X_{7,3},\ell_2^{35})=(97/5)^{1/4},\quad X_{7,3}=\operatorname{span}\{\chi_S:S\in\mathcal T\}\subset L^4.}
\]
Here the Banach--Mazur distance is the infimum of the products of an invertible linear map norm and its inverse norm.

## Assumptions and scope
All coefficients and norms are real. The probability space is the uniform 128-point sign cube. \(\|Q\|_p=(\mathbb E|Q|^p)^{1/p}\), and orthogonality gives \(\|Q_a\|_2^2=B\). The formula is a fixed-dimension theorem for exactly seven signs, homogeneous degree three, and exponent four; it does not claim corresponding formulas for other degrees, dimensions, or complex coefficients. The remainder constant \(14\) is valid but is not asserted to be optimal as a stability coefficient.

## Proof
**Walsh fourth-power expansion.** Write \(y_S=a_S^2\) and \(q=\sum_S y_S^2\). The product of four Walsh characters has expectation one exactly when the symmetric difference of their supports is empty. By classifying repeated indices,
\[
\mathbb E Q_a^4=3B^2-2q+24\sum_{F\in\mathcal Q}\prod_{S\in F}a_S,
\]
where \(\mathcal Q\) contains all unordered sets of four *distinct* triples whose symmetric difference is empty. For four real numbers \(u_1,\ldots,u_4\), three applications of the arithmetic--geometric mean inequality to complementary pairs give
\[
\big|u_1u_2u_3u_4\big|\leq \frac16\sum_{1\leq i<j\leq4}u_i^2u_j^2.
\]
Thus it remains to count the number of zero-symmetric-difference quadruples containing a specified unordered pair of triples.

**Pair counts.** For two distinct triples \(S,T\), set \(d=|S\mathbin\triangle T|\in\{2,4,6\}\). To choose a triple \(U\) with \(U\mathbin\triangle V=S\mathbin\triangle T\) and \(|V|=3\), it is necessary and sufficient to choose \(d/2\) elements of \(S\mathbin\triangle T\) and \(3-d/2\) elements of its complement. Hence the number of unordered pairs \(\{U,V\}\) is
\[
 p_d=\frac12\binom d{d/2}\binom{7-d}{3-d/2}=\begin{cases}10,&d=2,6,\\9,&d=4.\end{cases}
\]
Discarding the original pair leaves \(c_{S,T}=p_d-1\) quadruples, namely \(9\) if \(|S\cap T|=2\) or \(0\), and \(8\) if \(|S\cap T|=1\). (The remaining pair is automatically disjoint from the original one because a triple with the same symmetric difference as \(S,T\) that equals either \(S\) or \(T\) must equal the original pair.) Consequently, if \(\mathcal E\) denotes the unordered pairs \(\{S,T\}\) with \(|S\cap T|=1\),
\[
\begin{aligned}
\mathbb E Q_a^4
&\leq 3B^2-2q+4\sum_{S<T}c_{S,T}y_Sy_T\\
&=21B^2-20q-4\sum_{\{S,T\}\in\mathcal E}y_Sy_T.
\end{aligned}
\]

**A special strongly regular graph.** Let \(A\) be the 35-by-35 adjacency matrix on \(\mathcal T\) for the relation \(|S\cap T|=1\). Each vertex has \(\binom31\binom42=18\) neighbors. Distinct vertices have precisely nine common neighbors: if \(r=|S\cap T|\in\{0,1,2\}\), partition \(\{1,\ldots,7\}\) into \(S\cap T\) of size \(r\), the two one-sided differences of size \(3-r\) each, and the exterior of size \(r+1\). A common neighbor must have one member from each of \(S\) and \(T\), yielding
\[
N_r=\sum_{i=0}^{1}\binom ri\binom{3-r}{1-i}^{\!2}\binom{r+1}{1+i}=9
\quad (r=0,1,2).
\]
Thus \(A\mathbf1=18\mathbf1\) and \(A^2=9I+9J\), where \(J=\mathbf1\mathbf1^{\mathsf T}\). For any \(z\perp\mathbf1\), \(\|Az\|_2^2=9\|z\|_2^2\), so symmetry implies \(z^{\mathsf T}Az\geq-3\|z\|_2^2\).

**Remainder and optimal constant.** Decompose \(y=(B/35)\mathbf1+z\), with \(\sum_Sz_S=0\). Since \(\sum_{\{S,T\}\in\mathcal E}y_Sy_T=\tfrac12y^{\mathsf T}Ay\),
\[
5q+\sum_{\mathcal E}y_Sy_T=\frac25B^2+5\|z\|_2^2+\frac12z^{\mathsf T}Az\geq\frac25B^2+\frac72\|z\|_2^2.
\]
Substituting gives the claimed \(97B^2/5-14\|z\|_2^2\) inequality. For \(a_S=c\) all quadruple products are positive and equality holds in the arithmetic--geometric mean step; also \(z=0\). Hence \(97/5\) is exact. Replacing \(c\) by \(c\prod_{i\in S}\sigma_i\) is equivalent to flipping the input signs and preserves all norms.

**The optimal Euclidean position.** The sign changes of the underlying seven variables act diagonally on the 35 coefficient coordinates by distinct Walsh characters, and permutations of those variables act transitively on the triples. Thus averaging any positive-definite quadratic form \(H\) over this finite isometry group yields a scalar multiple of \(\sum_Sa_S^2\). If \(m\sqrt{H(a)}\leq\|Q_a\|_4\leq M\sqrt{H(a)}\) for all \(a\), the same inequalities hold for each group translate of \(H\); after squaring and averaging, the same ratio \(M/m\) works for the scalar Euclidean form. Therefore no Euclidean renorming improves the coordinate \(\ell_2\) distortion. For this form, \(\inf_{a\ne0}\|Q_a\|_4/\|Q_a\|_2=1\) by Jensen, attained by a single Walsh character, and the sharp supremum is \((97/5)^{1/4}\). This proves the Banach--Mazur formula.

## Verification
The accompanying standalone Python script uses exact integer and rational arithmetic. It independently enumerates all 35 triples, the 840 admissible distinct XOR-zero quadruples, the pair multiplicities \(9,8,9\), the degree-18 graph and all entries of \(A^2=9I+9J\). It also expands sample fourth moments using all 128 sign vectors and checks the rational stability inequality. The result was `VERIFY_OK`. The exhaustive combinatorial identities are proved for the entire fixed-size finite universe by complete enumeration; the analytic inequalities and Euclidean averaging are proved symbolically above rather than inferred from numerical tests. Run with `python3 verify.py` using the Python standard library.

## Relationship to prior work
Major's 2004 preprint gives general moment and tail estimates for homogeneous Rademacher polynomials; its estimates do not state the exact 35-dimensional constant or the stability remainder. Polyanskiy's Fourier-degree projection analysis (first submitted 2013; Section 2.3 of the available 2018 revision) estimates \(L^p\)-to-\(L^2\) projection norms but does not identify this exact \(L^2\)-to-\(L^4\) constant or the Euclidean distortion. Pass and Spektor (2014) study universal inequalities for pairwise-independent and exchangeable sign vectors; the fixed joint law of all 35 degree-three Walsh characters is not a generic exchangeable sign law, and their fourth-power bound \(35\) is weaker than \(97/5\). The seven-sign cubic case uses a 35-vertex intersection graph; it is not just the parity-doubled six-sign cubic reduction to smaller quadratic chaos. These comparisons do not exclude every unindexed historical equivalent theorem.

## Limitations
Only real coefficients, seven variables, homogeneous degree three and exponent four are addressed. The listed flat-character coefficients attain equality; a classification of all equality cases is not claimed. The coefficient \(14\) is not asserted sharp among possible quantitative stability remainders. Nothing is claimed for general cubic polynomial spaces or all dimensions, and bibliographic originality remains subject to specialized unindexed literature. Independent audit has not been performed.

## References
1. P. Major, *A multivariate generalization of Hoeffding's inequality*, arXiv:math/0411288v1 (first publicly submitted 2004-11-12), https://arxiv.org/abs/math/0411288.
2. Y. Polyanskiy, *Hypercontractivity of spherical averages in Hamming space*, arXiv:1309.3014v1 (first submitted 2013-09-12); Section 2.3 of v2 (2018), https://arxiv.org/abs/1309.3014.
3. B. Pass and S. Spektor, *On Khintchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859v1 (first submitted 2014-12-25), https://arxiv.org/abs/1412.7859.
