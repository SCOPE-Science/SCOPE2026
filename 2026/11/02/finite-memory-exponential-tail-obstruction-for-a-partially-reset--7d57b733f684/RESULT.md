# Finite-memory exponential-tail obstruction for a partially reset viscoelastic probe

## Finding

Consider the two-coordinate viscoelastic probe model of Santra and Das, with an independent Poisson clock of rate \(r>0\) resetting only the probe to zero. For every **finite** bath-friction ratio \(g>0\), its unique stationary law \(\pi_{r,g}\) has a probe coordinate \(X\) with the two rigorously established properties
\[
\mathbb E_{\pi_{r,g}}e^{sX}=+\infty\quad\text{for every real } |s|\geq\sqrt{r(g+1)},
\]
\[
\liminf_{z\to\infty}\frac1z\log\mathbb P_{\pi_{r,g}}(X>z)
\geq-\sqrt{r(g+1)}.
\]
The analogous left-tail bound holds by symmetry. In particular,
\[
\lim_{z\to\infty}\frac{-\log\mathbb P_{\pi_{r,g}}(|X|>z)}{z^2}=0.
\]
Thus no finite memory parameter gives an asymptotically Gaussian stationary far tail. The known quasistatic **comparison mixture**, obtained by treating the bath as frozen before the long-distance limit, has instead the strictly positive Gaussian logarithmic tail coefficient \(r/[2(2r+1)]\). This supplies an explicit obstruction to extrapolating that quasistatic law uniformly into arbitrarily remote spatial tails. It does **not** assert an exact finite-\(g\) exponential rate or prove convergence of the finite-\(g\) stationary law to the quasistatic mixture.

## Assumptions and scope

Let \(r,g\) be arbitrary fixed positive real numbers. Between reset events, let \(W\) and \(B\) be independent standard one-dimensional Brownian motions and let
\[
 dX_t=(Q_t-X_t)\,dt+\sqrt 2\,dW_t,\qquad
 dQ_t=\frac{X_t-Q_t}{g}\,dt+\sqrt{\frac2g}\,dB_t.
\]
At the times of an independent, homogeneous rate-\(r\) Poisson process, the update is \((X,Q)\mapsto(0,Q)\). The clock and the two noises are mutually independent. All quantities are in the dimensionless convention of the motivating paper, so the Brownian generators are \(\partial_{xx}\) and \(g^{-1}\partial_{qq}\). The stationary law is defined on \(\mathbb R^2\), and the tail results concern its probe marginal.

For comparison only, define the separate quasistatic Gaussian mixture \(\nu_r\) by
\[
 \nu_r(dx)=\left[\int_0^\infty re^{-ra}\frac{\exp(-x^2/[2\sigma_r^2(a)])}{\sqrt{2\pi\sigma_r^2(a)}}\,da\right]dx,
 \qquad \sigma_r^2(a)=1-e^{-2a}+\frac{1+r}{r}(1-e^{-a})^2.
\]
This is the bath-frozen limiting expression in Eq. (28) of Santra and Das, not a formula for the stationary finite-\(g\) marginal.

## Proof

**1. Stationarity and centering.** The diffusion has a globally Lipschitz drift and nondegenerate Brownian covariance. Its jump rate is finite and its reset map is continuous. For the quadratic function \(V(x,q)=x^2+gq^2\), the full generator gives the exact identity
\[
 {\cal L}V(x,q)=4-2(x-q)^2-rx^2.
\]
The negative quadratic form is positive definite for \(r>0\). Hence \({\cal L}V\le4-cV\) for some \(c=c(r,g)>0\). Standard Foster–Lyapunov existence, together with irreducibility and strong Feller smoothing from the nondegenerate diffusion on any no-reset interval, yields a unique invariant probability law with finite second moment. Stationary first-moment balance gives \(0=-(1+r)\mathbb E X+\mathbb E Q\) and \(0=(\mathbb E X-\mathbb E Q)/g\); therefore \(\mathbb E X=\mathbb E Q=0\). Invariance under simultaneous sign inversion and uniqueness imply that the probe marginal is symmetric.

**2. Exact last-reset kernel.** Put \(\lambda=1+1/g\). Starting a reset-free evolution at \((X_0,Q_0)=(0,q)\), diagonalization of the linear drift gives
\[
 X_a=b_g(a)q+\xi_a,\qquad
 b_g(a)=\frac{g}{g+1}(1-e^{-\lambda a}),
\]
where \(\xi_a\) is centered Gaussian, independent of \(q\), with variance
\[
 v_g(a)=\frac{2a}{g+1}+\frac{g^2}{(g+1)^2}(1-e^{-2\lambda a}).
\]
Indeed, the two noise kernels in the probe coordinate are \([1+ge^{-\lambda u}]/(g+1)\) and \(g[1-e^{-\lambda u}]/(g+1)\) for the probe and bath Brownian increments, respectively. Itô isometry yields \(v_g\) exactly. In particular, \(0\le b_g(a)<1\) and \(v_g(a)=2a/(g+1)+O(1)\) as \(a\to\infty\).

Let \(\mu_Q\) be the stationary bath marginal. State-independent Poisson arrival times sample this marginal; since the forward interarrival interval is independent of the pre-reset state, the stationary elapsed age is exponential and independent of the bath coordinate at the last reset. Thus, for every nonnegative measurable probe test function \(h\),
\[
 \mathbb E_{\pi_{r,g}}h(X)
 =\int_0^\infty re^{-ra}\int_{\mathbb R}\mu_Q(dq)\,
  \mathbb E\bigl[h(b_g(a)q+\sqrt{v_g(a)}Z)\bigr]da,
\]
where \(Z\) is a standard normal independent of the other variables. This is a last-reset conditioning identity; **it does not reset or discard the bath memory**.

**3. Divergence of exponential moments.** Apply the nonnegative test function \(h(x)=e^{sx}\) and Tonelli's theorem. For every real \(s\), possibly with value \(+\infty\),
\[
 \mathbb E_{\pi_{r,g}}e^{sX}=
 \int_0^\infty re^{-ra+s^2v_g(a)/2}
 \mathbb E_{\mu_Q}[e^{sb_g(a)Q}]\,da.
\]
Because \(\mathbb E Q=0\), Jensen's inequality makes the final expectation at least one (even when it is infinite). Also \(v_g(a)\ge2a/(g+1)\). Therefore
\[
 \mathbb E_{\pi_{r,g}}e^{sX}
 \ge r\int_0^\infty\exp\bigl(-(r-s^2/(g+1))a\bigr)da.
\]
The integral diverges at equality and beyond, proving the stated exponential-moment obstruction without assuming any exponential moments of the bath marginal.

**4. Quantified tail lower bound.** Select \(K<\infty\) such that \(p:=\mu_Q([-K,K])>0\). The preceding kernel implies, for all \(z>0\),
\[
 \mathbb P_{\pi_{r,g}}(X>z)
 \ge p\int_0^\infty re^{-ra}\,
 \overline\Phi\left(\frac{z+K}{\sqrt{v_g(a)}}\right)da,
\]
where \(\overline\Phi\) is the standard normal upper tail. Restrict the integral to \(a\in[cz,cz+1]\) for an arbitrary fixed \(c>0\). As \(z\to\infty\), Gaussian tail asymptotics and \(v_g(cz)=2cz/(g+1)+O(1)\) give
\[
 \liminf_{z\to\infty}\frac1z\log\mathbb P(X>z)
 \ge-rc-\frac{g+1}{4c}.
\]
Minimizing the right-hand cost over positive \(c\), with \(c=\tfrac12\sqrt{(g+1)/r}\), yields \(-\sqrt{r(g+1)}\). The same bound applies to the left tail by sign symmetry. Since probabilities do not exceed one, the claimed zero quadratic logarithmic tail coefficient follows by squeezing.

**5. Quasistatic comparator.** The variance \(\sigma_r^2(a)\) in the separately defined Gaussian mixture is continuous and strictly increasing, with supremum \(\sigma_\infty^2=(2r+1)/r\). Bounding each Gaussian tail from above by a normal tail of variance \(\sigma_\infty^2\), and bounding from below by restricting ages to any interval where \(\sigma_r^2(a)\) is within an arbitrarily small tolerance of its supremum, proves
\[
 \lim_{z\to\infty}\frac{-\log\nu_r(|x|>z)}{z^2}
 =\frac1{2\sigma_\infty^2}=\frac{r}{2(2r+1)}>0.
\]
The comparison is between the exact finite-\(g\) law and an explicitly defined quasistatic expression; convergence of the finite-\(g\) stationary law as \(g\to\infty\) is not needed for, and not established by, the main theorem.

## Verification

A standalone symbolic checker, `checks/check_kernel.py`, verifies the generator's quadratic Lyapunov identity, the exact no-reset Gaussian kernel and variance derivative, the optimization constant, and the limiting variance of the quasistatic mixture. It also performs several finite-parameter consistency checks. The infinite-distance limits and invariant-law arguments are proved above and do not depend on numerical experiments.

## Relationship to prior work

Santra and Das (2026, arXiv:2603.17027v1) introduced this coupled probe–bath resetting model, derived stationary moments, and obtained a Gaussian mixture in a strong-memory quasistatic approximation. Their Eq. (7) provides the no-reset covariance used here, and Eq. (28) is the comparison mixture. The contribution established here is the **finite-bath-memory, arbitrary-distance** exponential-moment obstruction, a quantitative one-sided tail lower bound with its rate, and the resulting failure of a uniform Gaussian far-tail approximation. No new Gaussian-mixture formula, stationary second-moment calculation, or exact finite-\(g\) tail exponent is claimed. Earlier interacting two-particle resetting models such as Falcao and Evans (2016) use collision-triggered resetting of both particles rather than retention of one Brownian bath coordinate.

## Limitations

The tail bound is one-sided in strength: it supplies a lower bound on the probability of far excursions, **not** a matching upper bound or an exact exponential decay rate. The moment result proves divergence beyond a specified threshold but does **not** prove finiteness below it. The strict Gaussian quadratic coefficient concerns the separately defined quasistatic mixture and not a rigorously established interchange of the finite-\(g\) stationary and frozen-bath limits. The proof assumes a single linear Gaussian bath coordinate, positive finite \(g\), thermal noise in both coordinates, position-only Poisson resetting, and full-space stationary dynamics. It does not treat finite-speed returns, multiple baths, or nonlinear couplings.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1 (first posted 2026-03-17), sections II–III, Eqs. (2), (7), (11), (28), https://arxiv.org/abs/2603.17027 .
2. R. Falcao and M. R. Evans, *Interacting Brownian Motion with Resetting*, arXiv:1610.03503v1 (2016), https://arxiv.org/abs/1610.03503 .
