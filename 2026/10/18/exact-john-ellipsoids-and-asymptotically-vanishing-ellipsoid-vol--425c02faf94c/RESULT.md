# Exact John ellipsoids and asymptotically vanishing ellipsoid-volume deficit for two-point spindles

## Finding

Let \(m\ge2\), \(0<d<1\), and let \(S_m(d)\subset\mathbb R\times\mathbb R^{m-1}\) be the unit-radius spindle (unit-ball convex hull) of the two points \(\pm d e_1\). Put
\[
c=\sqrt{1-d^2},\qquad q=1-c,\qquad D=d^2.
\]
Its unique maximum-volume inscribed ellipsoid (John ellipsoid) is
\[
E_m(d)=\left\{(t,y):\frac{t^2}{z_m}+\frac{\|y\|_2^2}{r_m^2}\le1\right\},
\]
where
\[
z_m=\frac{2mD}{2m-1+D+\sqrt{(1-D)\{4m(m-1)+1-D\}}},
\qquad r_m^2=\frac{z_m(D-z_m)}{1-z_m}.
\]
In particular, \(q<z_m<D\), and the entire contact set consists of the two rotational orbits
\[
\left\{\left(\pm\sqrt{z_m/m},\ r_m\sqrt{(m-1)/m}\,v\right):v\in S^{m-2}\right\}.
\]
After mapping the ellipsoid to the unit ball, all contacts lie at the **universal axial latitudes** \(\pm1/\sqrt m\), independent of \(d\).

Let \(\kappa_m=\pi^{m/2}/\Gamma(m/2+1)\) be the volume of the Euclidean unit \(m\)-ball. For every fixed \(d\in(0,1)\), as \(m\to\infty\),
\[
\begin{aligned}
\operatorname{Vol}_m(S_m(d))
 &=\kappa_m q^{m-1/2}\left(1+\frac{3c}{8m}+O_d(m^{-2})\right),\\
\operatorname{Vol}_m(E_m(d))
 &=\kappa_m q^{m-1/2}\left(1+\frac{c}{8m}+O_d(m^{-2})\right),\\
\frac{\operatorname{Vol}_m(S_m(d))}{\operatorname{Vol}_m(E_m(d))}
 &=1+\frac{c}{4m}+O_d(m^{-2}).
\end{aligned}
\]
Thus the exact John ellipsoid fills all but a sharply determined first-order fraction of the spindle's volume in high dimension, although it does not fill the spindle setwise.

## Assumptions and scope

The radius of the defining balls is one. The two endpoints are separated by \(2d\), with \(0<d<1\); this excludes a singleton and the limiting Euclidean ball. The dimension \(m\ge2\) is an integer. All ellipsoids are ordinary Euclidean full-dimensional ellipsoids, without an assumed alignment: symmetry and uniqueness force the claimed alignment. The asymptotic error terms are for fixed \(d\), not uniform as \(d\) approaches zero or one. The surface \(S^{0}\) in dimension two means two points.

The spindle is the ball hull \(\bigcap\{B(a,1):\{-de_1,de_1\}\subset B(a,1)\}\), rather than the intersection of just the two unit balls centered at the endpoints. Its exact meridian representation is
\[
S_m(d)=\{(t,y):|t|\le d,\ \|y\|_2\le R(t)\},
\qquad R(t)=\sqrt{1-t^2}-c.
\]
The distinction between a spindle and a two-ball lens is essential.

## Proof

**1. Symmetry reduction.** The meridian formula above follows either from the unit-ball-hull definition or by intersecting the radius-one balls whose centers run through the perpendicular sphere of radius \(c\) in the central hyperplane. The spindle is invariant under axial reflection and every rotation of \(\mathbb R^{m-1}\). Uniqueness of the John ellipsoid and these symmetries imply that its center is the origin and its transverse semiaxes coincide. Every candidate therefore has the form
\[
E(s,r)=\{(t,y):t^2/s^2+\|y\|_2^2/r^2\le1\},
\qquad 0<s\le d,\ r>0.
\]
The inclusion criterion is exactly
\[
r\le\inf_{0\le t<s}\frac{\sqrt{1-t^2}-c}{\sqrt{1-t^2/s^2}}.
\]
Write \(z=s^2\) and \(Y(t)=\sqrt{1-t^2}\). For \(0<t<s\), the logarithmic derivative of the displayed ratio has the sign of \(1-z-cY(t)\). This expression increases strictly with \(t\). If \(z\le q\), its minimum is at \(t=0\) and the largest permissible transverse radius is \(r=q\). If \(q<z<D\), the ratio has a unique minimum at the interior point determined by \(Y(t_*)=(1-z)/c\). At that point,
\[
t_*^2=1-\frac{(1-z)^2}{c^2},\qquad
r^2=z\left(1-\frac{c^2}{1-z}\right)=\frac{z(D-z)}{1-z}.
\]
At \(z=D\) the transverse radius tends to zero, so a maximum occurs inside the parameter range.

**2. Maximization and contact geometry.** For \(z\le q\), the ellipsoid volume \(\kappa_m q^{m-1}\sqrt z\) increases strictly. For \(q<z<D\), maximizing volume is equivalent to maximizing
\[
z^m\left(\frac{D-z}{1-z}\right)^{m-1}.
\]
Its logarithmic derivative vanishes exactly when
\[
m(D-z)(1-z)=(m-1)c^2z,
\quad\text{equivalently}\quad
mz^2-(2m-1+D)z+mD=0.
\]
The left side minus the right side of the first equation is strictly decreasing on \((q,D)\), positive at \(q\), and negative at \(D\). Hence the unique optimum is the smaller quadratic root; rationalizing that root gives the stated stable formula for \(z_m\).

Substituting the optimum relation into the contact equation yields \(t_*^2=z_m/m\). Since the ratio in step 1 has only one interior minimizer, these are precisely the two contact orbits. Transforming by \((t,y)\mapsto(t/\sqrt{z_m},y/r_m)\) sends them to vectors
\[
\left(\pm\frac1{\sqrt m},\sqrt{\frac{m-1}m}\,v\right),\qquad v\in S^{m-2}.
\]
The centered probability measure obtained by taking equiprobable signs and uniform \(v\) has second moment matrix \(I_m/m\). Multiplying this measure by \(m\) therefore gives John's exact isotropic contact certificate. It independently proves global optimality among **all** inscribed ellipsoids, not only axially aligned candidates. Uniqueness follows from John's ellipsoid theorem.

**3. High-dimensional volume comparison.** The source meridian representation gives the exact integral
\[
\operatorname{Vol}_m(S_m(d))=
2\kappa_{m-1}\int_0^d\left(\sqrt{1-t^2}-c\right)^{m-1}\,dt.
\]
Set \(k=m-1\) and \(t=\sqrt{q/k}\,u\). On every bounded \(u\)-interval,
\[
k\log\frac{\sqrt{1-qu^2/k}-c}{q}
=-\frac{u^2}{2}-\frac{(1+q)u^4}{8k}+O_d\!\left(\frac{u^6+u^8}{k^2}\right).
\]
Uniform Gaussian domination on a growing \(u\)-interval, with an exponentially small complementary integral, justifies termwise integration. The fourth moment of a standard Gaussian is three; hence
\[
\int_0^d R(t)^k\,dt=
q^k\sqrt{\frac{\pi q}{2k}}
\left(1-\frac{3(1+q)}{8k}+O_d(k^{-2})\right).
\]
The gamma-ratio expansion
\[
\frac{\kappa_{m-1}}{\kappa_m}\sqrt{\frac{2\pi}{m-1}}
=1+\frac3{4(m-1)}+O(m^{-2})
\]
proves the first volume formula.

Expanding the smaller quadratic root and the transverse semiaxis yields
\[
z_m=q+\frac{qc}{2m}+O_d(m^{-2}),\qquad
r_m=q\left(1-\frac{c}{8m^2}+O_d(m^{-3})\right).
\]
It follows that \(\sqrt{z_m}\,r_m^{m-1}=q^{m-1/2}(1+c/(8m)+O_d(m^{-2}))\). Multiply by \(\kappa_m\) for the John volume, and divide the two expansions for the asserted sharp ratio.

## Verification

The attached `check_spindle_john.py` separately checks the quadratic stationarity identity, the four-sign rotational contact covariance, the meridian inclusion and unique contact latitude, the one-dimensional global volume optimum, and numerical convergence to the two sharp asymptotic coefficients. All mathematical claims for arbitrary dimensions and parameters are established by the proof; the finite computations are supplementary checks, not an exhaustive certificate.

## Relationship to prior work

Artstein-Avidan and Florentin, *Symmetrizations of Ball-Bodies* (arXiv:2602.14090, first public February 15, 2026), Proposition 3.2, give an exact one-variable volume integral for two-point ball hulls and establish convexity of that volume under endpoint displacement. This paper motivates the present question but does not state the John semiaxes, universal contact orbits, or the sharp high-dimensional John-volume deficit. Bezdek, Lángi, Naszódi, and Papez, *Ball-Polyhedra* (arXiv:1110.4329; journal publication 2007), and Lángi, Naszódi, and Talata, *Ball and Spindle Convexity with respect to a Convex Body* (2011), define the spindle/ball-hull construction. Their spindle-convexity, separation, and covering results do not supply this ellipsoid classification. John's general contact theorem is a standard tool, not a prior evaluation of this particular body. A specialized unindexed treatment under another name for circular spindle bodies remains a priority risk.

## Limitations

The asymptotic expansion holds for fixed \(0<d<1\) and is not claimed uniform in the degenerating endpoint regimes. The ellipsoid is not identical to the spindle at any finite \(m\) and \(0<d<1\); the result concerns volume ratio rather than Hausdorff approximation or arbitrary ball-polyhedra. Exact closed forms for all other intrinsic volumes are not asserted. No independent audit of the finding has been performed.

## References

1. S. Artstein-Avidan and D. I. Florentin, *Symmetrizations of Ball-Bodies*, arXiv:2602.14090 (2026), especially Proposition 3.2 and Eq. (5). https://arxiv.org/html/2602.14090
2. K. Bezdek, Z. Lángi, M. Naszódi, P. Papez, *Ball-Polyhedra*, Discrete & Computational Geometry 38 (2007), 201–230; arXiv:1110.4329 (2011 public preprint), especially Definition 2.1 and Remark 2.2. https://arxiv.org/pdf/1110.4329
3. Z. Lángi, M. Naszódi, I. Talata, *Ball and Spindle Convexity with respect to a Convex Body* (2011), especially Definition 1.2 and the general compactness argument in Section 7. https://real.mtak.hu/26367/1/paper.pdf
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant* (1948), 187–204. John's maximal-inscribed-ellipsoid contact characterization is used in its standard form.
