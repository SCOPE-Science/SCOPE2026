# Two-lineup products of two simplices have an exact all-vertex minimum sphere
## Finding
Let
\[
d,e\ge2
\]
and let
\[
A_{d,e}
=
\left\{
a_{ij}=\mathbf e_i\oplus\mathbf f_j:
1\le i\le d,\ 1\le j\le e
\right\}
\subset
\mathbb R^d\oplus\mathbb R^e
\tag{1}
\]
be the standard vertex configuration of
\[
\Delta_{d-1}\times\Delta_{e-1}.
\]
Fix lineup weights
\[
1>\alpha>\beta>0,
\qquad
\alpha+\beta=1.
\tag{2}
\]
Write
\[
L_{d,e}^{(2)}
=
L_{2,(\alpha,\beta)}(A_{d,e})
\tag{3}
\]
for the corresponding two-lineup polytope in the sense of Castillo and Labbé.

Its unique minimum enclosing Euclidean sphere has center
\[
\boxed{
c
=
\frac1d\sum_{i=1}^d\mathbf e_i
\oplus
\frac1e\sum_{j=1}^e\mathbf f_j
}
\tag{4}
\]
and radius
\[
\boxed{
R
=
\sqrt{
1+\alpha^2+\beta^2-\frac1d-\frac1e
}.
}
\tag{5}
\]

Every vertex of the lineup polytope lies on this sphere.

In fact, the vertices have a complete elementary classification. They are exactly
\[
\mathbf e_i
\oplus
\left(
\alpha\mathbf f_j+\beta\mathbf f_{j'}
\right),
\qquad
j\ne j',
\tag{6}
\]
and
\[
\left(
\alpha\mathbf e_i+\beta\mathbf e_{i'}
\right)
\oplus
\mathbf f_j,
\qquad
i\ne i'.
\tag{7}
\]
Hence
\[
L_{d,e}^{(2)}
\]
has exactly
\[
de(d+e-2)
\tag{8}
\]
vertices, and all of them are contact points of its minimum enclosing sphere.

There is a sparse positive contact certificate. Choose any cyclic ordering of the \(e\) column indices and let \(j^+\) denote the successor of \(j\). The \(de\) vertices
\[
u_{ij}
=
\mathbf e_i
\oplus
\left(
\alpha\mathbf f_j+\beta\mathbf f_{j^+}
\right)
\tag{9}
\]
satisfy
\[
\boxed{
c
=
\frac1{de}
\sum_{i=1}^d\sum_{j=1}^e u_{ij}.
}
\tag{10}
\]
Thus only \(de\) of the \(de(d+e-2)\) contact vertices are needed to certify optimality and uniqueness of the sphere.

## Assumptions and scope
The simplices are the standard simplices with orthonormal coordinate bases
\[
\mathbf e_1,\ldots,\mathbf e_d
\quad\text{and}\quad
\mathbf f_1,\ldots,\mathbf f_e.
\]
The Euclidean metric is the direct-sum metric on
\[
\mathbb R^d\oplus\mathbb R^e.
\]

The lineup weights satisfy the source convention for length two:
\[
1>\alpha>\beta>0,
\qquad
\alpha+\beta=1.
\]
The theorem concerns the two-lineup polytope, not the full sweep polytope and not lineup lengths greater than two.

The result is realization-sensitive. Arbitrary affine images of the product of simplices do not preserve the radius in (5).

## Proof
A linear functional on the product of the two standard simplices has additive vertex values
\[
\lambda(a_{ij})=p_i+q_j
\tag{11}
\]
for some row scores \(p_i\) and column scores \(q_j\).

Assume the scores are generic. Let \(i\) be the unique index maximizing the row scores and let \(j\) be the unique index maximizing the column scores. Then
\[
a_{ij}
\]
is the unique top vertex.

Let \(i'\) be the index of the second-largest row score and let \(j'\) be the index of the second-largest column score. Any vertex
\[
a_{rs}
\]
with both
\[
r\ne i
\quad\text{and}\quad
s\ne j
\]
satisfies
\[
p_r+q_s
<
p_{i'}+q_j
\]
and
\[
p_r+q_s
<
p_i+q_{j'}.
\]
Therefore the second vertex in a two-lineup is necessarily one of
\[
a_{i'j}
\quad\text{or}\quad
a_{ij'}.
\tag{12}
\]
So the first two vertices always share a row or a column.

Conversely, every ordered pair sharing a row or a column is realizable as the top two vertices of an additive functional. For example, to realize
\[
(a_{ij},a_{ij'})
\]
with \(j\ne j'\), choose \(p_i\) strictly larger than all other row scores by a sufficiently large gap, choose \(q_j\) largest and \(q_{j'}\) second largest, and make all remaining scores generic below them. The column-sharing case is symmetric.

The source proves that an occupation vector is a vertex of the lineup polytope if and only if its ordered list is an actual lineup. Since the occupation vector of
\[
(a_{ij},a_{ij'})
\]
is
\[
\alpha a_{ij}+\beta a_{ij'}
=
\mathbf e_i
\oplus
\left(
\alpha\mathbf f_j+\beta\mathbf f_{j'}
\right),
\]
and similarly for a column-sharing pair, this proves the classification (6)--(7). Distinct ordered pairs give distinct occupation vectors because
\[
\alpha\ne\beta.
\]
The count (8) follows.

Every vector in (6) or (7) has squared norm
\[
1+\alpha^2+\beta^2.
\tag{13}
\]
Every such vector also has row-block coordinate sum \(1\) and column-block coordinate sum \(1\). Hence its scalar product with (4) is
\[
\frac1d+\frac1e,
\tag{14}
\]
while
\[
\|c\|^2=\frac1d+\frac1e.
\tag{15}
\]
For every lineup-polytope vertex \(v\),
\[
\|v-c\|^2
=
1+\alpha^2+\beta^2
-
\frac1d
-
\frac1e.
\tag{16}
\]
Thus all vertices lie on the sphere (4)--(5).

It remains to prove that this common vertex sphere is the minimum enclosing sphere.

Every ordered same-row pair used in (9) is realizable by the preceding construction, so every \(u_{ij}\) is a lineup-polytope vertex. Fix a row coordinate \(i\). It occurs in each of the \(e\) vertices
\[
u_{i1},\ldots,u_{ie}
\]
with coefficient \(1\). After averaging all \(de\) certificate vertices, its coefficient is therefore
\[
\frac1d.
\]
Fix a column coordinate \(j\). In each row, it occurs once with coefficient \(\alpha\) and once with coefficient \(\beta\). Since
\[
\alpha+\beta=1,
\]
its average coefficient is
\[
\frac1e.
\]
This proves the barycentric identity (10).

For any candidate center \(q\), averaging squared distances over the certificate vertices gives
\[
\frac1{de}
\sum_{i,j}
\|u_{ij}-q\|^2
=
R^2+\|q-c\|^2.
\tag{17}
\]
Therefore
\[
\max_{i,j}\|u_{ij}-q\|^2
\ge
R^2+\|q-c\|^2.
\tag{18}
\]
At \(q=c\), every vertex of the entire lineup polytope is at distance \(R\). If
\[
q\ne c,
\]
one of the certificate vertices has distance strictly larger than \(R\). Consequently no smaller enclosing ball exists and no other center achieves radius \(R\). This proves (4)--(5) and uniqueness.

## Verification
The proof is symbolic and applies to every
\[
d,e\ge2
\]
and every admissible pair of lineup weights.

The source-dependent premises were checked in the full primary text: the definition of lineup and occupation vector, the characterization of lineup-polytope vertices by realizable lineups, and the additive-tableau description for products of two simplices.

The accompanying `verify.py` uses exact rational arithmetic for all
\[
2\le d,e\le8
\]
and several distinct admissible rational weight pairs. It enumerates the classified lineup vertices, verifies the count (8), the common squared radius (16), the cyclic barycentric certificate (10), and explicit additive-score witnesses for every ordered row-sharing and column-sharing pair. These finite checks are corroborative only.

## Relationship to prior work
Castillo and Labbé develop lineup polytopes of products of simplices as a polyhedral tool for quantum marginal problems. Their paper gives algorithms for lineups and facets, studies realizable tableaux, treats products of two and three simplices, and develops special symmetry for cubes. It does not state a Euclidean circumradius, minimum-enclosing-sphere theorem, or all-vertex cosphericity theorem.

The earlier work introducing lineup polytopes arose from convex one-body representability for fermionic and bosonic systems. It supplies the general occupation-vector framework but does not provide the product-of-two-simplices metric theorem stated here.

The present result uses the special rank-two feature of additive score tables: after the largest entry, the second-largest entry must share its row or column. This collapses the full two-lineup vertex set to the two families (6)--(7), and the equal norm of those two families is what makes complete cosphericity possible.

Targeted literature and published-result searches under “lineup polytope”, “product of two simplices”, “occupation vector”, “circumsphere”, “circumradius”, “minimum enclosing sphere”, and “Chebyshev center” did not locate a theorem implying (4)--(10).

## Limitations
The theorem is specific to lineup length two. For longer lineups, different overlap patterns can produce occupation vectors with different squared norms, so the all-vertex cosphericity argument does not automatically extend.

The formula depends on the standard orthogonal simplex realization and therefore is not affine invariant.

The result determines the minimum enclosing sphere but not the inradius, John ellipsoid, or complete pairwise vertex-distance spectrum.

The classification of two-lineups is short once additive scores are written down, so an equivalent folklore observation may exist without lineup-polytope terminology. The positive contact certificate and the exact minimum-enclosing conclusion reduce, but do not eliminate, that residual originality risk.

## References
1. Federico Castillo and Jean-Philippe Labbé, *Lineup polytopes of products of simplices*, arXiv:2306.00082, first public version 2023-05-31; Annales de l'Institut Henri Poincaré D 12 (2025), 787--818, DOI 10.4171/AIHPD/202.
2. Federico Castillo, Jean-Philippe Labbé, Julia Liebert, Arnau Padrol, Eva Philippe, and Christian Schilling, *An effective solution to convex one-body N-representability*, arXiv:2105.06459, first public version 2021-05-13.
