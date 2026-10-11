# Exact ordinary and fractional illumination of every product of simplices
## Finding
Let
\[
P=\Delta_{d_1}\times\cdots\times\Delta_{d_k}\subset\mathbb R^n,
\qquad
n=d_1+\cdots+d_k,
\]
where every \(\Delta_{d_j}\) is a nondegenerate simplex of dimension \(d_j\ge1\).

Then the ordinary and fractional illumination numbers coincide exactly with the number of vertices:
\[
\boxed{
 i(P)=i^*(P)=\prod_{j=1}^k(d_j+1)=f_0(P).
}
\tag{1}
\]

In particular, within the full product-of-simplices class the cube is the unique shape attaining the Hadwiger value \(2^n\). Every nonparallelotope product of simplices satisfies the sharp uniform gap
\[
\boxed{
 i(P)=i^*(P)\le3\cdot2^{n-2}=\frac34\,2^n.
}
\tag{2}
\]
Equality in (2) holds exactly when one factor is a triangle and all remaining factors are segments.

## Assumptions and scope
A nonzero vector \(u\) illuminates a boundary point \(x\in\partial K\) of a convex body \(K\) when
\[
x+\varepsilon u\in\operatorname{int}K
\]
for some \(\varepsilon>0\). The ordinary illumination number \(i(K)\) is the least cardinality of an illuminating set of directions.

For fractional illumination, a finitely supported nonnegative measure \(\mu\) on the unit sphere is admissible when, at every boundary point, the total \(\mu\)-weight of illuminating directions is at least one. Its infimum total weight is \(i^*(K)\).

Illumination numbers are invariant under invertible affine maps, so each simplex factor may be replaced by the standard simplex
\[
\Sigma_d=
\left\{x\in\mathbb R^d:
 x_j\ge0,
 \ \sum_{j=1}^d x_j\le1
\right\}.
\]

## Proof
We first prove the key simplex fact.

The vertices of \(\Sigma_d\) are
\[
0,e_1,\ldots,e_d.
\]
A vector \(u=(u_1,\ldots,u_d)\) lies in the interior tangent cone at the origin exactly when
\[
u_j>0
\qquad(1\le j\le d).
\tag{3}
\]
At the vertex \(e_i\), it lies in the interior tangent cone exactly when
\[
u_j>0\quad(j\ne i),
\qquad
\sum_{j=1}^d u_j<0.
\tag{4}
\]
These \(d+1\) open tangent cones are pairwise disjoint. Indeed, (3) is incompatible with the negative sum in (4). If \(i\ne h\), simultaneous membership in the cones at \(e_i\) and \(e_h\) would force every coordinate positive: the \(e_i\)-cone forces \(u_h>0\), the \(e_h\)-cone forces \(u_i>0\), and both force all other coordinates positive. This contradicts the required negative coordinate sum. The one-dimensional case is the same statement that the two endpoint tangent rays point in opposite directions.

Now let
\[
P=P_1\times\cdots\times P_k
\]
with each \(P_j\) a simplex. A vertex of \(P\) is a tuple
\[
v=(v_1,\\ldots,v_k),
\]
and the interior tangent cone factors as
\[
\operatorname{int}T_P(v)
=
\operatorname{int}T_{P_1}(v_1)
\times\cdots\times
\operatorname{int}T_{P_k}(v_k).
\tag{5}
\]
Hence a direction
\[
u=(u_1,\ldots,u_k)
\]
can illuminate two distinct vertices only if, in every factor, its block \(u_j\) belongs to the two corresponding simplex tangent-cone interiors. The simplex fact shows this is impossible as soon as the two vertices differ in one coordinate. Therefore
\[
\boxed{
\text{every direction illuminates at most one vertex of }P.
}
\tag{6}
\]

This already proves the lower bounds. Any ordinary illuminating set needs at least one direction per vertex, so
\[
i(P)\ge f_0(P).
\]
For a fractional illumination \(\mu\), let \(A_v\) be the set of directions illuminating a vertex \(v\). By (6), the sets \(A_v\) are pairwise disjoint. Since every vertex requires weight at least one,
\[
\mu(S^{n-1})
\ge
\sum_{v\in V(P)}\mu(A_v)
\ge
f_0(P),
\]
and thus
\[
i^*(P)\ge f_0(P).
\tag{7}
\]

For the matching upper bound, choose one vector
\[
u_v\in\operatorname{int}T_P(v)
\]
for every vertex \(v\). These \(f_0(P)\) directions illuminate every vertex. They also illuminate every boundary point. Indeed, if \(x\) lies in a face \(F\), choose a vertex \(v\) of \(F\). The facet inequalities active at \(x\) are a subset of those active at \(v\); since \(u_v\) points strictly inward through every facet active at \(v\), it also points strictly inward through every facet active at \(x\). Hence \(u_v\) illuminates \(x\). Therefore
\[
i(P)\le f_0(P).
\]
Assigning unit mass to the same directions gives
\[
i^*(P)\le f_0(P).
\]
Together with (7), this proves (1).

It remains to optimize the exact value at fixed dimension. Since
\[
d+1\le2^d
\]
for every \(d\ge1\), with equality only at \(d=1\), formula (1) gives
\[
i(P)=i^*(P)
=
\prod_j(d_j+1)
\le
2^{\sum_jd_j}=2^n.
\]
Equality holds exactly when every \(d_j=1\), namely for a parallelotope.

If at least one factor has dimension \(d\ge2\), then
\[
d+1\le3\cdot2^{d-2},
\tag{8}
\]
with equality only at \(d=2\). Applying (8) to one nonsingular factor and the inequality \(d_j+1\le2^{d_j}\) to all others gives
\[
\prod_j(d_j+1)
\le
3\cdot2^{n-2}.
\]
Equality requires exactly one two-dimensional factor and every remaining factor one-dimensional, proving (2) and its equality statement.

## Verification
The bundled `verify.py` checks the standard-simplex tangent-cone logic for deterministic integer directions in dimensions through eight, verifies product vertex counts, and exhaustively checks the fixed-dimension maximization over all integer partitions through dimension twelve.

These finite checks are only regression tests. The quantified proof is the exact cone-disjointness argument (3)--(6), followed by the elementary product estimate (8).

## Relationship to prior work
Naszódi introduced fractional illumination and placed it between antipodal-set size and ordinary illumination. His paper states the classical Levi--Hadwiger--Gohberg--Markus conjecture, records
\[
a(K)\le i^*(K)\le i(K),
\]
and proves the fractional \(2^d\) upper bound for centrally symmetric bodies, with equality for parallelotopes.

The result here concerns a different natural class: products of simplices, generally nonsymmetric unless every factor is a segment. It gives both ordinary and fractional values exactly, rather than only an upper bound.

Livshyts and Tikhomirov later proved that bodies sufficiently close to the cube but not parallelotopes use fewer than \(2^n\) directions. The present theorem is complementary: it gives a global exact formula on the entire product-of-simplices class, together with the dimension-free relative gap \(3/4\) from the cube for every nonparallelotope in that class.

Targeted searches under “product of simplices,” “polysimplex,” Cartesian-product, prism, ordinary illumination, and fractional illumination formulations did not locate a published theorem implying (1) or (2).

## Limitations
The multiplicative formula is proved for Cartesian products of simplices. It is not asserted for arbitrary Cartesian products of convex polytopes.

The theorem does not establish the general Hadwiger illumination conjecture or its fractional analogue. It verifies them, with a stronger exact statement, only on the product-of-simplices class.

The tangent-cone proof is short, so an equivalent result may exist implicitly in older illumination or simple-polytope literature under different terminology. This is the main residual originality risk.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4 (2009), 83--88. DOI: 10.55016/ojs/cdm.v4i2.62022.
2. G. Livshyts and K. Tikhomirov, *Cube is a strict local maximizer for the illumination number*, arXiv:1710.05070v1, 13 October 2017; *Discrete & Computational Geometry* 63 (2020), 209--228. DOI: 10.1007/s00454-019-00115-9.
