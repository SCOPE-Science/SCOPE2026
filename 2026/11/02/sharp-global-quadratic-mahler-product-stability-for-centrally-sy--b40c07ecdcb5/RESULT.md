# Sharp global quadratic Mahler-product stability for centrally symmetric hexagons

## Finding

Every nondegenerate centrally symmetric planar convex hexagon is affinely equivalent to a three-segment zonotope
\[
K(a,b,c)=\frac a2[-u_1,u_1]+\frac b2[-u_2,u_2]+\frac c2[-u_3,u_3],\qquad a,b,c>0,
\]
where \(u_1=(1,0)\), \(u_2=(1/2,\sqrt3/2)\), and \(u_3=(-1/2,\sqrt3/2)\). Within this gauge the positive length triple is unique up to a common factor and permutation.

Write \(S=a+b+c\), \(Q=ab+bc+ca\), \(D=(a+b)(b+c)(c+a)\), and define the affine-invariant squared generator discrepancy
\[
V(K)=\frac{(a-b)^2+(b-c)^2+(c-a)^2}{S^2}.
\]
With \(\mathcal M(K)=\operatorname{area}(K)\operatorname{area}(K^\circ)\), the exact Mahler-product deficit is
\[
9-\mathcal M(K)=\frac{c(a-b)^2+a(b-c)^2+b(c-a)^2}{D}.
\]
It obeys the **sharp global two-sided stability inequality**
\[
\boxed{\frac12 V(K)\le 9-\mathcal M(K)\le 2V(K).}
\]
For positive triples, both inequalities are strict unless \(a=b=c\), when both sides vanish. The constants \(1/2\) and \(2\) cannot be improved for the class of genuine symmetric hexagons. Moreover, at fixed \(S\), the Mahler product is strictly Schur-concave in \((a,b,c)\): every nontrivial majorization toward a more unequal triple strictly lowers the product (except permutations). Near an equal triple, the ratio of the positive deficit to \(V(K)\) tends to \(9/8\).

## Assumptions and scope

A hexagon is compact, has nonempty interior, is centrally symmetric, and has six noncollinear consecutive edges (no zero-length generators). The center is taken as the origin. Its polar is \(K^\circ=\{y:\langle y,x\rangle\le1\ \forall x\in K\}\). The center is the Santaló point by central symmetry. The inequalities hold for every \(a,b,c>0\), with no bounded aspect-ratio assumption. The majorization order uses triples with the same sum. Sharpness refers to limits within this open hexagon family, not equality at a degenerate endpoint.

Every such hexagon is the Minkowski sum of its three opposite edge-vector segments. A nonsingular linear transformation takes its three distinct unoriented edge directions to those of the displayed \(u_j\). A projective transformation of the real projective line fixing three distinct lines is the identity; hence two such normalized representations differ only by a scalar, and a permutation of the lines induces an affine automorphism. Thus \(V(K)\) is well defined on affine-equivalence classes of centrally symmetric genuine hexagons.

## Proof

**Exact areas.** For three vectors \(v_j=a_j u_j\), the area of the zonotope \(\sum[-v_j/2,v_j/2]\) is \(\sum_{i<j}|\det(v_i,v_j)|\). Since the three direction determinants have absolute value \(\sqrt3/2\),
\[
\operatorname{area}(K)=\frac{\sqrt3}{2}(ab+bc+ca)=\frac{\sqrt3}{2}Q.
\]
The six edges of \(K\) have directions \(\pm u_1,\pm u_2,\pm u_3\). The corresponding polar vertices lie on the six outward normals. In cyclic order, their radial lengths are the three values \(4/(\sqrt3(b+c))\), \(4/(\sqrt3(a+c))\), and \(4/(\sqrt3(a+b))\), repeated antipodally. Consecutive polar vertex rays differ by \(\pi/3\). Shoelace integration over those six triangles therefore gives
\[
\operatorname{area}(K^\circ)=\frac{16\sqrt3}{3}\frac{S}{D}.
\]
Thus, writing \(P=abc\) and using \(D=SQ-P\),
\[
\mathcal M(K)=\frac{8SQ}{D}=8+\frac{8P}{D},\qquad
9-\mathcal M(K)=\frac{SQ-9P}{D}.
\]
Direct expansion proves
\[
SQ-9P=c(a-b)^2+a(b-c)^2+b(c-a)^2=:W.
\]
This establishes the exact formula and already identifies the affine-regular equality case.

**Sharp global bounds.** Put \(N=(a-b)^2+(b-c)^2+(c-a)^2\), so \(V=N/S^2\). By permutation assume \(a\ge b\ge c>0\), and set \(x=a-b\), \(y=b-c\), \(z=c\). Then \(x,y\ge0\) and \(z>0\). The lower and upper inequalities are respectively equivalent to \(L:=2S^2W-DN\ge0\) and \(U:=2DN-S^2W\ge0\). Exact expansion in \(x,y,z\) yields
\[
\begin{aligned}
L={}&20z^3(x^2+xy+y^2)\\
&+2z^2(x+2y)(4x^2+13xy+13y^2)\\
&+4zy(x+y)(2x^2+11xy+11y^2)\\
&+6y^2(x+y)^2(x+2y),\\[2pt]
U={}&14z^3(x^2+xy+y^2)\\
&+z^2(x+2y)(20x^2+11xy+11y^2)\\
&+2z(3x^4+16x^3y+20x^2y^2+8xy^3+4y^4)\\
&+3x^2y(x+y)(x+2y).
\end{aligned}
\]
All terms are nonnegative. If \(x+y>0\), the first term of each expansion is strictly positive because \(z>0\). If \(x=y=0\), both vanish. Dividing by the positive \(2DS^2\) proves the stated inequalities with their equality conditions. Taking \(a=1,b=c=\varepsilon\to0^+\) gives \((9-\mathcal M)/V\to1/2\), while \(a=b=1,c=\varepsilon\to0^+\) gives the limit \(2\). Thus both constants are sharp.

**Majorization.** At fixed \(S\), \(\mathcal M=8/(1-P/(SQ))\) is increasing in \(f=P/Q\). For unequal positive \(a,b\), keeping \(c\) fixed,
\[
(\partial_a-\partial_b)\log f
=(b-a)\left(\frac1{ab}-\frac1Q\right).
\]
The bracket is positive since \(Q>ab\). Hence \((a-b)(\partial_a-\partial_b)\log f<0\) whenever \(a\ne b\). The standard differential criterion for Schur concavity, or equivalently integrating this inequality under a pairwise averaging transfer, yields strict Schur concavity modulo permutations. Finally, for \(a,b,c\to t>0\) with not all equal, the exact formulas give \(W=tN+o(N)\), \(D=8t^3+o(1)\), and \(S^2=9t^2+o(1)\), so \((9-\mathcal M)/V\to9/8\).

## Verification

The accompanying `verification.py` is self-contained and uses only the Python 3 standard library. Execute `python3 verification.py`. It expands and compares both nonnegative-certificate polynomials using exact integer coefficients, checks the exact rational inequalities for \(12^3=1728\) positive integer triples, and independently constructs convex hulls and polar vertices numerically to compare the resulting shoelace area products. The numerical examples are not an infinite proof; the nonnegative polynomial identities establish the universal inequalities.

## Relationship to prior work

Meyer and Reisner (2011), Theorem 2, already prove \(\mathcal M(K)\le9\) for centrally symmetric hexagons and characterize affine-regular equality; **that endpoint theorem is prior work, not a new result here**. The new statement is the explicit **global, two-sided, sharp** control of the Mahler-product deficit by a normalized generator variance on every affine class, including exact coefficients, equality, endpoint extremality, and strict Schur ordering. Their published argument is an extremal first-variation proof and does not state this quantitative global comparison.

Böröczky, Makai, Meyer and Reisner (2013; arXiv version 2015) prove lower bounds and stability around Mahler minima using Banach–Mazur distances. Their lower-end stability is not an upper deficit estimate against the affine-regular hexagon, nor does it give the displayed optimal constants. Other general affine-stability results may potentially imply weaker bounds in different metrics; equivalence to the present sharp fixed-gauge inequalities was not established.

## Limitations

The result is specific to centrally symmetric nondegenerate hexagons. It does not assert analogous sharp constants for arbitrary six-gons, centrally symmetric polygons with eight or more vertices, or higher-dimensional zonotopes. The invariant \(V\) is defined in the canonical three-direction affine gauge and is not the Euclidean variance of side lengths in an arbitrary drawing. The limiting sharp examples converge toward degenerate three-generator parameter triples, although each approximant is a genuine hexagon. Priority outside the inspected primary literature and available mathematical finding database is not conclusively settled.

## References

1. M. Meyer and S. Reisner, *On the volume product of polygons*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **81** (2011), 93–100. DOI: 10.1007/s12188-011-0054-3. First public online date stated in the paper: 2011-04-05. See Theorem 2 and Section 3.
2. K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies—lower estimates with stability*, Studia Scientiarum Mathematicarum Hungarica **50** (2013), 159–198. DOI: 10.1556/SScMath.50.2013.2.1235. Author preprint: arXiv:1507.01481.
