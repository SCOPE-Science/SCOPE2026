# Universal critical load and phase-resolved extinction at neutral invasion in periodically pulsed competition

## Finding

At a **neutral invasion threshold**, a two-population competitive impulsive differential equation can display globally attracting species exclusion with an exact and phase-resolved algebraic law rather than exponential exclusion. Under the hypotheses below, define a positive periodic resident profile \(x_*(t)\), the pulse-and-growth factor \(S(t)\), and \(I>0\). **For every pair of strictly positive initial densities**, \(x\) approaches the resident cycle, \(y\) vanishes, and for each \(0\le t<T\) (using the specified one-sided pulse convention),

\[
\lim_{n\to\infty}n y(nT+t)=\frac{S(t)x_*(t)^\lambda}{I}.
\]

More strikingly, the *weighted competitive load per intervention cycle* obeys the universal law

\[
\boxed{\lim_{n\to\infty} n\int_{nT}^{(n+1)T}g(t)y(t)\,dt=1.}
\]

Its cumulative counterpart has both an exact finite-time identity and a logarithmic asymptotic with an explicit initial-state constant:

\[
\boxed{\int_0^{NT}g(t)y(t)\,dt=\log N+\log\!\left(\frac{y(0)I}{x(0)^\lambda}\right)+o(1).}
\]

The coefficient one in the cyclic load is independent of seasonal forcing, pulse number, pulse timing, pulse strength and interaction magnitudes, provided the stated exact neutrality and positive gap hold. It is a *dimensionless, weighted* load, not an assertion that unweighted density has universal coefficient.

## Assumptions and scope

Fix a cycle duration \(T>0\), a real number \(\lambda>0\), and a finite set of pulse phases \(0<\tau_1<\cdots<\tau_m<T\) with \(m\ge1\). Let \(r,s:\mathbb R\to\mathbb R\) be continuous \(T\)-periodic functions. Let \(a,b,g:\mathbb R\to(0,\infty)\) be continuous \(T\)-periodic functions, hence each is bounded below by a strictly positive constant. Put pulse factors \(p_j,q_j\in(0,1]\) and \(P=\prod_{j=1}^m p_j\), \(Q=\prod_{j=1}^m q_j\).

Between the regularly repeated pulses, the positive populations evolve according to

\[
\dot x=x\bigl(r(t)-a(t)x-b(t)y\bigr),\qquad
\dot y=y\bigl(s(t)-\lambda a(t)x-[\lambda b(t)+g(t)]y\bigr).
\]

At \(nT+\tau_j\), with integer \(n\ge0\), set \(x^+=p_jx^-\), \(y^+=q_jy^-\). Initial values \(x(0),y(0)\) are arbitrary and strictly positive; no pulse occurs at \(t=0\). All values at the pulse phases in this paper are **right-continuous**, while integrals ignore pulse points.

Assume the resident is supercritical and the rare second species is precisely neutral in its linear invasion exponent:

\[
P\exp\!\left(\int_0^T r(t)\,dt\right)>1,
\quad
\frac{Q}{P^\lambda}\exp\!\left(\int_0^T[s(t)-\lambda r(t)]\,dt\right)=1.
\]

There is a unique globally attracting strictly positive \(T\)-periodic, piecewise-smooth resident solution \(x_*(t)\) of \(\dot x=x(r-ax)\), with the same \(x\)-pulses. For \(0\le t<T\) define

\[
S(t)=\exp\!\left(\int_0^t[s(u)-\lambda r(u)]\,du\right)
\prod_{\tau_j\le t}\frac{q_j}{p_j^\lambda},\qquad
I=\int_0^Tg(t)S(t)x_*(t)^\lambda\,dt>0.
\]

In particular \(S(0)=S(T)=1\) with the periodic extension of the pulse factor. The results hold with any finite number of pulses, including zero-size disturbances \(p_j=q_j=1\). The theorem is a dynamical-systems statement for this explicitly **aligned interaction-coefficient family**; it does not assert a general result for every competitive impulsive Lotka–Volterra system.

## Proof

**1. Positive bounded forward solutions.** Local Lipschitz continuity of the right-hand side and positive multiplicative pulses preserve the strictly positive cone. The logistic upper estimates \(\dot x\le x(\max r-\min a\,x)\) and \(\dot y\le y(\max s-\lambda\min b\,y)\), together with pulses at most one, bound both populations globally. Hence solutions exist for every forward time, and their continuous-time per-capita derivatives are bounded uniformly once the fixed initial state is chosen.

**2. Resident cycle.** For the scalar resident equation put \(u=1/x\). Between pulses \(\dot u=-r(t)u+a(t)\), and across each pulse \(u^+=u^-/p_j\). Therefore its one-period map is \(u_{n+1}=\alpha u_n+\beta\), where \(\alpha=[P\exp(\int_0^T r)]^{-1}<1\) and \(\beta>0\). It has a unique positive fixed point \(u_*=\beta/(1-\alpha)\), generating the positive periodic solution \(x_*(t)\). Every positive scalar initial datum converges exponentially to this periodic solution in reciprocal coordinates.

**3. Exact cancellation and monotone ratio.** Define \(z(t)=y(t)/x(t)^\lambda\), and \(z_n=z(nT)\). Between pulses, the specially aligned interaction terms cancel:

\[
\frac{d}{dt}\log z(t)=s(t)-\lambda r(t)-g(t)y(t).
\]

A pulse multiplies \(z\) by \(q_j/p_j^\lambda\). Using the neutrality equality over a full period gives

\[
z_{n+1}=z_n\exp(-J_n),\qquad
J_n=\int_{nT}^{(n+1)T}g(t)y(t)\,dt>0.
\]

Thus \(z_n\) decreases to some \(z_\infty\ge0\). In each cycle the bounded logarithmic derivative of \(y\) and finitely many fixed, strictly positive impulse multipliers provide a constant \(c>0\), independent of \(n\), with \(y(nT+t)\ge c y(nT)\) for all \(0\le t<T\). Similarly there is a uniform upper factor \(C\) bounding \(y(nT+t)\le C y(nT)\). If \(z_\infty>0\), telescoping yields \(\sum_n J_n=\log(z_0/z_\infty)<\infty\). Since \(g\) is bounded below, \(\int_0^\infty y<\infty\), and the uniform intra-cycle bounds force \(y(nT+t)\to0\), uniformly in \(t\in[0,T)\), including the right limits at pulses.

Now let \(u=1/x\) for the *full* system. It obeys \(\dot u=-[r(t)-b(t)y(t)]u+a(t)\) and jumps \(u^+=u^-/p_j\). On consecutive periods its exact linear-affine map has coefficients \(\alpha_n\to\alpha<1\), \(\beta_n\to\beta>0\) as \(y\to0\). For large \(n\), \(\alpha_n\le\rho<1\), so the standard contraction estimate for the differences \(u_n-u_*\) shows \(u_n\to u_*\); the variation-of-constants formula gives \(x(nT+t)\to x_*(t)\) uniformly over phases. Consequently \(z_n=y(nT)/x(nT)^\lambda\to0\), contradicting \(z_\infty>0\). We conclude \(z_\infty=0\). Even without assuming a summable load, the within-cycle representation below and bounded \(x\) imply \(y\to0\) as soon as \(z_n\to0\). Repeating the reciprocal argument therefore establishes unconditional convergence \(x\to x_*\) for every positive initial pair.

**4. Precise asymptotics.** The exact in-cycle representation, for \(0\le t<T\), is

\[
y(nT+t)=z_n S(t)x(nT+t)^\lambda
\exp\!\left[-\int_{nT}^{nT+t}g(u)y(u)\,du\right].
\]

The pulse convention in \(S\) makes this identity hold on both sides of a pulse. The proven convergence of \(x\) and \(y\), plus boundedness, implies uniformly in phase that \(y(nT+t)/z_n\to S(t)x_*(t)^\lambda\). Hence \(J_n/z_n\to I>0\). From the exact period relation,

\[
\frac1{z_{n+1}}-\frac1{z_n}=\frac{e^{J_n}-1}{z_n}\longrightarrow I.
\]

Cesàro averaging the increments yields \(1/(nz_n)\to I\). Thus \(nz_n\to1/I\), proving the full phase profile, and \(nJ_n=(nz_n)(J_n/z_n)\to1\). Finally the *exact* finite-cycle telescoping identity \(\sum_{k=0}^{N-1}J_k=\log(z_0/z_N)\) gives \(\int_0^{NT}g y=\log N+\log(z_0 I)+o(1)\), as stated. No finite simulation is used as an infinite-time argument.

## Verification

An executable finite diagnostic is included at `checks/pulse_critical_check.py`; it requires Python 3, NumPy and SciPy and runs with `python checks/pulse_critical_check.py`. It independently constructs a two-pulse example with seasonal growth and interaction rates, checks the neutral pulse-growth product to numerical precision, finds the resident cycle, integrates the coefficient \(I\), and compares the exact log-ratio identity with direct numerical integration. It also follows the loads for 2,800 cycles. For this illustrative case \(I\approx0.7974172507420441\), and at the final cycle \(nJ_n\approx1.000042086\) and \(nz_nI\approx0.999972226\). The maximum tested per-cycle log-ratio discrepancy is approximately \(5.05\times10^{-11}\). These tests check implementations and selected finite orbits; the universal and infinite-time claims are established by the argument above.

## Relationship to prior work

Courcelle, MacDonald and Patel [1] develop permanence and robust-permanence results for pulsed Lotka–Volterra systems. Their two-species Theorem 4.3 assumes **strict** invasion inequalities; these do not yield a global fate or an extinction coefficient at exact equality. Their primary model uses autonomous between-pulse flow and one periodic pulse. The present statement addresses the equality boundary for a coefficient-aligned competitive family, even with periodic seasonal functions and multiple pulses within each forcing period. Schreiber [2] develops sign-based invasion and extinction criteria for flow-kick systems; an exactly zero invasion exponent is not covered by the strict sign alternatives, and that work's described conclusions do not provide the displayed \(1/n\) amplitude or load law. Earlier impulsive competition work [3–5] addresses persistence and stability under other criteria; access to the full text of [3] and [4] was limited, so a conceptually equivalent older calculation remains possible.

The logarithmic-ratio cancellation is a classical idea, and the final scalar reciprocal/Cesàro step is elementary once this identity is available. What is asserted as the distinct result here is the **combined exact global critical classification**, the explicit forcing-and-pulse-dependent periodic profile, and the model-independent normalized load coefficient at neutrality, not discovery of either algebraic technique individually.

## Limitations

The interaction-coefficient alignment \(\lambda a\) and \(\lambda b+g\), the strict positivity of \(g\), strict positivity of the initial populations, a supercritical resident and exact neutral invasion are all essential hypotheses for the stated theorem. With unaligned coefficients, negative or amplifying nonpositive pulses, a marginal resident, or multiple interacting invaders, this proof does not establish the same rate. The limiting normalized load describes a deterministic dynamical model, not an empirical extinction-time prediction for finite populations. Although current source comparisons did not identify a covering theorem, novelty is not formally certified; broad impulsive-system literature may contain an equivalent reduction. The claim has not undergone independent scientific audit.

## References

[1] E. Courcelle, J. S. MacDonald, and S. Patel, *Persistence of n-Species Lotka–Volterra Models with Periodic Pulses*, arXiv:2609.09343v1 (first public 2026-09-08). https://arxiv.org/abs/2609.09343
[2] S. J. Schreiber, *Coexistence and Extinction in Flow-Kick Systems: An invasion growth rate approach*, arXiv:2507.02157v2; *J. Math. Biol.* **91**, 50 (2025). https://arxiv.org/abs/2507.02157
[3] J. Jin, L. Han, and Z. Li, *The persistence in a Lotka–Volterra competition systems with impulsive*, *Chaos, Solitons & Fractals* **24** (2005), 1105–1117. https://doi.org/10.1016/j.chaos.2004.09.065
[4] *The periodic competing Lotka–Volterra model with impulsive effect*, *Math. Med. Biol.* **21** (2004), 129 ff. https://doi.org/10.1093/imammb/21.2.129
[5] *Uniformly asymptotic stability of almost periodic solutions for a competitive system with impulsive perturbations*, *Adv. Difference Equations* (2014), article 2. https://doi.org/10.1186/1687-1847-2014-2
