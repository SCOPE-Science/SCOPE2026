# Refractory-time variance is identifiable through integrated fluctuations under partial Brownian resetting

## Finding

Consider a partially reset Brownian particle alternating between Brownian exploration and frozen refractory periods. When the reset contraction is strictly partial, the stationary **one-time position distribution** depends on the refractory-time law only through its mean. In contrast, the **long-time variance per unit time of the integrated position** determines its refractory-time variance exactly. This yields a sharp ordering of all clocks having the same mean: deterministic refractory periods uniquely minimize integrated-position fluctuations, and no finite maximum exists.

Precisely, let \(0<a<1\), \(r>0\), \(D>0\), and let the independent, identically distributed refractory periods \(R_i>0\) have \(h=\mathbb E R_i\in(0,\infty)\), \(v=\operatorname{Var}(R_i)\in[0,\infty)\), and \(\mathbb E[R_i^4]<\infty\). For the stationary position process \(X_t\), define

\[
\Gamma=\lim_{T\to\infty}\frac{1}{T}\operatorname{Var}\left(\int_0^T X_t\,dt\right).
\]

The limit exists and satisfies the **exact identity**

\[
\boxed{\displaystyle
\Gamma=\frac{2D\left[2+2a(1+a)rh+a^2(1+a)(rh)^2\right]}{r^2(1-a)^2(1+a)(1+rh)}
+\frac{2Da^2}{(1-a^2)(1+rh)}\,v.}
\]

Furthermore, with the same normalization,

\[
T^{-1/2}\int_0^T X_t\,dt\;\Longrightarrow\;\mathcal N(0,\Gamma).
\]

For fixed \((a,r,D,h)\), the set of all possible \(\Gamma\) over the stated refractory laws is exactly \([\Gamma(h,0),\infty)\). The unique minimizing **law** is \(R_i=h\) almost surely. The single number \(\Gamma\) identifies the otherwise invisible clock variance by

\[
\boxed{\displaystyle v=\frac{(1-a^2)(1+rh)}{2Da^2}\bigl[\Gamma-\Gamma(h,0)\bigr].}
\]

For example, at \(D=r=h=1\), \(a=1/2\), deterministic refractoriness gives \(\Gamma=31/3\), whereas exponential refractoriness of the **same mean** gives \(\Gamma=32/3\), although the stationary one-time position densities agree exactly.

## Assumptions and scope

On the real line, exploration follows \(dX_t=\sqrt{2D}\,dW_t\). Independent exploration lengths \(E_i\) have exponential law of rate \(r\). At the end of an exploration period, the particle jumps \(X\mapsto aX\), freezes at the resulting location for an independent duration \(R_i\), then begins the next Brownian exploration. All exploration clocks, Brownian increments and refractory lengths are independent across cycles. The refractory distribution is strictly positive, has finite positive mean, and has finite fourth moment; no density or memoryless property is assumed. The process is observed in its unique stationary regime, though the limiting fluctuation coefficient is independent of any finite-variance initial position.

The assertion concerns the signed path integral of **position**, not first-passage times, occupation above a target, the time integral of squared displacement, or a nonfrozen refractory phase. The open restriction \(0<a<1\) is necessary for strict clock-variance identifiability: the coefficient of \(v\) vanishes at complete resetting \(a=0\).

## Proof

**1. Stationary cycle endpoints.** Index complete exploration-plus-refractory cycles and denote the position at the beginning of exploration \(i\) by \(Y_i\). Let \(B_i=\sqrt{2D}\,W_i(E_i)\). Independent cycles satisfy

\[
Y_{i+1}=a(Y_i+B_i),\qquad \mathbb E B_i^2=\frac{2D}{r}.
\]

This contracting random affine recursion has a unique stationary centered, finite-fourth-moment solution. Its variance is

\[
V:=\mathbb E Y_i^2=\frac{2Da^2}{r(1-a^2)}.
\]

The cycle length is \(C_i=E_i+R_i\), with \(\mathbb E C_i=1/r+h\).

**2. Exactly integrated cycle reward.** Put \(J_i=\sqrt{2D}\int_0^{E_i}W_i(s)\,ds\). Since the refractory position is \(a(Y_i+B_i)\), the exact area accumulated in one cycle is

\[
I_i=\int_{\text{cycle }i}X_t\,dt=(E_i+aR_i)Y_i+J_i+aR_iB_i.
\]

The Brownian/exponential moment identities (obtained by conditioning on the length \(E_i\)) are

\[
\mathbb E J_i^2=\frac{4D}{r^3},\quad
\mathbb E(J_iB_i)=\frac{2D}{r^2},\quad
\mathbb E B_i^2=\frac{2D}{r}.
\]

**3. A martingale correction for cross-cycle memory.** Define

\[
c=\frac1r+ah,\qquad k=\frac{ac}{1-a},\qquad
M_i=I_i+\frac{c}{1-a}(Y_{i+1}-Y_i).
\]

The endpoint recursion simplifies this to

\[
M_i=(E_i+aR_i-c)Y_i+J_i+(aR_i+k)B_i.
\]

With respect to the sigma-field of completed preceding cycles, \(\mathbb E[M_i\mid\mathcal F_i]=0\): the future clock and noise are independent, the coefficient of \(Y_i\) has mean zero, and the Brownian terms have conditional mean zero. Thus the \(M_i\) are stationary ergodic square-integrable martingale differences, and their cross-cycle covariances vanish **exactly**. Telescoping the correction shows that the sum of cycle areas and the sum of martingale differences differ only by an endpoint multiple of \(Y_n-Y_0\), which is negligible at the \(\sqrt T\) scale.

Independence, centering and the displayed moments give

\[
\begin{aligned}
\mathbb E M_i^2={}&V\left(\frac1{r^2}+a^2v\right)+\frac{4D}{r^3}
+\frac{4D}{r^2}(ah+k)\\
&+\frac{2D}{r}\left[a^2v+(ah+k)^2\right].
\end{aligned}
\]

This identity uses the **variance** of the refractory durations, not their third or fourth moments. Those higher moments are required only for the limit argument.

**4. Passage from cycles to physical time.** The cycle durations are independent identically distributed with finite fourth moments, while the endpoint chain is contractive and geometrically mixing. Its stationary ergodic martingale-difference sequence obeys the martingale functional central limit theorem. The cycle-count renewal law gives \(N(T)/T\to(1/r+h)^{-1}\). Use the **first completed cycle after** the observation time as the stopping index, so that optional martingale stopping and quadratic-variation identities apply. The extra terminal-cycle reward, the unfinished-time segment and the telescoped endpoint correction have bounded second moments on the renewal scale and hence are \(o(T)\) in their contributions to total variance and \(o_{\mathbb P}(\sqrt T)\) in the central-limit normalization. This follows from the exponential exploration tails, \(\mathbb E R_i^4<\infty\), and the contractive endpoint recursion; the nonlattice exponential component provides ordinary renewal convergence. The martingale isometry, ergodic theorem and uniform integrability then identify both the physical-time variance rate and CLT variance as

\[
\Gamma=\frac{\mathbb E M_i^2}{1/r+h}.
\]

Substitution of \(V\), \(c\) and \(k\), followed by rational simplification, yields the boxed formula in the Finding section. In particular

\[
\frac{\partial\Gamma}{\partial v}=\frac{2Da^2}{(1-a^2)(1+rh)}>0.
\]

**5. Same stationary snapshot; all fluctuation values.** A stationary observer is exploring with probability \((1+rh)^{-1}\) and frozen with probability \(rh/(1+rh)\). Conditional on exploring, position is distributed as \(Y+B_E\), with an independent exponentially distributed age of rate \(r\); conditional on being frozen, position is distributed as \(Y\). These laws and weights depend only on \((a,r,D,h)\), not on \(v\). Therefore all positive refractory laws sharing mean \(h\) produce the **same** stationary positional distribution.

Every finite \(v\ge0\) is attainable: for \(v=0\) take \(R=h\); for \(v>0\), fix \(0<\epsilon<h\) and take the strictly positive two-point law

\[
\mathbb P(R=h-\epsilon)=\frac{v}{v+\epsilon^2},\qquad
\mathbb P(R=h+v/\epsilon)=\frac{\epsilon^2}{v+\epsilon^2}.
\]

Its mean is \(h\), its variance is \(v\), and it has finite support. Since \(\Gamma\) is strictly affine in \(v\), this proves the exact half-line range, uniqueness of the deterministic minimizing law, and the inverse identification formula. No finite maximum exists.

## Verification

The standalone file `verify.py` reproduces the stationary endpoint variance, cycle-reward martingale variance, symbolic simplification, and the exact derivative with respect to clock variance using SymPy. As an **independent analytic check for exponential refractory times**, it solves the two-phase Markov-Poisson equation and verifies agreement with the cycle formula. It also checks the complete-reset limit.

Nine independently sampled cycle-martingale tests (three parameter sets, deterministic/exponential/two-point refractory laws, 650,000 cycles each) yielded relative discrepancies below \(0.7\%\). A separate compiled simulator integrates the actual position trajectory up to fixed physical time, **including the unfinished final phase**, for 2,400 replicas per refractory law at horizon 4,000; deviations from predicted variance rates were \(1.21\%\), \(1.04\%\), and \(0.56\%\). The analytic argument, not the finite Monte Carlo sample, establishes the theorem for all admissible laws.

Run with `python verify.py` after installing Python 3, NumPy, SymPy, and optionally Numba (the physical-time tests run when Numba is available). No third-party datasets are required.

## Relationship to prior work

Olsen and Löwen (arXiv:2406.10039v1, 2024) introduce **exactly** this partial-reset/frozen-refractory model and derive its time-dependent one-time propagator, stationary subpopulation characteristic functions (their equations (30)–(33)), and stationary spatial cumulants. In particular, the one-time law's dependence solely on mean refractory time is **prior work**. Those one-time formulas do not give the long-time variance of a path integral, its strict clock-variance coefficient, or the inversion and exact fixed-mean optimum established here.

Di Bello, Chechkin, Hartmann, Palmowski and Metzler (arXiv:2305.13722, 2023) analyze time-dependent one-time densities for partial resetting **without** frozen refractory intervals. García-Valladares, Gupta, Prados and Plata (arXiv:2310.19913, 2023) treat alternating exploration and refractory phases under **complete** resetting to a fixed location, including first-passage observables. Olsen and Löwen (arXiv:2401.12685, 2024) use a distinct sense of partial resetting: a hidden **velocity** is reset while the observed **position** is not; their refractory-time-dependent transport coefficient is a different observable. Singh and Pal (arXiv:2202.02715, 2022) investigate additive Brownian functionals stopped at first passage, also a different observable. General renewal-reward and martingale techniques are classical and are not claimed as new. The claimed advance is the exact observation-level distinction between clock laws, the positive partial-reset variance penalty, and complete sharp ordering within this physical model.

## Limitations

The theorem assumes an independent renewal refractory clock, an exponential exploration clock, complete immobility during pauses, identical reset fraction \(0<a<1\), and finite fourth refractory moment. It does not identify the **full** refractory law from \(\Gamma\): only its variance is identified once \(a,r,D,h\) are given. Higher-order temporal measurements would be needed to separate laws sharing mean and variance. A generic Markov-additive theorem may provide an alternative proof or imply portions of the asymptotics; priority among implicit general results has not been independently adjudicated. The finite numerical experiments verify finite cases but do not certify a continuum of parameter choices.

## References

1. K. Stølevik Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (public 2024-06-14), https://arxiv.org/abs/2406.10039 . Full lawful text was compared, including its stationary equations and discussion.
2. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722 (2023), https://arxiv.org/abs/2305.13722 .
3. G. García-Valladares, D. Gupta, A. Prados and C. A. Plata, *Stochastic resetting with refractory periods: pathway formulation and exact results*, arXiv:2310.19913 (2023), https://arxiv.org/abs/2310.19913 .
4. Tal-Friedman and collaborators, *Diffusion with Partial Resetting*, arXiv:2205.03363 (2022), https://arxiv.org/abs/2205.03363 .
5. K. Stølevik Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (2024), https://arxiv.org/abs/2401.12685 .
6. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715 (2022), https://arxiv.org/abs/2202.02715 .
