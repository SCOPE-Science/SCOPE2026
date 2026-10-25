# A third-order silhouette-type bias at minimum projected area of a regular tetrahedron

## Finding
Consider the regular tetrahedron \(T\subset\mathbb R^3\) with vertices
\[
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1).
\]
Its edge length is \(2\sqrt2\). For \(U\) uniform on the unit sphere, let \(S(U)\) be the Euclidean area of the orthogonal projection of \(T\) onto \(U^\perp\), and \(N(U)\) its vertex count, either \(3\) or \(4\) almost surely. Set \(s_*=2\sqrt2\). For \(\varepsilon\downarrow0\), the **joint small-surplus and silhouette-type law** is
\[
\begin{aligned}
\Pr\{S<s_*+\varepsilon,\ N=3\}
 &=\frac{3}{2\sqrt2\pi}\varepsilon^2+\frac7{8\pi}\varepsilon^3+O(\varepsilon^4),\\
\Pr\{S<s_*+\varepsilon,\ N=4\}
 &=\frac{3}{2\sqrt2\pi}\varepsilon^2+\frac5{8\pi}\varepsilon^3+O(\varepsilon^4).
\end{aligned}
\]
In particular,
\[
\boxed{\Pr\{N=3\mid S<s_*+\varepsilon\}=\frac12+\frac{\sqrt2}{24}\varepsilon+O(\varepsilon^2).}
\]
Thus although triangle and quadrilateral shadows contribute equally to the leading near-minimum area probability, the triangular shadow has a strictly larger third-order contribution. The first nonzero conditional bias is positive.

## Assumptions and scope
The tetrahedron has the **explicit coordinate normalization** above; coefficients change under rescaling. Directions are Haar-uniform, with \(U\) and \(-U\) representing the same plane. The exceptional directions with ambiguous silhouette count have spherical measure zero. All expansions are as a **positive absolute area surplus** \(\varepsilon\to0^+\), not a relative surplus. The claimed remainders concern a fixed tetrahedron and do not assert uniformity in shape perturbations. The minimum projected area really is \(s_*\), and equality occurs at twelve directions, each having two nonzero coordinates of absolute magnitude \(1/\sqrt2\).

## Proof
**1. Area and silhouette in ordered absolute coordinates.** Every face of this tetrahedron has area \(2\sqrt3\), and its outer normal is, up to sign, one of the four vertex directions normalized by \(\sqrt3\). The standard face-projection identity gives
\[
S(u)=\sum_{v\in\operatorname{vert}(T)}|u\cdot v|.
\]
For \(a\ge b\ge c\ge0\) the ordered absolute values of \(u\)'s coordinates, direct expansion of the four signed scalar products gives
\[
S(u)=\max\{4a,\ 2(a+b+c)\}.
\]
For generic \(u\), the projected vertex is interior to the other three projected vertices precisely in the region \(a<b+c\). Consequently \(N=3\) exactly when \(a<b+c\), and \(N=4\) exactly when \(a>b+c\). These alternatives can equivalently be checked by projecting all four vertices and evaluating their planar hull.

**2. Locate all minima.** Since \(1=a^2+b^2+c^2\le a(a+b+c)\), if \(a<1/\sqrt2\) then \(S\ge2(a+b+c)>2\sqrt2\). If \(a\ge1/\sqrt2\), then \(S\ge4a\ge2\sqrt2\). Equality requires \(a=b=1/\sqrt2\) and \(c=0\), and each such direction realizes the bound. There are exactly \(3\times4=12\) spherical minimizers, pairwise separated, so for sufficiently small surplus the sublevel set is a disjoint union of twelve local neighborhoods.

**3. An exact chart at a minimizing direction.** Take \(u_0=(1,1,0)/\sqrt2\) and use orthonormal tangent coordinates
\[
u(x,y)=\sqrt{1-x^2-y^2}\,u_0+x(1,-1,0)/\sqrt2+y(0,0,1).
\]
Writing \(x=r\cos\phi\), \(y=r\sin\phi\), the preceding formula becomes exactly, near \(u_0\),
\[
S(u(x,y))=s_*\sqrt{1-r^2}+b(\phi)r,
\qquad b(\phi)=\max\{2\sqrt2|\cos\phi|,\,2|\sin\phi|\}.
\]
The triangular regime is \(|\tan\phi|>\sqrt2\); the quadrilateral regime is \(|\tan\phi|<\sqrt2\). Put \(\theta_0=\arctan\sqrt2\). In each of four symmetric planar angular quadrants, the quadrilateral sector is \(0<\phi<\theta_0\), and the triangular sector is \(\theta_0<\phi<\pi/2\).

**4. Uniform radial and spherical-area expansion.** Since \(b(\phi)\ge2\sqrt{2/3}\), the unique sufficiently small positive solution of \(S=s_*+\varepsilon\) satisfies, uniformly in \(\phi\),
\[
R_\varepsilon(\phi)=\frac\varepsilon{b(\phi)}+\frac{s_*\varepsilon^2}{2b(\phi)^3}+O(\varepsilon^3).
\]
The spherical Jacobian of the chart is \(r\,dr\,d\phi/\sqrt{1-r^2}\). Thus the area of a fixed angular sector with \(0\le r<R_\varepsilon(\phi)\) is obtained from
\[
1-\sqrt{1-R_\varepsilon^2}
=\frac{\varepsilon^2}{2b^2}+\frac{s_*\varepsilon^3}{2b^4}+O(\varepsilon^4)
\]
uniformly. In particular no logarithm or fractional power appears to these orders.

**5. Evaluate both sectors exactly.** Elementary substitutions \(z=\tan\phi\) and \(z=\cot\phi\) give the full angular integrals over all four quadrants,
\[
\begin{array}{c|cc}
 & \int b^{-2}\,d\phi &\int b^{-4}\,d\phi\\ \hline
N=3&1/\sqrt2&7\sqrt2/48\\
N=4&1/\sqrt2&5\sqrt2/48
\end{array}.
\]
For example, in one quadrant the quadrilateral integrals are \(\int_0^{\theta_0}(8\cos^2\phi)^{-1}d\phi\) and \(\int_0^{\theta_0}(64\cos^4\phi)^{-1}d\phi\); the triangular integrals use \((4\sin^2\phi)^{-1}\) and \((16\sin^4\phi)^{-1}\) on \([\theta_0,\pi/2]\). The twelve equal neighborhoods and normalized Haar measure supply the multiplier \(12/(4\pi)\). Substituting the two columns gives precisely the two displayed probabilities.

Finally, if \(a_2=3/(2\sqrt2\pi)\), \(a_{3,3}=7/(8\pi)\), and \(a_{3,4}=5/(8\pi)\), then dividing the two expansions gives
\[
\frac{a_2\varepsilon^2+a_{3,3}\varepsilon^3+O(\varepsilon^4)}
{2a_2\varepsilon^2+(a_{3,3}+a_{3,4})\varepsilon^3+O(\varepsilon^4)}
=\frac12+\frac{a_{3,3}-a_{3,4}}{4a_2}\varepsilon+O(\varepsilon^2)
=\frac12+\frac{\sqrt2}{24}\varepsilon+O(\varepsilon^2).
\]
This completes the proof of the **joint** endpoint expansion.

## Verification
The standalone `verify_projection.py` separately projects all four coordinate vertices onto random two-planes and constructs their planar convex hulls with `scipy.spatial.ConvexHull`, comparing both area and silhouette type against the analytical formula. It then integrates the **exact** chart boundary using `scipy.integrate.quad` and `scipy.optimize.brentq`, checking the two third-order coefficients and conditional slope for a sequence of positive surpluses. Dependencies: Python 3 with `numpy` and `scipy`; run `python verify_projection.py` in the package directory. The program prints `ALL_TETRA_PROJECTION_CHECKS_OK` after its assertions pass. The proof of the continuous theorem is analytical; these finite diagnostics are corroboration only.

## Relationship to prior work
Feldman and Klain, *Angles as probabilities* (2008), prove the **unconditional** probability that a random tetrahedral shadow is triangular through vertex solid angles. Finch, *Planar Projections and Second Intrinsic Volume* (2012), §2.1 gives the regular tetrahedron's **unconditional** area moments and the separate unconditional probabilities of triangular and quadrilateral shadows. Finch's §5 gives a **piecewise formula for shadow area as a function of direction**, including silhouettes. Neither publication explicitly states the two type-resolved **small-surplus distribution coefficients**, their cancellation at leading order, or the strictly positive \(\sqrt2/24\) linear conditional bias. The latter is a further local asymptotic calculation and is not being presented as a new unconditional area law.

The previously published area-weighted silhouette moment formulas for tetrahedra also concern zero-th through second integral moments of \(S\) conditioned on \(N\). Those finite moments do not by themselves imply type-resolved endpoint density or the coefficient computed here. The distinction is implication rather than terminology: the exact endpoint coefficients depend on local angular geometry at the twelve minimizing orientations and on the spherical Jacobian.

Vickers and Brown (2001) study broader projected-area and projected-perimeter distributions of solid particles. The accessible abstract concerns several nonpolyhedral families; their full paper was unavailable for direct comparison. This is an acknowledged historical-priority risk, not evidence that their result fails to cover the theorem.

## Limitations
The result is for one explicitly normalized **regular tetrahedron**, Haar-uniform orthogonal views, and the lower tail of projected area, jointly with silhouette type. It does not evaluate the full conditional law, other tetrahedron shapes, projected perimeter, or nonuniform views. A complete historical-priority guarantee cannot be made from the accessible sources. No independent mathematical audit or external certification is claimed.

## References
1. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1, publicly posted 19 September 2008; especially Theorem 1.
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, publicly posted 12 March 2012; especially §§2.1 and 5.
3. G. T. Vickers and D. J. Brown, *The Distribution of Projected Area and Perimeter of Convex, Solid Particles*, Proceedings of the Royal Society A 457 (2001), 283–306, doi:10.1098/rspa.2000.0667 (full text inaccessible at preparation time).
4. *Area-weighted silhouette probabilities of arbitrary tetrahedra*, published mathematical research record `ddfd7f3eeb66`, with first/second conditional moments distinct from local threshold asymptotics.
