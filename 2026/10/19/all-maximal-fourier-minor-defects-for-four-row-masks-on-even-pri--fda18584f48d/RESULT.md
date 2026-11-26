# All maximal Fourier-minor defects for four-row masks on even prime cycles

## Finding
Let \(p\ge5\) be an odd prime, \(N=2p\), \(\omega=e^{2\pi i/N}\), and let \(d\) be any integer with \(3\le d\le 2p-1\). Retain the four Fourier rows \(R_d=\{0,1,2,d\}\). For any four-element column set \(C\subset\mathbb Z_{2p}\), write \(F_{R_d,C}=(\omega^{rc})_{r\in R_d,c\in C}\). Every singular maximal minor has rank exactly three, and the following four mutually exclusive cases classify **all** singular minors:

1. If \(d\) is odd and \(d\notin\{p,p+2\}\), no maximal minor is singular.
2. If \(d\in\{p,p+2\}\), a maximal minor is singular exactly when all four column indices have the same parity. The number of singular maximal minors is \(2\binom p4\).
3. If \(d\) is even and \(d\ne p+1\), a maximal minor is singular exactly when its columns are two antipodal pairs, that is, \(C=\{a,a+p,b,b+p\}\) with distinct residues \(a,b\pmod p\). The number is \(\binom p2\).
4. If \(d=p+1\), a maximal minor is singular precisely when either its four column indices have one parity, or it has two even indices and two odd indices with the two even-index sums and two odd-index sums congruent modulo \(p\). The number is \(2\binom p4+\frac{p-1}{2}\binom p2\).

In particular, this four-row harmonic frame is full spark if and only if \(d\) is odd and \(d\notin\{p,p+2\}\). Equivalently, within this entire family, full spark holds exactly when the row set is uniformly distributed over the divisors of \(2p\). Cases 2–4 provide the complete singular-minor incidence beyond the mere full-spark dichotomy.

## Assumptions and scope
The row and column indices are interpreted modulo \(2p\), and the rows are distinct because \(3\le d\le2p-1\). For this statement, **full spark** means all \(4\times4\) column minors of the fixed \(4\times2p\) row submatrix are nonzero. A set of four row indices is **divisor-uniform** if its populations in residue classes modulo each divisor of \(2p\) differ by at most one. For this family, the divisor \(p\) presents four distinct classes except at \(d=p,p+1,p+2\); the divisor \(2\) presents the balanced \((2,2)\) population exactly when \(d\) is odd. The only nontrivial divisors are \(2\) and \(p\).

The theorem concerns complex Fourier matrices, not reductions modulo a finite field. A vanishing determinant means literal complex singularity. The prime restriction \(p\ge5\) ensures that four distinct column indices exist in each parity class and that the valuation estimate in the proof applies as stated.

## Proof
**Generalized Vandermonde reduction.** For distinct nodes \(z_1,z_2,z_3,z_4\), the determinant for row exponents \(0,1,2,d\) factors into the ordinary nonzero Vandermonde determinant and the complete homogeneous symmetric polynomial \(h_{d-3}(z_1,z_2,z_3,z_4)\), where
\[
\prod_{j=1}^{4}(1-z_jt)^{-1}=\sum_{m\ge0}h_m(z_1,z_2,z_3,z_4)t^m.
\]
Any minor has rank at least three, since its first three rows form a \(3\times4\) ordinary Vandermonde matrix on distinct nodes.

Write each column root uniquely as \(z_j=\epsilon_j\xi^{a_j}\), where \(\xi=\omega^{p+1}\) is a primitive \(p\)-th root, \(\epsilon_j\in\{1,-1\}\) is determined by the parity of the column index, and \(a_j\) is that index modulo \(p\). Distinct roots of the same sign have different exponents. In \(\mathbb Z[\xi]\), \(u=\xi-1\) generates a prime with residue field \(\mathbb F_p\), and \(p\) has \(u\)-adic valuation \(p-1\).

**Odd fourth row.** Then \(d-3\) is even. In the generating function, reduce the nodes to their signs modulo \(u\). The values of \(h_{d-3}\) for the three sign populations \(4+0\), \(3+1\), and \(2+2\) are, respectively,
\[
\binom d3,\qquad \left(\frac{d-1}{2}\right)^2,\qquad \frac{d-1}{2}.
\]
Indeed the three generating functions are, after an overall sign change if needed, \((1-t)^{-4}\), \((1-t)^{-2}(1-t^2)^{-1}\), and \((1-t^2)^{-2}\). In the allowed interval the last two coefficients are nonzero modulo \(p\). The first is zero modulo \(p\) exactly when \(d\equiv0,1,2\pmod p\), which for the odd admissible degrees means \(d=p,p+2\). This leaves only parity-pure minors in those degrees. In those minors the row of degree \(p\) or \(p+2\) is a fixed sign times row zero or row two, respectively, which proves cases 1 and 2.

**Even fourth row, parity-pure columns.** For \(d\ne p+1\), the residues \(0,1,2,d\pmod p\) are distinct. After removing row sign factors this is a minor of the order-\(p\) Fourier matrix on distinct column residues, so Chebotarev's prime-order Fourier-minor theorem gives nonsingularity. For \(d=p+1\) the fourth row on parity-pure columns is a fixed sign times row one, hence these minors vanish.

**Even fourth row, mixed signs.** Take the \(a_j\) to be in \(\{0,\ldots,p-1\}\), and expand the determinant of \(\epsilon_j^{r_i}(1+u)^{r_i a_j}\) as an integer polynomial in a formal variable \(u\). For the calculation through degree four use the formal parameter \(\tau=\log(1+u)\), so that \((1+u)^{r_i a_j}=\exp(r_i a_j\tau)\) as formal series; no logarithm at a numerical root of unity is needed. Through degree four the rational denominators are invertible modulo \(p\). Let \(Z=(A,B,C,D)\) be the exponent row and \(\epsilon\) the sign row, with powers of \(Z\) and products of rows taken entrywise. Put the rows in order \(0,2,d,1\), an even permutation, subtract row zero from the two other even rows and then subtract \(d/2\) times the modified row two from the modified row \(d\). The four rows are now
\[
\begin{split}
&\mathbf1,\qquad 2Z\tau+2Z^2\tau^2+O(\tau^3),\\
&\frac{d(d-2)}2 Z^2\tau^2+\frac{d(d^2-4)}6 Z^3\tau^3+O(\tau^4),\\
&\epsilon+\epsilon Z\tau+O(\tau^2).
\end{split}
\]
The determinant coefficients below degree three vanish. Its degree-three coefficient in \(u\) is its degree-three coefficient in \(\tau\), namely \(d(d-2)\det(\mathbf1,Z,Z^2,\epsilon)\), with the listed vectors as rows. For \(\epsilon=(+,+,+,-)\), subtracting the first row from the sign row reduces this last determinant to a three-node Vandermonde, giving the coefficient
\[
2d(d-2)(A-B)(A-C)(B-C).
\]
It is a unit modulo \(p\), since the three same-sign exponents are distinct and \(d,d-2\) are nonzero modulo \(p\) for admissible even \(d\). Reversing all signs multiplies the determinant by a nonzero row factor. Thus no \(3+1\) split is singular.

For \(\epsilon=(+,+,-,-)\), take differences within the two column pairs in \(\det(\mathbf1,Z,Z^2,\epsilon)\). The degree-three coefficient is
\[
-2d(d-2)(A-B)(C-D)(A+B-C-D).
\]
Thus singularity requires \(A+B=C+D\) in \(\mathbb F_p\). Under this congruence the degree-four coefficients in \(u\) and \(\tau\) agree modulo \(p\) because the lower coefficients vanish modulo \(p\). A common shift of all exponents scales each formal row by an exponential with constant coefficient one and does not change this coefficient. Subtract the common mean in \(\mathbb F_p\) so that \(Z=(x,-x,y,-y)\). Multilinearity in the displayed rows gives the degree-four coefficient as
\[
d(d-2)\det(\mathbf1,Z,Z^2,\epsilon Z)+\frac{d(d^2-4)}3\det(\mathbf1,Z,Z^3,\epsilon).
\]
The term with the second and third rows both proportional to \(Z^2\) is zero. Write \(Z^2=\alpha\mathbf1+\gamma\epsilon\), with \(\gamma=(x^2-y^2)/2\), and \(Z^3=\alpha Z+\gamma\epsilon Z\). The two determinants are \(\gamma\det(\mathbf1,Z,\epsilon,\epsilon Z)\) and its negative, respectively, and differences within the column pairs give \(\det(\mathbf1,Z,\epsilon,\epsilon Z)=16xy\). Therefore the degree-four coefficient modulo \(p\), in the original exponents, is
\[
\frac23 d(d-2)(d-1)(A-B)(C-D)(A-C)(B-C).
\]
Here \((A-B)(C-D)(A-C)(B-C)=-4xy(x^2-y^2)\) under centering. For even \(d\ne p+1\), the factor \(d-1\) is nonzero modulo \(p\). If the unordered pairs are different but have the same sum, then they share no exponent, so the displayed coefficient is a unit. On evaluating at \(u=\xi-1\), the third term has valuation at least \(3+(p-1)>4\) and higher terms have valuation at least five. The fourth term is uniquely of least valuation, so the determinant is nonzero. If the pairs coincide, the columns are two antipodal pairs; all even-degree rows agree on each pair and only row one distinguishes signs, giving rank three. This proves case 3, including \(d=4\).

**Central even row.** For \(d=p+1\), \(z^{p+1}=\epsilon z\), so parity-pure minors vanish. A \(3+1\) split is nonsingular by the mixed-sign degree-three calculation. For a \(2+2\) split, write the nodes as \(a,b,-c,-e\) with \(a,b,c,e\in\langle\xi\rangle\). Replace the last row by its difference with row one, and add half of the new last row to row one. These rows are then supported on separate pairs. Subtract within each pair after normalizing those rows by column factors, or expand directly, to obtain the determinant, up to sign,
\[
2(a-b)(c-e)(ab-ce).
\]
Both within-pair differences are nonzero, so singularity is equivalent to \(ab=ce\), the equality of the two exponent sums modulo \(p\). With the chosen \(\xi\) these are exactly the respective column-index sums modulo \(p\). This proves case 4.

**Counts and uniformity.** Each parity gives \(\binom p4\) pure column sets. The \(p\) antipodal pairs give \(\binom p2\) sets of two pairs. In the central case any choice of two even columns fixes their sum in \(\mathbb F_p\); there are \((p-1)/2\) unordered pairs of distinct odd columns with that sum, by excluding the one fixed residue under reflection about the half sum. These mixed sets are disjoint from the parity-pure sets. Finally, the row residues modulo \(p\) are all distinct except at \(d=p,p+1,p+2\); the parity split is balanced exactly when \(d\) is odd. Together with the rank lower bound, this proves the classification and the stated equivalence.

## Verification
`check.py` is an exact finite cyclotomic-zero checker. It expresses each minor using \(p\) integer coefficients of powers of \(\xi\), which vanish in combination precisely when all coefficients agree. The recorded checks cover all fourth rows at \(p=5,7,11\), and odd and central fourth rows at \(p=13\). The companion `verify_expansions.py` checks the corrected symbolic identities by determinant expansion in the formal exponential parameter. Run it with Python 3 and SymPy. Because the coefficients below degree three vanish, and degree three vanishes modulo \(p\) on the equal-sum locus, these exponential-parameter checks certify the two required coefficients in the cyclotomic parameter there. The checks are distinct from the all-prime valuation argument in the proof.

## Relationship to prior work
Alexeev, Cahill and Mixon's *Full Spark Frames* proves the prime-order Fourier-minor property and characterizes divisor-uniform full-spark row sets at prime-power orders, while giving composite-order counterexamples to general sufficiency. Osgood, Siripuram and Wu establish the equivalent universal-sampling framework in the prime-power setting. Neither prime-power result directly resolves Fourier order \(2p\) for all odd primes \(p\).

An earlier exact four-row classification handles \(\{0,1,2,4\}\) for arbitrary Fourier order. Its result agrees with case 3 at \(d=4\) but does not cover variable fourth-row exponents or the central \(p+1\) incidence regime. A separate result completely classifies order-14 full-spark row subsets; this covers the full-spark dichotomy at \(p=7\) but does not give the singular-column census for each fourth row. Related results for fixed row masks do not give the stated all-parameters incidence. The contribution is that incidence, including the anomalous central count, not the cyclotomic and Schur mechanisms individually.

## Limitations
This theorem is restricted to Fourier order twice an odd prime, the indicated four-row mask, and maximal minors. It gives no general all-row-set classification for composite Fourier matrices and does not extend the theorem to \(2p^k\) with \(k>1\). Possible implicit prior coverage of parts of the full-spark direction in the cited conference paper remains a literature risk; an unlocated equivalent exact incidence classification is not ruled out by literature searches.

## References
1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public version October 17, 2011.
2. B. Osgood, A. Siripuram, W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets in Discrete Bandlimited Spaces*, arXiv:1204.0992, first public version April 4, 2012.
3. A. Achanta et al., *Coprime Conditions for Fourier Sampling for Sparse Recovery*, IEEE SAM (2014), DOI:10.1109/SAM.2014.6882460.
4. *Exact singular minors for the near-consecutive four-row harmonic frame*, identifier `2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d`.
5. *Complete full-spark classification for row subsets of the order-\(14\) Fourier matrix*, identifier `2026/10/4/SCOPE-complete-full-spark-classification-for-row-subsets-of-the-order--be518195ffd5`.
