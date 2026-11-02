# A sharp damping threshold for reversal of matched active-noise fourth cumulants in an inertial harmonic trap

## Finding
Consider two stationary inertial harmonic oscillators driven respectively by symmetric telegraph propulsion and planar active-Brownian propulsion, scaled to have **identical two-time force covariance**. Their entire position/velocity covariance functions agree, but the ordering of their stationary position fourth cumulants has a sharp damping-dependent transition. For relaxation rate \(a>0\), oscillation frequency \(b>0\), and orientation/telegraph correlation rate \(d>0\), write \(\Delta_4=\kappa_4(X^{\mathrm A})-\kappa_4(X^{\mathrm R})\). Define
\[
\begin{aligned}
C_0={}&432a^6+1846a^5d+2828a^4d^2+1887a^3d^3+588a^2d^4+93ad^5+6d^6,\\
C_1={}&156a^4+544a^3d+797a^2d^2+417ad^3+51d^4,\\
C_2={}&12a^2-30ad-27d^2,\qquad P=C_0+C_1b^2+C_2b^4.
\end{aligned}
\]
Then the exact difference is
\[
\Delta_4=\frac{3v^4 P}{8a(a+2d)(a^2+b^2)(4a^2+b^2)((a+d)^2+b^2)((a+2d)^2+b^2)((3a+d)^2+b^2)((3a+d)^2+9b^2)}.
\]
If \(a/d\ge(5+\sqrt{61})/4\), then \(\Delta_4>0\) for every \(b>0\). If \(0<a/d<(5+\sqrt{61})/4\), there is exactly one positive crossover frequency \(b_*\), specified by
\[
b_*^2=\frac{C_1+\sqrt{C_1^2-4C_2C_0}}{-2C_2},
\]
with \(\Delta_4>0\) for \(0<b<b_*\), \(\Delta_4=0\) at \(b=b_*\), and \(\Delta_4<0\) for \(b>b_*\). This is a classification of a fourth-order discrimination failure and reversal despite exact equality of **all** second-order stationary signals.

## Assumptions and scope
Fix \(a,b,d,v>0\) and \(T\ge0\). Let \(X\) solve the stationary version of
\[
\ddot X_t+2a\dot X_t+(a^2+b^2)X_t=vF_t+\sqrt{2T}\,\dot W_t,
\]
where \(W\) is a standard Brownian motion independent of \(F\). For the telegraph model, \(F^{\mathrm R}\in\{-1,1\}\) is stationary and switches at Poisson rate \(d/2\). For the planar active-Brownian model, \(F^{\mathrm A}_t=\sqrt2\cos\Theta_t\), where \(\Theta_t\) is the stationary uniform-angle diffusion \(d\Theta_t=\sqrt{2d}\,dB_t\pmod{2\pi}\). The diffusion \(B\) is independent of \(W\). Different noises can be coupled arbitrarily without changing the individual marginal claims. Fourth cumulants exist by the exponential mechanical Green function and bounded active forces. The parameter \(b>0\) denotes the damped oscillation frequency; critical and overdamped mechanical regimes are not covered. A common Gaussian thermal forcing does not change fourth cumulants, and does change equally all matching second-order covariances.

## Proof
**Step 1: equality of complete second-order data.** Stationarity and the telegraph generator give \(\mathbb E[F^{\mathrm R}_tF^{\mathrm R}_{t+s}]=e^{-d|s|}\). The angular diffusion generator acts on \(e^{i\theta}\) with eigenvalue \(-d\); uniform angular averaging and amplitude \(\sqrt2\) give the same covariance for \(F^{\mathrm A}\). Both means vanish. Since their common stable Green kernel is
\[
G(s)=\mathbf1_{\{s\ge0\}}e^{-as}\frac{\sin(bs)}b,
\]
all output covariances of position and velocity coincide; the common thermal contribution also coincides. In particular, their stationary position variances are both
\[
\operatorname{Var}(X)=\frac{v^2(2a+d)}{2a(a^2+b^2)[a^2+b^2+d(2a+d)]}+\frac{T}{2a(a^2+b^2)}.
\]

**Step 2: four-time forcing comparison.** For ordered times \(t_1\le t_2\le t_3\le t_4\), write \(u=t_2-t_1\), \(w=t_3-t_2\), and \(z=t_4-t_3\). The symmetric two-state Markov property and \(S_t^2=1\) yield
\[
\mathbb E\!\left[\prod_{i=1}^4F^{\mathrm R}_{t_i}\right]=e^{-d(u+z)}.
\]
Fourier expansion of \(\sqrt2\cos\Theta\) and the conditional propagators of angular charges \(\pm1,\pm2\), whose decay exponents are respectively \(d\) and \(4d\), yield
\[
\mathbb E\!\left[\prod_{i=1}^4F^{\mathrm A}_{t_i}\right]=e^{-d(u+z)}\left(1+\tfrac12e^{-4dw}\right).
\]
Thus the ordered-time four-point difference is exactly \(\tfrac12e^{-d(u+4w+z)}\). Pairwise contractions are identical, so this four-point difference also determines the fourth-cumulant difference of the output.

**Step 3: integrate the signed inertial Green kernel.** Thermal Gaussian cumulants vanish in fourth order. Fourfold convolution, symmetry under 24 time orders, and the preceding difference give
\[
\Delta_4=12v^4\int_{0\le s_1\le s_2\le s_3\le s_4}\left[\prod_{j=1}^4G(s_j)\right]e^{-d[(s_2-s_1)+4(s_3-s_2)+(s_4-s_3)]}\,ds_1\cdots ds_4.
\]
Set nonnegative gaps \(q_1=s_1\), \(q_j=s_j-s_{j-1}\) for \(j=2,3,4\). Writing each sine as a sum of two exponentials, integrate each gap independently. This gives the finite exact identity
\[
\Delta_4=\frac{3v^4}{4b^4}\sum_{\epsilon\in\{-1,1\}^4}\left(\prod_{j=1}^4\epsilon_j\right)\prod_{j=1}^4\left[(5-j)a+c_jd-ib\sum_{\ell=j}^4\epsilon_\ell\right]^{-1},
\]
where \((c_1,c_2,c_3,c_4)=(0,1,4,1)\). The 16 terms come in complex-conjugate pairs. Grouping them over the common positive real denominator and cancelling the removable \(b^4\) factor gives the displayed exact rational formula with polynomial \(P\). This last reduction is a finite rational identity, independently corroborated by exact stationary generator moment recurrences described below.

**Step 4: classify every sign.** Every factor outside \(P\) is strictly positive for the stated domain; also \(C_0,C_1>0\). The quadratic coefficient \(C_2\) has its unique positive zero at \(a/d=(5+\sqrt{61})/4\). If \(C_2\ge0\), then \(P>0\) for all \(b^2>0\). If \(C_2<0\), \(P\) as a quadratic in \(b^2\) starts positive, is strictly concave, and tends to minus infinity. Its two roots have negative product, hence precisely one is positive. The quadratic formula gives \(b_*^2\) above. The inequalities follow. At fixed common variance, subtracting three times its square shows that \(\Delta_4\) is also the difference of fourth central moments and its sign is the kurtosis ordering.

## Verification
Run `python verify.py` with SymPy installed. The program independently constructs stationary polynomial-generator equations degree by degree for both Markov forcings, solves exact-rational moments in six parameter examples, and checks the displayed difference and matched variances. Examples include \((a,b,d)=(1,2,1)\) with \(\Delta_4/v^4=57/133120>0\), and \((1,10,1)\) with \(\Delta_4/v^4=-61455/25304514480128<0\). Here the examples use \(v=1,T=0\); the general amplitude factor and Gaussian cancellation follow analytically. The exact 16-term gap-integral expression supplies an independent algebraic route to the universal identity. Finite checks alone are not treated as proof of the universal classification.

## Relationship to prior work
Sarkar, Santra and Basu studied stationary states of activity-driven harmonic chains, including telegraph and active-Brownian boundary forces and matched two-time correlations (arXiv:2210.09035). Patel and Chaudhuri derived inertial trapped active-Brownian moments (arXiv:2404.01107; with related free-inertial study arXiv:2310.00802). Dutta and collaborators treated an inertial run-and-tumble particle in a harmonic trap (arXiv:2406.06120). These works contain essential forward-model ingredients. The theorem here compares the two **covariance-matched** active mechanisms in the same inertial trap and classifies globally the sign and unique reversal of their fourth-cumulant contrast, including the damping threshold. Existing forward moments should not be mistaken for a new result in themselves; the difference formula and its threshold classification are the evaluated claim.

## Limitations
Only the underdamped linear harmonic model, symmetric telegraph flipping, uniformly initialized planar angular diffusion, independent additive Gaussian thermal noise, and exact stationary statistics are considered. The theorem does not assert Gaussianity, estimator performance with finitely many trajectories, or the ordering of all higher cumulants. Source comparisons do not certify publication priority against every possible broader result on filtered Markov forcing. No independent scientific audit has been performed.

## References
- S. Sarkar, S. Santra, A. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035v1 (2022-10-17).
- A. Patel, D. Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance*, arXiv:2404.01107v1 (2024-04-01).
- A. Patel, D. Chaudhuri, *Exact moments and re-entrant transitions in the inertial dynamics of active Brownian particles*, arXiv:2310.00802v1 (2023-10-01).
- A. Dutta et al., *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120v1 (2024-06-10).
