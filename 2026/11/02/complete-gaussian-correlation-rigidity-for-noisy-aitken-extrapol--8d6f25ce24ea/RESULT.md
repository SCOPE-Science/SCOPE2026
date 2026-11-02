# Complete Gaussian correlation rigidity for noisy Aitken extrapolation

## Finding
For three equal-variance jointly Gaussian observations of a geometric contraction, exact correlation of all three noises is the **only** covariance design that leaves unregularized Aitken \(\Delta^2\) extrapolation with a finite mean. Every other admissible covariance, including singular but not perfectly common ones, produces a nonzero, explicitly computed \(t^{-1}\) two-sided tail. The coefficient becomes exponentially small as equicorrelation approaches one while the mean remains infinite at every nonexact correlation.

Precisely, let \(0<r<1\), \(a\ne0\), \(\sigma>0\) and \(\theta\in\mathbb R\). Let \((\varepsilon_0,\varepsilon_1,\varepsilon_2)\) be any centered jointly Gaussian vector, possibly supported on a proper linear subspace, with \(\operatorname{Var}(\varepsilon_j)=\sigma^2\) for all three indices. Observe \(Z_j=\theta+ar^j+\varepsilon_j\), and define
\[
X=Z_1-Z_0,\qquad D=Z_2-2Z_1+Z_0,\qquad T=Z_0-\frac{X^2}{D}.
\]
The denominator is nonzero almost surely, even in the exceptional perfectly common case. Let \(m_X=a(r-1)\), \(m_D=a(r-1)^2\), \(v_X=\operatorname{Var}(X)\), \(v_D=\operatorname{Var}(D)\), and \(c=\operatorname{Cov}(X,D)\).

If all three noise coordinates coincide almost surely, \(T=\theta+\varepsilon_0\) and it has finite moments of every order. Otherwise \(v_D>0\) and
\[
\begin{aligned}
K&=\frac{\exp[-m_D^2/(2v_D)]}{\sqrt{2\pi v_D}}
\left(v_X-\frac{c^2}{v_D}+
\left(m_X-\frac{c m_D}{v_D}\right)^2\right)>0,\\
\lim_{t\to\infty}t\,\Pr(T-\theta>t)&=K,
\qquad\lim_{t\to\infty}t\,\Pr(T-\theta<-t)=K.
\end{aligned}
\]
Consequently \(\mathbb E|T-\theta|^p<\infty\) if and only if \(0<p<1\); in particular the unregularized extrapolate has neither finite mean absolute error nor finite mean-square error. Its capped-square loss satisfies \(\mathbb E[\min\{(T-\theta)^2,B^2\}]/B\to4K\) as \(B\to\infty\).

For equicorrelated errors with \(\operatorname{Corr}(\varepsilon_i,\varepsilon_j)=\rho\) for distinct indices, admissible \(-1/2\le\rho\le1\), and \(\rho<1\), the explicit one-sided tail coefficient becomes
\[
K(\rho)=\frac{\exp\!\left[-\frac{a^2(1-r)^4}{12\sigma^2(1-\rho)}\right]}{\sigma\sqrt{12\pi(1-\rho)}}
\left[\frac{a^2(1-r^2)^2}{4}+\frac{\sigma^2(1-\rho)}2\right].
\]
It is positive for every \(\rho<1\) and tends to zero with an essential-exponential factor as \(\rho\uparrow1\); at \(\rho=1\) the entire tail changes to the Gaussian law \(N(\theta,\sigma^2)\).

## Assumptions and scope
The three observations use the **same** deterministic geometric signal \(\theta+ar^j\). Their Gaussian errors have identical positive marginal variance but arbitrary cross-covariance, including positive-semidefinite singular covariances. No independence, stationarity in the index, symmetry of correlation or Gaussian process extension is assumed. The result concerns the single unregularized \(\Delta^2\) transform in exact arithmetic, not a recurrently extrapolated stochastic algorithm or a regularized estimator. All limits are for fixed \(a,r,\sigma\) and fixed covariance as the error threshold tends to infinity; the \(\rho\uparrow1\) statement is a subsequent parameter limit, not a uniform interchange of limits.

## Proof
**Step 1: The denominator degeneracy is exactly common noise.** Let \(U_j=\varepsilon_j\). If \(\operatorname{Var}(U_2-2U_1+U_0)=0\), the centered difference is identically zero, whence \(U_1=(U_0+U_2)/2\). Equal marginal variances and the identity
\[
\mathbb E\left[\left(\frac{U_0+U_2}{2}\right)^2\right]
=\sigma^2-\frac14\mathbb E[(U_0-U_2)^2]
\]
force \(U_0=U_2=U_1\) almost surely. Conversely common errors give zero random part in \(D\). In that case \(D=m_D\ne0\) and the deterministic geometric identity \(a-m_X^2/m_D=0\) gives \(T=\theta+U_0\).

**Step 2: The potential pole cannot cancel for any noncommon equal-variance coupling.** Suppose \(v_D>0\). Gaussian conditioning gives \(X\mid D=d\) mean \(m_X+(c/v_D)(d-m_D)\) and variance \(s^2=v_X-c^2/v_D\ge0\), including degenerate conditional laws. Thus
\[
\mathbb E[X^2\mid D=0]=s^2+(m_X-cm_D/v_D)^2.
\]
If this expression were zero, \(s^2=0\) and \(m_X=cm_D/v_D\). Therefore the jointly Gaussian pair satisfies \(X=kD\) identically, with \(k=m_X/m_D=1/(r-1)\). Comparing noise parts and rearranging yields
\[
U_2=(1+r)U_1-rU_0.
\]
Since each has variance \(\sigma^2\), taking variances of the right side gives
\[
0=2r(1+r)\big(\sigma^2-\operatorname{Cov}(U_0,U_1)\big).
\]
Because \(0<r<1\), it follows that the covariance is \(\sigma^2\), so \(U_0=U_1\) almost surely, then also \(U_2=U_1\). This contradicts \(v_D>0\); hence the displayed conditional second moment is strictly positive.

**Step 3: Pole-tail lemma, including singular joint Gaussians.** If \((U,V,W)\) is jointly Gaussian with \(\operatorname{Var}(V)>0\), set \(R=W-U^2/V\). For \(S=U^2/V\), the positive tail is exactly
\[
 t\Pr(S>t)=\int_0^\infty
 \Pr(U^2>z\mid V=z/t)f_V(z/t)\,dz.
\]
For each fixed \(z\), its integrand tends to \(\Pr(U^2>z\mid V=0)f_V(0)\). On \(0<V\le\delta\), the conditional Gaussian mean of \(U\) is uniformly bounded and conditional variance is fixed; its tails have a uniform exponentially decaying envelope in \(z\). On \(V>\delta\), \(S>t\) implies \(U^2>t\delta\), an exponentially unlikely Gaussian event, so that region contributes \(o(1)\) after multiplication by \(t\). Dominated convergence and the tail integral formula yield
\[
\lim_{t\to\infty}t\Pr(S>t)=f_V(0)\,\mathbb E[U^2\mid V=0].
\]
The same coefficient applies to \(-S\) by applying the argument to \(-V\). Finally, since \(W\) is Gaussian, \(\Pr(|W|>\epsilon t)=o(1/t)\) for every fixed \(\epsilon>0\). Sandwiched tails for \(R=W-S\) at thresholds \((1\pm\epsilon)t\), followed by \(\epsilon\downarrow0\), preserve both coefficients. This proof does not require a nonsingular covariance for the triple. Apply it to \((U,V,W)=(X,D,Z_0-\theta)\). The normal density of \(D\) at zero is \(f_D(0)=e^{-m_D^2/(2v_D)}/\sqrt{2\pi v_D}\), which proves the exact formula for \(K\) and its positivity.

**Step 4: Moment and capped-loss consequences.** From both tails, \(\Pr(|T-\theta|>t)\sim2K/t\). Integrating \(p\int_0^\infty t^{p-1}\Pr(|T-\theta|>t)dt\) shows finiteness for \(p<1\) and divergence for \(p\ge1\); finiteness at smaller \(t\) follows from a finite a.s. random variable. The identity \(\mathbb E\min\{Y^2,B^2\}=2\int_0^B t\Pr(|Y|>t)dt\) with \(Y=T-\theta\) gives the \(4KB\) limit.

**Step 5: Equicorrelated specialization.** For \(\rho<1\), direct covariance calculation gives
\[
 v_X=2\sigma^2(1-\rho),\quad v_D=6\sigma^2(1-\rho),\quad c=-3\sigma^2(1-\rho).
\]
Consequently \(v_X-c^2/v_D=\sigma^2(1-\rho)/2\), and \(m_X-cm_D/v_D=a(r^2-1)/2\). Substitution yields the stated closed form. Since \(a(r-1)^2\ne0\), the exponential suppresses the positive coefficient as \(\rho\uparrow1\), while Step 1 gives the exact Gaussian endpoint. This completes the proof.

## Verification
Run \(`python verify.py`\) with Python 3 and its standard library. The standalone script checks exact-rational covariance identities at six equicorrelations, evaluates the general Gaussian conditional coefficient for two thousand seeded positive-semidefinite covariance examples, verifies the noncancellation variance relation, and checks the small-noise endpoint numerically. Its 2,044 finite checks passed. The mathematical proof above, not the finite tests, establishes the universal quantifiers, positive heavy-tail constants, and moment thresholds.

## Relationship to prior work
Aitken's classical \(\Delta^2\) transform is the base nonlinear extrapolation; deterministic convergence acceleration is not new. Scieur, Oyallon, d'Aspremont and Bach (2018) analyze **regularized** nonlinear acceleration under independent stochastic perturbations and give finite expected-error bounds with noise-dependent regularization. Krzysik, De Sterck and Smith (2023) analyze deterministic restarted Anderson acceleration on affine normal systems. Neither result implies the unregularized, exactly equal-marginal **all-covariance** rigidity and sharp coefficient stated here. Ordinary ratio-distribution theory explains the generic reciprocal singularity but does not alone determine whether correlated equal-marginal Gaussian noise can make its pole disappear; the variance-rigidity argument in Step 2 resolves that question.

Other known Gaussian ratio and extrapolation tail phenomena may give an alternative derivation of the pole coefficient, so the specific all-correlation rigidity classification—not the idea that divisions by noisy differences can have heavy tails—is the claimed contribution. Equivalent formulations in specialized statistical extrapolation or correlated-noise literature remain a priority risk.

## Limitations
No claim is made that finite covariance or regularization is necessary for usable **quantile-based**, truncated or robust estimators. A tail coefficient tending to zero is not convergence in \(L^1\): each strictly subunit equicorrelation still has infinite first absolute moment. The calculation does not cover unequal marginal variances, non-Gaussian errors, infinitely many extrapolated levels or finite-precision division. No independent scientific validation has been performed.

## References
- D. Scieur, E. Oyallon, A. d'Aspremont and F. Bach, *Online Regularized Nonlinear Acceleration*, arXiv:1805.09639, first public 2018-05-24, https://arxiv.org/html/1805.09639v2 .
- O. A. Krzysik, H. De Sterck and A. Smith, *Asymptotic convergence of restarted Anderson acceleration for certain normal linear systems*, arXiv:2312.04776, first public 2023-12-08, https://arxiv.org/html/2312.04776v4 .
- AMS, *MSC2020*, entry 65B05, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=65Bxx .
