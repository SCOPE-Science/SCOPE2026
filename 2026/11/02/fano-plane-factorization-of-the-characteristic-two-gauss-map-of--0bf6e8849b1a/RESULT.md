# Fano-plane factorization of the characteristic-two Gauss map of Cayley's nodal cubic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(S\subset\mathbb P^3_k\) be the Cayley cubic
\[
S:\quad X_0X_1X_2+X_0X_1X_3+X_0X_2X_3+X_1X_2X_3=0.
\]
Its smooth point \(P=[1:1:1:1]\) is contained in **every** tangent plane at a smooth point of \(S\). Its reduced projective dual is the plane of hyperplanes containing \(P\), and its Gauss map is purely inseparable of degree \(4\). More precisely, the Gauss map factors into two dominant purely inseparable rational maps of degree \(2\), and the intermediate plane map is the complete anticanonical net of the blowup of \(\mathbb P^2_k\) in all seven points of \(\mathbb P^2(\mathbb F_2)\).

In coordinates \(u=X_0+X_3\), \(v=X_1+X_3\), \(w=X_2+X_3\), \(t=X_3\), the factorization is
\[
 S\dashrightarrow\mathbb P^2_{[u:v:w]}
 \dashrightarrow\mathbb P^2_{[A:B:C]},
\quad
[A:B:C]=[vw(v+w):uw(u+w):uv(u+v)].
\]
Both arrows have purely inseparable generic degree \(2\). The second map has seven distinct reduced base points: exactly \(\mathbb P^2(\mathbb F_2)\); after their blowup it is the morphism given by the complete linear system \(|3H-\sum_{i=1}^{7}E_i|=|-K|\).

Additionally, the classical integral quartic equation of the Steiner dual specializes in characteristic \(2\) to the **fourth power** of the linear equation defining this dual plane. This quadruple-plane flat specialization must not be confused with the reduced, scheme-theoretic image of the special-fiber Gauss map.

## Assumptions and scope
All statements about inseparability, the singularity type, and base points are over \(k=\overline{\mathbb F}_2\), though the maps and centers are defined over \(\mathbb F_2\). The source of the Gauss map is the smooth locus of the reduced cubic \(S\). The degree of a dominant generically finite rational map means the degree of its induced function-field extension, including the inseparable part. The classical quartic specializes as a fixed equation over \(\mathbb Z\); no assertion is made that reduced duality commutes with specialization.

## Proof
**1. Cubic and projection.** Substituting \(X_0=t+u\), \(X_1=t+v\), \(X_2=t+w\), \(X_3=t\), gives, in characteristic \(2\),
\[
F=t^2(u+v+w)+uvw.
\]
Thus \(P=[u:v:w:t]=[0:0:0:1]\) is a smooth point: the first three partial derivatives are \(t^2+vw\), \(t^2+uw\), \(t^2+uv\), and the fourth is identically zero. Projection from \(P\) is dominant, and in the affine chart \(u\ne0\) its function field is obtained from \(k(v/u,w/u)\) by adjoining \(t/u\) with
\[
(t/u)^2=\frac{(v/u)(w/u)}{1+v/u+w/u}.
\]
The right-hand function is not a square: its valuation along \(v/u=0\) is \(1\). Therefore projection has purely inseparable degree \(2\).

The only singular points of the cubic are its four coordinate vertices. Indeed, points with all four coordinates nonzero satisfy \(\sum_i1/X_i=0\), in which case every partial derivative is nonzero; points with exactly two nonzero coordinates are smooth, and exactly three nonzero coordinates do not lie on \(S\). At a coordinate vertex the quadratic tangent cone is \(yz+yw+zw\); it is a smooth conic in characteristic \(2\). Thus the four singularities are ordinary double points, and no hidden singular component affects the Gauss calculation.

**2. Gauss map and Fano-plane cubics.** Differentiating \(F\) in the new coordinates gives
\[
\gamma=[t^2+vw:t^2+uw:t^2+uv:0].
\]
Write \(L=u+v+w\). The equality \(t^2L=uvw\) on \(S\) shows, wherever \(L\ne0\), that
\[
L(t^2+vw)=vw(v+w),\qquad
L(t^2+uw)=uw(u+w),\qquad
L(t^2+uv)=uv(u+v).
\]
Thus the Gauss map factors through the displayed plane cubic map \(\Phi\), and every Gauss hyperplane contains \(P\).

The base ideal of \(\Phi\) consists of the three cubics \(vw(v+w)\), \(uw(u+w)\), \(uv(u+v)\). Over any extension of \(\mathbb F_2\), their common zero set is exactly the seven points \(\mathbb P^2(\mathbb F_2)\): if all coordinates are nonzero the three equations force \(u=v=w\), while if, say, \(u=0\), they require \(v=0\), \(w=0\), or \(v=w\). At each of the seven points the three linear terms span the two-dimensional cotangent space, so the base locus is reduced and a single blowup removes all base points, including infinitely near ones. The evaluation conditions imposed by these seven points on ternary cubics are independent: the coefficients of the three pure cubes vanish, those of each pair of reversed mixed monomials must agree, and the coefficient of \(uvw\) vanishes. Consequently the above three cubics form a basis for the full three-dimensional space of cubics through the seven points.

Let \(B\to\mathbb P^2\) be their blowup, \(H\) a line class, and \(E_1,\ldots,E_7\) the exceptional curves. The resulting morphism \(\widetilde\Phi:B\to\mathbb P^2\) has pullback of a target line \(D=3H-\sum E_i=-K_B\), with \(D^2=9-7=2\). Because the system is base-point-free, \(D^2>0\) forces a two-dimensional image, hence all of \(\mathbb P^2\), and the projection formula gives generic degree \(2\).

This generic degree-two map is not separable: on the affine chart \(u=1\), writing \(v=a,w=b\), its three coordinates are \(ab(a+b)\), \(b(1+b)\), and \(a(1+a)\). The determinant of the Jacobian of the two independent ratios is zero in characteristic \(2\) (the standalone verifier checks its cleared numerator identically). A degree-two inseparable extension in characteristic \(2\) is purely inseparable. Thus the second factor has pure inseparable degree \(2\); composing with projection gives pure inseparable degree \(4\). The image is the entire target plane, and the unique common point of all its represented hyperplanes is \(P\).

**3. Relation to the classical dual quartic.** For dual coordinates \(U_0,\ldots,U_3\), the classical Steiner quartic is given integrally by
\[
G=\left(\sum_{i=0}^{3}U_i^2-2\sum_{0\le i<j\le3}U_iU_j\right)^2
 -64U_0U_1U_2U_3.
\]
This polynomial vanishes identically under \(U_i=s_i^2\) with \(\sum_i s_i=0\), and in characteristic different from \(2\) it is the classical equation of the projective dual of the Cayley cubic. Reducing its coefficients modulo \(2\) yields
\[
G\equiv(U_0+U_1+U_2+U_3)^4\pmod2.
\]
Since \(G\) is primitive over \(\mathbb Z\), its hypersurface is flat over \(\mathbb Z\), so the special divisor is a quadruple plane. In contrast, the special-fiber Gauss image, which has an integral function field as its scheme-theoretic image, is the reduced plane \(U_0+U_1+U_2+U_3=0\).

## Verification
The included standalone `verify.py` checks exact coefficient identities in \(\mathbb F_2[u,v,w,t]\), all seven finite base points and their simple local ranks, the rank-seven conditions on ternary cubics, vanishing of the planar-map Jacobian wedge, and the integral quartic identity and characteristic-two reduction. Execute `python verify.py` with Python 3 and SymPy. This is not merely sampling in characteristic two: the finite seven-point calculation is paired with an all-algebraic-closure common-zero argument above.

## Relationship to prior work
Dardanelli and van Geemen (2004, arXiv:math/0409322, §3.1) identify Cayley's four-nodal cubic within classical cubic-surface and Hessian geometry. Dolgachev's *Classical Algebraic Geometry* (2012, §9.2) supplies the classical Steiner quartic equation and squared-coordinate Gauss parameterization. Kadyrsizova et al. (2020, arXiv:2007.12018) classify characteristic-two cubic surfaces by Frobenius splitting and line configurations; Catanese (2021, arXiv:2106.09988) studies Gauss maps and inseparability in characteristic-two quartic-surface geometry. The new statement here is not merely the classical equation or its reduction: it is the explicit factorization of the **characteristic-two** Cayley Gauss map into two degree-two purely inseparable maps, with the intermediate morphism precisely the anticanonical net through all seven Fano-plane points, together with the distinction between the reduced dual and the quadruple-plane flat limit.

## Limitations
The statement concerns only the specified cubic model and characteristic \(2\); it is not a classification of arbitrary strange cubic surfaces. The nonsmooth points are excluded from the domain of the Gauss map. The blowup morphism of the intermediate plane is generically finite, not asserted finite everywhere. A prior explicit computation of this particular Fano-plane factorization may exist under different terminology. The classical dual quartic equation is established literature and is not claimed as an original identity. Independent mathematical review has not been performed.

## References
1. E. Dardanelli and B. van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322, first posted 2004-09-18, especially §3.1. https://arxiv.org/abs/math/0409322
2. I. Dolgachev, *Classical Algebraic Geometry: A Modern View*, Cambridge University Press, 2012, §9.2 (the classical Cayley–Steiner duality). https://doi.org/10.1017/CBO9781139084437
3. Z. Kadyrsizova, J. Kenkel, J. Page, J. Singh, K. Smith, A. Vraciu, and E. Witt, *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018, first posted 2020-07-23. https://arxiv.org/abs/2007.12018
4. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, first posted 2021-06-18. https://arxiv.org/abs/2106.09988
