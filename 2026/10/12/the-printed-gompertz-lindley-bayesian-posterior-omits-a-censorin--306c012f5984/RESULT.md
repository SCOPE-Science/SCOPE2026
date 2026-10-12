# The printed Gompertz–Lindley Bayesian posterior omits a censoring factor
## Finding
The source models two independent latent failure times with
\[
T_{i1}\sim\mathrm{GLD}(\alpha,\beta_1),
\qquad
T_{i2}\sim\mathrm{GLD}(\alpha,\beta_2),
\]
where \(\alpha,\beta_1,\beta_2>0\). Its single-cause survival function is
\[
\overline F_j(t)
=
\frac{\alpha^2(e^{\beta_j t}+\alpha)}
{(1+\alpha)(e^{\beta_j t}+\alpha-1)^2},
\]
and its density is
\[
f_j(t)
=
\frac{\alpha^2\beta_j e^{\beta_jt}
(e^{\beta_jt}+\alpha+1)}
{(1+\alpha)(e^{\beta_jt}+\alpha-1)^3}.
\]

For progressive Type-II competing-risks data, the source first gives the standard model likelihood
\[
L_{\mathrm{model}}
\propto
\prod_{i=1}^m
\prod_{j=1}^2
\{f_j(t_i)\overline F_{3-j}(t_i)\}^{I(\delta_i=j)}
\{\overline F_1(t_i)\overline F_2(t_i)\}^{R_i}.
\]
Let
\[
R=\sum_{i=1}^mR_i=n-m.
\]
Every failure contribution contains
\[
\frac{\alpha^4}{(1+\alpha)^2},
\]
and every withdrawn-survivor contribution contains the same factor.

The specialized likelihood printed as Eq. (3.1) instead has a global factor
\[
\frac{\alpha^{4m}}{(1+\alpha)^{2m}},
\]
retains another factor \((1+\alpha)^{-2}\) inside each of the \(m\) failure terms, and retains \((1+\alpha)^{-2R_i}\) but no \(\alpha^{4R_i}\) inside each censoring term. Hence
\[
\boxed{
L_{3.1}
=
L_{\mathrm{model}}\,
\alpha^{-4R}(1+\alpha)^{-2m}.
}
\]
This is not a parameter-independent constant.

The next displayed log-likelihood, Eq. (3.2), is different: it places the full factor
\[
\frac{\alpha^4}{(1+\alpha)^2}
\]
in each failure term and, through two separate survival logarithms, also places
\[
\frac{\alpha^4}{(1+\alpha)^2}
\]
inside every censoring contribution. Thus
\[
\boxed{
\exp\{\ell_{3.2}\}
\propto L_{\mathrm{model}},
}
\]
not Eq. (3.1). The classical score equations derived from Eq. (3.2) therefore correspond to the stated competing-risks model, while Eqs. (3.1) and (3.2) are mutually inconsistent.

The discrepancy reappears in the Bayesian section. The source explicitly says it combines Eq. (3.1) with independent gamma priors and prints Eq. (4.2) with the same factorization. Therefore
\[
\boxed{
\pi_{\mathrm{correct}}(\alpha,\beta_1,\beta_2\mid t)
\propto
\pi_{4.2}(\alpha,\beta_1,\beta_2\mid t)
\alpha^{4R}(1+\alpha)^{2m}.
}
\]
The correction changes only the \(\alpha\)-dependence, but it can be large. Its log derivative is
\[
\boxed{
\frac{4R}{\alpha}+\frac{2m}{1+\alpha}.
}
\]

For the simulation configuration
\[
n=30,\qquad m=20,\qquad R=10,
\]
used in the article, this missing score term equals
\[
55.411255\ldots
\]
at \(\alpha=1.1\). The multiplicative correction changes by approximately
\[
3.82\times10^{16}
\]
between \(\alpha=1.1\) and \(\alpha=2\). It therefore cannot be treated as a harmless normalization.

The article's Metropolis–Hastings algorithm states that its stationary density is the posterior \(\pi^*\) printed in the Bayesian section. If Eq. (4.2) is used literally in that acceptance ratio, the Markov chain targets a different posterior from the stated competing-risks model.

## Assumptions and scope
The result uses the source's own Gompertz–Lindley density and survival functions, its independent two-cause competing-risks construction, and progressive Type-II censoring with predetermined removals.

The correction concerns the algebraically printed likelihood Eq. (3.1) and posterior Eq. (4.2). It does not alter the correctly expanded log-likelihood Eq. (3.2).

No claim is made about unavailable software. In particular, the numerical Bayesian tables could have been generated from a corrected implementation even though the displayed posterior is not the posterior of the stated model.

The finding does not challenge the use of gamma priors, Metropolis–Hastings sampling, or Tierney–Kadane approximation in principle; those methods become valid for this model when supplied with the corrected posterior kernel.

## Proof
For a failure from cause 1 at time \(t\), independence gives the likelihood contribution
\[
f_1(t)\overline F_2(t).
\]
Both factors contain \(\alpha^2/(1+\alpha)\), so the product contains
\[
\frac{\alpha^4}{(1+\alpha)^2}.
\]
The same is true for a cause-2 failure.

A unit withdrawn alive at time \(t\) contributes
\[
\overline F_1(t)\overline F_2(t),
\]
which again contains
\[
\frac{\alpha^4}{(1+\alpha)^2}.
\]
Thus, with \(m\) failures and \(R\) withdrawn survivors, the correct global powers contributed by these normalizing terms are
\[
\alpha^{4(m+R)}(1+\alpha)^{-2(m+R)}.
\]

In Eq. (3.1), the displayed global factor contributes
\[
\alpha^{4m}(1+\alpha)^{-2m}.
\]
The internal failure fractions contribute an additional
\[
(1+\alpha)^{-2m},
\]
and the censoring fractions contribute
\[
(1+\alpha)^{-2R}
\]
but no \(\alpha^{4R}\). Therefore its corresponding powers are
\[
\alpha^{4m}(1+\alpha)^{-4m-2R}.
\]
Dividing by the correct powers gives
\[
\alpha^{-4R}(1+\alpha)^{-2m},
\]
proving the likelihood identity.

Eq. (3.2) directly writes the full cause-specific failure factors and the two full survival logarithms for each withdrawn unit, so exponentiating it reproduces the model likelihood up to the usual parameter-free progressive-censoring combinatorial constant.

Multiplication by the same prior on both sides preserves the likelihood ratio. Hence the posterior correction is the reciprocal factor
\[
\alpha^{4R}(1+\alpha)^{2m}.
\]
Differentiating its logarithm gives the stated score correction.

## Verification
The bundled checker implements the source density and survival functions and a positive progressive-censoring example with two observed causes.

It evaluates the likelihood in three ways: directly from the general competing-risks formula, from the specialized Eq. (3.1) factorization as printed, and by exponentiating the expanded Eq. (3.2) kernel. It verifies that Eq. (3.2) agrees with the direct likelihood and that
\[
L_{3.1}/L_{\mathrm{model}}
=
\alpha^{-4R}(1+\alpha)^{-2m}.
\]

It then verifies the analytic score correction and the stated numerical magnitudes for the article's \((n,m)=(30,20)\) simulation setting.

These computations are reproducibility checks; the discrepancy follows exactly from counting the source's survival-function normalizers.

## Relationship to prior work
The primary article itself supplies both sides of the comparison. Its general progressive competing-risks likelihood in Eq. (2.4) and its expanded log-likelihood in Eq. (3.2) agree with each other. The specialized product in Eq. (3.1) does not. The Bayesian posterior Eq. (4.2) explicitly says it is obtained by combining Eq. (3.1) with the prior and reproduces the same defective factorization.

A later paper on bootstrap-calibrated estimation for the same progressively censored Gompertz–Lindley competing-risks setting focuses on maximum-likelihood bias correction and BCa intervals. Its accessible article record does not report this Bayesian posterior correction and does not cover the accepted claim.

Focused searches using the exact DOI, equation numbers, Gompertz–Lindley competing-risks terminology, missing survival-normalizer language, posterior-kernel terminology, and \(\alpha\)-factor aliases did not locate a published correction of Eqs. (3.1) and (4.2).

## Limitations
The result does not determine which posterior kernel was used in the authors' software.

It does not recompute the simulation tables, real-data posterior summaries, or credible intervals.

The classical log-likelihood Eq. (3.2) is consistent with the model, so this finding does not invalidate all of the paper's likelihood-based calculations.

A recent or unindexed correction may exist outside the sources examined.

## References
1. M. H. Abu-Moussa, E. M. Almetwally, and A. El-Raheem M. Abd El-Raheem, “Classical and Bayesian inference for progressively censored competing risks data under the Gompertz-Lindley model,” AIMS Mathematics 11 (2026), 12064–12093. DOI: 10.3934/math.2026495.
2. M. A. Khan, “Bootstrap-calibrated estimation for progressively censored competing risks data under the Gompertz-Lindley model,” ORA Mathematics 1 (2026), e2026006.
