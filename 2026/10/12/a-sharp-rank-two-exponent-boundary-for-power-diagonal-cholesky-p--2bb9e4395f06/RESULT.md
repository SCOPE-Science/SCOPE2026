# A sharp rank-two exponent boundary for power-diagonal Cholesky pivoting

## Finding

Let \(n\ge2\), let \(A\in\mathbb R^{n\times n}\) be symmetric positive semidefinite with every diagonal element \(d_i=A_{ii}>0\), and let \(a_i=Ae_i\). For a fixed real exponent \(\beta\ge0\), choose one pivot with probability
\[
 p_i=\frac{d_i^{\beta}}{\sum_{j=1}^n d_j^{\beta}},\qquad
 B_i=A-\frac{a_i a_i^{\mathsf T}}{d_i}.
\]
Here \(J_m\) denotes the \(m\times m\) all-ones matrix, and \(\|\cdot\|_F\) denotes Frobenius norm.

**One-step power-pivot theorem.** For every such \(A\), if \(0\le\beta\le2\), then
\[
 \mathbb E\|B_i\|_F^2\le\left(1-\frac1n\right)\|A\|_F^2.
\]
The dimension-dependent constant is sharp, with equality for every positive scalar identity matrix. In the rank-two block family
\[
 A_{m,t}=\operatorname{diag}(t,J_m),\qquad m\in\{2,3,\ldots\},\ t>0,\ n=m+1,
\]
the same contraction holds for *every* \(0\le\beta\le4\). This endpoint is exact for that family: for every fixed \(\beta>4\), some \(m,t\) violate the inequality strictly. Continuity makes the strict failure persist on a positive-definite perturbation of the chosen matrix.

The rank-two family supplies an explicit finite witness: for \(\beta=5\), \(m=100\), \(t=8\),
\[
 \mathbb E\|B_i\|_F^2=\frac{9102400}{913}
 >\frac{1006400}{101}
 =\left(1-\frac1{101}\right)\|A_{100,8}\|_F^2,
\]
with exact surplus \(499200/92213\).

## Assumptions and scope

All statements concern precisely **one** exact-arithmetic positive-semidefinite Cholesky rank-one downdate with replacement-free one-step pivot probabilities, not a multi-pivot convergence guarantee. The power exponent \(\beta\) is fixed and nonnegative. Strictly positive diagonal entries make all probabilities and denominators well defined, including for singular matrices such as \(A_{m,t}\). A strict failure of an inequality at a singular matrix persists for sufficiently small positive diagonal perturbations, but the sharp positive-direction statement on the block family is proved only for the stated singular family. Matrix order, not an eigenvector orientation convention, specifies the clusters.

## Proof

**General safe interval.** Set \(r_i=(A^2)_{ii}=\|a_i\|_2^2\) and \(S=\sum_i r_i=\|A\|_F^2>0\). Expanding the rank-one downdate,
\[
 S-\|B_i\|_F^2=
 \frac{2(A^3)_{ii}}{d_i}-\frac{r_i^2}{d_i^2}
 \ge\frac{r_i^2}{d_i^2}.
\]
The inequality is the elementary spectral Cauchy–Schwarz statement \(d_i(A^3)_{ii}\ge r_i^2\), obtained by applying Cauchy–Schwarz to the eigenvalue powers of \(A\) at coordinate \(i\). Consequently,
\[
 S-\mathbb E\|B_i\|_F^2
 \ge\frac{\sum_i d_i^{\beta-2}r_i^2}{\sum_i d_i^{\beta}}
 \ge\frac{S^2}{(\sum_i d_i^{2-\beta})(\sum_i d_i^{\beta})}.
\]
The last step is Cauchy–Schwarz. For \(0\le\beta\le2\), put \(u=\beta/2\in[0,1]\). Weighted arithmetic–geometric mean gives, for any \(i,j\),
\[
 d_i^{\beta}d_j^{2-\beta}=(d_i^2)^u(d_j^2)^{1-u}
 \le u d_i^2+(1-u)d_j^2.
\]
Summing over both indices yields
\[
 (\sum_i d_i^{\beta})(\sum_i d_i^{2-\beta})
 \le n\sum_i d_i^2\le nS,
\]
where the final inequality is the elementary fact that squared diagonal entries form a subsum of \(\|A\|_F^2\). Combining displays proves the claimed contraction. For \(A=cI_n\), each pivot removes exactly one diagonal square and equality holds, proving sharpness.

**Cluster formula.** For \(A_{m,t}=\operatorname{diag}(t,J_m)\), the first coordinate has diagonal \(t\); the other \(m\) coordinates have diagonal 1. Pivoting first leaves residual \(J_m\), of Frobenius square \(m^2\); pivoting anywhere in the cluster leaves residual \(\operatorname{diag}(t,0_m)\), of square \(t^2\). Hence the exact expected *decrease* in Frobenius square is
\[
 G_\beta(m,t)
 :=\|A_{m,t}\|_F^2-\mathbb E\|B_i\|_F^2
 =\frac{t^{\beta+2}+m^3}{t^{\beta}+m},
 \qquad \|A_{m,t}\|_F^2=t^2+m^2.
\]
The target contraction is equivalent to \(G_\beta(m,t)\ge(t^2+m^2)/(m+1)\). At exponent zero,
\[
 G_0(m,t)-\frac{t^2+m^2}{m+1}
 =\frac{m^3-m^2}{m+1}>0.
\]
At exponent four, elementary algebra with \(y=t^2>0\) yields
\[
 G_4(m,t)-\frac{t^2+m^2}{m+1}
 =\frac{m\,[y^3-my^2-y+m^3]}{(m+1)(y^2+m)}.
\]
The numerator polynomial is positive for all \(m\ge2\), \(y\ge0\). If \(y\ge m\), it equals \((y-m)(y^2-1)+m^3-m>0\). If \(0\le y\le m\), use \(y^2(m-y)\le4m^3/27\) to bound it below by \(23m^3/27-m>0\).

Finally, the first-pivot probability \(t^\beta/(t^\beta+m)\) increases with \(\beta\) for \(t>1\) and decreases for \(t<1\). The first-pivot decrease is \(t^2\), while a cluster pivot decreases by \(m^2\). Therefore, when \(1\le t\le m\), \(G_\beta\) is nonincreasing in \(\beta\), and its minimum for \(0\le\beta\le4\) is \(G_4\). When \(t<1\) or \(t>m\), it is nondecreasing and its minimum is \(G_0\). The two endpoint bounds establish the uniform rank-two-family assertion for every real \(\beta\in[0,4]\).

**Sharpness above four.** Fix a real \(\beta>4\) and choose any \(a\) satisfying \(2/\beta<a<1/2\). Set \(t=m^a\) along positive integers \(m\to\infty\). Then
\[
 G_\beta(m,m^a)\le m^{2a}+m^{3-a\beta}=o(m),
 \qquad \frac{m^{2a}+m^2}{m+1}\sim m.
\]
Thus the target contraction fails strictly for all sufficiently large integers \(m\). For each such fixed \(m,t\), all pivots have positive diagonal, and both the sampling probabilities and downdated Frobenius squares depend continuously on the entries of \(A\) near \(A_{m,t}\). Replacing \(A\) by \(A+\varepsilon I\), for sufficiently small \(\varepsilon>0\), retains the strict failure and makes the matrix positive definite. This is existence, not a uniform perturbation bound independent of dimension.

## Verification

The companion `verify.py` uses exact Python fractions to recompute the explicit \(\beta=5\) witness, test the one-step block formula against direct matrix downdates, and compare the safe-interval bound with exact rational positive-definite matrices. It also checks the polynomial identity for chosen integer inputs. Finite tests do not replace either the all-dimensional general inequality or the continuum-of-exponents argument above.

Reproduce using `python3 verify.py` from this package's directory. No nonstandard Python packages are required.

## Relationship to prior work

Chen, Epperly, Tropp, and Webber (arXiv:2207.06503, originally submitted 13 July 2022) introduce the residual-diagonal-proportional randomized Cholesky pivot algorithm, with trace-norm expectations and multi-pivot accuracy bounds. Steinerberger (arXiv:2404.11487, submitted 17 April 2024) explicitly introduces Gibbs powers \(\beta\), proves one-step Frobenius contraction for \(\beta=2\), gives the exact general pivot identity used above, and demonstrates that overly greedy pivoting can be counterproductive. The \(\beta=2\) contraction is **prior work**, not claimed as original here. The differentiating statements are the proven continuum \(0\le\beta\le2\) and the exact threshold \(\beta=4\) on an explicitly motivated rank-two isolated-column-versus-redundant-cluster family. These do not follow directly from the cited published theorems, which neither give the continuum guarantee nor this family-specific threshold. A separate published adaptive-pivoting bound or specialization may still contain the result; no priority certification is claimed.

## Limitations

The phase boundary \(\beta=4\) is sharp **only for the block family**, not established as the largest safe exponent for all positive-semidefinite matrices. In particular, the general case \(2<\beta\le4\) is left unresolved. One-step expected squared Frobenius contraction does not establish multi-step optimality or every-realization behavior. The sharpness counterexamples grow in dimension; positive-definite perturbations are shown to exist individually. The result does not assert a new sampling implementation, an exact floating-point guarantee, or independence of review.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, first submitted 2022-07-13. https://arxiv.org/abs/2207.06503
2. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487, submitted 2024-04-17. https://arxiv.org/abs/2404.11487
