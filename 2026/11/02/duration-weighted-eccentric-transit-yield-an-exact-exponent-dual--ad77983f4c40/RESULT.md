# Duration-weighted eccentric transit yield: an exact exponent duality and critical logarithmic law

## Finding

For the geometrically selected, duration-power-weighted transit-yield functional defined below, the normalized eccentric-orbit yield obeys the exact exponent reflection

\[
Y_\alpha(e)=Y_{3-\alpha}(e),\qquad 0\le\alpha\le3.
\]

For each fixed \(0<e<1\), \(\log Y_\alpha(e)\) is strictly convex in the exponent. Thus the *unique* least-enhanced power-law response is \(\alpha=3/2\), despite the fact that its yield exceeds the circular-orbit normalization:

\[
D^{-1/4}<Y_{3/2}(e)<D^{-1},\qquad D=1-e^2.
\]

The exact correction to multiplying the separately averaged geometric transit probability by the \(3/2\)-power of mean relative duration is

\[
\frac{Y_{3/2}(e)}{D^{-1/4}}=\frac1{2\pi}\int_0^{2\pi}\frac{d\omega}{\sqrt{1+e\sin\omega}}>1.
\]

At \(e=1/2\), this factor is approximately \(1.054648614831467\); the fully phase-weighted yield is approximately \(1.133293690137242\), whereas the product-of-means proxy is approximately \(1.074569931823542\).

The high-eccentricity limit has a critical logarithmic branch precisely at the minimizing exponent:

\[
Y_{3/2}(e)\sim\frac{\sqrt2}{\pi}D^{-1/4}\log\left(\frac8{\sqrt D}\right)
\quad (e\uparrow1).
\]

More generally, define \(A(\alpha)=2^{1-\alpha}\Gamma(3/2-\alpha)/(\sqrt\pi\Gamma(2-\alpha))\). For each fixed \(0\le\alpha<3/2\),

\[
Y_\alpha(e)\sim A(\alpha)D^{\alpha/2-1},
\]

and for \(3/2<\alpha\le3\) the reflected formula applies, \(Y_\alpha=Y_{3-\alpha}\). The cases \(Y_0=Y_3=D^{-1}\) and \(Y_1=Y_2=D^{-1/2}\) are exact at all eccentricities.

## Assumptions and scope

Fix a Keplerian orbit with eccentricity \(e\in[0,1)\) and semimajor axis \(a\). Write \(R=R_\star+R_p\), \(\rho=R/a\), and require \(0<\rho<1-e\), so the geometric transit probability never saturates at one. Assume uniformly random argument of periastron \(\omega\in[0,2\pi)\) and isotropic orbital inclinations; ignore mutual selection effects, limb darkening, time-window gaps, correlated noise and finite-cadence selection. For the standard small-\(R/a\), constant-speed transit approximation, the transit probability at a given periastron phase is \(p_{\mathrm{tr}}=\rho(1+e\sin\omega)/(1-e^2)\). Given that a transit occurs, its normalized impact parameter \(b\in[0,1]\) is uniform, and its duration is proportional to

\[
\tau(e,\omega,b)=\sqrt{1-b^2}\,\frac{\sqrt{1-e^2}}{1+e\sin\omega}.
\]

An idealized detection-volume or selection *weight* is proportional to \(\tau^\alpha\), with exponent \(0\le\alpha\le3\). For \(\alpha=3/2\), this includes the textbook white-noise Euclidean volume scaling based on signal-to-noise proportional to the square root of transit duration. It is **not** a probability that can be substituted for a thresholded completeness curve without further assumptions. The yield \(Y_\alpha(e)\) is the inclination- and periastron-integrated transit weight divided by its eccentricity-zero counterpart at fixed \(\alpha\). This normalization is finite and positive because the impact factor is integrable.

With \(D=1-e^2\), \(X(\omega)=1+e\sin\omega\) and \(I_s(e)=(2\pi)^{-1}\int X(\omega)^s\,d\omega\), averaging the geometric factor \(X/D\) times duration factor \((\sqrt D/X)^\alpha\) gives

\[
Y_\alpha(e)=D^{\alpha/2-1}I_{1-\alpha}(e).
\]

The separate impact-parameter integral \(\int_0^1(1-b^2)^{\alpha/2}\,db\) is identical in numerator and denominator and cancels. All identities are statements about this model, including the domain \(0\le\alpha\le3\); no assertion is made for an arbitrary observational selection function.

## Proof

**1. Exact duality for phase moments.** For every real \(s\) and \(0<e<1\), choose the phase origin so that \(X=1+e\cos\theta\). Put \(A=1+e\), \(B=1-e\), so \(D=AB\). The tangent half-angle substitution gives

\[
I_s(e)=\frac1\pi\int_{-\infty}^{\infty}
\frac{(A+Bt^2)^s}{(1+t^2)^{s+1}}\,dt.
\]

Now substitute \(t=\sqrt{A/B}\,u\), followed by \(u=1/v\) separately on the positive and negative half-lines. All integrals are absolutely convergent since \(e<1\). This yields

\[
I_s(e)=D^{s+1/2}\frac1\pi\int_{-\infty}^{\infty}
\frac{(1+v^2)^s}{(A+Bv^2)^{s+1}}\,dv
=D^{s+1/2}I_{-s-1}(e).
\]

Putting \(s=1-\alpha\) in the yield formula gives

\[
Y_\alpha(e)=D^{\alpha/2-1+3/2-\alpha}I_{\alpha-2}(e)
=D^{(3-\alpha)/2-1}I_{1-(3-\alpha)}(e)
=Y_{3-\alpha}(e).
\]

**2. Global and unique minimum.** Differentiating under the integral is valid uniformly in each bounded exponent interval, since \(1-e\le X\le1+e\). If \(\mu_\alpha\) is the probability measure on phase with density proportional to \(X^{1-\alpha}\), direct logarithmic differentiation gives

\[
\frac{d^2}{d\alpha^2}\log Y_\alpha(e)
=\operatorname{Var}_{\mu_\alpha}(\log X)>0.
\]

The variance is strictly positive for every \(e>0\) because \(X\) is nonconstant and \(\mu_\alpha\) has positive density. Symmetry about \(3/2\) forces the derivative there to vanish. Strict convexity proves that this is the unique global minimum on \([0,3]\). At \(e=0\), the functional equals one for every exponent, so uniqueness is expressly excluded.

**3. Strict enhancement and comparison with a mean-duration proxy.** The moment identities \(I_0=I_1=1\), \(I_{-1}=D^{-1/2}\) yield the stated endpoint and intermediate exact values. At the minimizing exponent,

\[
Y_{3/2}(e)=D^{-1/4}I_{-1/2}(e).
\]

Because the map \(x\mapsto x^{-1/2}\) is strictly convex and \(\langle X\rangle=1\), Jensen's inequality yields \(I_{-1/2}(e)>1\) for \(e>0\). The strict upper bound \(Y_{3/2}<D^{-1}\) follows from strict convexity in \(\alpha\) and the equal values \(Y_0=Y_3=D^{-1}\). The population-mean *relative* transit duration conditioned on transit is \(\sqrt D\), since the transit-selected phase density is proportional to \(X\); multiplying \(D^{-1}\) by \((\sqrt D)^{3/2}\) gives the different proxy \(D^{-1/4}\). This shows exactly why averaging before applying a nonlinear power produces a smaller number.

**4. Small-eccentricity and critical high-eccentricity limits.** By the binomial expansion, uniform in phase for sufficiently small \(e\),

\[
I_s(e)=1+\frac{s(s-1)}4e^2+O_s(e^4),
\qquad
Y_\alpha(e)=1+\frac{\alpha^2-3\alpha+4}{4}e^2+O_\alpha(e^4).
\]

For fixed \(s>-1/2\), dominated convergence as \(e\uparrow1\) gives

\[
I_s(1)=\frac{2^s\Gamma(s+1/2)}{\sqrt\pi\Gamma(s+1)}.
\]

Taking \(s=1-\alpha\) proves the fixed-\(\alpha<3/2\) power law. The case \(\alpha>3/2\) follows by reflection. At the borderline, the standard complete-elliptic-integral representation

\[
I_{-1/2}(e)=\frac{2}{\pi\sqrt{1+e}}\,
K\!\left(\sqrt{\frac{2e}{1+e}}\right)
\]

and \(K(k)=\log(4/\sqrt{1-k^2})+o(1)\) as \(k\uparrow1\) yield the logarithmic law, since \(1-k^2=(1-e)/(1+e)=D/(1+e)^2\). For the generic fixed \(\alpha\), the power-law expressions are asymptotics rather than uniform approximations across the transition at \(3/2\).

## Verification

Run the accompanying standalone Python 3 standard-library program `verification/check.py` with `python verification/check.py`. It directly quadratures phase moments, independently integrates the two-dimensional phase/impact-parameter formula, tests 44 exponent-reflection combinations, boundary exact values, strict sample orderings and representative numerical corrections. The recorded local execution returned **PASS: 92 numerical consistency assertions**. These sampled computations check the formulas but cannot prove the continuous-exponent, all-eccentricity or asymptotic statements; the preceding analytical argument does so.

## Relationship to prior work

Barnes (2007) gives the geometric eccentric-transit probability and phase-dependent transit durations. Burke (2008), especially its Sections 4–6, derives the full transit-duration distribution under isotropic inclinations, obtains a phase-averaged duration factor and discusses duration-dependent survey yield. Its complete duration distribution necessarily contains the information needed to calculate arbitrary moment integrals; the present result **does not claim** a new distribution or a new underlying orbital model. The newly assessed structural statement is the explicit reflection of power-law yield exponents, the unique least-enhancing exponent, the exact mean-power versus power-mean discrepancy, and the critical logarithmic asymptotic. Those relationships were not identified in the inspected published source material. Beatty and Gaudi (2008) address transit-survey yield under simplifying circular-orbit assumptions; Kipping (2014) gives complementary eccentricity/geometric prior formulas. General special-function identities could subsume the integral symmetry algebraically; historical priority of the full applied theorem is not independently certified.

## Limitations

The duration formula uses the small-star, approximately constant-speed limit. The requirement \(\rho<1-e\) rules out geometric probability saturation and cannot remain fixed as \(e\uparrow1\); the latter is a formal mathematical asymptotic in a family where the stellar radius ratio is allowed to shrink accordingly. The model omits observing windows, thresholds, noise correlations, grazing-target selection, limb darkening and survey-specific population structure. Power-law weighted yield is not itself a bounded detection probability. For fixed empirical survey completeness, a separate integration is needed. No error bound is asserted for approximating actual transits by the idealized expression. Known full transit-duration distribution theory is broader than the single moment functional; bibliographic comparisons have not established independent historical priority.

## References

- J. W. Barnes, *Effects of Orbital Eccentricity on Extrasolar Planet Transit Detection and Lightcurves*, arXiv:0708.0243v1, first submitted 2007-08-01. https://arxiv.org/abs/0708.0243
- C. J. Burke, *Impact of Orbital Eccentricity on the Detection of Transiting Extrasolar Planets*, arXiv:0801.2579v1, first submitted 2008-01-16. https://arxiv.org/abs/0801.2579
- T. G. Beatty and B. S. Gaudi, *Predicting the Yields of Photometric Surveys for Transiting Extrasolar Planets*, arXiv:0804.1150, 2008. https://arxiv.org/abs/0804.1150
- D. M. Kipping, *Bayesian priors for the eccentricity of transiting planets*, arXiv:1408.1393, 2014. https://arxiv.org/abs/1408.1393
