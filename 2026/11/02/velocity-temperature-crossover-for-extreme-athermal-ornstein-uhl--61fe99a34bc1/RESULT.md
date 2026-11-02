# Velocity-temperature crossover for extreme athermal Ornstein–Uhlenbeck first passage

## Finding

Consider independent active particles whose positions are time integrals of Ornstein–Uhlenbeck velocities, with no direct positional diffusion. There is a sharp crossover in the fastest particle's target-arrival timescale determined by the initial kinetic variance. Uniformly for arbitrary nonnegative sequences of that variance, the first arrival is asymptotic in probability to the time at which one particle's positional variance reaches \(\ell^2/(2\log N)\).

More precisely, let \(L_N=\log N\) and \(b_N=u_N L_N^{1/3}\). If \(b_N\to b<\infty\), then
\[
L_N^{1/3}T_N\xrightarrow{\mathbb P}s_b,
\qquad b s_b^2+\frac{2D_v}{3}s_b^3=\frac{\ell^2}{2},\quad s_b>0.
\]
If \(b_N\to\infty\), then
\[
\frac{\sqrt{2u_NL_N}}{\ell}T_N\xrightarrow{\mathbb P}1.
\]
In particular, with zero initial velocity variance,
\[
T_N\sim_{\mathbb P}\left(\frac{3\ell^2}{4D_v\log N}\right)^{1/3},
\]
whereas for fixed \(u_N=u>0\),
\[
T_N\sim_{\mathbb P}\frac{\ell}{\sqrt{2u\log N}}.
\]
The friction coefficient does not affect these leading constants. The complete crossover is not simply an interpolation of two fixed-parameter cases: the velocity law is allowed to vary with population size.

A finite-population estimate, useful without taking a limit, is provided below.

## Assumptions and scope

Fix \(\gamma,D_v,\ell>0\). For every integer \(N\ge3\), take mutually independent real Brownian motions \(B_1,\dots,B_N\). Take independent Gaussian starting velocities \(V_i(0)\sim\mathcal N(0,u_N)\), for an arbitrary finite \(u_N\ge0\), independent of all Brownian motions. Define
\[
dV_i(t)=-\gamma V_i(t)\,dt+\sqrt{2D_v}\,dB_i(t),
\qquad dX_i(t)=V_i(t)\,dt,\quad X_i(0)=0.
\]
No independent Brownian term is added to \(dX_i\). The first passage of particle \(i\) to the right target is \(\tau_i=\inf\{t\ge0:X_i(t)\ge\ell\}\); set \(T_N=\min_i\tau_i\). Define
\[
A(t)=\frac{1-e^{-\gamma t}}{\gamma},\quad
q_N(t)=u_NA(t)^2+2D_v\int_0^tA(s)^2\,ds.
\]
For each \(N\), \(q_N\) is continuous, strictly increasing on positive times, vanishes at zero and diverges as time increases. Thus there is exactly one \(t_N>0\) satisfying
\[
q_N(t_N)=\frac{\ell^2}{2\log N}.
\]
The notation \(Z_N\sim_{\mathbb P}a_N\) here means \(Z_N/a_N\to1\) in probability.

## Proof

**1. Exact variance.** The integrated Ornstein–Uhlenbeck solution is the centered Gaussian process
\[
X_i(t)=A(t)V_i(0)+\sqrt{2D_v}\int_0^t A(t-s)\,dB_i(s).
\]
Itô isometry gives \(\operatorname{Var}(X_i(t))=q_N(t)\). Its exact closed form is
\[
q_N(t)=\frac{u_N}{\gamma^2}(1-e^{-\gamma t})^2
+\frac{2D_v}{\gamma^2}\left[t-\frac{2(1-e^{-\gamma t})}{\gamma}
+\frac{1-e^{-2\gamma t}}{2\gamma}\right].
\]
All positive-time terms in the integral representation are nonnegative. As \(t\downarrow0\), uniformly in the choice of \(u_N\ge0\),
\[
q_N(t)=\left[u_Nt^2+\frac{2D_v}{3}t^3\right](1+O(\gamma t)),
\]
where the relative error constant depends only on the fixed positive physical coefficients (the weighted positive-sum formula makes it uniform in \(u_N\)). In particular, \(t_N\to0\) because \(q_N(t)\ge 2D_v\int_0^tA(s)^2\,ds\) and the right-hand side is positive at each fixed \(t>0\).

**2. Uniform first-passage bounds.** Let \(\tau\) denote one-particle first passage and \(q=q_N(t)\). Since paths are continuous, \(X(t)\ge\ell\) implies \(\tau\le t\), so
\[
\mathbb P(\tau\le t)\ge\Phi(-\ell/\sqrt q).
\]
For \(0<t\le\gamma^{-1}\), \(A(s)\ge(1-e^{-1})s\) on \([0,t]\). Therefore
\[
q\ge(1-e^{-1})^2\left[u_Nt^2+\frac{2D_v}{3}t^3\right].
\]
Writing \(m=\mathbb E\sup_{0\le s\le t}X(s)\), the absolutely continuous paths and the Gaussian velocity moments imply
\[
m\le\int_0^t\mathbb E|V(s)|\,ds
\le\sqrt{\frac{2}{\pi}}\left[t\sqrt{u_N}
+\frac23\sqrt{2D_v}\,t^{3/2}\right]
\le\frac{\sqrt{14/(3\pi)}}{1-e^{-1}}\sqrt q<2\sqrt q.
\]
The last inequality is Cauchy–Schwarz in two coordinates; the numerical constant is strictly below two. As the positional variance increases with time, \(\sup_{s\le t}\operatorname{Var}(X(s))=q\). Borell's inequality for the centered continuous Gaussian process gives
\[
\mathbb P(\tau\le t)
=\mathbb P\!\left(\sup_{s\le t}X(s)\ge\ell\right)
\le\exp\left[-\frac{(\ell-2\sqrt q)_+^2}{2q}\right].
\]
Independence of the \(N\) paths and \(1-p\le e^{-p}\) yield, for \(z_N(t)=\ell/\sqrt{q_N(t)}\),
\[
\mathbb P(T_N>t)\le\exp[-N\Phi(-z_N(t))],\qquad
\mathbb P(T_N\le t)\le N\exp[-(z_N(t)-2)_+^2/2].
\]
The two inequalities are valid for every \(0<t\le\gamma^{-1}\) and every integer \(N\ge3\).

**3. Concentration at the variance threshold.** Fix \(0<\varepsilon<1\), and let \(t_-=(1-\varepsilon)t_N\), \(t_+=(1+\varepsilon)t_N\). The small-time positive-sum expansion gives
\[
\frac{q_N(t_-)}{q_N(t_N)}\le(1-\varepsilon)^2(1+o(1)),
\quad
\frac{q_N(t_+)}{q_N(t_N)}\ge(1+\varepsilon)^2(1+o(1))
\]
uniformly over all choices of \(u_N\), since the leading powers are two and three. Since \(q_N(t_N)=\ell^2/(2L_N)\), the early-time bound in step 2 implies \(\mathbb P(T_N\le t_-)\to0\): its upper bound is \(N\exp[-L_N/(1-\varepsilon)^2+O(\sqrt{L_N})+o(L_N)]\). The Gaussian Mills lower bound and the late-time bound in step 2 imply \(\mathbb P(T_N>t_+)\to0\), since \(N\Phi[-\sqrt{2L_N}/(1+\varepsilon+o(1))]\to\infty\). Thus \(T_N/t_N\xrightarrow{\mathbb P}1\).

**4. Critical kinetic-temperature crossover.** Write \(L=L_N\). If \(u_NL^{1/3}\to b<\infty\), substitute \(t=sL^{-1/3}\) into the uniform variance expansion:
\[
Lq_N(sL^{-1/3})\to b s^2+\frac{2D_v}{3}s^3.
\]
This function is continuous and strictly increasing from zero to infinity on positive \(s\). Inverting at \(\ell^2/2\) gives \(L^{1/3}t_N\to s_b\) and the stated limit for \(T_N\). If \(u_NL^{1/3}\to\infty\), set \(a_N=\ell/\sqrt{2u_NL}\), so \(a_N\to0\) and \((D_v/u_N)a_N\to0\). The variance expansion gives \(q_N(a_N)/[\ell^2/(2L)]\to1\). Monotonicity then implies \(t_N/a_N\to1\). Combining with step 3 proves the remaining limit. QED.

## Verification

The independent `verify.py` supplied with this finding checks the exact Ornstein–Uhlenbeck variance against numerical quadrature, the short-time variance bounds and supremum constants, and finite-parameter instances of the temperature-crossover root. Successful finite checks support implementation reproducibility but do not establish the infinite-population theorem, which is proved above.

## Relationship to prior work

Bao's 2026 analysis of interacting extreme first-passage times includes an active Ornstein–Uhlenbeck discussion with a **strictly positive direct thermal positional diffusivity**. The present model removes that positional Brownian mechanism and determines both the exact leading athermal fastest-arrival scale and its critical transition as the initial velocity variance depends on population size. The source's explicit Brownian \(1/\log N\) bound therefore does not directly imply this result. General extreme-value conversion from single-particle short-time tails is standard (Lawley 2020); the novelty assessed here is the singular athermal Gaussian process with a triangular-array variance, explicit uniform first-passage control, and the kinetic-temperature crossover. Earlier integrated Ornstein–Uhlenbeck barrier work (Hesse 1991) concerns one-particle first passage. Long-time OU-area large deviations (Bassanoni et al. 2025) address a different time regime. These prior results are not claimed as new.

## Limitations

The theorem assumes independent particles, Gaussian initial velocities with a **common deterministic population-dependent variance**, no direct positional thermal noise, one spatial dimension, a fixed positive target, and fixed \(\gamma,D_v>0\). It gives convergence in probability and explicit finite-population probability bounds, but neither the centered extreme-time fluctuations nor finite-\(N\) optimal control. It is not a theorem for interacting particles or joint particle-number/force scalings. Generic short-time Gaussian extreme-value theory may encompass aspects of the argument; exhaustive publication priority is not established. The accessible public technical passages from the 2026 motivating source did not provide the entire manuscript for a line-by-line comparison.

## References

1. R. Bao, *Extreme First-Passage Time of Many Interacting Particles*, arXiv:2607.22528 (first public version, 24 July 2026), https://arxiv.org/abs/2607.22528.
2. S. D. Lawley, *Distribution of extreme first passage times of diffusion*, Journal of Mathematical Biology **80** (2020), DOI:10.1007/s00285-020-01496-9; preprint arXiv:1910.12170, https://arxiv.org/abs/1910.12170.
3. S. D. Lawley, *Extreme first-passage times of piecewise deterministic Markov processes*, arXiv:1912.03438, https://arxiv.org/abs/1912.03438.
4. C. H. Hesse, *The one-sided barrier problem for an integrated Ornstein-Uhlenbeck process*, 1991, DOI:10.1080/15326349108807200.
5. A. Bassanoni et al., *Rare Events and Single Big Jump Effects in Ornstein-Uhlenbeck Processes*, arXiv:2501.07704, https://arxiv.org/abs/2501.07704.
