# Sharp mortality–recruitment threshold for first arrivals of independent Brownian searchers

## Finding

Consider independent one-dimensional diffusers which each start a distance \(d>0\) from a perfectly absorbing target and undergo independent exponential mortality. Besides one initially present particle, fresh particles are injected by a homogeneous Poisson process. The exact survival identity for this model is established in previous literature; the finding here is the following *joint large-recruitment and large-mortality limit*, including its sharp critical window.

Write \(\theta=d^2/D\), where \(D>0\) is the Brownian diffusivity (generator \(D\partial_x^2\)), \(R=\lambda\theta\), and \(L=\log R\). Let \(T_{\lambda,\mu}\) be the first target-arrival time, \(Z_R=T_{\lambda,\mu}/\theta\). Suppose \(R\to\infty\) and \(\mu\theta=c^2L^2\) with a fixed \(c\ge0\).

**Subcritical regime.** For \(0\le c<1\), put
\[
h_c=\frac{1}{2(1+\sqrt{1-c^2})},\quad a_c=\frac{1}{4h_c^2}-c^2>0,\quad C_c=\frac{1}{2\sqrt\pi\,h_c^{3/2}a_c^2}.
\]
Then \(LZ_R\to h_c\) in probability. More precisely,
\[
W_R=a_c(L^2Z_R-h_cL)-\frac52\log L+\log C_c
\]
converges in distribution to the *reflected Gumbel* law
\[
\lim_{R\to\infty}\mathbb P(W_R>w)=\exp(-e^w),\qquad w\in\mathbb R.
\]
The \(\frac52\log\log R\) centering correction is part of the theorem.

**At and above the threshold.** For \(c\ge1\),
\[
R^{1-c}Z_R\ \Longrightarrow\ \operatorname{Exp}(1).
\]
In particular \(Z_R\Longrightarrow\operatorname{Exp}(1)\) at \(c=1\), whereas for \(c>1\) the typical arrival time grows at scale \(\theta R^{c-1}\), in contrast to the \(\theta/\log R\) scale below threshold.

**Critical window.** If instead \(\sqrt{\mu\theta}=L+\eta\), for any fixed \(\eta\in\mathbb R\) and sufficiently large \(R\), then
\[
Z_R\ \Longrightarrow\ \operatorname{Exp}(e^{-\eta}).
\]
Thus the mortality threshold is precisely \(\sqrt{\mu\theta}\sim\log(\lambda\theta)\); an order-one shift in its square root controls the effective arrival rate.

## Assumptions and scope

Every searcher moves as an independent one-dimensional Brownian motion with generator \(D\partial_x^2\), starting at positive distance \(d\), with absorption on first hitting zero. Each is independently killed at exponential rate \(\mu\ge0\). One particle starts at time zero. Additional independent searchers start at independent times of a Poisson process with rate \(\lambda>0\), all at the same distance and with fresh independent noises and mortality clocks. An arrival is registered only if the searcher hits before death. The observation time is measured from the initially present particle's injection. The limit holds for fixed \(c\) or fixed \(\eta\) as separately specified, not for arbitrary moving parameter sequences.

## Proof

**1. Individual arrival law and Poisson survival.** In dimensionless time, the first hitting time \(U\) of an immortal particle has density
\[
g(u)=\frac{e^{-1/(4u)}}{2\sqrt\pi\,u^{3/2}},\quad u>0.
\]
Write \(b=\mu\theta\). The defective distribution function of a successful mortal searcher is \(F_b(z)=\int_0^z e^{-bu}g(u)\,du\). The first particle survives without a registered arrival up to \(z\) with probability \(1-F_b(z)\). Poisson marking and independent displacement give the exact identity
\[
\mathbb P(Z_R>z)=[1-F_b(z)]e^{-RA_b(z)},\qquad
A_b(z)=\int_0^z(z-u)e^{-bu}g(u)\,du.
\tag{1}
\]
Equation (1) itself is known from earlier immigration-search work and is used only as input.

The elementary Lévy first-passage Laplace integral, or direct evaluation, yields
\[
q_b:=\int_0^\infty e^{-bu}g(u)\,du=e^{-\sqrt b}.
\tag{2}
\]
For \(b>0\), the time \(U_b\) conditional on eventual successful arrival has mean
\[
\mathbb E U_b=-\frac{d}{db}\log q_b=\frac{1}{2\sqrt b}.
\tag{3}
\]

**2. Sharp subcritical endpoint.** Take \(b=c^2L^2\), \(z=x/L\), and change variables \(u=y/L\) in (1). One obtains exactly
\[
RA_b(x/L)=\frac{e^L}{2\sqrt\pi\sqrt L}
\int_0^x(x-y)y^{-3/2}e^{-L\phi_c(y)}\,dy,\qquad
\phi_c(y)=\frac{1}{4y}+c^2y.
\tag{4}
\]
For \(0\le c<1\), the first positive solution of \(\phi_c(h)=1\) is \(h=h_c\), and \(\phi'_c(h_c)=-a_c<0\). In a fixed neighborhood of \(h_c\), \(\phi_c\) is strictly decreasing. The integrand in (4) is consequently localized at its *upper endpoint*, where the factor \(x-y\) vanishes to first order. Setting \(s=L(x-y)\), using Taylor's theorem and dominated convergence on bounded \(s\), and bounding the remaining integral by the strictly positive phase gap, yields uniformly for \(x=h_c+O(\log L/L)\)
\[
RA_b(x/L)=\frac{x^{-3/2}}{2\sqrt\pi[-\phi'_c(x)]^2}
L^{-5/2}e^{L(1-\phi_c(x))}[1+o(1)].
\tag{5}
\]
Indeed the endpoint integral contributes \(\int_0^\infty s e^{-[-\phi'_c(x)]s}\,ds=[-\phi'_c(x)]^{-2}\); the other powers of \(L\) follow from (4).

Take
\[
x_R(w)=h_c+\frac{\frac52\log L-\log C_c+w}{a_cL}.
\]
Then \(L[1-\phi_c(x_R(w))]=\frac52\log L-\log C_c+w+o(1)\), and (5) gives \(RA_b(x_R(w)/L)\to e^w\). Moreover \(0\le F_b(x_R(w)/L)\le\mathbb P(U\le x_R(w)/L)\to0\). Substitution into (1) proves the asserted reflected-Gumbel survival formula. Its tightness and the moving centering also imply \(LZ_R\to h_c\) in probability.

**3. Critical and supercritical regimes.** By (2), conditional on success, \(A_b(z)=q_b\mathbb E[(z-U_b)_+]\). The elementary inequality \(0\le z-(z-U)_+\le U\), combined with (3), gives
\[
0\le z-\frac{A_b(z)}{q_b}\le\frac{1}{2\sqrt b},\qquad
0\le F_b(z)\le q_b.
\tag{6}
\]
For fixed \(c\ge1\), \(q_b=R^{-c}\). Set \(z=tR^{c-1}\). Then \(RA_b(z)=R^{1-c}A_b(z)/q_b\to t\), because the error is bounded by \(R^{1-c}/(2cL)\to0\); also \(F_b(z)\le R^{-c}\to0\). Equation (1) therefore gives \(\mathbb P(R^{1-c}Z_R>t)\to e^{-t}\) for every \(t\ge0\).

For the separate critical-window scaling \(\sqrt b=L+\eta\), \(q_b=R^{-1}e^{-\eta}\) and \(\mathbb E U_b=1/[2(L+\eta)]\). With fixed \(z=t\), (6) gives \(RA_b(t)\to te^{-\eta}\) and \(F_b(t)\to0\), hence \(\mathbb P(Z_R>t)\to e^{-te^{-\eta}}\). This proves the complete claim.

## Verification

The standalone `verify_recruitment.py` uses deterministic quadrature and exact parameter identities. It checks the independent Fubini forms of the Poisson exponent, the killed-hitting Laplace transform, the conditional delay, the saddle normalization and subcritical numerical scaling, and the delay inequality in (6). It prints `PASS: 92 deterministic checks (not an infinite proof)` when run with Python, NumPy and SciPy. These finite checks corroborate but do not establish the asymptotic theorem; the proof above supplies its infinite-limit justification.

## Relationship to prior work

The elementary Brownian hitting density, the killed-walker Laplace transform, the marked Poisson survival identity (1), and fast-immigration extreme-value methods are established background. The main 2026 paper treats heterogeneous diffusion with recruitment and mortality at fixed parameters. The work by Linn and Kumar discusses stochastic redundancy under mortality; Giral-Barajas, Linn and Bressloff consider universal arrival-process statistics for nonconservative searches; Tung and Lawley rigorously address fast inhomogeneous immigration with a fixed passage-time law. Meerson and Redner study mortality with an initially present population of searchers, rather than sustained immigration. None of these established ingredients is claimed here as new. The assessment concerns the *explicit joint limit* \(\mu\theta\asymp[\log(\lambda\theta)]^2\), its threshold, the c-dependent subcritical reflected-Gumbel normalization, and its finite-width exponential crossover. Related general theorems could imply this result; no independent originality validation is claimed.

## Limitations

The model assumes exponential, independent mortality and Poisson immigration, Brownian first passages from one fixed distance, and perfect absorption. It does not cover interactions, moving targets, variable recruitment, nonexponential deaths, measurement noise, or general coupled parameter paths. The limit theorem is in distribution (and, below threshold, in probability); convergence of the mean arrival time has not been established. The heterogeneous-diffusion coordinate transformation motivates the model but is not needed for, nor asserted as an unconditional extension of, the theorem. Full texts of some relevant 2026 studies were not accessible, so an implicit broader-coverage originality risk remains.

## References

1. Gutiérrez, López, Singh, Fumeron, Henkel and Sandev, *Heterogeneous diffusion with recruitment and mortality*, arXiv:2610.08022v1 (October 6, 2026), https://arxiv.org/abs/2610.08022.
2. Linn and Kumar, *Dynamic redundancy and mortality in stochastic search*, arXiv:2601.07096 (2026), https://arxiv.org/abs/2601.07096.
3. Giral-Barajas, Linn and Bressloff, *Universality in the target arrival statistics of non-conservative search processes*, arXiv:2606.16025 (2026), https://arxiv.org/abs/2606.16025.
4. Tung and Lawley, *Passage times of fast inhomogeneous immigration processes*, arXiv:2508.14202 (2025), https://arxiv.org/abs/2508.14202.
5. Campos and Méndez, *Dynamic redundancy as a mechanism to optimize collective random searches*, Physical Review E 109, 064109 (2024), https://doi.org/10.1103/PhysRevE.109.064109.
6. Meerson and Redner, *Mortality, redundancy, and diversity in stochastic search*, Physical Review Letters 114, 198101 (2015), https://arxiv.org/abs/1502.06211.
