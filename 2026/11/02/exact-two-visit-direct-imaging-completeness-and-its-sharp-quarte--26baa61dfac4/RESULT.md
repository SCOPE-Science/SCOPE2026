# Exact two-visit direct-imaging completeness and its sharp quarter-orbit transition

## Finding

For a planet on a known circular orbit of physical radius \(a>0\), consider two instantaneous direct-imaging visits separated by orbital phase \(\Delta\). The detector resolves the planet if and only if its instantaneous sky-projected star–planet separation is at least \(r\), where \(0<r<a\). Assume an isotropically oriented orbital plane and a uniform unknown initial orbital phase. There are no photometric, outer-working-angle, exposure-time, or scheduling restrictions. Let
\[
\tau=\frac r a,\qquad h=\sqrt{1-\tau^2},\qquad
\alpha=\arcsin\tau,\qquad
\delta=\arccos|\cos\Delta|\in[0,\pi/2].
\]
Write \(P_2(\tau,\Delta)\) for the probability of resolving the planet on at least one visit.

**Exact completeness.** Define the equal-cap spherical lens area
\[
L_\alpha(s)=\begin{cases}
2\pi(1-h),&s=0,\\
2\pi-4h\arccos\!\left(\dfrac{h\tan(s/2)}{\tau}\right)
-2\arccos\!\left(\dfrac{\cos s-h^2}{\tau^2}\right),&0<s<2\alpha,\\
0,&s\ge 2\alpha.
\end{cases}
\]
Then the exact two-visit completeness is
\[
\boxed{P_2(\tau,\Delta)=1-\frac{L_\alpha(\delta)+L_\alpha(\pi-\delta)}{2\pi}.}
\]
It is nondecreasing on \(0\le\delta\le\pi/2\). The complete optimal-delay classification is:

- If \(0<\tau<1/\sqrt2\), all delays with \(2\arcsin\tau\le\delta\le\pi/2\) give **certain detection for every orbit orientation and initial phase**, and shorter delays do not. The optimum is therefore nonunique.
- If \(1/\sqrt2\le\tau<1\), only \(\delta=\pi/2\) is optimal modulo antipodal phase symmetry; when \(\tau=1/\sqrt2\), detection is certain (including equality at the instrumental cutoff), whereas when \(\tau>1/\sqrt2\), some orientations remain unresolved.

In particular, a quarter-orbit or three-quarter-orbit separation is always optimal. For \(\tau>1/\sqrt2\) the exact maximal probability is
\[
\boxed{P_\mathrm{max}(\tau)=1+\frac{4h}{\pi}\arccos\!\left(\frac{h}{\tau}\right)-\frac2\pi\arccos\!\left(\frac{h^2}{\tau^2}\right).}
\]
For \(\tau\le1/\sqrt2\), \(P_\mathrm{max}(\tau)=1\). In contrast, a single visit has completeness \(P_1(\tau)=h\).

**Geometric sharpness and onset law.** For any fixed pair of epochs, the sharp worst-case projected separation is
\[
\boxed{\min_{\mathrm{orientations,phases}}\max\{s_1,s_2\}
=a\sqrt{\frac{1-|\cos\Delta|}{2}}=a\sin(\delta/2).}
\]
Thus no pair of visits can guarantee detection when \(\tau>1/\sqrt2\). At the sharp boundary \(\tau_c=1/\sqrt2\), the unavoidable nondetection probability turns on with exponent \(3/2\):
\[
1-P_\mathrm{max}(\tau)
\sim \frac{4}{3\pi}(2\sqrt2)^{3/2}(\tau-\tau_c)^{3/2}
\qquad\text{as }\tau\downarrow\tau_c\text{ from above}.
\]

## Assumptions and scope

The orbit is circular, its radius \(a\) and angular frequency \(\omega>0\) are fixed and known, and the two visit times obey \(\Delta=\omega(t_2-t_1)\) modulo \(2\pi\). The orbital normal is uniform on the unit sphere, and conditional on the normal the initial phase is uniform on the orbit. Equivalently, the pair of unit star–planet direction vectors is a uniformly rotated copy of two unit vectors with dot product \(\cos\Delta\). The line of sight is fixed; averaging over isotropic orbital orientations is mathematically equivalent to averaging a line-of-sight unit vector uniformly over the sphere for a fixed orbital pair.

At epoch \(i\), the projected separation is \(s_i=a\sqrt{1-(\ell\cdot u_i)^2}\), where \(\ell\) is the unit line of sight and \(u_i\) is the unit star–planet direction. The observation is declared successful when \(s_i\ge r\); the equality convention matters only for the orientation-wise worst-case statement, not for probabilities. The sole failure mechanism is obscuration by a circular inner working angle. Instrumental angular distance may replace \(r/a\) if both angles are measured at the same system distance. This is not a model of measured brightness, atmospheric phase functions, eccentric orbits, uncertain periods, or real target-dependent visit costs.

## Proof

**1. Spherical reduction.** An epoch fails precisely when \(|\ell\cdot u_i|>h\). Since \(0<h<1\), this is, up to a measure-zero boundary, the union of two disjoint caps of angular radius \(\alpha=\arccos h\), centered at \(u_i\) and \(-u_i\). Let \(L_\alpha(s)\) be the surface area on the unit sphere of the intersection of two equal caps whose centers have angular separation \(s\in[0,\pi]\). Of the four possible signed cap intersections for two epochs, two have center separation \(\delta\) and two have center separation \(\pi-\delta\). The four intersections are disjoint except on null boundaries because caps with opposite centers at the same epoch are disjoint. Division by the unit-sphere area \(4\pi\) gives
\[
1-P_2(\tau,\Delta)
=\frac{2L_\alpha(\delta)+2L_\alpha(\pi-\delta)}{4\pi}.
\]

**2. Lens area.** When \(s\ge2\alpha\), two caps do not overlap in positive area. At \(s=0\) their overlap is a cap of area \(2\pi(1-h)\). For \(0<s<2\alpha\), call the two intersection points \(A,B\) and the cap centers \(U,V\). The spherical triangles \(UVA\) and \(UVB\) have side lengths \(\alpha,\alpha,s\). If \(\beta\) is the angle at either center and \(\gamma\) is the angle at either intersection point, the spherical law of cosines gives
\[
\cos\beta=\frac{h\tan(s/2)}{\sin\alpha},\qquad
\cos\gamma=\frac{\cos s-h^2}{\sin^2\alpha}.
\]
The lens consists of two cap sectors of azimuthal angle \(2\beta\), of total area \(4\beta(1-h)\), with two congruent spherical triangles removed. Each triangle has area \(2\beta+\gamma-\pi\) by spherical excess. Therefore
\[
L_\alpha(s)=4\beta(1-h)-2(2\beta+\gamma-\pi)
=2\pi-4h\beta-2\gamma,
\]
which proves the displayed formula. Direct differentiation of the angle formulas gives the particularly useful exact derivative
\[
\boxed{L_\alpha'(s)=-2\sqrt{1-\frac{h^2}{\cos^2(s/2)}}\quad(0<s<2\alpha).}
\]
This derivative tends continuously to zero at \(2\alpha\); beyond that point the derivative is zero. The magnitude of the derivative is strictly decreasing with \(s\) on its positive support, because \(h>0\) and \(\cos(s/2)\) decreases.

**3. Optimal timing and equality cases.** For \(0<\delta<\pi/2\), we have \(\delta<\pi-\delta\). Since \(L_\alpha'\le0\) and its magnitude is decreasing on its support,
\[
\frac{d}{d\delta}\{L_\alpha(\delta)+L_\alpha(\pi-\delta)\}
=L_\alpha'(\delta)-L_\alpha'(\pi-\delta)\le0.
\]
If \(\alpha<\pi/4\), then \(L_\alpha(\pi-\delta)=0\) throughout the considered interval and the inequality is strict for \(\delta<2\alpha\), becoming equality for \(\delta\ge2\alpha\). If \(\alpha\ge\pi/4\), the inequality is strict for every \(0<\delta<\pi/2\): where both derivatives are nonzero, their magnitudes differ strictly, and where the second vanishes the first remains negative. Continuity handles endpoints. This gives all optimizers and the guaranteed-detection criterion. Substituting \(\delta=\pi/2\) into the lens formula, using \(\arccos(-z)=\pi-\arccos z\), gives the closed expression for \(P_\mathrm{max}\) when \(\alpha>\pi/4\).

**4. Sharp worst-case guarantee.** Change the sign of \(u_2\) if necessary and set \(c=|u_1\cdot u_2|\). The symmetric rank-two matrix \(u_1u_1^{\mathsf T}+u_2u_2^{\mathsf T}\) has largest eigenvalue \(1+c\). Thus, for every unit \(\ell\),
\[
2\min\{(\ell\cdot u_1)^2,(\ell\cdot u_2)^2\}
\le(\ell\cdot u_1)^2+(\ell\cdot u_2)^2\le1+c.
\]
Both inequalities are equalities for \(\ell\) along the normalized sum of the sign-adjusted \(u_1,u_2\). Hence the maximum, over \(\ell\), of the smaller squared line-of-sight projection is exactly \((1+c)/2\). Applying \(s_i^2=a^2[1-(\ell\cdot u_i)^2]\) gives
\[
\min_\ell\max_i s_i=a\sqrt{(1-c)/2}
=a\sin(\delta/2).
\]
Every such line of sight is realized by an orbital orientation and phase, so the bound is sharp, not only a probability-one assertion. Its maximum over visit delays is \(a/\sqrt2\) at \(\delta=\pi/2\).

**5. Sharp onset of missed detections.** For \(\tau>\tau_c\), put \(\varepsilon=2\alpha-\pi/2>0\). The derivative and the zero overlap at tangency imply
\[
L_\alpha(\pi/2)=2\int_{\pi/2}^{2\alpha}
\sqrt{1-\frac{\cos^2\alpha}{\cos^2(s/2)}}\,ds.
\]
Writing \(v=2\alpha-s\), the square-root factor is \(\sqrt{(\tan\alpha)v}\,[1+O(v)]\) uniformly as \(\alpha\to\pi/4\) from above, with \(0\le v\le\varepsilon\). Consequently
\[
L_\alpha(\pi/2)\sim\frac43\varepsilon^{3/2},\qquad
\varepsilon\sim2\sqrt2(\tau-\tau_c).
\]
Since \(1-P_\mathrm{max}=L_\alpha(\pi/2)/\pi\), the stated asymptotic follows.

## Verification

The standalone script `checker.py` requires only Python 3's standard library. Invoke `python3 checker.py` from the directory containing this file. It tests the spherical-lens identity and derivative on a nontrivial grid, verifies the optimizer and all two-visit symmetry and plateau regimes across a range of resolution thresholds, integrates the actual event of detection over a deterministic spherical grid independently of the lens formula, and checks the minimax envelope numerically. A successful replay printed **7584 finite assertions passed**. These finite checks are corroboration; the analytic steps above establish the quantified theorem.

For example, with normalized inner working angle \(\tau=4/5\), the one-visit probability is \(3/5\), whereas optimally separated visits have
\[
P_\mathrm{max}=1+\frac{12}{5\pi}\arccos(3/4)-\frac2\pi\arccos(9/16)
\approx0.9324490317659733.
\]
The conditional chance of discovery at the second visit, given nondetection at the first, is about \(0.8311225794149333\) under these assumptions.

## Relationship to prior work

Brown and Soummer (2010, arXiv:1003.4700) define direct-imaging inner-working-angle completeness and dynamic completeness for repeated visits, and use a general orbital Monte Carlo method. Their exact general definitions certainly cover the detection event used here, but neither a sharp all-threshold two-visit optimum nor a closed spherical-lens formula or the \(3/2\) onset law is stated in their methods and results. Shao, Catanzarite, and Pan (2010, arXiv:1003.4702) analyze circular exoplanet imaging and orbital determination, explicitly including obscuration by the inner working angle; their question concerns orbital measurement and astrometric synergy rather than ideal two-visit minimax completeness. Greco and Burrows (2015, arXiv:1505.07832) study direct-imaging observability fractions with projected separation and brightness limitations using orbital Monte Carlo experiments. Stark and collaborators (2015, arXiv:1506.01723) optimize revisit delays in a substantially richer mission model numerically and report improvements in survey yield, without this exact special-case spherical-cap phase diagram in the inspected sections.

These references establish that the probability measure and operational problem are classical. The contribution assessed here is the closed-form ideal two-visit timing classification (including all equality cases), worst-case guarantee, and sharp onset exponent for a fixed circular orbital radius and a separation-only detection threshold. The general algorithms in prior literature can numerically evaluate this special case; the result does not assert a new general-purpose completeness algorithm or improvements for real missions with photometric constraints.

## Limitations

This exact model disregards orbital eccentricity, a distribution of orbital radii or periods, finite exposure duration and orbital smearing, brightness/phase constraints, outer working angles, detector noise, and competing target priorities. The optimal quarter-period delay is **not** claimed to be optimal with any of those features active. The results concern discovery of one planet at least once, not orbital parameter recovery, planet identity across multiple detections, or practical estimators. The scientific priority comparison is limited to inspected accessible records and is not an independent literature certification.

## References

1. Brown, R. A., and Soummer, R., *New Completeness Methods for Estimating Exoplanet Discoveries by Direct Detection*, arXiv:1003.4700, first posted 2010-03-24. https://arxiv.org/abs/1003.4700
2. Shao, M., Catanzarite, J., and Pan, X., *The Synergy of Direct Imaging and Astrometry for Orbit Determination of exo-Earths*, arXiv:1003.4702, first posted 2010-03-24. https://arxiv.org/abs/1003.4702
3. Greco, J. P., and Burrows, A., *The Direct Detectability of Giant Exoplanets in the Optical*, arXiv:1505.07832, first posted 2015-05-28. https://arxiv.org/abs/1505.07832
4. Stark, C. C., et al., *Lower Limits on Aperture Size for an ExoEarth-Detecting Coronagraphic Mission*, arXiv:1506.01723, first posted 2015-06-04. https://arxiv.org/abs/1506.01723
