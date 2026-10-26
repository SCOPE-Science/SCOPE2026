# An exponential-reset rigidity theorem for ordinary renewal representations of lattice walks

## Finding

Fix a symmetric continuous-time nearest-neighbor walk on the integers with independent Poisson jumps at rate \(\lambda>0\). Independently, reset its position to the origin and restart its jump clock at times of an ordinary renewal process with identically distributed strictly positive interreset times. Denote the reset walk by \(Y_t\).

**Theorem (sharp ordinary-renewal representation criterion).** There exists a wait-first, no-reset continuous-time random walk \(Z_t\), started at zero, with independent equiprobable \(+1\) and \(-1\) spatial jumps and independent, identically distributed waiting times in \((0,\infty]\), such that
\[
\mathcal L(Z_t)=\mathcal L(Y_t)\qquad\text{for every }t\ge0,
\]
**if and only if** the interreset survival function is \(\Phi(t)=e^{-rt}\) for a single \(r\ge0\). The endpoint \(r=0\) means there are no resets; if the resetting intervals are required finite almost surely, then \(r>0\).

When this representation exists its waiting law is unique, with
\[
\Pr(W\in du)=\lambda e^{-(\lambda+r)u}\,du\quad(u>0),\qquad
\Pr(W=\infty)=\frac r{\lambda+r}.
\]
In particular, **for positive resetting rate no ordinary no-reset CTRW having almost-surely finite iid waiting times has all these one-time laws**. The unique allowed surrogate can be realized as the underlying, unreset Poisson walk permanently stopped at an independent exponential time of rate \(r\).

Even though the two processes have equal position distributions at every fixed time, for \(r>0\) and \(0<s<t\) they have different temporal correlations:
\[
\mathbb E[Y_sY_t]=\frac\lambda r(1-e^{-rs})e^{-r(t-s)},\qquad
\mathbb E[Z_sZ_t]=\frac\lambda r(1-e^{-rs}).
\]
For every fixed \(\delta>0\), their pathwise time-averaged squared displacements are maximally separated:
\[
\lim_{T\to\infty}\frac1T\int_0^T(Y_{t+\delta}-Y_t)^2dt
 =\frac{2\lambda}r(1-e^{-r\delta})\quad\text{a.s.},
\]
whereas the identical average for \(Z\) tends to zero almost surely. The covariance and ergodic mechanisms are standard; the claimed contribution is the **if-and-only-if characterization, including uniqueness and the defective-wait obstruction**, together with this exact characterization's trajectory-level interpretation.

## Assumptions and scope

The underlying lattice walk has total jump rate \(\lambda\) and symmetric steps, independently of the resetting times. Between resets it begins afresh at zero. Interreset times \(T_1,T_2,\ldots\) are iid in \((0,\infty]\), are independent of jumps, and define a nonexplosive ordinary renewal process whose first interval is distributed as subsequent intervals. A value \(\infty\) means no further reset. The survival function \(\Phi(t)=\Pr(T_1>t)\) is right-continuous, with \(\Phi(0)=1\); atoms at strictly positive deterministic times are allowed. For uniqueness, a surrogate means a **wait-first ordinary** renewal CTRW: the first waiting time has exactly the same law as later waiting times, and each spatial jump is independent of all waiting times. This restriction is essential: an arbitrary nonrenewal counting process is not excluded.

The characterization concerns equality of one-time position laws for **all real times** and the **same symmetric nearest-neighbor jump kernel**. It makes no assertion about arbitrary alternative jump kernels, delayed/nonidentical renewal times, or a pathwise coupling preserving reset trajectories.

## Proof

**1. Transform of the reset-aged jump count.** Let \(C_t\) count the underlying \(\pm1\) jumps *since the latest reset* (not the cumulative number of jumps since time zero) and set \(G(z,t)=\mathbb E[z^{C_t}]\), \(0\le z\le1\). Conditioning on the first resetting time gives the exact renewal equation
\[
G(z,t)=\Phi(t)e^{-\lambda(1-z)t}+
\int_{(0,t]}G(z,t-u)\,\Pr(T_1\in du).
\]
Write \(F(s)=\int_0^\infty e^{-st}\Phi(t)\,dt\), \(s>0\). Since the reset-interval Laplace transform equals \(1-sF(s)\), the temporal Laplace transform of the renewal equation yields
\[
\widehat G(z,s)=\int_0^\infty e^{-st}G(z,t)dt
 =\frac{F(s+\lambda(1-z))}{sF(s)}. \tag{1}
\]
This formula is valid for arbitrary reset-interval laws under the stated nonexplosion assumptions, including laws with atoms and a mass at infinity.

**2. Spatial equality identifies the counting law.** Given \(C_t=n\), the characteristic function of \(Y_t\) is \((\cos\theta)^n\), so \(\mathbb E[e^{i\theta Y_t}]=G(\cos\theta,t)\). The same formula holds for a candidate surrogate with ordinary renewal count \(K_t\). Equality of the position laws for all \(t\ge0\) makes the generating functions equal for \(-1\le z\le1\), hence for \(0\le z\le1\). In particular their joint time-Laplace transforms in (1) must be equal for every such \(z\) and every \(s>0\). No inference about count laws from a single moment is used.

**3. Ordinary-renewal factorization is rigid.** Define \(w(s)=\mathbb E[e^{-sW};W<\infty]\), allowing \(\Pr(W=\infty)>0\). Elementary renewal counting gives
\[
\int_0^\infty e^{-st}\mathbb E[z^{K_t}]dt
=\frac{1-w(s)}{s(1-zw(s))}. \tag{2}
\]
Comparing (1) and (2), for any \(s>0\) and \(z\in[0,1]\),
\[
\frac{F(s+\lambda(1-z))}{F(s)}
=\frac{1-w(s)}{1-zw(s)}. \tag{3}
\]
In particular \(1-w(s)=F(s+\lambda)/F(s)>0\). Put \(u=s+\lambda(1-z)\); rearranging (3) shows
\[
\frac1{F(u)}=\frac1{F(s)}
\left(1+\frac{w(s)}{\lambda(1-w(s))}(u-s)\right),
\qquad s\le u\le s+\lambda. \tag{4}
\]
Thus \(u\mapsto 1/F(u)\) is affine on every interval \([s,s+\lambda]\). These intervals overlap throughout \((0,\infty)\), so this function is globally affine, say \(1/F(s)=as+b\). Since \(T_1>0\) almost surely, \(\lim_{s\to\infty}sF(s)=\Phi(0)=1\), hence \(a=1\). The bound \(F(s)\le1/s\) gives \(b\ge0\). Therefore
\[
F(s)=\frac1{s+r},\quad r=b\ge0.
\]
Uniqueness of Laplace transforms, together with right-continuity of survival functions, yields \(\Phi(t)=e^{-rt}\) for all \(t\ge0\). This proves necessity without assuming density or differentiability of the reset law.

**4. Converse and uniqueness.** When \(\Phi(t)=e^{-rt}\), substitute \(F(s)=1/(s+r)\) in (3), and set \(z=0\) to deduce uniquely
\[
w(s)=\frac\lambda{s+\lambda+r}.
\]
Its inverse Laplace–Stieltjes law is \(\lambda e^{-(\lambda+r)u}du\) over finite \(u\), with remaining mass \(r/(\lambda+r)\) at infinity. Substitution in (1) and (2), then uniqueness of the temporal Laplace transform and the count generating function, establishes equality of all one-time distributions. Both processes start at zero; probability laws are right-continuous in time, so equality initially obtained almost everywhere extends to every \(t\ge0\). This proves sufficiency and uniqueness.

An explicit realization takes independent jump and killing clocks of rates \(\lambda\) and \(r\). If a jump occurs first the process steps and restarts both clocks; if killing occurs first the process stays at its current position forever. Exponential memorylessness makes its next-jump waiting time precisely the defective law above, and its trajectory is distributed as \(Z_t=X_{t\wedge E}\) for an independent \(E\sim\mathrm{Exp}(r)\).

**5. Identical marginals do not identify motion.** For the reset walk, \(\mathbb E[Y_t]=0\) and \(\mathbb E[Y_t^2]=\lambda(1-e^{-rt})/r\). Conditional on \(Y_s\) and on the absence or occurrence of a reset during \((s,t]\), the future conditional mean equals \(e^{-r(t-s)}Y_s\), because a reset erases the prior position. This gives the displayed reset covariance. The stopped Poisson walk is a square-integrable martingale, so \(\mathbb E[Z_t\mid\mathcal F_s]=Z_s\) and \(\mathbb E[Z_sZ_t]=\mathbb E[Z_s^2]\), equal to the same one-time variance.

For the time average, construct a stationary version of the reset walk using a two-sided Poisson reset point process with independently marked Poisson-walk excursions. That marked process is stationary and ergodic under time shifts. At every fixed \(\delta>0\), its squared displacement over lag \(\delta\) is integrable, and the continuous-time ergodic theorem gives the stationary expectation as almost-sure time average. From the stationary variance \(\lambda/r\) and covariance \((\lambda/r)e^{-r\delta}\), the expectation is \(2\lambda(1-e^{-r\delta})/r\). Coupling the walk started at the origin to the stationary version after the first positive reset changes the time integral only over a finite random initial interval, whose contribution divided by \(T\) vanishes. Finally, \(Z\) is constant after its almost-surely finite killing time \(E\); its squared increments vanish whenever \(t\ge E\), so its time average tends to zero. This proves the claimed pathwise distinction.

## Verification

The standalone `verification.py` uses two independent finite-state generators (a reset walk and a permanently killed/stopped walk), computes all relevant spatial and two-time matrix propagators, and checks them against the formulas. It also independently compares the exact Laplace/count transforms for exponential resetting and checks obstruction for deterministic resetting across a grid of parameters. Run `python verification.py` with NumPy and SciPy installed. The script reports 207 passing numerical diagnostics. Finite-dimensional truncation is controlled by choosing a spatial window large relative to the tested jump and observation scales; it is **not** used to establish the theorem for all \(t\) or all reset laws.

An illustrative deterministic-reset failure is obtained from \(\Phi(t)=\mathbf1_{\{t<a\}}\), for which \(F(s)=(1-e^{-as})/s\); its reciprocal is not affine on positive intervals. Thus the ordinary-renewal representation fails for *every* finite deterministic interreset period, not merely the numerical test values.

## Relationship to prior work

Colantoni and Pagnini [1] derive the general renewal equation for one-time reset-CTRW marginals, especially their Eqs. (8)–(12), and study a Montroll–Weiss-like representation involving generally index-dependent coefficients in Eqs. (20)–(23). Their counting process need not be an ordinary iid-renewal count. The present result specializes to the Poisson nearest-neighbor jump clock and characterizes **exactly when** that stronger iid-wait property is possible, allowing defective waits. The general spatial renewal representation itself is established prior work.

Godrèche and Luck [2] derive a dressed ordinary-renewal description for the **total number of internal events accumulated across all reset cycles** under Poisson resetting (their Section 6.2). They separately study the number occurring in the *last* reset interval (their Section 8). The latter is the count needed for reset positions, not the cumulative event count. Their dressed total-event theorem therefore does not imply the present ordinary-renewal criterion; nor is the difference between the two counts denied here.

Bodrova and Sokolov [3] analyze complete versus incomplete resetting and the one-time displacement and scaling laws under power-law reset intervals. Their results do not supply the necessity-and-sufficiency ordinary-renewal representation theorem, and this finding makes no claims about their asymptotic regimes. Stojkoski and colleagues [4] establish two-time correlations and time-averaged observables for reset diffusion. The temporal decorrelation phenomenon is therefore not claimed as independently novel; it is used here as an exact, lattice-walk witness to the representational ambiguity.

## Limitations

This theorem only covers the prescribed symmetric nearest-neighbor spatial-jump kernel, a homogeneous Poisson underlying jump clock, and ordinary iid-renewal surrogates with possible infinitely long waiting times. Non-Poisson underlying CTRWs, altered spatial jump distributions, delayed renewals and arbitrary nonrenewal counts require different analyses. A mass at infinite waiting time is not standard in every definition of CTRW; if waiting times must be proper finite random variables, **no** positive-rate resetting has an ordinary-renewal surrogate. The theorem concerns all one-time distributions, not finite-dimensional trajectory equality, which explicitly fails for positive resetting rate.

The structural affine-rigidity conclusion follows from an elementary transform identity; a more general uninspected renewal-theoretic theorem may subsume it. No independent external validation or literature-wide priority guarantee is asserted.

## References

[1] F. Colantoni and G. Pagnini, *Master equations for continuous-time random walks with stochastic resetting*, arXiv:2507.07590, first public 10 July 2025. https://arxiv.org/html/2507.07590

[2] C. Godrèche and J.-M. Luck, *Replicating a renewal process at random times*, arXiv:2309.06997, 2023. https://arxiv.org/abs/2309.06997

[3] A. S. Bodrova and I. M. Sokolov, *Continuous time random walks under power-law resetting*, arXiv:2001.01350, 2020. https://arxiv.org/html/2001.01350v3

[4] V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686, 2021. https://arxiv.org/abs/2107.11686
