# Exact adsorption-count noise and wall-occupation covariance phases for a reset run-and-tumble particle

## Finding
For a one-dimensional run-and-tumble particle with bulk Poisson resetting and a sticky wall, whose desorption returns it to a prescribed bulk state, the limiting adsorption-count Fano factor and the joint covariance of adsorption counts and wall-occupation time are exactly computable. Their sign changes define two distinct critical desorption rates and, at sufficiently weak bulk resetting, an interval with **positive count–occupation covariance but sub-Poissonian adsorption counts**.

Let the bulk speed, tumbling rate, starting distance, resetting rate and desorption rate be respectively \(v>0\), \(\alpha>0\), \(x_0>0\), \(r>0\), and \(\gamma>0\). Put
\[
\beta=\frac{x_0}{v}\sqrt{r(r+2\alpha)},\qquad
\beta'=\frac{x_0}{v}\frac{r+\alpha}{\sqrt{r(r+2\alpha)}},
\]
\[
m=\frac{e^\beta-1}{r},\qquad
s^2=\frac{e^{2\beta}-1-2r\beta'e^\beta}{r^2},\qquad b=\gamma^{-1},\quad \mu=m+b.
\]
These are the mean and variance of a free excursion from \((x_0,-1)\) to the sticky wall and the mean wall residence, respectively. For the number \(N(t)\) of adsorptions and cumulative bound time \(H(t)\) up to time \(t\), the exact stationary asymptotic covariance-rate matrix, valid also from any fixed deterministic initial state, is
\[
\lim_{t\to\infty}\frac1t
\begin{pmatrix}\operatorname{Var}N(t)&\operatorname{Cov}(N(t),H(t))\\
\operatorname{Cov}(N(t),H(t))&\operatorname{Var}H(t)\end{pmatrix}
=\frac1{\mu^3}
\begin{pmatrix}s^2+b^2&b(s^2-mb)\\b(s^2-mb)&b^2(s^2+m^2)\end{pmatrix}.
\]
In particular, \(\lim_{t\to\infty}\operatorname{Var}N(t)/\mathbb E N(t)=\mathcal F=(s^2+b^2)/(m+b)^2\). The covariance is negative for \(\gamma<\gamma_C=m/s^2\), zero at equality, and positive above it.

There is a **unique** \(r_*>0\), characterized by
\[
r_*\beta'(r_*)=1-e^{-\beta(r_*)},
\]
such that \(s^2>m^2\) exactly when \(r<r_*\). For \(0<r<r_*\) the second critical rate is
\[
\gamma_F=\frac{2m}{s^2-m^2}>\gamma_C.
\]
Thus \(\mathcal F<1\) for \(\gamma<\gamma_F\), \(\mathcal F=1\) at equality and \(\mathcal F>1\) for \(\gamma>\gamma_F\). For \(r\ge r_*\), \(\mathcal F<1\) at every finite \(\gamma>0\). Below \(r_*\), the three open phases are: negative covariance and sub-Poissonian counts for \(\gamma<\gamma_C\); positive covariance and still sub-Poissonian counts for \(\gamma_C<\gamma<\gamma_F\); positive covariance and super-Poissonian counts for \(\gamma>\gamma_F\). In the weak-reset limit,
\[
\lim_{r\downarrow0}\frac{\gamma_C}{r}=1,\qquad
\lim_{r\downarrow0}\frac{\gamma_F}{r}=2.
\]
The limits require \(t\to\infty\) at each fixed \(r>0\) before taking \(r\downarrow0\).

## Assumptions and scope
The particle moves on \([0,\infty)\) at velocity \(v\sigma_t\), with \(\sigma_t\in\{-1,+1\}\) reversing at independent exponential rate \(\alpha\). While unbound, an independent Poisson clock of rate \(r\) instantaneously changes the configuration to position \(x_0\) and orientation \(-1\). On reaching zero with orientation \(-1\), the particle is adsorbed: its position remains at zero, its bulk tumbling and bulk reset clock cease, and its bound sojourn is exponential with rate \(\gamma\). At desorption it instantaneously returns to \((x_0,-1)\), independently of past excursions. All clocks are independently restarted at renewal epochs. \(N(t)\) counts transitions from bulk to wall; \(H(t)=\int_0^t\mathbf1_{\{\text{bound at }s\}}\,ds\). The theorem concerns this desorption-induced-return protocol, not reflection or desorption back at zero. All parameters are fixed positive real numbers except in expressly stated one-sided limits.

## Proof
**1. Excursion transform.** For the unreset run-and-tumble motion, let \(f_\pm(x,z)=\mathbb E_{x,\pm}[e^{-zT_0}]\) for the first incoming hit of zero, \(z>0\). The backward equations are
\[
\pm v\,\partial_x f_\pm+\alpha(f_\mp-f_\pm)=zf_\pm,
\qquad f_-(0,z)=1,
\]
with the bounded-at-infinity solution. The decaying spatial eigenvalue is \(k(z)=\sqrt{z(z+2\alpha)}/v\), and therefore
\[
\phi_0(z):=\mathbb E_{x_0,-} e^{-zT_0}=e^{-x_0k(z)}.
\]
This is the standard first-passage input. For independent Poisson bulk resetting at rate \(r\), condition on whether the first reset precedes adsorption to obtain
\[
\phi_r(z)=\frac{(r+z)\phi_0(r+z)}{z+r\phi_0(r+z)}.
\]
Writing \(f=\phi_0(r)=e^{-\beta}\), logarithmic or ordinary differentiation at \(z=0\) yields
\[
\mathbb ET_r=\frac{1-f}{rf}=m,
\qquad \operatorname{Var}T_r
=\frac{1-f^2+2r\phi_0'(r)}{r^2f^2}=s^2.
\]
In the last expression \(\phi_0'(r)=-\beta'e^{-\beta}\). Since the probability of a direct leftward traversal of \(x_0\) without tumble/reset is strictly positive, independent repeated attempts imply an exponential tail bound on \(T_r\) and hence all the required moments.

**2. Joint regenerative covariance.** Let \(B\sim\operatorname{Exp}(\gamma)\) be independent of \(T_r\). A complete adsorption-to-adsorption cycle has duration \(C=B+T_r\), with vector reward \(Y=(1,B)\). These cycles are independent and identically distributed. Their means are \(\mathbb EC=\mu=m+b\) and \(\mathbb EY=(1,b)\), so the long-time mean rate vector is \(a=(1,b)/\mu\). The renewal-reward central limit theorem gives the covariance-rate matrix
\[
\Sigma=\frac{\mathbb E[(Y-aC)(Y-aC)^\mathsf T]}{\mathbb EC}.
\]
Its entries follow by expanding the centered independent variables \(T_r-m\), \(B-b\) with \(\operatorname{Var}(B)=b^2\). This gives exactly the matrix in the Finding. An initial incomplete cycle and the terminal incomplete cycle do not affect the rates or asymptotic variances: all cycles have exponential moments, the incomplete reward is bounded by the remaining cycle, and standard regenerative second-moment convergence applies. The same regenerative theorem gives \(\mathbb EN(t)/t\to1/\mu\), from which the Fano expression follows. (The distributional multivariate central limit theorem also holds with limiting normal covariance \(\Sigma\).)

**3. Count and covariance transitions.** The numerator of the cross covariance is \(b(s^2-mb)\), which changes sign only at \(b=s^2/m\), giving \(\gamma_C=m/s^2\). Also
\[
\mathcal F-1=\frac{s^2-m^2-2mb}{(m+b)^2}.
\]
If \(s^2\le m^2\), this is negative for all \(b>0\); otherwise it vanishes only at \(b=(s^2-m^2)/(2m)\). When the latter is positive, \(\gamma_F/\gamma_C=2s^2/(s^2-m^2)>2\), so the claimed strict ordering follows.

**4. Unique resetting crossover.** Substituting the excursion moments gives
\[
s^2-m^2=\frac{2e^\beta}{r^2}
\bigl(1-e^{-\beta}-r\beta'\bigr).
\]
The ratio
\[
\frac{r\beta'}{1-e^{-\beta}}=
\frac{r+\alpha}{r+2\alpha}
\frac{\beta}{1-e^{-\beta}}
\]
is strictly increasing in \(r>0\): the first factor increases and the second increases because \(x/(1-e^{-x})\) is strictly increasing on positive reals and \(\beta(r)\) increases. The product tends to \(1/2\) as \(r\downarrow0\), and diverges as \(r\to\infty\). Hence it crosses one exactly once, proving uniqueness and the strict sign classification.

**5. Weak-reset double boundary.** Since \(\beta(r)\sim (x_0/v)\sqrt{2\alpha r}\), one has \(m\sim (x_0/v)\sqrt{2\alpha}\,r^{-1/2}\) and \(s^2\sim (x_0/v)\sqrt{2\alpha}\,r^{-3/2}\); furthermore \(m^2/s^2\to0\). Substituting into both threshold definitions proves \(\gamma_C/r\to1\) and \(\gamma_F/r\to2\).

## Verification
The standalone file `verify.py` performs exact-event simulation of individual run-and-tumble excursions including tumble/reset competition, direct independent regenerative trajectory simulation for adsorption counts and bound-time covariance, a numerical root check for the unique crossover, and small-reset threshold checks. It uses NumPy and SciPy. Run `python verify.py` in the package directory. At \(v=\alpha=x_0=1\) the crossover root is approximately \(r_*=0.5041300402\). Five finite-time covariance/Fano experiments, three excursion moment experiments, and four weak-reset comparisons passed the scripted tolerances. These finite computations are corroboration, not a proof of the infinite-time or small-reset limits.

## Relationship to prior work
Bressloff and Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary* (arXiv:2602.02446v1, first posted February 2, 2026) derives the underlying sticky-boundary model, bulk first-passage and renewal formulas, stationary probabilities and mean first-passage observables. Its return-on-desorption model provides the natural regeneration points. The present result does not claim that regenerative moment formulas or the telegraph first-passage transform are new; it determines and classifies the **combined** adsorption-count Fano and count–bound-time covariance phase diagram, including unique resetting crossover and weak-reset universal threshold ratio.

Evans and Majumdar (arXiv:1808.06450v2) treat run-and-tumble resetting without the same bound-time observable. Akimoto (arXiv:2306.00359; Physical Review E 108, 054113) develops general alternating-renewal count and occupation statistics. Such general results supply methods and may imply pieces of the covariance matrix, but their accessible abstract does not provide the present model-specific double thresholds or unique resetting crossover. Bressloff (arXiv:2503.01304) investigates encounter/collision-count models with resetting, distinct from this desorption-induced return process.

## Limitations
The full covariance rate and phase classification concern **independent** exponential bound sojourns and return to \((x_0,-1)\) on desorption. They do not apply unchanged to desorption released at the sticky wall, heavy-tailed residence, bound-state resetting, partial absorption, or interacting particles. The small-reset thresholds are limits of stationary fluctuation rates for \(r>0\); at \(r=0\) the unreset half-line excursion has infinite mean. The originality comparison includes a relevant general renewal paper whose full text was not accessible; implicit prior coverage of some special formulas is a remaining risk. No independent audit is asserted.

## References
1. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446v1 (February 2, 2026). https://arxiv.org/html/2602.02446v1
2. T. Akimoto, *Statistics of the number of renewals, occupation times, and correlation in ordinary, equilibrium, and aging alternating renewal processes*, arXiv:2306.00359; Phys. Rev. E 108, 054113 (2023). https://arxiv.org/abs/2306.00359
3. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450v2. https://arxiv.org/abs/1808.06450
4. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle with stochastic resetting*, arXiv:2503.01304 (2025). https://arxiv.org/abs/2503.01304
