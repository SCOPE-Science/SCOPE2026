# An exact temperature-contrast bifurcation for two-power Wien spectra

## Finding
Consider the dimensionless two-component radiative spectrum
\[
 S(x)=A x^3e^{-x}+B x^4 e^{-x/r},\qquad x>0,\quad A,B>0,\quad r>1.
\]
A sharp, universal temperature-contrast threshold separates spectra with one peak from those capable of having two. Specifically, let \(r_*\) be the unique real root greater than one of
\[
 28r^4-120r^3+168r^2-92r+15=0,
 \qquad r_*=2.1566408087322\ldots.
\]
For \(1<r\le r_*\), the spectrum has exactly one strict local maximum for every positive component-strength ratio. For \(r>r_*\), define
\[
 R_r(x)=\frac{r(x-3)}{x(4r-x)}e^{-(r-1)x/r},\quad 3<x<4r,
\]
and let \(x_-(r)<x_+(r)\) be the two roots in \((3,4r)\) of
\[
 \frac{1}{x-3}-\frac1x+\frac{1}{4r-x}-\frac{r-1}{r}=0.
\]
**There are exactly two strict local maxima separated by a strict local minimum if and only if**
\[
 \boxed{R_r(x_+(r))<B/A<R_r(x_-(r)).}
\]
Outside this strict strength-ratio window there is exactly one strict local maximum. At its two boundary strengths, the spectrum also has a stationary, nonextremal shoulder. At \(r=r_*\) and the unique critical strength \(B/A=R_{r_*}(x_*)=0.0164160061067\ldots\), the sole maximum is quartically flat, where \(x_*=5.6395948274587\ldots\).

The birth of the two-peak parameter window has an exact fractional-power law. With
\[
 k=\frac1{r_*^2}+\frac4{(4r_*-x_*)^2},\qquad
 h_2=\frac2{(x_*-3)^3}-\frac2{x_*^3}+\frac2{(4r_*-x_*)^3},
\]
and \(K=\frac{4k}{3}\sqrt{2k/h_2}=2.4517450659\ldots\),
\[
 \boxed{\log\frac{R_r(x_-(r))}{R_r(x_+(r))}
       =K(r-r_*)^{3/2}+o((r-r_*)^{3/2})\qquad(r\downarrow r_*).}
\]

## Assumptions and scope
The spectrum is an exact mathematical model of a **two-power Wien approximation** to two thermal radiative components: one with emissivity constant over the modelled band and the other with emissivity proportional to frequency. Here \(x=h\nu/(k_{\mathrm B}T_{\mathrm c})\), and \(r=T_{\mathrm h}/T_{\mathrm c}>1\). The two amplitudes \(A,B\) incorporate material emissivity and geometric normalization. The powers three and four arise from frequency-domain Wien radiance \(\nu^3e^{-h\nu/(k_{\mathrm B}T)}\) multiplied respectively by emissivity powers zero and one. All results concern the entire mathematical half-line \(x>0\) with these pure powers and are not statements about exact Planck functions, bounded emissivities outside a fitted band, or finite-band instrumental detectability.

## Proof
Differentiation and factorization give, on \(3<x<4r\),
\[
 S'(x)=x^3e^{-x/r}\left(4-\frac xr\right)
 \bigl(B-A R_r(x)\bigr).
\]
For \(0<x\le3\), both summand derivatives are nonnegative and their sum is positive, whereas for \(x\ge4r\) the sum is negative. Thus every positive critical point lies in \((3,4r)\), and its type is controlled by a crossing of the horizontal level \(B/A\) by \(R_r\).

Put \(H_r(x)=\partial_x\log R_r(x)\). Direct calculation gives
\[
 H_r(x)=\frac1{x-3}-\frac1x+\frac1{4r-x}-\frac{r-1}{r},
\quad
 \partial_x^2 H_r(x)=\frac2{(x-3)^3}-\frac2{x^3}+\frac2{(4r-x)^3}>0.
\]
The inequality is strict because \(0<x-3<x\). Consequently \(H_r\) is strictly convex, tends to \(+\infty\) at both endpoints, and has one strict interior minimum. At fixed admissible \(x\),
\[
 \partial_r H_r(x)=-\frac1{r^2}-\frac4{(4r-x)^2}<0.
\]
At \(r=1\), \(H_1>0\) throughout \((3,4)\); for sufficiently large \(r\), \(H_r(5)<0\). The minimum therefore crosses zero exactly once as \(r\) grows; the zero is characterized by simultaneous equations \(H_r(x)=0\) and \(\partial_x H_r(x)=0\). For completeness, clearing the strictly positive denominator \(r x(x-3)(4r-x)\) in \(H_r\) yields
\[
 N_r(x)=-4r^2x^2+12r^2x+12r^2+rx^3+2rx^2-18rx-x^3+3x^2.
\]
Its discriminant calculation, expressed as a resultant, is
\[
 \operatorname{Res}_x(N_r,\partial_x N_r)
 =-12r^2(r-1)(4r-3)^2
  (28r^4-120r^3+168r^2-92r+15).
\]
After setting \(r=1+t\), the remaining quartic becomes \(28t^4-8t^3-24t^2-4t-1\), which has exactly one positive root by Descartes' sign rule and existence by opposite signs at zero and infinity. This proves the uniqueness and exact algebraic characterization of \(r_*\).

When \(r<r_*\), \(H_r>0\) and \(R_r\) strictly increases from zero to infinity, hence it crosses every positive level once. At \(r=r_*\), it remains strictly increasing, with only a single horizontal tangent at \(x_*\). At \(r>r_*\), the strictly convex function \(H_r\) has exactly two simple zeros \(x_-<x_+\) and sign sequence positive, negative, positive. Thus \(R_r\) has precisely one local maximum followed by one local minimum. Counting crossings of the level \(B/A\), together with the sign of \(S'\), establishes the claimed necessary and sufficient bimodality criterion and boundary shoulders. At the critical equality \((r_*,R_{r_*}(x_*))\), the quadratic vanishing of \(H_{r_*}\) causes a cubic zero of \(B-A R_{r_*}(x)\); the sign of \(S'\) changes from positive to negative and the maximum has fourth-order leading contact.

For the onset exponent, set \(\varepsilon=r-r_*>0\) and \(y=x-x_*\). The Taylor expansion, uniformly for \(y=O(\sqrt\varepsilon)\), is
\[
 H_{r_*+\varepsilon}(x_*+y)
  =-k\varepsilon+\frac{h_2}{2}y^2
   +O(\varepsilon|y|+|y|^3+\varepsilon^2).
\]
The two roots satisfy \(y_\pm=\pm\sqrt{2k/h_2}\,\sqrt\varepsilon+O(\varepsilon)\). Integrating \(-H_r\) between these roots gives the stated positive \(\frac{4k}{3}\sqrt{2k/h_2}\varepsilon^{3/2}+o(\varepsilon^{3/2})\) logarithmic interval width.

## Verification
Run `python verify.py` with Python, SymPy, NumPy, and SciPy installed. Its tests independently differentiate the model, check log-derivative identities, factor the resultant, verify the root polynomial, solve for critical points across representative parameter families, evaluate spectral derivatives, and sample the onset exponent. The script prints `PASS` with 85 diagnostic test groups; symbolic algebra establishes the displayed polynomial identity. The proof above, rather than the finite tests, establishes the universal quantifiers. All files needed to reproduce these checks are embedded with this result.

## Relationship to prior work
Two-temperature debris-disk spectral modelling and emissivity-power corrections are established in Kennedy and Wyatt (2014), especially their spectral-energy-distribution section; the article does not derive the peak-count threshold for different emissivity powers. Došlá (2009) establishes general mode-count criteria for mixtures and treats equal-shape/different-rate and equal-rate/different-shape gamma families. Those general methods motivate the analysis, but the explicit two-power mixed-shape/different-rate threshold and its sharp opening coefficient are not stated in the examined cases. The standard Wien formula and the usual single-component peak positions are not claimed as discoveries.

## Limitations
This work gives a phase diagram of an ideal Wien approximation, not a data fit or a statement about full Planck emission or astrophysical spatial structure. The two powers three and four and strictly positive amplitudes are essential to the specific quartic threshold. More general emissivity exponents, physically bounded emissivity turnovers, and the consequences of detector passbands remain unproved. Historical priority is not asserted as certain; different mathematical formulations of gamma-mixture modes may contain equivalent results not located in the examined literature.

## References
- G. M. Kennedy and M. C. Wyatt, “Do Two Temperature Debris Disks Have Multiple Belts?”, first public arXiv version 18 August 2014, arXiv:1408.4116v1, https://arxiv.org/abs/1408.4116 . Sections 3–5 describe modified blackbody spectra and emissivity-power choices.
- Š. Došlá, “Conditions for Bimodality and Multimodality of a Mixture of Two Unimodal Densities,” *Kybernetika* 45 (2009), 279–292, https://www.kybernetika.cz/content/2009/2/279 . Its gamma mixture cases and the discussion of differing shapes and rates are compared.
