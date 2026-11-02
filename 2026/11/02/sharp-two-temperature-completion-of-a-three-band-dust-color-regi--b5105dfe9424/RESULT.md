# Sharp two-temperature completion of a three-band dust-color region

## Finding

Fix a positive base frequency \(\nu\) and a *known common* real emissivity index \(\beta\). Suppose an optically thin thermal spectrum is a finite sum of positive modified-blackbody components, each with positive finite temperature, and the emission is measured monochromatically at \(\nu\), \(2\nu\), and \(4\nu\). Write the positive intensities as \(I_1,I_2,I_4\), and form the dimensionless colors
\[
 U=\frac{I_2}{2^{\beta+3}I_1},\qquad
 V=\frac{I_4}{4^{\beta+3}I_1},\qquad
 f(u)=\frac{u^3}{1-2u+2u^2}.
\]

**Complete feasible-region theorem.** A positive intensity triple is realizable by any finite nonempty collection of such components if and only if
\[
 0<U<\frac12,\qquad f(U)\le V<\frac U2.
\]
The lower equality holds precisely when all positive-weight components have the same temperature; equivalently it is exactly the one-temperature locus. Every strict interior point \(f(U)<V<U/2\) is realized *exactly* by two components of distinct, positive finite temperatures and strictly positive amplitudes. No amount of finite-temperature mixing can reach the upper line, but this upper line is sharp as a limiting bound. Thus one temperature is enough precisely on the lower boundary; two distinct temperatures are necessary and sufficient everywhere else in the feasible region.

**Minimal observations.** Two monochromatic intensities at \(\nu,2\nu\), with a free positive overall amplitude, can never distinguish a temperature mixture from a single temperature: every feasible two-band ratio has an exact single-temperature realization. Three bands are therefore the minimum required for the indicated noiseless, fixed-index distinction.

A related emissivity-independent obstruction is \(I_1I_4/I_2^2>1\): such a triple cannot arise from a single modified blackbody with *any* common emissivity index. This obstruction can occur in a genuine positive two-temperature mixture, even for \(\beta=2\). It is not a necessary condition for mixing.

## Assumptions and scope

Let \(m\in\{1,2,4\}\). Assume explicitly
\[
 I_m=(m\nu)^{\beta+3}\sum_{j=1}^n
 \frac{c_j}{\exp(mh\nu/(k_{\mathrm B}T_j))-1},
 \qquad n\ge1,\quad c_j>0,\quad 0<T_j<\infty.
\]
Here \(h,k_{\mathrm B},\nu\) are fixed positive constants, \(\beta\in\mathbb R\) is specified and identical for every component, and the coefficients \(c_j\) are unrestricted positive optical-depth or mass-related amplitude factors. Repeated temperatures are allowed. These are *monochromatic flux densities per unit frequency*, not fluxes integrated over filters. All measurements are exact and background-subtracted. There is no self-absorption, optically thick emission, instrumental noise, foreground contamination, or variable emissivity across components. No physical temperature or amplitude bounds beyond strict positivity and finiteness are imposed.

## Proof

**Step 1: One-component color curve.** For a component of temperature \(T\), put
\[
 r=\exp\!\left(\frac{h\nu}{k_{\mathrm B}T}\right)>1,
 \qquad u=\frac1{r+1}\in\left(0,\frac12\right).
\]
Its intensity normalized by the first band has second-band color \(u\) and fourth-band color
\[
 \frac{r-1}{r^4-1}
 =\frac1{(r+1)(r^2+1)}
 =\frac{u^3}{1-2u+2u^2}=f(u).
\]
The map \(T\mapsto u\) is strictly increasing from \((0,\infty)\) onto \((0,1/2)\); indeed \(r=1/u-1\) recovers the unique temperature.

**Step 2: Every mixture is an exact barycenter.** Put \(r_j=\exp(h\nu/(k_{\mathrm B}T_j))\), \(u_j=1/(r_j+1)\), and
\[
 w_j=\frac{c_j/(r_j-1)}{\sum_{i=1}^n c_i/(r_i-1)}.
\]
Then \(w_j>0\), \(\sum_j w_j=1\), and direct cancellation of the common power-law factor gives
\[
 U=\sum_j w_j u_j,\qquad V=\sum_j w_j f(u_j).
\]
Thus the normalized color pair is a positive convex combination of points on the one-temperature curve; no statistical or numerical approximation is involved.

**Step 3: Strict convexity and two sharp boundaries.** Direct differentiation gives
\[
 f''(u)=\frac{2u(2u^2-6u+3)}{(1-2u+2u^2)^3}>0
 \quad\text{for }0<u<\tfrac12.
\]
The quadratic factor is decreasing on the interval and remains at least \(1/2\) there. Hence strict Jensen convexity yields \(V\ge f(U)\), with equality if and only if all \(u_j\), hence all \(T_j\), are identical. Also,
\[
 \frac u2-f(u)=\frac{u(1-2u)}{2(1-2u+2u^2)}>0
 \quad\text{for }0<u<\tfrac12.
\]
Averaging proves \(V<U/2\) strictly. Strict positivity of the component weights gives \(0<U<1/2\). This proves the necessary inequalities and all equality statements.

**Step 4: Every interior point admits two finite temperatures.** Fix any \(0<U<1/2\) and \(f(U)<V<U/2\). Set \(d=\min\{U,1/2-U\}>0\). For \(0<t<d\), put \(a=t\), \(b=1/2-t\), and
\[
 \lambda(t)=\frac{b-U}{b-a}\in(0,1),\qquad
 H(t)=\lambda(t)f(a)+(1-\lambda(t))f(b).
\]
The two-color barycenter has first coordinate \(U\). The function \(H\) is continuous, and the endpoint limits are
\[
 \lim_{t\downarrow0}H(t)=\frac U2,
 \qquad \lim_{t\uparrow d}H(t)=f(U).
\]
For the second limit, one or both endpoints \(a,b\) approach \(U\), and the corresponding barycentric weight tends to one. The intermediate-value theorem therefore provides a \(t\in(0,d)\) with \(H(t)=V\). Define \(r_a=1/a-1>1\), \(r_b=1/b-1>1\),
\[
 T_a=\frac{h\nu}{k_{\mathrm B}\log r_a},\qquad
 T_b=\frac{h\nu}{k_{\mathrm B}\log r_b}.
\]
These temperatures are finite, positive, and distinct since \(a<b\). For the target \(I_1>0\), let \(S=I_1/\nu^{\beta+3}\) and choose
\[
 c_a=S\lambda(t)(r_a-1),\qquad
 c_b=S(1-\lambda(t))(r_b-1).
\]
Both amplitudes are positive and reproduce the prescribed \(I_1\) and exactly the two normalized ratios \(U,V\). The lower boundary is realized by the unique temperature with \(u=U\) and a matching single amplitude; the upper line remains unattainable but is approached as \(t\downarrow0\). This proves sufficiency, two-temperature minimality, and the sharp upper endpoint.

**Step 5: The two-band impossibility.** For any finite mixture its two-band color \(U\) lies in \((0,1/2)\). Taking \(r=1/U-1\), \(T=h\nu/(k_{\mathrm B}\log r)\), and choosing the unique positive amplitude matching \(I_1\) gives a single-temperature spectrum with the same exact \(I_1,I_2\). Thus no two-band rule can separate these model classes.

**Step 6: An exact three-band mixing witness independent of \(\beta\).** For a single temperature,
\[
 \frac{I_1 I_4}{I_2^2}=\frac{f(U)}{U^2}
 =\frac{U}{1-2U+2U^2}<1.
\]
The power-law emissivity cancels because the frequencies are in geometric progression. Take two components with \(r_1=16\), \(r_2=3/2\), \(c_1=1\), \(c_2=1/20\), and any common \(\beta\), including \(\beta=2\). Then exact arithmetic gives
\[
 U=\frac{112}{425},\qquad
 V=\frac{104986}{1419925},\qquad
 \frac{I_1I_4}{I_2^2}=\frac{3187075}{2993536}>1.
\]
This cannot be a single modified-blackbody spectrum at any \(\beta\), while satisfying the strict feasible-region inequalities for the fixed common \(\beta\). The stronger three-band region test, however, assumes \(\beta\) was specified beforehand.

## Verification

The accompanying `verify.py` is standalone apart from Python 3 and SymPy. Run `python verify.py`. It checks the exact curvature and endpoint identities symbolically, tests the strict and equality cases for 1,200 rationally parametrized component pairs, reconstructs 400 interior target points numerically using the stated two-temperature chord construction, and confirms the three exact rational witness identities. A run of the embedded version produced 4,008 passing assertions. These finite assertions provide reproducibility and stress tests, **not** a replacement for the universal proof in Steps 1–5.

## Relationship to prior work

The one- and two-modified-blackbody modeling framework is established in Reach et al. (1995), Finkbeiner, Davis, and Schlegel (1999), and Meisner and Finkbeiner (2014). In particular, the 1995 paper explicitly fits two positive \(\beta=2\) thermal components, and Shetty et al. (2009, §§III.1.1 and IV.2) already investigate two-temperature mixing and estimate temperature from three flux ratios. The Planck Collaboration (2011) also uses fixed-index isothermal color-color loci with nongeometric photometric frequencies. The broad ideas of color-color diagrams, convex combinations, and three-flux inference are **not asserted as new**.

The assessed claim is specifically the *exact global image* of all finite common-index thermal mixtures at the three geometric frequencies, its closed-form rational lower boundary and sharp unattained upper boundary, its characterization of one versus two distinct temperatures, and the constructive fact that no third component enlarges the feasible region. The examined primary texts concern empirical spectral fitting and flux-ratio estimation; their stated results do not imply this complete necessary-and-sufficient region together with its two-component construction. A published equivalent exact inequality, or a stronger convex-geometric theorem explicitly specialized to this curve, would supersede the originality claim; historical priority has not been independently certified.

## Limitations

The emissivity index must be known and common to all components for the complete inequalities. When it is free, the normalized \(U,V\) cannot be formed without an additional parameter choice. Filters of nonzero bandwidth do not generally preserve the algebraic curve. A failure of these inequalities could alternatively indicate incorrect emissivity, measurement error, nonthermal emission, opacity, or calibration differences; it does not by itself establish a particular physical cause. Even when two temperatures suffice to fit three exact intensities, those individual temperatures and amplitudes are generally not identified uniquely. The sharp upper boundary requires temperatures approaching zero and infinity and is not reached under finite positive temperature bounds. All claims concern the exact idealized spectral model, not astrophysical data accuracy.

## References

1. W. T. Reach et al., *Far-Infrared Spectral Observations of the Galaxy by COBE*, arXiv:astro-ph/9504056v1, first public 1995-04-18. https://arxiv.org/abs/astro-ph/9504056
2. D. P. Finkbeiner, M. Davis, and D. J. Schlegel, *Extrapolation of Galactic Dust Emission at 100 Microns to CMBR Frequencies Using FIRAS*, arXiv:astro-ph/9905128, first public 1999-05-11. https://arxiv.org/abs/astro-ph/9905128
3. R. Shetty et al., *The Effect of Line of Sight Temperature Variation and Noise on Dust Continuum Observations*, arXiv:0902.3477v1, first public 2009-02-20. https://arxiv.org/html/0902.3477v1
4. A. M. Meisner and D. P. Finkbeiner, *Modeling Thermal Dust Emission with Two Components: Application to the Planck HFI Maps*, arXiv:1410.7523, first public 2014-10-28. https://arxiv.org/abs/1410.7523
5. Planck Collaboration, *Planck early results. XXIII. The first all-sky survey of Galactic cold clumps*, Astronomy & Astrophysics 536 (2011), A23, §2.5 and Fig. 2. https://www.aanda.org/articles/aa/full_html/2011/12/aa16472-11/aa16472-11.html
