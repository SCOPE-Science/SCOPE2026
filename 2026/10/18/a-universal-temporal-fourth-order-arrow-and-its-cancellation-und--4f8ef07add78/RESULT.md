# A universal temporal fourth-order arrow and its cancellation under random-amplitude Brownian resetting

## Finding
For a stationary Brownian particle whose position is multiplied at independent Poisson reset times by an independent, identically distributed real random amplitude, a two-time fourth-order contrast has an **exact, fixed sign for every positive lag**, and that sign is determined by a single moment of the multiplier distribution. Signed contractions always give a strict positive sign. Rare reset overshoots can reverse it, and a nonreversible process can have the contrast identically zero.

Specifically, let \(D,r>0\), let the multiplier \(A\) be real with \(\mathbb E|A|^4<1\), and put \(m_j=\mathbb E[A^j]\), \(\lambda_j=r(1-m_j)\) for \(j=1,2,3,4\). Let \(X\) be the stationary process specified below. For every \(t>0\), define
\[
H(t)=\mathbb E[X_t^3X_0]-\mathbb E[X_tX_0^3],\qquad
F=\mathbb E[(1-A)^3(1+A)].
\]
Then
\[
\boxed{H(t)=\frac{12D^2r F}{\lambda_2\lambda_4}\,G(t)},
\qquad
G(t)=\int_0^t e^{-\lambda_1 s-\lambda_3(t-s)}\,ds>0.
\]
Thus \(\operatorname{sgn}H(t)=\operatorname{sgn}F\) simultaneously for all positive lags, including the case \(H(t)\equiv0\) when \(F=0\). For \(F\ne0\), the absolute contrast has a unique positive-lag maximum, at
\[
t_*=\begin{cases}
\dfrac{\log(\lambda_3/\lambda_1)}{\lambda_3-\lambda_1},&\lambda_3\ne\lambda_1,\\[3pt]
\dfrac1{\lambda_1},&\lambda_3=\lambda_1.
\end{cases}
\]
If \(-1\le A\le1\) almost surely, then \(F>0\) under the fourth-moment assumption and hence \(H(t)>0\) for every \(t>0\).

An exact overshoot transition occurs for the natural two-atom law \(\Pr(A=-2)=p\), \(\Pr(A=0)=1-p\) with \(0\le p<1/16\):
\[
F=1-28p.
\]
Consequently the contrast is positive for \(p<1/28\), identically zero for \(p=1/28\), and negative for \(1/28<p<1/16\). At the zero-contrast point the stationary process is **not time-reversible**; therefore a vanished fourth-order temporal contrast is not a detailed-balance certificate.

For every permitted multiplier law, the entire two-time covariance agrees with that of a stationary *Gaussian* Ornstein–Uhlenbeck process having relaxation rate \(\lambda_1\), stationary variance \(2D/\lambda_2\), and diffusion coefficient \(2D\lambda_1/\lambda_2\). That Gaussian comparator has \(H(t)=0\) at all lags.

## Assumptions and scope
The position evolves by \(dX_t=\sqrt{2D}\,dW_t\) between events of an independent homogeneous Poisson process of rate \(r\). At the event times \(T_k\), its left limit jumps instantaneously to \(X_{T_k}=A_k X_{T_k-}\), where the real marks \(A_k\) are i.i.d., independent of the Brownian noise and of the event times, with \(\mathbb E|A|^4<1\). There is no confining potential or drift between resets. The process is defined in its unique stationary regime with finite fourth moment. Every conclusion is valid at each finite positive lag, without imposing a nonnegative multiplier or an almost-sure contraction beyond the stated fourth-moment bound.

## Proof
**1. Stationarity and moments.** On a two-sided marked Poisson process and independent two-sided Brownian motion, define
\[
X_t=\sqrt{2D}\int_{-\infty}^t\left(\prod_{k:s<T_k\le t} A_k\right)dW_s.
\]
The product is over finitely many events on any bounded interval. Writing its value as \(K_{s,t}\), independent marking gives \(\mathbb E[K_{s,t}^j]=e^{-\lambda_j(t-s)}\) for \(j=2,4\). Since \(\mathbb E|A|^4<1\), both rates are positive. The Brownian integral exists in \(L^2\), and conditional Gaussianity plus the two integrations of \(\mathbb E[K_{s,t}^2K_{u,t}^2]\) yields finite fourth moment. The exact values are
\[
v_2=\mathbb E[X_0^2]=\frac{2D}{\lambda_2},\qquad
v_4=\mathbb E[X_0^4]=\frac{24D^2}{\lambda_2\lambda_4}.
\]
For example, when \(s\le u\le t\), \(\mathbb E[K_{s,t}^2K_{u,t}^2]=e^{-\lambda_2(u-s)-\lambda_4(t-u)}\). Synchronous coupling of two initial states gives an exact fourth-power distance factor \(\mathbb E|X_t^x-X_t^y|^4=|x-y|^4e^{-\lambda_4t}\), proving uniqueness among stationary laws of finite fourth moment. All odd stationary moments up to order three vanish by Brownian and reflection symmetry.

**2. Conditional polynomial dynamics.** The jump-diffusion generator acting on polynomials is
\[
\mathcal Lf(x)=Df''(x)+r\bigl(\mathbb E[f(Ax)]-f(x)\bigr).
\]
In particular \(\mathcal Lx=-\lambda_1x\) and \(\mathcal Lx^3=6Dx-\lambda_3x^3\). Integrating the corresponding closed linear moment equations gives, for every starting point \(x\),
\[
\mathbb E[X_t\mid X_0=x]=e^{-\lambda_1t}x,
\quad
\mathbb E[X_t^3\mid X_0=x]=e^{-\lambda_3t}x^3+6D\,G(t)x.
\]
Here \(G(t)=(e^{-\lambda_1t}-e^{-\lambda_3t})/(\lambda_3-\lambda_1)\) when \(\lambda_1\ne\lambda_3\), with continuous extension \(t e^{-\lambda_1t}\) when they agree.

**3. Temporal contrast and sign.** Multiplying these identities by appropriate stationary initial moments gives
\[
H(t)=\bigl(6Dv_2-(\lambda_3-\lambda_1)v_4\bigr)G(t).
\]
Substitute the exact \(v_2,v_4\) to obtain
\[
6Dv_2-(\lambda_3-\lambda_1)v_4
=\frac{12D^2}{\lambda_2\lambda_4}
\bigl[\lambda_4-2(\lambda_3-\lambda_1)\bigr]
=\frac{12D^2r}{\lambda_2\lambda_4}\mathbb E[(1-A)^3(1+A)].
\]
The last equality follows from the polynomial identity \((1-a)^3(1+a)=1-2a+2a^3-a^4\). The integral defining \(G\) is strictly positive on \(t>0\), so its prefactor decides the sign for *every* lag. When \(|A|\le1\) almost surely, the integrand in \(F\) is nonnegative and strictly positive whenever \(|A|<1\). The fourth-moment condition rules out the distribution being supported entirely on \(\{-1,1\}\), and hence \(F>0\).

Differentiating the explicit two-exponential formula for \(G\) gives the unique critical point in the statement; \(G(0)=0\), \(G(t)>0\), and \(G(t)\to0\) as \(t\to\infty\), so the critical point is its unique global maximum.

**4. Covariance equivalence and irreversible blind spot.** The conditional first-moment equation yields
\[
\mathbb E[X_tX_0]=v_2e^{-\lambda_1t},\qquad t\ge0,
\]
and by stationarity its two-sided extension is \(v_2e^{-\lambda_1|t|}\). This is precisely the covariance of the Gaussian Ornstein–Uhlenbeck comparator specified above; Gaussian fourth moments are symmetric under the exchange in \(H\).

For \(A=-2\) with probability \(p\) and \(A=0\) otherwise, the fourth-moment hypothesis is \(16p<1\) and \(F=(1-p)\cdot1+p\cdot(-27)=1-28p\). At \(p=1/28\), the time-arrow contrast vanishes even though the jump kernel has a strictly positive rate \(r(1-p)\) from every nonzero position directly to zero and no reverse jumps from zero to nonzero positions. The stationary law has no atom at zero, because between Poisson jumps its Brownian evolution has a density. Therefore the off-diagonal jump-measure detailed-balance identity is violated: the measure on \(\{(x,0):x\ne0\}\) has positive mass, while its reversed measure does not. The continuous Brownian term cannot cancel this off-diagonal jump flux. Thus the stationary process is not reversible at the zero-contrast point.

## Verification
Run `python verify_time_arrow.py` with Python 3 and NumPy, SciPy and SymPy. It checks the exact multiplier polynomial, stationary second/fourth moments and generator identities, and independently compares the closed-form time contrast with a matrix exponential of the degree-four polynomial generator for ten finite-support mark laws including the sign reversal and the zero-contrast law. The supplied run passed 124 counted assertions. The numerical comparisons are independent finite-dimensional consistency tests; the conclusions for continuous multiplier laws and every positive lag follow from the proof, not from finite sampling.

## Relationship to prior work
Dahlenburg, Chechkin, Schumer and Metzler introduce random-amplitude stochastic resetting, including overshooting scenarios, but their principal example is ballistic motion rather than this Brownian time-antisymmetric fourth moment. Tal-Friedman, Roichman and Reuveni derive the partial-reset Brownian stationary distribution and higher *one-time* moments for a fixed positive contraction. Di Bello and collaborators analyze partial-reset *time-dependent one-point* propagators, also using fixed positive contractions. Their renewal and transform methods provide broad background and may implicitly yield special cases; they do not, in the inspected treatments, state the signed multiplier's exact all-lag temporal sign criterion, negative-overshoot reversal or irreversible zero-contrast case. Yuvan and Bier study time-reversal asymmetry in a *different* Langevin model with Lévy forcing and a harmonic potential. No uniqueness claim follows from unsuccessful database searches. Priority for the general formula remains subject to possible stronger stochastic-semigroup results.

## Limitations
The theorem requires Poisson clocks, multiplier marks independent across events and independent of Brownian noise, no between-event drift, and \(\mathbb E|A|^4<1\). It does not treat other waiting laws, state-dependent resets, coupled particles, nonlinear drift, or infinite fourth moments. A zero contrast is not a sufficient condition for reversibility; the explicit overshoot case demonstrates this. Statistical estimation from finite trajectories, including the optimum lag, is not analyzed. Prior general transition-semigroup formulas could imply parts of the calculation even if no explicit sign theorem was located.

## References
1. M. Dahlenburg, A. V. Chechkin, R. Schumer, and R. Metzler, *Stochastic resetting by a random amplitude*, arXiv:2104.14866v1 (first posted 2021-04-30). https://arxiv.org/abs/2104.14866
2. O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v1 (first posted 2022-05-06). https://arxiv.org/abs/2205.03363
3. C. Di Bello and collaborators, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722v1 (first posted 2023-05-23). https://arxiv.org/abs/2305.13722
4. S. Yuvan and M. Bier, *Breaking of time-reversal symmetry for a particle in a parabolic potential that is subjected to Lévy noise*, Physical Review E 104, 014119 (2021), DOI:10.1103/PhysRevE.104.014119.
