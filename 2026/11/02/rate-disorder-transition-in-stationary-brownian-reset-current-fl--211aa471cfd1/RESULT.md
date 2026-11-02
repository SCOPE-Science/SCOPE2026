# Rate-disorder transition in stationary Brownian-reset current fluctuations

## Finding

Let particles have independent Brownian displacements with diffusivity \(D>0\) and individually fixed Poisson-reset rates \(R>0\), returning to their own negative-half-line anchors. Suppose anchors and rates form a marked Poisson process of intensity \(\rho\,dz\,f(r)dr\), \(z>0\), with \(\rho>0\), and all motions are sampled in their stationary conditional laws. Write \(Q_t\) for the number of particles to the right of the origin at time \(t\), and
\[
V_T=\operatorname{Var}\left(T^{-1}\int_0^TQ_t\,dt\right),\qquad
V_\infty=\frac{\rho\sqrt D}{8}\mathbb E[R^{-1/2}].
\]
Assume \(f\) is a probability density on \((0,\infty)\) with \(f(r)\sim c r^a\) as \(r\downarrow0\), where \(c>0\) and \(a>-1/2\). Put \(\delta=a+1/2\) and
\[
K_a=\frac{\rho c\sqrt D\,\Gamma(a+1)(4a+5)}{2\sqrt\pi(2a+1)(2a+3)}>0.
\]
Then the dynamic connected current covariance \(H(t)=\mathbb E[\operatorname{Cov}(Q_0,Q_t\mid\text{anchors and rates})]\) has the sharp asymptotic
\[
H(t)\sim K_a t^{-\delta}\quad(t\to\infty),
\]
although every fixed-rate constituent has exponentially decaying covariance. The time-averaged variance has the complete trichotomy
\[
V_T-V_\infty\sim
\begin{cases}
\displaystyle\frac{2K_a}{(1-\delta)(2-\delta)}T^{-\delta},&-1/2<a<1/2,\\[1ex]
\displaystyle\frac{7\rho c\sqrt D}{16}\frac{\log T}{T},&a=1/2,\\[1ex]
\displaystyle\frac{7\rho\sqrt D}{16}\mathbb E[R^{-3/2}]\,T^{-1},&a>1/2.
\end{cases}
\]
The expectation in the last line is finite under the stated density asymptotic. The annealed covariance is \(\operatorname{Cov}(Q_0,Q_t)=V_\infty+H(t)\), and \(V_T\to V_\infty\); the plateau reflects permanent randomness of fixed anchors and rates. The critical density exponent \(a=1/2\) is the exact boundary between divergent and finite integrated dynamic correlation.

## Assumptions and scope

The marked anchors are a Poisson point process on \((0,\infty)\times(0,\infty)\) with intensity \(\rho\,dz f(r)dr\). At each mark \((z,r)\), let \(U_t\) be an independent stationary Brownian process with generator \(D\partial_{uu}+r(g(0)-g(u))\). Physical position is \(U_t-z\), and \(Q_t=\sum_{(z,r)}\mathbf1_{\{U_t>z\}}\). The whole collection of rates is drawn once and never redrawn at resets. Stationarity is two-sided in time. The notation \(\mathbb E\) includes both particle and mark randomness unless conditioning is displayed. No finite-\(N\) approximation, reflecting boundary, or independently time-resampled reset rates is assumed. The mass and second moment of \(Q_t\) are finite because \(\mathbb E R^{-1/2}<\infty\).

## Proof

**1. A fixed-rate two-time kernel.** Put \(\kappa=\sqrt{r/D}\). The invariant displacement density for one particle is \(\pi_r(u)=\kappa e^{-\kappa|u|}/2\), so \(p_r(z)=\mathbb P(U_0>z)=e^{-\kappa z}/2\). For \(t>0\), write \(\sigma=\sqrt{2Dt}\), \(h=\kappa\sigma=\sqrt{2rt}\), and let \(\Phi,\varphi\) be the standard normal CDF and density. Conditioning on no reset during \((0,t)\), which has probability \(e^{-rt}\), gives
\[
\operatorname{Cov}(\mathbf1_{\{U_0>z\}},\mathbf1_{\{U_t>z\}})=e^{-rt}\left[J_r(z,t)-p_r(z)q_r(z,t)\right],
\]
where \(J_r(z,t)=\mathbb P_{\pi_r}(U_0>z,U_0+B_t>z)\), \(q_r(z,t)=\mathbb P_{\pi_r}(U_0+B_t>z)\), and \(B_t\sim N(0,2Dt)\). The reset histories with at least one intervening reset contribute zero to this covariance. Direct Gaussian integration yields
\[
\int_0^\infty J_r(z,t)\,dz=\frac1{4\kappa}+\frac{e^{rt}\Phi(-h)}{2\kappa},
\]
\[
\int_0^\infty p_r(z)q_r(z,t)\,dz=\frac1{4\kappa}-\frac{e^{rt}}{4\kappa}\big[(1-h^2)\Phi(-h)+h\varphi(h)\big].
\]
Consequently the spatially integrated conditional covariance equals
\[
\int_0^\infty \operatorname{Cov}(\mathbf1_{\{U_0>z\}},\mathbf1_{\{U_t>z\}})\,dz
=\frac{1}{4\kappa}F(\sqrt{2rt}),\quad
F(h)=(3-h^2)\Phi(-h)+h\varphi(h).
\]
At \(t=0\), the same formula holds by continuity, giving \(3/(8\kappa)\). Differentiation gives \(F'(h)=-2[h\Phi(-h)+\varphi(h)]<0\), \(F(\infty)=0\), and hence \(F(h)>0\). Gaussian-tail bounds make every integral absolutely convergent.

**2. Poisson marking and exact covariance.** Conditional on marks, different particle paths are independent. Campbell's formula and the total covariance identity therefore give
\[
H(t)=\frac{\rho\sqrt D}{4}\int_0^\infty r^{-1/2}f(r)F(\sqrt{2rt})\,dr,\quad
\operatorname{Cov}(Q_0,Q_t)=H(t)+\frac{\rho\sqrt D}{8}\mathbb E[R^{-1/2}].
\]
The second summand is the variance of the conditional mean \(\sum p_r(z)\). Moreover \(\mathbb E Q_t=\rho\sqrt D\,\mathbb E[R^{-1/2}]/2\); both conditional stationarity and Poisson integrability follow from the same finite integral.

**3. Spectral-edge asymptotic.** Substitute \(u=rt\) in the exact expression for \(H\). For any \(a>-1/2\), elementary integration by parts and Gaussian moments show
\[
\int_0^\infty u^{a-1/2}F(\sqrt{2u})\,du
=\frac{2\Gamma(a+1)(4a+5)}{\sqrt\pi(2a+1)(2a+3)}.
\]
Since \(F(\sqrt{2u})\) decays like \(u^{-1/2}e^{-u}\), split the integral into small and large reset rates, use \(f(r)/(cr^a)\to1\) near zero and dominated convergence on the scaled small-rate part; the complement is exponentially small. This proves \(H(t)\sim K_a t^{-a-1/2}\).

**4. Time-average crossover.** By stationarity,
\[
V_T-V_\infty=\frac2{T^2}\int_0^T(T-t)H(t)\,dt.
\]
For \(0<\delta<1\), regular variation and the substitution \(t=T u\) give the beta integral \(2K_a/[(1-\delta)(2-\delta)]\). When \(\delta=1\), \(\int_0^T H(t)dt\sim K_a\log T\), while \(T^{-2}\int_0^T tH(t)dt=O(T^{-1})\), giving \(2K_a\log T/T\). When \(\delta>1\), Tonelli and the same Gaussian integral at exponent \(a=1/2\) yield \(\int_0^\infty H(t)dt=7\rho\sqrt D\,\mathbb E[R^{-3/2}]/32\), and dominated convergence gives \(2\int_0^\infty H/T\). These are all the asserted regimes.

## Verification

The accompanying `kernel_quadrature.py` computes the fixed-rate kernel independently by Gaussian quadrature for multiple diffusivities and rates. The separate `verification.py` checks the Mellin integral at seven rate-edge exponents and evaluates the resulting power-law constants against exact truncated-rate integrals. These are finite numerical cross-checks; the proof of the asymptotics is the dominated-convergence and regular-variation argument above.

## Relationship to prior work

Di Bello et al., *Current fluctuations in stochastically resetting particle systems* (2023, arXiv:2302.06696), treat a common strictly positive reset rate and derive one-time annealed and quenched distributions, including their stationary forms and nonuniform approach. The standard Brownian resetting renewal formula is also used there. The present claim concerns the different long-time phenomenon caused by a **fixed distribution of individual reset rates accumulating at zero**: an explicit algebraic temporal-current tail and a three-regime time-average variance law. Fixed-rate two-time formulae and their integrated \(T^{-1}\) coefficients give ingredients, but neither by itself asserts the phase boundary under slow-rate disorder. Known random-rate and heterogeneous-media resetting models address other position statistics and do not directly determine this mixed-rate stationary half-line current.

## Limitations

The result assumes a Poisson anchor process, rate marks fixed throughout each trajectory, independent particles, Brownian motion between instantaneous resets, and a genuine density asymptotic \(f(r)\sim cr^a\). It is a theorem about mean covariances and averaged time-window variance; no almost-sure rate of convergence or central limit theorem is asserted. The plateau is induced by frozen marks, not by failure of a single fixed-rate Markov particle to mix. More general regularly varying rate measures may add slowly varying factors; these are not covered by the stated exact constants. Independent publication-priority assessment has not been performed.

## References

1. C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso, G. Schehr, *Current fluctuations in stochastically resetting particle systems*, arXiv:2302.06696 (first version 13 February 2023), https://arxiv.org/abs/2302.06696.
2. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, arXiv:1102.2704 (2011), https://arxiv.org/abs/1102.2704.
3. E. Bertin, *Stochastic resetting of a population of random walks with resetting-rate-dependent diffusivity*, arXiv:2205.00817 (2022), https://arxiv.org/abs/2205.00817.
4. M. K. Lenzi et al., *Transient anomalous diffusion in heterogeneous media with stochastic resetting*, arXiv:2201.05598 (2022), https://arxiv.org/abs/2201.05598.
