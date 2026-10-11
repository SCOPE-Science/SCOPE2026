# Euclidean rigidity and exact area stability of equal-area equiangular polygons
## Finding
Let \(P\) be a strictly convex equiangular \(n\)-gon with \(n\ge5\). Assume that all triangles formed by three consecutive vertices have the same nonzero area.

Write the side lengths cyclically as
\[
\ell_0,\ell_1,\ldots,\ell_{n-1}.
\]
Then
\[
\boxed{\ell_{i+2}=\ell_i\quad\text{for every }i.}
\tag{1}
\]

Therefore:

- if \(n\) is odd, all side lengths are equal and \(P\) is regular;
- if \(n=2m\) is even, the side lengths alternate
\[
a,b,a,b,\ldots,a,b
\tag{2}
\]
for some \(a,b>0\).

Conversely, every positive pair \(a,b\) determines, up to Euclidean congruence, a unique strictly convex equiangular equal-area \(2m\)-gon with the alternating side pattern (2).

For even \(n\), its area has the exact closed form
\[
\boxed{
A(P)=
\frac{n}{16}
\left[
\cot\!\left(\frac{\pi}{n}\right)(a+b)^2
-
\tan\!\left(\frac{\pi}{n}\right)(a-b)^2
\right].
}
\tag{3}
\]
If the perimeter is fixed, the regular polygon with the same perimeter has side length
\[
\frac{a+b}{2},
\]
and
\[
\boxed{
A_{\mathrm{reg}}-A(P)
=
\frac{n}{16}\tan\!\left(\frac{\pi}{n}\right)(a-b)^2.
}
\tag{4}
\]
Thus the regular polygon is the unique area maximizer in this Euclidean subclass, and (4) is an exact quadratic stability identity rather than only an inequality.

Finally, when \(n=2m\),
\[
n\equiv0\pmod4
\]
implies that every polygon in the alternating family is centrally symmetric, whereas for
\[
n\equiv2\pmod4
\]
central symmetry occurs only when
\[
a=b.
\]

## Assumptions and scope
A convex equal-area polygon is one whose vertex triangles, formed by every three consecutive vertices, all have the same nonzero area. This is the class studied by Harel--Rabin and by Craizer--Teixeira--da Silva.

The additional assumption here is Euclidean equiangularity: every interior angle is
\[
\pi-\frac{2\pi}{n}.
\]
Equivalently, if the polygon is oriented counterclockwise, its successive edge directions differ by the fixed exterior angle
\[
\delta=\frac{2\pi}{n}.
\]

The theorem classifies exactly the intersection of the equal-area and equiangular classes. No claim is made for arbitrary equal-area polygons, whose affine moduli have much larger dimension.

## Proof
Let
\[
e_i=P_{i+1}-P_i
\]
be the oriented edge vectors. Since \(P\) is equiangular and strictly convex, after one rigid rotation we may write
\[
e_i=\ell_i u_i,
\qquad
u_i=
\left(
\cos(i\delta),
\sin(i\delta)
\right),
\qquad
\delta=\frac{2\pi}{n}.
\tag{5}
\]

The vertex triangle at \(P_{i+1}\) has area
\[
\frac12[e_i,e_{i+1}]
=
\frac12\ell_i\ell_{i+1}\sin\delta.
\tag{6}
\]
Because \(\sin\delta>0\) and all these areas are equal,
\[
\ell_i\ell_{i+1}
=
\ell_{i+1}\ell_{i+2}.
\]
All side lengths are positive, so
\[
\ell_{i+2}=\ell_i,
\]
proving (1).

If \(n\) is odd, addition by \(2\) generates all residue classes modulo \(n\). Hence all side lengths are equal. Equal lengths together with equal exterior angles give a regular polygon.

Now let \(n=2m\). Equation (1) gives the alternating pattern (2). Conversely, prescribe any \(a,b>0\) and let the edge vectors be
\[
e_i=
\begin{cases}
a\,u_i,&i\text{ even},\\
b\,u_i,&i\text{ odd}.
\end{cases}
\tag{7}
\]
The even directions form a regular \(m\)-point set on the unit circle, so
\[
\sum_{j=0}^{m-1}u_{2j}=0.
\]
The odd directions are a rotation of the same set, hence
\[
\sum_{j=0}^{m-1}u_{2j+1}=0.
\]
Therefore
\[
\sum_{i=0}^{n-1}e_i=0,
\]
so the edge chain closes. Its edge directions turn strictly monotonically by \(\delta\), with positive lengths, and hence it is a strictly convex polygon. Formula (6) shows that all vertex triangle areas equal
\[
\frac12ab\sin\delta.
\]
This proves existence and uniqueness up to congruence.

We next compute the area. Identify the plane with \(\mathbb C\), put
\[
z=e^{2\pi \mathrm{i}/n},
\qquad
c=\frac{a+b}{2},
\qquad
d=\frac{a-b}{2}.
\]
Then
\[
e_i=c z^i+d(-z)^i.
\tag{8}
\]
A convenient choice of vertices, differing from any other only by a translation, is
\[
p_i=
\alpha z^i+\beta(-z)^i,
\qquad
\alpha=\frac{c}{z-1},
\qquad
\beta=\frac{d}{-z-1},
\tag{9}
\]
because
\[
p_{i+1}-p_i=e_i.
\]

The signed polygon area is
\[
A(P)
=
\frac12
\sum_{i=0}^{n-1}
\operatorname{Im}\!\left(\overline{p_i}e_i\right).
\tag{10}
\]
Since \(n\) is even,
\[
\sum_{i=0}^{n-1}(-1)^i=0,
\]
so all mixed Fourier terms in (10) vanish. Thus
\[
A(P)
=
\frac n2
\left[
c\,\operatorname{Im}(\overline{\alpha})
+
d\,\operatorname{Im}(\overline{\beta})
\right].
\tag{11}
\]
The elementary identities
\[
\operatorname{Im}\frac1{e^{-2\pi \mathrm{i}/n}-1}
=
\frac12\cot\frac{\pi}{n},
\]
and
\[
\operatorname{Im}\frac{-1}{1+e^{-2\pi \mathrm{i}/n}}
=
-\frac12\tan\frac{\pi}{n}
\]
give
\[
A(P)
=
\frac n4
\left[
c^2\cot\frac{\pi}{n}
-
d^2\tan\frac{\pi}{n}
\right].
\]
Substituting
\[
c=\frac{a+b}{2},
\qquad
d=\frac{a-b}{2}
\]
proves (3).

The perimeter equals
\[
m(a+b).
\]
The regular polygon with this perimeter has side length \((a+b)/2\), so subtracting its area from (3) gives exactly (4).

For central symmetry, write \(n=2m\). Opposite edge directions satisfy
\[
u_{i+m}=-u_i.
\]
If \(m\) is even, then \(i\) and \(i+m\) have the same parity, so
\[
e_{i+m}=-e_i
\]
for every \(i\). Hence
\[
P_{i+m}+P_i
\]
is independent of \(i\), proving central symmetry.

If \(m\) is odd, opposite indices have opposite parity. Central symmetry would require
\[
e_{i+m}=-e_i,
\]
which forces
\[
a=b.
\]
Conversely \(a=b\) gives the regular polygon. This proves the parity statement.

## Verification
The bundled `verify.py` performs three independent checks.

First, for every
\[
5\le n\le60,
\]
it constructs random polygons from the classified families and verifies numerically that all consecutive vertex-triangle areas agree.

Second, for every even
\[
6\le n\le60
\]
and several rational choices of \(a,b\), it computes the polygon area directly by the shoelace formula and compares it with (3).

Third, it checks the central-symmetry parity statement by testing the exact opposite-edge condition.

These finite checks are diagnostic only. The classification and area formula are proved symbolically above.

## Relationship to prior work
Harel and Rabin introduced and parametrized equal-area polygons. They explicitly ask for converses to the fact that regular polygons are equal-area, classify their own more restrictive notion of symmetric equal-area polygons, and show that those are generalized affine-regular polygons. Their full text contains no equiangular specialization.

Craizer, Teixeira and da Silva develop the affine differential geometry of convex equal-area polygons, including affine curvature, evolutes, and an affine isoperimetric inequality. Their open preprint likewise contains no equiangular specialization. The theorem here instead intersects their affine class with a Euclidean angle constraint and obtains a complete parity classification plus an exact Euclidean fixed-perimeter area deficit.

The prior affine isoperimetric inequality does not imply (4): its perimeter and curvature are affine quantities, while (4) uses ordinary Euclidean perimeter and the Euclidean angle constraint.

Targeted searches under equal-area polygon, equiangular polygon, alternating side lengths, semiregular polygon, vertex-triangle area, and the exact fixed-perimeter deficit did not locate an implication-equivalent published statement.

## Limitations
The theorem applies only to strictly convex equiangular polygons. General convex equal-area polygons have many more degrees of freedom.

The area identity is Euclidean and is not affine invariant.

The proof is elementary once both defining conditions are written in edge coordinates, so an unindexed olympiad-style or expository observation remains the main originality risk.

The result does not settle the connectedness questions for the full equal-area moduli spaces.

## References
1. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, *Affine Properties of Convex Equal-Area Polygons*, arXiv:1103.2722v1, 14 March 2011; later *Discrete & Computational Geometry* 48 (2012), 580--595. DOI: 10.1007/s00454-012-9448-y.
2. G. Harel and J. M. Rabin, *Polygons Whose Vertex Triangles Have Equal Area*, *American Mathematical Monthly* 110 (2003), 606--619. DOI: 10.1080/00029890.2003.11920000.
