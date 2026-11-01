# Sharp crossing probability for independently sampled shortest geodesics on flat two-tori

## Finding

Let \(T=\mathbb R^2/\Lambda\) be any Euclidean flat two-torus. Sample four points \(A,B,C,D\) independently from normalized area measure, and connect \(A\) to \(B\) and \(C\) to \(D\) by their shortest geodesic segments. These segments are uniquely determined almost surely. Write \(p(T)\) for the probability that their interiors intersect transversely. Then

\[
\boxed{\frac{22}{243}\leq p(T)\leq\frac5{54}.}
\]

Equality on the left holds exactly for the equilateral/hexagonal flat torus up to similarity. Equality on the right holds exactly for rectangular flat tori, without any restriction on their aspect ratio. These equality claims concern unmarked, unoriented flat tori.

More precisely, choose a reduced lattice basis such that, after a similarity and possibly a reflection, \(\Lambda=\langle1,\tau\rangle\), where \(\tau=a+ib\), \(0\leq a\leq1/2\), and \(a^2+b^2\geq1\). Put \(B=a^2+b^2\) and \(q=2a\), so \(B\geq1\) and \(0\leq q\leq1\). The complete probability profile is

\[
\boxed{p(T)=\frac5{54}-\frac{q^2(2B-q)^2(2-q)^2}{18(4B-q^2)^3}.}
\]

For each fixed \(q>0\), this probability increases strictly with \(B\); for fixed \(B=1\), it decreases strictly as \(q\) increases from \(0\) to \(1\). A structural intermediate identity, useful independently of lattice reduction, is

\[
 p(T)=\frac{\mathbb E|\det(U,V)|}{\operatorname{area}(\mathcal V)},
\]

where \(\mathcal V\) is the centered Euclidean Voronoi cell of \(\Lambda\), and \(U,V\) are independent uniform points in \(\mathcal V\). Moreover, the two random minimizing arcs have **at most one transverse intersection almost surely**, so the determinant expression is a crossing probability, not merely an expected crossing count.

## Assumptions and scope

The metric is the quotient of the Euclidean metric; the torus lattice has rank two; the four endpoints are independent and Haar-uniform in area. Segments are minimizing and are not complete closed geodesics. Events of nonunique minimizing segments, shared endpoints, tangencies, and coincident arcs have probability zero. The reflection and similarity used to reduce the lattice do not affect crossing probabilities.

## Proof

**1. From shortest geodesics to a determinant.** Let \(\mathcal V\) be the Voronoi cell of the origin in \(\mathbb R^2\) for \(\Lambda\). It is a centrally symmetric convex fundamental domain, with area \(S=\det\Lambda\). By independence and translation invariance, the displacement of a minimizing geodesic between two Haar-uniform endpoints is uniform in \(\mathcal V\). The displacements \(U,V\) of the two independent arcs are independent; their initial points also have independent Haar distributions.

Condition on \(U,V\), outside the measure-zero collinear case. Translating the first starting point to the origin, write \(W\) for the second starting point relative to it, modulo \(\Lambda\). A transverse intersection exists precisely when

\[
 W\equiv sU-tV\pmod\Lambda\quad\text{for some }(s,t)\in(0,1)^2.
\]

The map from the open unit parameter square to the torus is injective almost everywhere. Indeed, if two different parameter pairs mapped to the same torus point, then \((s-s')U\) and \((t-t')V\) would represent the same lattice class. Their coefficients have magnitude below one, so both vectors lie in the interior of the convex Voronoi fundamental cell \(\mathcal V\). Two distinct interior points of a fundamental cell cannot differ by a lattice vector; therefore the two vectors coincide. Linear independence of \(U,V\) forces \(s=s'\) and \(t=t'\). This also proves the one-intersection assertion. The area formula for this injective affine map gives

\[
 \mathbb P(\text{crossing}\mid U,V)=\frac{|\det(U,V)|}{S}.
\]

Averaging proves the structural identity. All boundary exceptions are null events.

**2. Reduced Voronoi hexagons.** A planar lattice admits the reduced basis described in the finding (on boundary identifications the represented torus may admit more than one reduced basis). Take the invertible linear coordinate map \(x\mapsto(u,v)=(2\langle x,1\rangle,2\langle x,\tau\rangle)\), identifying complex numbers with planar vectors. The three relevant Voronoi inequalities, for the vectors \(1\), \(\tau\), and \(\tau-1\), become

\[
 H_{B,q}=\{(u,v):|u|\leq1,\ |v|\leq B,\ |v-u|\leq B+1-q\}.
\]

For \(B\geq1\) and \(0\leq q\leq1\), this is a rectangle with two opposite right triangles removed. Its area is \(S'=4B-q^2\). The normalized determinant functional \(\mathbb E|\det(U,V)|/\operatorname{area}(H_{B,q})\) is invariant under invertible linear coordinate changes (both determinants and areas gain the same absolute factor), so this transformed domain can be used directly.

**3. Exact two-point determinant integral.** Let \(H_+=H_{B,q}\cap\{v\geq0\}\). In counterclockwise order its boundary points on successive rays are

\[
 z_0=(1,0),\quad z_1=(1,B),\quad z_2=(q-1,B),\quad
 z_3=(-1,B-q),\quad z_4=(-1,0).
\]

Partition \(H_+\) into four triangles \(T_i=\operatorname{conv}(0,z_i,z_{i+1})\), with zero-area pieces retained at degeneracies. Put \(d_i=\det(z_i,z_{i+1})\) and \(w_i=z_i+z_{i+1}\). Explicitly,

\[
(d_0,d_1,d_2,d_3)=(B,\ B(2-q),\ q(B+1-q),\ B-q).
\]

For two independent points uniform in a triangle \(\operatorname{conv}(0,z,z')\) with \(d=\det(z,z')>0\), the expectation of the absolute determinant is \(4d/27\). To prove this, write each point as \(r[(1-t)z+tz']\), where \(t\) is uniform on \([0,1]\), \(r\) has density \(2r\) on \([0,1]\), and the variables are independent. Then \(\mathbb E r=2/3\) and \(\mathbb E|t-t'|=1/3\).

For \(i<j\), the angular sectors of \(T_i,T_j\) lie in ordered intervals of the same closed half-plane. Their mutual determinants are nonnegative. Using the triangle centroid \(w_i/3\), the self-sector and cross-sector integrals can be summed exactly. Central symmetry gives the factor of four:

\[
\begin{aligned}
I(B,q)&=\int_{H_{B,q}}\!\int_{H_{B,q}}|\det(x,y)|\,dx\,dy\\
&=\frac4{27}\sum_{i=0}^3d_i^3
+\frac2{9}\sum_{0\leq i<j\leq3}d_i d_j\det(w_i,w_j).
\end{aligned}
\]

Direct polynomial expansion and factorization yield the exact identity

\[
54I(B,q)=5(4B-q^2)^3-3q^2(2B-q)^2(2-q)^2.
\]

Since \(p=I/(S')^3\), the announced formula follows. The file `verification/check_crossing.py` independently verifies the polynomial identity by exact rational interpolation over its full bidegree bounds and tests direct projected segment crossings.

**4. Sharp bounds and equality.** Set

\[
\Delta(B,q)=\frac5{54}-p(T)
=\frac{q^2(2B-q)^2(2-q)^2}{18(4B-q^2)^3}.
\]

It is nonnegative, and vanishes exactly when \(q=0\). For \(q>0\), logarithmic differentiation gives

\[
\frac{\partial\log\Delta}{\partial B}
=-\frac{4(2B+q^2-3q)}{(2B-q)(4B-q^2)}\leq0,
\]

because \(2B+q^2-3q=2(B-1)+(q-1)(q-2)\geq0\). Thus \(\Delta(B,q)\leq\Delta(1,q)\), with equality for \(q>0\) only when \(B=1\). Finally,

\[
\Delta(1,q)=\frac{q^2(2-q)}{18(2+q)^3},\qquad
\frac{d}{dq}\Delta(1,q)=\frac{4q(1-q)}{9(q+2)^4}\geq0.
\]

The unique maximum of \(\Delta\) occurs at \((B,q)=(1,1)\), with value \(1/486\). Therefore \(p\geq 5/54-1/486=22/243\). The point \((B,q)=(1,1)\) represents the equilateral lattice; \(q=0\) represents a rectangular lattice. Both are feasible, so both bounds and equality classifications are sharp. \(\square\)

## Verification

Exact-rational polynomial checks use the triangle-sector formula and its bidegree bounds (degree at most three in \(B\) and six in \(q\)). A separate random-position calculation samples two minimizing displacement vectors, varies the relative start point uniformly modulo the lattice, and directly solves intersection equations over nearby deck translations. The checker validates the non-multiplicity assertion and checks its empirical intersection frequencies against the exact formula on rectangular, equilateral, and intermediate lattices. Finite tests corroborate but are not substitutes for the preceding proof.

## Relationship to prior work

Glorieux and Yarmola (2020, arXiv:2003.08190v1), especially Proposition 2.2, Proposition 3.1, and Theorem 1.1, study the probability that a random *three-vertex geodesic triangle* on a flat torus is null-homotopic. Their key quantity is a three-copy intersection functional \(F(D,D,D)\), not the two-arc crossing probability or the absolute-determinant functional above. The reduced Voronoi-cell description is credited to that work. Both problems distinguish rectangular and equilateral lattices, but neither event nor its integral formula coincides.

Artzrouni (2007, arXiv:0712.1477v1) studies crossings of fixed-length random-direction steps in planar regions and on spheres, with approximate formulas in suitable regimes. That sampling scheme does not choose shortest arcs between independent uniform points on a compact flat torus. The random-simplex results discussed by Rademacher (2010, arXiv:1008.3944v1, in particular the Busemann inequality quoted as Lemma 9) give general affine bounds but neither of the torus-specific sharp endpoints or equality classifications established here.

## Limitations

No statement is made for curved tori, other quotient dimensions, nonuniform endpoint sampling, complete geodesics, or nonminimizing arcs. The exact result is a two-arc probability; it does not by itself determine higher-order crossing correlations. Historical priority is provisionally assessed from the inspected sources and mathematical-record comparisons; unindexed equivalent formulas remain a possibility.

## References

1. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190v1, first public March 18, 2020, https://arxiv.org/abs/2003.08190.
2. M. Artzrouni, *Crossing paths in 2D random walks*, arXiv:0712.1477v1, December 10, 2007, https://arxiv.org/abs/0712.1477.
3. L. Rademacher, *On the monotonicity of the expected volume of a random simplex*, arXiv:1008.3944v1, August 24, 2010, https://arxiv.org/abs/1008.3944.
4. *Mathematics Subject Classification 2020*, entry 53C22 (geodesics).
