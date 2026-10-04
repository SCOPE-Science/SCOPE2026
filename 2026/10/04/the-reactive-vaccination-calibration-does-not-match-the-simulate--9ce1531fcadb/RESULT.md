# The reactive-vaccination calibration does not match the simulated susceptible equation
## Finding
The reactive-vaccination rate calculation in Oraby and Ndeffo-Mbah's Texas measles model is performed with a different susceptible-population equation from the one used for the counterfactual simulations.

The main intervention model replaces the susceptible equation by
\[
\frac{dS_a}{dt}=-\lambda_a(t)S_a(t)-\nu_a(t)\,\mathrm{VE}_a S_a(t),
\]
and the released implementation applies the same multiplicative vaccination term. By contrast, the supplementary calibration section introduces, in isolation,
\[
\frac{dS_a}{dt}=-\nu_a\bigl(S_a-S_{\infty,a}\bigr)
\]
and therefore uses
\[
\nu_a=-\frac1T\log\left(\frac{S_a(T)-S_{\infty,a}}{S_a(0)-S_{\infty,a}}\right).
\]
These are different dynamical systems: the first has zero as its vaccination-only asymptote and contains vaccine efficacy; the second has the positive asymptote \(S_{\infty,a}\) and omits vaccine efficacy.

For the values used in the supplement, \(T=150\) days and \(\mathrm{VE}=0.93\). Under the simulated law with infection switched off, the exact solution is
\[
S_a(T)=S_a(0)e^{-\nu_a\mathrm{VE}T}.
\]
Thus a one-half reduction requires
\[
\nu_{1/2}=\frac{\log 2}{150\cdot0.93}
=0.004968796993\ldots\;\text{day}^{-1},
\]
which is the same for both age groups because the requested reduction factor and vaccine efficacy are the same.

The supplement instead states that reducing \(0.33\) to \(0.165\) and \(0.22\) to \(0.11\) over 150 days requires \(0.00658\) and \(0.00846\) per day, respectively. Those values solve its affine target-relaxation equation. Inserted into the simulated multiplicative law, the corresponding endpoints are approximately
\[
0.33e^{-0.00658124369\cdot0.93\cdot150}=0.1317636,
\qquad
0.22e^{-0.00846158537\cdot0.93\cdot150}=0.0675749,
\]
not \(0.165\) and \(0.11\).

Therefore the supplement's half-susceptibility calibration cannot be used as a calibration of the counterfactual vaccination equation actually stated and implemented.

## Assumptions and scope
The object is the reactive-vaccination component of the age-structured multistage SEIR model in Oraby and Ndeffo-Mbah. The comparison holds for each age group separately. To match the supplement's phrase “in isolation,” infection is switched off during the calibration comparison, so \(\lambda_a(t)=0\). Vaccine efficacy is fixed at the source value \(\mathrm{VE}=0.93\), and the campaign duration is \(T=150\) days.

No assumption is made about the posterior distribution, the fitted transmission process, or the epidemiological effectiveness of vaccination. The result is an equation-consistency statement about how a vaccination rate maps to a target susceptible fraction.

## Proof
For the intervention equation used in the main model, with \(\lambda_a(t)=0\) and constant \(\nu_a\), separation of variables gives
\[
\frac{dS_a}{S_a}=-\nu_a\mathrm{VE}\,dt,
\]
so
\[
S_a(T)=S_a(0)e^{-\nu_a\mathrm{VE}T}.
\]
If the desired endpoint is \(S_a(T)=S_a(0)/2\), then
\[
e^{-\nu_a\mathrm{VE}T}=\frac12,
\]
and hence
\[
\nu_a=\frac{\log 2}{\mathrm{VE}T}.
\]
Substituting \(\mathrm{VE}=0.93\) and \(T=150\) gives
\[
\nu_a=0.004968796993\ldots\;\text{day}^{-1}.
\]

For comparison, solving the supplementary affine equation
\[
\dot S_a=-\nu_a(S_a-S_{\infty,a})
\]
gives
\[
S_a(T)=S_{\infty,a}+(S_a(0)-S_{\infty,a})e^{-\nu_aT},
\]
which leads exactly to the supplement's logarithmic target formula. With \(S_{\infty}=0.067\), the two half-target calculations give
\[
\nu_0=0.006581243690\ldots,
\qquad
\nu_1=0.008461585371\ldots.
\]
These differ because the distances from \(0.33\) and \(0.22\) to the positive asymptote \(0.067\) differ.

Evaluating the main multiplicative equation at these two rates instead yields
\[
S_0(150)=0.1317635673\ldots,
\qquad
S_1(150)=0.0675748848\ldots,
\]
so neither reaches the stated half-target. This establishes the mismatch.

## Verification
The standalone checker `verify.py` recomputes both supplementary target-relaxation rates, the correct half-reduction rate for the simulated multiplicative vaccination law, and the endpoints obtained when the supplementary rates are inserted into that law. It also checks that the correct multiplicative-law rate halves both source initial susceptible fractions to high numerical precision.

The public implementation was inspected at `G_Bayesian_Measles_NB.ipynb`: its SEIR right-hand side subtracts the vaccination term proportional to \(\nu_t\,\mathrm{VE}\,S\), matching the main article rather than the supplementary target-relaxation equation.

## Relationship to prior work
The source article states the multiplicative vaccination equation in its main counterfactual model and its supplement separately derives campaign rates from an affine target-relaxation equation. The accompanying public notebook implements the multiplicative form. Searches for the article title together with the printed rates, target-susceptibility formula, vaccination calibration, correction, and erratum did not locate a published reconciliation or prior statement of this exact mismatch.

A separate 2025 Texas measles spatial-spread preprint by Ndeffo-Mbah and coauthors studies a different modeling question and does not supply this source-specific calibration correction. General vaccination-compartment models do not by themselves cover the claim: the finding is the incompatibility between two equations asserted within this particular study and its released implementation.

## Limitations
This result does not rerun the Bayesian fit and does not claim that the reported counterfactual trajectories are numerically incorrect. The implementation is consistent with the main article's multiplicative vaccination term; the problem is that the supplement's half-reduction calculation is derived from another ODE and therefore does not calibrate that implemented term.

The source ultimately explores \(0.1\%\), \(0.2\%\), and \(0.3\%\) daily campaign scenarios. The finding does not assert that those policy scenarios are inadmissible; it only separates them from the printed 150-day half-susceptibility calculation. Infection during a real campaign would add the separate force-of-infection loss \( -\lambda_a S_a\), so the isolated calculation is not a prediction of total susceptible decline in an epidemic trajectory.

## References
1. T. Oraby and M. L. Ndeffo-Mbah, “The 2025 measles outbreak in Texas,” *BMC Infectious Diseases* 26, 1430 (2026), DOI 10.1186/s12879-026-13663-2.
2. Supplementary Material 1 for DOI 10.1186/s12879-026-13663-2, especially the reactive-vaccination campaign design and model-parameter table.
3. Public implementation: `tamfatkh/measles`, `G_Bayesian_Measles_NB.ipynb`.
4. M. L. Ndeffo-Mbah, S. Mokhtar, A. Pandey, and C. R. Wells, “Risk and Spatial Spread of a Measles Outbreak in Texas,” medRxiv 2025.09.01.25334576.
