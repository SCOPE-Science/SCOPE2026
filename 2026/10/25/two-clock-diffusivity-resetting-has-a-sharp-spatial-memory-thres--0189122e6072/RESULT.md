# Two-clock diffusivity resetting has a sharp spatial-memory threshold

## Finding
Independent resetting of a common fluctuating diffusivity and of particle positions creates a sharp long-lag memory boundary. The cross-coordinate squared-position covariance approaches the same *relative* magnitude as the same-coordinate covariance exactly when medium relaxation is no faster than position resetting. Otherwise their asymptotic ratio is strictly below one. The result is an exact stationary fourth-order two-time statement, not a conventional thermodynamic phase transition.

For positive parameters \(a,b,\Lambda\), let
\[
V=\frac{16\Lambda^4(a+11b)}{a^2b^2(a+b)},\qquad
H=\frac{40\Lambda^4}{a^2(a+b)},\qquad
M=\frac{32\Lambda^4(a+6b)}{a^2b^2(a+b)}.
\]
For different coordinate labels \(i\ne j\) and all \(t\ge0\),
\[
\operatorname{Cov}(X_i(0)^2,X_j(t)^2)=K(t)
=e^{-bt}\left(V+2H\int_0^t e^{(b-a)s}\,ds\right).
\]
For the same coordinate and for the empirical spatial mean \(S_n=n^{-1}\sum_i X_i^2\), respectively,
\[
\operatorname{Cov}(X_i(0)^2,X_i(t)^2)=K(t)+2Me^{-bt},\qquad
\operatorname{Cov}(S_n(0),S_n(t))=K(t)+\frac{2M}{n}e^{-bt}.
\]
The ratio of different- to same-coordinate lag covariances is
\[
R(t)=\frac{K(t)}{K(t)+2Me^{-bt}}.
\]
It is **strictly increasing** for \(t\ge0\) and obeys the sharp classification
\[
\lim_{t\to\infty}R(t)=
\begin{cases}
1,&a\le b,\
\displaystyle\frac{a^2+10ab-6b^2}{5(a^2+6ab-6b^2)},&a>b.
\end{cases}
\]
The second expression belongs to \((1/5,1)\) for every \(a>b\). When the two reset rates coincide **but their clocks remain independent**, the covariance has a repeated-rate form \(K(t)=e^{-bt}(V+2Ht)\). Both absolute covariances tend to zero; the limit of their *ratio* does not express enduring time correlations.

## Assumptions and scope
Take an integer \(n\ge2\) and \(a,b,\Lambda>0\). Let \(B,W_1,\ldots,W_n\) be independent standard Brownian motions. A real medium variable follows \(dY_t=\sqrt2\Lambda\,dB_t\), with jumps resetting \(Y\) to zero at points of a rate-\(a\) Poisson clock. Each position follows \(dX_i=\sqrt2\,Y_t\,dW_i\) between jumps of an independent common rate-\(b\) clock resetting all \(X_i\) to zero **without altering \(Y\)**. The two clocks, as well as the Brownian motions, are mutually independent. Using \(Y_t\) instead of \(|Y_t|\) changes no position law conditional on the medium, because they generate the same quadratic variation. This *asynchronous resetting* is distinct from the original common-clock protocol.

Construct the stationary state using two-sided independent Poisson clocks and Brownian noises. The medium has a finite exponentially distributed backward age, and each position has a finite backward age to the common position clock. All moments used here are finite. At a fixed time, conditional on the entire medium path and position-reset clock, the coordinates are independent centered Gaussian variables with a common conditional variance \(Z_t=2\int_{\tau_b(t)}^t Y_s^2\,ds\), where \(\tau_b(t)\) is the last position-reset instant. Finite-dimensional convergence in the number of coordinates follows by conditional strong laws; no uniform-in-time convergence is asserted.

## Proof
**1. Medium and mixed stationary moments.** The invariant generator on the medium and two positions, with independent reset clocks, is
\[
\mathcal L f=\Lambda^2\partial_{yy}f+y^2(\partial_{xx}+\partial_{zz})f
+a[f(x,z,0)-f(x,z,y)]+b[f(0,0,y)-f(x,z,y)].
\]
Here the notation \(f(x,z,y)\) has medium coordinate \(y\), while \(x,z\) denote two different particle coordinates. Stationarity gives
\[
\mathbb E Y^2=\frac{2\Lambda^2}{a},\quad
\mathbb E Y^4=\frac{24\Lambda^4}{a^2},\quad
\mathbb E X_i^2=\frac{4\Lambda^2}{ab},\quad
\operatorname{Cov}(X_i^2,Y^2)=H.
\]
The last identity follows by applying the generator to \(X_i^2Y^2\):
\[
(a+b)\mathbb E[X_i^2Y^2]=2\mathbb E[Y^4]+2\Lambda^2\mathbb E[X_i^2].
\]
Likewise \(b\mathbb E[X_i^2X_j^2]=4\mathbb E[X_i^2Y^2]\) for distinct coordinates. Therefore
\[
\mathbb E[X_i^2X_j^2]=M,\qquad
\operatorname{Cov}(X_i^2,X_j^2)=V,
\]
with \(M,V\) as in the finding. Conditional Gaussianity yields \(\mathbb E X_i^4=3M\), and the same-coordinate square variance equals \(V+2M\). As an independent check, the stationary medium-square autocovariance is \(20\Lambda^4 a^{-2}e^{-a|t|}\). Integrating it twice against the independent exponential age of the position-reset clock gives \(\mathbb E Z_t^2=M\) and \(\operatorname{Var}Z_t=V\), reproducing the generator results.

**2. Two-time common-environment covariance.** Write \(K(t)=\operatorname{Cov}(X_i(0)^2,X_j(t)^2)\) for distinct labels. Since a coordinate's squared-position drift is \(2Y_t^2\) and the shared position reset kills its square at rate \(b\),
\[
K'(t)=2\operatorname{Cov}(X_i(0)^2,Y_t^2)-bK(t).
\]
The medium square has conditional-mean relaxation rate \(a\), independently of position resets, so its mixed covariance is \(H e^{-at}\). Thus \(K'(t)+bK(t)=2He^{-at}\), with \(K(0)=V\). Solving gives the stated integral, and, if \(a\ne b\), the equivalent explicit form
\[
K(t)=Ve^{-bt}+\frac{2H}{b-a}(e^{-at}-e^{-bt}).
\]
When \(a=b\), its continuous limit is \(e^{-bt}(V+2Ht)\). The integral expression proves \(K(t)>0\) for all finite \(t\ge0\).

**3. Brownian self-memory.** Conditional on the environment and clock, two observations of the same coordinate remain jointly Gaussian. Their conditional covariance equals the pre-observation quadratic variation \(Z_0\) if there is *no position reset* in \((0,t]\), and is zero otherwise. Wick's identity therefore supplies an additional squared-coordinate covariance of \(2\mathbb E[Z_0^2]\Pr(\text{no position reset})=2Me^{-bt}\). This addition is absent for distinct independent Brownian drivers. Averaging over the \(n\) diagonal and \(n(n-1)\) off-diagonal terms gives the formula for \(S_n\).

**4. Sharp threshold and spatial non-self-averaging.** Factor out \(e^{-bt}\) and set \(h(t)=V+2H\int_0^t e^{(b-a)s}ds\). Since \(h'(t)=2He^{(b-a)t}>0\), the ratio \(R(t)=h(t)/(h(t)+2M)\) is strictly increasing. If \(a\le b\), then \(h(t)\to\infty\), hence \(R(t)\to1\). If \(a>b\), then \(h(t)\to V+2H/(a-b)\), giving after substitution the displayed rational value. Its strict bounds follow from positivity and the factorization of the denominator-minus-numerator by \((a-b)(a+6b)\); as \(a/b\to\infty\), its limit is \(1/5\), and as \(a/b\downarrow1\), it approaches \(1\). Conditional laws of large numbers imply \(S_n(t)\to Z_t\) almost surely as \(n\to\infty\) for every fixed time. Since \(\operatorname{Var}Z_t=V>0\), macroscopic squared-position fluctuations survive arbitrarily many particles.

## Verification
A standalone symbolic checker evaluates the independent-clocks generator on all required monomials, independently reconstructs the stationary second moment from the medium autocovariance and exponential position-reset age, checks the two-time covariance ODE, the equal-rate limit, the separation of same- and cross-coordinate terms, and the rational limiting ratio. It also passes 72 positive-parameter/lag substitution and positivity comparisons. Run \(\texttt{python3 verification/checker.py}\). The corresponding recorded output is provided. Exact symbolic identities, not finite simulations, establish the theorem. Limits for \(a,b,\Lambda\) equal to zero and infinite-dimensional uniform process convergence are not asserted.

## Relationship to prior work
Santra, Basu and Sabhapandit (2022, first publicly available 1 May 2022) studied the same stochastic Brownian diffusivity under a **single common Poisson clock resetting both positions and diffusivity**. Their paper gives stationary position distributions and their temporal approach; its common-clock results do not cover independent clocks with two freely varying positive reset rates. The present result treats precisely that different resetting protocol and classifies an observable temporal memory ratio. Related published work studies two-time observables in ordinary fixed-diffusivity resetting and equal-time spatial correlations under unreset common stochastic diffusivity. Neither gives this two-clock result. Prior stationary correlation identities for the synchronous protocol are acknowledged as mathematically different, not incorporated as new discoveries. A broader prior-work search has residual priority uncertainty, especially for hidden-medium resetting models.

## Limitations
The clocks are independent Poisson processes; there is one common position-reset clock and one independent medium-reset clock. The model assumes Brownian diffusivity, independent coordinate Brownian drivers, and infinite stationary history. Different reset-to-nonzero states, individually reset coordinates, non-Poisson waits, drifts, and non-Brownian hidden media are outside the theorem. The equality threshold describes long-lag *relative covariance decay*, not a physical phase transition or positive limiting absolute correlation. No empirical finite-sample identification or independent mathematical audit is claimed.

## References
- I. Santra, U. Basu, S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (1 May 2022), https://arxiv.org/abs/2205.00549.
- M. Mesquita, S. N. Majumdar, S. Sabhapandit, *Dynamically emergent correlations in a Brownian gas with diffusing diffusivity*, arXiv:2506.20859 (2025), https://arxiv.org/abs/2506.20859.
- V. Stojkoski et al., *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686 (2021), https://arxiv.org/abs/2107.11686.
