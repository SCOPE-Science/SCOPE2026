# Sharp quasi-Schatten thresholds for polynomial Rhaly matrices and Cesàro shift defects

## Finding

Let \(\alpha>1\), and suppose complex coefficients \((\eta_n)_{n\ge0}\) obey two-sided polynomial bounds \(c(n+1)^{-\alpha}\le|\eta_n|\le C(n+1)^{-\alpha}\) for fixed \(0<c\le C<\infty\). The Rhaly (terraced) matrix \(R_\eta\), initially defined on finitely supported sequences by
\[
 (R_\eta x)_n=\eta_n\sum_{j=0}^n x_j,
\]
extends uniquely to a compact operator on \(\ell^2(\mathbb N_0)\) and has the sharp Schatten classification
\[
 \boxed{R_\eta\in\mathcal S_p\quad\Longleftrightarrow\quad p>1/\alpha\qquad(0<p<\infty).}
\]
In particular, if \(C\) is the ordinary Cesàro operator and \(S\) is the unilateral right shift, then **for every integer \(m\ge1\)** the shift-covariance defect \(D_m=S^{*m}CS^m-C\) satisfies
\[
 \boxed{D_m\in\mathcal S_p\quad\Longleftrightarrow\quad p>1/2.}
\]
The latter provides the sharp quasi-Schatten refinement of the classical Hilbert–Schmidt shift defect. The nonmembership includes the critical exponent \(p=1/2\).

## Assumptions and scope

The Hilbert space is complex \(H=\ell^2(\mathbb N_0)\) with standard basis \((e_n)_{n\ge0}\). The scalars \(c,C\) may depend on \(\eta\), but do not depend on the index. No monotonicity or constant phase is required; only the two-sided magnitude bounds above. The operator \(C\) is given by \((Cx)_n=(n+1)^{-1}\sum_{j=0}^n x_j\). The isometry \(S\) is defined by \(Se_n=e_{n+1}\). For \(p\in(0,1)\), \(\mathcal S_p\) denotes the Schatten quasi-ideal with \(\|T\|_p^p=\sum_{j\ge1}s_j(T)^p\); no norm triangle inequality is assumed. The assertion does not cover the borderline polynomial regime \(\alpha=1\), general coefficients with upper bounds but without lower bounds, or arbitrary finite sums of terraced matrices.

## Proof

**1. A uniform triangular-block singular-value estimate.** Denote by \(V_N\) the lower triangular \(N\times N\) matrix with all entries on and below its diagonal equal to one. Its inverse \(V_N^{-1}=I-L_N\), where \(L_N\) is the strict one-step lower shift, satisfies \(\|V_N^{-1}\|\le2\). Thus
\[
 s_N(V_N)\ge1/2,\qquad s_1(V_N)\le N.
\]
For each \(2\le j\le N\), divide \(\{1,\ldots,N\}\) into \(j\) contiguous intervals with lengths at most \(\lceil N/j\rceil\). On each row interval retain entries in strictly earlier column intervals. The resulting matrix has rank at most \(j-1\). Its difference from \(V_N\) is a block-diagonal sum of lower triangular all-one matrices of order at most \(\lceil N/j\rceil\), hence has operator norm at most that quantity. The singular-value approximation principle gives
\[
 s_j(V_N)\le \lceil N/j\rceil\le 2N/j\qquad(2\le j\le N).
\]
Consequently for every fixed \(0<p<1\) a constant \(K_p<\infty\) exists such that
\[
 \|V_N\|_p^p\le N^p+(2N)^p\sum_{j=2}^N j^{-p}\le K_p N
 \quad\text{for all }N\ge1.
\]
At \(p=1\), the analogous estimate is \(\|V_N\|_1\le K N(1+\log N)\) with a universal \(K\).

**2. Dyadic row decomposition and the upper inclusion.** Introduce pairwise disjoint row intervals \(I_k=\{2^k,\ldots,2^{k+1}-1\}\) for \(k\ge0\), and isolate row zero. Write \(N=2^k\) and let \(P_k\) project onto \(I_k\). The operator \(P_kR_\eta\) is a sum \(B_k+T_k\), where \(B_k\) is the rank-one rectangle of entries \(\eta_n\) in rows \(n\in I_k\) and columns \(0\le j<N\), and \(T_k\) is the square internal block \(\operatorname{diag}(\eta_n:n\in I_k)V_N\). Both are regarded as operators on \(H\), supported on the indicated rows and columns. Since \(|\eta_n|\le C N^{-\alpha}\) on \(I_k\),
\[
 \|B_k\|_p^p=\|B_k\|^p\le C^pN^{p(1-\alpha)},
 \quad
 \|T_k\|_p^p\le C^pK_pN^{1-\alpha p}
\]
for \(0<p<1\). Because \(p\le1\), \(p(1-\alpha)\le1-\alpha p\). Hence \(\|P_kR_\eta\|_p^p\le C'_p2^{k(1-\alpha p)}\), using the standard \(p\)-subadditivity of Schatten quasi-norm powers. This series is summable exactly when \(\alpha p>1\). Including the rank-one row zero, the corresponding operator series converges in the complete quasi-Banach ideal \(\mathcal S_p\) and agrees coefficientwise with the original terraced matrix.

For \(p=1\), the triangular bound above and \(\|B_k\|_1\le C N^{1-\alpha}\) give \(\|P_kR_\eta\|_1\le C'2^{k(1-\alpha)}(1+k)\). It is summable since \(\alpha>1\). Thus \(R_\eta\in\mathcal S_1\subseteq\mathcal S_p\) for every \(p\ge1\). In particular, the constructed extension is compact and unique.

**3. Sharp lower obstruction from compressions.** On the same \(N\times N\) block, \(P_kR_\eta P_k=\operatorname{diag}(\eta_n:n\in I_k)V_N\). By the lower coefficient bound and step 1,
\[
 s_N(P_kR_\eta P_k)\ge \bigl(c(2N)^{-\alpha}\bigr)/2
 =c\,2^{-\alpha-1}N^{-\alpha}.
\]
Therefore all \(N\) singular values of this compression are at least that amount, and for any \(p>0\),
\[
 \|P_kR_\eta P_k\|_p^p\ge
 c^p2^{-p(\alpha+1)}N^{1-\alpha p}.
\]
If \(R_\eta\in\mathcal S_p\), then \(\|P_kR_\eta P_k\|_p\to0\) as \(k\to\infty\). Indeed, finite-rank operators are dense in \(\mathcal S_p\), both orthogonal projections tend strongly to zero, and the Schatten \(p\)-quasi-ideal property controls the finite-rank approximation error. For \(\alpha p\le1\), however, the displayed lower bound fails to tend to zero (and grows when \(\alpha p<1\)), giving the contradiction. This proves sharpness, including the excluded endpoint.

**4. The Cesàro shift-covariance specialization.** The matrix coefficients of \(S^{*m}CS^m\), indexed from zero, equal \(1/(i+m+1)\) when \(j\le i\), and vanish otherwise. Thus
\[
 (D_m)_{ij}=-\frac{m}{(i+1)(i+m+1)}\,\mathbf1_{\{j\le i\}}.
\]
For every \(m\ge1\) and \(i\ge0\),
\[
 \frac{m}{m+1}(i+1)^{-2}\le
 \frac{m}{(i+1)(i+m+1)}\le m(i+1)^{-2}.
\]
Apply the already proved classification with \(\alpha=2\). No claim is made that the shift defect is a self-commutator: \(S^{*m}CS^m-C\) and \(C^*C-CC^*\) are distinct operators with different spectral behavior.

## Verification

Run `python3 VERIFY.py` in this extracted package directory (Python standard library only). It checks exact integer inversion of the triangular matrices, the finite-rank interval decomposition, and the exact rational coefficients and polynomial bounds of the Cesàro defects. The included script prints a count of checks and exits unsuccessfully if any identity fails. The infinite Schatten classifications are justified by the analytic estimates above, not inferred from finite tests.

## Relationship to prior work

Sang's 2026 treatment of the Cesàro operator in the Toeplitz algebra recounts Barría–Halmos's Hilbert–Schmidt result for \(S^*CS-C\), and gives its matrix diagonal, but does not state a sharp quasi-Schatten threshold. Bellavita, Dellepiane, and Stylogiannis (2025) characterize general Rhaly \(\mathcal S_q\) membership for \(1<q<\infty\), and explicitly identify the absence of a complete criterion for \(0<q\le1\) as an open question (final Section 7). The present theorem settles a natural polynomial-decay class, including phase-oscillating coefficients, in that quasi-ideal range and supplies the sharp Cesàro covariance application. It does not solve the full open question for arbitrary Rhaly weights. Published work on the Cesàro **self-commutator** establishes a cubic Schatten eigenvalue threshold, but its operator is not the shift-covariance defect treated here.

## Limitations

The two-sided polynomial coefficient hypothesis is essential to the necessity proof; no characterization for arbitrary irregular Rhaly sequences is asserted. The proof gives exact membership thresholds, not sharp constants or a limit for individual singular values. Bibliographic priority is not fully settled: the full June 2026 manuscript on Rhaly operators on weighted Hardy spaces was unavailable through the attempted authorized sources, and older asymptotic Toeplitz literature might contain an equivalent reformulation. There is no independent mathematical audit.

## References

1. C. Bellavita, E. Dellepiane, and G. Stylogiannis, *Schatten class for Rhaly matrices and spaces of analytics functions* (2025), arXiv:2503.21930v1, first public 2025-03-27, https://arxiv.org/abs/2503.21930. Specifically Theorems 5.5, 5.7–5.8 and concluding open questions.
2. Y. Sang, *The Cesàro Operator is in the Toeplitz Algebra* (2026), arXiv:2608.25740v1, first public 2026-08-26, https://arxiv.org/abs/2608.25740. See Introduction for the 1982 Hilbert–Schmidt result.
3. J. Barría and P. R. Halmos, *Asymptotic Toeplitz operators*, Transactions of the American Mathematical Society 273 (1982), 621–630, DOI:10.1090/S0002-9947-1982-0667164-X.
4. C. Bellavita, E. Dellepiane, and G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices* (2026), arXiv:2606.15875; bibliographic overlap risk, full manuscript not inspected.
5. *The sharp trace-class endpoint for monotone-modulus Rhaly matrices* (2026), published mathematical result, identifier `2026/10/11/SCOPE-the-sharp-trace-class-endpoint-for-monotone-modulus-rhaly-matric--182bfa9e0a1a`; covers \(\mathcal S_1\), not quasi-Schatten \(p<1\).
6. *Cubic spectral decay of the classical Cesàro self-commutator* (2026), published mathematical result, identifier `2026/10/11/SCOPE-cubic-spectral-decay-of-the-classical-ces-ro-self-commutator--1d9ae52b1d38`; concerns \(C^*C-CC^*\), not \(S^*CS-C\).
