# A common sharp exponential-tail scale for a selectively reset viscoelastic Brownian pair

## Finding

Fix a bath-friction ratio \(\gamma>0\) and a Poisson-reset rate \(r>0\). Let independent standard Brownian motions drive the dimensionless two-coordinate model
\[
\mathrm dX_t=(Q_t-X_t)\,\mathrm dt+\sqrt2\,\mathrm dB_t,
\qquad
\mathrm dQ_t=(X_t-Q_t)\,\mathrm dt/\gamma+\sqrt{2/\gamma}\,\mathrm dW_t.
\]
At each independent rate-\(r\) Poisson event, only \(X\) is replaced by zero; \(Q\) is unchanged. In its unique stationary distribution, **both** the reset probe and the unreset bath coordinate have the *same exact exponential-moment boundary*
\[
\boxed{\quad
\mathbb E e^{kX}<\infty\ \Longleftrightarrow\ |k|<\sqrt{r(\gamma+1)},
\qquad
\mathbb E e^{kQ}<\infty\ \Longleftrightarrow\ |k|<\sqrt{r(\gamma+1)}.
\quad}
\]
For either \(Z=X\) or \(Z=Q\), the following logarithmic spatial-tail limit consequently holds, with a matching constructive lower bound:
\[
\boxed{\quad\lim_{x\to\infty}\frac{-\log\mathbb P(|Z|>x)}{x}=\sqrt{r(\gamma+1)}.\quad}
\]
The statements include the moment boundary itself (both moment-generating functions diverge at equality). They concern logarithmic tail rates, **not** an asserted density prefactor or an exact Laplace density. In particular, at every finite \(\gamma>0\) neither stationary marginal has a positive quadratic-exponential moment. The bath-memory-dominated Gaussian-looking profile therefore has a singular far-tail regime at any finite bath-friction ratio.

For the explicit check \(\gamma=1\), \(r=2\), the common tail rate is exactly \(2\), even though the stationary variances are respectively \(\mathbb E X^2=4/5\) and \(\mathbb E Q^2=8/5\).

## Assumptions and scope

The noises are independent; the resetting clock is independent of them and of all past states. Reset events are instantaneous, and the bath coordinate is never explicitly reset. The system is observed under its stationary two-sided law, with the time origin independent of the Poisson clock. Parameters \(r\) and \(\gamma\) are fixed finite positive real numbers. There is no additional confining potential, external drive, correlated noise, or finite-speed return phase. The observables are marginal stationary probabilities for each coordinate, not joint two-coordinate large deviations.

Write \(\lambda=1+\gamma^{-1}\), and for a reset-free flight lasting \(t\geq0\) define
\[
\begin{aligned}
 a(t)&=\frac{\gamma+e^{-\lambda t}}{\gamma+1},
 &h(t)&=\frac{\gamma(1-e^{-\lambda t})}{\gamma+1},\\
 U(t)&=\frac{2(\gamma+1)t+1-e^{-2\lambda t}}{(\gamma+1)^2},
 &V(t)&=\frac{2(\gamma+1)t+\gamma^2(1-e^{-2\lambda t})}{(\gamma+1)^2}.
\end{aligned}
\]
Both variance functions grow as \(2t/(\gamma+1)+O(1)\). All exponentials and expectations refer to the dimensionless coordinates in the displayed stochastic differential equations.

## Proof

**1. Exact between-reset transition.** The deterministic drift matrix is
\[
A=\begin{pmatrix}-1&1\\\gamma^{-1}&-\gamma^{-1}\end{pmatrix},
\qquad A^2=-\lambda A.
\]
Consequently \(e^{At}=I+(1-e^{-\lambda t})A/\lambda\). Starting just after a reset with \((X_0,Q_0)=(0,q)\) gives
\[
X_t=h(t)q+\xi_t,\qquad Q_t=a(t)q+\eta_t,
\]
where \((\xi_t,\eta_t)\) is a centered Gaussian pair, independent of \(q\). Integrating the covariance \(\int_0^t e^{As}\operatorname{diag}(2,2/\gamma)e^{A^Ts}\,\mathrm ds\) gives \(\operatorname{Var}(\xi_t)=V(t)\) and \(\operatorname{Var}(\eta_t)=U(t)\). No independence of \(\xi_t\) and \(\eta_t\) is required.

**2. The embedded unreset-bath chain.** At successive Poisson reset times the bath values form the random affine recursion
\[
Q_{j+1}=a(T_j)Q_j+\sqrt{U(T_j)}G_j,
\]
with independent \(T_j\sim\operatorname{Exp}(r)\), independent standard Gaussians \(G_j\), and independent innovations. For every \(t>0\), \(0<a(t)<1\); moreover \(\mathbb E|\log a(T)|<\infty\), \(\mathbb E\log a(T)<0\), and the Gaussian innovations have finite logarithmic moments. Hence the perpetuity converges and gives a unique symmetric stationary bath law \(\nu\). Sampling the stationary process at independent Poisson epochs yields this same \(\nu\) because the bath is continuous at resets and arrivals are state-independent. Its stationary existence also constructs the stationary continuous-time joint process by choosing an independent exponential time since the last reset.

**3. An exact exponential-moment threshold for the bath.** Put
\[
k_c=\sqrt{r(\gamma+1)}.
\]
The noise moment \(\mathbb E\exp(\theta^2 U(T)/2)\) is finite exactly when \(|\theta|<k_c\), by the displayed linear growth of \(U(t)\). For any \(0<\theta<k_c\), set \(L(q)=\cosh(\theta q)\). The bath transition kernel \(P\) satisfies
\[
(PL)(q)=\mathbb E\left[e^{\theta^2U(T)/2}\cosh(\theta a(T)q)\right].
\]
For each fixed \(T>0\), \(\cosh(\theta a(T)q)/\cosh(\theta q)\to0\) as \(|q|\to\infty\); this ratio is at most one. Dominated convergence applies because the preceding Gaussian-noise moment is finite. Thus \((PL)(q)/L(q)\to0\). There are finite \(R,B\) with \(PL\leq L/2+B\) globally. Iterating from \(Q_0=0\) yields a uniform bound on \(\mathbb E L(Q_j)\), and weak convergence of the perpetuity together with lower semicontinuity yields \(\int L\,\mathrm d\nu<\infty\). Symmetry gives finiteness of \(\mathbb E e^{\theta Q}\) for all \(|\theta|<k_c\).

At and beyond the endpoint, the perpetuity equation and symmetry instead imply
\[
\mathbb E e^{\theta Q}=\mathbb E\left[e^{\theta^2U(T)/2}\cosh(\theta a(T)Q)\right]
\geq\mathbb E e^{\theta^2U(T)/2}=\infty
\qquad(|\theta|\geq k_c).
\]
This implication holds in the extended nonnegative sense and proves the sharp threshold, including boundary divergence.

**4. The reset probe has precisely the same threshold.** In stationary time, the age \(T\) since the preceding Poisson reset is \(\operatorname{Exp}(r)\) and is independent of the bath value \(Q_0\sim\nu\) at that reset and of subsequent driving noises. With \(H(u)=\mathbb E e^{uQ_0}\), conditioning on \(T\) gives the exact identity, in the extended sense,
\[
\mathbb E e^{kX}=r\int_0^\infty e^{-rt+k^2V(t)/2}H(kh(t))\,\mathrm dt.
\]
For \(|k|<k_c\), the inequality \(|h(t)|\leq\gamma/(\gamma+1)<1\) bounds the bath factor by the finite constant \(H(|k|\gamma/(\gamma+1))\). The remaining integral converges because the exponent has asymptotic linear slope \(-r+k^2/(\gamma+1)<0\). If \(|k|\geq k_c\), symmetry gives \(H(kh(t))\geq1\), and that integral diverges since the asymptotic slope is nonnegative. This proves the exact probe boundary.

**5. Exact logarithmic tail limits.** For either stationary marginal \(Z\) and any \(0<k<k_c\), Chernoff's bound gives \(\mathbb P(Z>x)\leq\mathbb E e^{kZ}e^{-kx}\). Thus the lower bound on the logarithmic decay rate is \(k_c\). For the reverse bound, choose \(B>0\) with \(\nu([-B,B])>0\), and restrict the stationary last-reset age to
\[
t_x\leq T\leq t_x+1,\qquad t_x=\frac{x}{2}\sqrt{\frac{\gamma+1}{r}}.
\]
On this event, both conditional Gaussian means \(h(T)Q_0\) and \(a(T)Q_0\) lie within \([-B,B]\), and both conditional variances equal \(2T/(\gamma+1)+O(1)\). The probability of the age event is \(\exp(-rt_x+O(1))\), while a standard Gaussian tail estimate yields a conditional right-tail logarithm at least \(-(x+B)^2/(2[2t_x/(\gamma+1)+O(1)])+O(\log x)\). Summing the two costs gives \(-k_c x+o(x)\). Thus \(\liminf_{x\to\infty}x^{-1}\log\mathbb P(Z>x)\geq-k_c\). Combining with Chernoff establishes \(\lim_{x\to\infty}x^{-1}\log\mathbb P(Z>x)=-k_c\). The stationary laws are symmetric, so replacing the one-sided probability by \(\mathbb P(|Z|>x)\) leaves the exponent unchanged. Finally, any positive Gaussian-type moment \(\mathbb E e^{cZ^2}\) would entail all linear exponential moments through \(k|Z|\leq cZ^2+k^2/(4c)\), contradicting the finite cutoff.

## Verification

Run `python verify_tail.py` with Python 3, NumPy and SciPy. The verifier independently checks the two-by-two semigroup by matrix exponentiation, obtains both noise variances by direct numerical integration of the diffusion covariance, solves the three stationary second-moment equations, independently reconstructs the bath variance from its affine-reset recursion, and cross-checks the probe variance by exponential-age mixing. It also verifies the critical Gaussian-weight slopes and the large-displacement saddlepoint cost for several parameter values. The current package verifier passed 387 deterministic checks. These are finite consistency tests; the assertions for every real parameter and the infinite-tail limit are proved in the preceding steps.

The transparent exact check \(\gamma=1\), \(r=2\) has \(k_c=2\), \(V(t)=U(t)=t+(1-e^{-4t})/4\), stationary covariances \(\mathbb E[X^2]=4/5\), \(\mathbb E[XQ]=3/5\), and \(\mathbb E[Q^2]=8/5\). They can be obtained directly from the linear moment equations without using any simulation.

## Relationship to prior work

Santra and Das, arXiv:2603.17027v1, introduce the same two-coordinate selective-reset model and derive the finite-parameter variance, a fourth-moment expression and large-\(\gamma\) quasistatic Gaussian-mixture approximation (especially Secs. II–III and Appendix A). The asymptotic Gaussian profile discussed there is in the strong-memory regime; it does not provide the exact far-tail moment boundary for every **fixed finite** \(\gamma\). The theorem here extracts a nonuniform finite-\(\gamma\) extreme-tail law, not a new physical model, covariance or kurtosis formula.

Biswas, Dubbeldam, Sandev and Pal (arXiv:2412.09260; Sec. III) study a generalized-Langevin resetting model in which the *entire* memory state is renewed at resets, supporting ordinary renewal equations. That is a different mechanism: the retained bath here is an autoregressive mark and its exponential integrability needs its own proof. Tal-Friedman, Roichman and Reuveni (arXiv:2205.03363; Sec. II) solve scalar Brownian diffusion with a proportional reset \(x\mapsto ax\); their infinite convolution of Laplace variables provides useful context but does not cover the coupled two-coordinate dynamics or the exact \(\sqrt{r(\gamma+1)}\) boundary. The elementary Brownian-reset exponential rate \(\sqrt{r/D}\) is well known; its existence does not by itself identify the observed rate for partial bath retention.

## Limitations

This is a *logarithmic* tail result only: no multiplicative asymptotic constant, full large-deviation rate function, crossover displacement scale, exact density formula, or uniformity as \(\gamma\to\infty\) is asserted. The result does not apply to nonlinear baths, state-dependent reset clocks, non-Gaussian forces, correlated driving noises, added confinement, or finite-speed returns. Fixed-parameter exponent \(\sqrt{r(\gamma+1)}\) diverges as \(\gamma\to\infty\); this does not contradict a Gaussian-looking quasistatic profile on fixed or experimentally accessible displacement ranges. No independent literature-priority audit has been carried out.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1, first publicly submitted 2026-03-17, https://arxiv.org/html/2603.17027v1 .
2. A. Biswas, J. L. A. Dubbeldam, T. Sandev and A. Pal, *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260, first publicly submitted 2024-12-12, https://arxiv.org/abs/2412.09260 .
3. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with partial resetting*, Physical Review E 106, 054116 (2022), https://arxiv.org/abs/2205.03363 .
4. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters 106, 160601 (2011), https://doi.org/10.1103/PhysRevLett.106.160601 .
