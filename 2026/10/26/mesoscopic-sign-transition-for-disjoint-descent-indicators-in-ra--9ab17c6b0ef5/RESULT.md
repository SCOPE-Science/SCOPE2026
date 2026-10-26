# Mesoscopic sign transition for disjoint descent indicators in random involutions

## Finding
Let \(n\ge4\), and choose uniformly an involution \(\pi\) of \(\{1,\ldots,n\}\) with exactly \(f\) fixed points, where \(0\le f\le n\) and \(n-f\) is even. For \(1\le i<n\) define the descent indicator \(D_i=\mathbf1\{\pi(i)>\pi(i+1)\}\). For every \(1\le i<j<n\) with \(j-i\ge2\), put
\[
B_n(f)=(2n-3)f^3-nf^2+\(n^2\)f-\(n^2\)(n-2).
\]
Then the covariance is independent of the two nonadjacent positions and equals
\[
\operatorname{Cov}(D_i,D_j)=
-\frac{(n-f)B_n(f)}{2\(n^2\)(n-3)(n-2)(n-1)^2}.
\]
The polynomial \(B_n\) has a unique positive real zero \(\rho_n\) in \((0,n-2)\). For each admissible \(\(f<n\)\), the covariance is positive for \(f<\rho_n\), zero if \(f=\rho_n\), and negative for \(f>\rho_n\); for \(f=n\) it vanishes because the involution is deterministic. The transition occurs on the mesoscopic scale
\[
\frac{\rho_n}{n^{2/3}}\longrightarrow 2^{-1/3}.
\]
More precisely, along any parity-admissible sequence with \(f/n^{2/3}\to c\in[0,\infty)\),
\[
\(n^2\)\operatorname{Cov}(D_i,D_j)\longrightarrow\frac{1-2c^3}{2}.
\]
The unrestricted even-order fixed-point-free case is not claimed as new; its disjoint-descent joint probability is known. The claimed contribution is the fixed-point-conditioned phase classification and critical scale.

## Assumptions and scope
An involution is a permutation \(\pi\) satisfying \(\pi^2=\mathrm{id}\). Its cycle lengths are one or two. The uniform law conditions on precisely \(f\) one-cycles; it is not the uniform law over all involutions with a random number of fixed points. The positions \(i,j\) denote **disjoint adjacent comparisons**, meaning \(j-i\ge2\). Every formula is exact for finite integer \(n\ge4\) and every admissible \(f\), including the boundary cases \(\(f=0\)\) where allowed, \(f=n-2\), and \(f=n\). No assertion is made for adjacent comparisons \(j=i+1\).

## Proof
Write \(I_{a,b}\) for the number of involutions on \(a\) labeled points with exactly \(b\) fixed points. Set \(I_{a,b}=0\) for inadmissible parameters and otherwise
\[
I_{a,b}=\frac{a!}{2^{(a-b)/2}((a-b)/2)!b!}.
\]
Let \(A_2\) count the involutions under consideration with an ascent at one specified position, and let \(A_{22}\) count those with ascents at any two specified nonadjacent positions. We first establish that these counts depend only on the indicated one- or two-comparison patterns.

The descent-preserving Robinson--Schensted correspondence identifies involutions with standard Young tableaux; an involution's fixed-point count is the number of odd-length columns of its shape. For a composition \(\alpha=(\alpha_1,\ldots,\alpha_r)\) of \(n\), standardizing semistandard tableaux shows that the number of fixed-\(f\) involutions with all descents contained among the partial sums of \(\alpha\) is the coefficient of \(u^f x_1^{\alpha_1}\cdots x_r^{\alpha_r}\) in the classical weighted Littlewood identity
\[
\sum_{\lambda}u^{\mathrm{oddcols}(\lambda)}s_\lambda(x)
=\prod_a(1-ux_a)^{-1}\prod_{a<b}(1-x_ax_b)^{-1}.
\]
The right side is symmetric in the variables. To require one ascent, use a composition with one part of size two and all remaining parts of size one; for two separated ascents, use two parts of size two. Symmetry proves that the corresponding counts do not depend on the selected positions, so long as the two comparisons do not overlap.

For these two coefficient extractions, the product on the right counts symmetric nonnegative integer matrices with prescribed row sums and with each diagonal unit weighted by \(u\). Equivalently, it counts orbits of involutions on labeled tokens after identifying the two tokens in each repeated color, and forbidding pairs joining two tokens of the same color. Burnside's lemma gives
\[
A_2=\frac12\bigl(I_{n,f}-I_{n-2,f}+I_{n-2,f-2}\bigr)
\]
and
\[
\begin{aligned}
4A_{22}={}&I_{n,f}-2I_{n-2,f}+3I_{n-4,f}\\
&+2I_{n-2,f-2}-2I_{n-4,f-2}+I_{n-4,f-4}.
\end{aligned}
\]
For completeness, in the second count the identity of the two-token-swap group has \(I_{n,f}-2I_{n-2,f}+I_{n-4,f}\) valid matchings. Each of the two single swaps fixes \(I_{n-2,f-2}-I_{n-4,f-2}\) of them. The simultaneous swap fixes \(I_{n-4,f-4}+2I_{n-4,f}\): either all four tokens are fixed, or the two repeated-color pairs are cross-matched in one of two ways. Division by the group order four yields the displayed formula. The single-color formula is the analogous two-element Burnside count.

Since \(D_i=1-\mathbf1\{\text{ascent at }i\}\),
\[
\operatorname{Cov}(D_i,D_j)
=\frac{A_{22}}{I_{n,f}}-\left(\frac{A_2}{I_{n,f}}\right)^2.
\]
To simplify, whenever \(r-s\) is nonnegative and even, put \(k=(r-s)/2\). Then (with the zero conventions above)
\[
\frac{I_{n-r,f-s}}{I_{n,f}}
=\frac{f(f-1)\cdots(f-s+1)\prod_{h=0}^{k-1}(n-f-2h)}{n(n-1)\cdots(n-r+1)}.
\]
Substitution and polynomial expansion yield precisely the stated rational covariance, with \(B_n(f)\) as defined above. All denominators are positive for \(n\ge4\).

To classify the sign, observe that
\[
B_n(0)=-\(n^2\)(n-2)<0,
\qquad
B_n(n-2)=2(n-3)(n-2)^2(n-1)>0.
\]
Moreover \(B_n'(x)=3(2n-3)x^2-2nx+\(n^2\)\) is everywhere positive: its leading coefficient is positive and its discriminant \(4\(n^2\)(10-6n)\) is negative for \(n\ge4\). Thus \(B_n\) has exactly one zero \(\rho_n\in(0,n-2)\), and the covariance sign is as claimed.

Finally, for any fixed \(c\ge0\),
\[
\frac{B_n(cn^{2/3})}{n^3}\longrightarrow 2c^3-1.
\]
Strict monotonicity locates the zero at \(\rho_n\sim2^{-1/3}n^{2/3}\). If \(f/n^{2/3}\to c\) along admissible integers, then \((n-f)/n\to1\) and the denominator of the covariance has asymptotics \(2n^6\); the numerator has asymptotics \(-n^4(2c^3-1)\). This proves the displayed \(\(n^2\)\)-scaled limit.

## Verification
Run the accompanying standard-library-only \(\texttt{check.py}\) with Python 3. It exhaustively enumerates all involutions of sizes four through eleven, grouped by fixed-point count, and verifies single-descent probabilities, all pairs of adjacent or nonadjacent descent indicators, and the exact nonadjacent covariance. It also checks the rational coefficient formulas for every admissible \(f\) and \(4\le n\le100\). The saved verifier completed 3,743 exact comparisons on 48,920 explicitly enumerated involutions. These finite tests support the algebra but do not prove the formulas for all sizes; the proof above does.

## Relationship to prior work
Dukes (2004 preprint) established involution Eulerian polynomial symmetries and discussed the joint fixed-point/descent generating functions. Chow (2008), building on Gessel--Reutenauer and classical Littlewood identities, established general fixed-point-weighted descent-set enumeration. We use, rather than reprove as novel, that symmetric-function framework. Kim (2017) explicitly computed one- and two-position descent probabilities for fixed-point-free involutions, including the disjoint case, which is the \(\(f=0\)\) specialization above. Kim and Lee (2018) studied central limit laws and asymptotic variance for descents in permutation conjugacy classes. The contribution isolated here is the exact sign transition as prescribed fixed points vary, and its \(n^{2/3}\) scaling, neither of which was identified in the inspected primary statements.

## Limitations
The full descent-set law is already accessible through the general formulas in the cited literature; the present work does not claim a new enumeration of that law or priority for the fixed-point-free specialization. The sign transition follows from a particular explicit extraction and analysis of those formulas. A broader or overlooked theorem may subsume this characterization. Scientific priority is not independently verified. No full classification of correlations involving overlapping comparisons or higher-order joint descent events is asserted. The local covariance is of order \(n^{-2}\) in the critical window, not a claim of macroscopic dependence or a central limit theorem.

## References
- W. M. B. Dukes, *Permutation statistics on involutions*, arXiv:math/0412222v1, 11 December 2004, https://arxiv.org/abs/math/0412222.
- C.-O. Chow, *On the Eulerian enumeration of involutions*, Electronic Journal of Combinatorics **15** (2008), R71, https://doi.org/10.37236/795.
- G. B. Kim, *Distribution of descents in matchings*, arXiv:1710.03896v1, 11 October 2017, https://arxiv.org/abs/1710.03896.
- G. B. Kim and S. Lee, *Central limit theorem for descents in conjugacy classes of symmetric groups*, arXiv:1803.10457v1, 28 March 2018, https://arxiv.org/abs/1803.10457.
