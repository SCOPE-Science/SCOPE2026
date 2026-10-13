# Re-entrant dengue invasion under accelerated one-dose vaccination and waning protection

## Finding

Consider the full chronological-age/vaccination-age SISUV host–vector equations of Banerjee, Götz, and Panda, **before** the paper's replacement of vaccination-age efficacy by a constant mean efficacy and **before** its linearization of the mosquito quasi-steady response. Let the vaccination rate \(\nu\geq0\) be constant, common to susceptible and infected unvaccinated hosts, and let vaccination efficacy at time \(y\) after the dose be \(\Omega(y)=e^{-y}\). There is an admissible set of strictly positive age-specific human-exposure rates for which the disease-free linear infection system has a growing exponential mode both with no vaccination and with all sufficiently large finite vaccination rates, but has no exponential mode with nonnegative real growth rate at the intermediate rate \(\nu=1\).

Specifically, at the fully specified parameter values below, the *mosquito-to-human-to-mosquito invasion multiplier* \(\mathcal K(\nu)\) satisfies

\[
1.17<\mathcal K(0)<1.18,\qquad
0.91<\mathcal K(1)<0.92,\qquad
1.05<\lim_{\nu\to\infty}\mathcal K(\nu)<1.06.
\]

Continuity therefore forces **at least two distinct vaccination-rate threshold crossings**: one in \((0,1)\) and another in \((1,\infty)\). No assertion is made that these are the only crossings. The mechanism is vaccination too early for protection that wanes before the age of greatest exposure. This is a threshold/invasion result, not a theorem that endemic solutions exist or that a positive equilibrium is globally attracting.

## Assumptions and scope

Host chronological age is \(x\in[0,A]\), with maximum age \(A>0\), and vaccinated host age since vaccination is \(0\leq y\leq x\). The nonvaccinated susceptible and infected densities are \(Q(t,x),J(t,x)\); vaccinated susceptible and infected densities are \(S(t,x,y),I(t,x,y)\). Susceptible and infected mosquitoes have populations \(u(t),v(t)\). Hosts have age-dependent natural mortality \(\mu(x)\geq0\), birth rate \(b(x)\geq0\), infected recovery rate \(\gamma>0\), mosquito recruitment \(\Lambda>0\), mosquito mortality \(\rho>0\), human incidence coefficient \(\vartheta(x)>0\) and human-to-mosquito transmission coefficient \(\sigma(x)>0\). Human incidence from infectious mosquitoes is \(\vartheta(x)v(t)/N(t)\) times susceptibility, with vaccinated susceptibility multiplied by \(1-\Omega(y)\). This is exactly the mechanism in equations (3)–(8) of the cited 2026 model.

Assume an infection-free stationary demographic profile \(p(x)>0\) satisfying \(p'(x)=-\mu(x)p(x)\), \(p(0)=\int_0^A b(x)p(x)\,dx\), and \(N=\int_0^A p(x)\,dx>0\). Susceptible vaccination occurs at rate \(\nu\), and vaccinations of infected unvaccinated hosts at the same rate transfer them into the infected vaccinated class. Vaccination is administered once; this model does not contain boosters, renewed vaccination of vaccinees, or waning back into the unvaccinated class.

The concrete example fixes

\[
A=4,\quad \mu(x)=1,\quad \gamma=\rho=\sigma(x)=1,\quad \Lambda=28,
\quad p(x)=e^{-x},\quad N=1-e^{-4},\quad b(x)=\frac1{1-e^{-4}},
\]

\[
\vartheta(x)=\frac1{1000}+\mathbf 1_{[2,3]}(x),\qquad
\Omega(y)=e^{-y},\qquad \nu\geq0.
\]

These are nondimensional parameters of the mathematical model, not estimated clinical vaccination rates. The exposure coefficient is **strictly positive at every age**, including outside the late-exposure window; its two jumps are allowed because the model requires bounded measurable age coefficients. Natural mortality and recovery are both strictly positive, and the renewal condition \(p(0)=\int_0^4 b(x)p(x)\,dx\) holds exactly.

## Proof

**1. Infection-free vaccination-age distribution.** At the disease-free demographic state, all hosts are susceptible, and the infection-free characteristic equations give

\[
Q_0(x)=p(x)e^{-\nu x},\qquad
S_0(x,y)=\nu p(x)e^{-\nu(x-y)}\mathbf 1_{0\leq y\leq x}.
\]

The density \(S_0\) includes vaccination upon exiting the unvaccinated class at chronological age \(x-y\); common host mortality is already absorbed into \(p(x)\). Direct integration shows \(Q_0(x)+\int_0^xS_0(x,y)dy=p(x)\). Thus the full vaccination-age model's disease-free fraction susceptible to a new mosquito-transmitted infection is

\[
g_\nu(x)=\frac{Q_0(x)+\int_0^x(1-\Omega(y))S_0(x,y)dy}{p(x)}
=1-P_\nu(x),
\quad
P_\nu(x)=\int_0^x\nu e^{-\nu a}\Omega(x-a)\,da.
\]

Here \(a\) is the chronological age at first vaccination. For \(\Omega(y)=e^{-y}\),

\[
P_0(x)=0,\quad P_1(x)=xe^{-x},\quad
P_\nu(x)=\frac{\nu(e^{-x}-e^{-\nu x})}{\nu-1}\ (\nu\ne1),\quad
\lim_{\nu\to\infty}P_\nu(x)=e^{-x}\quad (x>0).
\]

The last limit is dominated-convergence/approximate-identity convergence; no uniformly positive lower bound on the age of vaccination is assumed.

**2. Exact infection linearization and threshold.** Put \(H(t,x)=J(t,x)+\int_0^x I(t,x,y)dy\). The infected vaccination flux \(\nu J\) enters \(I\) at \(y=0\) and leaves \(J\), and hence cancels on adding the linearized infected-host transport equations. At the disease-free state, \(H=p h\) obeys

\[
\partial_t h+\partial_x h=-\gamma h+\frac{\vartheta(x)}N g_\nu(x)v(t),\quad h(t,0)=0,
\qquad
v'(t)=\frac\Lambda\rho\int_0^A\sigma(x)p(x)h(t,x)dx-\rho v(t).
\]

The susceptible-mosquito perturbation does not enter this first-order infected subsystem; at the disease-free state \(u_0=\Lambda/\rho\). For an exponential mode with complex growth parameter \(s\), characteristic integration yields

\[
s+\rho=\frac\Lambda{\rho N}\int_0^A \vartheta(a)g_\nu(a)
\int_a^A\sigma(x)p(x)e^{-(\gamma+s)(x-a)}\,dx\,da.
\]

Therefore define

\[
\boxed{\mathcal K(\nu)=\frac\Lambda{\rho^2 N}
\int_0^A\vartheta(a)[1-P_\nu(a)]
\int_a^A\sigma(x)p(x)e^{-\gamma(x-a)}\,dx\,da.}
\]

For positive coefficients, the right side of the characteristic equation is strictly decreasing in **real** \(s\geq0\), while its left side increases. Hence a positive real growing mode exists exactly when \(\mathcal K(\nu)>1\). Conversely, if \(\mathcal K(\nu)<1\) and \(\Re s\geq0\), taking absolute values bounds the right side by \(\rho\mathcal K(\nu)<\rho\leq|s+\rho|\), a contradiction. The equality case has the zero mode; the theorem needs only the strict cases. This establishes the claimed invasion criterion for the full host–vector infection linearization without making an unproved assertion about nonlinear persistence.

**3. Exact example and two crossings.** With the parameters displayed above,

\[
w(a):=\int_a^4 e^{-x}e^{-(x-a)}dx
=\frac{e^{-a}-e^{a-8}}2,\qquad
q(a)=\frac1{1000}+\mathbf 1_{[2,3]}(a).
\]

Set

\[
B_0=\int_0^4q(a)w(a)da,\quad
C_\infty=\int_0^4 q(a)w(a)e^{-a}da,\quad
C_1=\int_0^4 q(a)w(a)ae^{-a}da.
\]

Elementary antiderivatives produce, writing \(E=e^{-1}\),

\[
B_0=\frac{1+1000E^2-1000E^3-2E^4-1000E^5+1000E^6+E^8}{2000},
\]

\[
C_\infty=\frac{1+1000E^4-1000E^6-2009E^8}{4000},\qquad
C_1=\frac{1+5000E^4-7000E^6-10041E^8}{8000}.
\]

Consequently,

\[
\mathcal K(0)=\frac{28B_0}{1-E^4},\qquad
\mathcal K(1)=\frac{28(B_0-C_1)}{1-E^4},\qquad
\mathcal K(\infty)=\frac{28(B_0-C_\infty)}{1-E^4}.
\]

The accompanying standalone exact rational-interval check uses the 29th and 30th alternating Taylor truncations for \(e^{-1}\) to enclose all three expressions without floating-point assumptions. Its certified intervals are those in the Finding section. In particular, the strict inequalities \(\mathcal K(0)>1>\mathcal K(1)\) and \(\mathcal K(\infty)>1\) follow. Since \(P_\nu\) is continuous in \(\nu\) under the bounded integral, so is \(\mathcal K\). An intermediate-rate infection-invasion-suppressed region separates low-rate and sufficiently high-rate infection-invasion regimes by the intermediate value theorem.

**4. Why acceleration eventually harms the threshold.** For ages \(a>1\), the fraction protected at the intermediate rate is \(P_1(a)=ae^{-a}>e^{-a}=P_\infty(a)\). The dominant age-of-exposure window \([2,3]\) is entirely in this range. The small strictly positive background exposure makes the example conform to a positive age coefficient while retaining \(\mathcal K(1)<\mathcal K(\infty)\). A one-time dose administered close to birth has more time to wane before peak exposure than a dose administered later in life; increasing the vaccination hazard changes not just coverage but the distribution of time since the dose.

## Verification

Run \(\texttt{python3 verify.py}\) from the unpacked directory. It checks the displayed elementary-integral formulas using exact rational expressions in \(E=e^{-1}\), encloses \(E\) between alternating-series rational truncations, propagates interval arithmetic through the three reproduction multipliers, and prints `VERIFY_OK` only if the strict threshold inequalities hold. The verifier proves the finitely many required numerical inequalities; the transport, characteristic-equation, and continuity arguments above provide the infinite-dimensional mathematical proof.

## Relationship to prior work

Banerjee–Götz–Panda (arXiv:2602.21150, first version 24 February 2026) supply the chronological-age/vaccination-age SISUV equations and prove existence and uniqueness of an endemic fixed point **after** using a constant averaged vaccine efficacy \(\Omega_b\) (their equation (29)) and approximating mosquito recruitment feedback under low infection pressure (their equation (27)). Our result instead linearizes the **original, unaveraged equations (3)–(8)** at the disease-free state, restores explicit dependence on elapsed vaccination age, and identifies a re-entrant invasion outcome when the vaccination rate is varied. It does not strengthen or dispute their equilibrium uniqueness theorem for the averaged model.

Webb (2025) studies reproduction numbers in infection-age/vaccination-age epidemiology and Webb–Zhao (2024) study time-dependent vaccination effectiveness. These are methodological antecedents, not attributed as establishing this exact two-crossing parameter example for the full vector–host chronological-age model. Older literature on waning vaccine protection and optimal age at vaccination already makes clear that vaccination timing matters; the broad qualitative principle is not claimed as new. The contribution is the stated **mathematically exact counterexample in the unreduced 2026 dengue system**, with a positive exposure coefficient and a rigorously bounded invasion multiplier.

## Limitations

The model uses a single dose, deterministic age-specific transmission, stationary demography, and exponentially waning vaccine protection. Time rates are nondimensional, and the example should not be interpreted as an empirical vaccination recommendation. A linear invasion threshold does not establish whether endemic attractors or hysteretic nonlinear epidemic trajectories exist. The theorem guarantees at least two threshold crossings, not exactly two or a complete bifurcation diagram. The 2025 general vaccination-age article was not fully accessible for theorem-by-theorem comparison; independent novelty review remains outstanding. The present result does not claim novelty for general age-targeted vaccination principles.

## References

1. S. Banerjee, T. Götz, and S. Panda, *Age-Structured Epidemic Model under Vaccination with Vector Transmission*, arXiv:2602.21150v1 (24 February 2026); v2 (25 April 2026). https://arxiv.org/html/2602.21150
2. G. F. Webb, *Basic reproduction numbers for infection and vaccination age epidemic models*, *Numerical Algebra, Control and Optimization*, early access 30 April 2025. https://doi.org/10.3934/naco.2025013 (primary MSC 92C60).
3. G. F. Webb and X. E. Zhao, *An Epidemic Model with Infection Age and Vaccination Age Structure*, *Infectious Disease Reports* 16 (2024), 35–64. https://doi.org/10.3390/idr16010004
4. V. Rouderfer, N. G. Becker, and H. W. Hethcote, *Waning immunity and its effects on vaccination schedules*, *Mathematical Biosciences* 124 (1994), 59–82. https://doi.org/10.1016/0025-5564(94)90024-8
