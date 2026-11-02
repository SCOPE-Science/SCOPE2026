# The two bad fibers of the degree-nine maximizing sextic-plus-triangle

## Finding

Consider the relative degree-nine plane divisor \(\mathscr D\subset\mathbb P^2_{\mathbb Z}\) defined by
\[
F=XYZ\big((X^2+Y^2+Z^2)^3-27X^2Y^2Z^2\big).
\]
This is the integral equation underlying the degree-nine maximizing curve of Dimca--Ilardi--Pokora--Sticlaru, Example 6.4. Put \(Q=X^2+Y^2+Z^2\). The relative divisor is flat, and its geometric singularity and multiplicity pattern changes **precisely** in characteristics \(2\) and \(3\).

For every algebraically closed field of characteristic different from \(2,3\), the fiber is reduced, its degree-six component is irreducible and rational, and its entire singularity basket comprises six \(E_7\) points and seven nodes \(A_1\). The local Tjurina sum is \(49\). These characteristic-zero singularity counts are already published; the asserted arithmetic extension is their uniform validity over all primes greater than \(3\), together with the following two scheme-theoretic special fibers.

In characteristic \(2\), write \(S=X+Y+Z\) and \(G=S^3+XYZ\). Then
\[
F=XYZ\,G^2.
\]
The cubic \(G=0\) is an irreducible rational nodal cubic, with its **only** node at \(P=[1:1:1]\). Its normalization is
\[
\nu:\mathbb P^1\longrightarrow V(G),\qquad[s:t]\longmapsto[s^3:t^3:(s+t)^3].
\]
The coordinate lines each have contact order \(3\) with \(G\) at, respectively, \([0:1:1]\), \([1:0:1]\), and \([1:1:0]\). The reduced degree-six support has exactly seven singular points: the node of \(G\), those three order-three tangencies, and the three coordinate vertices. The projective Jacobian singular subscheme of the original nonreduced degree-nine fiber is, **scheme-theoretically**, the disjoint union of \(V(G^2)\) and the three reduced coordinate vertices.

In characteristic \(3\), the special fiber is
\[
F=XYZ\,Q^3.
\]
The conic \(Q=0\) is smooth, and the reduced support of degree \(5\) has exactly nine ordinary nodes: the three coordinate vertices and the six transverse coordinate-line--conic intersections. The projective Jacobian singular subscheme is the disjoint union of \(V(Q^3)\) and the three reduced coordinate vertices. The conic's four \(\mathbb F_3\)-rational points are exactly the reductions of the four generic off-axis nodes; its other six distinguished coordinate-axis intersection points are defined over \(\mathbb F_9\).

The thirteen distinguished characteristic-zero singular-point labels specialize as follows. At \(2\), four off-axis node labels meet at \(P\), the six \(E_7\) labels merge in three pairs at the cubic--line tangencies, and the three coordinate vertices remain distinct, giving label weights \((4,2,2,2,1,1,1)\). At \(3\), all thirteen labels remain distinct; the ten nonvertex labels lie on the now-triple conic.

## Assumptions and scope

All fibers and singular points are geometric unless a finite field is explicitly stated. A singular-point label means one of the four points \([1:\pm1:\pm1]\), the six coordinate-axis points with other two coordinates in the ratio \(1:\pm i\) where \(i^2=-1\), or the three coordinate vertices, considered as sections after base change to \(\mathbb Z[i]\). Label weights count **distinct generic labels**, not lengths of local singular schemes. The Jacobian subscheme is the projective subscheme cut out by \(F\) and its three partial derivatives; the equations below hold as saturated homogeneous ideals. Flatness concerns the indicated fixed integral equation, not an intrinsic moduli problem for maximizing curves or positive-characteristic freeness.

## Proof

**1. Flatness and the only possible changes.** The polynomial \(F\) is primitive of degree \(9\), with coefficient \(1\) on \(X^7YZ\). On every fiber it is a nonzero Cartier equation in the smooth relative surface \(\mathbb P^2_{\mathbb Z}\). The Cartier sequence is fiberwise exact, so \(\mathscr D\to\operatorname{Spec}\mathbb Z\) is flat. The elementary identities in steps 2--4 show that \(2\) and \(3\) are the only primes changing the geometric picture.

**2. Every characteristic different from two and three.** Put \(H=Q^3-27X^2Y^2Z^2\). The three derivatives obey
\[
H_X=6X(Q^2-9Y^2Z^2),\quad
H_Y=6Y(Q^2-9X^2Z^2),\quad
H_Z=6Z(Q^2-9X^2Y^2).
\]
At a singular point of \(H\) with all coordinates nonzero, these equations force \(X^2=Y^2=Z^2\); projectively there are four points \([1:\pm1:\pm1]\). In the chart \(Z=1\), the Hessian matrix at \((1,1)\) is
\[
\begin{pmatrix}72&-36\\-36&72\end{pmatrix},
\qquad\det=3888=2^4 3^5.
\]
The sign variants have the same nonzero determinant. They are therefore ordinary nodes in every characteristic other than \(2,3\).

At \(X=0\), the equation \(H=0\) becomes \((Y^2+Z^2)^3=0\). The two points \([0:1:\pm i]\) are the only singularities there, and similarly on the other two axes. At either point, \(X\) and \(W=Q\) are regular formal parameters because \(2Z\ne0\). Since \(Y,Z\) are units, the formal coordinate \(A=X\sqrt{27Y^2Z^2}\) is valid (characteristic not \(2\)) and \(H=W^3-A^2\). Thus \(H\) has a unibranch \(A_2\) cusp at each of the six axis points. Adding the corresponding coordinate-line factor gives the exact local two-branch germ, up to a unit,
\[
A(W^3-A^2)=0,
\]
which is of type \(E_7\) in all characteristics different from \(2,3\). There are no other singularities of \(H\). The three coordinate vertices are not on \(H\), so they give three further ordinary nodes of \(F\), and the above six \(E_7\) points plus four off-axis nodes exhaust its singular locus.

The sextic \(H\) is reduced because its singular locus is finite. It is irreducible: if it had a proper component of degree \(a\), \(1\le a\le5\), Bézout would force at least \(a(6-a)\ge5\) intersections with the complementary divisor (counting multiplicity). The six cusps are unibranch and cannot be component crossings, whereas each of the four ordinary nodes can contribute at most one to that intersection number. This is impossible. Its arithmetic genus is \(10\), and the six cusps plus four nodes contribute total delta invariant \(10\); its normalization therefore has genus zero. In the \(E_7\) local form, the Jacobian/Tjurina quotient has dimension \(7\) because \(2,3\) are invertible. Together with seven nodes this yields \(6\cdot7+7=49\).

**3. Characteristic two.** Since \(Q=S^2\) and \(-27=1\), the identity \(H=G^2\) is exact. The derivatives of \(G\) are \(S^2+YZ\), \(S^2+XZ\), and \(S^2+XY\). Their pairwise differences imply that any singular point with all coordinates nonzero has \(X=Y=Z\); if one coordinate is zero, the same equations contradict projectivity. Hence \(P\) is its only singular point. In the chart \(Z=1\), writing \(X=1+u\), \(Y=1+v\) gives
\[
G=u^2+uv+v^2+(u+v)^3,
\]
whose quadratic tangent cone splits into two distinct lines over \(\mathbb F_4\). Thus \(P\) is an ordinary node. Substitution of \([s^3:t^3:(s+t)^3]\) into \(G\) vanishes identically. These three cubic forms are linearly independent, so their image is not a line; degree considerations force the image to be the cubic \(V(G)\) and the map to have generic degree one. The map is therefore the normalization, and its two preimages of \(P\) have \(s/t\) equal to the two roots of \(r^2+r+1\). The pullbacks of \(X,Y,Z\) are \(s^3,t^3,(s+t)^3\), proving all three contact orders.

The full characteristic-two partial derivatives are
\[
(F_X,F_Y,F_Z)=G^2(YZ,XZ,XY).
\]
The ideal \(I_V=(XY,XZ,YZ)\) is the saturated ideal of the three coordinate vertices. None of them lies on \(G\), since \(G\) equals \(1\) at each vertex. Hence \((G^2)\cap I_V=G^2 I_V\), and both constituent ideals are saturated; this identifies the complete projective Jacobian subscheme. The ordinary-node and tangency descriptions of the reduced support follow from the preceding calculations. In particular its reduced singular-point count is \(1+3+3=7\).

**4. Characteristic three.** Since \(27=0\) and the Frobenius map raises a polynomial to its third power, \(H=Q^3\). The derivatives of \(Q\) are \(2X,2Y,2Z\), so \(Q\) is smooth. Each axis cuts it at two distinct nonvertex points because \(Y^2+Z^2\) is separable, and these are transverse intersections. Its reduced union with the coordinate triangle has exactly \(6+3=9\) ordinary nodes. The full partial derivatives are
\[
(F_X,F_Y,F_Z)=Q^3(YZ,XZ,XY).
\]
As \(Q\) avoids the coordinate vertices, the same saturated-intersection argument identifies the singular scheme as \(V(Q^3)\) disjoint from those three vertices. In \(\mathbb F_3\), a square is \(0\) or \(1\), so \(Q=0\) forces all three coordinates to be nonzero. This gives exactly four rational projective points \([1:\pm1:\pm1]\). The six marked axis points use \(i^2=-1\) and are defined over \(\mathbb F_9\), not \(\mathbb F_3\).

**5. Collisions of labels.** The four generic off-axis nodes have integral sign coordinates and reduce to one point modulo \(2\) and to four distinct points modulo \(3\). For the six axis points, \(i^2+1=(i+1)^2\) in characteristic \(2\), so each signed pair reduces to one of the three cubic-axis contacts. In characteristic \(3\), \(i\) and \(-i\) remain distinct, as do all four off-axis signs. The coordinate vertices remain separate in both characteristics. This gives exactly the stated label partitions.

## Verification

Run `python3 verify_maximizing9.py` in the same directory. This standard-library-only script reconstructs the integral polynomial, verifies the exact special-fiber and Jacobian identities in characteristics \(2\) and \(3\), verifies the characteristic-two normalization substitution and nodal tangent-cone expansion, enumerates the \(\mathbb F_2\) cubic and \(\mathbb F_3\) conic rational points, and verifies the generic Hessian determinant and the marked-sign collisions. Its finite checks at small odd primes illustrate the universal symbolic arguments above; the proof of the all-primes claim uses the displayed derivatives and the factorization \(3888=2^4 3^5\), not finite sampling.

## Relationship to prior work

Dimca, Ilardi, Pokora, and Sticlaru, *Construction of free curves by adding lines to a given curve* (arXiv:2301.01117, first submitted January 3, 2023), Example 6.4, introduce this equation over the complex numbers and prove the basket \(6E_7+7A_1\), maximality, and freeness with exponents \((3,5)\). The present assertion does not claim these generic properties as new. Rather, it classifies the **arithmetic fibers and projective Jacobian schemes** at every characteristic, identifies the nodal cubic normalization and the triple-conic reduction, and tracks the previously named singularities across those fibers. The established characteristic-two fact that all nodal plane cubics are projectively equivalent (for example, Berg's treatment of plane cubics in characteristic two) does not itself identify this particular integral degree-nine divisor or the relative singular schemes.

## Limitations

Only the specified primitive integral equation and its fibers are studied. Its nonreduced positive-characteristic fibers are not themselves reduced free divisors, and no claim of positive-characteristic freeness or intrinsic model-independent reduction is made. The Jacobian schemes here are positive-dimensional in characteristics \(2,3\); the collision weights of labeled points must not be mistaken for their local scheme lengths. Historic priority remains subject to unindexed literature and independent expert review; no independent mathematical audit or validation has been performed.

## References

1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117v4 (2023), Example 6.4, pp. 21--22. https://arxiv.org/abs/2301.01117
2. A. H. Berg, *Enumerative Geometry for Plane Cubic Curves in Characteristic 2*, Compositio Math. 111 (1998), 123--147, esp. Lemma 3.2 (nodal cubics). https://doi.org/10.1023/A:1000291224146
