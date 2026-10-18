# Sharp tetrahedral volume and optimizer partition in cubic signed permutahedra

## Finding

For every real parameter \(q>0\), define the full-dimensional convex polytope
\[
P_q=\operatorname{conv}\{(\varepsilon_1 a_{\pi(1)},\varepsilon_2 a_{\pi(2)},\varepsilon_3 a_{\pi(3)}):\pi\in S_3,\ \varepsilon_i\in\{-1,1\}\},\qquad(a_1,a_2,a_3)=(1,1+q,1+2q).
\]
Among **all** Euclidean tetrahedra contained in \(P_q\), allowing arbitrary interior or boundary corners, the exact maximum volume is
\[
M(q)=\frac83(1+q)(1+2q+2q^2).
\]
There are **exactly twelve** maximizing tetrahedra, forming a single orbit under signed coordinate permutations. They are all vertex-supported, their four-element vertex sets are pairwise disjoint, and together these twelve sets partition all 48 vertices of \(P_q\). A representative maximizer has vertices
\[
(-c,-b,-a),\quad(-a,b,c),\quad(a,b,-c),\quad(c,-b,a),
\qquad a=1,\ b=1+q,\ c=1+2q.
\]
It is a disphenoid with four squared edge lengths \(8+16q+12q^2\) and two opposite squared edge lengths \(8+16q+16q^2\).

The volume of the containing polytope is
\[
\operatorname{Vol}_3(P_q)=8+48q+84q^2+32q^3.
\]
Consequently its sharp tetrahedral occupancy ratio is
\[
\rho(q)=\frac{2(q+1)(2q^2+2q+1)}{3(8q^3+21q^2+12q+2)}.
\]
The ratio has **one and only one** global minimum on \((0,\infty)\), at the unique positive root \(q_*\) of
\[
10q^4-27q^2-26q-6=0,
\qquad q_*\approx2.031134931622,
\qquad \rho(q_*)\approx0.149423253588.
\]
For \(q=\sqrt2\), the polytope is the edge-two regular truncated cuboctahedron (great rhombicuboctahedron), giving the exact maximum tetrahedral fraction
\[
\rho(\sqrt2)=\frac{1+14\sqrt2}{138}\approx0.150717317922.
\]

## Assumptions and scope

The parameter is any finite real \(q>0\). The set of vertices is the orbit of the strictly increasing positive triple \((1,1+q,1+2q)\) under the hyperoctahedral group of order 48; each listed point is an exposed vertex. “Largest” concerns unrestricted **three-dimensional Euclidean volume**, not edge length, inscribed-sphere radius, or a regularity-constrained tetrahedron. All embedded statements, including the equality classification and optimizer partition, hold for each \(q>0\). At \(q=0\) the 48-vertex description collapses to the cube; the volume formulas extend continuously, but the twelve-optimizer assertion is not made there. No statement is made in higher dimensions or for arbitrary triples of positive coordinates.

## Proof

**1. A natural Minkowski deformation and its volume.** Write \(u_{(1)}\ge u_{(2)}\ge u_{(3)}\ge0\) for the decreasing rearrangement of the absolute coordinate values of a vector \(u\in\mathbb R^3\). The rearrangement inequality gives the support function
\[
h_{P_q}(u)=\sum_{i=1}^3|u_i|+q(2u_{(1)}+u_{(2)}).
\]
Since \(2u_{(1)}+u_{(2)}=\sum_{i<j}\max(|u_i|,|u_j|)\) and \(|s+t|+|s-t|=2\max(|s|,|t|)\), this is exactly the support function of the centered nine-generator zonotope
\[
P_q=\sum_{i=1}^3[-e_i,e_i]
+\frac q2\sum_{1\le i<j\le3}\bigl([-e_i-e_j,e_i+e_j]+[-e_i+e_j,e_i-e_j]\bigr).
\]
For a centered three-dimensional zonotope \(\sum[-g_i,g_i]\), its volume equals \(8\sum_{i<j<k}|\det(g_i,g_j,g_k)|\). Sorting the nine generators by the number \(k\in\{0,1,2,3\}\) of pair-root generators in a triple, the sums of absolute determinants *before* inserting the factors \(q/2\) are respectively \((1,12,42,32)\). Hence
\[
\operatorname{Vol}_3(P_q)=8\sum_{k=0}^{3}(1,12,42,32)_k(q/2)^k
=8+48q+84q^2+32q^3.
\]
The four finite sums are reproduced exactly by `CHECK.py`.

**2. Reduction to vertices.** Orient any nondegenerate contained tetrahedron so that its determinant is nonnegative. Holding three corners fixed, its signed determinant is affine in the fourth. Every corner can therefore be replaced by a polytope vertex without decreasing the determinant. Repeating for all four corners proves the global maximal value is attained at a quadruple of the 48 vertices.

**3. A uniform coefficientwise determinant bound.** Regard each coordinate of a vertex as an integer affine polynomial in \(q\). For any four distinct vertices, the oriented determinant is an integer polynomial \(D(q)=d_0+d_1q+d_2q^2+d_3q^3\). The signed-permutation group acts transitively on the 48 vertices and changes determinants only by a sign, so it suffices to fix the lexicographically first vertex \((-1-2q,-1-q,-1)\) and test the \(\binom{47}{3}=16215\) triples of other vertices. Exact integer coefficient arithmetic establishes, **for every such quadruple**,
\[
(|d_0|,|d_1|,|d_2|,|d_3|)\le(16,48,64,32)
\]
componentwise. It also establishes that exactly one anchored triple has coefficient vector \(\pm(16,48,64,32)\), namely the three other corners of the displayed representative. This is a finite theorem, not an inference from samples: `CHECK.py` constructs all 48 vertices, evaluates every one of the 16215 distinct anchored determinant polynomials, checks every bound over the integers, and verifies the unique equality case. Thus, for every \(q>0\),
\[
|D(q)|\le16+48q+64q^2+32q^3,
\]
and equality is possible only when every coefficient simultaneously attains its bound with a common sign. The displayed quadruple does attain it. Division by \(6\) gives \(M(q)\).

**4. Completeness and rigidity of maximizers.** The signed-coordinate-permutation orbit of the displayed quadruple has exactly twelve members. The same exact checker verifies that each of the 48 vertices occurs in exactly one of them. Since every vertex is group-equivalent to the anchored vertex and the anchored maximizing triple is unique, these are **all** vertex-supported maxima. Suppose now that an arbitrary maximizing tetrahedron has a possibly nonvertex corner \(x\). Replace its other three corners by vertices while preserving maximal volume, leaving \(x\) fixed. The resulting three vertex corners determine a linear functional on \(P_q\) whose maximum is the sharp determinant. Two distinct vertices could maximize that functional only if two distinct vertex-supported maximizing tetrahedra shared those three vertices. The twelve maximizing sets are disjoint, so the exposed maximizing face is a singleton vertex, forcing \(x\) to be that vertex. This works separately for every original corner, excluding all nonvertex maximizers. Direct subtraction of the representative coordinates gives the asserted disphenoid edge profile.

**5. The unique occupancy minimum.** Differentiating the stated rational function yields
\[
\rho'(q)=\frac{2(10q^4-27q^2-26q-6)}{3(8q^3+21q^2+12q+2)^2}.
\]
The numerator polynomial has precisely one positive root by Descartes’ rule of signs (one sign change), continuity, its negative value at zero, and its positive leading coefficient. Hence the derivative changes from negative to positive at that root and the minimum is unique and global. Substituting \(q=\sqrt2\) in the rational formula and rationalizing gives \((1+14\sqrt2)/138\).

## Verification

The standalone file `CHECK.py` requires only the Python standard library. Run `python3 CHECK.py`. It checks all 16215 anchored determinant coefficient vectors using exact integer arithmetic, the unique anchored equality configuration, the signed-permutation orbit and 48-vertex partition, the two disphenoid edge classes, and the zonotope volume coefficient sums. It printed all three `PASS` messages during the present verification. The uniform-in-\(q\) conclusion is deductive from integer coefficient bounds; no floating-point sample is used as an infinite-parameter proof. The one-variable derivative and Descartes argument are explicit above, independent of the computer check. The output is reproducible without an external dataset or package.

## Relationship to prior work

The regular truncated cuboctahedron has classical coordinate and volume descriptions, and the 2015 self-dated analysis of the great rhombicuboctahedron by Rajpoot computes several ambient-body metric quantities. Neither the inspected portions nor a full-text search of that study yielded an extremal contained tetrahedron. Horváth and Lángi (arXiv:1402.6496, first posted 2014-02-26) study maximum-volume polyhedra with prescribed vertex counts on a sphere; their optimization varies the containing configuration rather than fixing this signed-permutahedral family. Di Summa, Eisenbrand, Faenza and Moldenhauer (arXiv:1406.3512, first posted 2014-06-13) analyze algorithms and complexity for largest simplices in arbitrary vertex-described polytopes, rather than this exact formula or equality partition. Firsching (2015, arXiv:1407.0683) computes maximal **similar copies** of one prescribed polyhedron inside another and surveys Croft's Platonic-solid pairings. Those results hold the inner solid's similarity class fixed and do not furnish an unrestricted, explicitly varying disphenoid optimum for the 48-vertex type-\(B_3\) signed permutahedron. A related published formula for tetrahedra in a cube–octahedron **intersection** family concerns different polyhedra (at most 24 vertices rather than the present 48 for \(q>0\)) and does not imply this result. Exhaustive searches for the solid's aliases, type-\(B_3\) signed permutahedra, largest tetrahedra, and volume-ratio extrema did not locate an explicit stronger treatment. These comparisons support, but do not establish, historical priority.

## Limitations

The theorem uses one natural one-parameter Minkowski deformation and should not be inferred for arbitrary type-\(B\) permutahedra or other Archimedean solids. The coefficientwise bound is a finite, completely enumerated 16215-case exact certificate; the accompanying code and its enumeration argument are part of the proof. The statement is not an independently certified result. Historical coverage in unindexed polyhedral extremum tables and inaccessible papers remains possible, and the 2015 self-date of the Rajpoot PDF is not proof of its earliest online availability. The limiting cube parameter \(q=0\) does not retain 48 distinct vertices, so the optimizer classification is expressly restricted to \(q>0\).

## References

1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496, first submitted 2014-02-26. https://arxiv.org/html/1402.6496v3
2. M. Di Summa, F. Eisenbrand, Y. Faenza and C. Moldenhauer, *On largest volume simplices and sub-determinants*, arXiv:1406.3512, first submitted 2014-06-13. https://arxiv.org/abs/1406.3512
3. H. C. Rajpoot, *Mathematical Analysis of a Great Rhombicuboctahedron*, document dated 2015-03-02; publicly reachable at https://www.rxiv.org/pdf/2602.0106v1.pdf (mirror identifier does not verify the original posting date).
4. *Truncated cuboctahedron*, standard coordinate and volume reference. https://en.wikipedia.org/wiki/Truncated_cuboctahedron
5. H. T. Croft, *On Maximal Regular Polyhedra Inscribed in a Regular Polyhedron*, Proc. London Math. Soc. (1980), DOI:10.1112/plms/s3-41.2.279 (distinct regularity restrictions; full text not inspected).
6. M. Firsching, *Computing Maximal Copies of Polyhedra Contained in a Polyhedron*, Experimental Mathematics 24 (2015), 98–105, DOI:10.1080/10586458.2014.956374; author-hosted full text https://firsching.ch/assets/pdfs/ComputingMaximalCopies.pdf .
