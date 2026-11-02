# A sharp three-season arrow of time invisible to reciprocal-abundance autocorrelation

## Finding

Consider the periodically forced Beverton–Holt population recursion
\[
 x_{t+1}=\frac{a x_t}{1+\beta_t x_t},\qquad a>1,\quad \beta_t>0,\quad \beta_{t+n}=\beta_t.
\]
For each positive periodic forcing sequence there is a unique attracting positive population cycle \(x_t^*\). Define its inverse abundance \(y_t^*=1/x_t^*\). Reverse the seasonal crowding calendar by setting \(\beta_t^{\mathrm{rev}}=\beta_{-t}\), with indices modulo \(n\). Then **every cyclic inverse-abundance autocorrelation is unchanged under reversal**, for every period \(n\ge1\):
\[
 \frac1n\sum_{t=0}^{n-1}y_t^*y_{t+h}^*
 =\frac1n\sum_{t=0}^{n-1}y_t^{*,\mathrm{rev}}y_{t+h}^{*,\mathrm{rev}}
 \qquad(h\in\mathbb Z).
\]
Nevertheless three is the smallest period permitting an orientation-dependent phase-averaged saturating population response. In period three write the forward calendar \((b,c,d)\), with \(b,c,d>0\), and its reversal \((b,d,c)\). For every fixed \(q\ge0\), define the mean saturating response
\[
 M_q(b,c,d)=\frac13\sum_{t=0}^{2}\frac{x_t^*}{1+q x_t^*}.
\]
Then the exact, saturation-independent sign law is
\[
 \boxed{\operatorname{sgn}\bigl(M_q(b,c,d)-M_q(b,d,c)\bigr)
 =\operatorname{sgn}\bigl((b-c)(b-d)(c-d)\bigr).}
\]
In particular, the two orientation classes differ for **every finite** \(q\ge0\) exactly when the three crowding coefficients are pairwise distinct. If two are equal, the calendars differ only by a cyclic rotation and tie. The three reciprocal-abundance values for the two orientations have identical first and second power sums but have different third power sums in the pairwise-distinct case.

## Assumptions and scope

All population states and seasonal crowding coefficients are strictly positive. The intrinsic annual growth factor \(a>1\) is constant throughout a season cycle. The population is deterministic, scalar, and updated by the exact Beverton–Holt map shown above, with no harvesting subtraction, immigration, observation noise, or season-varying growth factor. The comparison uses steady-state phase averages; the same limits arise from averages of any positive trajectory because of global attraction. The response \(x/(1+q x)\) is a saturating census or yield proxy with \(q\ge0\), not a particular fitted harvesting model.

The first assertion ranges over **all integer periods \(n\ge1\), all positive periodic crowding sequences, and all integer lags \(h\)**. The strict three-season sign law ranges over **every** \(a>1\), every \(b,c,d>0\), and every finite \(q\ge0\); it includes \(q=0\), ordinary mean abundance.

## Proof

**1. Unique globally attracting periodic state.** Put \(y_t=1/x_t\). The nonlinear recurrence becomes the affine scalar equation
\[
 a y_{t+1}-y_t=\beta_t.
\]
Over a complete cycle, the map on \(y\) is an affine contraction with slope \(a^{-n}\) and strictly positive intercept. It has a unique positive periodic orbit that attracts every \(y_0>0\), and therefore every \(x_0>0\) approaches the unique positive periodic population orbit. This elementary argument independently supplies the existence and convergence required below.

**2. Every reciprocal-abundance autocorrelation survives reversal.** Write \(B_k\) and \(Y_k\) for the discrete Fourier transforms of \((\beta_t)\) and \((y_t^*)\), using frequency \(\omega_k=2\pi k/n\). The phase relation above gives
\[
 Y_k=\frac{B_k}{a e^{i\omega_k}-1}.
\]
The denominator never vanishes because \(a>1\). Reversal of a real sequence conjugates its Fourier coefficients, up to an immaterial phase for any cyclic shift: \(B_k^{\mathrm{rev}}=\overline{B_k}\). Hence
\[
 |Y_k^{\mathrm{rev}}|^2=|Y_k|^2
 \qquad (k=0,\ldots,n-1).
\]
The finite cyclic autocorrelation at every lag is the inverse discrete Fourier transform of these squared magnitudes. Thus all circular autocorrelations, and in particular the mean and variance of reciprocal abundance, are identical under the two calendars. This does **not** assert equality of their phase-resolved trajectories or of higher-order statistics.

**3. Exact three-season inverse cycles.** Let \(Q=a^3-1>0\). For the forward calendar, write the three reciprocal states as \(L_i/Q\), where
\[
 (L_0,L_1,L_2)=
 (b+ac+a^2d,\;a^2b+c+ad,\;ab+a^2c+d).
\]
For the reversed calendar, the numerators are
\[
 (R_0,R_1,R_2)=
 (b+ad+a^2c,\;a^2b+d+ac,\;ab+a^2d+c).
\]
These follow by substituting the affine equation around one period; no finite truncation or approximation is involved. Denote the elementary symmetric functions of either three-element list by \(e_1,e_2\). Both orientations share
\[
 e_1=(1+a+a^2)(b+c+d)
\]
and the same sum of squares,
\[
 \sum_iL_i^2=\sum_iR_i^2
 =(1+a^2+a^4)(b^2+c^2+d^2)
 +2(a+a^2+a^3)(bc+bd+cd).
\]
Consequently \(e_2=(e_1^2-\sum_iL_i^2)/2\) is common to both. Expansion of the two cubic products, followed by collecting the terms alternating in \(b,c,d\), yields the exact identity
\[
 \prod_iL_i-\prod_iR_i
 =-a(a-1)^3(a+1)(b-c)(b-d)(c-d).
 \tag{1}
\]
The multiplication can be verified term-by-term or by the accompanying symbolic checker. Because the first two power sums agree, Newton's cubic identity also gives
\[
 \frac13\sum_i\left(\frac{L_i}{Q}\right)^3
 -\frac13\sum_i\left(\frac{R_i}{Q}\right)^3
 =-\frac{a(a-1)^3(a+1)}{Q^3}(b-c)(b-d)(c-d).
\]
This is nonzero exactly when \(b,c,d\) are pairwise distinct, even though their reciprocal means and variances coincide.

**4. All saturating response strengths have the same orientation.** Fix a finite \(q\ge0\) and set \(z=qQ\). Define
\[
 P_L(z)=\prod_{i=0}^2(L_i+z),\quad
 P_R(z)=\prod_{i=0}^2(R_i+z),\quad
 E_2(z)=\sum_{0\le i<j\le2}(L_i+z)(L_j+z).
\]
By the common \(e_1,e_2\), the last expression is also the second elementary symmetric function of \((R_i+z)\); explicitly \(E_2(z)=e_2+2ze_1+3z^2>0\). Since the first two elementary functions agree, equation (1) implies \(P_L(z)-P_R(z)=\prod_iL_i-\prod_iR_i\), independent of \(z\). Also
\[
 M_q(b,c,d)=\frac{Q}{3}\frac{E_2(z)}{P_L(z)},\qquad
 M_q(b,d,c)=\frac{Q}{3}\frac{E_2(z)}{P_R(z)}.
\]
Subtraction therefore gives the **exact signed difference**
\[
 \boxed{M_q(b,c,d)-M_q(b,d,c)
 =\frac{Qa(a-1)^3(a+1)E_2(z)}{3P_L(z)P_R(z)}
 (b-c)(b-d)(c-d).}
 \tag{2}
\]
Every factor outside the last three differences is strictly positive. This proves the sign statement, strictness, and all \(q\ge0\) cases without relying on a numerical experiment.

**5. Sharp minimum period.** Reversing a one- or two-periodic calendar produces a cyclic rotation. Such a rotation only changes the phase origin of the attracting orbit, so every phase-averaged response ties. For three distinct positive crowding levels, equation (2) is nonzero; hence period three is minimal. If any two of \(b,c,d\) agree, the two three-season orders likewise coincide up to a cyclic shift.

## Verification

The standalone file `checker.py` performs exact symbolic checks of the two symmetric-polynomial equalities, identity (1), and the cleared-denominator form of (2), plus an independent rational reconstruction of periodic cycles, every cyclic inverse-autocorrelation for specified periods up to eight, and multiple positive parameter and saturation choices. On the delivered artifact, `python checker.py` reports `PASS: 612 exact assertions; polynomial identity and rational replay verified`. Finite rational tests are consistency checks; the Fourier and algebraic proofs above establish the universal quantifiers.

A fully rational witness takes \(a=2\) and \((b,c,d)=(1,2,3)\). The forward reciprocal cycle is \((17,12,13)/7\) and its reversal is \((15,11,16)/7\). Both have mean reciprocal abundance \(2\) and mean square reciprocal abundance \(602/147\), but their mean cubes differ by \(12/343\). At \(q=0\), the ordinary abundance averages differ by
\[
 M_0(1,2,3)-M_0(1,3,2)=-\frac{4067}{1750320}<0.
\]
The exact formula (2) proves that the sign remains negative for every finite \(q\ge0\).

## Relationship to prior work

The basic periodically forced Beverton–Holt model and the question of mean abundance under fluctuating carrying capacities were studied by Cushing and Henson (2002). Yang and Sacker (first available online 9 October 2012) give a general exact arbitrary-period expression for average state density relative to average seasonal carrying capacity and display a three-period formula in Appendix B. Their formula includes enough state-level information to evaluate the **ordinary mean** at \(q=0\) for either calendar; this is not represented as new here. The present claim instead concerns the joint **all-period reversal invariance of every inverse-density autocorrelation** and the **strict signed orientation theorem for every saturating response**, including a Vandermonde factor and sharp three-season onset. Those structural assertions are not stated in the inspected Yang–Sacker results and require additional reciprocal-state and spectral comparisons.

Allen and Kocic (2013) study arithmetic, geometric and harmonic resonance under periodic/random forcing; only their publisher/abstract record could be examined, creating a historical-priority limitation. Al-Ghassani and AlSharawi (first online 2019) study permutations in a **periodically harvested** Beverton–Holt model with **geometric-mean** population objective; their available abstract describes a different dynamics and comparison. Related results for other period lengths and different carrying-capacity multisets do not imply (2) or the all-lag invariance. No priority claim is made for the elementary affine transform, DFT identity, or classical symmetric-polynomial facts separately.

## Limitations

The result assumes time-independent intrinsic growth \(a\) and a deterministic scalar recurrence. With varying intrinsic growth, the reciprocal dynamics is a time-varying filter, so the Fourier-autocorrelation proof does not apply unchanged. The three-season sign theorem concerns phase averages of \(x/(1+qx)\), not every conceivable nonlinear observable, and says nothing about the relative ranking of arbitrary longer-period permutations. Inverse-density autocorrelation is a mathematical observable, not automatically a practical estimator from noisy sparse monitoring. Priority remains provisional because the complete Allen–Kocic (2013) and Al-Ghassani–AlSharawi (2019) articles were not accessible for full-text comparison. No independent external verification has been performed.

## References

1. J. M. Cushing and S. M. Henson, *A Periodically Forced Beverton-Holt Equation*, Journal of Difference Equations and Applications 8 (2002), 1119–1120. https://doi.org/10.1080/1023619021000053980
2. Y. Yang and R. J. Sacker, with Appendix A by C. Haskell, *Resonance and attenuation in the n-periodic Beverton–Holt equation*, Journal of Difference Equations and Applications 19 (2013), 1174–1191; first online 2012-10-09. https://doi.org/10.1080/10236198.2012.726988 ; authorized author-posted full text: https://dornsife.usc.edu/robert-sacker/wp-content/uploads/sites/256/2023/06/Yang-Sacker-BH.pdf
3. L. J. S. Allen and V. L. Kocic, *Resonance in Beverton–Holt population models with periodic and random coefficients*, Journal of Difference Equations and Applications 20 (2014), 925–946; first online 2013-11-12. https://doi.org/10.1080/10236198.2013.854779
4. A. S. Al-Ghassani and Z. AlSharawi, *The effect of maps permutation on the global attractor of a periodic Beverton–Holt model*, Applied Mathematics and Computation 370 (2020), 124905; first online 2019-12-02. https://doi.org/10.1016/j.amc.2019.124905
