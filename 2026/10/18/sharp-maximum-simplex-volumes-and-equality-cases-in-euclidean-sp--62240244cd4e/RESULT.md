# Sharp maximum-simplex volumes and equality cases in Euclidean spherical caps

## Finding
For every integer \(n\ge2\) and cap height \(0<h\le2\), let
\[
C_{n,h}=\{(x,z)\in\mathbb R^{n-1}\times\mathbb R:\ \|x\|^2+z^2\le1,\ z\ge1-h\}.
\]
If \(M_n(h)\) is the greatest Euclidean \(n\)-volume of any simplex contained in \(C_{n,h}\), then
\[
\boxed{
M_n(h)=\begin{cases}
\displaystyle\frac{h}{n}\,\frac{n^{n/2}}{(n-1)!(n-1)^{(n-1)/2}}\,[h(2-h)]^{(n-1)/2},&0<h\le1+\frac1n,\\[7pt]
\displaystyle\frac{(n+1)^{(n+1)/2}}{n!\,n^{n/2}},&1+\frac1n\le h\le2.
\end{cases}}
\]
For \(0<h\le1+1/n\), every maximizing simplex has the north pole \((0,1)\) as one vertex and a regular \((n-1)\)-simplex of circumradius \(\sqrt{h(2-h)}\), centered on the vertical axis, as its other \(n\) vertices in the base hyperplane \(z=1-h\). These are the only maximizers, up to orthogonal transformations fixing the axis. For \(1+1/n<h\le2\), the maximizers are exactly the regular \(n\)-simplices inscribed in the unit sphere and contained in the cap. Thus the exact saturation height is \(1+1/n\).

## Assumptions and scope
A simplex may have arbitrary orientation and arbitrary vertex positions within the entire solid cap, not just its spherical boundary. Euclidean volumes are ordinary (not factorial-normalized) volumes. The unit sphere has radius one, and the cap is the part above the plane \(z=1-h\). At positive heights the cap is full-dimensional. Degenerate simplices have zero volume and cannot maximize.

## Proof
**1. The full-ball bound, including equality.** Let \(v_0,\ldots,v_n\) lie in the unit \(n\)-ball and define their centroid \(\bar v=(n+1)^{-1}\sum_{i=0}^n v_i\). Put \(Y=[v_0-\bar v\ \cdots\ v_n-\bar v]\). The difference-matrix determinant identity gives
\[
(n!\,\operatorname{vol}_n\operatorname{conv}\{v_0,\ldots,v_n\})^2=(n+1)\det(YY^{\mathsf T}).
\]
Moreover,
\[
\operatorname{tr}(YY^{\mathsf T})=\sum_{i=0}^n\|v_i\|^2-(n+1)\|\bar v\|^2\le n+1.
\]
The arithmetic–geometric mean inequality on the \(n\) eigenvalues yields
\[
\operatorname{vol}_n\operatorname{conv}\{v_i\}\le V_n:=\frac{(n+1)^{(n+1)/2}}{n!\,n^{n/2}}.
\]
Equality forces every \(\|v_i\|=1\), \(\bar v=0\), and \(YY^{\mathsf T}=((n+1)/n)I_n\). Since the nullspace of \(Y\) is spanned by the all-ones vector, its column Gram matrix is \(((n+1)/n)(I_{n+1}-\mathbf1\mathbf1^{\mathsf T}/(n+1))\). Thus \(v_i\cdot v_j=-1/n\) for \(i\ne j\): equality holds precisely for regular \(n\)-simplices inscribed in the sphere.

**2. A sharp encompassing ellipsoid in the thin-cap regime.** Suppose \(0<h\le1+1/n\) and set \(t=h-1\), so \(-1<t\le1/n\). Define
\[
a^2=\frac{n^2(1-t^2)}{n^2-1},\qquad
b=\frac{n(1+t)}{n+1},\qquad
c=\frac{1-nt}{n+1}
\]
and
\[
E_{n,t}=\left\{(x,z):\ \frac{\|x\|^2}{a^2}+\frac{(z-c)^2}{b^2}\le1\right\}.
\]
For every \(z\in[-t,1]\), the difference between the squares of the permitted transverse radii in this ellipsoid and the unit ball is exactly
\[
a^2\left(1-\frac{(z-c)^2}{b^2}\right)-(1-z^2)
=\frac{2(1-nt)}{(n-1)(1+t)}(1-z)(z+t)\ge0.
\]
Consequently \(C_{n,h}\subseteq E_{n,t}\). For \(t<1/n\), the inequality is strict at all intermediate heights \(-t<z<1\).

The invertible affine transformation \(F(x,z)=(x/a,(z-c)/b)\) sends \(E_{n,t}\) onto the unit ball, the cap apex onto its north pole, and the cap's base rim onto the sphere latitude \(z'=-1/n\) with transverse radius \(\sqrt{n^2-1}/n\). Choose \(n\) base-rim vertices whose transverse components form a centered regular \((n-1)\)-simplex. Their images under \(F\), together with the north pole, have mutual scalar products \(-1/n\) and unit lengths; hence they form a regular \(n\)-simplex. The full-ball bound applied after \(F\) therefore yields a *sharp* cap bound
\[
M_n(h)=a^{n-1}b\,V_n
=\frac{h}{n}\frac{n^{n/2}}{(n-1)!(n-1)^{(n-1)/2}}(1-t^2)^{(n-1)/2},
\]
which is the first displayed branch, because \(1-t^2=h(2-h)\).

**3. Equality for smaller caps.** If \(t<1/n\), every vertex of a maximizing simplex must lie in \(C_{n,h}\cap\partial E_{n,t}\), because its affine image maximizes simplex volume in the ball. By the strict transverse-radius comparison above, these points are precisely the apex and the base rim. Since \(n+1\) base-rim vertices span at most \(n-1\) dimensions, exactly one vertex is the apex. The transformed regular-simplex equality condition forces the other \(n\) vertices to form the stated centered regular base simplex.

At \(t=1/n\), the ellipsoid equals the unit ball. For a regular maximizing \(n\)-simplex in the cap, let its vertical coordinates be \(z_0,\ldots,z_n\). The regular-simplex frame identities give
\[
\sum_{i=0}^n z_i=0,\qquad \sum_{i=0}^n z_i^2=\frac{n+1}{n},\qquad z_i\ge-\frac1n.
\]
With \(w_i=z_i+1/n\ge0\), one obtains \(\sum_i w_i=(n+1)/n\) and \(\sum_iw_i^2=((n+1)/n)^2\). Hence all cross-products \(w_iw_j\) vanish and exactly one \(w_i\) is nonzero. Thus one vertex has height \(1\), the other \(n\) have height \(-1/n\), and they form the same centered regular base simplex. This settles the transition equality case.

**4. Saturation.** For \(h\ge1+1/n\), the universal full-ball bound gives \(M_n(h)\le V_n\). The regular simplex constructed in step 2 at \(h=1+1/n\) still fits every larger cap, so equality is attained. The equality criterion from step 1 shows that the complete family of maximizers is exactly the set of inscribed regular \(n\)-simplices meeting the cap constraint.

## Verification
The accompanying standalone `verify.py` tests the exact rational ellipsoid containment factorization, the apex/base affine images, the resulting regular-simplex Gram identities, the equality of the sharp ellipsoid bound with the constructive volume, and continuity at the threshold for dimensions \(2\) through \(16\). It also compares randomly generated contained simplices against the predicted maximum in dimensions \(2\) through \(5\). These finite checks corroborate, but do not replace, the all-dimensional proof above.

## Relationship to prior work
Roy Han posed precisely the maximum-volume simplex problem in a Euclidean spherical cap in February 2015. Moritz Firsching's February 2016 answer calculated the volume of the apex-plus-regular-base construction and explicitly identified it as a lower bound, leaving optimality and the contact characterization unresolved. That construction and its lower bound are prior work, not claimed as new here. The result proved above establishes sharpness for the entire nontrivial cap range, classifies equality, and identifies the exact saturation threshold.

Horváth and Lángi's 2014 study gives the regular-simplex equality result for the *entire* unit ball (its Corollary 1), but does not consider the additional cap hyperplane constraint. The present sharp ellipsoid containment identity and its regular-simplex contact configuration connect that classical ball result to the cap optimization. Older results under the terminology of optimal determinant configurations or minimum-volume enclosing ellipsoids may exist and would require historical priority review.

## Limitations
This theorem addresses Euclidean spherical caps of a single unit ball, not arbitrary truncations of ellipsoids or unequal-ball intersections. The result is mathematically exact, but originality beyond the inspected sources is not independently established. The code checks finitely many cases and is not an exhaustive computational proof of the stated universal theorem. Independent audit has not been performed.

## References
1. Roy Han, “Maximal volume of a simplex inscribed in a spherical cap,” MathOverflow question 198405, posted 2015-02-25, with a lower-bound answer by Moritz Firsching, posted 2016-02-19. https://mathoverflow.net/questions/198405/maximal-volume-of-a-simplex-inscribed-in-a-spherical-cap
2. Ákos G. Horváth and Zsolt Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496, first submitted 2014-02-26, in particular Corollary 1. https://arxiv.org/abs/1402.6496
