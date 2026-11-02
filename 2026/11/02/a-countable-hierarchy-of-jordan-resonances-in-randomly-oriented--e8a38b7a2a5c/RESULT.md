# A countable hierarchy of Jordan resonances in randomly oriented Lüroth maps

## Finding
The independently switched standard and alternating Lüroth transformations admit **infinitely many distinct exceptional switching biases** at which the annealed polynomial transfer operator becomes defective. These biases form a strictly increasing sequence converging to \(3/4\). At each bias the defect is a genuine size-two Jordan block, detected by an exact cross-correlation of two adjacent monic shifted Legendre observables with a factor linear in lag.

For an odd integer \(d\ge1\), set
\[
\ell_j=\frac1{j(j-1)},\quad S_k=\sum_{j=2}^{\infty}\ell_j^k,\quad c_j=\frac1j+\frac{\ell_j}{2}-\frac12,\quad C_k=\sum_{j=2}^{\infty}\ell_j^k c_j.
\]
Define
\[
q_d=\frac{S_{d+2}}{S_{d+1}},\quad p_d=\frac{1+q_d}{2},\quad \lambda_d=S_{d+2},\quad B_d=(d+1)q_d C_{d+1}.
\]
Then \(B_d>0\), the eigenvalue \(\lambda_d\) has algebraic multiplicity two and geometric multiplicity one on the space of real polynomials of degree at most \(d+1\), and
\[
\frac12<p_1<p_3<p_5<\cdots<\frac34,\qquad
p_d=\frac34-\frac{3^{-(d+1)}}6+O(6^{-(d+1)}).
\]
Let \(P_m\) denote the ordinary Legendre polynomial, normalized by \(P_m(1)=1\), and put \(Q_m(x)=P_m(2x-1)/\binom{2m}{m}\), the monic shifted Legendre polynomial. Under stationary Lebesgue initialization and independent switching with probability \(p_d\), for each integer \(n\ge1\),
\[
\boxed{\displaystyle\mathbb E[Q_{d+1}(X_0)Q_d(X_n)]=
\frac{n B_d \lambda_d^{n-1}}{(2d+1)\binom{2d}{d}^2}>0.}
\]
These formulas are annealed, not quenched. In contrast, either deterministic transformation separately acts diagonally on its finite-dimensional polynomial generalized eigenspaces: every polynomial-restriction eigenvalue is simple.

## Assumptions and scope
Partition the unit interval, up to countably many endpoints, into \(I_j=[1/j,1/(j-1))\), \(j\ge2\). The **standard** Lüroth map has inverse branch
\[
 v_{+,j}(t)=\frac1j+\ell_j t,
\]
and the **alternating** Lüroth map has inverse branch
\[
 v_{-,j}(t)=\frac1j+\ell_j(1-t).
\]
Independently at each time select the standard map with probability \(p\in[0,1]\) or the alternating map with probability \(1-p\); write \(X_n\) for the resulting Markov trajectory with \(X_0\) uniformly distributed on \([0,1]\). All identities and the Jordan classification concern the annealed operator and the invariant subspaces of polynomials; no global spectrum or spectral-gap assertion is made. The branch boundaries have no effect on these Lebesgue-integral claims.

## Proof
**1. Exact polynomial action and stationarity.** Both transformations are full-branch, and every inverse branch has constant absolute derivative \(\ell_j\). As \(\sum_{j\ge2}\ell_j=1\), each map preserves Lebesgue measure. The annealed transfer operator (acting on functions against the future-coordinate observable) is
\[
(\mathcal P_p f)(t)=\sum_{j=2}^{\infty}\ell_j\{p f(v_{+,j}(t))+(1-p)f(v_{-,j}(t))\}.
\]
This is an exact norm-convergent expression for polynomials. Write \(y=t-1/2\); then \(v_{\pm,j}(t)-1/2=c_j\pm\ell_j y\). Consequently
\[
\mathcal P_p y^m=\sum_{j=2}^{\infty}\ell_j\{p(c_j+\ell_j y)^m+(1-p)(c_j-\ell_j y)^m\}.
\]
The degree at most \(m\) subspace is invariant. The leading coefficient equals \(S_{m+1}\) for even \(m\), and \((2p-1)S_{m+1}\) for odd \(m\). Explicitly the subleading coefficient is
\[
[y^{m-1}]\mathcal P_p y^m= m\big(p+(-1)^{m-1}(1-p)\big)\,C_m.
\]
Here the centered moment sum \(C_m=\sum_{j\ge2}\ell_j^m c_j\); this formula includes the weight \(\ell_j\) correctly, because the coefficient of \(y^{m-1}\) in each branch carries \(\ell_j^{m-1}\), and the outer inverse-Jacobian weight gives \(\ell_j^m\).

**2. The double eigenvalue and its nonzero connecting entry.** For \(m=d\) odd and \(m=d+1\) even, equality of the diagonal entries is exactly
\[
(2p-1)S_{d+1}=S_{d+2},\quad\text{hence}\quad p=p_d.
\]
At this parameter the entry taking \(y^{d+1}\) to degree \(d\) is \(B_d=(d+1)q_d C_{d+1}\). To show \(C_{d+1}>0\), note that the \(j=2\) summand equals \(2^{-(d+1)}/4\). On \(j\ge3\), \(|c_j|\le1/2\), \(\ell_j\le1/6\) and \(\sum_{j\ge3}\ell_j=1/2\). Thus the absolute value of all negative contributions is at most \((1/4)6^{-d}\), strictly below \((1/4)2^{-(d+1)}\) because \(3^d>2\). The other eigenvalues in degrees below \(d\) are larger than \(\lambda_d\), since \(S_k\) strictly decreases and \(q_d>0\). Therefore the double diagonal eigenvalue has one-dimensional eigenspace: on the quotient by degrees below \(d\), its matrix has the form \(\begin{psmallmatrix}\lambda_d&B_d\\0&\lambda_d\end{psmallmatrix}\). It gives a nontrivial size-two Jordan block. For degrees above \(d+1\), all diagonal entries are strictly smaller than \(\lambda_d\), so its algebraic multiplicity stays two in any higher polynomial restriction.

**3. The hierarchy and its boundary asymptotic.** The moment sequence \(S_k\) is strictly log-convex by strict Cauchy–Schwarz: \(S_{k+1}^2<S_k S_{k+2}\), because the branch lengths are not equal. Hence \(S_{k+1}/S_k\) increases strictly with \(k\). Dominance of the longest branch gives the limit \(1/2\), so \(p_d\uparrow3/4\). More quantitatively, for positive integers \(k\),
\[
S_k=2^{-k}(1+3^{-k}+O(6^{-k})),\quad
\frac{S_{k+1}}{S_k}=\frac12-\frac13 3^{-k}+O(6^{-k}).
\]
The tail bound follows from \(\sum_{j\ge4}\ell_j^k\le(1/12)^{k-1}\sum_{j\ge4}\ell_j\). Substitute \(k=d+1\) to obtain the stated asymptotic for \(p_d\). Strictly \(1/2< p_d<3/4\) because every \(S_{k+1}/S_k\) lies in \((0,1/2)\).

**4. Exact polynomial-prefactor correlation.** The leading coefficient of \(\mathcal P_{p_d}^n y^{d+1}\) is \(\lambda_d^n\). Since the two top diagonal entries both equal \(\lambda_d\), the degree-\(d\) coefficient satisfies a first-order Jordan recurrence, whose solution is \(n B_d\lambda_d^{n-1}\). The monic shifted Legendre polynomial \(Q_{d+1}\) has no degree-\(d\) coefficient in \(y\) because its parity is that of \(d+1\). Its iterated image therefore differs from \(\lambda_d^n Q_{d+1}+nB_d\lambda_d^{n-1}Q_d\) by a polynomial of degree at most \(d-1\). Orthogonality of shifted Legendre polynomials gives
\[
\int_0^1 Q_d(t)^2\,dt=\frac1{(2d+1)\binom{2d}{d}^{2}}.
\]
Finally, uniform stationarity and independent switching yield
\[
\mathbb E[Q_{d+1}(X_0)Q_d(X_n)] =\int_0^1 (\mathcal P_{p_d}^{n} Q_{d+1})(t)Q_d(t)\,dt,
\]
which proves the exact formula. At lag zero the cross-correlation vanishes by orthogonality.

**5. Deterministic comparison.** If \(p=1\), polynomial eigenvalues are \(S_{m+1}\), strictly decreasing with degree. If \(p=0\), they are \((-1)^m S_{m+1}\), pairwise distinct. Each deterministic polynomial restriction is therefore diagonalizable; defectiveness arises from switching.

## Verification
The standalone `verify.py` checks transfer polynomial coefficients using exact rational arithmetic for three finite-branch truncations, at three odd degrees and four lags (72 coefficient identities). This tests the algebra of the leading and adjacent coefficients, not the infinite-branch analytic theorem. Independently, high-precision convergent sums check the signs and ordering for the first eight odd degrees and print representative biases; these are numerical diagnostics only. The infinite-branch theorem is supported by the explicit analytic inequalities and operator calculation above. Run with `python verify.py` (requires the `mpmath` Python package for optional infinite-sum diagnostics).

## Relationship to prior work
Kalle and Maggioni introduce the random standard/alternating Lüroth family and analyze the expansion structure, invariant statistics, approximation quality and digit frequencies at the full-branch parameter; they supply the source dynamics but do not state the polynomial Jordan hierarchy or exact adjacent-degree correlations. Their earlier work develops invariant densities of random interval maps, including Lüroth maps with a hole, but does not state this spectral classification. Classical polynomial transfer calculations and finite-dimensional Jordan algebra are background tools and not separately claimed as novel. An earlier random skew-tent example exhibits a **single quadratic resonance**; it does not imply the present countable Lüroth hierarchy or its accumulation law because the branch moments and operator are different. The originality assertion is confined to the specific new classification and cross-correlation identities described here.

## Limitations
The conclusions are annealed and describe invariant finite-dimensional polynomial restrictions; no statement is made about global transfer-operator spectral isolation, quenched rates, or nonlinear observables beyond polynomial test functions. Exact proof holds for every positive odd degree, not just the finite degrees exercised by the checker. Algebraic equivalences in the broader generalized Lüroth or operator literature not located by the inspected searches remain a priority risk. No independent external mathematical audit has been performed.

## References
1. C. Kalle and M. Maggioni, *On Approximation by Random Lüroth Expansions*, arXiv:2101.01982v1, publicly posted 6 January 2021. Full text: https://arxiv.org/pdf/2101.01982.
2. C. Kalle and M. Maggioni, *Invariant Densities for Random Systems of the Interval*, arXiv:1805.11430, 2018 (revised 2020). Full text: https://arxiv.org/pdf/1805.11430.
3. Classical orthogonality of Legendre polynomials and Cauchy–Schwarz log-convexity for moment sequences (standard results).
