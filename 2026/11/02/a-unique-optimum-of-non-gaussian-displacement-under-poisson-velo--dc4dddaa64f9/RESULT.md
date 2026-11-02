# A unique optimum of non-Gaussian displacement under Poisson velocity resetting

## Finding

An inertial Brownian particle whose velocity, but not its position, is reset to zero has strictly positive displacement fourth cumulant at every positive observation time. More sharply, for any positive damping, velocity-noise intensity, and reset rate, its long-time excess kurtosis has an exact universal coefficient that increases and then decreases with the dimensionless reset rate. There is precisely one global optimum.

Define \(\beta=r/\gamma\) and
\[
H(\beta)=\frac{6\beta(7\beta^2+28\beta+27)}{(\beta+1)(\beta+2)(\beta+3)(\beta+4)}.
\]
For \(X_0=V_0=0\), writing \(\kappa_4(X_t)=\mathbb E[X_t^4]-3\mathbb E[X_t^2]^2\), the theorem states
\[
\kappa_4(X_t)>0\quad(t>0),\qquad
\lim_{t\to\infty}\gamma t\,\frac{\kappa_4(X_t)}{\operatorname{Var}(X_t)^2}=H(r/\gamma).
\]
The function \(H\) has a unique maximizer \(\beta_*\in(2.556536,2.556537)\), the unique positive zero of
\[
P(\beta)=7\beta^6+56\beta^5+116\beta^4-160\beta^3-959\beta^2-1344\beta-648.
\]
Numerically \(\beta_*=2.55653661983339\ldots\) and \(H(\beta_*)=3.75000322406561\ldots\). Both endpoint limits of \(H\) vanish, with \(H(\beta)\sim27\beta/4\) at zero and \(H(\beta)\sim42/\beta\) at infinity.

## Assumptions and scope

Let \(D>0\), \(\gamma>0\), and \(r>0\). Between the times of an independent, homogeneous Poisson process of rate \(r\), the motion in one spatial dimension obeys
\[
dX_t=V_t\,dt,\qquad dV_t=-\gamma V_t\,dt+\sqrt{2D}\,dW_t.
\]
At each Poisson epoch set \(V\) to zero while leaving \(X\) continuous and unchanged. Take \(X_0=V_0=0\). The Brownian motion \(W\) and Poisson clock are independent. The distribution of \(X_t\) is centered for every \(t\). Excess kurtosis means \(\kappa_4(X_t)/\operatorname{Var}(X_t)^2\) (without division by three). The asserted limit is at fixed positive parameters as \(t\) tends to infinity.

## Proof

**1. Reset-free Gaussian excursion.** Starting with velocity zero, the integrated Ornstein–Uhlenbeck displacement over duration \(s\) is centered normal with variance
\[
q(s)=\frac{2D}{\gamma^2}\left[s-\frac{2(1-e^{-\gamma s})}{\gamma}+\frac{1-e^{-2\gamma s}}{2\gamma}\right].
\]
Indeed, the stochastic convolution of the velocity gives
\[
X_s=\frac{\sqrt{2D}}{\gamma}\int_0^s(1-e^{-\gamma(s-u)})\,dW_u.
\]
Consequently \(q(0)=0\), \(q'(s)=2D(1-e^{-\gamma s})^2/\gamma^2\), and \(q\) is strictly convex on positive times, with \(0\le q(s)\le 2Ds/\gamma^2\).

**2. Random conditional variance.** Conditional on reset epochs up to time \(t\), all completed excursions and the last partial excursion have independent centered normal displacements. If \(T_j\) are complete reset intervals and \(a_t\) is the age since the last reset, the conditional variance is exactly
\[
A_t=\sum_{j=1}^{N_t}q(T_j)+q(a_t).
\]
Thus \(\operatorname{Var}(X_t)=\mathbb E A_t\) and \(\kappa_4(X_t)=3\operatorname{Var}(A_t)\). For any \(t>0\), no reset occurs with probability \(e^{-rt}>0\), giving \(A_t=q(t)\). Exactly one reset at an interior time \(u\) has positive probability and gives \(A_t=q(u)+q(t-u)<q(t)\), by strict superadditivity of a strictly convex \(q\) with \(q(0)=0\). Therefore \(\operatorname{Var}(A_t)>0\) and the finite-time strict inequality follows.

**3. Long-time cumulant rates.** Let \(T\) be exponential with rate \(r\), and put \(c=r\mathbb E[q(T)]\) and \(Y=q(T)-cT\). The renewal-reward law and centered-reward variance identity give
\[
\lim_{t\to\infty}\frac{\mathbb E[A_t]}t=c,\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}(A_t)}t=r\mathbb E[Y^2].
\]
For completeness, \(M_n=\sum_{j=1}^n(q(T_j)-cT_j)\) is a square-integrable martingale. Its stopping index \(N_t+1\), unlike \(N_t\), is a stopping time for the successive-interarrival filtration. Wald's second identity gives \(\mathbb E[M_{N_t+1}]=0\) and \(\mathbb E[M_{N_t+1}^2]=(rt+1)\mathbb E[Y^2]\). Since \(q\) has bounded derivative, the discrepancy \(A_t-ct-M_{N_t+1}\) is bounded in absolute value by a constant times the interarrival straddling \(t\); that interval is the sum of the Poisson backward age and independent exponential residual life, and has moments bounded uniformly in \(t\). Its \(L^2\) norm is thus uniformly bounded. The variance discrepancy after dividing by \(t\) tends to zero by Cauchy–Schwarz. The same decomposition gives the mean rate. This also supplies a proof without presupposing a Gaussian long-time distribution.

The elementary Laplace integrals for \(q(T)\), \(Tq(T)\), and \(q(T)^2\), with \(\mathbb ET^2=2/r^2\), yield
\[
\begin{aligned}
c&=\frac{4D}{(r+\gamma)(r+2\gamma)},\\
\lim_{t\to\infty}\frac{\kappa_4(X_t)}t
&=\frac{96D^2r(7r^2+28\gamma r+27\gamma^2)}{(r+\gamma)^3(r+2\gamma)^3(r+3\gamma)(r+4\gamma)}.
\end{aligned}
\]
Since \(\operatorname{Var}(X_t)\sim ct\), division gives the displayed formula for \(H(r/\gamma)\).

**4. A unique optimum.** Direct differentiation produces the exact factorization
\[
H'(\beta)=-\frac{6P(\beta)}{(\beta+1)^2(\beta+2)^2(\beta+3)^2(\beta+4)^2}.
\]
The coefficient sequence of \(P\), in descending powers, has exactly one sign change. By Descartes' rule, \(P\) has at most one positive zero, counting multiplicity. Since \(P(0)<0\), \(P(\beta)\to+\infty\) and continuity forces a positive zero, which is unique and simple. Therefore \(H\) rises strictly to this root and falls strictly after it. Exact rational substitution gives \(P(2.556536)<0<P(2.556537)\). Its endpoint expansions then show this root is the unique global maximum.

## Verification

A standalone program, `verify.py`, reconstructs the exact exponential-age moments, derives the cumulant rate a second way from the tilted Ornstein–Uhlenbeck generator, factors the derivative of \(H\), verifies the Descartes sign pattern and exact rational root bracket, and compares direct numerical quadrature of the excursion-reward expression with the rational formula for several parameter choices. Execute `python verify.py` with the dependencies listed in `requirements.txt`. Every numerical comparison supplements, but does not replace, the algebraic and probabilistic proof above.

## Relationship to prior work

Olsen and Löwen (2024) study precisely the one-coordinate velocity-resetting framework and derive a general Fourier–Laplace propagator, all-order moment recurrence, and effective long-time diffusivity. Those results include the model and its second-order transport behavior; neither the general propagator nor its renewal decomposition is claimed here. The proposed new contribution is the explicit long-time fourth-cumulant coefficient together with the sharp, all-positive-parameter, unique reset-rate maximum of the normalized non-Gaussian correction.

Meylahn, Sabhapandit, and Touchette (2015) study the *same resetting Ornstein–Uhlenbeck area model* through a general scaled-cumulant-generating-function renewal formula, which is strictly stronger than knowledge of any fixed low-order cumulant at a specified resetting rate. The present coefficient can in principle be extracted from that general relation; its explicit rational form and universal optimizing root are the added analytic classification, not an independent model or a new general renewal identity. Smith and Majumdar (2022) analyze areas of self-similar reset Gaussian processes, which include undamped Brownian-noise limits rather than the finite positive friction ratio optimized here. Related Gaussian-replacement models differ because velocity is redrawn from equilibrium instead of being set to zero.

## Limitations

The theorem is specific to Poisson resetting of velocity to zero, with independent Gaussian acceleration, positive damping, and *unreset* position. The finite-time strict cumulant statement holds for every \(t>0\), but the closed coefficient and optimization concern only the leading \(1/t\) excess-kurtosis asymptotic. They do not classify finite-time optimal rates, arbitrary reset-velocity laws, or the entire displacement distribution. General published renewal/large-deviation transforms may implicitly encode this cumulant; no independent priority certification is claimed.

## References

1. Kristian Stølevik Olsen and Hartmut Löwen, “Dynamics of inertial particles under velocity resetting” (2024), arXiv:2401.12685v1, https://arxiv.org/abs/2401.12685 . First publicly available 2024-01-23.
2. Janusz M. Meylahn, Sanjib Sabhapandit, and Hugo Touchette, “Large deviations for Markov processes with resetting,” *Physical Review E* 92, 062148 (2015), arXiv:1510.02431, https://arxiv.org/abs/1510.02431 .
3. N. R. Smith and S. N. Majumdar, “Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting” (2022), arXiv:2202.03546, https://arxiv.org/abs/2202.03546 .
