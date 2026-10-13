# A missing population normalization separates the printed SARS-CoV-2 model from its fitted reproduction numbers

## Finding

The published SARS-CoV-2 system uses the unnormalized infection term
\[
\beta S(E+A+\epsilon V).
\]
Its exposed equation is
\[
\dot E
=
\beta S(E+A+\epsilon V)
-
(p+q+\mu)E.
\]

The corresponding reproduction number printed in the article is
\[
\mathcal R_0
=
\frac{\beta\Lambda}{\mu(p+q+\mu)}
+
\frac{\beta\Lambda p}
{\mu(p+q+\mu)(\gamma_A+\mu)}
+
\frac{\beta\Lambda q\epsilon}
{\mu(p+q+\mu)(\kappa+\gamma_V+\mu+\delta)}.
\]

Table 4 uses
\[
N_0=59{,}310{,}000,
\qquad
\Lambda=\mu N_0,
\qquad
\beta=0.34,
\]
but reports
\[
\mathcal R_0=6.11.
\]
Direct substitution in the displayed formula instead gives
\[
\mathcal R_0
=
362{,}680{,}129.5753\ldots.
\]

Table 3 has the same factor discrepancy. With
\[
\beta=0.034,
\]
the printed formula gives
\[
\mathcal R_0
=
36{,}268{,}012.9575\ldots,
\]
whereas the table reports
\[
0.61.
\]

The reported values are recovered by exactly one population-scale normalization. If the incidence is
\[
\frac{\beta S(E+A+\epsilon V)}{N},
\]
then at the disease-free state
\[
N=N_0=\frac{\Lambda}{\mu},
\]
and the two reproduction numbers are
\[
0.6114991225\ldots
\]
and
\[
6.1149912253\ldots,
\]
which round to the table entries.

Equivalently, if the printed mass-action equations are retained, the transmission coefficient must be replaced by
\[
\beta_{\mathrm{eff}}
=
\frac{\beta_{\mathrm{table}}}{N_0}.
\]
For the endemic numerical example,
\[
\beta_{\mathrm{eff}}
=
5.7325914686\times10^{-9}.
\]

Thus the printed equations, the fitted transmission coefficients, and the reported reproduction numbers cannot all belong to the same dimensional model.

## Assumptions and scope

The calculation uses the equations, reproduction-number formula, parameter values, and initial data exactly as printed in the article.

The source states
\[
\Lambda=\mu N_0
\]
and uses count-valued initial compartments summing to
\[
N_0=59{,}310{,}000.
\]
No population normalization is printed in the infection terms.

The finding does not determine which implementation was used in unavailable simulation code. Two mathematically coherent repairs are possible: use a frequency-dependent incidence with a population denominator, or keep mass action and rescale the fitted \(\beta\) values by \(1/N_0\).

The theoretical dynamics of those repaired models are not identical when the total population varies, so the two repairs should not be conflated beyond the disease-free scaling calculation.

## Proof

Let
\[
D=
\frac1{p+q+\mu}
+
\frac{p}{(p+q+\mu)(\gamma_A+\mu)}
+
\frac{q\epsilon}
{(p+q+\mu)(\kappa+\gamma_V+\mu+\delta)}.
\]
The source's reproduction number is
\[
\mathcal R_0^{\mathrm{mass}}
=
\beta\frac{\Lambda}{\mu}D.
\]
Because the numerical tables impose
\[
\frac{\Lambda}{\mu}=N_0,
\]
this becomes
\[
\mathcal R_0^{\mathrm{mass}}
=
\beta N_0D.
\]

For a frequency-dependent infection term
\[
\frac{\beta S(E+A+\epsilon V)}N,
\]
the same next-generation calculation at the disease-free state \(N=N_0\) gives
\[
\mathcal R_0^{\mathrm{freq}}
=
\beta D.
\]
Therefore
\[
\mathcal R_0^{\mathrm{mass}}
=
N_0\mathcal R_0^{\mathrm{freq}}.
\]
The discrepancy is not an approximate fitting effect; it is exactly the population factor \(N_0\).

Using
\[
\mu=\frac1{64.13\cdot365},
\quad
p=0.176,
\quad
q=0.024,
\quad
\gamma_A=0.07,
\]
\[
\gamma_V=0.061,
\quad
\kappa=0.08,
\quad
\delta=1.7826\times10^{-5},
\quad
\epsilon=0.5,
\]
one obtains
\[
\mathcal R_0^{\mathrm{freq}}(0.034)
=
0.6114991225\ldots
\]
and
\[
\mathcal R_0^{\mathrm{freq}}(0.34)
=
6.1149912253\ldots.
\]
Multiplication by
\[
N_0=59{,}310{,}000
\]
gives the mass-action values stated above.

There is a second, equation-level scale check. Table 5 has
\[
E(0)+A(0)+\epsilon V(0)
=
25{,}187{,}303.5.
\]
With the printed mass-action coefficient
\[
\beta=0.34,
\]
the initial per-susceptible force is
\[
8{,}563{,}683.19\ {\rm day}^{-1}.
\]
After division by \(N_0\), it is
\[
0.1443885212\ {\rm day}^{-1}.
\]
This confirms independently that the table-sized coefficient is on a normalized-contact scale, not the scale required by the printed unnormalized mass-action term.

## Verification

The bundled `verify.py` uses exact rational arithmetic for every parameter that is printed as a terminating decimal and uses the exact table relation
\[
\Lambda=\mu N_0.
\]

It verifies the identity
\[
\mathcal R_0^{\mathrm{mass}}
=
N_0\mathcal R_0^{\mathrm{freq}},
\]
reproduces the two table-scale normalized values, computes the two unnormalized values, and reconstructs the initial infection-force comparison.

No numerical ODE integration is used to establish the inconsistency.

## Relationship to prior work

The motivating article derives its reproduction number from the unnormalized mass-action system, reports fitted coefficients \(\beta=0.034\) and \(\beta=0.34\), and reports reproduction numbers \(0.61\) and \(6.11\). The exact arithmetic above shows that those three pieces are not mutually compatible.

Frequency-dependent incidence is a standard alternative when compartment variables are population counts. For example, Ghosh and Ghosh formulate a count-valued COVID-19 model with infection term
\[
\beta(t)\bigl(I+\kappa A+\omega Q+\rho H\bigr)\frac SN.
\]
That literature establishes the normalization convention but does not identify or correct the source-specific mismatch here.

Searches by DOI, exact title, the reported \(\beta\) and \(\mathcal R_0\) values, normalization terminology, and correction or erratum terminology did not locate a published correction of this parameter-scale inconsistency.

## Limitations

The result identifies an internal scaling inconsistency, not the authors' undocumented implementation.

If the simulations used a hidden population denominator, the fitted curves may correspond to a coherent frequency-dependent model different from the printed equations. If they used the printed equations, the fitted transmission coefficients must instead have been rescaled by approximately \(1/N_0\).

The finding does not refit the South African data and does not reassess the article's stability theorems after choosing one repaired incidence convention.

## References

1. O. F. Egbelowo, J. B. Munyakazi, M. T. Hoang, “Mathematical study of transmission dynamics of SARS-CoV-2 with waning immunity,” AIMS Mathematics 7 (2022), 15917–15938. DOI: 10.3934/math.2022871.
2. S. K. Ghosh, S. Ghosh, “A mathematical model for COVID-19 considering waning immunity, vaccination and control measures,” Scientific Reports 13 (2023), 3610. DOI: 10.1038/s41598-023-30800-y.
