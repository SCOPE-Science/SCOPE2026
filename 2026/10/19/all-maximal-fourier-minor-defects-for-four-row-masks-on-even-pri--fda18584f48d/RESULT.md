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
**Generalized Vandermonde reduction.** For distinct \(N\)-th roots \(z_1,z_2,z_3,z_4\), the determinant for row exponents \(0,1,2,d\) factors into the ordinary nonzero Vandermonde determinant and the complete homogeneous symmetric polynomial \(h_{d-3}(z_1,z_2,z_3,z_4)\). The latter is defined by
\[
\prod_{j=1}^{4}(1-z_jt)^{-1}=\sum_{m\ge0}h_m(z_1,z_2,z_3,z_4)t^m.
\]
Any minor's rank is at least three, since its first three rows constitute the \(3\times4\) ordinary Vandermonde evaluation on four distinct nodes.

Write each column root uniquely as \(z_j=\epsilon_j\xi^{a_j}\), where \(\xi\) is a primitive \(p\)-th root, \(\epsilon_j\in\{1,-1\}\), and \(a_j\in\mathbb F_p\). The sign is determined by the parity of the original column index. Distinct roots with the same sign have different \(a_j\). Work in the cyclotomic integer ring \(\mathbb Z[\xi]\) and put \(u=\xi-1\). Reduction modulo the prime ideal \((u)\) sends \(\xi\) to \(1\) and identifies the residue field with \(\mathbb F_p\). Moreover, \(p\) has \(u\)-adic valuation \(p-1\).

**Odd fourth row.** If \(d\) is odd, \(d-3\) is even. Evaluating the generating function at the reductions \(z_j\mapsto\epsilon_j\), the values of \(h_{d-3}\) for the three sign-balance types (up to overall sign) are, respectively,
\[
\binom d3,\qquad \left(\frac{d-1}{2}\right)^2,\qquad \frac{d-1}{2}
\]
for sign populations \(4+0\), \(3+1\), and \(2+2\). For \(3\le d\le2p-1\), the last two integers are nonzero modulo \(p\). Since \(p\ge5\), \(p\mid\binom d3\) occurs exactly when \(d\equiv0,1,2\pmod p\); the odd integers in the permitted interval with that property are exactly \(p\) and \(p+2\). Therefore no determinant can vanish outside these two exceptional degrees, and a vanishing determinant at either requires all four column roots to have the same sign. Conversely, when all signs agree, the row of exponent \(p\) is the same fixed multiple of row zero, and the row of exponent \(p+2\) is the same fixed multiple of row two. This proves cases 1 and 2.

**Even fourth row, all four signs alike.** Now \(d\) is even. For \(d\ne p+1\), the residues \(0,1,2,d\pmod p\) are pairwise distinct. Within a fixed sign, the four column roots differ by distinct \(p\)-th roots, so the minor reduces, up to nonzero row and column factors, to a \(4\times4\) minor of the order-\(p\) Fourier matrix. Chebotarev's prime-order Fourier-minor theorem makes this nonsingular. At \(d=p+1\), by contrast, the fourth row agrees up to fixed sign with row one, so every parity-pure column set is singular.

**Even fourth row, mixed signs, away from the central degree.** It remains to analyze sign populations \(3+1\) and \(2+2\). Expand \(\det(z_j^{r_i})\), where \(r_i=0,1,2,d\), in powers of \(u\) by putting \(z_j=\epsilon_j(1+u)^{a_j}\) and applying the binomial theorem (the exponents \(a_j\) may be represented by arbitrary integers). This is a polynomial in \(u\) with coefficients in \(\mathbb Z\) because \(d\) is a nonnegative integer. For either mixed pattern, the coefficients of \(u^0,u^1,u^2\) vanish identically. All displayed coefficient congruences are in \(\mathbb F_p\), so replacing an exponent by another representative modulo \(p\) does not affect them.

For signs \((+,+,+,-)\) and corresponding exponents \((A,B,C,D)\), the \(u^3\)-coefficient is
\[
2d(d-2)(A-B)(A-C)(B-C).
\]
The factors are all nonzero modulo \(p\) when \(d\) is even in the permitted interval and the three plus-sign roots are distinct. Thus no \(3+1\) minor can be singular.

For signs \((+,+,-,-)\), the \(u^3\)-coefficient is
\[
-2d(d-2)(A-B)(C-D)(A+B-C-D).
\]
Since \(d(d-2)\not\equiv0\pmod p\) for even \(d\) in the permitted interval, vanishing forces \(A+B\equiv C+D\pmod p\). Subject to that congruence, the \(u^4\)-coefficient modulo \(p\) becomes
\[
\frac23d(d-2)(d-4)(A-B)(C-D)(A-C)(B-C).
\]
If \(d\notin\{4,p+1\}\), and the two unordered exponent pairs \(\{A,B\}\) and \(\{C,D\}\) are different, then \(A-C\) and \(B-C\) are also nonzero (otherwise equal sums would make both pairs identical). Hence this fourth coefficient is a unit modulo \(p\). The third coefficient is divisible by \(p\) and consequently has \(u\)-adic valuation at least \(p-1+3>4\); the first nonzero term has valuation exactly four. Thus the determinant is nonzero. If the two pairs are identical, the four roots consist of two antipodal pairs; all even-exponent Fourier rows agree within each pair, and only row one distinguishes the signs, so the rank is exactly three.

For \(d=4\), the Vandermonde factorization reads \(\det=V(z)(z_1+z_2+z_3+z_4)\). For sign populations \((+,+,-,-)\), this sum vanishes precisely when \(\xi^A+\xi^B=\xi^C+\xi^D\), which forces equality of the two unordered pairs: otherwise a nonzero polynomial of degree at most \(p-1\), with at most four nonzero coefficients, would be divisible by \(\Phi_p(T)=1+\cdots+T^{p-1}\), impossible for \(p\ge5\) unless the coefficients all cancel. This proves case 3, including its exact incidence description.

**Central even row.** When \(d=p+1\), note \(z^{p+1}=z^p z=\epsilon z\). Therefore parity-pure minors vanish. A \(3+1\) sign split cannot vanish, since an elementary row combination isolates the singleton column and the three same-sign columns form a nonsingular three-row Vandermonde block. For a \(2+2\) split, write the positive roots as \(a,b\in\langle\xi\rangle\) and the negative roots as \(-c,-e\), with \(c,e\in\langle\xi\rangle\). The determinant is exactly, up to column ordering,
\[
2(a-b)(c-e)(ab-ce).
\]
It vanishes exactly when the two products are equal, or equivalently when the sums of their two \(p\)-exponents agree. The latter condition is equivalent to equality modulo \(p\) of the sums of the two even and two odd column indices, since the map from indices to exponents is an invertible multiplication modulo \(p\). This proves case 4.

**Counts and uniformity.** There are \(p\) columns of each parity, yielding \(2\binom p4\) parity-pure sets. The \(p\) antipodal index-pairs produce \(\binom p2\) distinct two-pair column sets. For the central degree, choosing the two even columns gives \(\binom p2\) options; their sum in \(\mathbb F_p\) fixes a sum value for which exactly \((p-1)/2\) unordered pairs of distinct odd columns exist. The two contributions are disjoint and sum to \(2\binom p4+(p-1)\binom p2/2\). The row residue populations modulo \(2\) are \((2,2)\) exactly when \(d\) is odd, while modulo \(p\) they are all distinct except for \(d=p,p+1,p+2\). This proves the equivalence with divisor-uniformity and finishes the classification.

## Verification
The standalone `check.py` computes every \(4\times4\) Fourier minor as an exact element of \(\mathbb Z[\xi]\). A polynomial of degree below \(p\) vanishes at \(\xi\) precisely when all its \(p\) coefficients agree, which makes the checker an exact integer-arithmetic test rather than a floating-point rank calculation. It compares every column set with the stated structural criterion for all \(d\) when \(p\in\{5,7,11\}\), and every odd \(d\) plus the central even \(d=p+1\) at \(p=13\). All checks passed.

The companion `verify_expansions.py` uses symbolic binomial expansions of the actual four-row determinant to verify vanishing of the coefficients through degree two, the two \(u^3\)-coefficient identities, and the conditional \(u^4\) identity. It also passed. The unrestricted theorem follows from the preceding proof, not from a finite test range.

## Relationship to prior work
Alexeev, Cahill and Mixon's *Full Spark Frames* proves Chebotarev's Fourier-minor property and characterizes divisor-uniform full-spark row sets at prime-power orders, while giving composite-order counterexamples to general sufficiency. Osgood, Siripuram and Wu establish the equivalent universal-sampling framework in the prime-power setting. Thus neither prime-power result directly resolves Fourier order \(2p\) for all odd primes \(p\).

An earlier published four-row classification handles \(\{0,1,2,4\}\) for arbitrary Fourier order. Its result agrees with case 3 at \(d=4\) but does not cover variable fourth-row exponents or the central \(p+1\) incidence regime. Separate published work completely classifies order-14 full-spark row subsets, but cannot imply a uniform exact maximal-minor classification for all \(p\ge5\). Prior work on three-row minors and the \(\{0,1,3,4\}\) pattern also does not imply this theorem. The immediately related fixed \(\{0,1,2,5\}\) classification on twice odd prime powers is subsumed at prime exponent one by case 1 or 2, but is not a complete varying-fourth-row incidence theorem.

The cyclotomic and Schur mechanisms are not claimed as new individually; the contribution is the four-case **all-parameters, all-maximal-minors** classification, including the anomalous central count. See the literature citations below.

## Limitations
This theorem is restricted to Fourier order twice an odd prime, the indicated four-row mask, and maximal minors. It is not a general all-row-set classification for composite Fourier matrices, and it does not extend the theorem to \(2p^k\) with \(k>1\). Although relevant primary preprints were inspected in full, an IEEE conference paper concerning coprime conditions for sparse Fourier sampling was available only as an abstract; implicit prior coverage of parts of the full-spark direction remains a literature risk. An unindexed equivalent exact singular-minor classification is not ruled out by literature searches. Independent mathematical validation and publication-priority assessment have not been performed.

## References
1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public version October 17, 2011.
2. B. Osgood, A. Siripuram, W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992, first public version April 4, 2012.
3. A. Achanta et al., *Coprime Conditions for Fourier Sampling for Sparse Recovery*, IEEE SAM (2014), DOI:10.1109/SAM.2014.6882460 (abstract inspected, full text unavailable).
4. *Exact singular minors for the near-consecutive four-row harmonic frame*, publicly accessible research finding, October 2026, identifier `2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d`.
5. *Complete full-spark classification for row subsets of the order-\(14\) Fourier matrix*, publicly accessible research finding, October 2026, identifier `2026/10/4/SCOPE-complete-full-spark-classification-for-row-subsets-of-the-order--be518195ffd5`.
