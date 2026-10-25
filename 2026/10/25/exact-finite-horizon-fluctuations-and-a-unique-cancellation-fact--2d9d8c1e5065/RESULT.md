# Exact finite-horizon fluctuations and a unique cancellation factor for quadratic partial-reset losses

## Finding
Let \(X_t\) be stationary Brownian diffusion with diffusivity \(D>0\) and independent Poissonian proportional resets \(X_{\tau}=qX_{\tau-}\), of rate \(r>0\), where \(0\le q<1\). For stiffness parameter \(\kappa>0\), define the accumulated quadratic contraction loss
\[
L_T=\frac{\kappa(1-q^2)}{2}\sum_{0<\tau_j\le T}X_{\tau_j-}^2,
\qquad k=r(1-q^2).
\]
For every \(T\ge0\), its mean and variance are exactly
\[
\mathbb E L_T=\kappa DT,\qquad
\operatorname{Var}(L_T)=\frac{4\kappa^2D^2}{k}T+
\frac{2\kappa^2D^2(1-5q^2)}{k^2(1+q^2)}(1-e^{-kT}).
\]
Consequently, the variance is **exactly linear throughout the entire observation horizon**, rather than merely asymptotically linear, if and only if \(q=1/\sqrt5\). At that value \(\operatorname{Var}(L_T)=5\kappa^2D^2T/r\). For \(0\le q<1/\sqrt5\) the finite-horizon variance exceeds the limiting linear extrapolation; for \(1/\sqrt5<q<1\) it lies strictly below it for each \(T>0\).

The asymptotic Gaussian regime nevertheless coexists with the absence of all positive exponential moments:
\[
\frac{L_T-\kappa DT}{\sqrt T}\Longrightarrow
N\!\left(0,\frac{4\kappa^2D^2}{r(1-q^2)}\right)
\quad(T\to\infty),
\qquad \mathbb E e^{\theta L_T}=\infty
\quad(T>0,\ \theta>0).
\]

## Assumptions and scope
The process is defined on the real line by \(dX_t=\sqrt{2D}\,dB_t\) between points of an independent rate-\(r\) Poisson process; at each point, position is multiplied by \(q\). At time zero the process has its unique stationary law, independent of future Brownian and Poisson increments. The limiting case \(q=0\) is full instantaneous resetting to the origin; \(q=1\) is excluded. The coefficient \(\kappa\) sets the energy scale. \(L_T\) is the sum of instantaneous decreases in \(\kappa X^2/2\) at contraction jumps. It is a mathematical loss statistic, not by itself a general formula for thermodynamic work in a laboratory protocol with finite-duration trap-return phases or for entropy production. No reset of the clock occurs when \(L_T\) is observed.

## Proof
**Stationary moments and uniqueness.** The scalar generator is
\[
\mathcal G f(x)=Df''(x)+r[f(qx)-f(x)].
\]
The synchronous coupling of two trajectories using the same noises gives \(X_t-Y_t=q^{N_t}(X_0-Y_0)\), tending to zero almost surely. An invariant law exists by summing independent, geometrically contracted Brownian excursions backward from the Poisson clock. Its finite moments satisfy, from \(\mathbb E\mathcal G X^2=\mathbb E\mathcal G X^4=0\),
\[
m_2=\mathbb E X^2=\frac{2D}{k},\qquad
m_4=\mathbb E X^4=\frac{24D^2}{k^2(1+q^2)}.
\]
The moment equation for \(X^4\) is \(0=12Dm_2-r(1-q^4)m_4\).

**Joint polynomial dynamics.** Write \(c=\kappa(1-q^2)/2\) and \(Y_t=L_t\). The joint generator is
\[
\mathcal Hf(x,y)=D\partial_{xx}f(x,y)+r[f(qx,y+cx^2)-f(x,y)].
\]
Let \(m(T)=\mathbb E Y_T\), \(h(T)=\mathbb E(Y_TX_T^2)\), and \(j(T)=\mathbb E Y_T^2\). Direct application to \(y,yx^2,y^2\) gives
\[
\begin{split}
m'(T)&=rcm_2=\kappa D,\\
h'(T)&=2Dm(T)-kh(T)+rcq^2m_4,\\
j'(T)&=2rc\,h(T)+rc^2m_4,
\end{split}
\]
with \(m(0)=h(0)=j(0)=0\). Solving the second linear equation using \(m(T)=\kappa DT\), then integrating the third and subtracting \(m(T)^2\), gives the displayed variance. Alternatively, its derivative simplifies to
\[
\frac{d}{dT}\operatorname{Var}(L_T)=
\frac{4\kappa^2D^2}{k}+
\frac{2\kappa^2D^2(1-5q^2)}{k(1+q^2)}e^{-kT}.
\]
The coefficient of \(1-e^{-kT}\) vanishes exactly when \(q^2=1/5\); for \(T>0\), this factor is strictly positive. This proves uniqueness and both sides of the correction.

**Independent energy identity and central limit law.** Itô's formula with jumps for \(X_t^2\) yields pathwise
\[
L_T-\kappa DT=
\kappa\sqrt{2D}\int_0^T X_s\,dB_s-
\frac{\kappa}{2}(X_T^2-X_0^2).
\]
Synchronous contraction plus stationary construction yields ergodicity. Hence the quadratic variation of the martingale term, divided by \(T\), tends almost surely to \(2\kappa^2D\,m_2=4\kappa^2D^2/k\). Its continuous-martingale central limit theorem gives the normal limit. The stationary fourth moment makes \(X_T^2-X_0^2\) uniformly bounded in \(L^2\), so its contribution divided by \(\sqrt T\) vanishes in probability.

**No positive exponential moment.** In the stationary renewal representation, \(X_0\) contains an independent nondegenerate bilateral exponential (Laplace) summand (the Brownian displacement over the latest exponential interarrival), plus an independent remaining random variable. The Laplace summand has positive mass density proportional to \(e^{-c_0|x|}\) for some \(c_0>0\). For any real independent noise \(W\), any \(a>0\), and any \(\theta>0\), \(\mathbb E\exp[\theta a(Z+W)^2]=\infty\), by conditioning on \(W\) and integrating against the Laplace density. On the positive-probability event of exactly one Poisson reset in \((0,T]\), the loss is \(c(X_0+\sqrt{2D}B_{\tau})^2\), with \(\tau\) independent of \(X_0\) and \(B\), and \(c>0\). Conditioning on \(\tau\) proves \(\mathbb E e^{\theta L_T}=\infty\).

## Verification
The standalone file `work_variance_checker.py` uses an independently assembled six-dimensional polynomial-generator matrix to evolve \(1,\mathbb EX^2,\mathbb EX^4,\mathbb EL_T,\mathbb E[L_TX_T^2],\mathbb EL_T^2\). Its matrix exponential is compared with the asserted exact mean and variance over 648 positive-parameter and boundary-parameter test combinations, and with the independent Itô-energy covariance evaluation. A run with NumPy, SciPy and SymPy returned `PASS: 648 independent-generator cases, 3889 checks`. Such finite computations support algebraic reproducibility but are not the proof of all-parameter statements or the infinite-time limit.

## Relationship to prior work
Tal-Friedman, Roichman and Reuveni [1] introduce this proportional-reset diffusion and obtain its stationary law and stationary moments; those ingredients are credited, not claimed novel. Olsen and Gupta [2] examine thermodynamic work during finite-duration returning phases after proportional resetting and identify mean work-rate insensitivity; their physical work is not generally identical as a time-parametrized process to the instantaneous quadratic jump-loss statistic here. The present assertion concerns the exact finite-horizon variance and its unique \(q=1/\sqrt5\) cancellation, plus the coexistence of its large-time central limit law and divergent positive exponential moments. Gupta, Plata and Pal [3], and Gupta and Plata [4], study work fluctuations for resetting/return-to-origin protocols rather than this contracted-jump observable. Generic additive-functional central limit ideas and Gaussian-chaos tails are not claimed as new independently of this exact model-specific result.

## Limitations
This is a fixed-parameter stationary, one-dimensional, instantaneous-jump theorem. It does not establish a fluctuation theorem, nonstationary initial-condition universality, finite-time physical trap-work statistics when returns take nonzero durations, a large-deviation principle, or any optimal laboratory protocol. The \(q\to1\) limit is singular and is not interchangeable with fixed-\(q\) large-time asymptotics. The exact cancellation factor is an observable-specific characterization. Similar calculations may be implicit in more general affine jump-diffusion additive-functional theory; independent literature priority verification is warranted.

## References
1. N. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (first posted 2022-05-06), https://arxiv.org/abs/2205.03363 .
2. K. S. Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919 (first posted 2024-01-22), https://arxiv.org/abs/2401.11919 .
3. D. Gupta, C. A. Plata and A. Pal, *Work fluctuations and Jarzynski equality in stochastic resetting*, arXiv:1909.08512 (2019), https://arxiv.org/abs/1909.08512 .
4. D. Gupta and C. A. Plata, *Work fluctuations for diffusion dynamics submitted to stochastic return*, arXiv:2206.07618 (2022), https://arxiv.org/abs/2206.07618 .
5. K. S. Olsen et al., *Thermodynamic cost of finite-time stochastic resetting*, arXiv:2310.11267 (2023), https://arxiv.org/abs/2310.11267 .
