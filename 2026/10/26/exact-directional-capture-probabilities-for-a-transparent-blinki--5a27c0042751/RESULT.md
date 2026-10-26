# Exact directional capture probabilities for a transparent blinking Brownian target under resetting

## Finding
Consider a Brownian searcher on the real line with generator \(D\partial_{xx}\), starting at and resetting to \(x_0>0\) at Poisson rate \(r\geq0\). An independent gate at the origin switches from active to inactive at rate \(\alpha>0\) and from inactive to active at rate \(\beta>0\); resets never change the gate. The particle is killed at its first visit to the origin while the gate is active. An encounter during an inactive period is transparent. Let \(P_A(r)\) and \(P_I(r)\) be the probabilities that the killing approach comes from the **positive** half-line for initially active and inactive gates, respectively. Put

\[
\lambda=\alpha+\beta,\qquad \rho_r=\sqrt{\frac{r}{r+\lambda}},\qquad F_r=\exp\!\left(-x_0\sqrt{\frac{r+\lambda}{D}}\right).
\]

**Exact directional splitting law.** For every \(D,x_0,\alpha,\beta>0\) and \(r\ge0\),

\[
\boxed{P_A(r)=1-\frac{\alpha(1-F_r)}{2(r+\lambda)(1+\rho_r)}} ,
\qquad
\boxed{P_I(r)=1-\frac{F_r+\frac{\alpha}{r+\lambda}(1-F_r)}{2(1+\rho_r)}}.
\]

If the gate initially has its stationary law (active with probability \(\beta/\lambda\)), the exact positive-side probability is

\[
\boxed{P_E(r)=1-\frac{\alpha}{2\lambda}\frac{F_r+\frac{\lambda}{r+\lambda}(1-F_r)}{1+\rho_r}}.
\]

All three probabilities are **strictly increasing** in the reset rate on \([0,\infty)\), with continuous extension at \(r=0\). In particular the probability of capture from the wrong (negative) side has the universal strong-reset asymptotic

\[
\boxed{1-P_A(r)\sim1-P_I(r)\sim1-P_E(r)\sim\frac{\alpha}{4r}}\qquad(r\to\infty).
\]

At weak resetting the equilibrium-gate curve has the nonanalytic expansion

\[
\boxed{P_E(r)=1-\frac{\alpha}{2\lambda}+\frac{\alpha}{2\lambda^{3/2}}\sqrt r+O(r)}\qquad(r\downarrow0),
\]

whose leading two coefficients do not depend on the reset distance or diffusion coefficient. At \(r=0\), the equilibrium-gate value is exactly \(1-\alpha/(2\lambda)\) at **every** \(x_0>0\).

## Assumptions and scope
The particle is a one-dimensional standard Brownian motion of variance \(2Dt\) between independent Poisson resets. The two-state Markov gate is independent of Brownian noise and reset times. The original position is strictly on the positive side, and gate state is carried unchanged through resets. At capture, the preceding excursion in the most recent active gate interval approaches the origin from exactly one side almost surely, thereby defining the capture-side mark. The formulas require strictly positive \(\alpha,\beta,D,x_0\) and apply to both finite \(r>0\) and the no-reset limit \(r=0\). They are not formulas for an active/reflecting gate, or for a reset that also renews the target state.

## Proof
**1. Bare directional Laplace transforms.** First suppress resetting and let \(\tau\) be the first gate-active hitting time. For \(s>0\), let \(H_j(s,x)=\mathbb E_{x,j}e^{-s\tau}\) and \(G_j(s,x)=\mathbb E_{x,j}[e^{-s\tau}S]\), where \(S=+1\) if the final approach is from the positive side and \(-1\) otherwise. They solve the backward equations

\[
D f_A''-(s+\alpha)f_A+\alpha f_I=0,\qquad D f_I''-(s+\beta)f_I+\beta f_A=0
\]

on each open half-line. Write \(k=\sqrt{s/D}\), \(h=\sqrt{(s+\lambda)/D}\). Bounded solutions decompose into spatial modes \(e^{-k|x|}(1,1)\) and \(e^{-h|x|}(\alpha,-\beta)\). For \(H\), the active-gate absorbing boundary is \(H_A(s,0^\pm)=1\) and the inactive-gate solution and its first derivative are continuous at zero; reflection symmetry gives \(H_I'(s,0)=0\). For \(G\), the active boundary is \(G_A(s,0^+)=+1\), \(G_A(s,0^-)=-1\), while \(G_I\) is odd and continuous with \(G_I(s,0)=0\). Imposing these conditions gives, for \(x>0\),

\[
H_A=\frac{\beta h e^{-kx}+\alpha k e^{-hx}}{\alpha k+\beta h},\quad
H_I=\frac{\beta(h e^{-kx}-k e^{-hx})}{\alpha k+\beta h};
\]

\[
G_A=\frac{\beta e^{-kx}+\alpha e^{-hx}}{\lambda},\quad
G_I=\frac{\beta(e^{-kx}-e^{-hx})}{\lambda}.
\]

Hence the single-reset-free episode has positive-side discounted capture vector \(f^+(s)=(H(s,x_0)+G(s,x_0))/2\). Both the boundary conditions and the definition of the mark are essential: replacing transparency with reflection gives different formulas.

**2. Retained-gate renewal.** Let \(Q=\left(\begin{smallmatrix}-\alpha&\alpha\\\beta&-\beta\end{smallmatrix}\right)\), \(K=(rI-Q)^{-1}\) and take \(r>0\). Before a reset, the discounted gate state at the reset time is described by the substochastic matrix \(rL\), where

\[
L_{ij}=K_{ij}-H_i(r,x_0)K_{Aj},\qquad i,j\in\{A,I\}.
\]

To see this, integrate the unabsorbed gate-state probability over time, subtracting paths already absorbed at a time \(t\): after absorption the gate is in state \(A\), with subsequent gate transition resolvent \(K_{Aj}\). The first-event decomposition then reads

\[
p=f^+(r)+rLp,\quad\text{or}\quad
\bigl[I-rK+rH(r,x_0)K_{A\cdot}\bigr]p=f^+(r),
\]

where \(p=(P_A,P_I)^T\). Eventual absorption is certain: each new reset returns the particle to \(x_0\), and the independent ergodic gate visits the active state; a uniformly positive capture probability can be arranged over blocks of finitely many reset and gate events. Thus this finite-dimensional renewal system has its probabilistically unique solution. Insert the four elementary \(H,G\) expressions, and solve the two equations. Factoring the result yields exactly the three displayed closed forms; \(P_E=(\beta P_A+\alpha P_I)/\lambda\).

**3. Strict reset monotonicity.** The factor \((1+\rho_r)^{-1}\) is strictly decreasing. The numerator of \(1-P_I\) can be written \(F_r+u_r(1-F_r)\) with \(u_r=\alpha/(r+\lambda)\in(0,1)\); both \(u_r\) and \(F_r\) decrease, while this expression is increasing in either input, so the numerator strictly decreases. The same argument applies to \(P_E\), with \(u_r=\lambda/(r+\lambda)\). For \(P_A\), its remaining factor \((1-F_r)/(r+\lambda)\) decreases: the function \(t\mapsto(1-e^{-c\sqrt t})/t\) strictly decreases for every \(c,t>0\), as seen by differentiating or by the integral \((1-e^{-c\sqrt t})/t=\int_0^c e^{-u\sqrt t}du/\sqrt t\). Thus all three wrong-side probabilities strictly decrease with increasing \(r\). Continuity covers \(r=0\).

**4. Endpoint asymptotics.** For fixed \(x_0>0\), \(F_r\) is exponentially small in \(\sqrt r\), and \(\rho_r=1-\lambda/(2r)+O(r^{-2})\). Substitution gives \(1-P_j=\alpha/(4r)+O(r^{-2})\) for each initial-gate case. Conversely \(\rho_r=\sqrt{r/\lambda}+O(r^{3/2})\) and \(F_r=\exp(-x_0\sqrt{\lambda/D})+O(r)\), giving the equilibrium-gate small-\(r\) expansion. Setting \(r=0\) directly also follows from the strong Markov property at the first un-gated encounter: in gate stationarity, the gate is active with probability \(\beta/\lambda\); otherwise a Brownian particle at the transparent origin faces reflection-symmetric capture from either side.

## Verification
The included standalone `verify.py` evaluates the analytic formulas and, independently, reconstructs the two-state renewal matrix using the backward mode solutions. It tests their agreement over unequal switching rates and reset intensities, the equilibrium mixture identity, monotonicity, limiting expansions and probabilistic bounds. It also carries out seed-fixed event-driven Brownian-bridge crossing simulations: Brownian positions are sampled exactly at gate/reset event times, and a same-sign bridge is tested for hidden zero crossings with probability \(\exp[-|xy|/(D\Delta t)]\), avoiding a time-discretization bias. Monte Carlo checks are finite statistical checks, not a replacement for the proof.

Run `python3 verify.py` with a standard Python installation (no third-party packages required).

## Relationship to prior work
Zbik et al., arXiv:2512.09739, derive target-capture time transforms in this transparent, retained-gate model and investigate the side of arrival by simulations (their Figure 5 and Section III.3); their discussion does not provide the exact side-resolved probabilities derived here. The general retained-gate reset-renewal method and scalar time transforms are **not** claimed as new. Bressloff (arXiv:2009.02739) studies gated diffusive search with resetting but uses a reflecting closed target, without the two-sided capture mark. Bressloff (Phys. Rev. E 102, 022115, 2020) develops splitting probabilities for several targets rather than directional absorption at one transparent, time-gated target. Those broader methods may imply pieces of the result after a new side-marking construction; no claim is made of an entirely new renewal technique. The explicit simultaneous formulas, strict reset monotonicity and asymptotic calibration are the assessed contribution.

## Limitations
This result treats only one-dimensional unbiased Brownian motion, a transparent inactive target, an independent two-state exponential gate, complete instantaneous position resets to the original point, and no gate renewal at reset. It does not assert that these probabilities describe finite-step crossing simulations without Brownian-bridge correction. The asymptotic \(r\to\infty\) is for **fixed strictly positive** \(x_0\), and cannot be interchanged freely with \(x_0\downarrow0\). The novelty conclusion is limited by what could be inspected in relevant existing work, particularly general splitting-probability renewal theory.

## References
1. B. Zbik, B. Dybiec, K. Capała, Z. Palmowski and I. M. Sokolov, *Hitting the blinking target under stochastic resetting*, arXiv:2512.09739v1 (10 December 2025), https://arxiv.org/abs/2512.09739 .
2. P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (2020), https://arxiv.org/abs/2009.02739 .
3. P. C. Bressloff, *Search processes with stochastic resetting and multiple targets*, Physical Review E 102, 022115 (2020), https://doi.org/10.1103/PhysRevE.102.022115 .
4. G. Mercado-Vásquez and D. Boyer, *First Hitting Times to Intermittent Targets*, Physical Review Letters 123, 250603 (2019), https://doi.org/10.1103/PhysRevLett.123.250603 .
