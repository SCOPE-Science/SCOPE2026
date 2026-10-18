# Exact side-of-arrival law for a transparent blinking Brownian target

## Finding

For Brownian motion on the real line with **position-only Poisson resetting** and a **transparent, stochastically blinking target**, the probability of first detection from the side *opposite* the resetting site admits a closed formula, despite the nonrenewal character of the unreset gate. Specifically, with target-active-to-inactive rate \(\alpha>0\), inactive-to-active rate \(\beta>0\), resetting rate \(r>0\), diffusivity \(D>0\), reset site \(x_0>0\), and the initial gate drawn from its stationary distribution, put

\[
\lambda=\alpha+\beta,\quad z=\sqrt{\frac r{r+\lambda}},\quad
h=\exp\!\left[-x_0\sqrt{\frac{r+\lambda}{D}}\right].
\]

The exact probability \(p_-\) of eventual capture at the origin *from the negative half-line* is

\[
\boxed{\displaystyle
p_- = \frac{\alpha}{2\lambda}(1-z)
\left(1+\frac r\lambda h\right).}
\]

The complementary probability of first detection from the positive, initially occupied half-line is exactly \(p_+=1-p_-\). If the initial gate is instead specified, the two conditional opposite-side probabilities are

\[
\boxed{\displaystyle
p_-^{A}=\frac{\alpha}{2\lambda}(1-z)(1-h),\qquad
p_-^{I}=\frac{1-z}{2\lambda}\bigl[\alpha+(r+\beta)h\bigr].}
\]

The formulas imply four sharp consequences for the *same* directional-capture observable:

1. Holding the gate rates, reset position, and diffusivity fixed, \(p_-\) is **strictly decreasing** in the resetting rate \(r\); it is strictly decreasing in \(x_0\) for each \(r>0\).
2. Holding the inactive fraction \(\pi_I=\alpha/\lambda\), reset rate, position, and diffusivity fixed, \(p_-\) is **strictly increasing** with the *overall gate-switching speed* \(\lambda\). Thus the limiting side law is singular even though the first-passage-time law approaches that of a continuously active target:
\[
\lim_{\lambda\to\infty\atop \alpha/\lambda=\pi_I}p_-=\frac{\pi_I}{2}>0
\quad(0<\pi_I<1).
\]
3. For fixed \(x_0>0\), \(p_-\sim \alpha/(4r)\) as \(r\to\infty\), while \(p_-\to\alpha/(2\lambda)\) as \(r\downarrow0\).
4. More sharply, the strong-reset regime has a *spatial boundary layer*: whenever \(r\to\infty\), \(x_0=x_0(r)>0\), and \(x_0\sqrt{r/D}\to\ell\in[0,\infty)\),
\[
\boxed{\displaystyle p_-\longrightarrow\frac{\alpha}{4\lambda}e^{-\ell}.}
\]
This finite crossover contrasts with \(p_-\to0\) at every fixed positive resetting distance.

## Assumptions and scope

The process \(X_t\) evolves with generator \(D\partial_x^2\) on the *entire* real line, so its infinitesimal variance is \(2D\,dt\). Independently, resetting events form a Poisson process of intensity \(r\) and instantaneously replace \(X_t\) by \(x_0>0\), **without changing the target's state**. The target at \(0\) has two independent Markov states: \(A\), active, and \(I\), inactive; the transitions are \(A\to I\) at rate \(\alpha\), and \(I\to A\) at rate \(\beta\). While inactive, the target is fully *transparent*: the Brownian particle may cross zero freely. While active, its first visit to zero terminates the path. Time zero starts at \(X_0=x_0\); the initial gate is either \(A\), \(I\), or drawn from the equilibrium law \(\Pr(J_0=A)=\beta/\lambda\), \(\Pr(J_0=I)=\alpha/\lambda\).

At the detection time \(\tau=\inf\{t\ge0:X_t=0,\ J_t=A\}\), the side of approach is the almost-sure strict sign of \(X_t\) just before \(\tau\), over a sufficiently short interval where \(J=A\) and no reset occurs. Since gate-switch and reset times have continuous distributions independent of Brownian trajectories, simultaneous gate switches/resets at hitting are null events. Throughout \(D,r,\alpha,\beta,x_0>0\), eventual detection occurs with probability one. The statements do not apply to a reflecting inactive target or to resetting that also refreshes the gate.

## Proof

**Step 1: the coupled backward boundary problem.** Write \(F_j(x)\) for the probability of *negative-side* capture from location \(x\) and initial gate state \(j\in\{A,I\}\), and set \(u_j=F_j(x_0)\). On each open half-line, the strong Markov property and independent competing exponential clocks give

\[
\begin{aligned}
D F_A''+\alpha(F_I-F_A)+r(u_A-F_A)&=0,\\
D F_I''+\beta(F_A-F_I)+r(u_I-F_I)&=0.
\end{aligned}
\tag{1}
\]

Because an active hit from the right contributes zero and one from the left, the *one-sided* Dirichlet data are \(F_A(0^+)=0\) and \(F_A(0^-)=1\). When the target is inactive, there is no interface force or killing, so \(F_I\) and \(F_I'\) are continuous at zero. Both components must remain bounded as \(|x|\to\infty\).

**Step 2: exact spatial solution.** Let

\[
Q=\begin{pmatrix}-\alpha&\alpha\\\beta&-\beta\end{pmatrix},\quad
\kappa=\sqrt{r/D},\quad \mu=\sqrt{(r+\lambda)/D},\quad
\mathbf1=(1,1)^T,\quad v=(\alpha,-\beta)^T.
\]

The eigenpairs of \(Q\) are \((\mathbf1,0)\) and \((v,-\lambda)\). A constant particular solution is \(g=r(rI-Q)^{-1}u\). Every bounded solution to (1) consequently has the form

\[
F(x)=\begin{cases}
 g+a e^{-\kappa x}\mathbf1+c e^{-\mu x}v,&x>0,\\
 g+b e^{\kappa x}\mathbf1+e e^{\mu x}v,&x<0.
\end{cases}
\tag{2}
\]

Project \(u=F(x_0)\) onto the \(\mathbf1\) eigenspace. Since \(r(rI-Q)^{-1}\) acts as identity there, \(a e^{-\kappa x_0}=0\), hence \(a=0\). The active boundary difference and the inactive continuity yield \(b=\beta(e-c)\) and \(b+\alpha(e-c)=1\), so

\[
 e-c=\frac1\lambda,\qquad b=\frac\beta\lambda.
\]

Continuity of \(F_I'\) gives \(\mu(c+e)=\kappa/\lambda\). Solving,

\[
 c=\frac{z-1}{2\lambda},\qquad e=\frac{z+1}{2\lambda},\qquad b=\frac\beta\lambda.
\tag{3}
\]

The active right-side boundary now says \(g_A=-\alpha c\). The \(v\)-component of \(g=r(rI-Q)^{-1}u\), combined with \(u=F(x_0)\), gives \(g_A-g_I=rc h\), hence \(g_I=-c(\alpha+rh)\). At \(x=x_0\), (2) therefore yields

\[
 u_A=-\alpha c(1-h),\qquad
 u_I=-c\bigl[\alpha+(r+\beta)h\bigr].
\tag{4}
\]

Substituting (3) establishes both conditional formulas. Weighted by the stationary initial gate law, (4) reduces algebraically to the stated \(p_-\). The formulas obey \(0<u_A,u_I<1\), as required. To identify this bounded solution as the capture probability uniquely, observe that after each reset there is, uniformly over the two gate states, a strictly positive probability of reaching an active target before the next reset. This follows by requiring a short interval of suitable gate behavior and a Brownian first passage within that interval. Therefore the number of resets before detection is dominated by a geometric random variable, and \(\tau<\infty\) almost surely. The standard stopped backward martingale argument then identifies the bounded boundary solution with the desired hitting probability; a difference of two bounded solutions has zero terminal contribution at \(\tau\) and thus vanishes.

**Step 3: strict monotonicity in reset rate and resetting distance.** Put \(z=\sqrt{r/(r+\lambda)}\). Then \(r/\lambda=z^2/(1-z^2)\), and

\[
\frac{2\lambda p_-}{\alpha}=1-z+\frac{z^2}{1+z}h(z),\quad
h(z)=\exp\!\left[-x_0\sqrt{\frac{\lambda}{D(1-z^2)}}\right].
\]

Here \(z\) rises strictly with \(r\), and \(h'(z)<0\). The derivative of the right-hand side is

\[
-1+\left(1-\frac1{(1+z)^2}\right)h(z)+\frac{z^2}{1+z}h'(z)<0,
\]

because \(0<h(z)<1\). Differentiating the original formula with respect to \(x_0\) proves strict negativity when \(r>0\).

**Step 4: strict monotonicity in switching speed and the singular limit.** Keep \(\pi_I=\alpha/\lambda\) fixed and vary \(\lambda\). For the fixed number \(a=x_0\sqrt{r/D}>0\), now \(h=e^{-a/z}\) and

\[
\frac{2p_-}{\pi_I}=G_a(z)=1-z+\frac{z^2}{1+z}e^{-a/z}.
\]

For each \(z\in(0,1)\), its derivative is

\[
G_a'(z)=-1+e^{-a/z}\left[\frac{z(2+z)}{(1+z)^2}+\frac{a}{1+z}\right].
\]

The bracketed expression multiplied by \(e^{-a/z}\) strictly decreases as a function of \(a\ge0\): its derivative in \(a\) is

\[
-e^{-a/z}\left[\frac1{(1+z)^2}+\frac{a}{z(1+z)}\right]<0.
\]

At \(a=0\), that product equals \(1-(1+z)^{-2}<1\). Therefore \(G_a'(z)<0\). Since \(z\) decreases strictly when \(\lambda\) increases, \(p_-\) strictly increases with gate-switching speed. The fast-switching limit has \(z\to0\), \(e^{-a/z}\to0\), and hence \(p_-\to\pi_I/2\). A permanently active target instead gives opposite-side probability zero; these are different pathwise observables despite convergence of the ordinary hitting-time law.

**Step 5: asymptotic boundaries.** As \(r\downarrow0\), \(z\to0\) and \(rh\to0\), giving \(p_-\to\alpha/(2\lambda)\). For fixed positive \(x_0\) and \(r\to\infty\), \(1-z=\lambda/(2r)+O(r^{-2})\), while \(rh\) is exponentially small in \(\sqrt r\), yielding \(p_-\sim\alpha/(4r)\). Finally, if \(x_0\sqrt{r/D}\to\ell\), then \(h\to e^{-\ell}\) and the term \((1-z)(r/\lambda)h\to\tfrac12e^{-\ell}\); the other term vanishes, giving the asserted \(\alpha e^{-\ell}/(4\lambda)\) boundary-layer profile. All these limits concern the *exact first-detection side* and not a finite-time approximation.

## Verification

The accompanying dependency-free `check.py` reconstructs the piecewise backward solution, verifies both generator equations at several points on each side, verifies the active boundary data and inactive value/derivative matching, checks the conditional and stationary normalizations, and numerically probes the derived monotonicity and limits. It completed 135 deterministic analytic-residual, algebraic, and limiting checks. Additionally, a separate event-interval Brownian-bridge simulation, independent of the backward-equation calculation, was run in four parameter regimes (12,000 trajectories each). Within each interval between reset/gate events, the bridge's conditional zero-crossing probability is evaluated from the exact Brownian reflection principle, rather than from time-discretized endpoints; all four empirical probabilities agreed with the formula within the declared statistical tolerances. These finite tests are consistency checks only; the proof in the previous section establishes the universally quantified statements.

Reproduce by running `python check.py` with Python 3.10 or later; it requires only the standard library. The checker is included in full alongside the six textual files.

## Relationship to prior work

Żbik, Dybiec, Capała, Palmowski, and Sokolov [1] developed the transparent two-state blinking-target model under position resetting and derived Laplace-transform first-passage-time laws and mean times. They presented the probability of capture from the original side numerically (their discussion of Fig. 5), rather than as an exact side-resolved hitting probability. Their first-passage-time laws are *not* presented as new here. The contribution here is the closed **side-of-approach** law and its exact switching/resetting monotonicities and singular scaling limits. In particular, knowing the first-detection-time distribution alone does not record the arrival side.

Bressloff [2] and Mercado-Vásquez–Boyer [3] study stochastic gating with resetting and first-passage observables. Their one-dimensional inactive targets impose reflective half-line boundary conditions, unlike the transparent interface here; consequently, these formulations do not provide the probability of approach from the opposite half-line. Bressloff [4] also develops renewal techniques and finite-interval gated-boundary splitting, but the reported splitting is between spatially distinct absorbing endpoints, not the directional side of the *same* transparent target. These distinctions were checked at the level of mathematical boundary conditions and asserted observables, not merely title similarity. A general matrix-valued backward boundary-value theory can furnish the *method*, and earlier comprehensive treatments may implicitly contain this specialization. No claim of mathematically certified historical priority is made.

## Limitations

The result is for a single dimension, strictly positive gate and reset rates, diffusion with no drift, a fixed positive resetting location, fully transparent inactivity, and particle-only resetting. Its singular fast-gating limit shows that the *approach-side* marking is not continuous under replacement of a fast-blinking target by a continuously active one; it must not be transferred to the continuously active model. Neither the joint distribution of detection time and side nor side-conditioned detection times are determined here. The boundary-layer limit is a simultaneous \(r\to\infty\), \(x_0(r)\to0^+\) regime; it is not a statement about side identification when the particle starts exactly at zero. Other classes of recurrent diffusions, non-Poisson resets and nonequilibrium initial gate laws need separate analysis. Independent mathematical and literature validation have not been performed.

## References

[1] B. Żbik, B. Dybiec, K. Capała, Z. Palmowski, I. M. Sokolov, *Hitting the blinking target under stochastic resetting*, arXiv:2512.09739 (first public version December 10, 2025), https://arxiv.org/abs/2512.09739 . Full open version: https://arxiv.org/html/2512.09739v2 .

[2] P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (2020), https://arxiv.org/abs/2009.02739 .

[3] I. N. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148 (2021), https://arxiv.org/abs/2107.02148 .

[4] P. C. Bressloff, *Renewal theory for Brownian motion with stochastically gated targets*, arXiv:2601.01588 (2026), https://arxiv.org/abs/2601.01588 .
