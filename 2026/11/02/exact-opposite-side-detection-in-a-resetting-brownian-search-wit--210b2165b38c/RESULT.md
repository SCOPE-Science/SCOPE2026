# Exact opposite-side detection in a resetting Brownian search with a transparent blinking target

## Finding

Consider a Brownian particle with generator \(D\partial_x^2\) on \(\mathbb R\), initialized and independently reset by a Poisson clock of rate \(r>0\) to \(a>0\). Its target is the origin. An independent stationary two-state gate changes from active to inactive and back, at rate \(\gamma>0\) in each direction. The gate is not reset. An active target kills the particle at its first contact with zero; an inactive target is transparent. Let \(P_-(r,\gamma;a,D)\) be the probability that the ultimately successful contact approaches zero from the *negative* half-line, for an initially stationary gate.

Set \(k=\sqrt{r/D}\) and \(h=\sqrt{(r+2\gamma)/D}\). Then

\[
\boxed{P_-=\frac14\left[1-\frac{k}{h}+\frac{k^2}{h(h+k)}e^{-ah}\right].}
\]

For every fixed \(a,D>0\), this probability is strictly decreasing in the resetting rate \(r>0\) and strictly increasing in the gate-switching rate \(\gamma>0\), and satisfies \(0<P_-<1/4\). Its sharp boundary limits are

\[
\begin{aligned}
\lim_{r\downarrow0}P_-&=\tfrac14,&
\lim_{r\to\infty}P_-&=0,\\
\lim_{\gamma\downarrow0}P_-&=\tfrac18 e^{-a\sqrt{r/D}},&
\lim_{\gamma\to\infty}P_-&=\tfrac14.
\end{aligned}
\]

The two fast-rate limits do not commute:

\[
\lim_{r\to\infty}\lim_{\gamma\to\infty}P_-=\tfrac14,
\qquad
\lim_{\gamma\to\infty}\lim_{r\to\infty}P_-=0.
\]

In particular, the fast-switching limit retains one-quarter opposite-side detection, whereas a target that is *active at every time* has zero opposite-side detection. This is a singular limit of the side-of-detection observable; it does not assert failure of convergence of first-passage times.

## Assumptions and scope

The process starts at \(X_0=a>0\). Between resets, \(dX_t=\sqrt{2D}\,dB_t\), with \(D>0\). The reset clock, Brownian motion, and gate are independent. Every reset maps the position to \(a\) and leaves the gate unchanged. The gate has generator \(\bigl(\begin{smallmatrix}-\gamma&\gamma\\\gamma&-\gamma\end{smallmatrix}\bigr)\), and is initially active or inactive with probability \(1/2\) each. Absorption occurs at the first \(t\) with \(X_t=0\) and active gate. A successful contact has an almost-surely well-defined incoming side: the active gate does not switch at the instant of contact, and over its active interval the killed path approaches from one open half-line.

All formulas concern the infinite-time eventual detection event in continuous Brownian time, not a discrete-time sign-change detector. The strictly positive-rate theorem does not assign a probability at the degenerate exactly frozen inactive gate; the one-sided \(\gamma\downarrow0\) limit is taken after eventual absorption.

## Proof

**1. Almost-sure absorption and backward equations.** Let \(u_A(x)\), \(u_I(x)\) denote the probabilities of eventual absorption from the negative side, conditional on gate state \(A\) or \(I\) at position \(x\). Each reset begins at \(a\). Uniformly over the two gate states, there is a strictly positive probability that the gate becomes active if necessary and then remains active during a specified interval while Brownian motion reaches zero before the next reset. The strong Markov property at reset epochs therefore bounds the number of unsuccessful reset epochs by a geometric tail; absorption occurs almost surely. The bounded backward equations away from zero are

\[
\begin{aligned}
D u_A''+\gamma(u_I-u_A)+r[u_A(a)-u_A(x)]&=0,\\
D u_I''+\gamma(u_A-u_I)+r[u_I(a)-u_I(x)]&=0.
\end{aligned}
\]

They have the side-resolved active-boundary conditions \(u_A(0+)=0\), \(u_A(0-)=1\). Since the inactive target does not interact with the particle, \(u_I\) and \(u_I'\) are continuous at zero. Boundedness holds at both infinite ends. The backward equations have at most one bounded probabilistic solution, by stopped-process martingale optional stopping at absorption and bounded convergence (or by the maximum principle with almost-sure killing).

**2. Two resolvent modes.** Put \(u_+=(u_A+u_I)/2\), \(u_-=(u_A-u_I)/2\), and \(U_\pm=u_\pm(a)\). Then

\[
D u_+''-r(u_+-U_+)=0,\qquad
D u_-''-(r+2\gamma)u_-+rU_-=0.
\]

Set \(c=r/(r+2\gamma)=k^2/h^2\). Boundedness on the positive half-line and the self-consistency condition at the reset point force

\[
u_+(x)=U_+,\quad
u_-(x)=cU_-+B_+e^{-hx}\qquad(x>0),
\]

where \(B_+=(1-c)U_-e^{ha}\). For \(x<0\), write

\[
u_+(x)=U_++A_-e^{kx},\qquad
u_-(x)=cU_-+B_-e^{hx}.
\]

The active jump conditions and continuity of both the inactive value and its derivative give exactly

\[
A_-=\tfrac12,\qquad
B_+=-\frac{h-k}{4h},\qquad
B_-=\frac{h+k}{4h}.
\]

Consequently

\[
U_-=-\frac{h}{4(h+k)}e^{-ha},
\qquad
U_+=\frac{h-k}{4h}+\frac{k^2}{4h(h+k)}e^{-ha}.
\]

Since the initial gate is stationary, \(P_-=\frac12[u_A(a)+u_I(a)]=U_+\), proving the formula. The displayed mode solutions directly satisfy all differential, reset, boundary, and matching conditions; uniqueness identifies them with the sought probabilities. For a deterministic initial gate, the corresponding additional exact formulas are

\[
\begin{aligned}
P_-^{A}&=\frac{h-k}{4h}(1-e^{-ah}),\\
P_-^{I}&=\frac{h-k}{4h}+\frac{h^2+k^2}{4h(h+k)}e^{-ah}.
\end{aligned}
\]

Their arithmetic mean equals \(P_-\).

**3. Strict monotonicity.** Write \(t=k/h\in(0,1)\), \(z=ah>0\). Four times the probability is

\[
F(t,z)=1-t+\frac{t^2}{1+t}e^{-z}.
\]

For fixed \(\gamma\), increasing \(r\) strictly increases both \(t\) and \(z\). We have

\[
\partial_tF=-1+\frac{t(2+t)}{(1+t)^2}e^{-z}<0,
\qquad
\partial_zF=-\frac{t^2}{1+t}e^{-z}<0.
\]

Thus \(P_-\) strictly decreases with \(r\). For fixed \(r\), increasing \(\gamma\) increases \(h\), whereas \(k\) is fixed. Direct differentiation gives

\[
\frac{dF}{dh}=\frac{k}{h^2}\left[1-e^{-z}\left(\frac{tz}{1+t}+\frac{t(2+t)}{(1+t)^2}\right)\right]>0.
\]

Indeed \(0<t/(1+t)<t(2+t)/(1+t)^2<1\), and \(e^{-z}(1+z)\le1\) for \(z\ge0\). This proves strict increase with \(\gamma\). The formula, or the comparison with \(r\downarrow0\), yields \(0<P_-<1/4\).

**4. Boundary laws.** Substitution into the closed form gives all four listed one-sided limits. More precisely, for fixed positive \(a,D,\gamma\),

\[
P_-=\frac14-\frac14\sqrt{\frac{r}{2\gamma}}+O(r)
\qquad(r\downarrow0),
\]

while for fixed positive \(a,D,r\),

\[
P_-=\frac14-\frac14\sqrt{\frac{r}{2\gamma}}+O(\gamma^{-3/2})
\qquad(\gamma\to\infty).
\]

The exponentially small contribution in the second expansion is absorbed by the remainder since \(a>0\). For fixed \(\gamma>0\), \(P_-\sim\gamma/(4r)\) as \(r\to\infty\). The two iterated limits then follow.

## Verification

The standalone file `verify.py` independently reconstructs the two mode solutions, checks the backward differential equations, both active boundary values, inactive value and derivative matching, reset self-consistency, strict parameter ordering on a large deterministic parameter grid, and near-boundary limits. It also simulates the process by drawing *exact exponential event intervals* and testing Brownian-bridge crossing probabilities, avoiding Euler sign-sampling bias. Four independent parameter examples agree within specified sampling-error tolerances. The program reports **5,406 checks passed**. Monte Carlo and finite checks are corroboration, not substitutes for the analytical uniqueness and derivative proofs.

## Relationship to prior work

Żbik et al. (2025/2026, arXiv:2512.09739) establish the transparent blinking-target model and give exact Laplace transforms for its (unmarked) first-passage time. Their Section III.3 treats the incoming side through simulations rather than a side-resolved analytical law. The present formula determines that missing observable and reveals a singular fast-switching limit. The stated increasing trend of initial-side absorption with gate-switching rate in their simulation discussion is opposite to the continuous-time side-resolved law above; reconciling numerical side-detection conventions is a worthwhile separate check.

Bressloff (2020, arXiv:2009.02739) treats an absorbing/reflecting gate, not a transparent inactive target. Biswas et al. (2023, arXiv:2304.10605) consider gated drift-diffusion on a half-line with reflection and mean completion times. Bressloff (2026, arXiv:2601.01588) develops a gated-boundary renewal formulation; its finite-interval splitting fluxes concern different absorbing ends. Bressloff (2026, arXiv:2601.13414) develops crossing through a switching impermeable/permeable interface and a stationary distribution, not termination at an active transparent-target contact. Those theories motivate the methods but do not state the two-sided marked hitting law above.

## Limitations

The exact law assumes equal active/inactive switching rates, a stationary initial gate, driftless Brownian motion, instantaneous Poisson resetting to a strictly positive point, and a transparent inactive target. The deterministic-initial-state formulas are included only for this same model. It does not classify unequal switching, drift, finite target width, or discrete sampling. The fast-switching singularity is specific to the incoming-side observable. Universal monotonicity and the quarter limit have analytical proofs; finite checking cannot establish global publication priority. Possible unlocated general marked-resolvent theorems, and agreement with simulations that use other side conventions, remain external-comparison risks.

## References

- Bartosz Żbik, Bartłomiej Dybiec, Karol Capała, Zbigniew Palmowski, Igor M. Sokolov. *Hitting the blinking target under stochastic resetting*. arXiv:2512.09739, first public version December 10, 2025. https://arxiv.org/html/2512.09739
- Paul C. Bressloff. *Diffusive search for a stochastically-gated target with resetting*. arXiv:2009.02739 (2020). https://arxiv.org/abs/2009.02739
- Arup Biswas, Arnab Pal, Debasish Mondal, Somrita Ray. *Rate enhancement of gated drift-diffusion process by optimal resetting*. arXiv:2304.10605 (2023). https://arxiv.org/abs/2304.10605
- Paul C. Bressloff. *Renewal theory for Brownian motion with stochastically gated targets*. arXiv:2601.01588 (2026). https://arxiv.org/abs/2601.01588
- Paul C. Bressloff. *Renewal theory for Brownian motion across a stochastically gated interface*. arXiv:2601.13414 (2026). https://arxiv.org/abs/2601.13414
