# An exponentially delayed vaccine-susceptibility crossover at the critical reinfection threshold

## Finding

In a deterministic leaky-immunity susceptible–infectious–recovered–infectious (SIRI) model with two pre-vaccination strata, the exact reinfection threshold admits an explicit scalar reduction. The resulting infected fraction has the universal critical tail \(tJ(t)\to1\), but the additive constant in cumulative reinfections changes discontinuously when the susceptibility of never-infected vaccinees moves away from the susceptibility of recovered individuals. The transition occurs on an **exponentially large** time scale and has an exact continuous crossover profile.

More precisely, take an infection-induced relative susceptibility \(\phi\in(0,1)\), a vaccinee susceptibility \(\theta\in[\phi,1]\), and transmission number \(R_0=1/\phi\). Initially there are \(s>0\) unvaccinated never-infected persons, \(v>0\) vaccinated never-infected persons and \(i>0\) infectious persons in normalized proportions, with \(s+v+i=1\) and no initially recovered persons. Let \(Q_{\theta}(t)\) denote the cumulative number of postinitial reinfection events per capita by time \(t\). Then:

\[
\lim_{t\to\infty}tJ_{\theta}(t)=1,
\qquad
\lim_{t\to\infty}\bigl(Q_{\theta}(t)-\log t\bigr)=
\begin{cases}
\log(1-v)-1,&\theta=\phi,\\
-1,&\theta>\phi.
\end{cases}
\]

The noncommuting limits have a sharp resolution. For \(z>0\) and \(\varepsilon\downarrow0\), put \(\theta_{\varepsilon}=\phi(1+\varepsilon)\) and \(t_{\varepsilon}=\exp(z/\varepsilon)\). For all sufficiently small \(\varepsilon>0\), \(\theta_{\varepsilon}\le1\), and

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\bigl[Q_{\theta_{\varepsilon}}(t_{\varepsilon})-
\log t_{\varepsilon}\bigr]=
\log(1-ve^{-z})-1.
}
\]

Thus a susceptibility difference \(\theta-\phi\) of arbitrarily small positive size can shift the long-time reinfection offset, but a fixed nontrivial portion of that shift is delayed until times exponential in \(\phi/(\theta-\phi)\). The statement is an exact mathematical limit, not an inference from observed counts.

## Assumptions and scope

Let \(S_U,S_V\) be the proportions never infected in the unvaccinated and vaccinated strata, \(R_U,R_V\) the proportions recovered from at least one infection, and \(I_U,I_V\) their infectious proportions. This notation is equivalent to the previously infected susceptible compartments in the source SIRI model. Let \(J=I_U+I_V\) and \(\lambda=R_0J\). Time is scaled to give unit recovery rate. The complete equations are

\[
\begin{aligned}
\dot S_U&=-\lambda S_U,
&\dot S_V&=-\theta\lambda S_V,\\
\dot R_U&=I_U-\phi\lambda R_U,
&\dot R_V&=I_V-\phi\lambda R_V,\\
\dot I_U&=\lambda(S_U+\phi R_U)-I_U,
&\dot I_V&=\lambda(\theta S_V+\phi R_V)-I_V.
\end{aligned}
\]

Assume \(S_U(0)=s>0\), \(S_V(0)=v>0\), \(I_U(0),I_V(0)\ge0\), \(I_U(0)+I_V(0)=i>0\), and \(R_U(0)=R_V(0)=0\), with \(s+v+i=1\). These equations preserve the nonnegative unit simplex and keep \(J(t)>0\) for finite \(t\). Unless expressly noted, limits are for fixed \(s,v,i,\phi\), with \(\theta\) as stated. We count only infection *events after time zero*, classifying an infection as a reinfection exactly when it originates from \(R_U\) or \(R_V\). The initially infected fraction is not included as a postinitial event.

## Proof

**Exact reduction.** Define accumulated infection pressure \(H(t)=\int_0^t\lambda(u)\,du\), and set

\[
Z(t)=e^{\phi H(t)},\quad
\alpha=\frac{1-\phi}{\phi}>0,\quad
\varepsilon=\frac{\theta-\phi}{\phi}\ge0.
\]

The susceptible equations integrate to

\[
S_U(t)=sZ(t)^{-1/\phi},\qquad S_V(t)=vZ(t)^{-\theta/\phi}.
\]

Conservation of population mass yields \(R_U+R_V=1-S_U-S_V-J\). At \(R_0\phi=1\), summing the infectious equations therefore gives

\[
\dot J=J\bigl(\alpha S_U+\varepsilon S_V-J\bigr).
\]

Since \(\dot Z/Z=\phi\lambda=J\), differentiation gives

\[
\ddot Z=\dot Z\left[\alpha sZ^{-1/\phi}+\varepsilon vZ^{-\theta/\phi}\right].
\]

The solution has \(\dot Z(0)=i\) and \(\dot Z>0\), so dividing by \(\dot Z\) and integrating with respect to \(Z\), including the case \(\varepsilon=0\), yields the exact initial-value problem

\[
\boxed{\dot Z=1-sZ^{-\alpha}-vZ^{-\varepsilon},\qquad Z(0)=1,\qquad J=\dot Z/Z.}
\tag{1}
\]

Here \(\alpha+1=1/\phi\) and \(\varepsilon+1=\theta/\phi\). The right-hand side of (1) is at least \(i\) and at most \(1\) whenever \(Z\ge1\). Consequently

\[
1+it\le Z(t)\le1+t\quad(t\ge0).
\tag{2}
\]

In particular \(Z\to\infty\). For fixed \(\theta=\phi\), equation (1) gives \(\dot Z\to1-v\); for any fixed \(\theta>\phi\), it gives \(\dot Z\to1\). Integration implies

\[
\lim_{t\to\infty}\frac{Z(t)}t=
\begin{cases}1-v,&\theta=\phi,\\1,&\theta>\phi.\end{cases}
\quad\text{and}\quad
\lim_{t\to\infty}tJ(t)=1.
\tag{3}
\]

**Exact reinfection identity.** Write \(E(t)\) for all postinitial infection events and \(P(t)\) for postinitial primary infections. Since \(\dot J=\dot E-J\), integrating and using \(\int_0^tJ(u)\,du=\log Z(t)\) gives

\[
E(t)=\log Z(t)+J(t)-i.
\]

The primary count is the decrease of the never-infected compartments:

\[
P(t)=s(1-Z^{-1/\phi})+v(1-Z^{-\theta/\phi}).
\]

Subtracting and using \(s+v+i=1\) proves, exactly for every \(t\ge0\),

\[
\boxed{Q(t)=\log Z(t)+J(t)-1+sZ(t)^{-1/\phi}+vZ(t)^{-\theta/\phi}.}
\tag{4}
\]

In (4), \(J(t)\to0\) and the last two terms vanish as \(t\to\infty\). Combining (3) and (4) establishes the two distinct fixed-parameter offsets in the theorem.

**Singular logarithmic-time crossover.** Fix \(z>0\). For \(\theta_{\varepsilon}=\phi(1+\varepsilon)\) let \(Z_{\varepsilon}\) solve (1) and set \(T_{\varepsilon}=e^{z/\varepsilon}\). From (2), for each fixed \(r\in(0,1]\),

\[
\varepsilon\log Z_{\varepsilon}(rT_{\varepsilon})\to z,
\qquad
Z_{\varepsilon}(rT_{\varepsilon})^{-\alpha}\to0,
\qquad
Z_{\varepsilon}(rT_{\varepsilon})^{-\varepsilon}\to e^{-z}.
\]

Indeed the lower and upper bounds in (2), after applying \(\varepsilon\log\), have the common limit \(z\); here \(i,s,v,\alpha\) do not vary with \(\varepsilon\). Integrating (1), rescaling the integral by \(r=u/T_{\varepsilon}\), and using bounded convergence (each integrand lies in \([0,1]\)) gives

\[
\begin{aligned}
\frac{Z_{\varepsilon}(T_{\varepsilon})}{T_{\varepsilon}}
&=\frac1{T_{\varepsilon}}+
\int_0^1 \left[1-sZ_{\varepsilon}(rT_{\varepsilon})^{-\alpha}
-vZ_{\varepsilon}(rT_{\varepsilon})^{-\varepsilon}\right]dr\\
&\longrightarrow1-ve^{-z}.
\end{aligned}
\tag{5}
\]

Because \(1-ve^{-z}>0\), equation (5) gives \(\log Z_{\varepsilon}(T_{\varepsilon})-\log T_{\varepsilon}\to\log(1-ve^{-z})\). The three nonlogarithmic terms of (4) converge respectively to \(0,-1,0\), since (2) also forces \(Z_{\varepsilon}(T_{\varepsilon})\to\infty\) and \(J_{\varepsilon}\le1/Z_{\varepsilon}\). This proves the claimed crossover. There is no assertion that \(z=0\) can be substituted before the large-time limit: the profile's \(z\downarrow0\) endpoint is obtained by continuity afterward.

## Verification

`verify.py` is a standalone Python 3 program using only the standard library. It checks the reduced identity against independently numerically integrated six-compartment equations for \(\phi=1/2\), \(s=1/2\), \(v=2/5\), \(i=1/10\), at \(\theta=1/2\) and \(\theta=13/20\). It checks conservation, integrated pressure, infectious prevalence, primary infections, and cumulative reinfections, and separately integrates the scalar equation using a logarithmic time change for \(\varepsilon=1/20,1/40,1/80\), at \(z=1\). The final finite-difference discrepancy from the limiting profile decreases below \(0.003\). These finite tests are reproducibility checks only; equations (1)–(5), not numerical simulation, prove the unrestricted claim.

Run with `python3 verify.py` from the directory containing that file.

## Relationship to prior work

Gutierrez and Gog, *Final-Size Solutions for SIRI Models with Vaccination* (first public medRxiv version on 2025-09-14; open-access journal publication 2026), formulate the same leaky-vaccination SIRI equations and establish implicit epidemic final-size results in their Section 4 for the **strictly subcritical reinfection condition** \(R_0\phi<1\). Their equations (23)–(35) develop the relationship between infection pressure and susceptible depletion; the paper explicitly restricts subsequent leaky-model final-size analysis to \(R_0\phi<1\) and does not derive the critical-time reinforcement or vaccine-equality crossover of (5). Those earlier equations and the threshold distinction are not claimed as new.

Katriel (2010) establishes fundamental threshold and extinction conclusions for a simpler partial-immunity reinfection model without a distinct never-infected vaccinated stratum. His critical-case vanishing-prevalence conclusion and earlier threshold are not claimed as new. The present statement concerns the additional vaccine susceptibility and its singular logarithmic-time parameter crossover. Gomes, White and Medley (2004, 2005) study reinfection and vaccination threshold mechanisms in models with materially different immunity and demographic assumptions. Generic critical \(1/t\) relaxation is established in nonlinear dynamics; the focal contribution here is the exact two-stratum reinfection-offset profile and its exponentially delayed interpolation. No claim of exhaustive uniqueness relative to unindexed literature is made.

## Limitations

The result assumes a deterministic, closed, well-mixed population of fixed size; homogeneous infectiousness and recovery rates; lifelong but leaky partial immune protection; no waning of immunity, births, deaths, heterogeneous contacts, or change in transmissibility of previously infected people. It applies only at the exact threshold \(R_0\phi=1\), with fixed positive initial fractions \(s,v,i\), zero initially recovered fractions, and \(\phi\le\theta\le1\). The limit \(\varepsilon\to0\) keeps \(s,v,i,\phi\) fixed. In a finite stochastic population, extinction precedes arbitrarily late exponential-time asymptotics; the theorem does not predict observable reinfection counts on those time scales. The proof neither treats \(R_0\phi\ne1\) nor supplies a uniform error rate for (5).

## References

1. M. A. Gutierrez and J. R. Gog, “Final-size solutions for SIRI models with vaccination,” medRxiv, posted 2025-09-14, DOI: `10.1101/2025.09.12.25335631`, version 1. https://www.medrxiv.org/content/10.1101/2025.09.12.25335631v1.full
2. M. A. Gutierrez and J. R. Gog, “Final-Size Solutions for SIRI Models with Vaccination,” *Bulletin of Mathematical Biology* **88** (2026), article 64, DOI: `10.1007/s11538-026-01610-w`, Section 4. https://link.springer.com/article/10.1007/s11538-026-01610-w
3. G. Katriel, “Epidemics with partial immunity to reinfection,” *Mathematical Biosciences* (2010), DOI: `10.1016/j.mbs.2010.09.003`.
4. M. G. M. Gomes, L. J. White and G. F. Medley, “Infection, reinfection, and vaccination under suboptimal immune protection: epidemiological perspectives,” *Journal of Theoretical Biology* (2004), DOI: `10.1016/j.jtbi.2004.02.015`.
5. M. G. M. Gomes, L. J. White and G. F. Medley, “The reinfection threshold,” *Journal of Theoretical Biology* (2005), DOI: `10.1016/j.jtbi.2005.03.001`.
