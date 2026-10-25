# A sharp, dose-independent endpoint rule for a one-generation sterile-insect release

## Finding

For a density-regulated pest population with Beverton–Holt recruitment and one breeding generation of sterile-male mating suppression, the best release time over any finite generation horizon is **always the first or the last breeding generation**. There is no strictly optimal intermediate release time. The choice switches at one explicit initial-population threshold which is independent of the number of sterile males released.

Precisely, fix a positive growth factor \(R\), sterile-male intensity \(s>0\), initial wild adult abundance \(x_0>0\), and integer horizon \(n\ge2\). Write
\[
B_R(x)=\frac{Rx}{1+x},\qquad G_{R,s}(x)=\frac{Rx^2}{(1+x)(x+s)}.
\]
For a placement \(t\in\{0,\ldots,n-1\}\), let \(x_n(t)\) result from \(n\) updates, with \(G_{R,s}\) used only at step \(t\), and \(B_R\) at all other steps. Minimizing \(x_n(t)\) gives:

1. If \(0<R\le1\), the unique optimum is the last generation \(t=n-1\).
2. If \(R>1\), put
   \[
   x_{\mathrm{crit}}=\frac{R-1}{1+R^{n/2}}.
   \]
   For \(x_0<x_{\mathrm{crit}}\), the first generation \(t=0\) is uniquely optimal; for \(x_0>x_{\mathrm{crit}}\), the last generation is uniquely optimal. At equality, **exactly the two endpoints** are optimal. For \(n=2\), these are the only two permitted dates; for \(n\ge3\), every interior date is strictly worse than at least one endpoint.

The threshold depends on \(R,n\) and the untreated initial abundance, but not on \(s\), provided \(s>0\). In particular it is a comparison of equal-dose release dates, not a claim that larger releases cannot further reduce abundance.

## Assumptions and scope

This is a **discrete-generation deterministic** model. The unforced Beverton–Holt map \(B_R\) represents density-regulated recruitment. The mating-success probability during the single treated generation is \(x/(x+s)\), so \(G_{R,s}(x)=B_R(x)x/(x+s)\). Relative sterile intensity \(s\) is constant in units matching \(x\); the sterile males neither reproduce nor persist into a subsequent breeding generation. The release has no direct adverse effect on survivors outside its assigned breeding generation. The initial state, pulse intensity, number of generations, and environmental conditions are identical for all candidate schedules. The objective is **terminal wild-adult abundance**, not the sum of abundance over time, cumulative reproduction, release cost, or extinction probability. The map is well defined and strictly positive for the stated positive parameters. No claim is made for alternative density-regulation/mating couplings, overlapping generations, stochastic extinction, survival-coupled releases, or continuous-in-time interventions.

The carrying-capacity scale has been absorbed into the abundance unit. For \(R>1\), the unforced positive equilibrium in these units is \(R-1\); \(x_0\) is not a fraction of that equilibrium. The first permissible pulse is before the first update and the last before the \(n\)-th update.

## Proof

**1. Exact terminal reciprocal.** Put \(z=1/x\), \(z_0=1/x_0\), and \(f(z)=(z+1)/R\). Direct inversion gives
\[
\frac{1}{B_R(x)}=f(z),\qquad
\frac{1}{G_{R,s}(x)}=f(z)+\frac{s}{R}z(z+1).
\]
Every update after the treated one is the affine map \(f\), with linear slope \(R^{-1}\). If \(z_t=f^t(z_0)\), the exact final reciprocal is therefore
\[
\boxed{\quad
z_n(t)=f^n(z_0)+\frac{s}{R^n}H_t,\qquad
H_t=R^t z_t(z_t+1).
\quad}
\]
This identity applies to every integer \(t\in\{0,\ldots,n-1\}\). The positive factor \(s/R^n\) proves that minimizing the positive terminal abundance \(x_n(t)=1/z_n(t)\) is equivalent to maximizing \(H_t\), independently of the dose \(s>0\).

**2. No interior date can win.** For \(R\ne1\), let \(z_*=1/(R-1)\), \(d=z_0-z_*\). The affine iteration has \(z_t=z_*+dR^{-t}\). Substituting yields the exact representation
\[
H_t=\frac{R}{(R-1)^2}R^t+(2z_*+1)d+d^2R^{-t}.
\]
Extending this formula to real \(t\), differentiation gives
\[
H''(t)=(\log R)^2\left(\frac{R}{(R-1)^2}R^t+d^2R^{-t}\right)>0.
\]
For \(R=1\), \(z_t=z_0+t\), hence \(H_t=(z_0+t)(z_0+t+1)\) and \(H''(t)=2>0\). Strict convexity implies \(H_t<\max\{H_0,H_{n-1}\}\) for every integer \(0<t<n-1\). For \(n=2\) there is no interior date.

**3. Last release when \(R\le1\).** Writing \(z_t=f^t(z_0)>0\), direct subtraction gives
\[
H_{t+1}-H_t=
R^{t-1}(z_t+1)\bigl((1-R)z_t+1+R\bigr)>0
\]
for every integer \(t\ge0\) if \(0<R\le1\). Thus the last date uniquely maximizes \(H_t\).

**4. Exact endpoint switch when \(R>1\).** Here \(z_*>0\). The representation from step 2 yields
\[
H_{n-1}-H_0=(R^{n-1}-1)
\left(\frac{R}{(R-1)^2}-\frac{(z_0-z_*)^2}{R^{n-1}}\right).
\]
Since \(R^{n-1}-1>0\) and \(z_0>0\), the bracket is positive precisely when
\[
 z_0<\frac{1+R^{n/2}}{R-1},
\]
which is equivalent to \(x_0>x_{\mathrm{crit}}\). At equality the two endpoints tie; when the inequality is reversed the first endpoint wins. Strict convexity excludes every interior tie and completes the full classification. Note that the negative branch of the squared endpoint equation lies outside \(z_0>0\) because \(z_*-R^{(n-1)/2}\sqrt{R}/(R-1)<0\) for \(n\ge2\).

**5. Corollary: least sterile dose to meet a terminal target.** Let \(x_n^{(0)}=1/f^n(z_0)\) be the untreated terminal population. For any desired \(0<\theta<x_n^{(0)}\), solving the exact reciprocal for \(x_n(t)\le\theta\) yields the minimum dose
\[
 s_{\min}=\frac{R^n\left(\theta^{-1}-(x_n^{(0)})^{-1}\right)}{\max\{H_0,H_{n-1}\}}.
\]
It is attained at the same optimal endpoint date(s); every interior date requires a strictly larger dose when \(n\ge3\). This statement is a direct consequence of the same one-dose scheduling theorem and does not assume any additional treatment dynamics.

## Verification

The accompanying standalone Python 3 standard-library file `verify.py` uses exact rational arithmetic. Running `python3 verify.py` reproduces 1,332 rational parameter cases and 7,992 placement identities, including strict interior comparisons, both sides of the endpoint threshold, exact threshold ties, and terminal target-dose inversions. These finite checks verify arithmetic and reproducibility; the proof above establishes the result for all stated real parameters and integers.

For \(R=3\), \(n=4\), and \(s=1\), the threshold is exactly \(1/5\). At initial abundance \(1/10\), releasing first gives final abundance \(81/160\), less than every later release. At initial abundance \(1/5\), both endpoint dates give \(27/25\), strictly below either interior placement. At initial abundance \(3/10\), releasing last gives \(19683/16900\), below the other placements. All fractions follow by four direct map updates and can be reproduced using the verifier.

## Relationship to prior work

Knipling (1955) introduced population suppression by sterile male mating. White et al. (2010) model multiple timed sterile releases in mosquitoes, including stage structure and phase effects. Gordillo (2014) studies spatially optimized sterile insect releases with density regulation, employing a density-dependent recurrence whose denominator differs from the product-form recruitment–mating model used here. Ramirez and Gordillo (2016) numerically optimize releases in a continuous-stage deterministic model. The 2019 stage-structured Beverton–Holt mosquito work of Li and Li uses multiple interacting stages and sustained sterile population rules. None of the inspected full texts states the finite-horizon, exactly one treated generation endpoint theorem above, and their equations do not imply it by an immediate parameter substitution.

Berryman (1967) models sterile-male effects on a wild population, but only its publisher abstract was accessible, leaving an additional mathematical-priority risk. Xue, Tang and Liang (2012) consider optimal intervention timing for impulsive fishery and pest models, a potentially broader comparison. Only bibliographic and abstract material was accessible; its full results cannot be ruled out by the present inspection. The present theorem should therefore be regarded as a self-contained, literature-checked result with **residual priority risk**, not as a claim of exhaustive historical novelty. It is not a theorem for the other authors' distinct models.

## Limitations

The result relies on the **product** \(B_R(x)x/(x+s)\). For example, replacing density regulation with the different sterile-insect recurrence displayed by Gordillo (2014) changes the reciprocal dynamics and is outside the proof. Exact optimality of a one-generation pulse says nothing about simultaneous multi-generation releases, variable release intensity through time, mosquito seasonality, stochastic population eradication, or habitat heterogeneity. The originality comparison is incomplete for potentially relevant full texts including Berryman (1967) and Xue, Tang and Liang (2012). No independent mathematical audit has been performed.

## References

1. Knipling, E. F. (1955). *Possibilities of Insect Control or Eradication Through the Use of Sexually Sterile Males*. Journal of Economic Entomology 48, 459–462. https://doi.org/10.1093/jee/48.4.459 . First published 1955-08-01.
2. White, S. M., et al. (2010). *Modelling pulsed releases for sterile insect techniques: fitness costs of sterile and transgenic males and the effects on mosquito dynamics*. Journal of Applied Ecology. https://doi.org/10.1111/j.1365-2664.2010.01880.x .
3. Gordillo, L. F. (2014). *Optimal sterile insect release for area-wide integrated pest management in a density regulated pest population*. Mathematical Biosciences and Engineering 11, 511–521. https://doi.org/10.3934/mbe.2014.11.511 .
4. Ramirez, S., and Gordillo, L. F. (2016). *Approximating Optimal Release in a Deterministic Model for the Sterile Insect Technique*. International Journal of Agronomy. Published 2016-02-29.
5. Xue, Y., Tang, S., and Liang, X. (2012). *Optimal timing of interventions in fishery resource and pest management*. Nonlinear Analysis: Real World Applications 13, 1630–1646. https://doi.org/10.1016/j.nonrwa.2011.11.020 . Full text not inspected.
6. Berryman, A. A. (1967). *Mathematical Description of the Sterile Male Principle*. The Canadian Entomologist 99, 858–865. https://doi.org/10.4039/Ent99858-8 . Full text not inspected.
7. Li, Y., and Li, J. (2019). *Stage-structured discrete-time models for interacting wild and sterile mosquitoes with Beverton-Holt survivability*. Mathematical Biosciences and Engineering. https://doi.org/10.3934/mbe.2019028 .
