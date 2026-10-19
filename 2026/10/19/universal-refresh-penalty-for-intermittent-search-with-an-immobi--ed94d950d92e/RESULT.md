# Universal refresh penalty for intermittent search with an immobilized state

## Finding
Consider a searcher that alternates independently between an active Markov search state and a completely immobilized state. At each Poisson position-reset event, the internal state is refreshed from its stationary distribution with probability \(\eta\in[0,1]\) and otherwise retained. If the off-to-on and on-to-off rates are \(\alpha,\beta>0\), and the reset rate is \(r>0\), then, when the particle begins at the reset point with its internal state stationary, its mean absorption time is
\[
M_\eta=\frac{\alpha+\beta}{\alpha q}\left(\frac1{F(q)}-1\right)+\frac{\beta}{\alpha(\alpha+\beta+r\eta)},\qquad
q=\frac{r(\alpha+\beta+r)}{\alpha+r}.
\]
Here \(F(q)=\mathbb E_{x_*}[e^{-q\tau};\tau<\infty]\), where \(\tau\) is the first absorption time of the *active-only* Markov motion without switching or resets. In particular, for any \(0\le\eta<\eta'\le1\),
\[
M_\eta-M_{\eta'}=\frac{\beta}{\alpha}\left(\frac1{\alpha+\beta+r\eta}-\frac1{\alpha+\beta+r\eta'}\right)>0.
\]
Thus the entire improvement due to internal-state refreshing is independent of the active search law, spatial geometry, starting/reset location and first-passage transform. Moreover, the mean absorption time starting **active** at the reset site is exactly independent of \(\eta\).

## Assumptions and scope
Let \(Y\) be a nonexplosive time-homogeneous strong Markov search process on a state space \(E\) with absorbing target \(A\), and fix a reset state \(x_*\in E\setminus A\). Its active-only first hitting time is \(\tau=\inf\{t\ge0:Y_t\in A\}\). Assume \(0<F(q)\le1\) at the displayed \(q>0\). For definiteness assume \(x_*\) cannot be absorbed at time zero. While active, the spatial coordinate evolves as an independent copy of \(Y\), restarted from its current state whenever reactivated. While inactive, the spatial coordinate is frozen and the target cannot be hit; all other internal memory is absent. Off-to-on switching occurs at constant rate \(\alpha>0\), and on-to-off at constant rate \(\beta>0\), independently of the spatial motion and reset alarms. Every reset alarm, of independent Poisson rate \(r>0\), places the spatial coordinate at \(x_*\). With probability \(\eta\), the internal state is redrawn from the stationary distribution \(\pi_0=\beta/(\alpha+\beta)\), \(\pi_1=\alpha/(\alpha+\beta)\); otherwise its current value is retained. All randomness used in refreshing is independent. The initial coordinate is \(x_*\), and the initial internal state is sampled from \(\pi\). A target hit terminates the search. The active-only hitting time need not have a finite mean and the active process may have nonunit eventual hitting probability. No claim is made for resets changing the active motion's hidden variables, for an immobile state with nonzero movement, or for nonexponential switching.

## Proof
Write \(a=u_1(x_*)\), \(b=u_0(x_*)\) for mean absorption times starting at \(x_*\) in the active and inactive states. Put \(S=\alpha+\beta\) and \(T=\pi_1a+\pi_0b\). At \(x_*\), a reset without a refresh does nothing to an inactive particle. First-step conditioning during the inactive holding time gives
\[
\alpha(a-b)+r\eta(T-b)=-1,
\qquad b-a=\Delta=\frac{S}{\alpha(S+r\eta)}.
\]
This identity holds for any active motion. Let \(u_i(z)\) denote the corresponding mean time from a general nonabsorbed state \(z\) while internal state \(i\). The inactive equation yields
\[
(\alpha+r)u_0(z)=\alpha u_1(z)+r[b-\eta\pi_1\Delta]+1.
\]
In the active equation, the instantaneous spatial generator is \(L\), and a reset gives the new mean \(a+\eta\pi_0\Delta\). Substitution into the active first-step equation gives
\[
L u_1(z)+q[a-u_1(z)]=-B,
\quad q=r\left(1+\frac{\beta}{\alpha+r}\right),\quad B=1+\frac\beta\alpha=\frac S\alpha.
\]
The cancellation making the forcing exactly \(B\) is checked algebraically:
\[
\frac{\beta}{\alpha+r}+r\Delta\left[\frac{\beta(1-\eta\pi_1)}{\alpha+r}+\eta\pi_0\right]=\frac\beta\alpha.
\]
The reduced equation is the backward equation of *active-only* search with independent Poisson resets to \(x_*\) at rate \(q\), with time cost multiplied by \(B\). By the renewal decomposition of an attempt ending at either absorption or an exponential reset, an attempt succeeds with probability \(F(q)>0\) and has mean length \((1-F(q))/q\). Therefore its mean total duration is \((1-F(q))/(qF(q))\), and
\[
a=\frac{B}{q}\left(\frac1{F(q)}-1\right).
\]
The positive success probability also proves finite mean completion, justifying the backward equations and their finite minimal solution; the reduction can alternatively be obtained directly by first-event conditioning without generator-domain regularity. Averaging the two initial internal states gives \(T=a+\pi_0\Delta\), proving the first displayed formula and the strict difference formula. The expression for \(a\) does not depend on \(\eta\). If \(\beta=0\), the penalty vanishes, consistent with permanent mobility; the theorem itself assumes strictly positive switching rates.

## Verification
The standalone `verify.py` builds finite absorbed Markov generators with independently varied asymmetric jump rates, switches and resets, then solves their full state-conditioned mean hitting-time equations. It computes \(F(q)\) separately from the active-only killed generator and compares the formula for active, inactive-minus-active, and stationary-average means, across six refresh probabilities. Running `python verify.py` with NumPy and SciPy produces 864 independent finite-generator comparisons, with maximum absolute discrepancy about \(1.35\times10^{-12}\). The proof is analytic and holds beyond the finite-state examples. For Brownian mobile search on a half-line with diffusion coefficient \(D>0\), absorbing origin and reset position \(x_*>0\), \(F(q)=e^{-x_*\sqrt{q/D}}\), giving an explicit physical specialization.

## Relationship to prior work
Evans and Majumdar (2018) developed a renewal description of run-and-tumble search with position-only versus velocity-randomizing reset protocols; their two *moving ballistic* velocity states are different from an active/frozen transport state, and their protocol-dependent expressions do not assert a geometry-independent additive refresh penalty for arbitrary active Markov motion. Bressloff (2020) investigated two *diffusing* internal states when each reset also refreshes the diffusion state; its analyzed protocol does not compare a continuous partial-refresh interpolation against state retention. The renewal identity for Poisson resetting is established background, not claimed new. The present result is the precise protocol-invariance of the active-start mean and universal rational penalty for a **strictly immobilized** state, valid for arbitrary active Markov dynamics.

## Limitations
The model requires an entirely frozen off state, exponential independent switching, constant Poisson reset rate, a single fixed spatial reset point, and stationary internal initialization for the averaged formula. The complete active-search dependence is hidden in \(F(q)\); the theorem does not determine this transform for general geometry. A general statement about faster completion in the sense of stochastic ordering is not proved; only mean times are compared. An independent priority assessment remains necessary, especially because the conclusion may be derivable from general matrix-renewal treatments not explicitly specialized to frozen-state transport.

## References
1. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, Journal of Physics A **51** (2018), 475003; arXiv:1808.06450, first posted 20 August 2018, https://arxiv.org/abs/1808.06450.
2. P. C. Bressloff, *Switching diffusions and stochastic resetting*, Journal of Physics A **53** (2020), 275003, DOI:10.1088/1751-8121/ab97e0, first verified public appearance by 17 June 2020.
3. M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A **53** (2020), 193001; arXiv:1910.07993.
