# Sharp stationary precision-floor threshold for stochastically rounded scalar descent

## Finding

An unbiased stochastic rounding step can maintain the **smallest possible stationary grid error** even after a scalar gradient method begins to overrelax. The precise point at which this ceases to be possible depends only on the target's fractional grid position. Beyond that point, the steady state necessarily uses additional grid sites, despite the fact that the mean remains unbiased.

Let \(0<\beta<1\), \(-1<a<1\), and \(J_0\in\mathbb Z\). Define the Markov recursion
\[
J_{n+1}=\left\lfloor aJ_n+(1-a)\beta+U_n\right\rfloor,
\qquad U_n\stackrel{\mathrm{iid}}{\sim}\mathrm{Unif}(0,1).
\]
(The uniform variables are independent of the starting state.) This is ideal unbiased rounding of one exact affine update to consecutive grid points. Put
\[
c_{\mathrm{crit}}(\beta)=\min\left\{\frac{\beta}{1-\beta},\frac{1-\beta}{\beta}\right\}.
\]
There is a unique invariant probability distribution \(\pi_{a,\beta}\). Its mean is \(\beta\), and for every deterministic starting integer the chain converges geometrically in \(W_1\), at contraction factor at most \(|a|\). Its stationary mean-square error satisfies
\[
\mathbb E_{\pi_{a,\beta}}(J-\beta)^2\ge \beta(1-\beta),
\]
with equality **if and only if** \(a\ge-c_{\mathrm{crit}}(\beta)\). In that region the unique stationary law is \(\Pr(J=1)=\beta\), \(\Pr(J=0)=1-\beta\). For \(-1<a<-c_{\mathrm{crit}}(\beta)\) the inequality is strict. In particular, when \(\beta=1/2\), every \(-1<a<1\) achieves the minimum.

The first post-threshold phase is explicit. If \(\beta=1/4\), \(a=-c\), and \(1/3<c\le3/5\), then the invariant support is precisely \(\{-1,0,1\}\), with
\[
\begin{aligned}
\pi(-1)&=\frac{3c-1}{4(5-3c)},\\
\pi(0)&=\frac{17-15c}{4(5-3c)},\\
\pi(1)&=\frac{1}{5-3c},\\
\mathbb E_{\pi}(J-1/4)^2&=\frac{3}{16}+\frac{3c-1}{2(5-3c)}.
\end{aligned}
\]
For \(c=2/5\), this is exactly \(65/304\), versus the unavoidable grid floor \(3/16\). At \(c>3/5\), site \(2\) becomes reachable from site \(-1\), so the three-site support is no longer closed. All statements rescale by the square of the grid spacing under an affine change of units.

## Assumptions and scope

The representable values form the infinite, equally spaced grid \(\mathbb Z\); no underflow or overflow occurs. Only the final value of the exact affine update is rounded, and each iteration uses a fresh independent uniform random variable. The target is strictly between adjacent grid values, \(0<\beta<1\). The multiplier satisfies \(-1<a<1\), the full deterministic scalar contraction range. For gradient descent on \(f(x)=\lambda(x-\beta)^2/2\) with \(\lambda>0\) and step size \(\eta\), one has \(a=1-\eta\lambda\); thus \(0<\eta\lambda<2\). A grid of spacing \(\Delta>0\) is obtained by multiplying all states and the target by \(\Delta\); variances then multiply by \(\Delta^2\).

## Proof

**1. Contractive Markov kernel and the invariant mean.** For every real \(z\), the random integer \(R(z,U)=\lfloor z+U\rfloor\) with \(U\sim\mathrm{Unif}(0,1)\) satisfies \(\mathbb E R(z,U)=z\). If \(z\le w\), using the same \(U\) gives \(R(z,U)\le R(w,U)\), hence
\[
\mathbb E|R(z,U)-R(w,U)|=\mathbb E(R(w,U)-R(z,U))=w-z.
\]
For affine arguments \(F(j)=aj+(1-a)\beta\), this coupling therefore gives expected distance \(|a|\,|j-k|\), irrespective of the sign of \(a\). By coupling initial distributions, the Markov operator contracts the Wasserstein-1 metric on probability distributions on \(\mathbb Z\) with finite first moment by at most \(|a|\). That space is complete, so the operator has one invariant probability measure and its iterates converge geometrically in \(W_1\). Because \(|R(z,U)-z|\le1\), the deterministic estimate
\[
|J_n-\beta|\le |a|^n|J_0-\beta|+\sum_{r=0}^{n-1}|a|^r
\]
holds pathwise. Thus deterministic starts and their limiting invariant law have uniformly bounded support, and the squared-error moments also converge. Conditional unbiasedness gives \(\mathbb E[J_{n+1}\mid J_n]=aJ_n+(1-a)\beta\); invariance implies \(\mathbb E_\pi J=\beta\).

**2. Absolute grid floor.** Every integer \(j\) satisfies \(j(j-1)\ge0\), with equality exactly at \(j=0\) or \(1\). For any integer random variable of mean \(\beta\),
\[
\mathbb E(J-\beta)^2=\beta(1-\beta)+\mathbb E[J(J-1)].
\]
Therefore the smallest possible mean-square error is \(\beta(1-\beta)\), attained only by the Bernoulli law on the two neighboring grid points.

**3. Sharp retention threshold.** The affine images of those two points are
\[
F(0)=(1-a)\beta,\qquad F(1)=a+(1-a)\beta.
\]
Stochastic rounding of a real number stays within \(\{0,1\}\) exactly when its input lies in \([0,1]\). If \(0\le a<1\), both images are in \([0,1]\). If \(-1<a<0\), writing \(c=-a\), the joint closure conditions reduce to
\[
c\le\frac{1-\beta}{\beta},\qquad c\le\frac{\beta}{1-\beta}.
\]
Whenever the two sites are closed, the Bernoulli law with mass \(\beta\) at \(1\) is invariant: its mean is \(\beta\), and the image mixture is still supported on these two points, so the mean determines its weights. By uniqueness it is the global invariant law. Conversely, if either closure condition fails, the Bernoulli law necessarily sends positive probability outside \(\{0,1\}\) in one step (both Bernoulli weights are nonzero). It cannot be invariant, and Step 2 gives strict excess error. Equality at the parameter boundary remains in the closed phase.

**4. Exact three-site phase.** Set \(\beta=1/4\), \(a=-c\), with \(1/3<c\le3/5\). Then
\[
F(-1)=\frac{1+5c}{4}\in(0,1],\quad
F(0)=\frac{1+c}{4}\in(0,1),\quad
F(1)=\frac{1-3c}{4}\in(-1,0).
\]
Consequently \(\{-1,0,1\}\) is closed, and all three states communicate with positive probability; the chain is aperiodic because \(0\) has a self-loop. Writing \(u=\pi(1)\), the balance equation at \(-1\) reads \(\pi(-1)=u(3c-1)/4\). The invariant mean is \(u-\pi(-1)=1/4\), giving \(u=1/(5-3c)\) and the probabilities stated above. Substitution into \(\mathbb E J^2-(1/4)^2\) yields the displayed variance. The boundary \(c=3/5\) is included: then \(F(-1)=1\). For \(c>3/5\), \(F(-1)>1\) and positive mass can jump to \(2\), so the three-site invariant support is lost. This completes the proof.

## Verification

The standalone standard-library script `verify.py` checks all two-site closure inequalities on a rational grid of parameters, tests the shared-uniform coupling identity with exact rational integration, proves the displayed three-state stationarity identities by rational calculation, and compares long but finite Markov iterations with the stationary formulas. The scripted checks are supplemental; they are not substituted for the global analytic existence, uniqueness, or sharpness arguments above.

Run with `python verify.py` under a standard Python 3 environment. It reports `PASS: 873 exact checks` on successful execution.

## Relationship to prior work

Connolly, Higham, and Mary establish the unbiased stochastic rounding rule and mean-independent rounding-error analysis; their paper studies floating-point error bounds and numerical kernels, not the exact stationary distribution of a rounded affine contraction. The stochastic-rounding survey by Croci and coauthors identifies applications and the important distinction between fixed-point and floating-point grids, without providing the phase threshold here. The gradient-descent studies of Xia and coauthors analyze convergence and biases under low-precision arithmetic; their displayed theory is finite-time or neighborhood/rate oriented rather than a complete invariant-law classification for a once-rounded, ideal fixed-grid scalar recursion. In particular, their commonly imposed small-step conditions do not entail the overrelaxation threshold in this theorem.

The coupling contraction and the elementary integer variance inequality are standard mathematical tools; novelty is **not** claimed for them in isolation. The asserted contribution is their explicit combination into the sharp all-fractional-positions precision-floor condition and the exact first post-transition invariant law. No search can exclude every unpublished or unindexed equivalent result.

## Limitations

This is a self-contained scalar and idealized fixed-point-arithmetic model: the exact gradient step is computed before a single unbiased stochastic rounding. Real low-precision software may round gradients, products, and subtractions separately, may have a nonuniform floating-point grid, and may cap exponents. None of those implementations is covered. The statement concerns stationary mean-square error, not the best transient stepsize, operation count, or a multi-dimensional optimization rate. The invariant law is unbiased in the mean but does not concentrate on the generally nonrepresentable target. The explicit three-state formula holds only on the stated parameter range.

## References

1. M. P. Connolly, N. J. Higham, T. Mary, *Stochastic Rounding and Its Probabilistic Backward Error Analysis*, SIAM Journal on Scientific Computing 43 (2021), A566–A585, doi:10.1137/20M1334796; publicly deposited preprint 2020-04-28.
2. M. Croci, M. Fasi, N. J. Higham, T. Mary, M. Mikaitis, *Stochastic Rounding: Implementation, Error Analysis, and Applications*, MIMS EPrint 2021.17, October 2021, https://eprints.maths.manchester.ac.uk/2836/1/cfhm21.pdf.
3. L. Xia, S. Massei, M. E. Hochstenbach, B. Koren, *On the influence of stochastic roundoff errors and their bias on the convergence of the gradient descent method with low-precision floating-point computation*, arXiv:2202.12276, first posted 2022-02-24.
4. L. Xia, S. Massei, M. E. Hochstenbach, *On the Convergence of the Gradient Descent Method with Stochastic Fixed-Point Rounding Errors under the Polyak–Łojasiewicz Inequality*, arXiv:2301.09511, first posted 2023-01-23.
