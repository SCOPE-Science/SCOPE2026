# Reciprocal latency–recovery duality and the unique SEIR overshoot minimum

## Finding

For every basic reproduction ratio \(\rho>1\), the closed homogeneous susceptible–exposed–infectious–removed (SEIR) model has a canonical infinitesimal-seed outbreak. Write \(\lambda=\sigma/\gamma>0\) for the progression-to-recovery rate ratio. Let \(s_{\mathrm{peak}}(\lambda)\) be the susceptible fraction at the unique global maximum of **infectious** prevalence, and let \(s_\infty\) be its final susceptible fraction. Then:

1. **Exact reciprocal duality:** \(s_{\mathrm{peak}}(\lambda)=s_{\mathrm{peak}}(1/\lambda)\). In fact, the entire susceptible–removed phase curve is conjugate by an explicit positive change of infected compartments and a constant rescaling of time.
2. **Strict extremum:** \(s_{\mathrm{peak}}(\lambda)\) strictly decreases as \(\lambda\) rises from \(0\) to \(1\), strictly increases from \(1\) to infinity, and satisfies \(s_\infty<s_{\mathrm{peak}}(\lambda)<1/\rho\). Consequently, the post-infectious-peak attack fraction \(\mathcal O_\rho(\lambda)=s_{\mathrm{peak}}(\lambda)-s_\infty\) has its **unique strict minimum at \(\lambda=1\)**.
3. **Sharp endpoints:** Both \(\lambda\downarrow0\) and \(\lambda\uparrow\infty\) give \(\mathcal O_\rho(\lambda)\to 1/\rho-s_\infty\), the classical SIR overshoot. Hence at every finite \(\lambda\), the infectious-peak overshoot lies strictly below the sharp classical bound \(0.2984256075\ldots\); its supremum over \(\rho>1\) and \(\lambda>0\) equals that bound but is not attained at finite \(\lambda\). The classical constant is established in the cited work of Nguyen et al.; its value itself is not claimed as new.

The exact reciprocal symmetry and strict intermediate-rate minimum are the findings. A representative value is \(\rho=2\): the post-peak fraction is approximately \(0.26074913\) at \(\lambda=1\), but \(0.28422712\) at each of \(\lambda=0.1\) and \(\lambda=10\); the limiting SIR fraction is approximately \(0.29681213\).

## Assumptions and scope

Normalize population to one and time by the positive recovery rate \(\gamma\). For \(\rho=\beta/\gamma>1\) and \(\lambda=\sigma/\gamma>0\), the no-demography, no-waning, homogeneous-mixing SEIR equations are
\[
\dot S=-\rho SI,\quad \dot E=\rho SI-\lambda E,\quad
\dot I=\lambda E-I,\quad \dot Z=I,
\]
where \(Z\) denotes recovered or removed mass and \(S+E+I+Z=1\). The canonical outbreak is the positive branch of the one-dimensional unstable manifold of the fully susceptible disease-free state \((1,0,0,0)\), characterized by \((S,E,I,Z)\to(1,0,0,0)\) as \(t\to-\infty\). It is unique up to translation of time. This is the rigorous vanishing-seed limit along the initially growing linearized mode, rather than an assertion about every finite initial allocation of exposed and infectious individuals.

A **peak** refers to the maximum of \(I\), not to the maximum of \(E+I\). An **overshoot** refers to new infections after that infectious peak, namely \(s_{\mathrm{peak}}-s_\infty\). The quantity \(\lambda\) varies with \(\rho\) held fixed; the ratios of initial exposed and infectious masses are naturally selected by the canonical outbreak condition.

## Proof

**Invariant and epidemic phase coordinate.** Set \(u=-\log S\). Along the positive outbreak, \(\dot u=\rho I>0\) and \(dZ/du=1/\rho\). Since \(Z\to0\) and \(S\to1\) as \(t\to-\infty\), the exact invariant reads
\[
J(u):=E+I=1-e^{-u}-\frac{u}{\rho}.
\]
Its second zero \(u_\infty>\log\rho\) satisfies \(e^{-u_\infty}=s_\infty\), with \(\log s_\infty=-\rho(1-s_\infty)\). The other zero is \(u=0\). On \((0,u_\infty)\), \(J>0\); it strictly increases before \(u_h=\log\rho\) and strictly decreases afterward. Indeed \(\dot J=I(\rho S-1)\).

**Exact one-parameter reduction.** Define
\[
V(u)=\frac{1+\lambda}{\lambda}I(u),\qquad
\kappa(\lambda)=\frac{(1+\lambda)^2}{\lambda}
=2+\lambda+\lambda^{-1}.
\]
Substituting \(I=\lambda V/(1+\lambda)\) into \(\dot I=\lambda J-(1+\lambda)I\) and dividing by \(\dot u=\rho I\) gives the exact scalar equation
\[
\boxed{\rho V(u)V'(u)=\kappa\bigl(J(u)-V(u)\bigr).}
\]
At the disease-free endpoint, \(J(u)=(1-1/\rho)u+O(u^2)\), and the growing outbreak solution has
\[
V(u)=b_\kappa u+O(u^2),\quad
\rho b_\kappa^2+\kappa b_\kappa
-\kappa(1-1/\rho)=0,\quad b_\kappa>0.
\]
This condition selects a unique positive solution. One direct uniqueness proof is to put \(V=uw\): then \(u w'=\kappa[J(u)/u-w]/(\rho w)-w\). At \(u=0\) its positive equilibrium is \(b_\kappa\), and the derivative in \(w\) there is strictly negative. Variation of constants after setting \(u=e^\tau\) supplies a unique bounded solution tending to \(b_\kappa\) as \(\tau\to-\infty\). Thus the entire phase curve depends on \(\lambda\) only through \(\kappa\), and \(\kappa(\lambda)=\kappa(1/\lambda)\).

There is also an explicit **full-system conjugacy**: if \(\lambda\ge1\) and \((S,E,I,Z)(t)\) is any nonnegative solution at ratio \(\lambda\), define \(s=\lambda t\) and
\[
\widehat S(s)=S(t),\quad \widehat I(s)=I(t)/\lambda,\quad
\widehat E(s)=E(t)+(1-1/\lambda)I(t),\quad
\widehat Z(s)=Z(t).
\]
Direct differentiation shows these variables obey the same SEIR equations at \(\widehat\lambda=1/\lambda\) and unchanged \(\rho\); all transformed compartments remain nonnegative. The transformation maps the canonical positive outbreak to the canonical positive outbreak. Consequently, the susceptible and removed curves coincide after time rescaling, and so do susceptible coordinates of the infectious peaks.

**Unique peak.** The derivative \(\dot I\) obeys
\[
\frac{d}{dt}(\dot I)+(\lambda+1)\dot I=\lambda\dot J.
\]
On the canonical outbreak, \(\dot I\to0\) as \(t\to-\infty\), so
\[
\dot I(t)=\lambda\int_{-\infty}^{t}e^{-(\lambda+1)(t-s)}\dot J(s)\,ds.
\]
It follows that \(\dot I>0\) before \(J\) reaches its maximum. After that point \(e^{(\lambda+1)t}\dot I(t)\) strictly decreases, and because \(I(t)\to0\), it must cross zero exactly once. Thus the infectious maximum occurs at a unique coordinate \(u_p(\kappa)>u_h\), precisely when \(V(u_p)=J(u_p)\). On \((0,u_p)\) one has \(0<V<J\).

**Strict ordering in \(\kappa\).** The positive slope \(b_\kappa\) is strictly increasing in \(\kappa\): the defining equation rearranges to \(\kappa=\rho b_\kappa^2/[(1-1/\rho)-b_\kappa]\), a strictly increasing function of \(b_\kappa\in(0,1-1/\rho)\). Fix \(\kappa_2>\kappa_1\). Initially \(V_2>V_1\). Until either curve reaches \(J\), the two curves remain strictly ordered: at a hypothetical first contact \(V_1=V_2<J\), the scalar equation gives \(V_2'-V_1'=(\kappa_2-\kappa_1)(J-V_1)/(\rho V_1)>0\), preventing a first loss of the positive ordering. Hence the larger-\(\kappa\) solution must reach \(J\) strictly earlier: \(u_p(\kappa_2)<u_p(\kappa_1)\). As \(\kappa\) is minimized uniquely at \(\lambda=1\), the asserted strict extremum and reciprocal invariance follow.

**Endpoint limit and sharp bound.** For \(u\le u_h\), write \(W=J-V>0\). Since \(V\le J<1\),
\[
W'=J'-\frac{\kappa}{\rho V}W
\le \sup_{[0,u_h]}J'-\frac\kappa\rho W.
\]
For each fixed \(u>0\), the resulting comparison estimate gives \(W(u)=O(\kappa^{-1})\) as \(\kappa\to\infty\). Thus \(V(u_h)\to J(u_h)\). At any fixed \(u>u_h\), \(J(u)<J(u_h)\), whereas \(V\) increases until the infectious peak. Hence \(u_p(\kappa)\to u_h\). Both endpoint limits of \(\lambda\) make \(\kappa\to\infty\), so \(s_{\mathrm{peak}}\to1/\rho\). At every finite \(\lambda\), \(u_p>u_h\), giving strict inequality below the SIR overshoot. The sharp SIR global maximum follows by expressing its overshoot as \((1-s_\infty)/[-\log s_\infty]-s_\infty\), differentiating, and solving \(e^L=1+L+L^2\) for the unique positive \(L=-\log s_\infty\); the resulting supremum is \(0.298425607525\ldots\).

## Verification

`verify.py` checks the complete four-compartment conjugacy and phase-coordinate reduction symbolically. It also solves the original nonlinear system for three reproduction ratios and five progression-rate ratios, comparing reciprocal pairs and checking the strict extremum; all checks pass. For \(\rho=2\), the computed infectious-peak susceptible fractions are approximately \(0.487414989\) at \(\lambda=0.1\) and \(\lambda=10\), and \(0.463937004\) at \(\lambda=1\). The finite-seed numerical trials use a growing-eigenmode initial allocation with total infection \(10^{-8}\); finite testing is not the proof for infinitely many parameters.

Run `python3 verify.py` with `sympy` and `scipy` installed. The proof above is independent of the numerical runs.

## Relationship to prior work

Nguyen, Freedman, Ozbay, and Levin (arXiv:2303.01650, first made public March 3, 2023; later *Journal of the Royal Society Interface* 20, 20230322) prove the universal SIR overshoot cap and discuss vaccination and contact heterogeneity. Their cap and final-size equation are adopted, not claimed as discoveries here. Their original preprint has no SEIR or latency analysis in the inspected main text.

Heng and Althaus (*Scientific Reports* 10, 2020, DOI:10.1038/s41598-020-76563-8) analyze the SEIR equations and obtain **approximately** universal time-scaled epidemic shapes by dropping a third derivative in an exact equation. They acknowledge that this approximation does not give an exact infectious-peak coordinate. Their exact equations are compatible with, but do not state, the reciprocal parameter conjugacy or its strict overshoot extremum. Dobie, Demirci, Bilge, and Ahmetolan (arXiv:1909.11317) examine numerical peak timing and stage delays in SEIR variants; their analyzed peak comparisons do not give the reciprocal phase-curve result.

The conservation law, final-size relation, and standard SEIR equations are classical. The assessed contribution is the **exact reciprocal conjugacy and its strict, globally quantified nonmonotonic infectious-peak overshoot**, not those prerequisites or the numerical constant independently established for SIR.

## Limitations

Results apply to the deterministic homogeneous-mixing SEIR process with exponentially distributed stage durations, permanent removal, no vaccination/demography, and the canonical vanishing-seed outbreak. For arbitrary finite initially infected populations with a fixed and unmatched exposed/infectious split, reciprocity and the unique-minimum statement need not hold; the full-system conjugacy explicitly transforms the initial split. The theorem does not apply without modification to infection-age kernels, multistage latency distributions, heterogeneous networks, finite stochastic populations, or alternative peak observables. It concerns the number infected **after infectious prevalence peaks**, not the fraction infected after the peak of total active infection \(E+I\).

## References

1. M. M. Nguyen, A. S. Freedman, S. A. Ozbay, S. A. Levin. *Fundamental Bound on Epidemic Overshoot in the SIR Model*. arXiv:2303.01650 (initial version March 3, 2023); doi:10.1098/rsif.2023.0322 (2023).
2. K. Heng, C. L. Althaus. *The approximately universal shapes of epidemic curves in the Susceptible-Exposed-Infectious-Recovered (SEIR) model*. *Scientific Reports* 10 (2020). doi:10.1038/s41598-020-76563-8; arXiv:2011.00378.
3. A. Peker Dobie, A. Demirci, A. H. Bilge, S. Ahmetolan. *On the time shift phenomena in epidemic models*. arXiv:1909.11317 (September 25, 2019).
