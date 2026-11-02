# A sharp crowd–resetting threshold for the fastest Brownian searcher

## Finding
Let \(N\ge2\) independent Brownian particles, each with generator \(D\partial_{xx}\), start at distance \(d>0\) from an absorbing target at the origin on the real line. Each particle independently returns to \(d\) at the events of its own rate-\(r_N\) Poisson clock. Absorption of the first particle ends the experiment. Define
\[
t_0=\frac{d^2}{4D},\quad L_N=\log N,\quad r_N=\frac{aL_N^2}{t_0},\quad T_N=\min_{1\le j\le N}\tau_j,
\]
where \(a\ge0\) is a fixed dimensionless parameter and \(\tau_j\) is the first absorption time of particle \(j\).

There is a sharp three-regime law:

1. If \(0\le a<1/4\), then
\[
\frac{L_N T_N}{t_0}\xrightarrow{\mathbb P}\frac{2}{1+\sqrt{1-4a}}.
\]
2. If \(a=1/4\), then
\[
\frac{L_N T_N}{t_0}\xrightarrow{\mathbb P}2.
\]
3. If \(a>1/4\), then
\[
\frac{aL_N^2}{t_0}\,N^{1-2\sqrt a}T_N\xrightarrow{\mathrm d}\operatorname{Exp}(1).
\]

The distinction is between an inverse-logarithmic first-arrival time and, above the threshold, an exponentially distributed time on the polynomially increasing scale \(t_0N^{2\sqrt a-1}/(aL_N^2)\). This is a triangular-array result with an increasing reset rate; no claim is made about unrestricted resetting optimization.

## Assumptions and scope
The particles have independent Brownian drivers and independent, memoryless resetting clocks. Every reset returns the particle to exactly its original distance \(d\); resetting is instantaneous; the target remains absorbing throughout. The rate coefficient \(a\) is fixed as \(N\to\infty\), including \(a=0\), while \(d,D>0\) remain fixed. All limits above concern the fastest first-hitting time, not a cover time or an averaged survival probability over random starting positions.

For a free particle let \(H\) be its hitting time of zero. Then its exact density and the probability that it hits before an independent rate-\(r_N\) reset are
\[
f_H(h)=\frac{\sqrt{t_0}}{\sqrt\pi\,h^{3/2}}e^{-t_0/h},\qquad
q_N=\mathbb P(H<R)=\mathbb E e^{-r_NH}=e^{-2\sqrt a\,L_N}.
\]
Here \(R\) is exponential of rate \(r_N\); at \(a=0\) interpret \(R=+\infty\).

## Proof
**1. One-attempt large deviations.** For \(t>0\) put \(q_N(t)=\mathbb P(H\le t,H<R)\). With \(t=t_0y/L_N\) and \(y>0\), the substitution \(h=t_0z/L_N\) gives the exact integral
\[
q_N(t_0y/L_N)=\frac{\sqrt{L_N}}{\sqrt\pi}
\int_0^y z^{-3/2}\exp\{-L_N(1/z+az)\}\,dz.
\]
The Laplace principle (the integrand is exponentially negligible near \(z=0\)) yields
\[
-\frac{1}{L_N}\log q_N(t_0y/L_N)\longrightarrow
I_a(y):=\inf_{0<z\le y}(z^{-1}+az).
\]
For \(a>0\), the unique unconstrained minimizer is \(z_*=a^{-1/2}\), with \(I_a(y)=y^{-1}+ay\) for \(y\le z_*\) and \(I_a(y)=2\sqrt a\) for \(y\ge z_*\). When \(a=0\), \(I_0(y)=y^{-1}\). In particular, for every \(a>0\) and \(c>z_*\),
\[
\frac{q_N(t_0c/L_N)}{q_N}\longrightarrow1,
\]
because the omitted tail beyond \(c\) has strictly larger exponential cost than the interior minimizer. The exact equality \(q_N=e^{-2\sqrt a L_N}\) fixes the prefactor in this last statement.

**2. Finite-time counting inequalities.** Let \(p_N(t)\) be the probability that one *resetting* particle hits by time \(t\). Continue the particle's reset clocks and independent Brownian excursions virtually after a possible hit. A hit by time \(t\) must be witnessed by a successful attempt starting either at time zero or at some reset time no later than \(t\). The expected number of such starts is \(1+r_Nt\); each has probability at most \(q_N(t)\) of completing a successful attempt by \(t\). Therefore
\[
p_N(t)\le(1+r_Nt)q_N(t).
\tag{1}
\]
For \(0<\delta\le t\), count instead the attempts starting by \(w=t-\delta\) and hitting before the next reset and within elapsed time \(\delta\). Call their number \(K\). Poisson stationarity, independence of the Brownian excursions and the fresh exponential time to the next reset give
\[
\mathbb EK=(1+r_Nw)q_N(\delta).
\]
For two distinct starts, the earlier attempted hit must precede the next reset, and insertion of a later Poisson point can only shorten that earlier opportunity. By the two-point Poisson factorial-moment identity and independence of the two Brownian excursions,
\[
\mathbb E[K(K-1)]\le(2r_Nw+r_N^2w^2)q_N(\delta)^2.
\]
Applying \(\mathbf1_{\{K\ge1\}}\ge K-K(K-1)/2\) and observing that every counted hit precedes \(t\) yields
\[
p_N(t)\ge(1+r_Nw)q_N(\delta)
-\left(r_Nw+\frac12r_N^2w^2\right)q_N(\delta)^2.
\tag{2}
\]
These are genuine probability inequalities for every finite \(N\), not approximations assuming independent successful attempts. The same argument with \(r_N=0\) reduces to \(p_N(t)=q_N(t)\).

**3. Subcritical regime.** Let \(0\le a<1/4\). The unique smallest positive solution of \(I_a(y)=1\) is
\[
y_-(a)=\frac{2}{1+\sqrt{1-4a}}.
\]
For any \(0<y<y_-(a)\), \(I_a(y)>1\), so inequality (1) and \(r_Nt_0y/L_N=ayL_N\) imply \(Np_N(t_0y/L_N)\to0\). For every \(y>y_-(a)\), \(I_a(y)<1\) and the first attempt alone gives \(p_N(t_0y/L_N)\ge q_N(t_0y/L_N)\), whence \(Np_N(t_0y/L_N)\to\infty\). Since the \(N\) particle processes are independent,
\[
\mathbb P(T_N>t)=(1-p_N(t))^N,
\]
and these two bounds establish convergence in probability to \(y_-(a)\). Both inequalities hold at \(a=0\) by the ordinary Brownian hitting-time formula.

**4. Critical regime.** At \(a=1/4\), \(I_a(y)>1\) for \(y<2\), giving the lower side as above. If \(y>2\), fix any \(c\in(2,y)\), choose \(t=t_0y/L_N\) and \(\delta=t_0c/L_N\). The interior-saddle property gives \(q_N(\delta)\sim N^{-1}\). Here \(r_N(t-\delta)=(y-c)L_N/4\). Inequality (2) thus gives
\[
Np_N(t)\ge\frac{y-c}{4}L_N(1+o(1))\longrightarrow\infty.
\]
Consequently \(L_NT_N/t_0\to2\) in probability.

**5. Supercritical regime.** Let \(a>1/4\), so \(q_N=N^{-2\sqrt a}\). Fix \(z>0\) and put
\[
s_N=\frac{1}{Nr_Nq_N}=\frac{t_0N^{2\sqrt a-1}}{aL_N^2},\qquad t=zs_N.
\]
Choose any \(c>a^{-1/2}\) and \(\delta=t_0c/L_N\). Then \(t/\delta\to\infty\), \(r_Nt\to\infty\), and \(q_N(\delta)/q_N\to1\). Using (1) with \(q_N(t)\le q_N\) and the lower bound (2) gives
\[
Np_N(zs_N)\longrightarrow z.
\]
Indeed, the quadratic correction is \(O((r_Ntq_N)^2)=O(N^{-2})\), whereas the linear term is asymptotic to \(z/N\). Therefore
\[
\mathbb P(T_N>zs_N)=(1-p_N(zs_N))^N\longrightarrow e^{-z},
\]
proving the asserted unit-exponential limit. This completes all three regimes.

## Verification
An included standard-library Python script `verify.py` checks the Brownian discounted-success integral against its exact Laplace-transform expression, the finite-horizon success probability against its error-function formula, the saddle-point inequalities, and the closed-form subcritical threshold. It reports 209 deterministic checks.

Reproduce the standalone checks with `python verify.py`. The analytical arguments above cover all integers \(N\to\infty\); finite numerical tests are not evidence of uniform asymptotics by themselves.

## Relationship to prior work
Bao (2026) investigates how interactions alter the familiar \(1/\log N\) extreme-Brownian-arrival benchmark. That work studies interacting diffusions without the present Poisson reset rule or resetting rates growing with \(N\). Biroli, Majumdar and Schehr (2023) previously derived an exact renewal transform for *the same independently resetting searcher model* at arbitrary finite \(N\), and studied mean-first-passage optimization and the critical finite count \(N=7\). Their finite-time transform, first-passage setup, and independent-resetting protocol are entirely prior results. Linn and Lawley (2023) established the single-searcher exponential law under frequent resetting at its natural mean-time scale. Hartmann, Majumdar and Schehr investigate many resetting particles with random initial locations and different large-time/large-distance asymptotics.

The claim here is only the simultaneous \(N\to\infty\), \(r_Nt_0=a(\log N)^2\) **three-regime limit**, including its nonuniform critical point and supercritical fastest-arrival exponential law. Neither a new exact single-walker transform nor a new optimal rate at fixed \(N\) is asserted. The existing exact transform is consistent with, but does not by itself state or prove, the triangular-array transition.

## Limitations
The classification is for a fixed coefficient \(a\), with no uniform result in shrinking windows around \(a=1/4\), no finite-\(N\) optimality statement, and no moment-convergence claim in the supercritical regime. Different reset protocols, random starting locations, bounded domains and interacting particles are not covered. Earlier exact renewal formulas remain authoritative for the finite-\(N\) model; independent assessment of publication priority and potential equivalent asymptotic formulations remains outstanding.

## References
1. R. Bao, *Extreme First-Passage Time of Many Interacting Particles*, arXiv:2607.22528 (first submitted 2026-07-24), https://arxiv.org/abs/2607.22528.
2. M. Biroli, S. N. Majumdar, G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (first submitted 2023-03-31), https://arxiv.org/abs/2303.18012.
3. S. Linn, S. D. Lawley, *First passage times under frequent stochastic resetting*, arXiv:2302.05409 (first submitted 2023-02-10), https://arxiv.org/abs/2302.05409.
4. A. K. Hartmann, S. N. Majumdar, G. Schehr, *The distribution of the maximum of independent resetting Brownian motions*, open manuscript, https://uol.de/f/5/inst/physik/ag/compphys/download/Alexander/publications/max_resetting10.pdf.
