# A unique balancing reversal for Euler characteristics of complete-intersection surfaces
## Finding
Fix integers \(c\ge2\) and \(S\ge2c\). Let
\[
X_{\mathbf d}\subset\mathbb P^{c+2}_{\mathbb C}
\]
be a smooth complete-intersection surface of multidegree
\[
\mathbf d=(d_1,\ldots,d_c),\qquad d_i\ge2,\qquad \sum_i d_i=S.
\]
Put
\[
x_i=d_i-1,\qquad T=S-c=\sum_i x_i,
\]
and
\[
h_2(\mathbf x)=\sum_{i\le j}x_ix_j.
\]
Then
\[
\chi_{\mathrm{top}}(X_{\mathbf d})
=
\left(\prod_i d_i\right)
\left(3-2T+h_2(\mathbf x)\right).
\]

If \(c\ge3\), the Euler characteristic is uniquely maximized, up to permutation, by the most balanced multidegree, meaning that all defining degrees differ by at most one. It is uniquely minimized, up to permutation, by
\[
(2,\ldots,2,S-2c+2).
\]

For \(c=2\), the same conclusion holds except at the single fixed-sum level \(S=6\). There,
\[
\chi_{\mathrm{top}}(X_{2,4})=64
\quad\text{and}\quad
\chi_{\mathrm{top}}(X_{3,3})=63,
\]
so the unbalanced bidegree \((2,4)\) uniquely maximizes while the balanced bidegree \((3,3)\) uniquely minimizes. For \(S=4\) and \(S=5\) there is only one unordered bidegree. For every \(S\ge7\), the balanced bidegree uniquely maximizes and \((2,S-2)\) uniquely minimizes.

By the Lefschetz hyperplane theorem, a smooth complete-intersection surface has \(b_1=b_3=0\). Hence
\[
b_2(X_{\mathbf d})=\chi_{\mathrm{top}}(X_{\mathbf d})-2,
\]
so the same extremal classification holds for the middle Betti number.

## Assumptions and scope
The ground field is \(\mathbb C\). The surface is smooth and is a complete intersection of \(c\) hypersurfaces in \(\mathbb P^{c+2}\). Every defining degree is at least two. The codimension \(c\) and the sum \(S\) of the defining degrees are fixed while the multidegree varies.

Fixing \(S\) has a direct geometric meaning because adjunction gives
\[
K_X\cong\mathcal O_X(S-c-3).
\]
Thus the theorem compares topological complexity among complete-intersection surfaces with fixed codimension and fixed canonical-polarization exponent.

## Proof
For a smooth complete intersection, the total Chern class is
\[
c(TX)=\frac{(1+H)^{c+3}}{\prod_i(1+d_iH)}.
\]
The coefficient of \(H^2\) is
\[
\binom{c+3}{2}-(c+3)\sum_i d_i+\sum_{i\le j}d_id_j.
\]
Since \(\int_XH^2=\prod_i d_i\), the topological Euler characteristic is this coefficient multiplied by \(\prod_i d_i\). After writing \(d_i=x_i+1\) and \(T=\sum_i x_i\), the coefficient simplifies to
\[
3-2T+h_2(\mathbf x),
\]
proving the displayed formula.

Now take two shifted degrees with
\[
x<y-1
\]
and balance them by
\[
(x,y)\longmapsto(x+1,y-1).
\]
Set
\[
\delta=y-x-1>0,
\qquad
B=(x+1)(y+1),
\qquad
C=3-2T+h_2(\mathbf x).
\]
The pair contribution to the degree product changes from \(B\) to \(B+\delta\), while the fixed-sum identity
\[
h_2(\mathbf x)=\frac{T^2+\sum_i x_i^2}{2}
\]
shows that \(h_2\), and therefore \(C\), changes from \(C\) to \(C-\delta\). If \(P\) denotes the product of all untouched degree factors, then
\[
\chi_{\mathrm{top}}(\text{balanced})-
\chi_{\mathrm{top}}(\text{original})
=P\delta(C-B-\delta).
\]

First suppose \(c=2\). Direct simplification gives
\[
C-B-\delta
=x^2+y^2-2x-4y+3
=(x-1)^2+(y-2)^2-2.
\]
Under \(x\ge1\) and \(y\ge x+2\), this expression is negative exactly for
\[
(x,y)=(1,3),
\]
where it equals \(-1\); it is positive for every other admissible balancing move. This exceptional pair corresponds exactly to the degree move
\[
(2,4)\longmapsto(3,3),
\]
and direct substitution gives \(64\mapsto63\). Hence \(S=6\) is the unique balancing reversal. At every other fixed sum admitting more than one bidegree, repeated balancing strictly increases the Euler characteristic and repeated unbalancing strictly decreases it.

Now suppose \(c\ge3\), and let the remaining shifted degrees be \(z_1,\ldots,z_{c-2}\). Write
\[
R=\sum_j z_j,
\qquad
H=h_2(z_1,\ldots,z_{c-2}).
\]
Then
\[
C-B-\delta
=
(x-1)^2+(y-2)^2-2+(x+y-2)R+H.
\]
The first three terms are at least \(-1\). Because at least one \(z_j\ge1\), while \(x+y\ge4\), one has
\[
(x+y-2)R+H\ge3.
\]
Therefore
\[
C-B-\delta\ge2>0.
\]
Every nontrivial balancing move strictly increases \(\chi_{\mathrm{top}}\).

Repeated balancing terminates at the unique multiset whose entries differ by at most one, proving the unique maximum. Conversely, unless the shifted multidegree is already
\[
(1,\ldots,1,T-c+1),
\]
one may transfer one unit from a nonminimal entry to a largest entry. This is the reverse of an admissible balancing move and strictly decreases the Euler characteristic. Iteration reaches the displayed one-heavy tuple, proving the unique minimum.

## Verification
The bundled exact-integer checker evaluates the Euler characteristic in two independent algebraic forms: directly from the coefficient of \(H^2\) in the Chern-class expression and from the shifted-degree formula above. It exhaustively checks all unordered multidegrees for \(2\le c\le7\) and \(2c\le S\le2c+18\), verifies every predicted maximizer and minimizer, and checks every admissible balancing move in those families.

The finite replay is regression evidence only. The infinite theorem follows from the symbolic balancing identity and the uniform lower bound in the proof.

## Relationship to prior work
Dessai and Wiemeler record the standard cohomological and Chern-class formulas for smooth complete intersections, including
\[
c(X)=(1+x)^{n+r+1}\prod_j(1+d_jx)^{-1},
\]
and note that the Euler characteristic is the top Chern number. Their paper is classified primarily under MSC \(14\mathrm{M}10\). Navarro Aznar gives a classical proof of the same complete-intersection Chern-class framework and an Euler-characteristic formula for nonsingular complete intersections.

The claim-specific literature and semantic-index searches compared fixed-sum Euler characteristic, middle Betti number, Chern-number, and balancing formulations. They located formulas and other extremal complete-intersection questions, but no theorem giving the fixed-\(S\) maximum/minimum classification above or the unique reversal at \((2,4)\leftrightarrow(3,3)\). The closest checked local findings concern Euclidean-distance degree at fixed adjunction level and signature for codimension-two surfaces; neither invariant determines the Euler characteristic range proved here.

## Limitations
The theorem concerns smooth complex complete-intersection surfaces with all defining degrees at least two. It does not address singular complete intersections, weighted projective ambient spaces, or comparisons in which codimension is allowed to vary.

The originality search cannot exclude an unindexed older source that extracts the same balancing consequence from the classical Chern-number formula. In particular, older papers on extremal Euler-Poincare characteristics study related but differently constrained questions.

## References
Anand Dessai and Michael Wiemeler, *Complete Intersections with S^1-action*, arXiv:1108.5327, first submitted 26 August 2011; later published in *Transformation Groups* 22 (2017), 295--320.

Vicente Navarro Aznar, *On the Chern Classes and the Euler Characteristic for Nonsingular Complete Intersections*, *Proceedings of the American Mathematical Society* 78 (1980), 143--148.
