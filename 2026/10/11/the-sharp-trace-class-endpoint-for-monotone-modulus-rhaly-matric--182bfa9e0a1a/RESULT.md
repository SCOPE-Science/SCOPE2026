# The sharp trace-class endpoint for monotone-modulus Rhaly matrices

## Finding

Let \((\eta_n)_{n\geq0}\) be any complex sequence for which \(a_n=|\eta_n|\) is nonincreasing. On finitely supported vectors in \(\ell^2(\mathbb N_0)\), form the Rhaly (terraced) matrix
\[
(R_\eta x)_n=\eta_n\sum_{k=0}^{n}x_k.
\]
There exist universal constants \(0<c<C<\infty\), independent of the sequence, for which the trace norm, interpreted as \(+\infty\) when no trace-class extension exists, satisfies
\[
c\sum_{n=0}^{\infty}a_n\log(n+2)
\ \leq\ \|R_\eta\|_{\mathcal S_1}
\ \leq\ C\sum_{n=0}^{\infty}a_n\log(n+2).
\]
In particular, **the matrix has a trace-class extension if and only if the logarithmically weighted absolute coefficients are summable**. Equivalently, the sharp dyadic criterion is
\[
a_0+\sum_{j=0}^{\infty}(j+1)2^j a_{2^j}<\infty.
\]
For the natural critical family \(\eta_n=((n+1)[\log(e+n)]^r)^{-1}\) with \(r\geq0\), trace-class membership holds exactly when \(r>2\). By contrast, the established \(\mathcal S_q\) criterion for \(1<q<\infty\) gives \(r>1/q\); taking \(q\downarrow1\) would miss an entire logarithmic factor at the trace endpoint.

## Assumptions and scope

The underlying Hilbert space is complex \(\ell^2(\mathbb N_0)\) with its canonical basis. Each \(\eta_n\) may have an arbitrary phase, and the only regularity hypothesis is \(a_0\geq a_1\geq\cdots\geq0\). The matrix is initially defined on finite-support sequences, and existence of a trace-class extension means agreement of every matrix coefficient with a member of \(\mathcal S_1(\ell^2)\). No boundedness or compactness is presupposed. The norms and the dyadic series are allowed to be infinite in the equivalence. The result says nothing about general nonmonotone absolute values or trace ideals on other sequence spaces.

## Proof

**1. Universal triangular-block trace estimate.** Let \(L_N\) be the \(N\)-by-\(N\) lower triangular matrix whose entries are one at and below the diagonal. For every integer \(N\geq1\), the singular values, in decreasing order, are
\[
s_k(L_N)=\bigl[2\sin\bigl((2k-1)\pi/(4N+2)\bigr)\bigr]^{-1},\qquad1\leq k\leq N.
\]
Indeed, \(L_N^{-1}\) is the first-difference matrix. The positive matrix \((L_N^*L_N)^{-1}=L_N^{-1}(L_N^{-1})^*\) has diagonal \((1,2,\ldots,2)\), with minus one on the adjacent diagonals. Its eigenvectors have components \(\cos((m+\tfrac12)\theta_k)\), indexed by \(0\leq m<N\), where \(\theta_k=(2k-1)\pi/(2N+1)\). Its eigenvalues are \(4\sin^2(\theta_k/2)\), proving the singular-value formula. From \(2t/\pi\leq\sin t\leq t\) on \([0,\pi/2]\), there are absolute \(c_0,C_0>0\) with
\[
c_0N\log(N+1)\leq\|L_N\|_{\mathcal S_1}\leq C_0N\log(N+1),\qquad N\geq1.
\]

**2. Dyadic decomposition and sufficiency.** Set \(I_j=\{2^j,\ldots,2^{j+1}-1\}\), and let \(P_j\) project onto the coordinates in \(I_j\). The row-zero contribution is \(\eta_0e_0\otimes e_0\). For each \(j\geq0\), the rows in \(I_j\) have precisely two disjoint column contributions: the internal block \(P_jR_\eta P_j=D_jL_{2^j}\), where \(D_j\) is diagonal with entries \(\eta_n\) for \(n\in I_j\), and one rank-one rectangular block supported on earlier columns \(\{0,\ldots,2^j-1\}\). The ideal property and step 1 give
\[
\|D_jL_{2^j}\|_1\leq a_{2^j}\|L_{2^j}\|_1
\leq C_0(j+1)2^j a_{2^j}.
\]
The earlier-column rectangular block has trace norm exactly \(\sqrt{2^j}\,(\sum_{n\in I_j}a_n^2)^{1/2}\leq2^ja_{2^j}\). Hence \(R_\eta\) is a trace-norm convergent sum of these blocks whenever
\[
a_0+\sum_{j\geq0}(j+1)2^ja_{2^j}<\infty,
\]
and its trace norm is bounded above by a universal multiple of that quantity. Agreement on matrix coefficients proves the asserted extension.

**3. Necessity by trace-norm pinching.** Suppose \(R_\eta\) has a trace-class extension. Compressing onto \(\mathbb Ce_0\) gives \(\|R_\eta\|_1\geq a_0\). More generally, for every \(J\geq0\), the pinching map to pairwise orthogonal blocks is trace-norm contractive:
\[
\sum_{j=0}^{J}\|P_jR_\eta P_j\|_1\leq\|R_\eta\|_1.
\]
This follows directly from trace-class/operator-norm duality by choosing a block-diagonal norm-one polar-sign witness on each finite block. For \(n\in I_j\), monotonicity gives \(a_n\geq a_{2^{j+1}}\). If the latter is nonzero, \(\|D_j^{-1}\|\leq a_{2^{j+1}}^{-1}\); the same bound is trivial when it vanishes. Consequently,
\[
\|P_jR_\eta P_j\|_1
=\|D_jL_{2^j}\|_1
\geq a_{2^{j+1}}\|L_{2^j}\|_1
\geq c_0(j+1)2^j a_{2^{j+1}}.
\]
Summing, shifting \(l=j+1\), and using \(a_1\leq a_0\) yield
\[
\|R_\eta\|_1\geq c_1\left(a_0+\sum_{l\geq0}(l+1)2^l a_{2^l}\right)
\]
for an absolute constant \(c_1>0\). This simultaneously proves necessity and the lower quantitative norm bound.

**4. Convert to the logarithmic criterion.** For a nonincreasing nonnegative sequence, elementary weighted Cauchy condensation on the dyadic intervals gives
\[
\sum_{n\geq0}a_n\log(n+2)
\asymp a_0+\sum_{j\geq0}(j+1)2^ja_{2^j},
\]
with absolute constants: each dyadic interval has \(2^j\) terms, its logarithm is comparable with \(j+1\), and its terms lie between \(a_{2^j}\) and \(a_{2^{j+1}}\). Combining steps 2 and 3 proves the theorem. For the critical family, the resulting series is comparable to \(\sum_{n\geq2}1/[n(\log n)^{r-1}]\), which converges precisely for \(r>2\). The known \(q>1\) Besov/Schatten criterion reduces there to \(\sum_j(j+1)^{-rq}<\infty\), giving \(r>1/q\).

## Verification

The companion dependency-free `VERIFY.py` checks the difference-matrix inverse identity exactly for finite \(N\), the explicit tridiagonal Gram inverse, the cosine eigenvector equations and singular-value trace estimates numerically, and the dyadic block reconstruction by rational arithmetic. Run `python3 VERIFY.py` from the extracted package directory. The theorem itself is established by the infinite-dimensional argument in the preceding section; finite tests alone do not prove it.

## Relationship to prior work

Bellavita–Dellepiane–Stylogiannis (arXiv:2503.21930; later *J. London Math. Soc.* 112 (2025), e70304) explicitly characterize \(\mathcal S_q\) membership for \(1<q<\infty\), as their Theorem 1.3 and Theorem 5.8 state; the displayed proof uses \(\sum_{n\geq1}n^{-q}\), which diverges at \(q=1\). Their preprint's complete theorem and proof were compared, not merely its abstract. The 2026 paper by Galanopoulos–Girela treats boundedness and compactness and identifies the preceding range \(1<q<\infty\) as already established. The June 2026 weighted-Hardy/factorable-matrix preprint concerns related Schatten problems; its publicly available abstract and extended summary were examined, but its original full text could not be read. The new statement is the **missing \(\mathcal S_1\) endpoint under a natural monotonicity hypothesis**, with an additional logarithmic loss. It neither claims general nonmonotone \(\mathcal S_1\) classification nor recasts the existing \(q>1\) test as new.

## Limitations

The monotone-modulus hypothesis is essential to the present lower-bound argument; no general \(\mathcal S_1\) criterion for oscillatory sequences is asserted. The universal norm constants are not optimized. Comparison with the complete June 2026 weighted-Hardy preprint remains outstanding because authorized full-text retrieval was unsuccessful; an equivalent previously stated specialization therefore remains a bibliographic risk. No independent mathematical audit has been performed.

## References

1. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Schatten class for Rhaly matrices and spaces of analytic functions*, arXiv:2503.21930v1, first posted 27 March 2025; full preprint publicly readable at ResearchGate, `https://www.researchgate.net/publication/390322398_Schatten_class_for_Rhaly_matrices_and_spaces_of_analytics_functions`.
2. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, *Journal of the London Mathematical Society* 112 (2025), e70304, DOI `10.1112/jlms.70304`.
3. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875, first posted 14 June 2026.
4. P. Galanopoulos, D. Girela, *Rhaly Operators Acting on Hardy, Bergman, and Dirichlet Spaces*, *Journal of Geometric Analysis* 36 (2026), article 115, DOI `10.1007/s12220-026-02361-9`.
