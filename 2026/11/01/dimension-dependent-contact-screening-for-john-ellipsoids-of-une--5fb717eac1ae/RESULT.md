# Dimension-dependent contact screening for John ellipsoids of unequal-ball lenses

## Finding

Let \(d\ge 2\) be an integer, \(0<q<1\), and \(0\le L<1+q\). For the full-dimensional spherical lens
\[
 K= B_2^d(0,1)\cap B_2^d(Le_1,q),
\]
its unique maximum-volume inscribed ellipsoid is
\[
 E=\left\{(x,y)\in\mathbb R\times\mathbb R^{d-1}:
       \frac{(x-c)^2}{a^2}+\frac{\|y\|_2^2}{b^2}\le1\right\}.
\]
The following formulas determine its center \(c\), axial semiaxis \(a\), transverse semiaxis \(b\), and all boundary contacts. They are exact, not numerical optimization procedures.

**Nested regime.** If \(0\le L\le1-q\), then \(E=B_2^d(Le_1,q)\), so \(c=L\) and \(a=b=q\).

**Axial-pole regime.** Suppose \(1-q<L<1+q\) and either \(q\le 1/d\), or \(q>1/d\) and
\[
 L\le L_c:=\frac{d(1-q^2)}{d-1}.
\]
There is a unique \(h>1\) solving
\[
 L=1+\frac{q(h-d-1)}{\sqrt{h(d^2+h-1)}}.
\]
Then
\[
 a=\frac{dq}{\sqrt{h(d^2+h-1)}},\qquad
 b=a\sqrt h,\qquad c=1-a.
\]
The larger ball contacts \(E\) only at the axial pole \((1,0)\); the smaller ball contacts it along the entire latitude corresponding to ellipsoid-normalized axial coordinate \(-1/d\). Thus the larger sphere's contact set is a singleton, even as the lens becomes arbitrarily thin, whenever \(q\le1/d\).

**Two-latitude regime.** This regime occurs exactly when \(q>1/d\) and \(L_c<L<1+q\). There is a unique
\[
  \frac1{\sqrt{dq}}<t<1
\]
solving
\[
 L=\frac{\theta(t)\left(t+\frac1{dt}\right)}{
           \sqrt{(1+\theta(t))(1+\theta(t)t^2)}},\qquad
 \theta(t)=\frac{d^2(1-q^2)t^2}{d^2q^2t^4-1}.
\]
Set
\[
 a=\frac1{\sqrt{(1+\theta)(1+\theta t^2)}},\quad
 b=a\sqrt{1+\theta},\quad c=a\theta t.
\]
Both balls have a nondegenerate latitude of contact, at normalized axial coordinates \(t\) and \(-1/(dt)\), respectively. Their product is identically \(-1/d\) in all dimensions and for every admissible separation.

The transition \(L=L_c\) is continuous: the larger-ball contact latitude collapses to its axial pole. When \(q\le1/d\), \(L_c\ge1+q\) and the two-latitude regime disappears entirely. In every regime the optimal volume is \(\kappa_d a b^{d-1}\), where \(\kappa_d\) is the volume of the unit Euclidean \(d\)-ball.

## Assumptions and scope

All balls are closed Euclidean balls and \(q\) denotes the smaller radius divided by the larger radius, normalized to one. A rigid motion puts their centers on the first coordinate axis. The strict inequality \(L<1+q\) ensures nonempty interior. At \(L=1+q\), their intersection is a singleton and no positive-volume inscribed ellipsoid exists; this degenerate endpoint is excluded. For \(q=1\), the equal-radius symmetric case has additional symmetry and is not claimed here. A latitude means all points \((c+a s,b\sqrt{1-s^2}\,v)\), with \(v\in S^{d-2}\), for a fixed \(-1<s<1\); in dimension two \(S^0\) denotes its two points. All uniqueness statements concern arbitrary ellipsoids in \(\mathbb R^d\), not just axial ellipsoids.

## Proof

**1. A one-variable containment certificate.** Parameterize the boundary of any candidate axial ellipsoid by
\[
 (x,y)=(c+as,\ b\sqrt{1-s^2}\,v),\qquad -1\le s\le1,\quad v\in S^{d-2}.
\]
For a containing ball with axial center \(s_0\) and radius \(R\), the squared distance from this boundary point to \(s_0e_1\) is
\[
 Q_{s_0}(s)=(c+as-s_0)^2+b^2(1-s^2).
\]
When \(b>a\), write \(\delta=b^2-a^2>0\). Completing the square shows \(Q_{s_0}\) is a strictly concave quadratic with vertex
\[
 u_{s_0}=\frac{a(c-s_0)}{\delta},\qquad
 Q_{s_0}(s)=Q_{s_0}(u_{s_0})-\delta(s-u_{s_0})^2.
\]
Consequently \(Q_{s_0}(s)\le R^2\) for all \(-1\le s\le1\) is a global containment certificate, and its equality points exactly determine sphere contacts. This boundary containment extends to the entire ellipsoid by convexity of Euclidean balls.

**2. Axial-pole regime.** Substitute the displayed formulas for \(a,b,c,L\), with \(h>1\). Direct substitution yields
\[
 Q_L(s)-q^2=-\delta\left(s+\frac1d\right)^2.
\]
For the larger unit ball one has \(Q_0(1)=1\), and the vertex position is
\[
 u_0=\frac{a c}{\delta}=\frac{1-a}{a(h-1)}.
\]
Thus \(Q_0(s)\le1\) throughout \([-1,1]\) precisely when \(u_0\ge1\), equivalent to \(ah\le1\). Squaring positive terms gives the explicit condition
\[
 (d^2q^2-1)h\le d^2-1.
\]
If \(q\le1/d\), the condition holds for all \(h>1\). Otherwise its endpoint is
\[
 h_c=\frac{d^2-1}{d^2q^2-1}.
\]
The map from \(h\) to \(L\) is strictly increasing, because its derivative is
\[
 \frac{q(d+1)^2(h+d-1)}{2[h(d^2+h-1)]^{3/2}}>0.
\]
It takes \(h=1\) to \(L=1-q\), and tends to \(1+q\) as \(h\to\infty\). Substitution at \(h=h_c\) gives exactly \(L_c=d(1-q^2)/(d-1)\). For \(u_0\ge1\), the larger sphere therefore touches only at \(s=1\), while the smaller sphere contacts at \(s=-1/d\).

**3. Two-latitude regime.** Put \(t\in(1/\sqrt{dq},1)\), and define \(\theta,a,b,c,L\) as above, so \(b^2-a^2=a^2\theta\). Then the concave quadratics obey two exact identities:
\[
 Q_0(s)-1=-a^2\theta(s-t)^2,\qquad
 Q_L(s)-q^2=-a^2\theta\left(s+\frac1{dt}\right)^2.
\]
For clarity, the first equality follows from \(c=a\theta t\) and \(a^2(1+\theta)(1+\theta t^2)=1\). The second follows from \(c-L=-a\theta/(dt)\) and
\[
 q^2=\frac{1+\theta/(d^2t^2)}{1+\theta t^2},
\]
which is precisely the equation defining \(\theta(t)\). Both spheres contain the whole ellipsoid and have exactly the stated contact latitudes.

To establish uniqueness of the scalar parameter, write \(u=t^2\), \(v=q^2\),
\[
 A=d^2u(vu+1-v)-1,\qquad B=d^2u^2-1.
\]
On \(1/(dq)<u<1\), both \(A\) and \(B\) are positive, and the displayed separation satisfies
\[
 L^2=\frac{d^2(1-v)^2u(du+1)^2}{AB}.
\]
After differentiating, with \(z=du>1\), the numerator of the negative derivative contains the positive factor
\[
 T=v(z+1)^3(z-1)+(1-v)\big((2d+1)z^2-2z-1\big)>0.
\]
Indeed
\[
 \frac{dL^2}{du}=-\frac{d^2(1-v)^2(du+1)^2T}{A^2B^2}<0.
\]
The second parenthesis is strictly positive for \(z>1\), \(d\ge2\); at \(z=1\) it is \(2d-2>0\) and its derivative is positive. At \(t=1\), \(L=L_c\); as \(t\downarrow1/\sqrt{dq}\), \(L\uparrow1+q\). Therefore every \(L_c<L<1+q\) has exactly one qualifying \(t\).

**4. Global maximality and uniqueness.** Affinely normalize the constructed ellipsoid by \(z=((x-c)/a,y/b)\), so it becomes the unit ball. For an axial contact latitude of normalized coordinate \(s\), the uniform distribution on its transverse sphere has mean \((s,0)\) and covariance-second-moment matrix
\[
 \operatorname{diag}\left(s^2,\ \frac{1-s^2}{d-1}I_{d-1}\right).
\]
For the axial-pole regime place probability mass \(w_1=1/(d+1)\) at \(s_1=1\) and \(w_2=d/(d+1)\) uniformly on \(s_2=-1/d\). For the two-latitude regime put
\[
 (s_1,s_2)=\left(t,-\frac1{dt}\right),\qquad
 w_1=\frac{-s_2}{s_1-s_2},\qquad
 w_2=\frac{s_1}{s_1-s_2}.
\]
All weights are positive; in both regimes \(w_1s_1+w_2s_2=0\) and
\[
 w_1s_1^2+w_2s_2^2=-s_1s_2=\frac1d.
\]
The resulting contact measure thus has mean zero and second moment \(I_d/d\). These are John's exact sufficiency conditions for the unit ball to be the unique maximum-volume inscribed ellipsoid, after multiplying the probability weights by \(d\). The nested case is immediate. This establishes global optimality and uniqueness even against all translated, tilted, and nonsymmetric competing ellipsoids.

## Verification

The included dependency-free `verify.py` implements both unique scalar root solves, independently maximizes the exact quadratic distance-to-sphere functions over \([-1,1]\), checks the contact first and second moments, and tests nested, one-pole, two-latitude, and transition-adjacent parameter cases. Running `python3 verify.py` passed 675 \((d,q,L)\) configurations. The analytic square identities, strict derivative signs, and John's criterion constitute the infinite-dimensional proof; finite diagnostics are corroboration only. The normalized John contact measure can also be discretized on each sphere using a symmetric finite unit-vector ensemble with transverse second moment \(I_{d-1}/(d-1)\).

## Relationship to prior work

John's extremal-ellipsoid criterion is classical. Güler and Gürtuna (2007, arXiv:0709.0707v1) give a general modern treatment with exact results for slabs, truncated second-order cones, and cylinders; those explicit families do not identify the unequal-radius, two-sphere intersection or its contact bifurcation. Uhler and Wright's *Packing Ellipsoids with Overlap* uses mathematical programming for overlap of ellipsoids, discussing a general maximum-volume inscribed-ellipsoid formulation but employing a different trace-based overlap objective; its material inspected does not supply these scalar formulas. Kahan's work concerns a circumscribing ellipsoid for intersections, principally of concentrically centered ellipsoids, an opposite optimization. General SDP formulations for arbitrary ellipsoid intersections provide numerical characterization but do not themselves imply the present sharp \(q=1/d\) screening threshold or exact contact classes. The equal-radius lens has a separate reflection-symmetric structure; that result does not imply this unequal-radius boundary.

## Limitations

This is a mathematical exact characterization, not an independent historical-priority certification. In particular, an equivalent older special case may exist under alternative terminology in ellipsoidal approximation or optimal design literature. The statement excludes tangent/empty intersections and equal-radius input. Finite numerical checks do not establish the general theorem. General noncoaxial balls reduce by rigid motion to the stated setting, but intersections of three or more balls and arbitrary ellipsoids are not classified here.

## References

1. Osman Güler and Filiz Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, first publicly submitted 2007-09-05, https://arxiv.org/abs/0709.0707 .
2. Caroline Uhler and Stephen J. Wright, *Packing Ellipsoids with Overlap*, available research PDF, https://optimization-online.org/wp-content/uploads/2012/04/3418.pdf .
3. W. Kahan, *Circumscribing an Ellipsoid about the Intersection of Two Ellipsoids*, https://people.eecs.berkeley.edu/~wkahan/Ellipint.pdf .
4. Fritz John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant*, 1948, pp. 187–204.
