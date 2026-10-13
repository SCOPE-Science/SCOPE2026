# Exact boundary identifiability stratification of the FEPW model
## Finding
Consider the flexible exponential power–Weibull (FEPW) survival function
\[
R(x;\tau,\eta,\kappa,\varphi)
=
\exp\!\left\{
1-\exp[(\tau x)^\eta]-(\kappa x)^\varphi
\right\},
\qquad x>0,
\]
with \(\eta,\varphi>0\). The defining section of the 2026 source allows
\[
\tau,\kappa\ge0
\]
and Proposition 1 then asserts identifiability of the full parameter vector.

On that stated closed scale domain, the correct structural classification is:

\[
\begin{array}{c|c|c}
\text{scale stratum} & \text{survival law} & \text{identifiability consequence}\\
\hline
\tau>0,\ \kappa>0 &
\exp\{1-\exp[(\tau x)^\eta]-(\kappa x)^\varphi\} &
(\tau,\eta,\kappa,\varphi)\text{ is identifiable}\\
\tau=0,\ \kappa>0 &
\exp[-(\kappa x)^\varphi] &
\eta\text{ is erased}\\
\tau>0,\ \kappa=0 &
\exp\{1-\exp[(\tau x)^\eta]\} &
\varphi\text{ is erased}\\
\tau=0,\ \kappa=0 &
1 &
\text{not a proper finite lifetime law.}
\end{array}
\]

Moreover, no proper law in one of the first three strata coincides with a law in either of the other two strata. Hence the source's four-parameter map is injective exactly on the positive interior
\[
(\tau,\eta,\kappa,\varphi)\in(0,\infty)^4.
\]
The boundary is naturally a union of lower-dimensional Weibull and exponential-power submodels, with the double-zero point excluded from the finite-lifetime model.

This does not invalidate the source's positive-interior numerical analyses: its Bayesian section later states that all four parameters are strictly positive and places Gamma priors on the positive real line. The correction is to the model domain and Proposition 1 as originally stated.

## Assumptions and scope
Identifiability means injectivity of the map from a parameter vector to the survival function on \(x>0\).

The claim uses exactly the source's survival function and its initially stated parameter restrictions
\[
\eta,\varphi>0,\qquad \tau,\kappa\ge0.
\]
No assertion is made about numerical weak identifiability near the boundary, rates of estimation as a scale tends to zero, or posterior concentration. The statement is structural.

The phrase “proper finite lifetime law” excludes the double-zero survival \(R(x)\equiv1\), which places all mass at \(+\infty\) rather than defining an ordinary lifetime distribution on \((0,\infty)\).

## Proof
Define the cumulative hazard
\[
H(x)=-\log R(x)
=
\exp[(\tau x)^\eta]-1+(\kappa x)^\varphi.
\]

First suppose \(\tau>0\) and \(\kappa>0\). Write
\[
a=\tau^\eta>0,\qquad b=\kappa^\varphi>0,
\]
so
\[
K(x):=H(x)+1=e^{a x^\eta}+b x^\varphi.
\]
The exponential term dominates every power as \(x\to\infty\), and therefore
\[
\log K(x)=a x^\eta+o(1).
\]
Consequently,
\[
\eta
=
\lim_{x\to\infty}
\frac{\log\log K(x)}{\log x},
\]
and, once \(\eta\) is known,
\[
a
=
\lim_{x\to\infty}
\frac{\log K(x)}{x^\eta}.
\]
Thus \(\tau=a^{1/\eta}\) is identified. Subtracting the identified exponential term gives
\[
K(x)-e^{a x^\eta}=b x^\varphi.
\]
Hence
\[
\varphi
=
\frac{\log\{K(x_2)-e^{a x_2^\eta}\}
-\log\{K(x_1)-e^{a x_1^\eta}\}}
{\log x_2-\log x_1}
\]
for any distinct positive \(x_1,x_2\), and then
\[
b=\frac{K(x)}{x^\varphi}-\frac{e^{a x^\eta}}{x^\varphi},
\qquad
\kappa=b^{1/\varphi}.
\]
This proves injectivity on the positive interior.

Now let \(\tau=0\) and \(\kappa>0\). Since \((0x)^\eta=0\) for \(x>0\),
\[
R(x)=
\exp\{1-e^0-(\kappa x)^\varphi\}
=
e^{-(\kappa x)^\varphi},
\]
which is independent of \(\eta\). Distinct values of \(\eta\) therefore generate exactly the same law. The remaining pair \((\kappa,\varphi)\) is the ordinary Weibull scale-shape parameterization and is identifiable.

Similarly, if \(\tau>0\) and \(\kappa=0\),
\[
R(x)=
\exp\{1-e^{(\tau x)^\eta}\},
\]
which is independent of \(\varphi\). The pair \((\tau,\eta)\) is identifiable because
\[
\log\{1-\log R(x)\}=(\tau x)^\eta
\]
determines the log-log slope \(\eta\) and then \(\tau\).

At the double-zero point,
\[
R(x)=\exp(1-e^0)=1
\]
for every \(x>0\). Thus the associated random lifetime never fails at a finite time and is not a proper distribution on \((0,\infty)\).

It remains to exclude coincidences across the three proper strata. An interior cumulative hazard
\[
e^{a x^\eta}-1+b x^\varphi
\]
grows faster than every power and has a strictly positive polynomial residual after its exponential term is identified, so it cannot equal either a pure Weibull hazard \(b_0x^{\varphi_0}\) or a pure exponential-power hazard \(e^{a_0x^{\eta_0}}-1\). A pure exponential-power hazard also grows faster than every power, so it cannot equal a pure Weibull hazard. Hence the stated strata are disjoint at the level of proper laws.

## Verification
The included checker substitutes multiple boundary parameter vectors directly into the source survival function. It verifies that changing \(\eta\) when \(\tau=0\) leaves the survival function unchanged, that changing \(\varphi\) when \(\kappa=0\) leaves it unchanged, and that the double-zero survival is identically one.

For a positive-interior test parameter vector, the checker also evaluates the asymptotic log-log slope and leading coefficient at high precision and recovers \(\eta\) and \(\tau^\eta\) to shrinking error. These calculations are consistency checks only; injectivity is proved analytically above.

## Relationship to prior work
The 2026 FEPW source itself is the decisive comparison. Its defining equations permit \(\tau,\kappa\ge0\), while Proposition 1 concludes equality of the entire four-parameter vector from equality of survival functions. The proof analyzes nonzero asymptotic terms and does not treat the zero-scale strata. Later, the Bayesian section instead says that all four parameters are strictly positive and uses Gamma priors supported on the positive real line. The present classification reconciles these two parameter-domain statements.

The earlier additive Chen–Weibull and Weibull–Chen literature studies closely related additive competing-risk lifetime models. Those sources motivate positive-component reliability models and hazard flexibility, but the inspected primary records do not state this source-specific FEPW boundary quotient or repair Proposition 1 on the domain containing zero scales.

Focused searches using the exact DOI, model name, identifiability, zero-scale, boundary, and correction terminology located the original article and mirrors but no corrigendum or published boundary stratification.

## Limitations
The result is about exact structural identifiability, not practical estimability near \(\tau=0\) or \(\kappa=0\). Fisher-information degeneration and local rates near those boundaries are not analyzed.

The source's estimation procedures work with strictly positive parameters, so the correction does not by itself show an error in its reported positive-interior maximum-likelihood or Bayesian fits.

The related additive Chen–Weibull full publisher record available during this check exposed its abstract and bibliographic material rather than all theorem text. No inspected material covered the FEPW boundary statement, but an older general identifiability theorem for additive hazards could encode a related principle under broader notation.

## References
1. M. G. M. Ghazal, “Hamiltonian Monte Carlo–based inference for the flexible exponential power–Weibull distribution with applications in reliability analysis,” AIMS Mathematics 11 (2026), 11659–11705. DOI: 10.3934/math.2026481.
2. T. T. Thach and R. Briš, “An additive Chen–Weibull distribution and its applications in reliability modeling,” Quality and Reliability Engineering International 37 (2021), 352–373. DOI: 10.1002/qre.2740.
3. B. Tarvirdizade and M. Ahmadpour, “A New Extension of Chen Distribution with Applications to Lifetime Data,” Communications in Mathematics and Statistics 9 (2021), 23–38. DOI: 10.1007/s40304-019-00185-4.
