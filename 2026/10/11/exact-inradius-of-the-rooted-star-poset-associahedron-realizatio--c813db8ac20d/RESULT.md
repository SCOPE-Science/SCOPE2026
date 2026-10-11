# Exact inradius of the rooted-star poset associahedron realization
## Finding
For every integer
\[
n\ge3,
\]
let \(P_n\) be the rooted-star poset with one minimal element \(0\) and \(n-1\) incomparable maximal elements \(1,\ldots,n-1\), each covering \(0\). Consider Sack's explicit realization
\[
\mathscr A_{\mathrm{Sack}}(P_n)
\subset
\mathbb R^{P_n}_{\Sigma=0}
\]
of the poset associahedron.

Its unique Euclidean incenter is
\[
\boxed{
p_0^*=-n^{2n-1},
\qquad
p_i^*=\frac{n^{2n-1}}{n-1}
\quad
(1\le i\le n-1).
}
\tag{1}
\]

Its exact inradius is
\[
\boxed{
r_{\mathrm{in}}
\bigl(\mathscr A_{\mathrm{Sack}}(P_n)\bigr)
=
\frac{
n^{2n}-(n-1)n^4
}{
\sqrt{(n-1)(n-2)}
}.
}
\tag{2}
\]

The realization has
\[
2^{n-1}-2
\]
facets, one for each nonempty proper subset of the \(n-1\) leaves. Nevertheless, the maximal ball is tangent exactly to the
\[
n-1
\]
facets indexed by the two-element tubes
\[
\{0,i\},
\qquad
1\le i\le n-1.
\tag{3}
\]

Equivalently, after an isometric change of coordinates, the entire Euclidean Chebyshev problem is controlled by the singleton inequalities of a symmetric cardinality-dependent generalized permutahedron.

## Assumptions and scope
Sack's realization is the one defined in the cited source by the linear forms
\[
\alpha_\tau(p)
=
\sum_{\substack{i\lessdot j\\i,j\in\tau}}
(p_j-p_i),
\]
the full-tube hyperplane
\[
\alpha_{P_n}(p)=n^{2n},
\]
and the proper-tube halfspaces
\[
\alpha_\tau(p)\ge n^{2|\tau|}.
\]

The metric is the standard Euclidean metric inherited from \(\mathbb R^n\) on the affine span of the realization.

The theorem concerns the rooted-star family in this particular realization. It does not claim affine-invariant metric information for all combinatorially equivalent permutohedra, nor a general inradius formula for arbitrary poset associahedra.

## Proof
Write
\[
m=n-1
\]
for the number of leaves and define
\[
y_i=p_i-p_0
\qquad
(1\le i\le m).
\tag{4}
\]

For the rooted-star Hasse diagram, every cover relation is
\[
0\lessdot i.
\]
Hence
\[
\alpha_{P_n}(p)
=
\sum_{i=1}^{m}y_i.
\]
The full-tube equation is therefore
\[
\sum_{i=1}^{m}y_i
=
M,
\qquad
M=n^{2n}.
\tag{5}
\]

Since
\[
p_i=p_0+y_i
\]
and
\[
\sum_{i=0}^{m}p_i=0,
\]
equation (5) forces
\[
p_0=-\frac Mn,
\]
which is constant on the affine span. Therefore infinitesimal variations satisfy
\[
dp_0=0,
\qquad
dp_i=dy_i.
\]
Thus the map from the affine span of the \(p\)-realization to the hyperplane
\[
\sum_i y_i=M
\]
is an isometry for the inherited Euclidean metric.

The proper tubes are exactly
\[
\tau_S=\{0\}\cup S
\]
with
\[
\varnothing\ne S\subsetneq[m].
\]
For such a tube,
\[
\alpha_{\tau_S}(p)
=
\sum_{i\in S}y_i.
\]
Consequently the realization becomes
\[
\boxed{
\sum_{i=1}^{m}y_i=M,
\qquad
\sum_{i\in S}y_i
\ge
n^{2(|S|+1)}
\quad
\text{for }
\varnothing\ne S\subsetneq[m].
}
\tag{6}
\]

Consider first the singleton facets
\[
y_i=n^4.
\]
Inside the tangent space
\[
\mathbf1^\perp\subset\mathbb R^m,
\]
the projected normal is
\[
e_i-\frac1m\mathbf1,
\]
whose norm is
\[
\sqrt{\frac{m-1}{m}}.
\tag{7}
\]

If a radius-\(r\) Euclidean ball centered at \(c\) lies in the polytope, every singleton facet gives
\[
c_i-n^4
\ge
r\sqrt{\frac{m-1}{m}}.
\tag{8}
\]
Summing (8) over all \(i\) and using
\[
\sum_i c_i=M
\]
gives
\[
r
\le
\left(
\frac Mm-n^4
\right)
\sqrt{\frac{m}{m-1}}.
\tag{9}
\]
At equality in (9), every inequality in (8) must be equality, so the only possible optimal center is
\[
c_i^*=\frac Mm
\qquad
(1\le i\le m).
\tag{10}
\]

Returning to the original coordinates,
\[
p_0^*=-\frac Mn=-n^{2n-1},
\]
and
\[
p_i^*
=
-\frac Mn+\frac Mm
=
\frac{M}{n(n-1)}
=
\frac{n^{2n-1}}{n-1},
\]
which proves (1).

It remains to verify that the ball centered at (10) with radius equal to the right-hand side of (9) satisfies every non-singleton facet strictly.

Let
\[
k=|S|,
\qquad
1\le k\le m-1.
\]
The projected normal of the subset hyperplane
\[
\sum_{i\in S}y_i=n^{2(k+1)}
\]
has norm
\[
\sqrt{\frac{k(m-k)}m}.
\tag{11}
\]
Its distance from \(c^*\) is therefore
\[
D_k
=
\frac{
kM/m-n^{2(k+1)}
}{
\sqrt{k(m-k)/m}
}.
\tag{12}
\]
For \(k=1\), this is exactly the upper bound in (9).

Put
\[
A=\frac Mm
\]
and
\[
q_k
=
\frac{n^{2(k+1)}}A
=
\frac{m}{n^{2(m-k)}}.
\tag{13}
\]
Then
\[
\frac{D_k}{A}
=
\sqrt m\,
\frac{k-q_k}{\sqrt{k(m-k)}}.
\tag{14}
\]

For every
\[
1\le k\le m-1,
\]
one has
\[
q_k
\le
\frac{m}{n^2}
=
\frac{n-1}{n^2}
<
\frac14.
\tag{15}
\]
Hence for
\[
k\ge2,
\]
\[
k-q_k
>
k-\frac14
\ge
\frac78k.
\]
Thus
\[
\frac{D_k}{A}
>
\frac78
\sqrt{\frac{mk}{m-k}}.
\tag{16}
\]
On the other hand,
\[
\frac{D_1}{A}
=
\sqrt{\frac{m}{m-1}}\,(1-q_1)
<
\sqrt{\frac{m}{m-1}}.
\tag{17}
\]
For every
\[
k\ge2,
\]
\[
49k(m-1)-64(m-k)
=
m(49k-64)+15k
>
0,
\]
so
\[
\frac78
\sqrt{\frac{mk}{m-k}}
>
\sqrt{\frac{m}{m-1}}.
\tag{18}
\]
Equations (16)--(18) show
\[
D_k>D_1
\qquad
(2\le k\le m-1).
\tag{19}
\]

Therefore the singleton facets are exactly the closest facets to the forced center. The radius in (9) is attained, the center is unique, and only the singleton facets are tangent.

Finally, substituting
\[
M=n^{2n},
\qquad
m=n-1
\]
into (9) gives
\[
r_{\mathrm{in}}
=
\frac{
n^{2n}-(n-1)n^4
}{
\sqrt{(n-1)(n-2)}
},
\]
which proves (2)--(3).

## Verification
The proof is arbitrary-dimensional and symbolic. The only source-dependent ingredients are Sack's exact definition of \(\alpha_\tau\), the threshold \(n^{2|\tau|}\), the full-tube hyperplane, and the statement that the resulting halfspace intersection realizes the poset associahedron.

For the rooted-star poset, the reduction to (6) is exact: connected convex proper tubes are precisely the root together with a nonempty proper set of leaves.

The accompanying `verify.py` checks the formula for
\[
3\le n\le200.
\]
For every subset cardinality
\[
1\le k\le n-2,
\]
it computes the squared facet distance using exact rational arithmetic after clearing the projected-normal denominator, verifies that \(k=1\) is the unique minimizing cardinality, and confirms the closed inradius formula. These finite checks are corroborative only.

## Relationship to prior work
Sack gives the explicit halfspace realization of Galashin's poset associahedra used here. The source develops the realization through configuration spaces, tubes, and compactification geometry; it does not state an Euclidean inradius, Chebyshev-center, or metric-facet theorem.

For the rooted-star poset, all proper tubes contain the root, so proper tubings are chains of nonempty proper leaf subsets. Thus this poset associahedron is combinatorially a permutohedron, but Sack's realization is a highly nonstandard cardinality-weighted realization whose Euclidean metric is not determined by that combinatorial type.

Targeted published-result and literature searches used “poset associahedron”, “rooted star”, “star poset”, “inradius”, “Chebyshev center”, “largest inscribed ball”, and the source's \(\alpha_\tau\)-realization. The closest indexed star-poset result concerns interval-resolution complexity, not polyhedral metric geometry. No covering theorem was located.

## Limitations
The theorem treats only the rooted-star family in Sack's realization. General posets have overlapping tube geometries and nontrivial cover-graph normal vectors, so the same singleton-facet reduction need not hold.

The scale \(n^{2|\tau|}\) is built into the source realization. Different realizations of the same poset associahedron can have very different Euclidean inradii.

The exact inequality separating singleton facets from all larger tubes is elementary once the star reduction (6) is made. An equivalent observation could therefore exist as folklore about this specific symmetric generalized-permutahedral slice; search nonappearance is not treated as a formal global novelty certificate.

## References
1. Andrew Sack, *A realization of poset associahedra*, arXiv:2301.11449, first public version 2023-01-26. The arXiv record lists MSC \(52B11\) first.
2. Pavel Galashin, *\(P\)-associahedra*, arXiv:2110.07257.
