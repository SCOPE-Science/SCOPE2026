# The first three random-shadow area moments reconstruct every right circular cylinder

## Finding

Let \(K(r,h)\subset\mathbb R^3\) be the filled right circular cylinder of radius \(r>0\) and height \(h>0\). Project it orthogonally onto a plane chosen uniformly from the two-dimensional Grassmannian, without retaining the plane's direction. Write \(A\) for the projected area and \(m_j=\mathbb E[A^j]\) for its raw moments. **The ordered triple \((m_1,m_2,m_3)\) determines \((r,h)\) uniquely for all \(r,h>0\).** Its first two entries are not globally determining: there is a sharp, explicitly characterized two-branch ambiguity.

Put \(t=h/r\), \(y=t/(1+t)\in(0,1)\), and \(q_j=m_j/m_1^j\) for \(j=2,3\). The complete inversion formulas are
\[
\begin{aligned}
m_1&=\frac\pi2 r^2(1+t),\\
m_2&=\frac{r^4}{3}(\pi^2+4\pi t+8t^2),\\
m_3&=r^6\left(\frac{\pi^3}{4}+\frac{3\pi^3t}{8}+3\pi t^2+\frac{3\pi t^3}{2}\right),\\
q_2&=\frac{4}{3\pi^2}\left[\pi^2(1-y)^2+4\pi y(1-y)+8y^2\right],\\
q_3&=2-3y+\frac{24}{\pi^2}y^2+\left(1-\frac{12}{\pi^2}\right)y^3.
\end{aligned}
\]
The single variable \(y\) is the unique point in \((0,1)\) satisfying the two displayed normalized-moment equations. Then
\[
t=\frac{y}{1-y},\qquad r=\sqrt{\frac{2m_1}{\pi(1+t)}},\qquad h=tr.
\]

More precisely, let
\[
a=\pi^2-4\pi+8,\quad s=\frac{2\pi(\pi-2)}{a},\quad
t_{\rm crit}=\frac{\pi^2-8}{4(4-\pi)},\quad
t_{\rm vertex}=\frac{\pi(\pi-2)}{2(4-\pi)}.
\]
At a fixed positive mean shadow area, the first two moments have **exactly two** noncongruent cylinder solutions at every aspect ratio \(t>t_{\rm crit}\), except \(t=t_{\rm vertex}\), where the two branches coalesce. At \(0<t\le t_{\rm crit}\) they determine a unique cylinder. The distinct companion for \(t>t_{\rm crit}\), \(t\ne t_{\rm vertex}\), is obtained from \(z=s-y\in(0,1)\) and \(t'=z/(1-z)\), with the radius fixed by the common value of \(m_1\). Numerically \(t_{\rm crit}\approx0.5444980198\) and \(t_{\rm vertex}\approx2.088996040\).

An explicit exact two-moment collision takes \(r_1=h_1=1\), \(y_1=1/2\), \(y_2=s-1/2\), \(t_2=y_2/(1-y_2)\), \(r_2=\sqrt{2/(1+t_2)}\), and \(h_2=t_2r_2\). These two noncongruent cylinders have the same \(m_1,m_2\), but different \(m_3\).

## Assumptions and scope

The cylinder is solid, convex, nondegenerate, and bounded. Orthogonal projections have their ordinary Euclidean areas. The projection plane is Haar-uniform, independently of the cylinder's orientation; no directional labels are available. Moments are exact population expectations, not finite-sample estimators. The inverse uniqueness is among *right circular cylinders only*. Orientation and translation cannot be recovered, and are not parameters of the claim. All radii and heights are strictly positive and finite.

## Proof

**1. Exact shadow-area model.** Write the cylinder as the Minkowski sum of a radius-\(r\) disk orthogonal to its axis and a centered axial segment of length \(h\). For a unit normal \(U\) to the random plane, \(X=|U\cdot e_3|\) is uniform on \([0,1]\); set \(Y=\sqrt{1-X^2}\). The disk projects to an ellipse with semiaxes \(r,rX\), and the axial segment projects to a segment of length \(hY\) parallel to the ellipse's minor axis. A planar convex body expanded by a segment acquires area equal to that segment's length times the body's perpendicular width. Hence the **exact** projected area is
\[
A(X)=\pi r^2X+2rh\sqrt{1-X^2}. \tag{1}
\]
The formula extends to the two endpoint orientations by continuity.

**2. Compute the first three raw moments.** Integrating powers of (1) with respect to uniform \(X\) gives the first three formulas in the finding. In particular the elementary identities
\[
\int_0^1X\,dX=\tfrac12,\quad
\int_0^1Y\,dX=\tfrac\pi4,\quad
\int_0^1XY\,dX=\tfrac13,\quad
\int_0^1X^2Y\,dX=\tfrac\pi{16},\quad
\int_0^1XY^2\,dX=\tfrac14,\quad
\int_0^1Y^3\,dX=\tfrac{3\pi}{16}
\]
prove the stated polynomial moment identities after expanding. Substituting \(t=h/r\) and dividing by the appropriate powers of \(m_1\) gives precisely the quadratic and cubic expressions \(q_2(y)\) and \(q_3(y)\).

**3. Precisely classify the second-moment ambiguity.** The coefficient of \(y^2\) in \(q_2\) equals \(4a/(3\pi^2)>0\). Consequently, for any \(y,z\in(0,1)\),
\[
q_2(y)=q_2(z)\quad\Longleftrightarrow\quad y=z\ \text{or}\ y+z=s. \tag{2}
\]
Here \(1<s<2\): using \(3.14<\pi<22/7\), the inequalities reduce to \(\pi^2>8\) and \(\pi<4\). A distinct reflected companion \(z=s-y\) belongs to \((0,1)\) if and only if \(y>s-1\), except that \(y=s/2\) is its own reflection. Transforming \(y=s-1\) and \(y=s/2\) back to \(t=y/(1-y)\) gives the two displayed critical aspect ratios. Equality of \(m_1\) fixes the positive scale \(r\) uniquely for each candidate \(t\). This proves the claimed exact two-moment classification, including the strict endpoint conventions.

**4. The third moment separates every reflected pair.** Let \(y\ne z\) satisfy \(y+z=s\) and \(0<y,z<1\). Then
\[
\frac{q_3(y)-q_3(z)}{y-z}
=-3+\frac{24s}{\pi^2}+\left(1-\frac{12}{\pi^2}\right)(s^2-yz). \tag{3}
\]
Since \(\pi^2<12\), the coefficient \(1-12/\pi^2\) is negative; also \(yz\le s^2/4\). Therefore the right side of (3) is at most
\[
-3+\frac{24s}{\pi^2}+\frac{3s^2}{4}\left(1-\frac{12}{\pi^2}\right)
=\frac{12f(\pi)}{\pi a^2},\quad
f(p)=p^4-6p^3+4p^2+36p-64. \tag{4}
\]
This upper bound is strictly negative. Indeed, throughout \([157/50,22/7]\),
\[
f'(p)\ge4(157/50)^3-18(22/7)^2+8(157/50)+36>0,
\]
and direct rational substitution yields \(f(22/7)<0\). Since \(157/50<\pi<22/7\), \(f(\pi)<0\). Thus \(q_3(y)\ne q_3(z)\) whenever \(y\ne z\) and \(q_2(y)=q_2(z)\). Together with (2) this proves the asserted global first-three-moment uniqueness and completes the inverse reconstruction.

## Verification

The standalone `verify.py` uses **only the Python standard library**. It gives exact-rational checks of the polynomial sign in (4), including its derivative bound and the rational interval containing \(\pi\). It checks normalized-moment reflection and strict cubic separation, compares the analytic moment integrals with 21 independent smooth one-variable numerical quadratures, and reconstructs 48 projected convex hulls from polygonal discretizations of the cylinder's two circular rims. To run it after extracting the complete package, execute `python3 verify.py`. In the reference execution, all checks passed. The finite numerical tests corroborate but do not replace Steps 1–4; the theorem holds for all positive real radii and heights by the analytic argument.

## Relationship to prior work

Finch (2012) develops Haar-projection area and perimeter moments of regular polytopes, especially tetrahedra, cubes, and crosspolytopes; his moment framework motivates the direction-free observable but does not give the present cylinder inverse. Kim, Yaskin, and Zvavitch (2015) study the distribution of projection volumes without labels, proving important general non-identifiability examples; their results do not yield this exact three-moment cylinder reconstruction. Agimelen and collaborators (2014) study size/shape inference from **chord-length histograms** of particle populations and explicitly consider thin cylindrical models. That measurement, model, and inversion problem are different from the exact single-cylinder **projected-area moments** treated here. Prior work on a right cylinder's **joint area–perimeter shadow covariance** computes a different mixed moment and does not imply equality or separation of the first two and third pure area moments. Elementary Cauchy projection formulas underlie the forward geometry but not the inverse branch-separation inequality (4).

## Limitations

No assertion is made about arbitrary convex bodies, elliptic or oblique cylinders, mixtures of particles, nonuniform orientations, empirical noise, optimal statistical sample sizes, or inversion stability. Only the first **two consecutive** moments are proved insufficient; the theorem does not rule out other nonconsecutive pairs of observations. The exact arithmetic of the third-moment separation is sensitive to \(\pi\), but is certified by elementary rational inequalities rather than floating-point tests. An historically equivalent cylinder-specific moment inverse theorem outside the inspected literature remains possible; independent historical-priority review has not been performed.

## References

1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, first public 12 March 2012, https://arxiv.org/html/1203.2464v1 .
2. O. S. Agimelen, P. Hamilton, I. Haley, A. Nordon, M. Vasile, J. Sefcik, A. J. Mulholland, *Estimation of Particle Size Distribution and Aspect Ratio of Non-Spherical Particles From Chord Length Distribution*, arXiv:1408.4399v1, first public 19 August 2014, https://arxiv.org/html/1408.4399v2 .
3. J. Kim, V. Yaskin, A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 22 December 2015, https://arxiv.org/html/1512.07289v1 .
