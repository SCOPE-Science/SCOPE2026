# Sharp finite-chain throughput and cotangent bulk profile for nonlinear steric transport

## Finding
For each integer \(r\ge2\), the homogeneous nonlinear ribosome-flow chain with availability \(1-x^r\) has a sharp stationary-current approach to its infinite-chain limit:
\[
\lim_{n\to\infty}n^2(J_n-J_*)=\frac{2\pi^2 r}{(r+1)^{2+1/r}},\quad J_*=\frac{r}{(r+1)^{1+1/r}}.
\]
The interior density profile is not flat at order \(n^{-1}\). At every fixed \(0<t<1\),
\[
\lim_{n\to\infty} n\left(e_{n+1-\lfloor t(n+1)\rfloor}-s_r\right)
=-\frac{2\pi s_r}{r+1}\cot(\pi t),\qquad s_r=(r+1)^{-1/r}.
\]
These two limits comprise a single finite-size bottleneck theorem.

## Assumptions and scope
Choose an integer \(r\ge2\), an integer \(n\ge1\), and unit transition rates. For \(1\le i\le n\), let \(x_i\in[0,1]\) evolve by
\[
\dot x_i=x_{i-1}(1-x_i^r)-x_i(1-x_{i+1}^r),\quad x_0=1,\quad x_{n+1}=0.
\]
The positive equilibrium is unique (Zhou, Theorem 2.2); denote it by \(e_1,\ldots,e_n\). Its equal edge flux is \(J_n=e_i(1-e_{i+1}^r)\) for every \(0\le i\le n\). All limits fix \(r\) first. The endpoint values \(t=0,1\) are excluded, and the profile uses the specified downstream-to-upstream indexing.

## Proof
**1. Scalar shooting and threshold.** Put \(F_J(x)=J/(1-x^r)\), and recursively set \(y_0=0\) and \(y_{k+1}=F_J(y_k)\) whenever \(0\le y_k<1\). The equilibrium equations imply \(y_k=e_{n+1-k}\) for \(0\le k\le n+1\), so \(y_{n+1}=1\) and \(y_1,\ldots,y_n\in(0,1)\). Conversely any such orbit yields the unique equilibrium. The function \(h(x)=x(1-x^r)\) on \([0,1]\) has its unique maximum at \(s_r=(r+1)^{-1/r}\), with value \(J_*=r s_r/(r+1)\). If \(J\le J_*\), the shooting orbit starting at zero cannot cross the smaller fixed point of \(F_J\) (at \(J=J_*\), its parabolic fixed point); thus it cannot reach one. This proves \(J_n>J_*\). For \(J>J_*\), every subunit step is strictly increasing, since
\[
F_J(x)-x=\frac{J-h(x)}{1-x^r}>0.
\]
As long as it stays below one, each step increases strictly with \(J\). A finite first-hitting threshold therefore determines \(J_n\). For any fixed \(J>J_*\), the increasing orbit must hit or exceed one in finitely many steps; otherwise its limit would be a forbidden fixed point in \([0,1)\). It follows from monotone shooting and the exact boundary hit that \(J_n\downarrow J_*\).

**2. Parabolic bottleneck and current.** Set \(\delta=J-J_*>0\), \(u=x-s_r\), and \(\Delta_\delta(x)=F_J(x)-x\). At the unique maximum of \(h\),
\[
h''(s_r)=-r/s_r,\quad
\Delta_\delta(s_r+u)=a\delta+b u^2+O(\delta|u|+|u|^3),
\quad a=\frac{r+1}{r},\quad b=\frac{r+1}{2s_r}.
\]
The error holds uniformly for \(|u|\le\varepsilon\) and sufficiently small \(\delta\), with \(\varepsilon>0\) fixed. Each step outside the smaller window \([s_r-\varepsilon,s_r+\varepsilon]\) has drift bounded below by a positive constant depending on \(\varepsilon\); hence the total exterior number of steps is \(O_\varepsilon(1)\). Inside the window \(\sup|\Delta_\delta'(x)|=O(\varepsilon+\delta)\), so along a monotone orbit the count of steps and the integral \(\int dx/\Delta_\delta(x)\) across the same window differ by a relative factor \(1+O(\varepsilon)\), plus an \(O_\varepsilon(1)\) boundary error (the integrand varies by this relative amount across each step). The integral is asymptotic, first as \(\delta\downarrow0\) and then \(\varepsilon\downarrow0\), to
\[
\int_{-\varepsilon}^{\varepsilon}\frac{du}{a\delta+b u^2}
\sim \frac{\pi}{\sqrt{ab\delta}}.
\]
Consequently the number of iterations from zero to one obeys \(n+1\sim\pi/\sqrt{ab(J_n-J_*)}\). Rewriting gives \(n^2(J_n-J_*)\to\pi^2/(ab)=2\pi^2 r s_r/(r+1)^2\).

**3. Interior cotangent profile.** Fix \(0<t<1\) and \(k_n=\lfloor t(n+1)\rfloor\). As the exterior counts are uniformly bounded for each window, \(y_{k_n}\) belongs to every fixed neighborhood of \(s_r\) for sufficiently large \(n\). The same integral comparison, now stopped at \(y_{k_n}\), yields the normalized passage-time identity
\[
\frac{k_n}{n+1}=\frac12+\frac1\pi\arctan\left[(y_{k_n}-s_r)\sqrt{\frac{b}{a(J_n-J_*)}}\right]+o(1).
\]
This follows by first bounding the relative integral error by \(O(\varepsilon)\) in a fixed window, taking \(n\to\infty\), then letting \(\varepsilon\to0\); the asymptotic exterior times vanish after division by \(n\). The arctangent therefore tends to \(\pi(t-1/2)\). Since \(\sqrt{a(J_n-J_*)/b}\sim\pi/(bn)\), inversion gives
\[
 n(y_{k_n}-s_r)\longrightarrow\frac{\pi}{b}\tan\bigl(\pi(t-1/2)\bigr)
=-\frac{2\pi s_r}{r+1}\cot(\pi t),
\]
as claimed.

## Verification
The included `check.py` computes the unique stationary current by monotone scalar shooting and tests convergence of both normalized observables for multiple powers and chain lengths. The analytic comparisons above, rather than finite experiments, prove the limits. In particular, the passage-time integral is applied only at a nondegenerate quadratic maximum of \(h\), and the endpoint bulk-profile regimes are expressly excluded.

## Relationship to prior work
Zhou (arXiv:2610.10602v1) introduces the nonlinear availability law, establishes global equilibrium uniqueness, and investigates gain of entrainment. The exact finite-chain current coefficient and spatial cotangent profile are separate stationary quantities not given by its inspected statements. Zarai–Margaliot–Tuller (2013) treats the classical linear vacancy law and the infinite-dimensional homogeneous current, not this power-law family or its scaled interior spatial profile. Saddle-node bottleneck scaling is a classical principle; the exact model-dependent coefficient and density-profile law, rather than that principle alone, are the contributions here.

## Limitations
The exponent \(r\) is a fixed integer at least two, all edge rates equal one, and the two boundary occupancies are fixed at one and zero. No uniformity as \(r\to\infty\), no boundary-layer profile at \(t=0\) or \(t=1\), and no assertion for heterogeneous rates is made. Older literature on nonlinear one-dimensional transport recursions may contain an equivalent result; no independent external audit was performed.

## References
1. H. Zhou, *Gain of Entrainment in Ribosome Flow Models with Nonlinear Steric Hindrance: Global Rigidity and Dimension-Induced Gain*, arXiv:2610.10602v1, 7 October 2026, especially Theorem 2.2 and equation (2.6).
2. Y. Zarai, M. Margaliot and T. Tuller, *Explicit expression for the steady-state translation rate in the infinite-dimensional homogeneous ribosome flow model*, IEEE/ACM Transactions on Computational Biology and Bioinformatics **10** (2013), 1322–1328, DOI: 10.1109/TCBB.2013.120.
3. C. Kuehn, *Scaling of saddle-node bifurcations: degeneracies and rapid quantitative changes*, Journal of Physics A **42** (2009), 045101.
