# Unbounded mutation erases the final susceptible fraction in an evolutionary SIR equation

## Finding

**Final-size domain dichotomy and singular mutation limit.** Let the infective trait be a nonnegative transmission-rate multiplier. In the susceptible–infected–recovered model below, with strictly positive initial infected mass and a strictly positive trait-diffusion coefficient, reflecting mutation on the full nonnegative half-line implies
\[
S(t)\longrightarrow0,\qquad I(t)\longrightarrow0,\qquad R(t)\longrightarrow1.
\]
This holds no matter how small the diffusion coefficient is or how low the initial infectivity is. On the finite trait interval \([0,L]\), with reflecting mutation, the final susceptible fraction is instead strictly positive and satisfies the sharp, parameter-dependent lower bound \(S_\infty\ge u_L\), where \(u_L\in(0,S_0)\) is the unique root of
\[
\log\frac{S_0}{u_L}=\frac{kL}{\mu}(S_0+I_0-u_L).
\]
For fixed smooth initial infected data of compact support on the half-line, the zero-mutation and long-time limits do not commute:
\[
\lim_{\mathcal D\downarrow0}\lim_{t\to\infty}S_{\mathcal D}(t)=0
\quad<\quad
\lim_{t\to\infty}\lim_{\mathcal D\downarrow0}S_{\mathcal D}(t)=S_{0\mathrm{diff},\infty}.
\]
Here \(S_{0\mathrm{diff},\infty}>0\) denotes the terminal susceptible fraction when the diffusion coefficient equals zero, not the initial susceptible fraction \(S_0\).

## Assumptions and scope

Fix contact coefficient \(k>0\) and recovery rate \(\mu>0\). On a trait domain \(\Omega\), let the nonnegative infected density \(\rho(t,\lambda)\) satisfy
\[
\partial_t\rho=\frac{\mathcal D}{2}\partial_{\lambda\lambda}\rho+(k\lambda S(t)-\mu)\rho,
\qquad I(t)=\int_\Omega\rho(t,\lambda)\,d\lambda.
\]
Define \(S(0)=S_0>0\), \(R(0)=R_0\ge0\), and \(I(0)=I_0>0\) with \(S_0+I_0+R_0=1\). Couple the compartments by
\[
S'=-kS\int_\Omega\lambda\rho(t,\lambda)\,d\lambda,
\qquad R'=\mu I.
\]
Choose smooth, nonnegative, compactly supported initial density \(\rho_0\not\equiv0\) of integral \(I_0\), compatible with the boundaries when diffusion is present. Use the no-flux condition \(\partial_\lambda\rho=0\) at finite endpoints. On the unbounded half-line \(\Omega=[0,\infty)\), impose reflection at zero and the natural integrable decay at infinity, and take \(\mathcal D>0\). On \([0,L]\), assume \(L>0\) and \(\mathcal D\ge0\). For the singular comparison on \([0,\infty)\), fix the same compactly supported \(\rho_0\) while \(\mathcal D\downarrow0\). Solutions mean global nonnegative mass-conserving classical/mild solutions with finite trait first moments on finite time intervals.

The underlying infection probability in the motivating microscopic formulation is physically bounded by one. The unbounded model is a **mathematical rate-trait extension** of its continuum selection–diffusion equation, not a probability-valued model or an epidemiological forecast.

## Proof

**1. Global mass budget and prevalence decay.** Integrating the mutation equation with no-flux boundaries gives
\[
I'=kS\int_\Omega\lambda\rho\,d\lambda-\mu I=-S'-\mu I.
\]
Thus \(S+I+R=1\), \(S\) is nonincreasing and strictly positive at any finite time, and \(0\le I,R\le1\). Local existence and finite-time first moments follow from the Neumann heat semigroup and standard local coupling arguments. On \([0,\infty)\), the coefficient \(k\lambda S(t)\le k\lambda\); the Feynman–Kac upper comparison with reflecting Brownian motion of variance parameter \(\mathcal D\) controls \(\int(1+\lambda)\rho(t,\lambda)d\lambda\) on every finite time interval. Indeed, for starting trait \(\lambda_0\) in the compact initial support and \(0\le t\le T\), a reflected path obeys \(X_t\le\lambda_0+\sqrt{\mathcal D}\sup_{s\le T}|B_s|\), and its time-integral exponential has finite expectation by Gaussian maximal tails. The mass budget then extends the local solution globally.

Since \(-S'\ge0\) and \(\int_0^\infty(-S')dt\le S_0\), variation of constants yields
\[
I(t)=I_0e^{-\mu t}+\int_0^t e^{-\mu(t-v)}[-S'(v)]\,dv\longrightarrow0.
\]
The last convergence holds because convolution of an integrable nonnegative function with a decaying exponential tends to zero. Consequently \(R_\infty=1-S_\infty\), with \(S_\infty\in[0,S_0]\).

**2. Every positive diffusion coefficient exhausts susceptibles on the half-line.** Suppose \(a=S_\infty>0\). Fix any width \(H>0\). Choose \(L_*>0\) so large that
\[
\eta:=k a L_*-\mu-\frac{\mathcal D\pi^2}{2H^2}>0.
\]
Indeed, since \(k\lambda S\ge0\), Duhamel comparison with the reflecting heat semigroup gives \(\rho(t_0,\lambda)\ge e^{-\mu t_0}(P_{t_0}\rho_0)(\lambda)>0\) for every \(\lambda>0\) and \(t_0>0\). Hence for some \(c>0\), on the closed interval \([L_*,L_*+H]\),
\[
\rho(t_0,\lambda)\ge c\sin\!\left(\frac{\pi(\lambda-L_*)}{H}\right).
\]
Define on this subinterval, with zero Dirichlet values at its endpoints,
\[
w(t,\lambda)=c e^{\eta(t-t_0)}
\sin\!\left(\frac{\pi(\lambda-L_*)}{H}\right).
\]
Because \(S(t)\ge a\) and \(\lambda\ge L_*\), this function is a subsolution of the exact linear equation obeyed by \(\rho\), conditional on the actual \(S(t)\):
\[
\partial_tw-\frac{\mathcal D}{2}\partial_{\lambda\lambda}w-(k\lambda S(t)-\mu)w\le0.
\]
Parabolic comparison on the fixed interval gives \(\rho\ge w\). Therefore
\[
I(t)\ge\int_{L_*}^{L_*+H}w(t,\lambda)d\lambda
=\frac{2cH}{\pi}e^{\eta(t-t_0)}\longrightarrow\infty,
\]
contrary to \(I(t)\le1\). Thus \(S_\infty=0\), and step 1 gives \(I_\infty=0\), \(R_\infty=1\). The interval is chosen after the hypothetical \(a>0\) is fixed; no uniform lower bound in diffusion strength is asserted.

**3. Bounded traits retain susceptibles, with a sharp lower bound.** On \([0,L]\), \(0\le\lambda\le L\). The equation for \(S\) yields
\[
\log\frac{S_0}{S_\infty}
=k\int_0^\infty\!\int_0^L\lambda\rho(t,\lambda)\,d\lambda dt
\le kL\int_0^\infty I(t)dt
=\frac{kL}{\mu}(S_0+I_0-S_\infty).
\]
Positivity of \(S_\infty\) follows already from the weaker inequality \(S_\infty\ge S_0\exp[-kL(1-R_0)/\mu]>0\). Set \(\beta=kL/\mu\). The strictly convex function
\[
h(x)=\log(S_0/x)-\beta(S_0+I_0-x)
\]
tends to \(+\infty\) as \(x\downarrow0\) and is negative at \(x=S_0\), so it has exactly one root \(u_L\) in \((0,S_0)\). The established inequality \(h(S_\infty)\le0\) forces \(S_\infty\ge u_L\).

The bound is **sharp as an infimum** over admissible initial densities and mutation coefficients. Take \(\mathcal D=0\) and smooth densities supported in \([L-\varepsilon,L]\) with the specified infected mass. The same integrated inequality with both \(L-\varepsilon\) and \(L\) brackets their terminal susceptible fractions between the corresponding two homogeneous-SIR final-size roots; both roots converge to \(u_L\) as \(\varepsilon\downarrow0\). Equality is exact for a measure-valued monomorphic initial distribution concentrated at \(L\), if those initial data are admitted.

**4. Zero-mutation singularity.** Fix compactly supported initial \(\rho_0\) on \([0,\infty)\). When \(\mathcal D=0\), the support remains in some \([0,L]\); step 3 gives a strictly positive terminal susceptible fraction. In contrast, step 2 gives zero for every \(\mathcal D>0\). Over any finite time interval, Neumann heat-semigroup continuity as \(\mathcal D\downarrow0\), together with the above finite-horizon Feynman–Kac moment bound and continuity of the coupled scalar equations, gives \(S_{\mathcal D}(t)\to S_{0\mathrm{diff}}(t)\) for every fixed finite \(t\). Taking limits in the two orders yields the displayed strict inequality.

## Verification

The accompanying `verify.py` uses standard-library exact rational arithmetic to check a sample high-trait interval certificate. For \(k=2\), \(\mu=1\), \(\mathcal D=1\), \(a=1/10\), \(L_*=40\), \(H=1\), the coefficient \(kaL_*-\mu-\mathcal D\pi^2/(2H^2)\) is strictly greater than \(2\), using \(\pi^2<10\). It also numerically brackets the unique bounded-domain root for \(S_0=99/100\), \(I_0=1/100\), \(kL/\mu=2\). These checks illustrate, rather than replace, the analytic estimates in the proof. Run `python3 verify.py` on the standalone companion file; the expected final line is `VERIFY_OK`.

## Relationship to prior work

Lamata-Otín, Arenas, Gómez-Gardeñes, and Soriano-Paños (2026), arXiv:2603.18801, introduce the evolving-infectivity SIR continuum equation and analyze early-time growth, policy-sensitive infection peaks, and numerically evaluated attack rates. Their supplementary derivations explicitly rely on diffusion distributions lying away from boundaries for the early-time moment approximation. The result here instead resolves the **infinite-time, exact continuum** limit for a specified reflecting half-line versus a bounded trait domain. It does not purport to invalidate finite-time simulations or the bounded-probability interpretation.

Alfaro and Carles (2014) solve the **mass-normalized replicator–mutator equation** with linear fitness and analyze Gaussian acceleration; these heat-transform phenomena are prior work, not claimed here. Their equation does not couple a susceptible mass to a recovering infection population and hence does not state this SIR final-size dichotomy. Almeida et al. (2020/2021) study final-size equations in heterogeneous SEIR systems, including diffusion under their own structured-population assumptions; their general framework is a serious comparison point, but its publicly accessible abstract/preview did not establish this particular unbounded evolving-infectivity claim. Bernardi et al. (2025) provide a broad structured-compartment framework whose explicit underlying trait domains are bounded intervals, and therefore do not entail the present half-line result.

## Limitations

The positive-diffusion zero-susceptible conclusion is for the **uncapped, unbounded rate-trait PDE**, not for physical transmission probabilities, which cannot exceed one. No result here quantifies the potentially enormous time required for rare high-trait mutation tails to matter, and no finite-population extinction statement is made. Bounds concern exact deterministic asymptotics; stochastic fadeout and numerical prevalence cutoffs are outside scope. The capped bound is an infimum over mutation strengths allowing zero; it need not be attained by smooth initial densities with strictly positive diffusion. A plausible broad heterogeneous-SEIR final-size reference was not accessible in full, so completeness of the originality comparison is an acknowledged residual risk.

## References

1. S. Lamata-Otín, A. Arenas, J. Gómez-Gardeñes, D. Soriano-Paños, *Interplay between evolutionary and epidemic time scales challenges the outcome of control policies*, arXiv:2603.18801v1 (first posted 2026-03-19); arXiv:2603.18801v2 (2026-10-03). https://arxiv.org/abs/2603.18801 ; full HTML https://arxiv.org/html/2603.18801v1 .
2. M. Alfaro and R. Carles, *Explicit solutions for replicator-mutator equations: extinction vs. acceleration*, SIAM J. Appl. Math. 74 (2014), 1919–1934, arXiv:1405.2768, DOI 10.1137/140979411. https://arxiv.org/html/1405.2768v1 .
3. L. Almeida, P.-A. Bliman, G. Nadin, B. Perthame, N. Vauchelet, *Final size and convergence rate for an epidemic in heterogeneous populations*, Mathematical Models and Methods in Applied Sciences 31 (2021), 1021–1051, arXiv:2010.15410, DOI 10.1142/S0218202521500251.
4. E. Bernardi, T. Lorenzi, M. Sensi, A. Tosin, *Heterogeneously structured compartmental models of epidemiological systems: from individual-level processes to population-scale dynamics*, Studies in Applied Mathematics (2025); consult the original for its model domain and hypotheses before transferring general conclusions.
