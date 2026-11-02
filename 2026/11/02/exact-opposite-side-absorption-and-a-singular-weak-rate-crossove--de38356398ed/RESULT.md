# Exact opposite-side absorption and a singular weak-rate crossover for a blinking Brownian target

## Finding

For a Brownian searcher on the whole real line, reset to a positive starting point but facing a *transparent* inactive target at zero, the direction of eventual capture has an exact closed form. Write

\[
a=\sqrt{r/D},\qquad b=\sqrt{(r+2\gamma)/D},\qquad z=\frac a b,\qquad v=e^{-b x_0}.
\]

For every \(D,r,\gamma,x_0>0\), define \(P_-\) as the probability of approach from the negative side at absorption, opposite the starting side, when the gate initially follows its symmetric stationary law. Then

\[
\boxed{P_-=\frac14\left(1-z+\frac{z^2e^{-b x_0}}{1+z}\right).}
\]

In particular \(0<P_-<1/4\). The probability is strictly decreasing with \(r\) and \(x_0\), and strictly increasing with the gate-switching rate \(\gamma\), all other parameters held fixed. For the two deterministic initial gate states the exact probabilities are

\[
\begin{aligned}
F_A&=\frac{(1-z)(1-v)}4,\\
F_I&=\frac{(1-z)(1-v)}4+\frac{v}{2(1+z)}.
\end{aligned}
\]

The two weak-rate limits do not commute. If \(r,\gamma\downarrow0\) and \(r/\gamma\to c\in[0,\infty]\) in the extended-real sense, then

\[
\boxed{P_-\longrightarrow\frac1{4\left(1+\sqrt{c/(c+2)}\right)},}
\]

where \(c=\infty\) means the continuous limiting value \(1/8\). Thus the limit is \(1/4\) when \(r/\gamma\to0\), but \(1/8\) when \(r/\gamma\to\infty\). More explicitly,

\[
\lim_{\gamma\downarrow0}\lim_{r\downarrow0}P_-=\frac14,
\qquad
\lim_{r\downarrow0}\lim_{\gamma\downarrow0}P_-=\frac18.
\]

At fixed \(r>0\), the rapid-switching limit of the directional probability is also \(1/4\), even though the hitting-time distribution converges to the permanently absorbing-target limit, whose opposite-side probability is zero. Therefore the direction observable is singular under rapid switching.

## Assumptions and scope

Let \(B_t\) be standard one-dimensional Brownian motion, and between resets take \(dX_t=\sqrt{2D}\,dB_t\). Independently, a target at the origin alternates between active state \(A\) and inactive state \(I\), with transition rate \(\gamma\) in each direction. The inactive target is *transparent*: it does not reflect, kill, or alter the Brownian motion. The active target kills the trajectory at the first zero of \(X\) while the gate is active. Independent Poisson resets of rate \(r\) move \(X\) instantaneously to the fixed point \(x_0>0\), and **do not change the gate state**. The gate begins either deterministically in \(A\) or \(I\), or at its equilibrium law \((1/2,1/2)\). Put \(\tau=\inf\{t\ge0:X_t=0,\ J_t=A\}\).

The opposite-side event is NOT the literal inequality \(X_{\tau-}<0\), since continuity gives \(X_{\tau-}=0\) upon capture. Instead, the capture direction is the sign of \(X_t\) throughout some nonempty left-neighborhood of \(\tau\) within the last active-gate interval. Almost surely such a neighborhood exists: the jump times of the independent gate and reset processes have no coincidence with the random capture time, and a continuous path cannot cross zero during that active interval before its first capture. The event in the definition of \(P_-\) is this incoming-side event.

All statements concern this symmetric two-state gate and point resetting. The limit involving \(c\) assumes fixed \(x_0,D>0\) and positive parameters at every finite stage. No assertion is made for a process defined *at* \(r=\gamma=0\), where the stopping-time behavior is different.

## Proof

**1. Absorption in a no-reset excursion.** Temporarily turn off position resetting, and fix a Laplace variable \(s>0\). Let

\[
a_s=\sqrt{s/D},\quad b_s=\sqrt{(s+2\gamma)/D},\quad u_s=e^{-a_s x_0},\quad v_s=e^{-b_s x_0},\quad t_s=\frac{b_s-a_s}{b_s+a_s}.
\]

The standard Brownian first-zero transform is \(\mathbb E_{x_0}e^{-sT_0}=u_s\). Conditional on the initial gate being \(A\), the discounted probabilities that it is \(A,I\) at \(T_0\) are \((u_s+v_s)/2\) and \((u_s-v_s)/2\). From initial gate \(I\), they are interchanged. These follow by decomposing the two-state gate semigroup into its stationary and decaying modes with decay rate \(2\gamma\).

If the first zero occurs while the gate is inactive, the search restarts *locally* at \((0,I)\) (without relocating the particle). Let \(t_s^{(0)}\) be the Laplace transform of the subsequent absorption time from \((0,I)\). For \(x\ge0\), bounded solutions \(f_A,f_I\) satisfy

\[
D f_A''-(s+\gamma)f_A+\gamma f_I=0,
\qquad D f_I''-(s+\gamma)f_I+\gamma f_A=0,
\]

with \(f_A(0)=1\) and \(f_I'(0)=0\). The latter is the reflection-symmetry condition at zero for the inactive gate, not a reflecting target. The general bounded solutions are linear combinations of \(e^{-a_sx}(1,1)\) and \(e^{-b_sx}(1,-1)\). Solving the two boundary conditions gives

\[
t_s^{(0)}=f_I(0)=\frac{b_s-a_s}{b_s+a_s}=t_s.
\]

By reflection symmetry, conditional on a first arrival at \((0,I)\), each eventual approach side is assigned precisely half the discounted success mass \(t_s\). The no-reset discounted opposite-side capture weights, conditional on initial gate \(A\) and \(I\), are thus

\[
\ell_A(s)=\frac{t_s(u_s-v_s)}4,
\qquad \ell_I(s)=\frac{t_s(u_s+v_s)}4.
\]

The corresponding no-reset *total* capture transforms are

\[
g_A(s)=\frac{b_su_s+a_sv_s}{a_s+b_s},
\qquad g_I(s)=\frac{b_su_s-a_sv_s}{a_s+b_s}.
\]

The formulas follow by adding absorption at the first zero while \(A\) to absorption after the first zero while \(I\).

**2. Resets preserve the gate.** Now put \(s=r\), omit the subscript on \(a,b,u,v,t\), and write the target gate generator as \(Q\). The gate transition matrix at an independent rate-\(r\) exponential time is

\[
R=r(rI-Q)^{-1}=\begin{pmatrix}C&H\\H&C\end{pmatrix},
\quad C=\frac{r+\gamma}{r+2\gamma}=\frac{1+z^2}2,
\quad H=\frac\gamma{r+2\gamma}=\frac{1-z^2}2.
\]

Let \(K_{jk}\) be the probability that a resetting event precedes absorption, and that the gate is \(k\) when it occurs, given initial gate \(j\). Since any absorption occurs with gate \(A\), the strong Markov property and convolution with the gate transition semigroup give

\[
K_{jk}=R_{jk}-g_j(r)R_{Ak}.
\]

Indeed the first term counts all first reset events; the subtracted term counts the same events after a hypothetical earlier (no-reset) absorption. If \(F=(F_A,F_I)^\mathsf T\) is the eventual opposite-side capture vector, first-event decomposition yields

\[
F=\ell(r)+KF.
\]

The system has a unique probabilistic solution: in every fresh excursion, irrespective of the gate state, there is a strictly positive probability of absorption before the next reset, so the number of excursions is finite almost surely. Define \(S=CF_A+HF_I\). Summing the two equations gives

\[
(g_A+g_I)S=\ell_A+\ell_I,
\quad
S=\frac{t u/2}{2bu/(a+b)}=\frac{1-z}4.
\]

The first component of the same system gives

\[
H(F_A-F_I)=\ell_A-g_AS=-\frac{(1-z)v}4.
\]

Consequently \(F_I-F_A=v/[2(1+z)]\), whence

\[
F_A=\frac{(1-z)(1-v)}4,
\qquad
F_I=\frac{(1-z)(1-v)}4+\frac{v}{2(1+z)}.
\]

Averaging the initial gate states yields the formula in the finding. Note that this uses a two-state renewal matrix; replacing the gate at each reset by an independent equilibrium draw would change that matrix and the answer.

**3. Strict inequalities and monotonicities.** Put \(q(z)=z^2/(1+z)\). Then \(4P_-=1-z+q(z)e^{-b x_0}\), \(0<z<1\), \(0<e^{-b x_0}<1\), and \(0<q(z)<z\), proving \(0<P_-<1/4\). Also

\[
q'(z)=1-\frac1{(1+z)^2}\in(0,3/4),
\qquad \frac{q(z)}z=\frac{z}{1+z}<\frac12.
\]

As \(r\) increases with \(D,\gamma,x_0\) fixed, \(z\) and \(b\) strictly increase. The derivative is strictly negative since \(q'(z)e^{-bx_0}<1\) and \(e^{-bx_0}\) decreases. At fixed \(r,D,x_0\), varying \(\gamma\) amounts to increasing \(b\) with \(z=a/b\). Writing \(y=bx_0\), direct differentiation gives

\[
\frac{4b}{z}\frac{\partial P_-}{\partial b}
=1-e^{-y}\left(q'(z)+y\frac{q(z)}z\right)
>1-e^{-y}\left(\frac34+\frac y2\right)>0,
\]

because \(e^{-y}(3/4+y/2)\le3/4\) for \(y\ge0\). This proves increase in \(\gamma\); the strict decrease in \(x_0\) follows from \(\partial_{x_0}P_-=-bq(z)e^{-bx_0}/4<0\).

**4. Singular limits.** If \(r,\gamma\downarrow0\), then \(b x_0\to0\), and \(z\to\sqrt{c/(c+2)}\). The exact expression reduces to

\[
\frac14\left(1-z+\frac{z^2}{1+z}\right)=\frac1{4(1+z)}.
\]

The two iterated limits follow by setting first \(r\downarrow0\) or first \(\gamma\downarrow0\). At fixed \(r>0\) and \(\gamma\to\infty\), \(z\to0\) and \(P_-\to1/4\). If the target is permanently active from the outset, capture occurs at the first zero from the starting positive side even with resets, hence its opposite-side probability is exactly zero. This proves the nonconvergence of this directional observable although the hitting-time law itself tends to the permanently active law.

## Verification

The accompanying reproducible `verify.py` implements two independent formulations: the killed-excursion renewal system and a six-condition backward boundary-value problem for the eventual capture-side probabilities. It also checks the exact expression on positive parameter grids, strict numerical trends, and the weak-rate scaling profile. A separate exact-event Brownian-bridge simulation checks capture-side probabilities with recorded sampling error bounds. These computations are consistency checks; the universal quantifiers and singular limits are established by the proof above.

Execute `python verify.py` with Python 3 and NumPy installed. No externally obtained data, pretrained models, or stochastic input files are required. The fixed simulation seed makes the run reproducible.

## Relationship to prior work

Żbik, Dybiec, Capała, Palmowski and Sokolov (arXiv:2512.09739) introduce this transparent-inactive, persistent-gate resetting model. They derive first-passage-time and mean-time transforms; Section III.3 and Figure 5 discuss the side of capture through simulations. The present claim is an analytical directional splitting law, strict parameter monotonicity, and a singular joint-rate phase profile; it is not a claim to originate the stochastic model, the total hitting-time transform, or renewal methods. In particular, a marginal stopping-time distribution alone does not determine an incoming-side distribution.

Mercado-Vásquez and Boyer (arXiv:2107.02148) study a gate that is reflecting when inactive and is reinitialized at resetting; in that half-line geometry there is no opposite-side capture. Bressloff (arXiv:2009.02739) studies diffusive gated-target mean first-passage quantities for reflecting/absorbing boundary geometries. General stochastic-resetting splitting-probability methods are older than the present calculation, and are credited as mathematical tools rather than claimed as new.

## Limitations

This proof applies only to the real-line Brownian model with a symmetric two-state gate, independent Poisson resets to a fixed positive point, transparent inactivity, and no gate reset. It does not establish comparable inequalities for asymmetric gate rates, finite reactive windows, drift, non-Brownian motions, random reset sites, or resetting the gate. The directional side is a pathwise mark at absorption and its rapid-switching behavior must not be inferred from convergence of the unmarked hitting-time distribution. Independence of a publication-priority audit has not been established. Some unlocated general flux-splitting theorem could cover the closed form or its comparative consequences.

## References

- B. Żbik, B. Dybiec, K. Capała, Z. Palmowski, and I. M. Sokolov, *Hitting the blinking target under stochastic resetting*, arXiv:2512.09739 (first publicly posted 2025-12-10), https://arxiv.org/abs/2512.09739 ; full text https://arxiv.org/html/2512.09739 . Especially Sections II, III.1, III.3, and Appendix B.
- G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148 (2021), https://arxiv.org/abs/2107.02148 .
- P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (2020), https://arxiv.org/abs/2009.02739 .
