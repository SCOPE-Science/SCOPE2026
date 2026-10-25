# A universal final-size sandwich for epidemics with fluctuating individual susceptibility

## Finding
For a closed susceptible–infectious–removed epidemic with exogenous individual risk fluctuations, write \(S_0>0\) and \(I_0>0\) for the initially susceptible and infectious masses, and let \(\gamma>0\) be the recovery rate. Each susceptible has a bounded nonnegative infection-risk process \(b(t)\), whose one-time distribution \(\nu\) is the same for every \(t\ge0\). All susceptible risk paths are identically distributed, independent of their infection events and of the deterministic force of infection. Neither independence through time nor a Markov assumption is needed. Let \(\bar b=\int b\,d\nu\).

Compare three SIR systems with identical initial masses and recovery rates: *frozen risk*, where each person retains a fixed draw \(b\sim\nu\); *fluctuating risk*, where each person follows the stationary-marginal path process; and *homogeneous risk*, where everyone has the constant risk \(\bar b\).

If \(Z\) denotes the final number ever infected, **including the initially infectious mass**, then
\[
\boxed{Z_{\mathrm{frozen}}\le Z_{\mathrm{fluctuating}}\le Z_{\mathrm{homogeneous}}.}
\]
The inequalities hold without assumptions on the temporal correlation, reversibility, switching intensity, or regularity of risk paths beyond bounded measurability and stationary one-time marginals. This isolates the effect of *persistence versus turnover* of the same individual risk distribution.

## Assumptions and scope
Let \(b:[0,\infty)\times\Omega\to[0,B]\) be jointly measurable on a probability space, with \(B<\infty\), such that \(b(t)\) has the same probability law \(\nu\) for every deterministic time \(t\ge0\). Take \(S_0,I_0,\gamma>0\) and optionally \(R_0\ge0\), with total initial mass normalized or not. The deterministic mean-field model is
\[
S(t)=S_0\mathbb E\!\left[\exp\!\left(-\int_0^t b(u)I(u)\,du\right)\right],\qquad
I'(t)=-S'(t)-\gamma I(t),\quad I(0)=I_0.
\]
This is the susceptibility-path representation of an SIR system in which risk behavior evolves exogenously in the susceptible population; infection does *not* feed back into the risk process. Boundedness ensures a unique nonnegative solution via the associated Volterra equation (or finite-state ODE in the Markov examples). The total infected mass is \(Z=I_0+S_0-S_\infty\). Susceptibles cannot be reinfected, and infectiousness and recovery are homogeneous.

For a nonnegative measurable \(q\) on \([0,\infty)\), let \(z_q\) denote the unique positive solution of \(\gamma z=I_0+S_0-S_0q(z)\), when \(q(z)\) is either \(q_\nu(z)=\mathbb E_\nu[e^{-bz}]\) or \(q_{\mathrm{hom}}(z)=e^{-\bar b z}\). Set \(Z_q=\gamma z_q\). These exactly describe the frozen and homogeneous models.

## Proof
**1. Extinction and mass balance.** The mass \(S(t)\) is decreasing, \(S'(t)=-S_0I(t)\mathbb E[b(t)e^{-\int_0^t b(u)I(u)du}]\), and the scalar infectious equation preserves positivity. Also \(R'(t)=\gamma I(t)\); hence \(z=\int_0^\infty I(t)dt\le(S_0+I_0)/\gamma\). Since \(I\) has bounded derivative and is nonnegative and integrable, \(I(t)\to0\), giving
\[
\gamma z=I_0+S_0-S_\infty.
\]
Because \(I_0>0\), \(z>0\).

**2. Conditional Jensen for temporal risk.** Let \(U\) be independent of the risk process with density \(w(t)=I(t)/z\) on \([0,\infty)\). Define \(C(\omega)=\int_0^\infty b(t,\omega)w(t)\,dt\). By construction \(C=\mathbb E[b(U)\mid\text{risk path}]\). Stationary one-time marginals give \(b(U)\sim\nu\) and \(\mathbb E[C]=\bar b\). Two applications of Jensen's inequality to the strictly convex map \(c\mapsto e^{-zc}\) yield
\[
e^{-\bar b z}\le\mathbb E[e^{-zC}]\le\mathbb E_\nu[e^{-bz}].
\]
Since \(S_\infty=S_0\mathbb E[e^{-zC}]\), these are exact bounds at the *actual* epidemic pressure \(z\), without replacing that pressure by either comparison pressure.

**3. Comparing the final-size roots.** For either benchmark function \(q\), define \(F_q(v)=\gamma v-I_0-S_0+S_0q(v)\). We have \(F_q(0)=-I_0<0\), \(F_q(v)\to+\infty\), and \(F_q\) is convex because it is a positive combination of exponentials and a linear function. Therefore \(F_q\) has exactly one positive zero, is negative before it, and positive after it. At the actual pressure, the Jensen bounds and mass balance give
\[
F_{q_\nu}(z)=S_0q_\nu(z)-S_\infty\ge0,
\qquad F_{q_{\mathrm{hom}}}(z)=S_0q_{\mathrm{hom}}(z)-S_\infty\le0.
\]
Consequently \(z_\nu\le z\le z_{\mathrm{hom}}\). Multiplying by \(\gamma\) proves the stated bounds for total ever-infected mass.

**4. Equality conditions.** Strict convexity in the conditional Jensen step gives strictness of the frozen comparison if with positive probability the sample path \(b(t)\) is nonconstant under the positive density \(w(t)dt\). Strictness in the other Jensen step holds if \(C\) is nondegenerate. For a stationary finite-state irreducible continuous-time chain with finite positive rates and at least two different risk values, the events of no jump from two states over an initial interval have positive probabilities, and the full integrated risk has nonzero variability; both inequalities are strict. This includes arbitrarily slow and arbitrarily fast finite switching.

## Verification
The analytic argument uses no numerical extrapolation. An accompanying `verify.py` independently evaluates the two-state susceptibility-switching ODE at representative risk values and checks both root bounds and conservation. Its numerical assertions corroborate rather than establish the universal theorem.

For illustration, take \(S_0=0.995\), \(I_0=0.005\), \(\gamma=1\), two risk states \(b_1=0.5\), \(b_2=3\), symmetric stationary weights \((1/2,1/2)\), and symmetric risk-state switching rate \(k=0.2\). The three final ever-infected fractions are approximately \(0.50324\) (frozen), \(0.63132\) (switching), and \(0.715\) (homogeneous), consistent with the strict sandwich. They have the same initial growth coefficient \(\bar b S_0-\gamma\).

## Relationship to prior work
Berestycki, Desjardins, Weitz, and Oury study epidemic risk diffusion and, in their zero-diffusion Gaussian submodel, derive a final-size comparison with classical SIR models (their Proposition 5). Their displayed comparison uses instantaneous mean and minimum risk, not the arbitrary-stationary-process *frozen-risk versus changing-risk* ordering proved here. Tkachenko and coauthors study temporal individual social-activity heterogeneity and transient stabilization; their models provide important context, but their accessible abstract is not evidence of the exact distribution-free sandwich. Katriel analyzes the final-size equation for permanently heterogeneous susceptibility, which gives the frozen benchmark. The argument here connects dynamic turnover to that baseline through conditional Jensen and the endogenous epidemic final-size root.

This prior-work comparison is provisional: an equivalent bound might exist in general Feynman–Kac, heterogeneous epidemic, or stochastic-activity literature. No independent priority certification is asserted.

## Limitations
The process \(b(t)\) must have the same marginal law at every time, be exogenous, and affect susceptibility only. The theorem does not cover risk behavior changing in direct response to the epidemic, correlated susceptibility and infectiousness, reinfection, network contact heterogeneity, or population turnover. It orders total *final* infections, not infection peaks, rates at each time, or arbitrary epidemic time series. The proof does not determine the size of the gap beyond these bounds.

## References
- H. Berestycki, B. Desjardins, J. S. Weitz, and J.-M. Oury, “Epidemic modeling with heterogeneity and social diffusion,” *Journal of Mathematical Biology* **86** (2023), 60. DOI: 10.1007/s00285-022-01861-w. First verified public date: 2023-03-25.
- A. V. Tkachenko et al., “Stochastic social behavior coupled to COVID-19 dynamics leads to waves, plateaus, and an endemic state,” *eLife* **10** (2021), e68341. DOI: 10.7554/eLife.68341.
- G. Katriel, “The size of epidemics in populations with heterogeneous susceptibility,” *Journal of Mathematical Biology* **65** (2012), 237–262. DOI: 10.1007/s00285-011-0460-2.
