# Exact rise–fall sign rigidity and a critical duration law for a resonant mixed tide

## Finding
Consider the normalized two-harmonic water-level proxy
\[
h(t)=\cos(2t)+a\cos(t+\phi),\qquad 0<a<2,\quad \phi\in\mathbb R,
\]
with the physical time variable rescaled so that one complete cycle has length \(2\pi\). Let \(R(a,\phi)\) be the total length in one cycle on which \(h'(t)>0\) (total rising-water duration), and let \(E(a,\phi)=2\pi-R(a,\phi)\) be the falling-water duration. The model has exactly two strict high waters and two strict low waters in each cycle. Its true, unweighted duration imbalance obeys the **global sign law**
\[
\operatorname{sgn}(R(a,\phi)-\pi)=\operatorname{sgn}(\sin 2\phi).
\]
The equality case \(R=E=\pi\) occurs precisely when \(\phi\in (\pi/2)\mathbb Z\). In particular, the sign cannot reverse when the amplitude ratio \(a\) changes anywhere within the two-high-water domain \(0<a<2\).

The exact time-averaged cubic moment of the water-level rate is
\[
\frac1{2\pi}\int_0^{2\pi}h'(t)^3\,dt=-\frac32a^2\sin(2\phi).
\]
Consequently its signed skewness and the actual rising-duration imbalance have strictly opposite signs whenever nonzero; this agreement is an exact feature of this two-frequency proxy, not a general property of tidal records.

Along the natural equal-quadrature phase \(\phi=\pi/4\), put
\[
\alpha(a)=\arcsin\!\left(\frac{\sqrt{a^2+32}-a}{8}\right),\qquad
\beta(a)=\arcsin\!\left(\frac{\sqrt{a^2+32}+a}{8}\right).
\]
Both inverse sines take values in \((0,\pi/2)\) for \(0<a<2\). The rising duration is exactly
\[
R(a,\pi/4)=2[\alpha(a)+\beta(a)],
\]
and has the sharp one-sided boundary law
\[
R(a,\pi/4)-\pi=\frac\pi3-\frac2{\sqrt3}\sqrt{2-a}+O(2-a)
\quad\text{as }a\uparrow2.
\]
Thus the limiting duration imbalance is \(\pi/3\), approached with a specified square-root deficit when two stationary points coalesce. For small amplitude, at any fixed phase,
\[
R(a,\phi)-\pi=\frac{a^2}{8}\sin(2\phi)+O(a^4)
\quad\text{as }a\downarrow0.
\]
The latter coefficient shows that rise–fall asymmetry first enters at second order in the diurnal-to-semidiurnal amplitude ratio.

## Assumptions and scope
The high-frequency constituent has unit amplitude and exactly double the low-frequency constituent's angular frequency. The two amplitudes and their relative phase are fixed throughout each ideal cycle; an additive water-level datum would not change any conclusion. The true annual, lunar, solar and compound tidal constituents are not exactly commensurate, so the theorem applies directly to the ideal resonant proxy, not to every measured tide. No tidal velocity, channel morphology, nonlinear shallow-water dynamics, or sediment transport is modeled. In the theorem, rising and falling are defined by the sign of the time derivative of **water level**, not by measured horizontal flood/ebb currents. At \(a=2\), some phases have degenerate extrema and the two-high-water statement is intentionally not extended to that boundary.

## Proof
**Four simple stationary points.** We have
\[
h'(t)=-2\sin(2t)-a\sin(t+\phi),\qquad
h''(t)=-4\cos(2t)-a\cos(t+\phi).
\]
If a stationary point were degenerate, squaring the equalities \(a\sin(t+\phi)=-2\sin(2t)\) and \(a\cos(t+\phi)=-4\cos(2t)\) and adding would give
\[
a^2=4\sin^2(2t)+16\cos^2(2t)=4[1+3\cos^2(2t)]\ge4,
\]
contrary to \(0<a<2\). At \(a=0\), the derivative has four simple zeros per cycle, two maxima and two minima. By continuous dependence and absence of degeneracy, their numbers remain two and two throughout the domain.

**No unbalanced phase can have equal total durations.** Write \(z=e^{it}\). Every stationary point is a unit-circle root of
\[
P(z)=2z^4+ae^{i\phi}z^3-ae^{-i\phi}z-2.
\]
List the four simple roots in counterclockwise order, alternating maxima and minima, as \(z_0,z_1,z_2,z_3\). Define the alternating products \(U=z_0z_2\), \(V=z_1z_3\) and sums \(A=z_0+z_2\), \(B=z_1+z_3\). Vieta's formulas give
\[
UV=-1,\qquad U+V+AB=0.
\]
If the measure of the positive-derivative set equals that of the negative-derivative set, the sum of the lengths of alternating root arcs equals \(\pi\), whence \(U/V=-1\). Together with \(UV=-1\), this forces \(U^2=1\) and \(V=-U\), hence \(AB=0\). Therefore one of the alternating root pairs is antipodal: both \(z\) and \(-z\) solve \(P=0\). Adding and subtracting \(P(z)=P(-z)=0\) yields
\[
z^4=1,\qquad z^2=e^{-2i\phi}.
\]
It follows that \(e^{-2i\phi}=\pm1\), or \(\phi\in(\pi/2)\mathbb Z\). Conversely, for such phases \(h\) is reflection-symmetric about a suitable time origin, so its increasing and decreasing sets have equal lengths. Thus the zero set of the duration imbalance is **exactly** the indicated phase lattice for every \(0<a<2\).

**The sign.** Let \(t_j(a)\) be the four smoothly continued stationary times with \(t_j(0)=j\pi/2\), allowing their real lifts outside \([0,2\pi)\). Even \(j\) correspond to maxima and odd \(j\) to minima. The total rising duration is
\[
R(a,\phi)=2\pi+t_0(a)+t_2(a)-t_1(a)-t_3(a).
\]
The implicit function theorem applied to \(h'(t_j(a))=0\) gives the expansion
\[
t_j(a)=\frac{j\pi}{2}+(-1)^{j+1}\frac a4\sin\!\left(\frac{j\pi}{2}+\phi\right)
+\frac{a^2}{16}\sin\!\left(\frac{j\pi}{2}+\phi\right)
\cos\!\left(\frac{j\pi}{2}+\phi\right)+O(a^3).
\]
Substitution cancels the first-order terms and yields \(R-\pi=a^2\sin(2\phi)/8+O(a^3)\). The transformation \(a\mapsto-a\) is equivalent to shifting \(t\mapsto t+\pi\), leaving \(R\) unchanged; analyticity removes odd powers, improving the remainder to \(O(a^4)\). For any fixed phase not in \((\pi/2)\mathbb Z\), continuity in \(a\) and the established absence of zeros prevent a sign change. The small-amplitude expansion gives exactly the asserted global sign.

**Moment identity.** Expanding the cube of \(h'\) and averaging over a full period leaves only the resonant cross term. Since
\[
\frac1{2\pi}\int_0^{2\pi}\sin(2t)\sin^2(t+\phi)\,dt=\frac14\sin(2\phi),
\]
we obtain \(\langle h'^3\rangle=-3a^2\sin(2\phi)/2\). Also \(\langle h'^2\rangle=2+a^2/2>0\), so normalized skewness has precisely the same sign as this cubic moment, opposite to \(R-\pi\).

**Exact quadrature-phase duration and boundary.** At \(\phi=\pi/4\), shift \(x=t+\pi/4\). Then
\[
h=\sin(2x)+a\cos x,\quad h_x=2-4\sin^2x-a\sin x.
\]
The two roots for \(\sin x\) are \((\sqrt{a^2+32}-a)/8=\sin\alpha\) and \(- (\sqrt{a^2+32}+a)/8=-\sin\beta\). The four stationary angles are \(\alpha\), \(\pi-\alpha\), \(\pi+\beta\), \(2\pi-\beta\). Their alternating rising arcs total \(2(\alpha+\beta)\). As \(a\uparrow2\), one finds \(\alpha\to\pi/6\) and
\[
\beta=\frac\pi2-\sqrt{\frac{2-a}{3}}+O((2-a)^{3/2}),\qquad
\alpha=\frac\pi6+O(2-a).
\]
The claimed sharp square-root expansion follows, with its nonzero leading coefficient.

## Verification
Run the included `verify.py` using Python 3; it depends only on the standard library. It independently searches stationary roots over a full period, counts four simple roots on a grid of sample parameter values, evaluates the total rising time, compares its sign and the quadrature-phase closed formula, checks a small-amplitude expansion, evaluates a time-averaged cubic moment by numerical quadrature, and probes the critical square-root scaling. The analytic proof above establishes the continuous-parameter assertions; finite numerical checks are supplementary only.

A concrete check is \(R(1,\pi/4)-\pi\approx0.134074996409853\); the rising duration is longer than half the period, while the cubic moment is negative. The zero phase-lattice symmetry was also checked numerically.

## Relationship to prior work
Hoitink, Hoekstra and van Maren (2003) established that astronomical tidal interactions can create asymmetry and analyzed sediment transport, primarily for K1/O1/M2 current combinations. Nidzieko (2010) used derivative skewness as an indicator of mixed-tide asymmetry and explained its phase sensitivity. Song, Wang, Kiss and Bao (2011) established a general resonant-harmonic decomposition of skewness, including an exact formula for two harmonics; **the moment identity itself is not claimed to be original here**. Guo, Wang, Townend and He (2019) demonstrated that derivative skewness can even indicate the wrong duration direction for general tidal shapes. The novelty assessed here is instead an **exact, all-amplitude sign equivalence for actual, unweighted rising/falling times** inside the two-high-water region, together with its explicit quadrature-phase duration and boundary coefficient. Classical Stoner–Wohlfarth astroid theory already identifies a similar two-to-one-extremum bifurcation of the double-cosine potential; the simple extrema-count boundary is not claimed as new.

The checked literature did not provide the alternating-stationary-root duration argument, the exact absence of amplitude-induced direction reversals throughout \(0<a<2\), or the displayed quadrature-phase duration law. This is not a proof of historical uniqueness. Woodworth, Blackman, Pugh and Vassie (2005) discuss asymmetries in tidal elevation distributions; only their abstract was obtainable. The unpublished or inaccessible reach of older harmonic-geometry analyses remains a priority risk.

## Limitations
The theorem concerns only the exactly commensurate, two-term signal. It does not transfer the sign rigidity to any additional harmonic, slow amplitude or phase modulation, non-tidal trend, nonstationary forcing, actual measured current, or estuary hydrodynamics. At \(a\ge2\) the number of high waters may change; the sign law is not asserted there. The numerical experiment checks finitely many parameters and cannot establish the proof's global quantifiers. The historical-priority comparison is not an independent audit and does not guarantee absence of equivalent earlier results.

## References
1. A. J. F. Hoitink, P. Hoekstra, D. S. van Maren, “Flow asymmetry associated with astronomical tides: Implications for the residual transport of sediment,” *Journal of Geophysical Research: Oceans* **108** (2003), DOI: 10.1029/2002JC001539. First online 2003-10-09.
2. P. L. Woodworth, D. L. Blackman, D. T. Pugh, J. M. Vassie, “On the role of diurnal tides in contributing to asymmetries in tidal probability distribution functions in areas of predominantly semi-diurnal tide,” *Estuarine, Coastal and Shelf Science* **64** (2005), 235–240, DOI: 10.1016/j.ecss.2005.02.014.
3. N. J. Nidzieko, “Tidal asymmetry in estuaries with mixed semidiurnal/diurnal tides,” *Journal of Geophysical Research: Oceans* **115** (2010), DOI: 10.1029/2009JC005864.
4. D. Song, X. H. Wang, A. E. Kiss, X. Bao, “The contribution to tidal asymmetry by different combinations of tidal constituents,” *Journal of Geophysical Research: Oceans* **116** (2011), DOI: 10.1029/2011JC007270.
5. L. Guo, Z. B. Wang, I. Townend, Q. He, “Quantification of tidal asymmetry and its nonstationary variations,” *Journal of Geophysical Research: Oceans* **124** (2019), 773–787, DOI: 10.1029/2018JC014372.
