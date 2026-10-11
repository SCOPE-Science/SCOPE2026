# Loday's three canonical polytopes share one exact Euclidean inradius
## Finding
For \(n\ge2\), put
\[
H_n=
\left\{
x\in\mathbb R^n:
\sum_{i=1}^n x_i=\binom{n+1}{2}
\right\},
\qquad
\mu_n=\frac{n+1}{2}.
\]
Consider in \(H_n\), with its intrinsic Euclidean metric, the three canonical polytopes emphasized in the Loday-associahedron literature:
\[
\operatorname{Perm}(n),\qquad
\operatorname{Asso}(n),\qquad
\operatorname{Para}(n).
\]
They are respectively the standard permutahedron, Loday's associahedron, and Loday's parallelepiped.

All three have the same exact Euclidean inradius:
\[
\boxed{
r_n=
\frac{\sqrt{n(n-1)}}{2}.
}
\tag{1}
\]
Moreover, their known common vertex barycenter
\[
\boxed{
b_n=\mu_n\mathbf1
}
\tag{2}
\]
is an incenter of all three.

For \(\operatorname{Perm}(n)\) and \(\operatorname{Asso}(n)\), this incenter is unique.

For \(\operatorname{Para}(n)\), define
\[
p_i(c)=\sum_{j=1}^i c_j,
\qquad
a_i=\sqrt{\frac{i(n-i)}{n}}
\qquad
(1\le i<n).
\]
The complete incenter set is
\[
\boxed{
\binom{i+1}{2}+r_na_i
\le
p_i(c)
\le
\binom{n+1}{2}
-\binom{n-i+1}{2}
-r_na_i
\quad
(1\le i<n).
}
\tag{3}
\]
Thus \(\operatorname{Para}(2)\) and \(\operatorname{Para}(3)\) have a unique incenter, while for \(n\ge4\) the incenter set has dimension
\[
\boxed{n-3.}
\tag{4}
\]

The centered maximal ball at \(b_n\) has the following exact contact structure.

For \(\operatorname{Perm}(n)\), its tangent facets are precisely the subset facets indexed by subsets of cardinality \(1\) or \(n-1\). Hence there are \(2n\) tangent facets for \(n\ge3\), and two for \(n=2\).

For \(\operatorname{Asso}(n)\), its tangent facets are precisely the interval facets of cardinality \(1\) or \(n-1\). Hence there are
\[
\boxed{n+2}
\]
tangent facets for \(n\ge3\), and two for \(n=2\).

For \(\operatorname{Para}(n)\), its centered inball is tangent exactly to the endpoint prefix/suffix facets. For \(n\ge3\) these are
\[
x_1=1,\qquad x_1=n,\qquad x_n=1,\qquad x_n=n,
\]
so there are four tangent facets; for \(n=2\) there are two.

## Assumptions and scope
The realization is exactly the one used in the cited Loday-associahedron survey. In particular, all three polytopes lie in \(H_n\), and distance is measured intrinsically in that affine hyperplane.

The theorem is metric and therefore realization-dependent. Other affine realizations of the associahedron need not have the same inradius.

The word “incenter” means a center of a largest intrinsic Euclidean ball. It need not be unique in general; formula (3) describes all such centers for the parallelepiped.

## Proof
The cited survey gives the following facet descriptions.

For the permutahedron,
\[
\sum_{i\in I}x_i
\ge
\binom{|I|+1}{2}
\tag{5}
\]
for every nonempty proper subset \(I\subset[n]\).

For Loday's associahedron, the same inequality is retained only for intervals
\[
I=[a,b]\subsetneq[n].
\tag{6}
\]

For Loday's parallelepiped, only the prefix and suffix inequalities are retained:
\[
\sum_{j=1}^i x_j
\ge
\binom{i+1}{2},
\qquad
\sum_{j=i+1}^n x_j
\ge
\binom{n-i+1}{2}
\qquad
(1\le i<n).
\tag{7}
\]

Let \(I\subsetneq[n]\) have cardinality \(k\). Inside the tangent space
\[
\mathbf1^\perp,
\]
the intrinsic normal of the hyperplane
\[
\sum_{i\in I}x_i=\text{constant}
\]
is
\[
\nu_I=
\mathbf1_I-\frac{k}{n}\mathbf1.
\]
Its squared norm is
\[
\|\nu_I\|^2
=
k-\frac{k^2}{n}
=
\frac{k(n-k)}{n}.
\tag{8}
\]

At the common barycenter \(b_n=\mu_n\mathbf1\), the slack in (5) for a \(k\)-set is
\[
k\mu_n-\binom{k+1}{2}
=
\frac{k(n-k)}2.
\tag{9}
\]
Therefore the intrinsic distance from \(b_n\) to any retained facet supported on a \(k\)-set is
\[
d_k
=
\frac{k(n-k)/2}{\sqrt{k(n-k)/n}}
=
\frac12\sqrt{nk(n-k)}.
\tag{10}
\]
For \(1\le k\le n-1\),
\[
k(n-k)\ge n-1,
\]
with equality exactly at
\[
k=1
\quad\text{or}\quad
k=n-1.
\tag{11}
\]
Every one of the three facet systems retains at least one facet of one of these extremal cardinalities, so (10) shows that the centered ball
\[
B_{H_n}(b_n,r_n)
\]
with \(r_n\) from (1) is contained in all three polytopes.

For \(\operatorname{Perm}(n)\) and \(\operatorname{Asso}(n)\), all singleton inequalities
\[
x_i\ge1
\]
are facets. If \(B_{H_n}(c,r)\) is contained in either polytope, then by (8)
\[
c_i-1
\ge
r\sqrt{\frac{n-1}{n}}
\qquad
(i\in[n]).
\]
Summing and using
\[
\sum_i c_i=\binom{n+1}{2}
\]
gives
\[
\frac{n(n-1)}2
\ge
nr\sqrt{\frac{n-1}{n}},
\]
hence
\[
r\le\frac{\sqrt{n(n-1)}}2=r_n.
\tag{12}
\]
Equality in (12) forces equality in every singleton inequality above and therefore
\[
c_i=\mu_n
\]
for every \(i\). This proves both the exact inradius and uniqueness of the incenter for the permutahedron and associahedron.

For \(\operatorname{Para}(n)\), the two facets
\[
x_1=1
\qquad\text{and}\qquad
x_1=n
\]
are parallel intrinsic hyperplanes. Their distance inside \(H_n\) is
\[
\frac{n-1}{\sqrt{(n-1)/n}}
=
\sqrt{n(n-1)}.
\]
No Euclidean ball lying between them can have radius larger than half this distance, which is \(r_n\). The centered ball already attains that value, so the parallelepiped has the same inradius.

It remains to describe all parallelepiped incenters. The intrinsic normal norm for a prefix of size \(i\) is \(a_i\). Thus a radius-\(r_n\) ball centered at \(c\) lies between the corresponding prefix and suffix facets if and only if
\[
p_i(c)-\binom{i+1}{2}
\ge
r_na_i
\]
and
\[
\binom{n+1}{2}-p_i(c)-\binom{n-i+1}{2}
\ge
r_na_i.
\]
These are exactly the two inequalities in (3).

The coordinates
\[
p_1,\ldots,p_{n-1}
\]
are independent affine coordinates on \(H_n\). At \(i=1\) and \(i=n-1\), the interval in (3) collapses to a point. For
\[
1<i<n-1,
\]
its length is
\[
i(n-i)-\sqrt{(n-1)i(n-i)},
\tag{13}
\]
which is strictly positive because
\[
i(n-i)>n-1.
\]
This proves (4) and the uniqueness statement for \(n=2,3\).

Finally, the tangency classifications follow directly from (10)--(11) and the retained facet families in (5)--(7).

## Verification
The proof is exact and arbitrary-dimensional. It requires no finite computation.

The source-dependent inputs were checked directly in the full text of the cited survey: the common affine hyperplane, all three facet descriptions, the removahedron nesting
\[
\operatorname{Perm}(n)\subseteq\operatorname{Asso}(n)\subseteq\operatorname{Para}(n),
\]
and the previously known equality of their vertex barycenters.

The accompanying `verify.py` symbolically checks the distance formula, tangent-cardinality conditions, and parallelepiped incenter interval lengths for dimensions \(2\) through \(30\). These calculations are corroborative only.

## Relationship to prior work
Pilaud, Santos, and Ziegler present these three polytopes together and emphasize three geometric relationships among them. In particular, they record the removahedron nesting and the previously known fact that the vertex barycenters of
\[
\operatorname{Perm}(n),\quad
\operatorname{Asso}(n),\quad
\operatorname{Para}(n)
\]
all coincide. They also provide the facet descriptions used in the proof above.

The earlier barycenter theorem of Hohlweg, Lortie, and Raymond establishes the common vertex barycenter for the permutahedron and associahedron. A barycenter statement is not an inradius statement: a vertex barycenter need not be an incenter of a general polytope.

The inspected survey contains no occurrence of “inradius,” “circumradius,” “Chebyshev,” or “radius.” Targeted searches for Loday associahedron inradius, common inradii of the three Loday polytopes, Chebyshev centers, largest inscribed balls, and the characteristic value
\[
\frac{\sqrt{n(n-1)}}2
\]
did not locate a theorem implying the result above.

The new metric statement complements the known barycenter coincidence: the same point is not merely a common vertex barycenter, but an incenter of all three polytopes, and the three bodies have exactly the same inradius despite strictly nested facet systems. Their incenter geometry nevertheless separates sharply, because the parallelepiped develops a positive-dimensional incenter set for \(n\ge4\).

## Limitations
The result concerns the canonical Loday realization and intrinsic Euclidean distance in its standard affine hyperplane. It does not extend automatically to other associahedron realizations.

The literature comparison cannot exclude an equivalent observation hidden in older associahedron or generalized-permutahedron literature under different metric terminology. The exact facet systems make the proof short once the Euclidean normal projection is written down, so folklore is a genuine residual risk.

No claim is made here about the circumradii, John ellipsoids, or other metric invariants of the three polytopes.

## References
1. Vincent Pilaud, Francisco Santos, and Günter M. Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471, first public version 2023-05-15; Archiv der Mathematik 121 (2023), 559--601, DOI 10.1007/s00013-023-01895-6.
2. Christophe Hohlweg, Jonathan Lortie, and Annie Raymond, *The Centers of Gravity of the Associahedron and of the Permutahedron are the Same*, Electronic Journal of Combinatorics 17 (2010), R72, DOI 10.37236/344.
3. Jean-Louis Loday, *Realization of the Stasheff Polytope*, Archiv der Mathematik 83 (2004), 267--278.
