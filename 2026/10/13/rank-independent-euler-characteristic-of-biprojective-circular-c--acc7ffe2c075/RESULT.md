# Rank-independent Euler characteristic of biprojective circular-complex components
## Finding
Let
\[
2\le a\le b,
\]
let
\[
X:\mathbb C^a\longrightarrow\mathbb C^b,
\qquad
Y:\mathbb C^b\longrightarrow\mathbb C^a,
\]
and define the biprojective circular-complex variety
\[
Z_{a,b}
=
\left\{
([X],[Y])
\in
\mathbb P\operatorname{Hom}(\mathbb C^a,\mathbb C^b)
\times
\mathbb P\operatorname{Hom}(\mathbb C^b,\mathbb C^a)
:
XY=0,\ YX=0
\right\}.
\]

For every
\[
1\le c\le a-1,
\]
put
\[
Z_{a,b}^{(c)}
=
\left\{
([X],[Y])\in Z_{a,b}:
\operatorname{rank}X\le c,\ 
\operatorname{rank}Y\le a-c
\right\}.
\]
These are the natural biprojective rank closures associated with the irreducible circular-complex components whose dense affine orbits have ranks
\[
(c,a-c).
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(Z_{a,b}^{(c)}\right)
=
a(a-1)b(b-1)
}
\]
for every
\[
1\le c\le a-1.
\]
Moreover the full biprojective variety has the same Euler characteristic:
\[
\boxed{
\chi_{\mathrm{top}}(Z_{a,b})
=
a(a-1)b(b-1).
}
\]

Since the ambient product has Euler characteristic
\[
(ab)^2,
\]
the common ratio is
\[
\boxed{
\frac{\chi_{\mathrm{top}}(Z_{a,b}^{(c)})}{(ab)^2}
=
\frac{\chi_{\mathrm{top}}(Z_{a,b})}{(ab)^2}
=
\left(1-\frac1a\right)
\left(1-\frac1b\right).
}
\]

For
\[
a=1,
\]
there is no pair of nonzero maps in opposite directions whose two compositions both vanish, so the biprojective variety is empty and its Euler characteristic is zero.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

Each matrix is projectivized separately. Thus points of
\[
Z_{a,b}
\]
represent circular complexes with both arrows nonzero, modulo independent nonzero scalar multiplication of the two arrows.

The source literature studies the affine variety
\[
L_{a,b}
=
\{(X,Y):XY=0,\ YX=0\}
\]
and its orbit closures. The equations and rank conditions are bihomogeneous in the two matrix blocks, so the varieties above are the corresponding natural closed subvarieties of the product of the two projective matrix spaces.

The theorem concerns ordinary topological Euler characteristic. It does not assert equality of Betti numbers, Hodge numbers, dimensions, singularities, or multidegrees of the different rank closures.

## Proof
Choose bases of
\[
\mathbb C^a
\quad\text{and}\quad
\mathbb C^b.
\]
The diagonal torus
\[
T=(\mathbb C^*)^a\times(\mathbb C^*)^b
\]
acts by
\[
(g_a,g_b)\cdot(X,Y)
=
(g_bXg_a^{-1},\,g_aYg_b^{-1}).
\]
Both composition equations and all rank bounds are invariant under this action.

Choose a generic integral one-parameter subgroup
\[
\lambda:\mathbb C^*\longrightarrow T
\]
whose induced weights on each matrix-coordinate space are pairwise distinct. Such a cocharacter exists because every unwanted equality of two coordinate weights cuts out a proper integral hyperplane.

Therefore the fixed points in each projective matrix factor are precisely the matrix-coordinate points. Write
\[
X=E_{j i},
\qquad
Y=E_{\ell k},
\]
where
\[
1\le i,\ell\le a,
\qquad
1\le j,k\le b.
\]
Here
\[
E_{j i}:\mathbb C^a\to\mathbb C^b
\]
sends the \(i\)-th basis vector to the \(j\)-th basis vector, and
\[
E_{\ell k}:\mathbb C^b\to\mathbb C^a
\]
sends the \(k\)-th basis vector to the \(\ell\)-th basis vector.

The composition
\[
XY:\mathbb C^b\to\mathbb C^b
\]
is nonzero exactly when
\[
\ell=i,
\]
while
\[
YX:\mathbb C^a\to\mathbb C^a
\]
is nonzero exactly when
\[
k=j.
\]
Thus a coordinate pair lies in the circular-complex variety exactly when
\[
\ell\ne i
\qquad\text{and}\qquad
k\ne j.
\]

There are
\[
a(a-1)
\]
ordered choices for
\[
(i,\ell)
\]
with distinct entries, and
\[
b(b-1)
\]
ordered choices for
\[
(j,k)
\]
with distinct entries. Hence
\[
\# Z_{a,b}^{\mathbb C^*}
=
a(a-1)b(b-1).
\]

Every such coordinate pair has
\[
\operatorname{rank}X=\operatorname{rank}Y=1.
\]
Consequently, for every
\[
1\le c\le a-1,
\]
all these fixed points also lie in
\[
Z_{a,b}^{(c)},
\]
and there are no other fixed points there. Therefore
\[
\#\left(Z_{a,b}^{(c)}\right)^{\mathbb C^*}
=
a(a-1)b(b-1)
\]
independently of \(c\).

For a complex projective algebraic variety with an algebraic
\[
\mathbb C^*
\]
action, compactly supported Euler characteristic equals that of the fixed locus. Because the varieties here are projective, compactly supported and ordinary Euler characteristics agree. The fixed loci are finite, so
\[
\chi_{\mathrm{top}}\!\left(Z_{a,b}^{(c)}\right)
=
a(a-1)b(b-1).
\]
The same argument applied to the full union
\[
Z_{a,b}
\]
gives the identical value.

Finally,
\[
\chi_{\mathrm{top}}
\left(
\mathbb P^{ab-1}\times\mathbb P^{ab-1}
\right)
=
(ab)^2,
\]
which yields the ratio formula.

## Verification
The bundled checker exhaustively enumerates all coordinate matrix-unit pairs for
\[
2\le a\le12,
\qquad
a\le b\le12.
\]
For every pair
\[
(a,b)
\]
it checks the two matrix-unit composition conditions directly and compares the surviving count with
\[
a(a-1)b(b-1).
\]

For every
\[
1\le c\le a-1,
\]
it separately checks that every surviving fixed point has ranks bounded by
\[
(c,a-c),
\]
so the fixed-point count is rank-independent across all nontrivial biprojective component closures.

The checker also verifies the zero boundary at
\[
a=1
\]
and the ambient Euler ratio.

These finite computations are regression evidence only. The all-parameter theorem is the torus-fixed-point argument above.

## Relationship to prior work
Mehta and Trivedi study the affine variety of circular complexes and its orbit closures, proving strong singularity properties. Their classification record lies in algebraic geometry, with \(14M05\) listed first among its MSC entries.

Magyar gives an open full-text treatment of the same two-step circular-complex variety
\[
L_{a,b}
=
\{(X,Y):XY=0,\ YX=0\}.
\]
He records that it has finitely many orbits and that, for
\[
a\le b,
\]
its irreducible components are the closures of the dense orbits with rank pairs
\[
(c,a-c),
\qquad
0\le c\le a.
\]
He then realizes those component closures as opposite cells of affine Schubert varieties and recovers their normality, Cohen--Macaulayness, and rational singularities.

Targeted full-text searches in Magyar's paper found no occurrence of “Euler,” “Poincaré,” “Betti,” “topolog,” or “fixed point.” Targeted semantic and web searches for circular complexes together with Euler characteristic, biprojective topology, matrix-unit fixed points, and Poincaré polynomials did not locate the formula above.

The result is not implied by the Euler formula for a linear multiprojective chain complex. Closing a two-arrow chain into a circular complex adds a second composition equation and removes both free endpoints. The resulting fixed-point count is therefore
\[
a(a-1)b(b-1),
\]
and the rank-independence across the distinct circular-complex component closures is a genuinely cyclic feature of this parameter space.

## Limitations
The theorem computes only ordinary Euler characteristic. The rank closures have different dimensions and singularity geometry despite sharing this invariant.

The biprojective parameter space excludes the affine coordinate axes because both arrows are required to be nonzero.

The fixed-point proof is short, so an older unindexed or folklore computation under different terminology remains a residual originality risk.

## References
V. B. Mehta and V. Trivedi, *The variety of circular complexes and \(F\)-splitting*, *Inventiones Mathematicae* 137 (1999), 449--460, DOI 10.1007/s002220050333.

P. Magyar, *Affine Schubert Varieties and Circular Complexes*, arXiv:math/0210151, submitted 10 October 2002.
