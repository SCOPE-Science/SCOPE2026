# Exact extremal ellipsoids and a sharp spike threshold for one-apex Euclidean balls

## Finding
For each integer \(d\ge2\), let \(B_2^d\) be the closed unit Euclidean ball and let \(e_1\) be its first coordinate vector. For every \(a\ge1\), define the full-dimensional convex body
\[
K_{d,a}=\operatorname{conv}\bigl(B_2^d\cup\{ae_1\}\bigr).
\]
Write points as \((z,y)\in\mathbb R\times\mathbb R^{d-1}\) and set
\[
E(c;b,r)=\left\{(z,y):\frac{(z-c)^2}{b^2}+\frac{\|y\|_2^2}{r^2}\le1\right\},\qquad b,r>0.
\]
Then the unique maximum-volume inscribed (John) ellipsoid is
\[
J(K_{d,a})=\begin{cases}
B_2^d,&1\le a\le d,\\
E\left(\frac{a-d}{d+1};\frac{a+1}{d+1},\frac{a+1}{d+1}\sqrt{\frac{d^2-1}{a^2-1}}\right),&a>d.
\end{cases}
\]
For the unique minimum-volume enclosing (Löwner) ellipsoid, define
\[
\zeta=-\frac{2}{\sqrt{(d-1)^2a^2+4d}+(d-1)a},\qquad
b_L=\frac{d(a-\zeta)}{d+1},\qquad c_L=a-b_L,\qquad r_L=\sqrt{-d b_L\zeta}.
\]
For all \(a\ge1\), its exact form is
\[
L(K_{d,a})=E(c_L;b_L,r_L).
\]
Thus the added apex leaves the entire John ellipsoid unchanged precisely through the sharp threshold \(a=d\), whereas the Löwner ellipsoid changes as soon as \(a>1\).

The normalized John volume is
\[
\frac{\operatorname{vol}_d(J(K_{d,a}))}{\operatorname{vol}_d(B_2^d)}=
\begin{cases}1,&1\le a\le d,\\
\displaystyle\left(\frac{a+1}{d+1}\right)^d
\left(\frac{d^2-1}{a^2-1}\right)^{(d-1)/2},&a>d.
\end{cases}
\]
The right-hand expression has expansion
\[
1+\frac{(a-d)^2}{2(d^2-1)}+O\bigl((a-d)^3\bigr)
\]
at \(a=d\). Hence this volume response is continuously differentiable but not twice continuously differentiable across the spike threshold.

## Assumptions and scope
The dimension is an integer \(d\ge2\), the spike parameter is real \(a\ge1\), and all volumes and ellipsoid axes use the standard Euclidean metric. Extremality is over **all** nondegenerate affine ellipsoids, not only bodies of revolution. Uniqueness is understood as equality of ellipsoid subsets of \(\mathbb R^d\). The case \(a=1\) is included: the convex body and both ellipsoids coincide with the unit ball. The result asserts no characterization for several exterior points.

## Proof
**1. A contact certificate.** We use the standard necessary-and-sufficient John contact criterion and its Löwner analogue: after an affine map sends a proposed extremal ellipsoid to \(B_2^d\), the appropriate common boundary contacts \(u_i\) have positive weights \(\lambda_i\) satisfying \(\sum_i\lambda_i u_i=0\) and \(\sum_i\lambda_i u_i u_i^T=I_d\); containment and these identities imply uniqueness. For either contact configuration below choose one pole, weighted \(d/(d+1)\), and \(d\) equally weighted contacts at axial coordinate \(\pm1/d\), with transverse components at the vertices of a regular simplex on \(S^{d-2}\). Give the ring total weight \(d^2/(d+1)\). The pole has the opposite axial sign. Explicitly,
\[
\frac{d}{d+1}\cdot1+\frac{d^2}{d+1}\cdot\frac1{d^2}=1,\qquad
\frac{d^2}{d+1}\cdot\frac{1-d^{-2}}{d-1}=1.
\]
The axial barycenter is zero, the simplex has zero transverse barycenter, and all mixed covariances vanish. The weights total \(d\), as required. For the planar case \(d=2\), the transverse regular simplex is the pair \(\{-1,1\}\).

**2. The body profile.** For \(a>1\), rotational symmetry and tangency from the apex to the unit sphere give the exact section radius
\[
R_K(z)=\begin{cases}
\sqrt{1-z^2},&-1\le z\le1/a,\\
\displaystyle\frac{a-z}{\sqrt{a^2-1}},&1/a\le z\le a.
\end{cases}
\]
The conical portion is bounded by the linear support inequalities \(z+\sqrt{a^2-1}\,u\cdot y\le a\), for every \(u\in S^{d-2}\).

**3. John ellipsoid for short spikes.** When \(1\le a\le d\), the unit ball is contained in the body. It touches the body at its negative axial pole and at the sphere latitude \(z=1/d\). Indeed, \(1/d\le1/a\), so the latitude lies on the exposed spherical boundary rather than on the conical extension. In the normalized unit-ball coordinates these are the pole and positive ring of step 1. Their isotropic weights certify that the unit ball is the globally unique John ellipsoid. The endpoint \(a=1\) follows directly because the body is the ball.

**4. John ellipsoid for long spikes.** Assume \(a>d\), and set
\[
b=\frac{a+1}{d+1},\quad c=b-1,\quad
r=b\sqrt{\frac{d^2-1}{a^2-1}}.
\]
The support of \(E(c;b,r)\) in every direction \((1,\sqrt{a^2-1}\,u)\) equals
\[
c+\sqrt{b^2+(a^2-1)r^2}=c+db=a.
\]
Thus the ellipsoid is inside the tangent cone from the apex. Its lower axial endpoint equals \(c-b=-1\), and its conical contacts, normalized to its unit ball, are exactly the positive latitude \(1/d\). Their physical axial coordinate is \(c+b/d=(a-d+1)/d>1/a\), so these are actual contacts with the conical portion of the body.

For \(-1\le z\le1/a\), compare the spherical radius with the ellipsoid slice by defining
\[
\Delta(z)=1-z^2-r^2\left(1-\frac{(z-c)^2}{b^2}\right).
\]
Its quadratic coefficient is \(-1+r^2/b^2<0\) because \(a>d\). We have \(\Delta(-1)=0\). At \(z=1/a\), the sphere and cone coincide, and the already-proved cone containment gives \(\Delta(1/a)\ge0\). Concavity implies \(\Delta(z)\ge0\) throughout the interval. For \(1/a\le z\le a\), cone containment gives precisely the required section inequality. Therefore \(E(c;b,r)\subseteq K_{d,a}\). Applying the certificate from step 1 to its south pole and positive conical contact ring proves global uniqueness.

**5. Löwner ellipsoid.** The displayed \(\zeta\) is the negative root of
\[
d\zeta^2-(d-1)a\zeta=1.
\]
Put \(b=b_L\), \(c=c_L\), \(r=r_L\). The added apex satisfies \(a=c+b\), so it touches the ellipsoid at the positive axial pole. The sphere at latitude \(z=\zeta\) contacts the ellipsoid because
\[
\frac{\zeta-c}{b}=-\frac1d,\qquad
\frac{(\zeta-c)^2}{b^2}+\frac{1-\zeta^2}{r^2}=1,
\]
where the second equality follows by substituting the quadratic equation for \(\zeta\). Since \(a>1\) implies \(-d\zeta<1<a\), we have \(b^2>r^2\). Consequently
\[
q(z)=\frac{(z-c)^2}{b^2}+\frac{1-z^2}{r^2}
\]
is a concave quadratic in \(z\). Its derivative vanishes at \(z=\zeta\), and \(q(\zeta)=1\). Hence \(q(z)\le1\) for all \(-1\le z\le1\); the proposed ellipsoid contains the full unit ball and the extra apex, therefore their convex hull. The apex and the negative contact latitude normalize to the pole and negative ring of step 1, proving uniqueness by the Löwner contact criterion. At \(a=1\), the parameters reduce to \(c=0\), \(b=r=1\), and the conclusion is immediate.

**6. Sharpness and onset.** The inscribed ellipsoid parameters agree with the unit ball at \(a=d\), and the contact certificate proves exact equality throughout \(1\le a\le d\). For \(a>d\) its axial semiaxis is \((a+1)/(d+1)>1\), so the John ellipsoid differs from the ball. Its volume is proportional to \(br^{d-1}\), giving the displayed formula. The logarithmic first derivative on the long-spike side vanishes at \(a=d\); its second derivative there equals \(1/(d^2-1)\). Taylor expansion of the volume ratio yields the quadratic onset and the claimed differentiability boundary. Similarly, the Löwner ellipsoid is the ball only at \(a=1\), since for \(a>1\) it must contain the exterior apex.

## Verification
The attached standalone Python checker implements the exact parameter formulas. Across 320 combinations in dimensions \(2,3,4,5,6,10,20,50\), it independently checks the cone-support identity, the sphere-contact equation, the contact first/second moments, and dense radial containments on 3,001 axial samples per configuration. The observed largest floating-point discrepancy was on the order of \(10^{-16}\). These finite computations are consistency checks; all universal containment, extremality and uniqueness statements follow from the analytical proof above.

## Relationship to prior work
Keith Ball's early account of John's theorem supplies the contact decomposition and general containment framework. Güler and Gürtuna derive exact John–Löwner ellipsoids for ball slabs, truncated cones and cylinders. In contrast, the present object is the **convex hull** of an entire ball and a single exterior point; it is neither the ball intersected with a halfspace nor the truncated-cone body considered there. Its polar is indeed the clipped ball \(B_2^d\cap\{z\le1/a\}\), but origin polarity does not preserve the volume ordering of generally translated ellipsoids. Therefore the slab classification cannot simply be transferred to give the proposed two extremal ellipsoids. Ivanov and collaborators study broader constrained ellipsoids of revolution, but the inspected results do not give the present explicit one-apex classification or threshold. The closest related generic ellipsoid results provide methods, not the exact formulas and the sharp unchanged-John regime.

## Limitations
The classification requires the Euclidean unit ball plus **one** axial exterior point, in all dimensions at least two. It does not treat multiple spikes, non-Euclidean norms or general ball truncations. The mathematical proof and computational checks are internal consistency evidence, not an independent audit. Historical priority remains subject to unindexed or inaccessible earlier literature; an unsuccessful indexed search does not prove novelty. The numerical checker does not provide an infinite-dimensional or exhaustive certificate.

## References
1. K. Ball, *Ellipsoids of maximal volume in convex bodies*, publicly posted 1990-09-25, arXiv:math/9201217.
2. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (first posted 2007-09-05), Sections 2–3, 5–8.
3. G. Ivanov, Z. Lángi, M. Naszódi and Á. Sagmeister, *John Ellipsoids of Revolution*, arXiv:2507.06947 (2025), Sections 1, 4 and 7.
