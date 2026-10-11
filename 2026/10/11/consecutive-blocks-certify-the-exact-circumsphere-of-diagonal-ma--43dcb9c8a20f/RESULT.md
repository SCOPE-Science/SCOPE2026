# Consecutive blocks certify the exact circumsphere of diagonal matching-field polytopes
## Finding
Let
\[
2\le k<n,
\qquad
m=n-k+1,
\]
and let
\[
P_{\mathcal D(k,n)}\subset\mathbb R^{k\times n}
\]
be the diagonal matching-field polytope in the standard matching-field coordinates.

The source identifies this polytope with the Grassmannian Gelfand--Tsetlin polytope through an explicit unimodular equivalence. Its vertices are
\[
v_I
=
e_{1,j_1}+\cdots+e_{k,j_k},
\qquad
I=\{j_1<\cdots<j_k\}\subset[n].
\tag{1}
\]

Define the active band
\[
B=
\left\{
(i,j):
1\le i\le k,\ 
i\le j\le i+n-k
\right\}.
\tag{2}
\]
Put
\[
\boxed{
c=
\frac1m
\sum_{(i,j)\in B}e_{i,j}.
}
\tag{3}
\]
Then \(c\) is the unique center of the minimum enclosing Euclidean sphere of \(P_{\mathcal D(k,n)}\), and
\[
\boxed{
R\bigl(P_{\mathcal D(k,n)}\bigr)
=
\sqrt{\frac{k(n-k)}{n-k+1}}.
}
\tag{4}
\]

Every vertex in (1) is a contact point of this sphere.

More sharply, the \(m\) consecutive-block vertices
\[
v_s
=
\sum_{i=1}^k e_{i,s+i},
\qquad
0\le s\le n-k,
\tag{5}
\]
already certify optimality, because
\[
\boxed{
c=\frac1m\sum_{s=0}^{m-1}v_s.
}
\tag{6}
\]
Thus an equal-weight certificate of only \(n-k+1\) contact vertices proves the exact minimum enclosing sphere, even though the polytope has \(\binom nk\) vertices.

## Assumptions and scope
The metric is the standard Euclidean metric for which the matrix-coordinate vectors
\[
e_{i,j}
\]
are orthonormal.

The theorem concerns the diagonal matching-field realization itself. Although the source proves that this realization is unimodularly equivalent to the usual Grassmannian order-polytope model of the Gelfand--Tsetlin polytope, unimodular maps need not be orthogonal, so formula (4) is not asserted for arbitrary unimodular or affine realizations.

The range \(2\le k<n\) isolates the nontrivial Grassmannian cases. The same argument also specializes to \(k=1\), where the polytope is a regular simplex.

## Proof
For
\[
I=\{j_1<\cdots<j_k\}\subset[n],
\]
the source gives the diagonal matching-field vertex (1).

Because the \(j_i\) are strictly increasing,
\[
i\le j_i\le n-k+i.
\tag{7}
\]
Hence all coordinates outside the band \(B\) vanish on the polytope. In each row \(i\), every vertex has exactly one coordinate equal to \(1\), so
\[
\sum_{j=i}^{i+n-k}x_{i,j}=1
\qquad
(1\le i\le k).
\tag{8}
\]

Let
\[
A=
\left\{
x:
x_{i,j}=0\text{ outside }B,\ 
\sum_{j=i}^{i+n-k}x_{i,j}=1
\text{ for every }i
\right\}.
\tag{9}
\]
There are \(m\) active coordinates in each row, so
\[
\dim A=k(m-1)=k(n-k).
\tag{10}
\]

The source proves that \(P_{\mathcal D(k,n)}\) is affinely isomorphic to the order polytope of the Grassmannian poset
\[
Q_{k,n}=[k]\times[n-k],
\]
which is full-dimensional in \(\mathbb R^{k(n-k)}\). Therefore
\[
\dim P_{\mathcal D(k,n)}=k(n-k).
\tag{11}
\]
Since the polytope lies in \(A\), equations (10)--(11) imply
\[
\operatorname{aff}P_{\mathcal D(k,n)}=A.
\tag{12}
\]

The point of \(A\) nearest the origin is obtained by distributing each row sum uniformly among its \(m\) active coordinates. This is exactly \(c\) in (3). Thus
\[
\|c\|^2=\frac{k}{m}.
\tag{13}
\]

Every vertex \(v_I\) has exactly \(k\) unit coordinates, so
\[
\|v_I\|^2=k.
\tag{14}
\]
Each of those \(k\) coordinates lies in the active band, hence
\[
\langle v_I,c\rangle=\frac{k}{m}.
\tag{15}
\]
Combining (13)--(15),
\[
\|v_I-c\|^2
=
k-\frac{k}{m}
=
\frac{k(m-1)}m
=
\frac{k(n-k)}{n-k+1}.
\tag{16}
\]
So all \(\binom nk\) vertices lie on the sphere (3)--(4).

It remains to prove that this common vertex sphere is the minimum enclosing sphere.

For
\[
0\le s\le m-1,
\]
the consecutive set
\[
I_s=\{s+1,s+2,\ldots,s+k\}
\]
is a \(k\)-subset of \([n]\), and its diagonal matching-field vertex is \(v_s\) from (5).

Fix an active coordinate \((i,j)\in B\). There is exactly one value
\[
s=j-i
\]
in \(\{0,\ldots,m-1\}\) for which \(v_s\) contains \(e_{i,j}\). Hence every active coordinate appears exactly once among \(v_0,\ldots,v_{m-1}\). This proves the barycentric identity (6).

For any point \(q\in\mathbb R^{k\times n}\), use (6) and the fact that every \(v_s\) lies at distance \(R\) from \(c\):
\[
\frac1m\sum_{s=0}^{m-1}\|v_s-q\|^2
=
R^2+\|q-c\|^2.
\tag{17}
\]
Therefore
\[
\max_s\|v_s-q\|^2
\ge
R^2+\|q-c\|^2.
\tag{18}
\]
At \(q=c\), every vertex of the full polytope is at distance \(R\). If \(q\ne c\), equation (18) shows that one of the consecutive-block vertices already lies at distance strictly larger than \(R\). Thus no other center can achieve radius \(R\), and no smaller enclosing sphere exists.

This proves the exact radius, uniqueness of the center, and the all-vertex contact statement.

## Verification
The proof is exact for all \(2\le k<n\).

The source-dependent facts were checked in the full primary text: the diagonal matching field sends every \(k\)-subset to the identity permutation; its vertices are exactly the vectors in (1); Theorem 2.15 identifies the Grassmannian order polytope with \(P_{\mathcal D(k,n)}\); and the displayed unimodular map shows the active row coordinates explicitly.

The accompanying `verify.py` checks every pair
\[
2\le k<n\le10.
\]
It enumerates all \(\binom nk\) vertices, verifies the active-band affine dimension by exact rational row reduction, checks the common squared radius in (16), and verifies the consecutive-block barycentric identity (6). These finite checks are corroborative only.

## Relationship to prior work
Clarke, Higashitani, and Mohammadi prove that the Grassmannian Gelfand--Tsetlin polytope is realized as the diagonal matching-field polytope and use that realization as the base point of mutation families leading to FFLV and block-diagonal matching-field polytopes. Their results concern lattice equivalence, toric degenerations, Newton--Okounkov bodies, and combinatorial mutations.

Earlier matching-field work introduced matching-field polytopes and studied toric degenerations of Grassmannians. That literature provides the ambient exponent-vector construction but does not state the Euclidean minimum enclosing sphere of the diagonal realization.

The usual Grassmannian Gelfand--Tsetlin order polytope is unimodularly equivalent to the present realization, but this does not transfer Euclidean radii. The exact sphere in (3)--(4) is therefore a metric fact about the native matching-field coordinates, not a consequence of lattice equivalence alone.

Targeted published-result and literature searches under “diagonal matching field polytope”, “Gelfand--Tsetlin polytope”, “circumsphere”, “circumradius”, “minimum enclosing sphere”, “row sums”, and “consecutive blocks” did not locate a theorem implying (3)--(6).

## Limitations
The theorem is specific to the diagonal matching-field realization and its standard orthonormal coordinate metric.

Combinatorial mutations and unimodular equivalences preserve important lattice data but generally do not preserve Euclidean circumspheres, so no radius statement is made for the FFLV or intermediate mutation polytopes.

The result determines the minimum enclosing sphere but not the inradius, John ellipsoid, or full pairwise vertex-distance spectrum.

The all-vertex cosphericity follows quickly once the exact affine hull is recognized. The mathematically stronger part is the explicit \(n-k+1\)-vertex positive contact certificate proving that the common sphere is genuinely minimum enclosing and uniquely centered. An equivalent observation could exist in the toric-degeneration literature under different metric language; search nonappearance is not treated as a formal novelty certificate.

## References
1. Oliver Clarke, Akihiro Higashitani, and Fatemeh Mohammadi, *Combinatorial Mutations of Gelfand--Tsetlin Polytopes, Feigin--Fourier--Littelmann--Vinberg Polytopes, and Block Diagonal Matching Field Polytopes*, arXiv:2208.04521, first public version 2022-08-09; Journal of Pure and Applied Algebra 228 (2024), 107637, DOI 10.1016/j.jpaa.2024.107637.
2. Fatemeh Mohammadi and Kristin Shaw, *Toric degenerations of Grassmannians from matching fields*, arXiv:1809.01026, first public version 2018-09-04; Algebraic Combinatorics 2 (2019), 1109--1124, DOI 10.5802/alco.77.
