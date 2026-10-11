# Singleton collision facets determine the inball of the Bottman–Poliakova constrainahedron
## Finding
Let
\[
m,n\ge3,\qquad d=m+n-2,
\]
and let
\[
C_{\mathrm{BP}}(m,n)\subset\mathbb R^d
\]
be the explicit constrainahedron realization of Bottman and Poliakova. Its affine hull is
\[
\sum_{i=1}^{d} z_i=C,\qquad
C=\binom n2\binom m2+\binom n2+\binom m2.
\tag{1}
\]
Put
\[
\mu=\frac Cd.
\tag{2}
\]
With the Euclidean metric inherited by the affine hyperplane (1), the incenter is unique and equals
\[
\boxed{c_*=\mu\mathbf1.}
\tag{3}
\]
The exact inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(C_{\mathrm{BP}}(m,n)\bigr)
=
\frac{C-d}{\sqrt{d(d-1)}}.
}
\tag{4}
\]
The maximal ball is tangent exactly to the
\[
\boxed{d=m+n-2}
\]
singleton collision facets
\[
z_i=1.
\tag{5}
\]

There is a quantitative reason. Suppose a facet uses \(t\) collision coordinates. Decompose its selected horizontal coordinates into maximal interval runs of lengths
\[
r_1,\ldots,r_a
\]
and its selected vertical coordinates into maximal interval runs of lengths
\[
q_1,\ldots,q_b.
\]
Set
\[
R=\sum_i r_i,\qquad Q=\sum_j q_j,\qquad t=R+Q.
\tag{6}
\]
After translating all coordinates by \(1\), the facet offset is at most
\[
\boxed{
F(R,Q)
=
\binom R2+\binom Q2+
\binom{R+1}{2}\binom{Q+1}{2}.
}
\tag{7}
\]
For every proper nonsingleton facet,
\[
\frac{F(R,Q)}{t(t-1)}
<
\frac{C-d}{d(d-1)}.
\tag{8}
\]
This strict density gap makes every nonsingleton facet inactive at the inball.

## Assumptions and scope
The parameters satisfy
\[
m,n\ge3.
\]
This guarantees that singleton horizontal and vertical collision sets are proper intervals and hence genuine facets in the Bottman–Poliakova classification.

The realization is exactly the convex realization defined from good rectangular preorders and the explicit coordinates in the cited source. Distances are intrinsic to (1), with the metric inherited from the ambient coordinate space.

The result is realization-specific. A combinatorially equivalent constrainahedron realization need not have the same Euclidean inradius.

## Proof
Bottman and Poliakova use \(n-1\) horizontal collision coordinates and \(m-1\) vertical collision coordinates. Their affine-sum lemma gives (1).

Their facets have three types. For a horizontal interval of \(r\) selected collision coordinates, the facet equation is
\[
z(S)=\binom{r+1}{2},
\tag{9}
\]
and the vertical case is identical.

For a mixed facet, let the selected horizontal coordinates be a union of separated interval runs of lengths \(r_1,\ldots,r_a\), and let the selected vertical coordinates be a union of separated interval runs of lengths \(q_1,\ldots,q_b\). Define
\[
U=\sum_i\binom{r_i+1}{2},
\qquad
V=\sum_j\binom{q_j+1}{2}.
\tag{10}
\]
The source gives the mixed facet constant
\[
h=U+V+UV.
\tag{11}
\]

Translate by
\[
w=z-\mathbf1.
\]
A facet supported on \(t\) coordinates changes its lower constant from \(h\) to \(h-t\).

For a pure interval, \(h-t=\binom R2=F(R,0)\). For a mixed facet,
\[
h-t=(U-R)+(V-Q)+UV.
\tag{12}
\]
Because the interval runs are disjoint,
\[
U-R=\sum_i\binom{r_i}{2}\le\binom R2,
\qquad
U\le\binom{R+1}{2},
\]
and similarly for \(V,Q\). Substituting these bounds in (12) proves (7).

Write
\[
H=n-1,\qquad K=m-1,\qquad d=H+K.
\]
A direct simplification gives
\[
C-d=F(H,K).
\tag{13}
\]

For positive \(R,Q\), define
\[
G(R,Q)=\frac{F(R,Q)}{(R+Q)(R+Q-1)}.
\tag{14}
\]
Direct algebra gives
\[
G(R+1,Q)-G(R,Q)
=
\frac{
Q\bigl((Q^2+1)R+(Q-1)^2\bigr)
}{
2(R+Q)(R+Q-1)(R+Q+1)
}.
\tag{15}
\]
Thus \(G\) is strictly increasing in \(R\) when \(R,Q\ge1\), and by symmetry it is strictly increasing in \(Q\). If one coordinate is zero,
\[
G(R,0)=\frac12.
\tag{16}
\]
Since \(H,K\ge2\), the full density \(G(H,K)\) is strictly larger than \(1/2\).

Every proper nonsingleton facet therefore satisfies
\[
\frac{h-t}{t(t-1)}
\le G(R,Q)
<
G(H,K)
=
\frac{C-d}{d(d-1)}.
\tag{17}
\]

At the uniform point \(c_*\), the slack of a \(t\)-coordinate facet is
\[
\frac{tC}{d}-h
=
\frac{t(C-d)}d-(h-t).
\tag{18}
\]
Using (17),
\[
\frac{tC}{d}-h
>
\frac{C-d}{d}\frac{t(d-t)}{d-1}.
\tag{19}
\]
Inside the tangent space \(\mathbf1^\perp\), the projected normal of a \(t\)-coordinate subset has norm
\[
\sqrt{\frac{t(d-t)}d}.
\tag{20}
\]
Thus every nonsingleton facet has distance strictly larger than
\[
\frac{C-d}{\sqrt{d(d-1)}}
\sqrt{\frac{t(d-t)}{d-1}}
\ge
\frac{C-d}{\sqrt{d(d-1)}}.
\tag{21}
\]

For a singleton facet \(z_i=1\), the distance from \(c_*\) is exactly
\[
\frac{\mu-1}{\sqrt{(d-1)/d}}
=
\frac{C-d}{\sqrt{d(d-1)}}.
\tag{22}
\]
Hence the ball in (4) is feasible and touches exactly the singleton facets.

Finally, suppose a radius-\(r\) ball centered at \(q\) lies in the polytope. Every singleton facet gives
\[
q_i-1\ge r\sqrt{\frac{d-1}{d}}.
\]
Summing over all coordinates and using \(\sum_iq_i=C\) yields
\[
r\le\frac{C-d}{\sqrt{d(d-1)}}.
\]
At equality every singleton inequality is equality, forcing \(q_i=\mu\) for all \(i\). This proves optimality and uniqueness.

## Verification
The proof is symbolic and applies to every \(m,n\ge3\).

The source-dependent inputs were checked directly in the primary full text and page images: the affine-sum lemma, the three facet types, the pure-interval facet constants, and the mixed-facet constant (11).

The accompanying `verify.py` enumerates all horizontal and vertical collision subsets for \(3\le m,n\le9\). It decomposes each subset into maximal interval runs, rebuilds the source facet constants, computes exact squared intrinsic distances from the uniform center, and verifies that the unique minimizing facet class consists of singleton intervals. The finite replay is corroborative only.

## Relationship to prior work
Bottman and Poliakova introduced constrainahedra as polytopes encoding collisions of horizontal and vertical lines and gave the explicit realization used here. Their paper proves the lattice, convex realization, affine-sum formula, and complete facet description, but does not state an inradius or Chebyshev-center theorem.

Chapoton and Pilaud independently realize the same constrainahedron combinatorial family through shuffles of associahedra. Their published paper is classified primarily under MSC \(52B11\), and it explicitly distinguishes its realization geometrically from the Bottman–Poliakova realization. Metric statements about that shuffle realization therefore do not imply the theorem here.

The directly inspected Bottman–Poliakova full text contains no occurrence of “inradius”, “Euclidean”, “Chebyshev”, or “circumradius”. Targeted literature and published-result searches under constrainahedron, good rectangular preorder, inradius, Chebyshev center, and Euclidean facet-distance formulations did not locate a covering theorem.

## Limitations
The theorem is specific to the Bottman–Poliakova realization. It does not assert the same radius for the geometrically different shuffle realization or for arbitrary affine realizations.

The range \(m,n\ge3\) is deliberate. Boundary cases can have different equality patterns and are not included.

The result determines the inball and tangent facets, not the circumradius, John ellipsoid, or full pairwise vertex metric.

A residual originality risk remains for an equivalent Chebyshev-center observation expressed purely in generalized-permutahedron or collision-coordinate language. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Nathaniel Bottman and Daria Poliakova, *Constrainahedra*, arXiv:2208.14529, first public version 2022-08-30.
2. Frédéric Chapoton and Vincent Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first public version 2022-01-18; Annales Henri Lebesgue 7 (2024), 1535--1601, DOI 10.5802/ahl.225.
