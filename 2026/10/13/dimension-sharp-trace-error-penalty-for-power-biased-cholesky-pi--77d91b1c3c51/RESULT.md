# Dimension-sharp trace-error penalty for power-biased Cholesky pivoting

## Finding

**One-pivot theorem.** Let \(n\ge2\), let \(A\in\mathbb R^{n\times n}\) be symmetric positive semidefinite with strictly positive diagonal and rank at least two, and fix any real \(q>1\). At the first pivot, select index \(j\) with probability proportional to \(d_j^q\), where \(d_j=A_{jj}\), and form the exact pivoted-Cholesky/Nyström residual
\[
R_j=A-\frac{Ae_je_j^{\mathsf T}A}{d_j}.
\]
Write \(\mathcal E_q(A)=\mathbb E\operatorname{tr}R_j\), with \(\mathcal E_1(A)\) denoting the original diagonal-proportional pivot rule. Then
\[
0<\frac{\mathcal E_q(A)}{\mathcal E_1(A)}\le n^{1-1/q}.
\]
The *exponent* of the dimension in this universal upper bound is optimal, already among rank-two matrices. Indeed, for every integer \(m\ge1\) and \(t>0\), set
\[
A_{m,t}=\operatorname{diag}\!\left(t,\mathbf1_m\mathbf1_m^{\mathsf T}\right).
\]
This matrix has dimension \(n=m+1\), rank two, and positive diagonal. Its exact one-pivot risks and their ratio are
\[
\mathcal E_1(A_{m,t})=\frac{2mt}{t+m},\qquad
\mathcal E_q(A_{m,t})=\frac{m(t^q+t)}{t^q+m},
\]
\[
\frac{\mathcal E_q(A_{m,t})}{\mathcal E_1(A_{m,t})}
=\frac{(t+m)(t^{q-1}+1)}{2(t^q+m)}.
\]
In particular, \(\mathcal E_q>\mathcal E_1\) **if and only if** \(1<t<m\), and equality occurs at \(t=1\) or \(t=m\). For each fixed \(q>1\), choose \(t=((q-1)m)^{1/q}\). Then
\[
\lim_{m\to\infty}\frac{\mathcal E_q(A_{m,t})/\mathcal E_1(A_{m,t})}
{m^{1-1/q}}
=\frac{(q-1)^{(q-1)/q}}{2q}>0.
\]
Consequently, no dimension-independent one-pivot trace-error comparison with the original rule holds for any fixed exponent \(q>1\). The same optimal dimension exponent is obtainable with strictly positive-definite matrices by arbitrarily small diagonal perturbations of these examples.

**Exact squared-diagonal two-block extremum.** Fix \(n\ge2\). Among all rank-two orthogonal equal-entry block matrices
\[
A=\operatorname{diag}(a\mathbf1_r\mathbf1_r^{\mathsf T},
 b\mathbf1_s\mathbf1_s^{\mathsf T}),\qquad
r,s\ge1,\quad r+s=n,\quad a,b>0,
\]
the largest possible \(\mathcal E_2(A)/\mathcal E_1(A)\) equals
\[
\boxed{\frac12+\frac{n}{4\sqrt{n-1}}}.
\]
It is attained when one block is a singleton and the ratio of its diagonal entry to that in the other block equals \(\sqrt{n-1}\), up to relabeling the blocks. This extremum is asserted **only within the displayed two-block class**; the universal full-matrix upper bound above has not been claimed sharp in constant.

For example, with \(n=17\) and \(A=\operatorname{diag}(4,\mathbf1_{16}\mathbf1_{16}^{\mathsf T})\), one has
\[
\mathcal E_1(A)=\frac{32}{5},\qquad
\mathcal E_2(A)=10,\qquad
\frac{\mathcal E_2(A)}{\mathcal E_1(A)}=\frac{25}{16}.
\]

## Assumptions and scope

The algorithm evaluates the diagonal and one pivot column of a finite real positive-semidefinite matrix, uses exact arithmetic, and performs exactly one rank-one update. Its selection probabilities are \(d_j^q/\sum_i d_i^q\). Strict positivity of every \(d_j\) makes the pivot update well-defined. Rank at least two ensures \(\mathcal E_1(A)>0\) so the risk ratio is meaningful. The first theorem holds for every real exponent \(q>1\), not only integer exponents. The trace of the positive-semidefinite residual is the nuclear-norm approximation error.

## Proof

**1. Nonnegative pivot risks and change of sampling measure.** Every positive-semidefinite matrix admits a Gram factorization \(A=VV^{\mathsf T}\). For any pivot with \(d_j>0\), define the unit vector \(u_j=V^{\mathsf T}e_j/\sqrt{d_j}\). Then
\[
R_j=V(I-u_ju_j^{\mathsf T})V^{\mathsf T}\succeq0.
\]
Since \(\operatorname{rank}A\ge2\), the residual has rank \(\operatorname{rank}A-1\ge1\), so \(r_j=\operatorname{tr}R_j>0\). Set \(T=\sum_i d_i\) and \(Q=\sum_i d_i^q\). The definition of the two pivot laws gives
\[
\mathcal E_q(A)=\frac{\sum_i d_i^qr_i}{Q}
\le\frac{(\max_i d_i)^{q-1}}{Q}\sum_i d_ir_i
=\frac{T(\max_i d_i)^{q-1}}{Q}\mathcal E_1(A).
\]
Hölder's inequality and \(\max_i d_i^q\le Q\) give
\[
T\le n^{1-1/q}Q^{1/q},\qquad
(\max_i d_i)^{q-1}\le Q^{(q-1)/q}.
\]
Their product proves the universal comparison. No eigenvalue or leverage-score assumption is needed.

**2. Exact rank-two risk.** In \(A_{m,t}\), pivoting the singleton removes its rank-one block and leaves a residual of trace \(m\); pivoting any of the \(m\) identical block coordinates removes the entire block and leaves trace \(t\). The probabilities of these two events are \(t^q/(t^q+m)\) and \(m/(t^q+m)\), respectively. Their expectation gives the asserted \(\mathcal E_q\); substituting \(q=1\) gives \(\mathcal E_1\). Subtracting one from the ratio yields the exact identity
\[
\frac{\mathcal E_q(A_{m,t})}{\mathcal E_1(A_{m,t})}-1
=\frac{(m-t)(t^{q-1}-1)}{2(t^q+m)}.
\]
For \(q>1\) this proves all strict and equality cases. At \(t=((q-1)m)^{1/q}\), divide the explicit ratio by \(m^{1-1/q}\) and pass to the limit, obtaining the strictly positive constant in the theorem. Together with Step 1 this proves optimality of the exponent \(1-1/q\).

**3. Sharp squared-diagonal extremum within the two-block class.** For the two orthogonal equal-entry blocks of respective sizes \(r,s\), scale \(b=1\) without affecting the ratio and put \(t=a/b\). The two pivot choices leave traces \(s\) and \(rt\), hence direct averaging yields
\[
\frac{\mathcal E_2(A)}{\mathcal E_1(A)}
=\frac{(rt+s)(t+1)}{2(rt^2+s)}=:F_{r,s}(t).
\]
Its derivative is
\[
F'_{r,s}(t)=\frac{(r+s)(s-rt^2)}{2(rt^2+s)^2}.
\]
Thus the unique maximum for fixed \(r,s\) occurs at \(t=\sqrt{s/r}\) and equals
\[
\frac{(\sqrt r+\sqrt s)^2}{4\sqrt{rs}}
=\frac12+\frac{n}{4\sqrt{rs}}.
\]
Because \(rs\ge n-1\) for positive integers with \(r+s=n\), the displayed global maximum over the two-block class is attained by \(\{r,s\}=\{1,n-1\}\), proving the formula and the exact integer example.

**4. Positive-definite approximation.** For any fixed \(m,t,q\), replace \(A_{m,t}\) by \(A_{m,t}+\delta I\), \(\delta>0\). Its diagonal stays positive and its one-pivot trace risks depend continuously on \(\delta\) near zero. Since the denominator \(\mathcal E_1(A_{m,t})\) is nonzero, the ratio converges to that of the rank-two matrix as \(\delta\downarrow0\). Choosing a sufficiently small positive \(\delta\) separately for each increasing \(m\) preserves a positive fixed fraction of the limiting dimension-power gap. Therefore the lower exponent remains optimal in the positive-definite class.

## Verification

Run `python3 verify.py` alongside this document; it requires only the Python standard library. It uses exact fractions to compare direct Schur-complement residuals with the rank-two closed forms, to test the universal bound for integer exponents on seeded Gram matrices, and to evaluate the \(17\)-dimensional witness and a positive-definite perturbation. The packaged run produced `PASS 2137 exact-rational checks`. Finite computation checks the examples and algebraic implementation; the proof above, not enumeration, establishes the all-dimension and real-exponent assertions.

## Relationship to prior work

Chen, Epperly, Tropp, and Webber (arXiv:2207.06503, first posted 2022-07-13) introduce and analyze RPCholesky, including the diagonal-proportional rule and a family of Gibbs/power pivot laws (Section 2.3.4). Their Section 5 and Appendix C give near-optimality and comparisons with uniform and greedy pivoting. The known \(q=1\) expectation identity and the algorithm itself are not claimed as new.

Steinerberger (arXiv:2404.11487, first posted 2024-04-17) proves a Frobenius-norm contraction for the \(q=2\) pivot rule and reports empirical examples where squared-diagonal sampling produces slightly larger trace error than \(q=1\) (Section 2.3 and Table 1). That qualitative possibility is not claimed as new either. The quantitative theorem here instead proves, for *every fixed finite* \(q>1\), a dimension-sharp growth exponent for the one-pivot trace-error ratio, with exact two-block boundaries and an explicit squared-diagonal extremum. The source results about a different objective or the limiting greedy law do not, without an additional argument, give these finite-exponent one-pivot comparisons.

## Limitations

The result compares expected trace error **after one pivot**; it makes no assertion about later adaptive pivots, complete factorization complexity, iteration-to-tolerance behavior, high-probability error, or error in the Frobenius norm. The universal constant \(1\) in the upper bound is not asserted to be optimal, nor is the two-block extremum asserted to be the global optimum among all positive-semidefinite matrices. The examples are exact rank-two positive-semidefinite matrices, with positive-definite versions furnished by a limiting perturbation argument. Literature priority outside the inspected sources is not independently certified.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, first public posting 2022-07-13; https://arxiv.org/abs/2207.06503; published in *Communications on Pure and Applied Mathematics*, DOI:10.1002/cpa.22234.
2. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487, first public posting 2024-04-17; https://arxiv.org/abs/2404.11487.
3. Mathematics Subject Classification 2020, 65F55, numerical methods for low-rank matrix approximation and matrix compression; https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=65F55.
