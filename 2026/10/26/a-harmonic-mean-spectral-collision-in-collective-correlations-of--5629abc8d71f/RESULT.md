# A harmonic-mean spectral collision in collective correlations of a switching harmonic trap

## Finding
For \(N\geq2\) independent Brownian particles confined by a *shared*, symmetrically switching harmonic trap, the distinct-particle stationary squared-position covariance at lag \(t\) has exactly three exponential modes, except at one sharp switching rate where two modes collide and generate a genuine \(t e^{-2rt}\) term. If the two positive trap relaxation rates are \(a\ne b\), and their environmental switching rate is \(r>0\), the critical rate is
\[
r_*=\frac{2ab}{a+b}.
\]
The slowest decay is \(e^{-2rt}\) for \(r<r_*\), is \(t e^{-2rt}\) at \(r=r_*\), and is \(e^{-\alpha_-t}\) for \(r>r_*\), with strictly positive leading coefficients, where \(\alpha_-=a+b+r-\sqrt{r^2+(a-b)^2}\). The common-noise, collective interpretation holds for every finite \(N\ge2\) and for the infinite-particle empirical mean-square limit.

## Assumptions and scope
Let \((S_t)_{t\in\mathbb R}\) be a stationary two-state continuous-time Markov chain, switching in each direction at rate \(r>0\), and set \(\mu_1=a\), \(\mu_2=b\), where \(a,b,D>0\) and \(a\ne b\). Conditional on the common process \(S\), particles have independent Brownian drivers and follow
\[
dX_i(t)=-\mu_{S_t}X_i(t)\,dt+\sqrt{2D}\,dB_i(t),\qquad i=1,\ldots,N,\quad N\ge2.
\]
Use the stationary solution integrated from \(-\infty\). Define \(C(t)=\operatorname{Cov}(X_i(0)^2,X_j(t)^2)\) for \(i\ne j\), \(t\ge0\); stationarity makes this independent of the chosen pair. Set
\[
K=2ab+r(a+b),\quad J=4ab+r(a+b),\quad P=4ab+3r(a+b)+2r^2,\quad s=2r,
\]
\[
L=\sqrt{r^2+(a-b)^2},\qquad \alpha_\pm=a+b+r\pm L.
\]
All denominators below are nonzero when \(r\ne r_*\); at \(r=r_*\), use the stated continuous limiting formula.

## Proof
**Reduction to a common variance.** Conditional on the entire environmental path, each stationary \(X_i(t)\) is centered Gaussian with the same conditional variance
\[
V_t=2D\int_{-\infty}^{t}\exp\!\left(-2\int_u^t\mu_{S_w}\,dw\right)\,du,
\qquad \dot V_t=2D-2\mu_{S_t}V_t.
\]
The conditional particle laws are independent across distinct indices, even at different times. Therefore
\[ C(t)=\operatorname{Cov}(V_0,V_t).\]
Moreover, conditional laws of large numbers give \(N^{-1}\sum_i X_i(t)^2\to V_t\) almost surely as \(N\to\infty\), for each fixed \(t\). The variance process is bounded between \(D/\max(a,b)\) and \(D/\min(a,b)\), ensuring all moment calculations below.

**Exact stationary moments and derivatives.** Use column phase probabilities, \(\pi=(1/2,1/2)^T\), \(Q=\bigl(\begin{smallmatrix}-r&r\\r&-r\end{smallmatrix}\bigr)\), \(A=Q-2\operatorname{diag}(a,b)\), and \(A_2=Q-4\operatorname{diag}(a,b)\). The column vectors of phase-resolved moments are uniquely
\[
m=-2D A^{-1}\pi,\qquad z=-4D A_2^{-1}m.
\]
With \(\bar v={\bf1}^Tm\), stationarity gives \(C'(0+)=\mathbb E[(V_0-\bar v)\dot V_0]=0\), and integration by parts for a bounded stationary, piecewise differentiable process gives \(C''(0+)=-\mathbb E[\dot V_0^2]\). Direct substitution into the two linear systems yields
\[
C_0:=C(0)=\frac{D^2(a-b)^2P}{K^2J}>0,
\quad W:=\mathbb E[\dot V_0^2]=\frac{4D^2r(a-b)^2(a+b+r)}{KJ}>0.
\]
The second-derivative equality also follows by differentiating the moment-evolution equations below, so no pathwise second derivative at switching jumps is assumed.

**Three-mode formula.** Define column vectors
\[
u(t)_j=\mathbb E[(V_0-\bar v){\bf1}_{\{S_t=j\}}],\qquad
w(t)_j=\mathbb E[(V_0-\bar v)V_t{\bf1}_{\{S_t=j\}}].
\]
They solve \(u'=Qu\), \(w'=Aw+2Du\), with \(u(0)=m-\bar v\pi\), \(w(0)=z-\bar vm\) and \(C(t)={\bf1}^Tw(t)\). Since \({\bf1}^Tu(0)=0\), \(u(t)=e^{-st}u(0)\). The eigenvalues of \(-A\) are \(\alpha_-\) and \(\alpha_+\). Consequently \(C\) solves
\[
(\partial_t+s)(\partial_t+\alpha_-)(\partial_t+\alpha_+)C=0.
\]
For \(r\ne r_*\), the three distinct modes and conditions \(C(0)=C_0\), \(C'(0+)=0\), \(C''(0+)=-W\) yield
\[
C(t)=A_-e^{-\alpha_-t}+A_+e^{-\alpha_+t}+A_se^{-st},
\]
\[
A_-=\frac{\alpha_+s C_0-W}{(\alpha_+-\alpha_-)(s-\alpha_-)},\qquad
A_+=\frac{\alpha_-s C_0-W}{(\alpha_--\alpha_+)(s-\alpha_+)},
\]
\[
A_s=\frac{\alpha_-\alpha_+ C_0-W}{(\alpha_--s)(\alpha_+-s)}
=\frac{D^2(a-b)^2}{K\,[2ab-r(a+b)]}.
\]
The last identity is an algebraic simplification of the stationary moment systems. As \(r\) crosses \(r_*\), the sign of \(s-\alpha_-\) switches exactly once because \(s=\alpha_-\) is equivalent to \(r(a+b)=2ab\); \(s<\alpha_+\) always. Thus for \(r<r_*\), the slowest coefficient is \(A_s>0\). For \(r>r_*\), \(A_->0\): indeed \(W/C_0=4r(a+b+r)K/P<2r(a+b+2r)\le s\alpha_+\). After multiplying by the positive \(P\), the strict inequality is exactly \(r[a^2+6ab+b^2+6r(a+b)+4r^2]>0\).

**Resonance.** At \(r=r_*\), the forcing mode \(s=2r\) equals \(\alpha_-\). The resulting second-order pole is *not removable*: taking the limit in the exact noncritical representation gives
\[
C(t)=\bigl(B+Tt\bigr)e^{-2rt}+E e^{-\alpha_+t},\quad
T=\frac{D^2(a-b)^2}{K(a+b-r)}>0,
\]
where \(B,E\) are uniquely specified by \(C(0)=C_0\) and \(C'(0+)=0\), equivalently
\[
E=-\frac{2rC_0-T}{\alpha_+-2r},\qquad B=C_0-E.
\]
Therefore the quoted critical, subcritical and supercritical large-lag asymptotics follow. For the exact rational parameters \(a=2\), \(b=2/3\), \(r=1\), \(D=1\),
\[
C(t)=\left(\frac{79}{600}+\frac t5\right)e^{-2t}-\frac{19}{1600}e^{-16t/3},\qquad C(0)=\frac{23}{192}.
\]

## Verification
The standalone `verify.py` uses SymPy to independently solve both stationary moment systems, check \(C_0\), \(W\), the full Laplace transform and its three residues, and prove the resonance example by exact rational simplification. It then checks hundreds of positive parameter quadruples at several lags against a separately constructed four-dimensional matrix exponential of the exact conditional-moment evolution, with 2,817 assertions in total. Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The preceding generator, stationary moment and pole arguments, rather than sampling, establish the full parameter-range theorem.

## Relationship to prior work
Biroli, Kulkarni, Majumdar and Schehr (arXiv:2312.02570v1, 5 December 2023) develop the shared switching-trap gas, its stationary joint law and equal-time interparticle correlations; in particular, their equal-time squared-position covariance is the \(t=0\) limit of the observable here. The additional contribution assessed here is the exact *two-time* cross-particle squared-position covariance, its three competing relaxation modes and the harmonic-mean spectral collision with a nonzero polynomial prefactor. The published stationary snapshot does not by itself state the lag-dependent spectral crossover. The general theory of Markov-modulated linear filters permits moment propagators; no claim is made that the block-matrix method itself is new. Comparisons with studies of annealed stiffness and semi-Markovian switching are limited by differences in driving and available full text.

## Limitations
The setting requires symmetric memoryless switching, strictly positive unequal trap rates, common switching for all particles, additive independent Brownian noise, a stationary initialization and fixed time lags. The crossing is an eigenvalue-resonance of a finite-dimensional moment system, not a thermodynamic phase transition. For \(a=b\) the collective covariance vanishes and no normalized spectral classification applies. The statement does not classify asymmetric-switching generalizations, nonlinear confinement, or empirical finite-sample estimation; broader mathematical priority beyond inspected sources remains subject to independent scholarly review.

## References
- G. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (5 December 2023), https://arxiv.org/abs/2312.02570 .
- Study of annealed stochastic stiffness and nonequilibrium fluctuations in a harmonic trap (2025), as compared in the accompanying review; its continuous stiffness mechanism differs from the two-state switching model.
- Research on semi-Markovian switching traps, arXiv:2607.05173 (2026), relevant possible comparison not fully verified in the available material.
