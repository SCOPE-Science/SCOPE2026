# Exact extremal ellipsoids and contact transition for regular-polygon-spiked balls

## Finding
Fix integers \(d\ge3\) and \(m\ge5\), and a real number \(a\ge1\). In the orthogonal decomposition \(\mathbb R^d=V\oplus W\), where \(V=\mathbb R^2\) and \(W=\mathbb R^{d-2}\), let \(v_j=(\cos(2\pi j/m),\sin(2\pi j/m))\), \(0\le j<m\), and set
\[
P_m=\operatorname{conv}\{(v_j,0):0\le j<m\},\quad K_{d,m,a}=\operatorname{conv}\bigl(B_2^d\cup aP_m\bigr).
\]
Write \(g_m=\cos(\pi/m)\), \(b=ag_m\), and \(a_*=\sqrt{d/2}/g_m\). Define \(E(A,B)=\{(x,y)\in V\oplus W:\|x\|^2/A^2+\|y\|^2/B^2\le1\}\).

**Theorem.** The unique maximum-volume inscribed (John) ellipsoid is \(J(K_{d,m,a})=E(A,B)\), where
\[
(A^2,B^2)=\begin{cases}
(1,1),&1\le a\le a_*,\\
\left(\dfrac{2b^2}{d},\dfrac{(d-2)b^2}{d(b^2-1)}\right),&a>a_*.
\end{cases}
\]
The unique minimum-volume enclosing (Löwner) ellipsoid is
\[
L(K_{d,m,a})=E(a,1).
\]
In particular the exact ellipsoid-volume ratio is
\[
\mathcal R_{d,m}(a)=\frac{\operatorname{vol}_d L(K_{d,m,a})}{\operatorname{vol}_d J(K_{d,m,a})}=
\begin{cases}
a^2,&1\le a\le a_*,\\
\dfrac{d}{2g_m^2}\left[\dfrac{d(b^2-1)}{(d-2)b^2}\right]^{(d-2)/2},&a>a_*.
\end{cases}
\]
The ratio increases strictly with \(a\), starts at \(1\), and has the sharp unattained limit
\[
\mathcal R_{d,m}(\infty)=\frac{d}{2g_m^2}\left(\frac d{d-2}\right)^{(d-2)/2}.
\]
It is once continuously differentiable, but not twice differentiable, at the contact transition \(a=a_*\). In fact, with \([f'']_{a_*}=f''(a_*+)-f''(a_*- )\),
\[
\left[(\log\mathcal R_{d,m})''\right]_{a_*}=-\frac{4d}{(d-2)a_*^2}.
\]
The planar regular-polygon vertex orbit is the full contact set of the enclosing ellipsoid on the planar spike boundary, and its other contacts include the transverse unit sphere. Above the John transition, the inscribed ellipsoid is certified by the \(m\) edge-normal contact orbits with transverse spherical coordinates described in the proof.

## Assumptions and scope
The Euclidean unit ball is closed. The polygon is the regular circumradius-one \(m\)-gon embedded in a fixed two-dimensional linear subspace; no additional points are included. The parameter \(a\) uniformly scales all polygon vertices, and the ambient dimension is an integer at least three. The restriction \(m\ge5\) isolates genuine nonrectangular polygonal spike configurations; no claim is made here for arbitrary irregular polygons, or for unrelated polytope truncations. The case \(a=1\) yields exactly the unit ball, and the transition satisfies \(a_*>1\).

## Proof
**1. Symmetry reduction.** Uniqueness of either extremal ellipsoid and invariance of \(K_{d,m,a}\) under the regular polygon's dihedral group on \(V\) and the full orthogonal group on \(W\) force both ellipsoids to be centered at the origin and to have the form \(E(A,B)\). Indeed, the polygon rotation has no nonzero fixed vector in \(V\), the transverse sign reversal fixes only \(y=0\), and invariance of a symmetric shape matrix forces scalar diagonal blocks with no cross terms. This also applies for \(d=3\), when \(W\) is one-dimensional.

**2. Exact support-function containment.** Write a unit normal \(u=(t\xi,\sqrt{1-t^2}\,\omega)\), with \(0\le t\le1\), \(\xi\in S^1\), and \(\omega\in S^{d-3}\) (the latter is \(S^0\) for \(d=3\)). Then
\[
h_K(u)=\max\{1,at\max_{0\le j<m}\langle\xi,v_j\rangle\},\quad
h_{E(A,B)}(u)^2=A^2t^2+B^2(1-t^2).
\]
The minimum over \(\xi\) of \(\max_j\langle\xi,v_j\rangle\) is exactly the regular polygon inradius \(g_m=\cos(\pi/m)\), attained at each outward edge-normal direction \(\xi_j=(\cos((2j+1)\pi/m),\sin((2j+1)\pi/m))\). Hence, **for every** \(A,B>0\),
\[
E(A,B)\subseteq K \quad\Longleftrightarrow\quad
A^2t^2+B^2(1-t^2)\le\max\{1,bt\}^2\quad\text{for all }t\in[0,1].
\]
If \(b\le1\), this is equivalent to \(A^2\le1\) and \(B^2\le1\), so the unit ball is optimal. If \(b>1\), put \(s=t^2\). The expression on each of \([0,b^{-2}]\) and \([b^{-2},1]\) is affine in \(s\). Checking its endpoints gives the **equivalent** inequalities
\[
B^2\le1,\qquad A^2+(b^2-1)B^2\le b^2.
\]
The endpoint \(s=1\) inequality \(A^2\le b^2\) follows automatically from the latter. Thus no unsampled direction is omitted.

**3. Solving the John determinant problem.** For \(b>1\), put \(y=B^2\). Since volume is proportional to \(A^2B^{d-2}\), one maximizes
\[
\Phi(y)=\log\left(b^2-(b^2-1)y\right)+\frac{d-2}{2}\log y,
\qquad 0<y\le1.
\]
This is strictly concave because
\[
\Phi''(y)=-\frac{(b^2-1)^2}{(b^2-(b^2-1)y)^2}-\frac{d-2}{2y^2}<0.
\]
Its only unconstrained maximum lies at \(y_0=(d-2)b^2/[d(b^2-1)]\), yielding \(A^2=2b^2/d\). It belongs to \((0,1)\) precisely when \(b^2>d/2\). Otherwise \(y=1\), \(A^2=1\) is the unique maximum. Combining this with the case \(b\le1\) proves the displayed John formula. Symmetry and uniqueness rule out any off-center or nonsymmetric competitor.

**4. Explicit isotropic John contacts.** There is a direct optimality certificate independent of the determinant comparison. For \(b\le\sqrt{d/2}\), let \(t=\sqrt{2/d}\); the unit-normal points \((t\xi_j,\sqrt{1-t^2}\,\omega)\) are contacts of the inscribed unit ball with \(K\). For \(b>\sqrt{d/2}\), use \(t=1/b\), and define normalized contact points on the John unit sphere as
\[
p_{j,\omega}=\left(\frac A b\xi_j,\ B\sqrt{1-b^{-2}}\,\omega\right).
\]
Here \(A^2/b^2=2/d\) and \(B^2(1-b^{-2})=(d-2)/d\), so these points have unit norm. The underlying ellipsoid support equals the body support \(1\) in the directions \((b^{-1}\xi_j,\sqrt{1-b^{-2}}\,\omega)\), hence they are genuine boundary contacts after normalizing by \(\operatorname{diag}(A^{-1}I_2,B^{-1}I_{d-2})\). Uniformly average over \(j\) and uniformly over \(\omega\in S^{d-3}\). Both means vanish, and the covariance equals
\[
\operatorname{diag}\left(\frac1d I_2,\frac1d I_{d-2}\right)=\frac1d I_d.
\]
Multiplying this probability measure by \(d\) gives John's positive isotropic contact certificate. At and below the transition the identical covariance computation applies with \(t=\sqrt{2/d}\). This confirms global John optimality even without assuming symmetry of competitors.

**5. Löwner ellipsoid and its contacts.** Any symmetric candidate \(E(C,D)\) containing \(K\) contains the transverse unit ball, so \(D\ge1\), and contains the polygon vertices \((av_j,0)\), so \(C\ge a\). Equality in both conditions gives \(L=E(a,1)\), which contains the ball and all vertices and is therefore feasible; uniqueness and symmetry prove global optimality. Its normalized contact measure gives total probability \(2/d\) uniformly to the \(m\) planar vertex contacts and total probability \((d-2)/d\) to the transverse unit sphere. The mean is zero and covariance is \(I_d/d\), as required by the Löwner contact criterion.

**6. Ratio, monotonicity, and differentiability.** Volumes equal \(\kappa_d\) times the product of semiaxes, so the ratio is \(a^2/(A^2B^{d-2})\) and simplifies to the stated branches. For \(a>a_*\), differentiation with \(b=ag_m\) gives
\[
\frac{d}{da}\log\mathcal R_{d,m}(a)=\frac{d-2}{a(b^2-1)}>0;
\]
for \(a<a_*\) it is \(2/a>0\). The two values agree at \(b^2=d/2\), proving \(C^1\) regularity, while one further derivative gives the displayed nonzero jump. Taking \(a\to\infty\) proves the sharp unattained endpoint.

## Verification
The proof uses exact support functions in **all directions**, strict concavity on the entire feasible semiaxis domain, and explicit John/Löwner positive contact measures. The separate standard-library program `verify.py` checks the algebraic contact identities and support inequalities over 96 dimension–polygon–parameter configurations; additional direct constrained numerical optimizations of the reduced strictly concave objective agree with the formulas. These finite checks corroborate but are not substitutes for the all-dimensional proof.

## Relationship to prior work
The extremal-ellipsoid contact characterizations are due to Fritz John and are discussed in Keith Ball's 1990 preprint and Güler and Gürtuna's 2007 study. Ball's work gives a broader obstruction involving sufficiently large lower-dimensional ellipsoids inside a body in John position, but does not determine the present convex hull's exact John/Löwner ellipsoids, discrete-polygon contact orbit, or piecewise volume-ratio profile. Güler and Gürtuna compute ellipsoids for slabs and truncated second-order cones/cylinders rather than a Euclidean ball with a coplanar regular polygon of protruding vertices. A separately published half-cone John formula concerns a truncated circular cone, and a published six-spike spherical-hull result concerns illumination rather than ellipsoid optimization. In the available comparisons, neither implies the exact classification stated here.

## Limitations
The claimed formulas concern only the stated regular-polygon-spiked balls with \(d\ge3\), \(m\ge5\), and \(a\ge1\). They are not presented as a new general theorem about all convex bodies or all polygonal spike configurations. An independent historical-priority assessment has not been performed; older unindexed convex-approximation and extremal-ellipsoid literature could contain equivalent special cases. The numerical tests cover finite parameter sets, while the theorem itself is analytic.

## References
1. Keith Ball, *Ellipsoids of maximal volume in convex bodies*, arXiv:math/9201217v1, first public version 25 September 1990; later *Geometriae Dedicata* 41 (1992), 241–250.
2. Osman Güler and Filiz Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, 5 September 2007, especially Sections 2–4 and 8.
3. *Exact John ellipsoid of the Khachiyan half-cone*, publicly available mathematical record at `https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-john-ellipsoid-of-the-khachiyan-half-cone--12746f7a27eb` (distinct conic body).
4. *Endpoint instability of the six-spike octahedral cap body*, publicly available mathematical record at `https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-endpoint-instability-of-the-six-spike-octahedral-cap-body--1f124f444fca` (illumination invariant rather than ellipsoidal invariant).
