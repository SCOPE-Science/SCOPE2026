# A sharp contact bifurcation for the Löwner ellipsoid of two unequal balls

## Finding
Let \(d\ge2\), \(0<q<1\), and \(L>0\). Write \(B_d(s,r)=\{x\in\mathbb R^d:\|x-se_1\|_2\le r\}\), and set
\[
K_{d,q,L}=\operatorname{conv}\bigl(B_d(0,1)\cup B_d(L,q)\bigr).
\]
Its unique minimum-volume covering ellipsoid \(E\) is always of the form
\[
E(c,a,b)=\left\{x:\frac{(x_1-c)^2}{a^2}+\frac{\|x_\perp\|_2^2}{b^2}\le1\right\},
\]
with the following **sharp three-regime determination**.

1. If \(0<L\le1-q\), then \(E=B_d(0,1)\).
2. Define \(L_c=d(1-q^2)/((d-1)q)\). If \(1-q<L\le L_c\), put \(H=L+q\), let \(r>0\) uniquely solve \(dr^2+(d-1)Hr=1\), and set
\[
a=\frac{d(H+r)}{d+1},\qquad c=\frac{H-dr}{d+1},\qquad b^2=dar.
\]
Then \(E=E(c,a,b)\). The large sphere touches in one latitude orbit and the smaller sphere only at its outward axial tip.
3. If \(L>L_c\), let
\[
 b_c=\sqrt{\frac{d^2-q^2}{d^2-1}},\quad
 u_1(b)=\sqrt{1-b^{-2}},\quad
 u_2(b)=\sqrt{1-q^2b^{-2}},\quad \eta(b)=u_1(b)u_2(b).
\]
There is exactly one \(b_\infty>b_c\) with \(d\eta(b_\infty)=1\). There is exactly one \(b\in(b_c,b_\infty)\) satisfying
\[
 L=\frac{b\sqrt{d\eta(b)}}{\sqrt{1-d\eta(b)}}(u_1(b)+u_2(b)).
\]
Put \(T=b\sqrt{d\eta(b)/(1-d\eta(b))}\), \(a=\sqrt{b^2+T^2}\), \(c=Tu_1(b)\). Then \(E=E(c,a,b)\). **Both** boundary spheres touch along a nondegenerate latitude orbit. In the normalized ellipsoid, their two axial latitude coordinates \(y_1<0<y_2\) satisfy the universal relation \(y_1y_2=-1/d\).

The relative volume in either nonnested regime is exactly \(ab^{d-1}\), relative to the volume of the unit ball. The transition at \(L=L_c\) is continuous: the smaller sphere's latitude collapses to its outward tip there.

## Assumptions and scope
Euclidean norm, full-dimensional closed balls, \(d\) an integer \(\ge2\), \(0<q<1\), \(L>0\). Radii have been normalized by dividing by the larger radius. "Löwner ellipsoid" means minimum \(d\)-volume enclosing ellipsoid with no axial-symmetry restriction. Claims include the transition values, non-nested and nested regimes, all dimensions, and uniqueness. The two latitude orbits are transverse \((d-2)\)-spheres (two symmetric points when \(d=2\)).

## Proof
**Support and contact criterion.** The support of \(K\) in a unit direction of axial coordinate \(t\in[-1,1]\) is \(h_K(t)=\max\{1,Lt+q\}\). The support of \(E(c,a,b)\), writing \(T^2=a^2-b^2>0\), is \(h_E(t)=ct+\sqrt{b^2+T^2t^2}\). Containment follows exactly when \(h_E(t)\ge1\) and \(h_E(t)\ge Lt+q\) for every \(t\in[-1,1]\).

**Global minimality certificate.** Suppose \(K\subseteq E\), and under the affine normalization \(x\mapsto ((x_1-c)/a,x_\perp/b)\), some measure supported on \(K\cap\partial E\) has mean zero and covariance \(I_d/d\). For any competing ellipsoid, its normalized image is \(v+AB_d\) with symmetric positive-definite \(A\). Containment of the contact points yields \(d^{-1}\operatorname{tr}(A^{-2})+\|A^{-1}v\|^2\le1\). The arithmetic-geometric mean inequality implies \((\det A)^{-2/d}\le d^{-1}\operatorname{tr}(A^{-2})\le1\); hence \(\det A\ge1\). Equality requires \(v=0\) and \(A=I_d\). Thus \(E\) is globally optimal and unique, regardless of the orientation of competing ellipsoids.

**Nested phase.** For \(L\le1-q\), the smaller ball is contained in the unit ball. The entire unit sphere supplies the certificate, proving the first case.

**Single-latitude phase.** For \(H=L+q>1\), the equations in the finding define positive \(a>b\), and direct substitution gives the exact identity
\[
1-\left[\frac{(t-c)^2}{a^2}+\frac{1-t^2}{b^2}\right]
=\frac{a^2-b^2}{a^2b^2}(t+r)^2\qquad(-1\le t\le1).
\]
Hence the unit ball is contained, touching exactly at axial coordinate \(t=-r\); the outward tip \(He_1\) satisfies \(H=c+a\). After normalization the latitude has axial coordinate \(-1/d\), while the tip becomes \(+1\). Give the latitude uniformly distributed transverse directions and mass \(d/(d+1)\), and give the tip mass \(1/(d+1)\). The resulting mean is zero and covariance \(I_d/d\), so the ellipsoid is uniquely volume-minimizing for the unit ball plus the tip.

The smaller sphere is contained exactly when \(q\le b^2/a=dr\). Indeed, convexity of \(g(t)=\sqrt{b^2+(a^2-b^2)t^2}\) yields its tangent inequality at \(t=1\):
\[
h_E(t)-(Lt+q)\ge (b^2/a-q)(1-t).
\]
Conversely, when \(q>b^2/a\), the difference vanishes at \(t=1\) but has positive derivative there, so it is negative for some \(t<1\). Substituting \(r=q/d\) into \(dr^2+(d-1)Hr=1\) gives exactly \(L=L_c\). As \(r\) decreases strictly with \(H\), this proves the stated sharp screening interval and its contacts.

**Double-latitude phase.** For \(b>b_c\), the functions \(u_1,u_2,\eta\) increase strictly; hence \(L(b)=b\sqrt{d\eta/(1-d\eta)}(u_1+u_2)\) increases continuously from \(L_c\) at \(b=b_c\) to \(+\infty\) as \(b\uparrow b_\infty\), proving existence and uniqueness of the scalar root. In the resulting ellipsoid \(T^2=a^2-b^2\), \(c=Tu_1\), and \(L-c=Tu_2\). For \(s=0,L\), minimizing
\[
\sqrt{b^2+T^2t^2}+(c-s)t\quad(-1\le t\le1)
\]
gives \(b\sqrt{1-(c-s)^2/T^2}\), provided \(|c-s|\le T^2/a\). For \(s=0\) this condition holds automatically because \(u_1\le d u_2\); for \(s=L\) it is equivalent to \(u_2\le d u_1\), precisely \(b\ge b_c\). The two minima are therefore exactly \(1\) and \(q\). Both balls are contained, with contact on exactly one latitude per boundary sphere (strict inequality here since \(b>b_c\)).

Normalized contact latitude coordinates are
\[
y_1=-\frac{a u_1}{T},\qquad y_2=\frac{a u_2}{T},\qquad
 y_1y_2=-\frac{a^2u_1u_2}{T^2}=-\frac1d.
\]
Here the last identity follows from \(a^2/T^2=1/(d\eta)\). Take the mixture of uniform transverse contact orbits with masses \(p_1=y_2/(y_2-y_1)\) and \(p_2=-y_1/(y_2-y_1)\). Its mean is zero, its axial variance is \(-y_1y_2=1/d\), and its transverse covariance is also \(I_{d-1}/d\) by rotational symmetry. Apply the global certificate above. Finally the formulas continuously match at \(b=b_c\): there \(u_2=du_1\), \(y_2=1\), and \(L=L_c\). This completes all cases.

## Verification
The included standard scientific Python script `verify.py` computes the three regimes from their explicit scalar equations, tests support inequalities on sampled directions, checks the normalized contact identity, and verifies continuity at the transition over selected dimensions and radii. These are finite diagnostic tests only; every universal claim follows from the analytic proof above. To reproduce, use `python verify.py` with Python 3 and NumPy/SciPy.

## Relationship to prior work
Yıldırım, *On the Minimum Volume Covering Ellipsoid of Ellipsoids* (2006), studies approximate minimum-volume enclosing ellipsoids of general convex hulls of ellipsoids. Güler and Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases* (2007), develop optimality conditions and explicitly solve truncations, cones, and cylindrical shapes. These works explain general certificate techniques; neither of their inspected available results supplies the unequal-ball exact bifurcation or the scalar two-contact formula. The equal-radius capsule and the limiting point-hull give distinct endpoint geometries and do not imply the full unequal-radius parameter transition. This is a comparison of mathematical statements, not a claim of exhaustive historical priority.

## Limitations
This is an exact Euclidean ball-hull result for two balls, not arbitrary ellipsoids, three or more balls, or norms other than the Euclidean norm. A general closed form in radicals for the second-phase scalar root is not asserted. Historical-priority risk remains, particularly from older special-case computations in the optimization or computational-geometry literature; the full Yıldırım article was not accessible for direct comparison. No independent review has been performed.

## References
1. E. Alper Yıldırım, *On the Minimum Volume Covering Ellipsoid of Ellipsoids*, SIAM Journal on Optimization **17** (2006), 621–641, DOI: 10.1137/050622560. First verified public online date: 2006-09-15.
2. Osman Güler and Filiz Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, publicly posted 2007-09-05, especially Sections 2 and 8.
