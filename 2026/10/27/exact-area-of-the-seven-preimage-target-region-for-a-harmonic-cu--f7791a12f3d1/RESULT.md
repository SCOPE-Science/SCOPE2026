# Exact area of the seven-preimage target region for a harmonic cubic

## Finding
For the harmonic polynomial \(F(z)=z^3-\overline z^{\,2}\), define the regular seven-preimage set
\[
U_7=\{w\in\mathbb C\setminus(F(\{J_F=0\})): \#\{z\in\mathbb C:F(z)=w\}=7\}.
\]
Then \(U_7\) is a bounded, connected, star-shaped open set with fivefold rotational symmetry. Its boundary consists of five smooth caustic segments meeting at five transverse double points. The **exact planar area** is
\[
\operatorname{area}(U_7)=\frac{160}{243}\left(\arccos\frac14-\frac{2\pi}{5}+\frac{\sqrt{15}}{64}\right)
=0.0803255144042085\ldots.
\]
More generally the regular seven-preimage set of \(F_b(z)=z^3-b\overline z^{\,2}\), for \(b>0\), has area \(b^6\operatorname{area}(U_7)\), because \(F_b(bu)=b^3F(u)\).

## Assumptions and scope
Here area denotes ordinary planar Lebesgue measure; zeros are counted **without multiplicity** and only regular targets are assigned a valence. The Jacobian is \(J_F(z)=9|z|^4-4|z|^2\), so the critical locus is the origin together with \(|z|=2/3\). The target \(w=0\) is critical, as is every point of the caustic described below; exclusion of the critical values does not affect area. The result concerns the specific harmonic cubic and its positive coefficient rescalings, not arbitrary harmonic polynomials.

## Proof
**1. Critical-value curve and monotone polar angle.** Parametrize the nontrivial critical circle by \(z=(2/3)e^{it}\). Its image is
\[
C(t)=\frac8{27}e^{3it}-\frac49e^{-2it},\qquad 0\le t<2\pi.
\]
It never vanishes because the two Fourier amplitudes differ. Direct differentiation gives
\[
\operatorname{Im}(\overline{C(t)}C'(t))=-\frac{32}{243}(1+\cos5t).
\]
Consequently \(\arg C(t)\) decreases monotonically and strictly over every nontrivial interval, with total change \(-4\pi\). To see the total change, factor \(C(t)=(4/27)e^{-2it}(2e^{5it}-3)\); the second factor winds zero times about the origin. Every ray is thus met exactly twice (with the natural continuous convention at isolated zero angular derivative points).

**2. Valence and the inner radial envelope.** Outside the critical circle the map preserves orientation, and inside it reverses orientation. The harmonic argument principle, or degree additivity over the disk and its exterior, yields for each regular target
\[
N(w)=3-2\operatorname{wind}(C,w).
\]
Because the polar argument of \(C\) travels twice around clockwise and radial intersections occur in pairs, the winding numbers are \(0,-1,-2\), and the seven-preimage locus is precisely the region **inside both radial intersections**. This region is star-shaped about the origin in the closure sense, and its boundary is the smaller radial envelope of the two caustic branches. Near \(w=0\), the five simple unit-modulus solutions of \(z^3=\overline z^{\,2}\) persist, while the critical solution at the origin splits into two solutions of opposite signs; hence nearby regular targets have seven preimages, identifying the innermost region. Strict radial ordering can change only at a self-intersection.

**3. Exact location of double points and boundary segments.** If \(C(t+h)=C(t-h)\) for distinct parameter points, then
\[
2e^{5it}\sin(3h)+3\sin(2h)=0.
\]
After excluding coinciding parameters, this forces \(\cos h=\pm1/4\) and \(e^{5it}=\pm1\). Up to periodicity, there are exactly five distinct double-point images at modulus \(5/27\), namely \((5/27)e^{6\pi i j/5}\) for \(j=0,\ldots,4\). In particular, the solutions \(t=\pm h_0\), where \(h_0=\arccos(1/4)\), map to \(5/27\). Their other equivalent parameter representations give the same five images; the derivative vectors at these parameter pairs are not parallel, so the crossings are transverse.

Set \(\delta=h_0-2\pi/5>0\). The five selected arcs making up the inner radial envelope are exactly \(C(t)\) for \(|t-2\pi j/5|\le\delta\), with \(j=0,\ldots,4\). Indeed the endpoints are consecutive double points, the open portions contain no self-intersection, and at \(t=0\) the radius \(|C(0)|=4/27\) is the **smaller** of the two radial intersections on the negative real ray. Continuity and the complete double-point classification force the same choice on every intervening ray. These arcs join to form a simple star-shaped boundary. The fivefold rotational symmetry follows from \(C(t+2\pi/5)=e^{6\pi i/5}C(t)\).

**4. Oriented area.** The boundary is clockwise, so Green's formula, with \(t\) traversing each selected arc in increasing order, gives
\[
\begin{aligned}
\operatorname{area}(U_7)
&=-\frac{5}{2}\int_{-\delta}^{\delta}\operatorname{Im}(\overline{C(t)}C'(t))\,dt\\
&=\frac{160}{243}\left(\delta+\frac{\sin(5\delta)}5\right).
\end{aligned}
\]
The identities \(\delta=\arccos(1/4)-2\pi/5\) and \(\sin(5\delta)=5\sqrt{15}/64\) give the advertised closed form. The coefficient scaling follows by substituting \(z=bu\) and observing the dilation of the target plane by \(b^3\).

## Verification
The supplementary script `verify_area.py` computes the constant by two separate methods: the derived exact caustic-arc formula, and an independently discretized polar integral of the minimum of the two radial intersections. With 10,001 caustic samples and 40,001 angular quadrature points the results are respectively \(0.0803255144042085\ldots\) and \(0.0803262828733777\ldots\), an absolute discrepancy of less than \(8\times10^{-7}\). It also checks the critical-value identity and five vertex radii at finitely many sample points. The proof above, not finite discretization, establishes the exact assertion.

## Relationship to prior work
Brilleslyper, Brooks, Dorff, Howell, and Schaubroeck (2020) use winding of critical hypocycloids to classify **numbers of zeros** in real-parameter harmonic trinomial families; Brooks and coauthors (2022) extend such counts to complex parameters. Those established root-counting principles are used here. The present claim concerns a different invariant: the two-dimensional Lebesgue **area of the target locus attaining seven preimages** for one fixed map, including its exact inner-caustic envelope. Neither inspected paper states the present area expression. A 2023 study of convex combinations of harmonic families concerns changes of valence under polynomial interpolation, not this target-plane area. This work does not claim that the general winding principle or the occurrence of seven roots is new.

## Limitations
Historical priority for the precise area formula remains provisional; geometrically equivalent older caustic-area calculations under different names are possible. The 2023 related paper was accessible in bibliographic/abstract form rather than complete readable text. The numerical verification has finite discretization error, unlike the closed-form proof. Transverse-intersection classification applies specifically to this fivefold caustic. No independent audit has been performed.

## References
1. M. Brilleslyper, J. Brooks, M. Dorff, R. Howell, L. Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proceedings of the AMS Series B **7** (2020), 82–90, DOI 10.1090/bproc/51 (publicly available 2020-06-17).
2. J. Brooks, M. Dorff, A. Hudson, E. Pitts, C. Whiffen, A. Woodall, *Zeros of a Family of Complex-Valued Harmonic Trinomials*, Bulletin of the Malaysian Mathematical Sciences Society **45** (2022), 1079–1091, DOI 10.1007/s40840-021-01230-8.
3. J. Brooks, M. Dixon, M. Dorff, A. Lee, R. Ottinger, *Zeros of Convex Combinations of Elementary Families of Harmonic Functions*, Mathematics **11** (2023), 4057, DOI 10.3390/math11194057.
