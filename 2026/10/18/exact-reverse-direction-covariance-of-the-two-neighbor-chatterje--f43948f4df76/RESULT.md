# Exact reverse-direction covariance of the two-neighbor Chatterjee rank statistic

## Finding

Consider the Lin–Han right-nearest-neighbor rank coefficient with exactly two neighbors, denoted \(\xi_{n,2}(X,Y)\). Under independent continuous marginals, for every integer \(n\ge4\), its forward and reverse versions have **strictly positive** covariance and the exact correlation

\[
\boxed{\operatorname{Corr}(\xi_{n,2}(X,Y),\xi_{n,2}(Y,X))=
\frac{10(4n^4+n^3+11n^2-127n+147)}
{n(n-1)(n+1)(4n^2+14n+35)}.}
\]

The correlation attains its unique integer-sample-size maximum at \(n=5\), with value \(201/205\); at \(n=4\) it is \(301/310\), and it strictly decreases for every \(n\ge5\). In particular,
\[
\lim_{n\to\infty}n\operatorname{Corr}(\xi_{n,2}(X,Y),\xi_{n,2}(Y,X))=10.
\]

More precisely, the finite-sample mean is zero and
\[
\begin{aligned}
\operatorname{Var}(\xi_{n,2}(X,Y))
&=\frac{4(4n^2+14n+35)}{5(n+1)(4n+3)^2},\\
\operatorname{Cov}(\xi_{n,2}(X,Y),\xi_{n,2}(Y,X))
&=\frac{8(4n^4+n^3+11n^2-127n+147)}
{n(n-1)(n+1)^2(4n+3)^2}.
\end{aligned}
\]

Consequently, \(n\operatorname{Var}(\xi_{n,2})\to1/5\) while \(n^2\operatorname{Cov}(\xi_{n,2}(X,Y),\xi_{n,2}(Y,X))\to2\). The covariance statement concerns only second moments; it does **not** assert a bivariate central limit theorem.

## Assumptions and scope

Let \((X_i,Y_i)\), \(1\le i\le n\), be independent and identically distributed pairs, where \(X\) and \(Y\) are independent and each has an atomless distribution. Sorting observations by increasing \(X\) makes their \(Y\)-rank sequence \(\pi=(\pi_1,\ldots,\pi_n)\) a uniform permutation of \(\{1,\ldots,n\}\). Sorting by \(Y\) instead gives \(\pi^{-1}\).

The coefficient is exactly the Lin–Han normalization [1, equation (2.4)] with \(M=2\): the first and second right neighbors are used when available, and unavailable right neighbors are replaced by the observation itself. Thus define
\[
S(\pi)=\sum_{i=1}^{n-1}\min(\pi_i,\pi_{i+1})
+\sum_{i=1}^{n-2}\min(\pi_i,\pi_{i+2})+\pi_{n-1}+2\pi_n,
\qquad
c_n=\frac{12}{(n+1)(4n+3)}.
\]
Then \(\xi_{n,2}(X,Y)=-2+c_nS(\pi)\) and \(\xi_{n,2}(Y,X)=-2+c_nS(\pi^{-1})\). All assertions concern integers \(n\ge4\), with no assumptions about marginal densities, symmetry, or moments beyond atomlessness and independence.

## Proof

**Step 1: a permutation quadratic-assignment identity.** Write \(E\) for the set of two-element subsets of \(\{1,\ldots,n\}\). For real arrays \(A=(A_{ij})_{\{i,j\}\in E}\) and \(B=(B_{ij})_{\{i,j\}\in E}\), let
\[
T_{A,B}(\pi)=\sum_{i<j}A_{ij}B_{\pi_i\pi_j},
\]
where the subscripts of \(B\) are unordered. Define the edge mean \(\bar A=|E|^{-1}\sum_{i<j}A_{ij}\), edge-centered array \(A^\circ_{ij}=A_{ij}-\bar A\), and centered vertex sums \(s_i(A)=\sum_{j\ne i}A^\circ_{\min(i,j),\max(i,j)}\). Notice that \(\sum_i s_i(A)=0\). Set
\[
A^{[1]}_{ij}=\frac{s_i(A)+s_j(A)}{n-2},
\qquad A^{[2]}=A^\circ-A^{[1]}.
\]
Use analogous notation for \(B\), and the usual Euclidean inner product on edge arrays. For every \(n\ge4\),
\[
\begin{aligned}
\operatorname{Var}(T_{A,B}(\pi))
&=\frac{\|A^{[1]}\|^2\|B^{[1]}\|^2}{n-1}
+\frac{\|A^{[2]}\|^2\|B^{[2]}\|^2}{n(n-3)/2},\\
\operatorname{Cov}(T_{A,B}(\pi),T_{A,B}(\pi^{-1}))
&=\frac{\langle A^{[1]},B^{[1]}\rangle^2}{n-1}
+\frac{\langle A^{[2]},B^{[2]}\rangle^2}{n(n-3)/2}.
\end{aligned}\tag{1}
\]

For completeness, the edge-permutation representation has three explicit orthogonal invariant subspaces: the constant arrays, the arrays of the form \(a_i+a_j\) with \(\sum_i a_i=0\), and their orthogonal complement, respectively of dimensions \(1\), \(n-1\), and \(n(n-3)/2\). The three corresponding orthogonal projections are exactly the mean, \([1]\), and \([2]\) terms displayed above. A matrix commuting with every permutation of the vertices has entries indexed by pairs of edges that depend only on whether their intersection has \(0\), \(1\), or \(2\) vertices. Consequently, the real commutant has dimension exactly three. Since the three explicit nonzero projections already furnish three mutually orthogonal invariant summands, no summand decomposes further; the three representations are inequivalent irreducibles. Applying real matrix-coefficient orthogonality in each of the two nonconstant summands gives (1). In particular, for an irreducible real orthogonal representation of dimension \(d\), the two identities used are \(\mathbb E\langle a,U_\pi b\rangle^2=\|a\|^2\|b\|^2/d\) and \(\mathbb E[\langle a,U_\pi b\rangle\langle a,U_{\pi^{-1}}b\rangle]=\langle a,b\rangle^2/d\). The equality of these coefficients follows directly by averaging the rank-one operators over the group and using irreducibility; thus no independence of reversed statistics is assumed.

**Step 2: separate edges and boundary ranks.** On unordered pairs define \(A_{ij}=\boldsymbol{1}\{1\le|i-j|\le2\}\), \(B_{ij}=\min(i,j)\); on vertices define \(\ell_i=i\), and \(u_i=\boldsymbol{1}\{i=n-1\}+2\boldsymbol{1}\{i=n\}\). Then
\[
S(\pi)=T_{A,B}(\pi)+L(\pi),
\qquad L(\pi)=\sum_i u_i\ell_{\pi_i}.
\]
Direct summation gives the six projection quantities
\[
\begin{array}{c|c}
\text{quantity}&\text{exact value}\\\hline
\|A^{[1]}\|^2&2(5n-18)/[n(n-2)]\\
\|A^{[2]}\|^2&(2n^3-17n^2+43n-26)/[(n-2)(n-1)]\\
\|B^{[1]}\|^2&n(n-1)(n+1)(4n-7)/180\\
\|B^{[2]}\|^2&n(n-3)(n-1)(n+1)/180\\
\langle A^{[1]},B^{[1]}\rangle&(n-3)/2\\
\langle A^{[2]},B^{[2]}\rangle&(n-3)(2n-7)/6.
\end{array}\tag{2}
\]
These are explicit polynomial sums, not estimated moments. One route to checking them is \(\bar B=(n+1)/3\), \(s_i(B)=in-i(i+1)/2-(n-1)(n+1)/3\), \(\|B^{[1]}\|^2=\sum_i s_i(B)^2/(n-2)\), the degree sequence of \(A\), and \(\|A^{[2]}\|^2=\|A^\circ\|^2-\|A^{[1]}\|^2\), likewise for \(B\). The same subtraction gives the mixed \([2]\)-inner product.

Substitution in (1) yields
\[
\begin{aligned}
\operatorname{Var}(T_{A,B})&=(n+1)(2n^2+7n-50)/90,\\
\operatorname{Cov}(T_{A,B}(\pi),T_{A,B}(\pi^{-1}))
&=(n-3)(n-2)(8n^2-39n+49)/[36n(n-1)].
\end{aligned}\tag{3}
\]

**Step 3: all boundary cross terms.** For centered vertex vectors \(a,b,c,d\), uniform-permutation sampling gives
\[
\operatorname{Cov}\left(\sum_i a_i b_{\pi_i},\sum_i c_i d_{\pi_i}\right)
=\frac{(a\cdot c)(b\cdot d)}{n-1}.\tag{4}
\]
The \([1]\)-component of \(T_{A,B}\) is the vertex statistic \((n-2)^{-1}\sum_i s_i(A)s_{\pi_i}(B)\), and the \([2]\)-component is orthogonal to vertex statistics. Center \(u,\ell\) as \(u^\circ,\ell^\circ\). Direct sums show
\[
\begin{aligned}
s(A)\cdot\ell^\circ&=0,&s(A)\cdot u^\circ&=-5+18/n,\\
s(B)\cdot\ell^\circ&=n(n-2)(n-1)(n+1)/24,
&u^\circ\cdot\ell^\circ&=(3n-5)/2,\\
\|u^\circ\|^2&=5-9/n,&\|\ell^\circ\|^2&=n(n^2-1)/12.
\end{aligned}\tag{5}
\]
By (4)–(5),
\[
\begin{aligned}
\operatorname{Var}(L)&=(n+1)(5n-9)/12,\\
\operatorname{Cov}(T_{A,B}(\pi),L(\pi))&=-(n+1)(5n-18)/24,\\
\operatorname{Cov}(T_{A,B}(\pi),L(\pi^{-1}))&=0,\\
\operatorname{Cov}(L(\pi),L(\pi^{-1}))&=(3n-5)^2/[4(n-1)].
\end{aligned}\tag{6}
\]
The zero third line uses the exact reflection cancellation \(s(A)\cdot\ell^\circ=0\), not a limiting approximation. Reversal symmetry gives the remaining cross-covariances.

**Step 4: sum the moments.** The mean of \(T_{A,B}\) is \((2n-3)(n+1)/3\); that of \(L\) is \(3(n+1)/2\), so
\[
\mathbb ES(\pi)=(n+1)(4n+3)/6.
\]
Combining (3) and (6) yields
\[
\begin{aligned}
\operatorname{Var}(S(\pi))&=(n+1)(4n^2+14n+35)/180,\\
\operatorname{Cov}(S(\pi),S(\pi^{-1}))
&=(4n^4+n^3+11n^2-127n+147)/[18n(n-1)].
\end{aligned}\tag{7}
\]
Since \(c_n\mathbb ES=2\), the coefficient is centered. Multiply (7) by \(c_n^2\) for the theorem's covariance and variance, and divide to obtain its correlation.

**Step 5: signs, exact maximizer, and limits.** Formula (1) plus (6) shows the reversed covariance is strictly positive: its \(\operatorname{Cov}(L,L^\mathrm{inv})\) term is positive for \(n\ge4\), and every other surviving term is a square divided by a positive dimension. The correlation formula is rational. For the difference between consecutive sample sizes, straightforward common-denominator expansion gives
\[
\rho_{n+1}-\rho_n=-\frac{10P(n)}{n(n-1)(n+1)(n+2)(4n^2+14n+35)(4n^2+22n+53)},
\]
where \(\rho_n=\operatorname{Corr}(\xi_{n,2}(X,Y),\xi_{n,2}(Y,X))\) and
\[
P(n)=16n^6+56n^5+90n^4-1536n^3-3967n^2-2969n+16842.
\]
Here \(P(4)=-10890<0\); for every \(k\ge0\),
\[
P(5+k)=16k^6+536k^5+7490k^4+54264k^3+206493k^2+362161k+192072>0.
\]
Thus \(\rho_5>\rho_4\), whereas \(\rho_{n+1}<\rho_n\) for all \(n\ge5\), proving the unique maximum. Taking leading terms of the exact expressions gives the three asymptotic limits above.

## Verification

The accompanying standalone Python 3 script `verify.py` uses only standard-library exact rational arithmetic. It independently enumerates all \(n!\) permutations for each \(4\le n\le8\), computes both directions' scores directly, and checks the resulting exact means, variances and covariances against (7). It separately recomputes the edge projections and their norms/inner products from their definitions for \(4\le n\le40\), tests every displayed moment decomposition, and checks the finite correlation inequalities up to \(n=500\). These are finite exact consistency checks; irreducibility, covariance identities for all \(n\), and the sharp monotonicity follow from the preceding proof, not enumeration.

## Relationship to prior work

Lin and Han [1] introduce the \(M\)-right-neighbor statistic and derive null marginal moments and asymptotics. Zhang [2] proves reverse-direction covariance and joint asymptotic normality for **Chatterjee's original, one-neighbor coefficient**, and explicitly identifies \(M\ge2\) reverse-direction joint calculations as a remaining problem. The present claim treats precisely the first nontrivial neighbor extension \(M=2\), giving its exact forward/reverse finite-sample correlation and leading decay constant. The Johnson two-subset decomposition used in the proof is a standard permutation-representation technique and is not claimed as new. Other rank-based symmetrization work [3] has a different statistic and does not itself provide this exact second-moment law.

## Limitations

The result applies only to independent atomless marginals and exactly two **right** neighbors, with Lin–Han's self-replacement boundary convention. It neither supplies the joint limit distribution nor proves validity of a normal or skew-normal calibration for the maximum of the two statistics. In particular, asymptotically vanishing correlation alone does not imply asymptotic independence. The historical-priority comparison covers the specified inspected sources, not every possible permutation-moment formulation; implicit coverage in wider quadratic-assignment or rank-statistic literature is a residual risk.

## References

[1] Zhexiao Lin and Fang Han, *On boosting the power of Chatterjee's rank correlation*, arXiv:2108.06828 (first posted 2021-08-15), especially equation (2.4) and Sections 2–3. https://arxiv.org/html/2108.06828v1

[2] Qingyang Zhang, *On the asymptotic distribution of the symmetrized Chatterjee's correlation coefficient*, arXiv:2205.01769 (first posted 2022-05-03), especially Lemmas 1–3 and Section 4. https://arxiv.org/html/2205.01769v3

[3] Qingyang Zhang, *On extensions of Chatterjee–Spearman test*, arXiv:2406.16859 (2024). https://arxiv.org/abs/2406.16859
