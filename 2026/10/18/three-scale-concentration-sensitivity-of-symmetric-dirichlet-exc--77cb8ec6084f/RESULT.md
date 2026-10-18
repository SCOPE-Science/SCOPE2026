# Three-scale concentration sensitivity of symmetric Dirichlet exceedances

## Finding

Let \(X=(X_1,\ldots,X_m)\sim\operatorname{Dirichlet}_m(\alpha,\ldots,\alpha)\) with integers \(m\ge2\) and real \(\alpha>0\). For \(t\in(0,1)\), set \(L=\sum_i\log X_i\), \(N(t)=\sum_i\mathbf1\{X_i>t\}\), and \(C_{m,\alpha}(t)=\operatorname{Cov}(L,N(t))\). Then

\[
C_{m,\alpha}(t)=m\,\partial_\alpha\Pr\{\operatorname{Beta}(\alpha,(m-1)\alpha)>t\}.
\]

For every such \(m,\alpha\), there is a **unique** \(t_{m,\alpha}\in(0,1)\) such that \(C_{m,\alpha}(t)>0\) below it and \(C_{m,\alpha}(t)<0\) above it. Three scale limits specify this transition:

\[
\begin{aligned}
\lim_{\alpha\downarrow0}C_{m,\alpha}(t)&=(m-1)\log\frac{1-t}{t},
&\lim_{\alpha\downarrow0}t_{m,\alpha}&=\tfrac12,\\
\lim_{\alpha\to\infty}t_{m,\alpha}&=\tfrac1m,\\
\lim_{m\to\infty}\frac{C_{m,\alpha}(y/m)}m&=G_\alpha(y),
&\lim_{m\to\infty}m t_{m,\alpha}&=y_\alpha.
\end{aligned}
\]

In the third line, \(\alpha>0\) and \(y>0\) are fixed,
\[
g_\alpha(u)=\frac{\alpha^\alpha u^{\alpha-1}e^{-\alpha u}}{\Gamma(\alpha)},\qquad
G_\alpha(y)=\int_y^\infty g_\alpha(u)
\big(\log u-u+1+\log\alpha-\psi(\alpha)\big)\,du.
\]
The function \(G_\alpha\) has exactly one zero \(y_\alpha\) in \((0,\infty)\), positive below and negative above. For \(\alpha=1\),
\[
G_1(y)=e^{-y}(\log y+\gamma-y)+E_1(y),\qquad
 y_1=1.3714020181783595\ldots,
\]
where \(\gamma\) is Euler's constant and \(E_1(y)=\int_y^\infty e^{-u}/u\,du\). In particular, the growing-dimension cutoff is not simply \(1/m\) at finite shape.

## Assumptions and scope

The coordinates are strictly positive almost surely and sum to one. All logarithms are natural; all expectations are under this fully symmetric finite-dimensional Dirichlet law. \(\psi\) is the digamma function. The covariance measures the derivative of expected threshold occupancy with respect to the common shape parameter; no independence of the threshold indicators is assumed. All three limits are taken in the stated, distinct orders. The first covariance limit holds for fixed interior \(t\), not uniformly up to \(t=0,1\). The third is a fixed-shape, growing-dimensional limit, not a fixed-total-mass Dirichlet-process limit.

## Proof

**1. Score identity.** The Dirichlet density is \(\Gamma(m\alpha)\prod_i x_i^{\alpha-1}/\Gamma(\alpha)^m\). Its \(\alpha\)-score is
\[
S(X)=L-m\psi(\alpha)+m\psi(m\alpha)=L-\mathbb E L.
\]
Differentiation under the integrable density gives \(\partial_\alpha\mathbb E N(t)=\mathbb E[S(X)N(t)]\). Exchangeability and the beta marginal yield the displayed covariance identity. Write
\[
f_{m,\alpha}(x)=\frac{x^{\alpha-1}(1-x)^{(m-1)\alpha-1}}{B(\alpha,(m-1)\alpha)},\quad
h_{m,\alpha}(x)=\log x+(m-1)\log(1-x)-\psi(\alpha)-(m-1)\psi((m-1)\alpha)+m\psi(m\alpha).
\]
Then
\[
C_{m,\alpha}(t)=m\int_t^1 h_{m,\alpha}(x)f_{m,\alpha}(x)\,dx,
\qquad\int_0^1h_{m,\alpha}f_{m,\alpha}=0.
\]

**2. Unique threshold.** The derivative \(h'_{m,\alpha}(x)=(1-mx)/(x(1-x))\). Therefore \(h\) increases strictly to its sole maximum at \(x=1/m\), decreases strictly afterward, and tends to \(-\infty\) at both endpoints. Since its beta-density integral vanishes, its maximum must be positive, yielding exactly two simple roots \(a<1/m<b\) and signs negative, positive, negative. Since \(C'(t)=-m h(t)f(t)\), \(C(0+)=C(1-)=0\), the tail integral rises to a positive maximum at \(a\), falls through a unique zero between \(a\) and \(b\), reaches a negative minimum at \(b\), then rises to zero. This proves the unique sign transition, including \(m=2\), where symmetry gives \(t_{2,\alpha}=1/2\).

**3. Sparse-concentration limit.** For each fixed \(m\), as \(\alpha\downarrow0\),
\[
B(\alpha,(m-1)\alpha)^{-1}=\frac{m-1}{m}\alpha+O_m(\alpha^3).
\]
The incomplete-beta integral through any fixed interior \(t\) has expansion
\[
\int_0^t x^{\alpha-1}(1-x)^{(m-1)\alpha-1}\,dx
=\frac1\alpha+\log\frac{t}{1-t}+O_{m,t}(\alpha).
\]
It follows that
\[
\Pr\{X_1>t\}=\frac1m+\frac{m-1}{m}\alpha\log\frac{1-t}{t}+O_{m,t}(\alpha^2),
\]
where the remainder is differentiable in \(\alpha\) near zero by the same dominated endpoint subtraction. Differentiation yields the claimed covariance limit. Its strict signs on the two sides of \(1/2\), combined with the proven uniqueness of the finite-shape threshold, squeeze \(t_{m,\alpha}\to1/2\).

**4. Concentrated-shape limit.** From \(\psi(z)=\log z+O(1/z)\), \(h_{m,\alpha}\) converges uniformly on compact subintervals of \((0,1)\) to
\[
h_\infty(x)=\log x+(m-1)\log(1-x)+m\log m-(m-1)\log(m-1).
\]
This is negative except at its unique maximum \(x=1/m\), where it equals zero. Both finite-\(\alpha\) score roots \(a,b\) consequently converge to \(1/m\): for any fixed \(\varepsilon>0\), outside the \(\varepsilon\)-neighborhood the score is eventually strictly negative, and the maximum is positive. The unique covariance root lies strictly between \(a,b\), so \(t_{m,\alpha}\to1/m\).

**5. Growing dimension.** With \(Y_m=mX_1\), the beta marginal has the density of a normalized beta variable. For fixed \(\alpha>0\), Stirling's formula and \((1-u/m)^{(m-1)\alpha-1}\to e^{-\alpha u}\) show that \(Y_m\) converges in law and locally in density to \(g_\alpha\). Digamma asymptotics show, uniformly on compact positive \(u\)-ranges,
\[
h_{m,\alpha}(u/m)\to H_\alpha(u)=\log u-u+1+\log\alpha-\psi(\alpha).
\]
The normalized covariance \(C_{m,\alpha}(y/m)/m\) is the upper-tail integral of these two factors. Uniform integrability follows, for instance, from the exact second moment of the centered beta score, \[\mathbb E[h_{m,\alpha}(X_1)^2]=\psi_1(\alpha)+(m-1)^2\psi_1((m-1)\alpha)-m^2\psi_1(m\alpha)=O_\alpha(1),\] where \(\psi_1\) is the trigamma function: its large-argument expansion gives the finite limit \(\psi_1(\alpha)-1/\alpha\). This uniform square-integrability, along with local density and score convergence and tightness of \(Y_m\), proves convergence of the upper-tail score integrals for each fixed \(y>0\). The limiting score \(H_\alpha\) has \(H'_\alpha(u)=1/u-1\), is negative at zero and infinity, and has positive maximum because its mean under \(g_\alpha\) is zero. As in step 2, its tail integral has exactly one sign change. Pointwise convergence at two continuity points bracketing \(y_\alpha\) and uniqueness of the finite covariance zero imply \(m t_{m,\alpha}\to y_\alpha\). At \(\alpha=1\), one integration by parts gives the explicit \(E_1\) expression.

## Verification

Running `python dirichlet_log_exceedance_verify.py` with Python 3, NumPy-compatible SciPy, and mpmath completes 139 cross-checks: 75 comparisons of quadrature with an independent fourth-order finite difference of the beta CDF; 42 numerical sign checks over 21 parameter pairs; 12 high-precision small-shape comparisons; seven growing-dimensional comparisons; and three special symmetry/closed-form checks. The printed gamma root is approximately \(1.3714020181784\). These experiments independently check formulas over finite test points but do **not** certify any quantifier over all parameters; the analytic argument is the proof.

## Relationship to prior work

The gamma representation and extremal statistics of Dirichlet vectors are classical; Bose–Dasgupta–Maulik (2008) study Dirichlet and gamma maxima, not the derivative/covariance profile here. Griffiths–Spanò (2010) establish orthogonal-polynomial and canonical-correlation structures for Dirichlet laws, without this score–exceedance asymptotic triple. Portnoy–Torrado–Veerman (2023), Theorem 4.3, prove the broader **finite-parameter single crossing** property for fixed-mean beta families. Thus the existence of a concentration crossing is not offered as an independent priority claim; it is retained as a necessary ingredient for the precise score-covariance and three-scale interpolation theorem. The latter gives actual limiting covariance amplitudes and moving root locations not stated by that theorem. Hjelle (2025) analyzes approximate threshold-count optimization in a **fixed-total-mass** regime; its exponential-integral root \(0.434818\ldots\) pertains to varying total mass and is not the fixed-shape gamma score root \(1.371402\ldots\) here. A historical possibility of implicit derivation from those broader results remains.

## Limitations

The results are for equal positive Dirichlet parameters and common thresholds only. They do not prove monotonicity of \(t_{m,\alpha}\) as a function of \(\alpha\), and the limits do not commute indiscriminately. No claim is made about arbitrary asymmetric Dirichlet priors, joint distributions of threshold counts, publication priority, or independent verification.

## References

1. Bose, A., Dasgupta, A., and Maulik, K. (2008), *Maxima of Dirichlet and triangular arrays of gamma variables*, arXiv:0803.3518 (public 2008-03-25).
2. Griffiths, R. and Spanò, D. (2010), *Orthogonal polynomial kernels and canonical correlations for Dirichlet measures*, arXiv:1003.5131.
3. Arab, I., Oliveira, P., and Wiklund, T. (2020), *Convex transform order of Beta distributions with some consequences*, arXiv:2005.08204.
4. Portnoy, S., Torrado, N., and Veerman, J. (2023), *The Bunching and Monotonicity Properties of Families of Probability Distributions*, https://web.pdx.edu/~veerman/bunching.pdf (especially Theorem 4.3).
5. Hjelle, E. O. (2025), *Heuristics for setting sparse Dirichlet priors*, https://eohjelle.com/posts/heuristics-for-setting-sparse-dirichlet-priors/.
