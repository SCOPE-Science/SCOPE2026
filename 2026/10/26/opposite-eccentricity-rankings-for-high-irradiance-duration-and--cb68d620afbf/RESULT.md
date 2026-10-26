# Opposite eccentricity rankings for high-irradiance duration and excess dose

## Finding
Fix a stellar luminosity and a semimajor axis for a bound two-body Kepler orbit. Let \(F_0\) be the incident flux at distance equal to the semimajor axis, and choose a high-flux threshold \(F_\mathrm{c}=\eta F_0\) with \(\eta>1\). Write
\[
\delta=1-\eta^{-1/2}\in(0,1).
\]
Across all eccentricities \(0\le e<1\), the orbital-time fraction \(H_\eta(e)\) spent strictly above \(F_\mathrm{c}\) is zero for \(e\le\delta\); for \(e>\delta\),
\[
H_\eta(e)=\frac{\arccos(\delta/e)-\sqrt{e^2-\delta^2}}{\pi}.
\]
It has **exactly one global maximizer**, \(e_*=\sqrt\delta\), and is strictly increasing on \((\delta,e_*)\) and strictly decreasing on \((e_*,1)\). Its sharp maximum is
\[
H_\mathrm{max}=\frac{\arccos\sqrt\delta-\sqrt{\delta(1-\delta)}}{\pi}.
\]
In contrast, the mean **excess high-flux dose**
\[
J_\eta(e)=\frac1P\int_0^P\left(\frac{F(t)}{F_0}-\eta\right)_+\,dt
\]
is exactly zero for \(e\le\delta\) and **strictly increases** for \(\delta<e<1\). Therefore, after \(e_*\), increasing eccentricity *shortens* the time above the threshold while *increasing* the accumulated flux excess above that same threshold.

## Assumptions and scope
The orbit obeys Newtonian two-body Kepler motion with fixed semimajor axis \(a>0\), fixed central gravitational parameter and fixed stellar luminosity \(L>0\). Eccentricity ranges over \([0,1)\) at this fixed semimajor axis; the Kepler period \(P\) is therefore fixed. Stellar irradiation is treated as an inverse-square instantaneous point-source flux \(F(t)=L/(4\pi r(t)^2)\), with no occultation, atmospheric response, finite stellar radius, or orbital perturbations. The reference flux is \(F_0=L/(4\pi a^2)\). The excess \((y)_+\) means \(\max\{y,0\}\). The comparison concerns orbital forcing, not temperature, climate habitability, or a biological dose-response law. Threshold \(\eta>1\) is fixed while eccentricity varies.

Let \(E\in[-\pi,\pi]\) be eccentric anomaly centered at periastron. The exact radius and physical-time weighting are
\[
r(E)=a(1-e\cos E),\qquad \frac{dt}{P}=\frac{1-e\cos E}{2\pi}\,dE.
\]
These formulas also specify how all integrals and strict boundary cases are interpreted. For \(e=0\), the incident flux equals \(F_0\) and neither threshold statistic is positive.

## Proof
**1. Exceedance interval.** Since \(1-e\cos E>0\), the strict inequality \(F(E)>\eta F_0\) is equivalent to
\[
1-e\cos E<\eta^{-1/2},\quad\text{or}\quad e\cos E>\delta.
\]
For \(e\le\delta\), this holds nowhere, except a measure-zero contact at equality, so both statistics vanish. For \(e>\delta\), the exceedance interval is exactly \(-E_0<E<E_0\), where \(E_0=\arccos(\delta/e)\in(0,\pi/2)\). Integrating the physical-time weight gives
\[
H_\eta(e)=\frac1{2\pi}\int_{-E_0}^{E_0}(1-e\cos E)\,dE
=\frac{E_0-e\sin E_0}{\pi},
\]
which is the claimed closed form because \(e\sin E_0=\sqrt{e^2-\delta^2}\).

**2. Exact and unique duration optimum.** Direct differentiation for \(e\in(\delta,1)\) yields
\[
H_\eta'(e)=\frac{\delta/e-e}{\pi\sqrt{e^2-\delta^2}}
=\frac{\delta-e^2}{\pi e\sqrt{e^2-\delta^2}}.
\]
Its denominator is positive and its numerator changes sign exactly once, from positive to negative, at \(e=\sqrt\delta\). Because \(0<\delta<\sqrt\delta<1\), this critical eccentricity is admissible and is the unique global maximizer: the function is identically zero for \(e\le\delta\), positive beyond onset, and strictly decreases after the critical point all the way toward \(e=1\). Substituting the critical eccentricity proves the displayed exact maximum. At threshold onset, \(H_\eta(\delta)=0\) continuously; no open-orbit endpoint at \(e=1\) needs to be included.

**3. Strict excess-dose ordering.** Using the same orbit-time weight and symmetry gives, for \(e>\delta\),
\[
J_\eta(e)=\frac1\pi\int_0^{E_0(e)}
\left[\frac1{1-e\cos E}-\eta(1-e\cos E)\right]dE.
\]
The integrand vanishes at the moving upper endpoint \(E_0(e)\), because there \(F=\eta F_0\). Hence Leibniz differentiation has no endpoint term:
\[
J_\eta'(e)=\frac1\pi\int_0^{E_0(e)}
\cos E\left[\frac1{(1-e\cos E)^2}+\eta\right]dE>0.
\]
The final inequality is strict because \(0<E_0(e)<\pi/2\), so \(\cos E>0\) throughout the integration interval. This proves the opposite duration/dose eccentricity rankings without appealing to numerics. For direct evaluation, the antiderivative also yields
\[
J_\eta(e)=\frac1\pi\left[\frac2{\sqrt{1-e^2}}\arctan\!\left(\sqrt{\frac{1+e}{1-e}}\tan\frac{E_0}2\right)-\eta(E_0-e\sin E_0)\right].
\]
The positive excess dose diverges as \(e\uparrow1\) within the idealized point-source model, whereas the duration fraction tends to the finite positive value \((\arccos\delta-\sqrt{1-\delta^2})/\pi\).

## Verification
A standalone standard-library program `verify.py` numerically integrates the time-weighted Kepler anomaly directly, without using the derived closed forms. It tested 90 seeded parameter/eccentricity pairs with direct quadrature of both duration and excess dose, plus bracketing comparisons around each proposed optimum and increasing-excess checks. These are finite reproducibility checks only; the proof above establishes the universal quantifiers.

An illustrative high-flux threshold is \(\eta=16/9\), so \(\delta=1/4\) and the unique duration-optimal eccentricity is exactly \(e_*=1/2\). The maximum time fraction is \(1/3-\sqrt3/(4\pi)=0.195501109477885\ldots\). At eccentricities \(e=0.3,0.5,0.8,0.99\), respectively, the duration fractions are approximately \(0.133644,0.195501,0.156939,0.113825\); the corresponding mean excess doses are approximately \(0.022587,0.229793,0.929716,6.473496\). Thus a later eccentricity can lower the duration fraction even as its excess dose rises.

Run `python verify.py` in the directory containing this report and the included standalone program.

## Relationship to prior work
Kane and Gelino's *The Habitable Zone Gallery* (arXiv:1202.2377v1, 2012) explicitly calculates the fraction of orbital time spent inside an insolation-defined habitable zone using Kepler's equation, and thus establishes the **underlying time-fraction methodology**. Their *The Habitable Zone and Extreme Planetary Orbits* (arXiv:1205.2429v1, 2012), particularly Section 3, discusses periastron exposure duration and eccentric-planet habitability. Dressing and collaborators' *Habitable Climates: The Influence of Eccentricity* (arXiv:1002.4875v1, 2010) develops more physically detailed climate modeling and contrasts orbital-mean irradiation with transient effects. These are not presented as new models here.

The added mathematical statement is the sharp global eccentricity optimizer for **one fixed, above-circular flux threshold**, together with a proof that threshold duration and accumulated excess flux rank high-eccentricity orbits in opposite orders. The inspected main results of those studies concern calculating time-in-zone for given orbits or climate response and do not state these two coupled optimization and ordering conclusions. The results are elementary consequences of Kepler's anomaly formulas once the specific two-metric comparison is posed, so broader rearrangement or orbital-insolation analyses may already cover them. No historical uniqueness is asserted.

## Limitations
The conclusion requires **fixed semimajor axis**, **fixed stellar luminosity**, an **above-circular threshold**, and an **instantaneous inverse-square flux**, not an atmosphere-mediated hazard. Varying the semimajor axis along with eccentricity, using a threshold defined relative to orbital-average rather than circular flux, or modeling thermal inertia could alter the result. At high eccentricities the idealized orbit approaches the point source; actual stellar size, collision limits, tides, and atmospheric processes restrict the applicable physical regime. The theorem does not claim duration is a sufficient proxy for habitability, nor does an increasing excess dose alone determine planetary climate.

## References
1. C. D. Dressing, D. S. Spiegel, C. A. Scharf, K. Menou, and S. N. Raymond, *Habitable Climates: The Influence of Eccentricity*, arXiv:1002.4875v1 (first publicly posted 2010-02-25); https://arxiv.org/abs/1002.4875 .
2. S. R. Kane and D. M. Gelino, *The Habitable Zone Gallery*, arXiv:1202.2377v1 (2012-02-10), especially §3.3 and Kepler equation (6); https://arxiv.org/abs/1202.2377 .
3. S. R. Kane and D. M. Gelino, *The Habitable Zone and Extreme Planetary Orbits*, arXiv:1205.2429v1 (2012-05-11), especially §3; https://arxiv.org/abs/1205.2429 .
