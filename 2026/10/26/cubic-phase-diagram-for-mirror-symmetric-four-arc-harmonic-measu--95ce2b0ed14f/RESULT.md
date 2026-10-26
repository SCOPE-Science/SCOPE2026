# Cubic phase diagram for mirror-symmetric four-arc harmonic measure

## Finding
Let \(0<\delta<b<a<\pi-\delta\), with \(a-b>2\delta\). On the unit circle let \(E\) be the union of the four open arcs of angular half-width \(\delta\) centered at \(\pm a\) and \(\pm b\). Write \(u(z)=\omega(z,E,\mathbb D)\), the harmonic measure of \(E\) from \(z\in\mathbb D\). A critical point means \(\nabla u(z)=0\), and its multiplicity is the order of the zero of \(u_x-i u_y\).

Set \(A=\cos a\), \(B=\cos b\), \(c=\cos\delta\), and form the real polynomial
\[
H(t)=(A+B)t^3-4c(2AB+1)t^2+4(A+B)(AB+3c^2-1)t-8c(A^2+B^2+2c^2-2).
\]
For \(t\notin[-2,2]\), write \(J(t)\) for the unique solution of \(z+z^{-1}=t\) in \(\mathbb D\); this solution is determined without choosing a global square-root branch by \(|J(t)|<1\).

**Complete critical-point description.** There are exactly three critical points in \(\mathbb D\), counted with multiplicity. If \(A+B\ne0\), they are exactly \(J(t)\) for the three roots of \(H\), with multiplicity. No root of \(H\) lies in \([-2,2]\). Let \(\Delta(H)\) be the ordinary real cubic discriminant, with the usual convention that it is positive for three distinct real roots. Then \(\Delta(H)>0\) gives three distinct real critical points; \(\Delta(H)<0\) gives one real critical point and a nonreal conjugate pair; and \(\Delta(H)=0\) gives a repeated critical point on the real diameter. Thus \(\Delta(H)=0\) is an explicit algebraic collision test in the three geometric parameters. Both strict phases occur for genuinely nonantipodal four-arc configurations.

For the antipodal subfamily \(a+b=\pi\), the origin is critical, and the remaining two critical points are
\[
\begin{cases}
\pm r,&0<b<\pi/4,\\
\pm ir,&\pi/4<b<\pi/2-\delta,
\end{cases}
\qquad
r^2=\dfrac{|\cos(2b)|}{\cos(2\delta)+\sqrt{\cos^2(2\delta)-\cos^2(2b)}}.
\]
At \(b=\pi/4\), all three critical points coalesce into one critical point of order three at the origin. The sharp angle \(\pi/4\) is independent of arc width throughout \(0<\delta<\min\{b,\pi/2-b\}\).

## Assumptions and scope
All angles are measured in radians. The four boundary arcs are pairwise disjoint by the strict inequalities above; their endpoints are not included, which does not affect harmonic measure. The function \(u\) is the Poisson integral of their indicator and takes values strictly between zero and one inside the disk. The words *three critical points* always count analytic multiplicity; on a collision locus there may be fewer than three distinct points. In the cubic case the displayed discriminant is an exact decision rule rather than an assertion that its zero set is a single smooth hypersurface. The exceptional leading-coefficient case \(A+B=0\) is treated separately, not by applying the cubic discriminant to a lower-degree polynomial.

## Proof
**1. Exact derivative.** Let \(f\) be the unique analytic function with \(\operatorname{Re}f=u\) and imaginary part zero at the origin. For the pair of arcs centered at \(\pm\theta\), the Poisson–Fourier expansion gives
\[
f_\theta'(z)=\frac4\pi\sum_{n=1}^\infty\sin(n\delta)\cos(n\theta)z^{n-1}.
\]
With \(N_\theta(z)=\cos\theta(1+z^2)-2cz\) and
\[
Q_\theta(z)=\prod_{\epsilon=\pm1}\left(1-2z\cos(\theta+\epsilon\delta)+z^2\right),
\]
the elementary geometric-series identity yields
\[
f_\theta'(z)=\frac{4\sin\delta}{\pi}\frac{N_\theta(z)}{Q_\theta(z)}.
\]
Therefore
\[
f'(z)=\frac{4\sin\delta}{\pi}\frac{P(z)}{Q_a(z)Q_b(z)},
\quad P(z)=N_a(z)Q_b(z)+N_b(z)Q_a(z).
\]
All denominator zeros are on the unit circle, at the eight distinct arc endpoints. The critical points of \(u\) in the disk are precisely the zeros of \(P\), because \(f'=u_x-i u_y\).

**2. Reciprocal structure and interior count.** Each \(N_\theta\) is reciprocal of degree two and each \(Q_\theta\) is reciprocal of degree four, so \(P(z)=z^6P(1/z)\) as a polynomial identity (even if its leading or constant coefficient vanishes). No boundary point is a zero of \(P\): away from endpoints, \(u\) has a constant boundary value zero or one in a neighborhood, and the Hopf boundary-point lemma gives a nonzero radial derivative and hence \(f'\ne0\). At an endpoint of a \(\pm\theta\) arc, \(N_\theta\ne0\) and the other pair's denominator is nonzero, so the simple pole of \(f'\) does not cancel. Explicitly, at \(z=e^{i(\theta\pm\delta)}\),
\[
N_\theta(z)=-2z\sin\theta\sin(\theta\pm\delta)\ne0.
\]
(The analogous conjugate endpoints follow from real coefficients.) If zero has multiplicity \(m\) as a root of \(P\), reciprocity gives degree \(6-m\) and pairs each remaining nonzero root with its inverse. Since there are no unit-modulus roots, exactly \(m+(6-2m)/2=3\) roots lie in the open disk, counted with multiplicity.

**3. The cubic phase test.** The identities
\[
Q_\theta(z)=z^2\bigl[t^2-4c\cos\theta\,t+4(\cos^2\theta+c^2-1)\bigr],\quad
N_\theta(z)=z(\cos\theta\,t-2c),\quad t=z+z^{-1}
\]
show, after expansion, that \(P(z)=z^3H(z+z^{-1})\) for nonzero \(z\). When \(A+B\ne0\), \(P(0)\ne0\) and \(H\) is cubic. The mapping \(z\mapsto z+z^{-1}\) is a conformal bijection from \(\mathbb D\setminus\{0\}\) to \(\mathbb C\setminus[-2,2]\); its inverse is \(J\). Thus the three cubic roots give exactly the critical points and preserve multiplicities. No real cubic root can lie in \([-2,2]\), since that would give a forbidden boundary zero of \(P\). The standard real-cubic discriminant theorem now gives the asserted real/nonreal trichotomy, including repeated roots when the discriminant vanishes. The explicit discriminant can be evaluated without expanding it as
\[
\Delta(H)=h_2^2h_1^2-4h_3h_1^3-4h_2^3h_0-27h_3^2h_0^2+18h_3h_2h_1h_0,
\]
where \(H(t)=h_3t^3+h_2t^2+h_1t+h_0\).

The two strict phases are nonempty in the admissible, nonantipodal region: taking \(c=9/10\), \((A,B)=(-3/4,4/5)\) gives \(\Delta=14626551073/2500000000>0\); taking \((A,B)=(-11/20,3/5)\) gives \(\Delta=-914716481579/62500000000<0\). Both have \(A+B=1/20\) and satisfy the stated angle-separation conditions. Along the continuous straight segment between these two points in the \((A,B)\)-plane, with \(c=9/10\), disjointness is maintained and the discriminant vanishes at least once by continuity. Therefore the collision is genuine within the admissible family and not an artifact of a degenerate arc endpoint.

**4. Exact antipodal splitting.** If \(a+b=\pi\), then \(A=-B\), and
\[
H(t)=-4c(1-2B^2)t^2+16c(1-B^2-c^2).
\]
Consequently \(z=0\) is critical. The configuration is invariant under \(z\mapsto-z\), and after the covering \(w=z^2\), the four arcs become two equal arcs with half-width \(2\delta\) and centers \(\pm2b\). For this two-arc harmonic measure, the critical point \(w_0\) is the unique disk solution of
\[
\cos(2b)(1+w^2)-2\cos(2\delta)w=0.
\]
Because \(2\delta<2b<\pi-2\delta\), its sign is that of \(\cos(2b)\), and its magnitude equals the displayed \(r^2\). The covering contributes the additional critical point at \(z=0\) and lifts \(w_0\) to the two square roots. For \(b=\pi/4\), the two-arc critical point is \(w_0=0\) and the derivative of the four-arc harmonic measure has a zero of order three at the origin. These exhaust the three available interior critical multiplicities.

## Verification
The standalone `check.py` carries out exact symbolic checks of both the rational derivative's Joukowski reduction and the reciprocal sextic identity, computes the two quoted discriminants as rational numbers, and checks that the corresponding geometric arcs are strictly disjoint. It verifies the expected real/nonreal critical points in both phases and the third-order zero at the square configuration. Independent high-precision Fourier-series summation checks the analytic derivative against its rational expression at two interior points; the discrepancies are below \(1.1\times10^{-70}\). Run `python check.py` after installing the dependencies stated in `requirements.txt`. The mathematical proof of the universal statements is the argument above, not an inference from these test cases.

## Relationship to prior work
Walsh's work on critical points of harmonic measure supplies the classical electrostatic and location framework. Ortel (1975) treats interpolation by linear combinations of harmonic measures, and Dubinin–Vuorinen (arXiv:1011.4178, first released 2010-11-18 UTC) treats extremal domain decomposition for harmonic measure. Neither latter work proves the present disk four-arc cubic phase diagram: their problems concern interpolation and extremal harmonic measure, respectively. The cubic axis-phase test, its nonantipodal realization, and the width-independent threefold square collision are the contribution assessed here, not the familiar Poisson formula or a general number-of-critical-points estimate. Walsh's 1948 full text and the corresponding chapter of his 1950 monograph were not available for a conclusive comparison and remain material priority risks.

## Limitations
The classification concerns four *equal-width*, reflection-symmetric, pairwise disjoint boundary arcs on one disk; it is not a theorem about arbitrary asymmetric four-arc configurations or multiply connected domains. The polynomial discriminant determines the number of real critical points; it does not by itself describe the geometry of every harmonic-measure level curve. Full historical priority against the unavailable Walsh material is not established. There has been no independent mathematical audit.

## References
1. J. L. Walsh, “On the Location of the Critical Points of Harmonic Measure,” *Proceedings of the National Academy of Sciences* **33** (1947), 18–20, DOI 10.1073/pnas.33.1.18. Bibliographic record and limited online text inspected.
2. J. L. Walsh, “The critical points of linear combinations of harmonic functions,” *Bulletin of the American Mathematical Society* **54** (1948), 196–205, DOI 10.1090/S0002-9904-1948-08984-4. Abstract and bibliographic description inspected; full article not read.
3. M. Ortel, “Interpolation by Linear Sums of Harmonic Measures,” *Canadian Mathematical Bulletin* **18** (1975), 249–253, DOI 10.4153/CMB-1975-048-2. Complete open full text inspected.
4. V. N. Dubinin and M. Vuorinen, “An extremal decomposition problem for harmonic measure,” arXiv:1011.4178v1 (2010-11-18), full text of v4 inspected; the earliest verified precise electronic public date among these selected mathematical sources is 2010-11-18. The earlier Walsh publications have historical month/year bibliographic records, not verified exact public-release days.
