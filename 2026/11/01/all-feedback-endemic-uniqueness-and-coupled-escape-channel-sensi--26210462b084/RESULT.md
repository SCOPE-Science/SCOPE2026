# All-feedback endemic uniqueness and coupled escape-channel sensitivity at maximal reinfection

## Finding

Consider the autonomous four-compartment SIRCm system with transmission-driven feedback \(g=SI\), as specified below. At the maximal-reinfection endpoint \(\sigma=1\), for arbitrary positive demographic and transition rates and arbitrary independently chosen nonnegative feedback strengths \(\varepsilon_1,\varepsilon_2\), the following complete equilibrium classification holds.

If \(\beta\leq\mu+\alpha\), the disease-free equilibrium \((1,0,0,0)\) is the only equilibrium in the population simplex. If \(\beta>\mu+\alpha\), there is exactly one endemic equilibrium, and all four of its coordinates are strictly positive. Its transmission signal \(Z^*=S^*I^*\) is strictly increasing in each feedback strength separately, throughout the entire nonnegative parameter quadrant. Its infected fraction \(I^*\) is strictly increasing in \(\varepsilon_1\). As a function of \(\varepsilon_2\), \(I^*\) is strictly increasing whenever \(\varepsilon_1>0\), but is **exactly independent** of \(\varepsilon_2\) when \(\varepsilon_1=0\). This distinction concerns endemic equilibria, not orbital stability.

There is also an exact large-\(\varepsilon_2\) limit. Put \(k=(\mu+\alpha)/\beta\), \(a=1-k\). With \(\varepsilon_1\) fixed, \(Z^*\) increases to the unique positive root \(z_\infty\in(0,ka)\) of
\[
\delta\varepsilon_1 z^2+(\alpha+\mu+\delta-ka\delta\varepsilon_1)z-ka(\mu+\delta)=0.
\]
The corresponding equilibrium satisfies \(C^*\to0\), \(S^*\to k\), and \(I^*\to z_\infty/k\). For \(\varepsilon_1=0\), the quadratic is interpreted as its linear specialization.

## Assumptions and scope

The state space is \(\Omega=\{(S,I,R,C)\in[0,1]^4:S+I+R+C=1\}\), and \(\mu,\beta,\alpha,\delta,\gamma>0\). The endpoint \(\sigma=1\) means that every contact between cross-immune and infectious individuals produces an infection, rather than a noninfectious clearance. The feedback parameters \(\varepsilon_1,\varepsilon_2\ge0\) are independent and finite. Define \(G_j=1+\varepsilon_j SI\). The ordinary differential equations are
\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta SI+\gamma G_2C,\\
\dot I&=\beta(S+C)I-(\mu+\alpha)I,\\
\dot R&=\alpha I-(\mu+\delta G_1)R,\\
\dot C&=\delta G_1R-(\beta I+\mu+\gamma G_2)C.
\end{aligned}
\]
These are exactly the transmission-driven equations of Ramírez-Gutiérrez et al. [1] with \(\sigma=1\); there is no seasonal forcing. No conclusion for general \(0<\sigma<1\) is claimed. All derivatives or order comparisons below concern equilibrium coordinates, not empirical causal estimates.

## Proof

**1. Disease-free and threshold cases.** If \(I=0\) at equilibrium, the \(R\) equation gives \(R=0\); then the \(C\) equation gives \(C=0\), hence \(S=1\). If \(I>0\), the infected equation yields \(S+C=k=(\mu+\alpha)/\beta\). But \(S+C=1-I-R<1\), so necessarily \(k<1\). Hence the disease-free equilibrium is unique when \(\beta\le\mu+\alpha\).

**2. A one-dimensional parametrization.** Assume \(k<1\), let \(a=1-k>0\), \(U=\mu a>0\), \(V=\mu+\gamma>0\), and \(g=\gamma\varepsilon_2\ge0\). Write \(z=SI\). At an endemic equilibrium, \(S+C=k\), \(R=a-I\), and the stationary susceptible equation gives
\[
C_g(z)=\frac{\beta z-U}{V+gz},\quad
S_g(z)=k-C_g(z),\quad
I_g(z)=\frac{z}{S_g(z)},\quad
R_g(z)=a-I_g(z).
\tag{1}
\]
The lower endpoint is \(z_0=U/\beta>0\). On the interval \(z>z_0\) where \(S_g(z)>0\),
\[
C_g'(z)=\frac{\beta V+gU}{(V+gz)^2}>0,
\]
so \(S_g\) strictly decreases, \(I_g=z/S_g\) strictly increases, and \(R_g\) strictly decreases. At \(z=z_0\), \(C_g=0\) and \(I_g=\mu a/(\mu+\alpha)<a\). At the other end of the maximal domain where \(S_g>0\), \(I_g\) tends to infinity: either \(S_g\downarrow0\) at a finite endpoint, or \(z\to\infty\) with \(S_g\le k\). Thus there is a unique \(z_{\max}(g)>z_0\) with \(I_g(z_{\max})=a\). Precisely for \(z\in(z_0,z_{\max})\), all four quantities in (1) are positive and sum to one.

**3. Strictly monotone equilibrium equation.** The stationary \(C\) equation is equivalent to
\[
G_g(z)=\delta\left(\frac1z+\varepsilon_1\right),
\quad
G_g(z):=\frac{C_g(z)}{zR_g(z)}\left(\beta I_g(z)+V+gz\right).
\tag{2}
\]
Using (1), this function factors exactly as
\[
G_g(z)=\frac{\beta-U/z}{R_g(z)}
\left(1+\frac{\beta z}{S_g(z)(V+gz)}\right).
\tag{3}
\]
The factor \(\beta-U/z\) is strictly increasing and positive on \((z_0,z_{\max})\). The factor in parentheses is strictly increasing because \(z/(V+gz)\) and \(1/S_g(z)\) are strictly increasing. Finally \(1/R_g(z)\) strictly increases. Thus \(G_g\) increases strictly and continuously from zero to infinity. The right side of (2) is strictly decreasing in \(z\). Consequently there is exactly one \(z^*\) satisfying (2). At that point the stationary \(S,I,C\) equations hold. Conservation of the unit sum gives \(\dot R=0\), proving both existence and uniqueness of the strictly positive equilibrium.

**4. Comparative statics.** Increasing \(\varepsilon_1\) raises the right side of (2) at fixed \(z\) and leaves \(G_g\) unchanged; the unique solution \(z^*\) therefore increases strictly. For \(g_2>g_1\ge0\), and at each feasible fixed \(z>z_0\) for \(g_1\), (1) gives \(C_{g_2}(z)<C_{g_1}(z)\), \(S_{g_2}(z)>S_{g_1}(z)\), and \(R_{g_2}(z)>R_{g_1}(z)\). Formula (3) then gives \(G_{g_2}(z)<G_{g_1}(z)\). That fixed \(z\) remains feasible for \(g_2\). At the equilibrium for \(g_1\), equation (2) is strictly below equality for \(g_2\); uniqueness and strict increase in \(z\) show \(z^*(g_2)>z^*(g_1)\). Since \(g=\gamma\varepsilon_2\), the transmission signal strictly increases in \(\varepsilon_2\) as well.

At equilibrium, the stationary \(R\) equation and \(R=a-I\) give the exact relation
\[
I^*=a\,\frac{M}{\alpha+M},
\qquad M=\mu+\delta(1+\varepsilon_1 z^*).
\tag{4}
\]
The right side is strictly increasing in \(M\). Increasing \(\varepsilon_1\) strictly increases \(\varepsilon_1 z^*\), including a change from zero to a positive value. For fixed \(\varepsilon_1>0\), increasing \(\varepsilon_2\) increases \(z^*\) and hence \(M\). If \(\varepsilon_1=0\), \(M=\mu+\delta\) is independent of \(\varepsilon_2\). These are exactly the claimed strict and zero comparative statics.

**5. Large second-channel feedback.** Since \(z^*=S^*I^*<ka\), strict increase in \(g\) gives a limit \(z_\infty\in[z^*(0),ka]\). In (1), \(C_g(z^*)\to0\) because the numerator is bounded and \(g z^*\to\infty\), so \(S^*\to k\) and \(I^*\to z_\infty/k\). Passing to the exact equation (4) yields the quadratic displayed under Finding. Its constant coefficient is strictly negative and its leading coefficient is nonnegative; if \(\varepsilon_1>0\) there is exactly one positive root, and if \(\varepsilon_1=0\) there is exactly one positive linear root. Equation (4) also gives \(I^*<a\), so the limiting root belongs to \((0,ka)\). This proves the stated limit. \(\square\)

## Verification

The self-contained `verify.py` uses exact rational identities to check the scalar reduction and evaluates equilibrium residuals for 80 parameter combinations with independently varied feedbacks. It also checks the predicted monotonic and zero-dependence cases numerically. Run `python verify.py` with Python 3 standard library. Numerical tests are corroboration only: the strict all-parameter inequalities, infinite-domain uniqueness, and limiting formula are established analytically in the proof.

## Relationship to prior work

The SIRCm model, including the two distinct mechanisms \(g=SI\) and \(g=I\), is due to Ramírez-Gutiérrez, Lóczi, Muñoz-Moncayo and Ketcheson [1]. They establish endemic existence for arbitrary feedbacks and uniqueness in weak and strong feedback regimes, but their general transmission-driven quartic analysis does not establish the all-feedback endpoint classification or the cross-channel comparative statics above. The original SIRC model [2] is the zero-feedback special case and cannot imply strict dependence on two positive feedback strengths.

An earlier exact all-feedback theorem for the *prevalence-driven* SIRCm system [3] proves uniqueness and, at \(\sigma=1\), independence of endemic infection from the second feedback parameter. That is a different model: replacing \(g=I\) with \(g=SI\) couples the second feedback to the first through the susceptible fraction. The present theorem shows a strict response when \(\varepsilon_1>0\) in the transmission-driven case. In particular, [3] does not imply this opposite strict-dependence conclusion. The proof uses a direct scalar monotonicity reduction rather than general global-stability claims.

## Limitations

The theorem is limited to \(\sigma=1\), the maximal-reinfection endpoint. It does not cover \(0<\sigma<1\), nonautonomous transmission, negative feedback parameters, vanishing positive rate coefficients, or the stability of endemic equilibria and periodic trajectories. The numerical checks are finite diagnostics rather than exhaustive proof. The absence of an exact match in searched records is not a proof of historical priority; a general scalar monotonicity theorem may subsume parts of the argument. The 2006 original SIRC article was consulted only through accessible abstract/metadata, not full text. There has been no independent scientific validation.

## References

1. D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo and D. I. Ketcheson, *Compartmental epidemiological models with infection-driven immune escape*, arXiv:2610.01111v1, first publicly posted 2026-10-01. https://arxiv.org/html/2610.01111v1 (especially equations (1)–(3), Sections 3–4 and Appendix 7).
2. R. Casagrandi, L. Bolzoni, S. A. Levin and V. Andreasen, *The SIRC model and influenza A*, Mathematical Biosciences 200 (2006), 152–169, DOI:10.1016/j.mbs.2005.12.029.
3. *All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system*, published published-finding corpus record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342 (RESULT.md, full text inspected).
