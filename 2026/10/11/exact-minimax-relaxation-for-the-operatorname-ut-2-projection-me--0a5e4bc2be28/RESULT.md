# Exact minimax relaxation for the \(\operatorname{UT}_2\) projection mean
## Finding
Let \(A_1,\ldots,A_m\in\operatorname{UT}_2\) have positive weights \(\omega_1,\ldots,\omega_m\) summing to \(1\), and let \(G\) be their Karcher mean. In Huang's normalization, let \(c_0\ge 1\) denote the coefficient controlling the off-diagonal projection-mean recurrence. For a relaxation denominator \(c>c_0/2\), let \((X_k)\) be the corresponding projection-mean iteration and define
\[
R_c(X_0)=\limsup_{k\to\infty}\|X_k-G\|_1^{1/k}.
\]
Then the exact worst-case asymptotic rate over nonstationary initial data is
\[
\sup_{X_0\in\operatorname{UT}_2,\,X_0\ne G}R_c(X_0)
=
\max\left\{\left|1-\frac1c\right|,\left|1-\frac{c_0}{c}\right|\right\}.
\]
Consequently, the unique minimax-optimal relaxation denominator is
\[
c_* = \frac{1+c_0}{2},
\]
and the corresponding exact worst-case rate is
\[
R_* = \frac{c_0-1}{c_0+1}.
\]
Thus the globally rate-optimal choice balances the diagonal mode and the off-diagonal mode rather than choosing the one-step fixed-diagonal value \(c=c_0\).

## Assumptions and scope
Here \(\operatorname{UT}_2\) is the Lie group of real upper-triangular \(2\times2\) matrices with positive diagonal entries. The matrix norm is the matrix \(1\)-norm used in the source's convergence discussion; the exponential root rate is unchanged under any equivalent norm in this finite-dimensional space.

The coefficient \(c_0\) is the positive scalar defined from the normalized diagonal data in Huang's formula. The source proves \(c_0\ge1\). The iteration is considered only in the convergent regime \(c>c_0/2\). No claim is made about transient error constants, finite-step optimality, higher-dimensional triangular groups, or data-dependent choices of \(c\) that vary with the iteration index.

## Proof
Put
\[
r=1-\frac1c,
\qquad
\lambda=1-\frac{c_0}{c}.
\]
Huang's arbitrary-initial-point analysis gives the asymptotic upper bound
\[
R_c(X_0)\le \max\{|r|,|\lambda|\}
\]
for every initial point whenever \(c>c_0/2\). It remains to prove that both factors are individually unavoidable.

First consider an initial point having the Karcher mean's diagonal. In the source normalization the only free coordinate is the upper-right entry \(t_k\), and the projection update has the affine recurrence
\[
t_{k+1}=t_k+\frac{b-c_0t_k}{c},
\]
where the fixed point is \(t_*=b/c_0\). Hence
\[
t_{k+1}-t_*=
\left(1-\frac{c_0}{c}\right)(t_k-t_*)
=\lambda(t_k-t_*).
\]
For every nonfixed choice \(t_0\ne t_*\), the matrix error is supported in one off-diagonal coordinate and therefore
\[
R_c(X_0)=|\lambda|.
\]
This proves that the second factor in the upper bound is sharp.

For the diagonal mode, use Huang's normalized diagonal formula. If a normalized diagonal coordinate starts at \(p_0>0\), then
\[
p_k=p_0^{r^k}.
\]
Choose \(p_0\ne1\). When \(r\ne0\),
\[
p_k-1
=
\exp\!\big((\log p_0)r^k\big)-1
=
(\log p_0)r^k+O(r^{2k}).
\]
A nonzero diagonal entry of \(X_k-G\) therefore has exponential root rate \(|r|\), so
\[
R_c(X_0)\ge |r|.
\]
If \(r=0\), then \(c=1\); unless \(c_0=1\), the fixed-diagonal family already supplies the nonzero worst factor \(|\lambda|\). When \(c_0=c=1\), Huang's upper bound is \(0\), so the exact worst-case rate is \(0\). Combining these cases with the universal upper bound gives
\[
\sup_{X_0\ne G}R_c(X_0)=\max\{|r|,|\lambda|\}.
\]

It remains to optimize over \(c\). Write \(s=1/c\); the admissible interval is \(0<s<2/c_0\), and the objective becomes
\[
F(s)=\max\{|1-s|,|1-c_0s|\}.
\]
Because \(c_0\ge1\), the unique equioscillation point is
\[
s_* = \frac{2}{1+c_0}.
\]
For \(s\le s_*\), one has \(F(s)\ge 1-s\ge1-s_*\). For \(s\ge s_*\), one has \(s\ge1/c_0\) and hence \(F(s)\ge c_0s-1\ge c_0s_*-1\). The two endpoint expressions coincide at \(s_*\), both equal to \((c_0-1)/(c_0+1)\). Therefore \(s_*\) is the unique minimizer, giving
\[
c_* = \frac{1+c_0}{2},
\qquad
R_* = \frac{c_0-1}{c_0+1}.
\]

## Verification
The proof uses the exact fixed-diagonal affine recurrence and the exact normalized diagonal formula from the primary source, together with the source's arbitrary-initial asymptotic upper bound. The lower bounds are supplied by explicit initial-data families, so no finite sampling is used to infer worst-case sharpness.

The edge cases \(c=1\), \(c=c_0\), and \(c_0=1\) were checked separately. In the admissible regime \(c>c_0/2\), both \(|1-1/c|\) and \(|1-c_0/c|\) are strictly below \(1\). The scalar minimax step was also checked directly by the two one-sided inequalities around \(s_*=2/(1+c_0)\), so no differentiability assumption at the maximum's kink is needed.

## Relationship to prior work
Huang derives the closed-form Karcher mean on \(\operatorname{UT}_2\), proves the sharp fixed-diagonal convergence threshold \(c>c_0/2\), and proves a sufficient convergence theorem for arbitrary initial points. His arbitrary-initial theorem gives the two-mode upper rate bound
\[
\max\left\{\left|1-\frac1c\right|,\left|1-\frac{c_0}{c}\right|\right\},
\]
but the inspected text does not identify this bound as the exact worst-case rate over initial data and does not optimize it over \(c\).

The preceding work of Huang and Lawson on Karcher means for upper-triangular Lie groups establishes existence, uniqueness, analyticity, and recursive formulas in arbitrary dimension. Its accessible abstract concerns computation of the mean itself rather than the sharp tuning of the projection-mean relaxation parameter.

The present result closes the natural tuning question in dimension two: the two factors in Huang's upper bound are realized by distinct explicit modes, which turns the estimate into an exact minimax objective and yields a unique rate-optimal parameter.

## Limitations
The theorem is specific to the \(2\times2\) triangular setting and to a constant relaxation denominator. It does not assert optimal transient behavior, monotonicity of the error at every step, or an analogous formula for \(\operatorname{UT}_n\) when \(n>2\). The originality assessment is literature-based; a short equivalent minimax corollary could exist under generic relaxation or stationary-iteration terminology even though targeted searches did not locate one.

## References
1. Huajun Huang, *The Karcher Mean on \(2\times2\) Triangular Matrices with Positive Diagonal Entries*, arXiv:2609.37018v1, first public 2026-09-29. Primary MSC 47A64.
2. Huajun Huang and Jimmie Lawson, *The Karcher Mean on Lie Groups of Upper Triangular Matrices*, arXiv:2609.34267v1, first public 2026-09-28.
