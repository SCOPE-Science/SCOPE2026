# Sharp two-moment endemic-incidence envelopes under a fixed realized vaccine-dose budget

## Finding

**Theorem.** Consider the homogeneous SIRVS renewal model described below. Let its basic reproduction number be \(\mathcal R>1\), its mean infectious duration \(a>0\), and its mean duration of perfect vaccine protection \(b>0\). Vaccination occurs at a constant hazard \(v\) for susceptible and naturally recovered individuals only, and the *actual stationary doses administered per capita per unit time* are constrained to equal \(f\), where
\[
0<f<\frac{1-1/\mathcal R}{b}.
\]
Suppose the naturally acquired perfect-immunity duration \(T\) belongs to the class
\[
\mathcal P=\{T:\ell\le T\le L,\quad \mathbb E T=m,\quad\operatorname{Var}(T)=s^2\},
\]
where \(0<\ell<m<L\) and \(0<s^2<(m-\ell)(L-m)\). The duration \(T\) may have any probability law on this interval, including atoms.

Define the two two-point probability laws
\[
\begin{split}
u_-&:\qquad \mathbb P(T=\ell)=\frac{s^2}{(m-\ell)^2+s^2},\quad
\mathbb P\!\left(T=m+\frac{s^2}{m-\ell}\right)=\frac{(m-\ell)^2}{(m-\ell)^2+s^2};\\
\nu_+&:\qquad \mathbb P\!\left(T=m-\frac{s^2}{L-m}\right)=\frac{(L-m)^2}{(L-m)^2+s^2},\quad
\mathbb P(T=L)=\frac{s^2}{(L-m)^2+s^2}.
\end{split}
\]
For any \(T\in\mathcal P\) there is a unique strictly positive endemic *stationary equilibrium* obeying the dose constraint. If \(v_T\) is its vaccination hazard, \(J_T\) is the rate of new infections per capita, and \(I_T\) is the infectious fraction, then
\[
 v_{\nu_+}\le v_T\le v_{\nu_-},\qquad
 J_{\nu_+}\le J_T\le J_{\nu_-},\qquad
 I_{\nu_+}\le I_T\le I_{\nu_-}.
\]
Every bound is **attained**. Because \(s^2>0\), equality in either end of the incidence interval holds only for the corresponding two-point law. Distinct general laws can give the same equilibrium inside the interval; the theorem does not claim injectivity.

The bound has explicit one-variable specifications. Put
\[
B_T(v)=\frac{1-\mathbb E[e^{-vT}]}{v}=\mathbb E\int_0^T e^{-vt}\,dt,
\qquad K=1-\frac1{\mathcal R}-fb>0.
\]
Find the unique positive root of
\[
 v\left[\frac1{\mathcal R}+\frac{K B_T(v)}{a+B_T(v)}\right]=f.
\]
Then
\[
J_T=\frac{K}{a+B_T(v_T)},\qquad I_T=aJ_T.
\]
Consequently both sharp endpoints can be calculated by solving this scalar equation for the displayed two-point laws, without identifying the full natural-immunity distribution.

## Assumptions and scope

The population mass is one, and all individuals mix homogeneously. Individuals pass from susceptible \(S\) to infectious \(I\), then to fully protected naturally recovered \(C\), then back to susceptible upon loss of natural immunity. Susceptible and naturally recovered individuals, but not infectious or currently vaccine-protected individuals, receive vaccinations at the same constant per-individual hazard \(v\). Vaccination instantaneously transfers them to a completely protected class \(V\), and vaccine protection ends after an independent nonnegative duration of mean \(b\). A naturally recovered individual is susceptible to this vaccination hazard during natural immunity; vaccination supersedes the remaining natural-immunity clock.

The infection kernel has finite mean infectious duration \(a\) and integrated mean secondary transmission potential \(\mathcal R\), so in stationary homogeneous mixing its force of infection is \(\mathcal R J\), where \(J\) is the incidence rate. The stationary renewal identities below require only these means, independent episode durations, and finite mean occupancies; they make no claim about global dynamical stability or transients. The support, mean, and variance constraints on \(T\) are nondegenerate as stated. Dirac masses are legitimate renewal-law limits, but if a particular PDE representation requires continuous densities only, the two-point envelopes are sharp suprema/infima in its weak closure rather than literally attained in that narrower class.

The constraint \(f\) is the *administered-dose flow*, not a fixed prescribed hazard and not the stock of vaccines. The hazard \(v_T\) is adjusted separately for each immunity-duration law to keep actual administered doses equal. A fixed-vaccination-hazard comparison does not substitute for this constraint.

## Proof

**1. Stationary balance and budget closure.** Suppose \(J>0\) is constant. Infection incidence equals \(J=S\mathcal RJ\), so \(S=1/\mathcal R\). Little's law / renewal-reward gives infectious occupancy \(I=aJ\). During each recovered period of duration \(T\), the independent vaccination hazard \(v\) competes with spontaneous loss of immunity; thus mean time in \(C\) is
\[
\mathbb E\min(T,E_v)=\mathbb E\int_0^T e^{-vt}\,dt=B_T(v),
\]
where \(E_v\) is independent exponential waiting time of rate \(v\). Hence \(C=J B_T(v)\). The actual administered-dose flow is \(f=v(S+C)\), so the vaccinated stock, regardless of the shape of its duration law, equals \(V=fb\). The total population constraint yields
\[
1=S+I+C+V=\frac1{\mathcal R}+J(a+B_T(v))+fb,
\]
which is precisely \(J=K/(a+B_T(v))\) with \(K>0\). Substituting into \(f=v(S+C)\) produces the displayed scalar budget equation.

**2. Uniqueness for each immunity law.** Define \(G_T(v)=v/\mathcal R+K v B_T(v)/(a+B_T(v))\). For \(v>0\), differentiation gives the exact expression
\[
G_T'(v)=\frac1{\mathcal R}+K\frac{B_T(v)^2+a\,\mathbb E[T e^{-vT}]}{(a+B_T(v))^2}>0,
\]
since \(B_T(v)+vB_T'(v)=\mathbb E[T e^{-vT}]\). Also \(G_T(0+)=0\), and \(G_T(v)\ge v/\mathcal R\to\infty\). There is exactly one root of \(G_T(v)=f\). Because \(K>0\), this root is strictly less than \(\mathcal R f\). It gives positive \(J\), nonnegative class occupancies and consistent balance, establishing exactly one positive *stationary* endemic equilibrium in the specified mass-action renewal setting.

**3. Sharp two-moment Laplace envelopes.** The assumptions on \(s^2\) ensure \(\ell<u:=m+s^2/(m-\ell)<L\) and \(\ell<d:=m-s^2/(L-m)<L\). Direct substitution shows that \(\nu_-\) and \(\nu_+\) both have mean \(m\) and variance \(s^2\).

Fix \(v>0\) and write \(g(t)=e^{-vt}\), so \(g'''(t)=-v^3e^{-vt}<0\). Let \(Q_-\) be the quadratic Hermite interpolant matching \(g(\ell)\), \(g(u)\), and \(g'(u)\). The Hermite remainder on \([\ell,L]\) is
\[
g(t)-Q_-(t)=\frac{g'''(\xi_t)}{6}(t-\ell)(t-u)^2\le0.
\]
Let \(Q_+\) match \(g(d)\), \(g'(d)\), and \(g(L)\). Its remainder is
\[
g(t)-Q_+(t)=\frac{g'''(\eta_t)}{6}(t-d)^2(t-L)\ge0.
\]
These formulas include the interpolation nodes by continuity. Because expectations of any quadratic are determined solely by \(\mathbb ET=m\) and \(\mathbb E T^2=m^2+s^2\), and the quadratic bounds touch the corresponding two-point laws, they imply
\[
\mathbb E_{\nu_+}e^{-vT}\le\mathbb E_Te^{-vT}\le\mathbb E_{\nu_-}e^{-vT},
\]
with equality precisely at the relevant two-point law. Equivalently,
\[
 B_{\nu_-}(v)\le B_T(v)\le B_{\nu_+}(v)
\]
for all \(v>0\); thus one pair of laws simultaneously realizes the envelope at **every** hazard, not merely at a selected \(v\).

**4. Propagating bounds through the endogenous dose constraint.** For fixed \(v\), \(G_T(v)\) is strictly increasing as a function of \(B_T(v)\). The global inequalities in Step 3 therefore imply \(G_{\nu_-}(v)\le G_T(v)\le G_{\nu_+}(v)\). Since each of these functions is strictly increasing in \(v\), their roots obey
\[
v_{\nu_+}\le v_T\le v_{\nu_-}.
\]
Furthermore, each \(B_T(v)\) decreases strictly in \(v>0\) because \(T\ge\ell>0\). Therefore
\[
B_{\nu_-}(v_{\nu_-})\le B_T(v_T)\le B_{\nu_+}(v_{\nu_+}).
\]
Using the formula for \(J\), and then \(I=aJ\), reverses this inequality and proves the claimed incidence/prevalence bounds. Equality at an endpoint forces equality in the strict Hermite bound at a positive hazard, and hence the corresponding two-point law. The proof relies on analytical inequalities for all admissible \(T\), not on finite experiments.

## Verification

Run `python3 CHECK.py` with Python 3.9 or later; it uses only the standard library. It tests exact-rational moments and extremal weights, both budget identities and mass conservation, the independent fixed-hazard formula in Yang–Saldaña–Scoglio, the three-law example, and a broad parameter sweep. The script prints the assertion count and numerical endpoint solutions. These checks are finite corroboration and are not a proof of the all-law bounds.

For an explicit nondegenerate example choose \(\mathcal R=3\), \(a=1/2\), \(b=1\), \(f=2/5\), \((\ell,m,L)=(1,3,7)\), and \(s^2=4\). Then \(K=4/15\), \(\nu_-=\tfrac12\delta_1+\tfrac12\delta_5\) and \(\nu_+=\tfrac45\delta_2+\tfrac15\delta_7\). An admissible intermediate law is \(\tfrac13\delta_1+\tfrac12\delta_3+\tfrac16\delta_7\). Their respective incidence rates are approximately \(0.1813468073\), \(0.1750958197\), and \(0.1700143310\). All receive the same actual dose flow \(2/5\). Dividing or multiplying by the mean infectious duration is **not** implicit: the infectious *prevalence* is explicitly \(I=aJ\), one half the above numbers.

## Relationship to prior work

Yang, Saldaña and Scoglio (arXiv:2303.15326, first submitted March 27, 2023) develop the non-Markovian SIRVS system, give its fixed-vaccination-hazard stationary formula in terms of Laplace transforms, and discuss vaccination thresholds. This theorem uses that model, does **not** claim discovery of its renewal equilibrium or transform dependence, and makes a different constraint: adjust the hazard to keep the **actual administered-dose flow fixed** while optimizing over all immunity-duration laws with a fixed support, mean, and variance. It produces simultaneous sharp extremal laws and a unique scalar budget calibration.

El Khalifi and Britton (arXiv:2311.00592, 2023) study individual heterogeneity of gradual immunity waning and vaccination needed for herd immunity; El Khalifi and Britton (arXiv:2211.09062, 2022) compare gradual and all-or-nothing immunity. Neither directly states the sharp two-moment fixed-administered-dose **endemic-incidence** envelope in this model. General classical moment-problem/Hermite interpolation results underlie the endpoint proof and are **not** claimed as novel mathematical techniques. Previous mathematical studies have established that immunity heterogeneity can affect endemic prevalence, so the general effect is **not** a novelty claim here.

## Limitations

No vaccination-stockpile dynamics, susceptible heterogeneity, contact-network structure, age-dependent infectiousness, or nonzero vaccine breakthrough is considered. Vaccine protection is perfect, naturally recovered individuals remain eligible for vaccination, and the administered-dose flow is constant at equilibrium. The support/mean/variance assumptions are essential for the stated sharp two-point laws. The result characterizes stationary endemic incidence only; it does not prove dynamic attainability or stability of those equilibria. The two-point maximizers are outside strictly absolutely continuous duration-law subclasses (whose bounds may only be approached). Independent scientific validation and exhaustive publication-priority review are not claimed.

## References

1. Yang, Saldaña and Scoglio, *Generalized epidemic model incorporating non-Markovian infection processes and waning immunity*, arXiv:2303.15326 (first public arXiv submission 2023-03-27), https://arxiv.org/abs/2303.15326 .
2. M. El Khalifi and T. Britton, *SIRS epidemics with individual heterogeneity of immunity waning*, arXiv:2311.00592 (2023-11-01), https://arxiv.org/abs/2311.00592 .
3. M. El Khalifi and T. Britton, *Extending SIRS epidemics to allow for gradual waning of immunity*, arXiv:2211.09062 (2022-11-16), https://arxiv.org/abs/2211.09062 .
4. Standard Hermite interpolation remainder and classical bounded two-moment extremal-measure methods (background tools, not novel results claimed here).
