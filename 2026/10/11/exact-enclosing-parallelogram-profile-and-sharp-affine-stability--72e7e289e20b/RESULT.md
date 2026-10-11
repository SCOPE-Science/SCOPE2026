# Exact enclosing-parallelogram profile and sharp affine stability for symmetric hexagons

## Finding

Let \(P\subset\mathbb R^2\) be a convex centrally symmetric hexagon with six genuine vertices. It has a three-segment Minkowski representation
\[
P=t+[-a,a]+[-b,b]+[-c,c],
\]
where \(a,b,c\) are nonzero and pairwise nonparallel vectors and \(t\) is the center of symmetry. The vectors may be taken to be half the three distinct edge vectors, up to signs and permutation.

Define three positive affine-covariant determinant magnitudes
\[
X=|\det(a,b)|,\qquad
Y=|\det(b,c)|,\qquad
Z=|\det(c,a)|,
\]
and write
\[
T=X+Y+Z,\qquad
M=\max\{X,Y,Z\},\qquad
m=\min\{X,Y,Z\}.
\]
Let \(q(P)\) denote the smallest area of **any** parallelogram containing \(P\), with no prescribed orientation. Then
\[
\boxed{\displaystyle
|P|=4T,\qquad
q(P)=4\left(T+\frac{XYZ}{M^2}\right),\qquad
\frac{q(P)}{|P|}=1+\frac{XYZ}{M^2T}.
}
\]

In particular, some globally minimizing enclosing parallelogram has each side pair parallel to a side pair of the hexagon. Among the three such tight parallelograms, choose the two hexagon edge directions whose determinant magnitude is largest; this always gives a global minimizer.

The profile sharpens the classical symmetric-body bound to an exact shape-dependent identity:
\[
\boxed{\displaystyle
1<\frac{q(P)}{|P|}\le\frac43,
}
\]
with equality on the right **exactly for affine-regular hexagons**. The lower endpoint is approached as one of the three generators degenerates, and is not attained by a genuine six-sided hexagon.

There is also a sharp affine-invariant stability law. With \(r=m/M\),
\[
\boxed{\displaystyle
\frac43-\frac{q(P)}{|P|}
\ge \frac{2(1-r)}{3(2+r)}.
}
\]
Equality is attainable for every \(r\in(0,1]\). Thus for \(0\le\varepsilon<1/3\),
\[
\frac{q(P)}{|P|}\ge\frac43-\varepsilon
\quad\Longrightarrow\quad
\boxed{\displaystyle
\frac{m}{M}\ge\frac{2-6\varepsilon}{2+3\varepsilon}.}
\]

The invariant and its stability law are unchanged by invertible affine coordinate changes.

## Assumptions and scope

A *centrally symmetric hexagon* here means a compact convex polygon with nonempty interior, exactly six vertices, and a center of symmetry. Thus the three independent pairs of opposite sides have distinct directions; degenerate four-sided cases are excluded.

A *circumscribed parallelogram* is any parallelogram that contains \(P\), including its boundary. The definition of \(q(P)\) imposes no edge-direction restriction. The theorem establishes that an optimal one can nevertheless be found among three explicit side-aligned candidates.

All determinant magnitudes are computed with the standard Euclidean area form. Under an invertible linear map, each is multiplied by the same factor \(|\det A|\); hence the dimensionless ratios and \(r\) are intrinsic to the affine shape.

The sharp inverse stability concerns determinant balance. It is not a quantitative estimate in Hausdorff or Banach--Mazur distance from an affine-regular hexagon.

## Proof

**1. Reduction of an unrestricted minimum to side-aligned candidates.** Translate the center of symmetry to the origin, and let
\[
h_P(u)=\max_{x\in P}u\cdot x.
\]
For linearly independent covectors \(u,v\), the unique *tight* centered parallelogram with these outer-normal directions is
\[
Q(u,v)=\{x:\ |u\cdot x|\le h_P(u),\quad|v\cdot x|\le h_P(v)\}.
\]
Every other parallelogram containing a centrally symmetric \(P\) with these same side directions has area at least that of \(Q(u,v)\). The linear coordinate map \(x\mapsto(u\cdot x,v\cdot x)\) gives
\[
|Q(u,v)|=\frac{4h_P(u)h_P(v)}{|\det(u,v)|}.
\]

For fixed \(v\ne0\), minimize \(h_P(u)/|\det(u,v)|\) over \(u\) nonparallel to \(v\). The support function of a polygon is linear on every cone of its outer normal fan. Within any such cone intersected with either open half-plane \(\det(u,v)>0\) or \(\det(u,v)<0\), the quotient is a ratio of two linear functions of \(u\), with the denominator of fixed sign. On a two-ray subcone, the value at a positive linear combination is a weighted average of the endpoint quotients, with nonnegative weights supplied by the denominator. It therefore cannot be smaller than both endpoint values. A boundary ray with \(\det(u,v)=0\) has divergent quotient, because \(P\) has interior. Consequently, for every fixed \(v\), a minimum is achieved when \(u\) is an outer normal to an edge of \(P\).

Since the area objective diverges as the normal directions become parallel, its global minimum exists. Start with one optimal pair, replace its first normal by an edge normal without increasing area, and then replace its second normal by an edge normal while holding the first fixed. The area cannot fall below the global minimum and hence remains optimal. It follows that at least one minimum-area containing parallelogram has both side directions parallel to sides of \(P\). Central symmetry gives exactly three unoriented edge directions, so just three pairs need to be considered.

**2. Exact areas of the three candidates.** Every centrally symmetric hexagon has the stated three-segment representation. The standard planar zonotope area identity gives
\[
|P|=4\bigl(|\det(a,b)|+|\det(b,c)|+|\det(c,a)|\bigr)=4T.
\]
For the candidate whose side directions are parallel to \(a,b\), write \(c=\alpha a+\beta b\). The determinant identities give
\[
|\alpha|=\frac{Y}{X},\qquad |\beta|=\frac{Z}{X}.
\]
In the coordinate basis \((a,b)\), the three-segment sum fits tightly in
\[
[-(1+|\alpha|),1+|\alpha|]\times[-(1+|\beta|),1+|\beta|].
\]
The enclosing parallelogram therefore has area
\[
\begin{aligned}
|Q_{ab}|&=4X(1+|\alpha|)(1+|\beta|)\\
&=4\frac{(X+Y)(X+Z)}X\\
&=4\left(T+\frac{YZ}{X}\right)\\
&=4\left(T+\frac{XYZ}{X^2}\right).
\end{aligned}
\]
Cyclic permutation gives two other candidates with additional terms \(XYZ/Y^2\) and \(XYZ/Z^2\). Their least value occurs for the largest denominator among \(X,Y,Z\), namely \(M\). The side-normal reduction proves this is the **unrestricted** minimum:
\[
q(P)=4\left(T+\frac{XYZ}{M^2}\right).
\]

**3. Sharp upper bound and equality.** Choose the pair associated with \(M\) and write the remaining normalized determinant moduli as \(x,y\in(0,1]\). Then
\[
\frac{q(P)}{|P|}=1+\frac{xy}{1+x+y}.
\]
Because \(x,y\le1\),
\[
\frac{xy}{1+x+y}\le\frac13,
\]
with equality only for \(x=y=1\). Thus equality in \(q(P)\le4|P|/3\) holds precisely when
\[
X=Y=Z.
\]
Now the coordinate coefficients of \(c=\alpha a+\beta b\) both have absolute value one. After changing signs of the segment generators if necessary, the three generators become \(a,b,a+b\); their zonotope is an affine image of the regular hexagon. Conversely, every affine-regular hexagon has these determinant magnitudes equal. This proves the equality classification.

**4. Sharp stability.** With the largest determinant normalized to one, let the smallest be \(r=m/M\) and the third be \(s\in[r,1]\). The product-to-sum ratio is increasing in \(s\):
\[
\frac{q(P)}{|P|}=1+\frac{rs}{1+r+s}
\le1+\frac{r}{2+r}.
\]
Therefore
\[
\frac43-\frac{q(P)}{|P|}
\ge\frac13-\frac{r}{2+r}
=\frac{2(1-r)}{3(2+r)}.
\]
For every \(0<r\le1\), take
\[
a=(1,0),\qquad b=(0,1),\qquad c=(-1,r).
\]
Then \((X,Y,Z)=(1,1,r)\), giving equality in the displayed bound. Finally, if the deficit is at most \(\varepsilon<1/3\), solving
\[
\frac{2(1-r)}{3(2+r)}\le\varepsilon
\]
yields
\[
r\ge\frac{2-6\varepsilon}{2+3\varepsilon}.
\]
This proves the complete claim.

## Verification

The bundled standalone script `verify.py` uses exact rational arithmetic to check the symbolic candidate-area identities, the formula for the sharp family, the deficit factorization and the inverse stability rearrangement. It also exactly enumerates the vertices of selected rational three-generator zonotopes and checks their convex-hull area against the determinant formula.

The global reduction to edge normals is an analytic proof about ratios of positive linear forms on normal-fan cones; finite sampling is not used to prove it. The area and rigidity conclusions follow from exact algebra after this reduction.

## Relationship to prior work

Fodor and Grundbacher study minimum-area containing quadrilaterals and summarize Petty's classical theorem: every centrally symmetric planar convex body has an enclosing parallelogram of area at most four-thirds of its area, with equality precisely for affine-regular hexagons. Their full primary preprint does not state an exact shape-by-shape determinant formula for centrally symmetric hexagons or a sharp stability law in the ratios of the three side-pair determinants.

Pełczyński and Szarek independently reprove the symmetric-body constant and equality case. Their inspected Section 4, including Lemma 4.1 and Corollary 4.1, handles the extremal constant and affinely regular equality but does not give the exact three-determinant profile or inverse determinant-balance inequality above.

Domokos, Lángi, and Mezei study affine shape dynamics, including centrally symmetric hexagons and extremal circumscribed rectangles. Their inspected hexagon discussion concerns invariant affine shapes rather than the unrestricted minimum-area enclosing parallelogram or the formula above.

The added structure here is the *complete unrestricted* area profile on every six-sided centrally symmetric polygon, the reduction to only three side-direction candidate pairs, and the sharp interpolation of the Petty deficit by a natural affine-invariant determinant condition number. The known four-thirds inequality and affine-regular equality case are explicitly treated as prior facts, not as original claims.

## Limitations

The exact formula applies to genuine centrally symmetric hexagons, not to arbitrary centrally symmetric convex bodies or polygons with more than six vertices. It does not solve the unrestricted quadrilateral problem for nonsymmetric convex bodies.

The quantitative stability controls the ratio of the smallest and largest generator-pair determinant magnitudes; no metric estimate for the distance to an affine-regular hexagon is asserted.

The original 1955 article of Petty could not be inspected directly in a lawful open full text. The later full-text reproof by Pełczyński--Szarek and the 2025 primary preprint were inspected instead. An earlier unindexed determinant-formula treatment of hexagonal enclosing parallelograms remains a residual originality risk.

## References

1. Ferenc Fodor and Florian Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185v1, first posted 5 June 2025; primary MSC2020 52A27.
2. C. M. Petty, *On the geometry of the Minkowski plane*, Rivista di Matematica della Università di Parma 6 (1955), 269--292.
3. A. Pełczyński and S. J. Szarek, *On parallelepipeds of minimal volume containing a convex symmetric body in \(\mathbb R^n\)*, Mathematical Proceedings of the Cambridge Philosophical Society 109 (1991), 125--148; DOI:10.1017/S0305004100069619.
4. Gábor Domokos, Zsolt Lángi, and Márk Mezei, *A shape evolution model under affine transformations*, arXiv:1604.07630v2.
