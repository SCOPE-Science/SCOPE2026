# Finite Gram reduction of sharp Cesàro self-commutator bounds at every order

## Finding

For every integer \(m\ge1\), the optimal weighted lower coefficient of the generalized Cesàro self-commutator has an exact representation using only an \((m-1)\times(m-1)\) Hermitian Gram matrix. The reduction works for every real shift \(\alpha>-1\), including shifts at which the self-commutator is not positive.

For \(m\ge1\), \(\alpha>-1\), define
\[
 c_m(\alpha)=\sup\{c\in\mathbb R:\ M_{\alpha,m}^*M_{\alpha,m}-M_{\alpha,m}M_{\alpha,m}^*\succeq cM_{\alpha,m}^*R_{\alpha,m}M_{\alpha,m}\}.
\]
The value is \(-\infty\) when this set is empty. Define \(G\) and \(\Lambda\) precisely below. The exact answer is
\[
\boxed{c_m(\alpha)=\begin{cases}-\infty,&-1<\alpha<0,\\[3pt] 1+\min\{0,\lambda_{\min}(G^{1/2}\Lambda G^{1/2})\},&\alpha\ge0.\end{cases}}
\]
When \(m=1\), the matrix is empty and its contribution is defined as zero. This is a finite-dimensional spectral formula, not merely a sufficient lower bound. Every Gram entry is given by an absolutely convergent, explicit scalar series.

As an exact special case, when \(m=2\) and \(0<\alpha<1\),
\[
\boxed{c_2(\alpha)=1-3\alpha(1-\alpha^2)\frac{3\psi(\alpha+3)-2\psi(\alpha+5/2)-\psi(\alpha+4)}6.}
\]
Here \(\psi\) is the digamma function. At \(\alpha=1/2\),
\[
 c_2(1/2)=\frac{261}{560}+\frac34\log2=0.985931813991\ldots .
\]
The optimal bound at order two is not attained by any nonzero input for \(0<\alpha<1\). At \(\alpha=0\) and every \(\alpha\ge1\), the optimal coefficient at order two is \(1\), and the equality cases can be realized by finitely supported inputs.

## Assumptions and scope

Work on the complex Hilbert space \(\ell^2(\mathbb N_0)\). The rising factorial is \((z)_k=z(z+1)\cdots(z+k-1)\), with \((z)_0=1\). For a positive integer \(m\), put
\[
 (M_{\alpha,m})_{nj}=\begin{cases}\displaystyle\frac{m(n-j+1)_{m-1}}{(n+\alpha+1)_m},&0\le j\le n,\\ 0,&j>n,\end{cases}\qquad \alpha>-1.
\]
Let \(H_m(t)=(t+1)_m\), \(D_m(t)=(t+m+1)_m\), and
\[
 R_{\alpha,m}=\operatorname{diag}(r_n)_{n\ge0},\qquad r_n=1-\frac{H_m(n+\alpha)}{D_m(n+\alpha)}>0.
\]
These definitions and the boundedness of \(M_{\alpha,m}\) are as in Ma, Theorems 1.1 and 2.3 [1]. For \(0\le r<m\), define the explicit monic polynomial of degree \(d=m-r-1\):
\[
 p_{m,r}(n;\alpha)=\sum_{s=0}^{d}\binom{d}{s}
 \frac{(m+r+1)_s(r+1-\alpha)_s}{(2r+2)_s}
 (n+\alpha+1)_{d-s}.
\]
Set
\[
 v_r(n)=\frac{p_{m,r}(n;\alpha)}{D_m(n+\alpha)},\quad
 \lambda_r=(2r+1)\binom{m+r}{2r+1}^{\!2}
 \alpha\prod_{j=1}^{r}(\alpha^2-j^2).
\]
The finite matrix \(G\), indexed by \(1\le r,s<m\), and the diagonal matrix \(\Lambda\) are
\[
 G_{rs}=\sum_{n=0}^{\infty}\frac{v_r(n)v_s(n)}{r_n},
 \qquad \Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_{m-1}).
\]
All series converge absolutely because \(r_n=m^2/n+O(n^{-2})\) and \(v_r(n)=O(n^{-r-1})\) for \(r\ge1\). The polynomials have distinct degrees, so the Gram matrix is positive definite for \(m\ge2\). The matrix \(G^{1/2}\Lambda G^{1/2}\) is Hermitian even when the coefficients change sign. The expression \(\lambda_{\min}\) refers to its smallest real eigenvalue.

## Proof

**1. Exact operator reduction.** Ma's analytically proved defect decomposition [1, Theorem 2.3, Eqs. (2.15)–(2.18)] provides a bounded operator \(B\) satisfying \(BM_{\alpha,m}=M_{\alpha,m}^*\) and
\[
 M^*M-MM^*=M^*Q M,\qquad Q=R+\sum_{r=0}^{m-1}\lambda_r v_rv_r^*.
\]
The finite-support right inverse \(L\) in [1, Eqs. (2.1)–(2.2)] satisfies \(MLx=x\) for every finitely supported sequence \(x\). Consequently the sharp coefficient equals the infimum, over nonzero finitely supported \(x\), of
\[
 \frac{\langle Qx,x\rangle}{\langle Rx,x\rangle}.
\]
Indeed, \(M\) has dense range containing all finitely supported sequences, and each numerator and denominator is continuous on \(\ell^2\), while the denominator is strictly positive for nonzero \(x\).

**2. A divergent but removable rank-one term.** The same explicit polynomial formulas give
\[
 r_n=\frac{m^2}{n}+O(n^{-2}),\quad
 v_0(n)=\frac1n+O(n^{-2}),\quad
 \sum_{n\ge0}\frac{|v_0(n)|^2}{r_n}=\infty.
\]
For \(r\ge1\), the corresponding weighted sum is finite. Let \(\mathscr H_R\) denote the completion of finitely supported sequences in the weighted norm \(\|x\|_R^2=\sum r_n|x_n|^2\).

When \(\alpha>0\), \(\lambda_0=m^2\alpha>0\). The finite-support kernel of the functional \(f_0(x)=\langle x,v_0\rangle\) is dense in \(\mathscr H_R\): given finitely supported \(x\), select a disjoint finite tail \(J\) and set
\[
 z_n=-\frac{f_0(x)}{\sum_{j\in J}|v_0(j)|^2/r_j}\,
 \frac{v_0(n)}{r_n}\,\mathbf1_{J}(n).
\]
Then \(f_0(x+z)=0\) (all relevant vectors are real) and
\[
 \|z\|_R^2=\frac{|f_0(x)|^2}{\sum_{j\in J}|v_0(j)|^2/r_j}\longrightarrow0
\]
as the tail is enlarged. With complex \(x\), the same expression uses the fixed Hermitian inner-product convention and the conjugate coefficient as appropriate. The finite-rank quadratic form contributed by \(r\ge1\) is continuous in \(\mathscr H_R\), so minimizing \(\langle Qx,x\rangle/\|x\|_R^2\) on finitely supported vectors is equivalent to minimizing the form with the nonnegative \(r=0\) term deleted on \(\mathscr H_R\). If \(\alpha=0\), all \(\lambda_r=0\) and the optimal coefficient is \(1\).

When \(-1<\alpha<0\), \(\lambda_0<0\). Set \(x^{(N)}_n=\mathbf1_{\{n\le N\}}v_0(n)/r_n\) and \(h_N=\sum_{n\le N}|v_0(n)|^2/r_n\). Then \(h_N\to\infty\), \(\|x^{(N)}\|_R^2=h_N\), and the \(r=0\) correction divided by the denominator is \(\lambda_0h_N\to-\infty\). All other corrections divided by \(h_N\) remain bounded by weighted Cauchy–Schwarz and the convergent Gram diagonal entries. Hence the infimum is \(-\infty\).

**3. Gram matrix and spectrum.** For \(\alpha>0\), put \(b_r(n)=v_r(n)/\sqrt{r_n}\in\ell^2\), \(1\le r<m\). Under the unitary identification \(x\mapsto R^{1/2}x\) of \(\mathscr H_R\) with \(\ell^2\), the remaining quadratic form is the identity plus the finite-rank self-adjoint operator
\[
 T=\sum_{r=1}^{m-1}\lambda_r b_rb_r^*.
\]
The Gram matrix of \((b_r)_{r=1}^{m-1}\) is exactly \(G\). By the polar decomposition of the synthesis map from \(\mathbb C^{m-1}\) to \(\ell^2\), the restriction of \(T\) to their span is unitarily equivalent to \(G^{1/2}\Lambda G^{1/2}\). On its infinite-dimensional orthogonal complement \(T=0\). Thus the bottom of the spectrum of \(I+T\) is
\[
 1+\min\{0,\lambda_{\min}(G^{1/2}\Lambda G^{1/2})\}.
\]
The density argument in Step 2 proves this is the actual infimum of the original operator ratio, not merely a lower estimate. This includes every integer \(m\), all \(\alpha>0\), and the empty-matrix convention at \(m=1\).

**4. Explicit second order and equality.** For \(m=2\), the only Gram entry is
\[
 S(\alpha)=G_{11}=\sum_{n=0}^{\infty}
 \frac1{2(n+\alpha+3)(n+\alpha+4)(2n+2\alpha+5)}.
\]
Partial fractions yield
\[
 \frac1{2(t+3)(t+4)(2t+5)}=
 \frac1{3(t+5/2)}+\frac1{6(t+4)}-\frac1{2(t+3)}.
\]
Summing by the digamma recurrence gives
\[
 S(\alpha)=\frac{3\psi(\alpha+3)-2\psi(\alpha+5/2)-\psi(\alpha+4)}6.
\]
Here \(\lambda_1=3\alpha(\alpha^2-1)\), so for \(0<\alpha<1\) the only finite-rank eigenvalue is negative and the displayed sharp formula follows. For \(\alpha\ge1\) the only remaining coefficient is nonnegative, giving \(c_2(\alpha)=1\). At \(\alpha=1/2\), the standard half-integer digamma recurrence gives \(S(1/2)=299/630-(2/3)\log2\), and hence the stated elementary value.

For \(0<\alpha<1\), equality would require simultaneous annihilation of the positive \(v_0\)-term and equality in weighted Cauchy–Schwarz for \(v_1\). The latter forces \(x\) proportional to \(R^{-1}v_1\), whose coordinates are \(1/(4(n+\alpha)+10)>0\), but \(\langle R^{-1}v_1,v_0\rangle>0\). Thus no nonzero \(x=My\) can attain the optimal coefficient. At \(\alpha=0\) equality is automatic; for \(\alpha\ge1\), choosing a nonzero finitely supported \(x\) orthogonal to the relevant \(v_0,v_1\) vectors and putting \(y=Lx\) gives equality.

## Verification

The accompanying standalone standard-library script checks, in exact rational arithmetic, the full finite-column Gram identity \(I-B^*B=R+\sum_r\lambda_rv_rv_r^*\) for orders \(1\) through \(4\), five rational parameter values on both sides of zero, and all tested column pairs. It independently checks the finite-support right inverse \(ML=I\) on finitely many exact matrix entries. It also evaluates a long positive partial sum at \(m=2\), \(\alpha=1/2\), against the derived rational-plus-logarithm formula, with a conservative numerical tolerance.

These finite calculations check the normalization and arithmetic in the analytic reduction. They do **not** establish the general-order operator identity or replace the proof of density, the spectral reduction, or convergence of the infinite series. To run the included script after extraction: `python cesaro_defect_finite_gram_verifier.py`.

## Relationship to prior work

Yicen Ma [1] analytically proves the exact bounded-operator defect decomposition, a qualitative hyponormality criterion for every positive integer order, and a nonsharp universal quantitative constant of \(1/36\). Its Lemma 3.2 gives a weighted Cauchy–Schwarz **lower estimate** from the negative rank-one terms; it does not identify the actual infimum of the generalized Rayleigh quotient, give the cross-Gram spectral formula, or show why the positive but weighted-unbounded rank-one direction does not change that infimum. These specific additional arguments yield the sharp coefficient for all orders; the explicit digamma formula and nonattainment at second order are consequences. They do not claim a new proof of the original hyponormality theorem.

Rhaly [2] develops interrupter identities for the same second-order matrices and proves hyponormality on the parameter set \(\{0\}\cup[1,\infty)\); its conjectural intermediate regime is settled in [1]. The inspected Rhaly article does not supply this sharp parameter-dependent relative commutator coefficient. Related Cesàro and Mellin-operator results concern different quantities such as trace or essential spectra and do not imply the present weighted optimization.

## Limitations

The exact formula depends on the natural weight \(R_{\alpha,m}\) and the integer-order generalized Cesàro family, not arbitrary bounded operators or alternative weights. The Gram entries are generally absolutely convergent infinite series rather than elementary closed forms; the spectral problem is finite-dimensional, but numerical truncations alone give neither the exact answer nor all-order correctness. No independent audit or external validation has been performed. Novelty comparisons cannot exclude every unindexed equivalent formulation in the older operator-theory literature.

## References

1. Y. Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1, first publicly posted 2026-09-18; especially Theorem 2.3, Eqs. (2.13)–(2.18), Lemma 3.2, and Section 7. https://arxiv.org/html/2610.00193v1
2. H. C. Rhaly Jr., *Supraposinormality and hyponormality for the generalized Cesàro matrices of order two*, Operators and Matrices **12** (2018), 133–142, DOI:10.7153/oam-2018-12-08. https://files.ele-math.com/articles/oam-12-08.pdf
3. T. Le and H. C. Rhaly Jr., *Coposinormality of the Cesàro matrices*, Archiv der Mathematik **110** (2018), 167–173, DOI:10.1007/s00013-017-1128-y; cited for background in [1].
