# A sharp overtide-energy frontier for double-high tidal crests

## Finding
Consider a unit-amplitude semidiurnal tidal component with two phase-opposed, phase-locked overtides,
\[
\eta_{a,b}(\theta)=\cos\theta-a\cos(2\theta)-b\cos(3\theta),\qquad a,b\geq0,
\]
and constrain their combined mean-square strength by \(a^2+b^2=E^2\), with \(E\geq0\). The temporal average of the squared overtide signal is \(E^2/2\), because the two harmonic frequencies are orthogonal. Define the **central-crest splitting excess** by
\[
\mathcal P(E)=\max_{\substack{a,b\geq0\\a^2+b^2=E^2}}\ \max_{\theta\in[-\pi,\pi]}\bigl[\eta_{a,b}(\theta)-\eta_{a,b}(0)\bigr].
\]
This quantity is zero when the nominal semidiurnal crest at \(\theta=0\) cannot be overtopped and is positive when a higher pair of symmetric crests flanks it.

**Theorem (sharp onset, unique mixed optimum, and separation law).** Define
\[
R(x)=\sqrt{4(1+x)^2+(2x+1)^4},\qquad G(x)=(1-x)R(x).
\]
Then \(\mathcal P(E)=0\) for every \(0\leq E\leq1/\sqrt{97}\). If \(E>1/\sqrt{97}\), there is exactly one \(x_E\in(0,1)\) satisfying
\[
1+E G'(x_E)=0.
\]
It determines the unique optimal overtide allocation
\[
a_E=\frac{2E(1+x_E)}{R(x_E)},\qquad
b_E=\frac{E(2x_E+1)^2}{R(x_E)},
\]
which has \(a_E,b_E>0\). The exact maximal excess is
\[
\boxed{\mathcal P(E)=E G(x_E)-(1-x_E)>0.}
\]
The two global high-water maxima occur at \(\theta=\pm\arccos x_E\); the nominal crest becomes a strict local minimum. As \(E\) increases, \(x_E\) decreases strictly, so the peak-to-peak angular separation \(2\arccos x_E\) grows strictly. Its limiting cosine is the unique positive root of
\[
48x^4+48x^3+8x^2-4x-3=0,
\]
namely \(x_\infty\approx0.3717081011\). At \(E\downarrow1/\sqrt{97}\), the unique optimal positive-excess allocation approaches the proportions \(a:b=4:9\).

These statements concern the full tidal cycle, not merely an assumed near-crest window. Below onset every admissible allocation attains the common value zero; uniqueness is asserted only above onset.

## Assumptions and scope
The phases of both overtides are fixed at \(\pi\) relative to the nominal primary crest, so the modeled elevation is even in time. The basic semidiurnal amplitude is normalized to one; restoring physical amplitude multiplies every vertical excess by that amplitude. The free amplitudes \(a,b\) are nonnegative. Their squared sum is the natural contribution of these two mutually orthogonal components to twice the mean-square sea-level variance. The objective compares the highest water level in one period with the level at the nominal semidiurnal crest. No external forcing dynamics, phase optimization, measurement error, or constraint on attainable coastal harmonic amplitudes is assumed.

## Proof
Put \(x=\cos\theta\in[-1,1]\). The Chebyshev identities give
\[
\begin{aligned}
\eta_{a,b}(\theta)-\eta_{a,b}(0)
&=(1-x)\left[-1+2a(1+x)+b(2x+1)^2\right].
\end{aligned}
\]
For fixed \(x\), the positive vector \((2(1+x),(2x+1)^2)\) has Euclidean norm \(R(x)\). Cauchy–Schwarz with \(a^2+b^2=E^2\) therefore yields the sharp bound
\[
F_E(x):=(1-x)(E R(x)-1)=E G(x)-(1-x),
\]
with equality, for \(x\in(0,1)\) and \(E>0\), only at \((a,b)=E(2(1+x),(2x+1)^2)/R(x)\). Maximizing the original objective is equivalent to maximizing \(F_E(x)\) over \([-1,1]\), because both maximizations concern compact sets and the maximizing amplitude vector is feasible.

**Removing the negative-cosine half.** For \(u\in[0,1]\), direct expansion gives
\[
5-G(-u)^2=u\,q(u),\qquad q(u)=6-u-8u^2+20u^3-16u^5.
\]
In degree-five Bernstein form, \(q\) has the strictly positive coefficients
\[
6,\quad\frac{29}{5},\quad\frac{24}{5},\quad5,\quad\frac{42}{5},\quad1.
\]
Thus \(G(x)\leq\sqrt5=G(0)\) for \(-1\leq x\leq0\), while \(1-x\geq1\), implying \(F_E(x)\leq F_E(0)\). Any positive-excess global maximizer must therefore lie in \((0,1)\), because \(F_E'(0)>0\).

**Strict concavity and threshold.** On \([0,1]\) the exact identities are
\[
G'(0)=\frac3{\sqrt5},\qquad G'(1)=-\sqrt{97},
\]
and
\[
G''(x)=-\frac{4\,p(x)}{R(x)^3},
\]
where
\[
\begin{aligned}
p(x)={}&384x^7+1152x^6+1584x^5+1392x^4\\
&+816x^3+264x^2+33x+1.
\end{aligned}
\]
Every coefficient of \(p\) is positive, so \(F_E''(x)=E G''(x)<0\) on \([0,1]\) whenever \(E>0\). Furthermore,
\[
F_E'(0)=1+\frac{3E}{\sqrt5}>0,\qquad F_E'(1)=1-E\sqrt{97}.
\]
If \(E\leq1/\sqrt{97}\), the strictly decreasing derivative stays nonnegative and the maximum occurs at \(x=1\), where \(F_E(1)=0\). This also holds at \(E=0\) by inspection. If \(E>1/\sqrt{97}\), the derivative changes sign exactly once, at \(x_E\), so the maximum there is positive, strict, and unique. Equality in Cauchy–Schwarz now gives precisely the stated positive amplitude pair. Since \(x_E\in(0,1)\), the two times \(\pm\arccos x_E\) are the only global maximizing phases modulo the period.

For these optimal amplitudes, positive excess forces \(4a_E+9b_E>1\): otherwise \(2a_E(1+x)+b_E(2x+1)^2\leq4a_E+9b_E\leq1\) for all \(x\in[0,1]\), contradicting \(F_E(x_E)>0\). Hence
\[
\eta_{a_E,b_E}''(0)=-1+4a_E+9b_E>0,
\]
proving that the nominal crest has split into a central local minimum flanked by global maxima.

By implicit differentiation of \(1+E G'(x_E)=0\),
\[
\frac{dx_E}{dE}=-\frac{G'(x_E)}{E G''(x_E)}<0.
\]
The monotone limit as \(E\to\infty\) is the unique zero of \(G'\) on \((0,1)\); multiplying \(G'\) by its positive denominator gives the stated quartic. Its uniqueness follows from strict negativity of \(G''\). The limit near onset is \(x_E\to1\), and the optimal amplitude direction there tends to \((4,9)/\sqrt{97}\).

## Verification
A standalone script, `check.py`, reconstructs the Chebyshev height-difference factorization, the exact second-derivative polynomial identity, the degree-five Bernstein certificate, and both endpoint derivatives with symbolic algebra. It additionally checks the exact optimizer \(E=5/6\), \(a=1/2\), \(b=2/3\), \(x_E=1/2\), with \(\mathcal P(E)=19/12\). Numerical grids over seven energy values corroborate, but do not prove, the global statements.

The separate-overtide thresholds are \(a>1/4\) for a phase-opposed second harmonic alone and \(b>1/9\) for a phase-opposed third harmonic alone. Yet the simultaneous choice \(a=1/20\), \(b=1/10\) lies below both individual thresholds and has symmetric high crests at \(\cos\theta=(\sqrt{157}-1)/12\), exceeding its central level by exactly
\[
\frac{157\sqrt{157}-1963}{2160}>0.
\]
This shows that two individually subthreshold overtides can jointly split the crest. It is a distinct illustrative allocation, not the maximizer at its energy.

## Relationship to prior work
The phenomenon of double high water and individual-harmonic thresholds is classical. Song et al. (2016) analyze the phase-dependent critical strength of the single \(M_4\) or \(M_6\) overtide and demonstrate enhanced splitting when both are present. Their full text explicitly leaves the combined critical condition unresolved in general; it does not optimize central-crest splitting over a fixed sum of overtide squared amplitudes. Bowers et al. (2013) model a different mechanism involving seiches. Byrne et al. (2017) revisit a higher-harmonic threshold and its phase dependence, without stating this two-overtide energy-constrained extremum. The theorem above instead gives the complete constrained optimum in the *restricted, phase-locked* three-harmonic class and does not purport to solve the arbitrary-phase combined-harmonic problem.

## Limitations
The extremum is an exact statement about a truncated, phase-locked harmonic reconstruction, not a forecast of coastal flooding. It does not assert that coastal dynamics can freely choose the optimal \(a,b\) or that the relative phases of both overtides are normally \(\pi\). Additional constituents, currents, nonstationary tides and wind-driven surges can move or erase the extrema. Large values of \(E\) may be physically atypical. The result optimizes crest *height difference*, not navigation duration, current reversal, an extreme-value probability, or a full physical-energy budget. Historical priority beyond the inspected sources is not independently certified.

## References
1. D. Song, Y. Yan, W. Wu, X. Diao, Y. Ding and X. Bao, “Tidal distortion caused by the resonance of sexta-diurnal tides in a micromesotidal embayment,” *J. Geophys. Res. Oceans* 121 (2016), 7599–7618. First published 2016-09-30. DOI: https://doi.org/10.1002/2016JC012039.
2. D. G. Bowers, R. G. Macdonald, D. McKee, W. A. M. Nimmo-Smith and G. W. Graham, “On the formation of tide-produced seiches and double high waters in coastal seas,” *Estuarine, Coastal and Shelf Science* 134 (2013), 108–116. DOI: https://doi.org/10.1016/j.ecss.2013.09.014.
3. H. A. M. Byrne, J. A. M. Green and D. G. Bowers, “The double high tide at Port Ellen: Doodson's criterion revisited,” *Ocean Science* 13 (2017), 599–607. DOI: https://doi.org/10.5194/os-13-599-2017.
