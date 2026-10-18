# Reentrant centered-variance anisotropy under complete resetting of a trapped active Brownian particle

## Finding
For a harmonically confined planar active Brownian particle whose **position and orientation reset together**, the stationary covariance ellipse reverses its major axis **twice** as the resetting rate increases, for every positive trap strength. In contrast, the uncentered longitudinal second moment exceeds the transverse one at every resetting rate. Moreover, the mean-longitudinal-displacement maximizing rate always lies strictly within the transverse-dominant regime.

In units with rotational diffusion coefficient one, let \(\beta>0\) denote harmonic relaxation, \(v>0\) propulsion, \(D\geq0\) translational diffusivity, and \(\rho>0\) complete-reset rate. Set
\[
 Q_\beta(\rho)=\rho^4+(\beta-1)\rho^3-(6\beta+2)\rho^2-4\beta(\beta+1)\rho+2\beta^2.
\]
Then
\[
\operatorname{Var}(X)-\operatorname{Var}(Y)=
\frac{v^2\rho Q_\beta(\rho)}
{(\rho+\beta)^2(\rho+2\beta)(\rho+1)^2(\rho+4)(\rho+\beta+1)}.
\]
For every \(\beta>0\), the polynomial has **exactly two distinct simple positive zeros** \(\rho_-(\beta)<\sqrt\beta<\rho_+(\beta)\). The variance difference is positive before the lower zero and after the upper zero; it is strictly negative between them and vanishes only at the two zeros. These signs do not depend on \(v>0\) or \(D\geq0\).

The two phase boundaries satisfy the exact asymptotics
\[
\begin{aligned}
 \beta\downarrow0:\quad &\rho_-(\beta)\sim(\sqrt2-1)\beta,\qquad \rho_+(\beta)\to2,\\
 \beta\to\infty:\quad &\rho_-(\beta)\to\tfrac12,\qquad \rho_+(\beta)\sim2\sqrt\beta.
\end{aligned}
\]
At all \(\rho>0\), independently of \(D\),
\[
\mathbb E[X^2]-\mathbb E[Y^2]=
\frac{2v^2\rho}{(\rho+4)(\rho+\beta+1)(\rho+2\beta)}>0.
\]
The stationary mean is \(\mathbb E[X]=v\rho/[(\rho+1)(\rho+\beta)]\), uniquely maximized at \(\rho=\sqrt\beta\), where the **centered** longitudinal variance is strictly *smaller* than the transverse variance.

## Assumptions and scope
Let \(W^x,W^y,B\) be independent standard Brownian motions. Between independent rate-\(\rho\) Poisson events, a state \((X,Y,\Theta)\in\mathbb R^2\times(\mathbb R/2\pi\mathbb Z)\) obeys
\[
\begin{aligned}
 dX_t&=(-\beta X_t+v\cos\Theta_t)\,dt+\sqrt{2D}\,dW^x_t,\\
 dY_t&=(-\beta Y_t+v\sin\Theta_t)\,dt+\sqrt{2D}\,dW^y_t,\\
 d\Theta_t&=\sqrt2\,dB_t\pmod{2\pi}.
\end{aligned}
\]
At each Poisson event the **whole state** resets to \((0,0,0)\). Assume \(\beta>0,\rho>0,v>0,D\geq0\). No chirality, orientation-only resetting, or anisotropic thermal noise is included. The unique stationary law exists by Poisson regeneration and has all moments used below; a new cycle begins from the deterministic reset state independently of the past. Reflection symmetry yields \(\mathbb E[Y]=0\) and \(\operatorname{Cov}(X,Y)=0\), so comparing \(\operatorname{Var}(X)\) and \(\operatorname{Var}(Y)\) indeed compares the two covariance eigenvalues.

## Proof
**1. Generator balance and covariance.** For smooth test functions of polynomial growth, stationarity gives \(\mathbb E[\mathcal L f]=0\), with
\[
\mathcal L f=(-\beta x+v\cos\theta)\partial_x f+(-\beta y+v\sin\theta)\partial_y f+D(\partial_{xx}+\partial_{yy})f+\partial_{\theta\theta}f+\rho[f(0,0,0)-f(x,y,\theta)].
\]
For each positive integer \(j\), applying the generator to \(\cos(j\theta)\) gives \(m_j:=\mathbb E[\cos(j\Theta)]=\rho/(\rho+j^2)\). In particular \(m_1=\rho/(\rho+1)\) and \(m_2=\rho/(\rho+4)\). For \(X\) and \(Y\),
\[
\mathbb E X=\frac{v m_1}{\rho+\beta}=\frac{v\rho}{(\rho+1)(\rho+\beta)},\qquad \mathbb E Y=0.
\]
Applying \(\mathcal L\) to \(x\cos\theta\) and \(y\sin\theta\) and using \(\cos^2\theta=(1+\cos2\theta)/2\), \(\sin^2\theta=(1-\cos2\theta)/2\) gives
\[
\begin{aligned}
(\rho+\beta+1)\,\mathbb E[X\cos\Theta]&=\tfrac v2(1+m_2),\\
(\rho+\beta+1)\,\mathbb E[Y\sin\Theta]&=\tfrac v2(1-m_2).
\end{aligned}
\]
Finally the two squared-coordinate generator equations give
\[
\begin{aligned}
(\rho+2\beta)\mathbb E[X^2]&=2D+2v\mathbb E[X\cos\Theta],\\
(\rho+2\beta)\mathbb E[Y^2]&=2D+2v\mathbb E[Y\sin\Theta].
\end{aligned}
\]
Subtracting these equations proves the stated strictly positive *uncentered* difference; subtracting \((\mathbb E X)^2\) then produces the asserted rational function with the quartic numerator \(Q_\beta\). In particular, isotropic translational diffusion cancels exactly.

**2. Independent representation of the uncentered difference.** At a stationary observation time, the age since the last reset has density \(\rho e^{-\rho t}\). In a reset-free excursion of length \(t\), the active position is a convolution of the orientation with \(e^{-\beta(t-s)}\); thermal coordinate contributions have the same second moment. For \(0\le s\le u\), Gaussian angular motion gives
\[
\mathbb E[\cos(\Theta_s+\Theta_u)]=e^{-(3s+u)}.
\]
Therefore the difference of raw second moments is \(2v^2\) times the integral over \(t\ge u\ge s\ge0\) of
\[
\rho e^{-\rho t}e^{-\beta(2t-s-u)}e^{-(3s+u)}\,ds\,du\,dt.
\]
Making the substitutions \(u=s+z\), \(t=u+w\) factorizes the integral into three convergent one-dimensional exponential integrals and yields \(2v^2\rho/[(\rho+4)(\rho+\beta+1)(\rho+2\beta)]\), independently verifying the generator calculation.

**3. Exactly two positive crossings.** Observe
\[
Q_\beta(0)=2\beta^2>0,\qquad
Q_\beta(\sqrt\beta)=-\beta(3\beta\sqrt\beta+3\beta+5\sqrt\beta+2)<0,
\]
and \(Q_\beta(\rho)\to+\infty\) as \(\rho\to+\infty\). Thus there are at least two distinct positive zeros, one on either side of \(\sqrt\beta\). The coefficient signs of the quartic, in decreasing powers, are \(+\), the sign of \(\beta-1\) (or zero), \(-\), \(-\), \(+\). They have exactly two sign variations for every \(\beta>0\); Descartes' rule of signs gives *at most* two positive roots counted with multiplicity. Both identified roots are therefore simple, are the only positive zeros, and give the asserted \(+,-,+\) sign pattern. The mean-displacement optimum is \(\sqrt\beta\) by differentiating \(\rho/[(\rho+1)(\rho+\beta)]\); its position strictly between the two covariance transitions follows from the displayed negative witness.

**4. Boundary asymptotics.** As \(\beta\downarrow0\), the rescaled polynomial obeys
\[
\beta^{-2}Q_\beta(\beta c)\longrightarrow2-4c-2c^2,
\]
whose unique positive simple root is \(c=\sqrt2-1\). At fixed \(\rho\), \(Q_0(\rho)=\rho^2(\rho-2)(\rho+1)\), and the simple positive root \(2\) persists. Two-root uniqueness, the intermediate-value theorem, and simple-root continuity identify the asserted lower and upper branches. As \(\beta\to\infty\), the fixed-rate limit \(\beta^{-2}Q_\beta(\rho)\to2-4\rho\) has a unique positive simple root \(1/2\). At the scale \(\rho=c\sqrt\beta\),
\[
\beta^{-5/2}Q_\beta(c\sqrt\beta)\longrightarrow c^3-4c,
\]
whose strictly positive simple root is \(c=2\). Again, the global two-root theorem selects the two branches and proves their limits without treating finite computations as a root-count proof.

## Verification
The accompanying `verify.py` uses exact SymPy algebra to reconstruct the generator-derived rational moments, verifies an independent time-integral factorization, checks the negative witness, and checks the polynomial scaling limits. It then performs 1,080 independent exact-rational moment-balance comparisons over a parameter grid, plus 22 symbolic and witness assertions. The program reports 1,102 assertions passed. These checks corroborate the proof; the infinite-parameter sign classification is established analytically by the intermediate-value theorem and Descartes' rule, not by enumeration. Run `python verify.py` with Python 3 and SymPy installed.

## Relationship to prior work
A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1 (first submitted 2024-09-11), established this full-reset trapped model, its mean displacement, total stationary mean-squared displacement, the longitudinal second moment and variance (Appendix D.2, equations 60 and 63), and a non-Gaussian **kurtosis** phase diagram. The source's equations already imply the present elementary moment inputs; none of those equations or the maximizer \(\rho=\sqrt\beta\) is claimed new. The contribution here is the **complete, for-every-trap-strength classification** of the *centered two-axis covariance ordering*, including exactly two simple transitions, an exact witness locating the known mean-optimal rate inside the transverse-dominant interval, and singular asymptotics for both transition curves. Inspection of both the initial and revised public manuscript found no such two-threshold centered-ellipse theorem; that statement is nevertheless algebraically derivable using their moment formulas, and a priority review should inspect any equivalent published classification.

For comparison, *Active Brownian particle under stochastic orientational resetting* (arXiv:2405.06769v1) studies orientation resetting without joint position resetting and does not supply a stationary full-reset trapped covariance-ellipse theorem. Kumar, Sadekar and Basu, *Active Brownian motion in two dimensions under stochastic resetting* (arXiv:2008.03294), treat the unconfined case. A broad earlier theorem specializing to the exact covariance ordering cannot be ruled out by a finite literature search.

## Limitations
The particle must reset both position and orientation to the same deterministic state, the trap must be isotropic and strictly confining, propulsion must be nonzero, and rotational diffusion must be positive (normalized to one). Purely passive motion \(v=0\) has no directional variance split. No statement is made for chirality, random reset orientations, partial/position-only/orientation-only resetting, anisotropic spatial diffusion or nonlinear trapping. The asymptotics are for the crossing rates at fixed nondimensionalization, not for other observables. A derived qualitative consequence of published exact second-moment formulas may have antecedents in the active-matter literature; independent novelty and correctness audit have not been performed.

## References
1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1, 2024-09-11, https://arxiv.org/html/2409.06920v1 . Revised v2: https://arxiv.org/html/2409.06920v2 .
2. A. Baouche, T. Franosch, and collaborators, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1, 2024-05-10, https://arxiv.org/html/2405.06769v1 .
3. V. Kumar, O. Sadekar, and U. Basu, *Active Brownian motion in two dimensions under stochastic resetting*, arXiv:2008.03294, https://arxiv.org/abs/2008.03294 .
