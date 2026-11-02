# An exact one-moment limit on eccentricity inference from double eclipses

## Finding
Consider a geometrically selected ensemble of planets for which **both** the primary transit and the secondary occultation are present. Under the idealized conjunction approximation and isotropic viewing orientations defined below, the entire observed distribution of periapsis arguments depends on an arbitrarily heterogeneous intrinsic eccentricity/orbital-scale distribution through **one** weighted mean eccentricity. In particular, write
\[
W=\frac{\eta}{1-e^2},\qquad M_0=\mathbb E[W],\qquad M_1=\mathbb E[eW],\qquad \varepsilon=\frac{M_1}{M_0}.
\]
For \(\omega\in[0,2\pi)\) and the event \(B\) that both eclipses occur,
\[
\boxed{p(\omega\mid B)=\frac{1-\varepsilon|\sin\omega|}{2\pi-4\varepsilon}},\qquad
\boxed{\mathbb P(B\mid T)=1-\frac{2\varepsilon}{\pi}},
\]
where \(T\) is the event of a primary transit. Every sine Fourier coefficient and every odd cosine Fourier coefficient of this density is zero; for each integer \(k\ge1\),
\[
\boxed{\mathbb E[\cos(2k\omega)\mid B]=\frac{2\varepsilon}{(4k^2-1)(\pi-2\varepsilon)}}.
\]
Conversely, the first even Fourier coefficient \(m=\mathbb E[\cos(2\omega)\mid B]\) uniquely determines the weighted eccentricity,
\[
\boxed{\varepsilon=\frac{3\pi m}{2(1+3m)}}.
\]
This is **identification of one weighted moment, not of the eccentricity distribution**. Distinct underlying eccentricity laws having the same \(\varepsilon\) have exactly the same conditioned periapsis law and the same fraction of transiting systems that also undergo an occultation.

## Assumptions and scope
A planet has intrinsic eccentricity \(0<e<1\), geometric scale \(\eta=(R_\star+R_p)/a>0\), and random periapsis argument \(\omega\), uniform on \([0,2\pi)\) independently of \((e,\eta)\). The viewing variable \(u=|\cos i|\) is independently uniform on \([0,1]\). The joint law of \((e,\eta)\) is arbitrary, including discrete or continuous heterogeneity, subject to \(0<\eta<1-e\) almost surely. This **unsaturated geometry** condition keeps both conjunction thresholds strictly below one. The adopted ideal conjunction geometry declares a primary transit and secondary occultation respectively when
\[
T:\;u\le\frac{\eta(1+e\sin\omega)}{1-e^2},\qquad
E:\;u\le\frac{\eta(1-e\sin\omega)}{1-e^2}.
\]
These are the standard thin-chord geometric criteria using the conjunction anomalies \(\pi/2-\omega\) and \(3\pi/2-\omega\). The result concerns geometrical event occurrence, not photometric eclipse detection or a complete orbital-light-curve model. All expectations are taken under the intrinsic ensemble law; \(M_0>0\) and \(0<\varepsilon<1\).

## Proof
**Nested orientation intervals.** Conditional on \((e,\eta,\omega)\), both events depend on the same \(u\). Their intersection has probability equal to the smaller threshold, not the product of individual event probabilities. Thus
\[
\mathbb P(B\mid e,\eta,\omega)=\frac{\eta}{1-e^2}(1-e|\sin\omega|)=W(1-e|\sin\omega|).
\]
The given bound \(\eta<1-e\) implies \(W(1+e)<1\), validating the probability formula without truncation.

**Exact averaging.** Independence and uniformity of \(\omega\) give \(\mathbb P(B\mid\omega)=M_0-M_1|\sin\omega|\). Since \(\int_0^{2\pi}|\sin\omega|\,d\omega=4\),
\[
\mathbb P(B)=M_0-\frac{2}{\pi}M_1,
\qquad \mathbb P(T)=M_0
\]
(the latter uses the zero mean of \(\sin\omega\)). Bayes' rule therefore gives the asserted conditioned density and conditional secondary-event probability. All integrals are finite because \(0<W<1\).

**Complete angular spectrum.** The conditional density is even and \(\pi\)-periodic. Consequently, all sine and odd cosine Fourier coefficients vanish. For each \(k\ge1\), elementary product-to-sum integration gives
\[
\int_0^{2\pi}|\sin\omega|\cos(2k\omega)\,d\omega=-\frac4{4k^2-1}.
\]
Substituting into the density proves the even Fourier formula. For \(k=1\), solve the strictly increasing map \(m=2\varepsilon/[3(\pi-2\varepsilon)]\) to obtain the inverse formula, valid for \(0<\varepsilon<1\).

**Nonidentifiability witness.** Fix \(\eta=1/10\). Compare a population where \(e=1/2\) surely with a population where \(e=1/4\) with probability \(15/22\) and \(e=3/4\) with probability \(7/22\). Both satisfy the unsaturated constraint and have \(\varepsilon=1/2\), as verified exactly from the weighted integrals. They are distinct intrinsic eccentricity distributions, yet the complete conditioned \(\omega\) laws and conditional eclipse frequencies coincide. The absolute transit probabilities are different—\(2/15\) versus \(8/55\)—so the result does not assert indistinguishability when such additional data are available. This proves the claimed one-moment identification boundary.

## Verification
The standalone standard-library Python file `check.py` at the same directory level checks the rational two-population witness, derives the selected weighted mean independently from the data arrays, numerically integrates the posterior density and its first six even harmonics, checks zero sine/odd-harmonic integrals, verifies the inverse formula, and compares the direct minimum-of-thresholds joint-event integral against the closed formula for five rational discrete ensembles. It passed on the actual packaged file prior to inclusion. Numerical quadrature is a cross-check; the proof above is analytic for arbitrary probability measures.

## Relationship to prior work
Kane and von Braun (arXiv:0908.0519, 2009), especially equations (1)–(3) and Section 3, derive the primary/secondary event geometry at fixed eccentricity and periapsis angle. Those formulas are the known starting point here; the existence of secondary eclipse selection is not claimed as new. Kipping (arXiv:1408.1393, 2014), Sections 2–3, develops Bayesian selection and a periapsis prior for transit-selected planets, but not the simultaneous-transit-and-occultation ensemble. The present result concerns the **heterogeneous double-event angular posterior**, its complete harmonic collapse onto one weighted mean, and the resulting identifiability limit. These are not asserted to be novel as a general fact about arbitrary binary selection kernels; a broader posterior-selection theorem could imply them. No equivalent source was identified in the targeted comparisons.

## Limitations
The conjunction impact-parameter approximation assumes fixed apsidal geometry, no orbital precession across events, isotropic inclination, and orientation-independent intrinsic parameters. Radii, detectability, limb-darkening, observation windows, and instrumental selection are excluded. If \(\eta\ge1-e\), probability saturation can destroy the one-moment closure. If the periapsis prior is not uniform or depends on orbital parameters, it also need not hold. At \(e=0\) the argument of periapsis is physically undefined; the statement assumes positive eccentricity. Recovering a weighted mean does not recover the intrinsic eccentricity distribution, nor even its unweighted mean. Absolute transit/occultation counts may carry additional information unavailable from the conditioned angular law alone. This is a mathematical selection model, not an empirical population estimate.

## References
- S. R. Kane and K. von Braun, *Exoplanetary Transit Constraints Based upon Secondary Eclipse Observations*, arXiv:0908.0519v1 (public 2009-08-04), https://arxiv.org/abs/0908.0519 ; published in PASP (2009).
- D. M. Kipping, *Bayesian priors for the eccentricity of transiting planets*, arXiv:1408.1393v1 (public 2014-08-06), https://arxiv.org/abs/1408.1393 ; MNRAS 444 (2014), 2263–2269.
