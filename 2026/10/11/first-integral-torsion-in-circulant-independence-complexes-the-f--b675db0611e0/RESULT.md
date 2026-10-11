# First integral torsion in circulant independence complexes: the fourteen-vertex threshold

## Finding
For an integer \(n\geq1\) and \(S\subseteq\{1,\ldots,\lfloor n/2\rfloor\}\), let \(C_n(S)\) be the simple undirected graph on \(\mathbb Z/n\mathbb Z\) in which distinct \(i,j\) are adjacent precisely when their cyclic distance \(\min((i-j)\bmod n,(j-i)\bmod n)\) belongs to \(S\). Write \(\operatorname{Ind}(C_n(S))\) for the simplicial complex of all independent vertex subsets.

**Theorem.** For every \(1\leq n\leq14\) and every step set \(S\), the reduced integral homology of \(\operatorname{Ind}(C_n(S))\) has nonzero torsion if and only if \(n=14\) and \(S\) is one of
\[
\{1,3,4\},\quad\{2,3,5\},\quad\{1,5,6\},\qquad
\{1,2,5,7\},\quad\{3,4,5,7\},\quad\{1,3,6,7\}.
\]
These are two multiplication-by-units orbits, of three step sets each. The first consists of six-regular graphs and the second of seven-regular graphs, so they are exactly two graph-isomorphism types among the six presentations. In each exceptional case,
\[
\widetilde H_1(\operatorname{Ind}(C_{14}(S));\mathbb Z)
\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z,
\]
and every other reduced integral homology group vanishes. Moreover, **every exceptional independence complex is homotopy equivalent to the Klein bottle**.

The pure representative \(\operatorname{Ind}(C_{14}(\{1,2,5,7\}))\) is simplicially isomorphic to the previously published Datta--Upadhyay Klein-bottle triangulation \(Q_{7,2}\); its Klein-bottle topology is not claimed as new. The other representative, \(\operatorname{Ind}(C_{14}(\{1,3,4\}))\), is nonpure and has an explicit fourteen-step elementary simplicial collapse to a triangulated Klein bottle. The new contribution is the sharp first-order classification for circulant independence complexes, including the nonpure exceptional orbit and its collapse.

## Assumptions and scope
Circulants here are labeled by the fixed cyclic vertex set; equality of step sets refers to these cyclic labels. All graph edges are undirected, loops excluded, and adjacency uses distances at most \(\lfloor n/2\rfloor\). The result concerns **all** these graphs through order fourteen, including disconnected graphs and the empty-step graph, not all flag complexes or all finite graphs. The stated isomorphism-type count concerns only the six torsion-positive cases.

## Proof
**1. Exhaustive connected reduction.** If \(S=\varnothing\), the independence complex is a simplex and is contractible. For nonempty \(S\), put \(d=\gcd(n,s:s\in S)\). The graph has exactly \(d\) connected components, each isomorphic to \(C_{n/d}(S/d)\). Its independence complex is the join of those \(d\) component independence complexes. If \(d>1\) and \(n\leq14\), each component has at most seven vertices. The calculation below proves all circulant complexes through order seven have torsion-free integral homology; the reduced join Künneth formula then proves the same for disconnected graphs through fourteen. Graphs of order one or two also have torsion-free homology directly.

It therefore suffices to check all connected nonempty-step circulants for \(3\leq n\leq14\), characterized by \(\gcd(n,s:s\in S)=1\). The numbers of these step-set presentations at successive orders three through fourteen are
\[
(1,2,3,5,7,12,14,27,31,54,63,119),
\]
for a total of **338**. Every subset of the \(\lfloor n/2\rfloor\) admissible distances is generated once. An independent-face enumeration recursively adds increasing vertices only when no previously chosen vertex is adjacent, therefore generates every face exactly once.

**2. Exact integral chain test.** Orient each face by its increasing vertex order. For each \(k\geq1\), form the integer boundary on \(k\)-element faces
\[
\partial_{k-1}[v_0,\ldots,v_{k-1}]
=\sum_{j=0}^{k-1}(-1)^j[v_0,\ldots,\widehat v_j,\ldots,v_{k-1}].
\]
Using exact Smith normal form on every positive-dimensional boundary matrix, the complete census finds a nonunit invariant factor **only** for the six indicated fourteen-vertex step sets. In each case the boundary from triangles to edges has exactly one nonunit factor, equal to \(2\); no other boundary of any of the 338 complexes has a nonunit factor.

To see why these tests are decisive, for each \(i\geq0\), the natural map from \(C_i/\operatorname{im}\partial_{i+1}\) to \(\operatorname{im}\partial_i\) has kernel \(H_i\); its target is a subgroup of a free abelian chain group and hence torsion-free. Therefore the torsion of \(H_i\) is exactly the torsion of the cokernel of \(\partial_{i+1}\), which is read from nonunit Smith factors. The augmentation in degree zero has torsion-free image, and \(\widetilde H_0\) is always free. Thus the all-orders conclusion, including torsion absence for the connected cases, follows from the exact census rather than from finite-field tests.

The representatives have face vectors and integer boundary ranks, respectively,
\[
\begin{aligned}
S=\{1,3,4\}:&\quad (14,49,42,7),\quad (13,35,7),\\
S=\{1,2,5,7\}:&\quad (14,42,28),\quad (13,28).
\end{aligned}
\]
Their reduced rational Betti numbers are \(\widetilde\beta_1=1\) and zero in all other degrees. The sole nonunit Smith factor yields exactly \(\mathbb Z/2\mathbb Z\) in degree one, proving the integral homology assertion.

**3. The surface models.** For \(S=\{1,2,5,7\}\), the complex is two-dimensional with \(14\) vertices, \(42\) edges, and \(28\) triangles. Every edge belongs to two triangles and the link of every vertex is a single six-cycle. Its geometric realization is therefore a connected closed surface of Euler characteristic \(14-42+28=0\). Propagating oriented triangle signs across shared edges gives an explicit inconsistency (verified independently from the chain calculation), so the surface is nonorientable, hence a Klein bottle.

More precisely, the \(Q_{7,2}\) triangles published by Datta and Upadhyay are \(\{i,i+1,i+2\}\) and \(\{i,i+2,i+8\}\) for all \(i\in\mathbb Z/14\mathbb Z\). Multiplication of all labels by \(3\) modulo fourteen sends this entire list of triangles exactly to the facets of \(\operatorname{Ind}(C_{14}(\{1,2,5,7\}))\), giving a direct simplicial isomorphism. This identifies a portion of the theorem already covered by that earlier work.

For \(S=\{1,3,4\}\), the original complex has \(7\) tetrahedra. The certificate `surface_certificate.json` specifies, in order, **seven free triangle/tetrahedron pairs and seven subsequent free edge/triangle pairs**. Every pair is verified to be free at the moment of removal; deleting these fourteen pairs produces a two-dimensional complex with the same \((14,42,28)\) face vector. Every remaining edge has two incident triangles, every vertex link is one cycle, the realization is connected, and orientability propagation gives a contradiction. Its Euler characteristic is zero; by the classification of closed surfaces it is a Klein bottle. Every elementary collapse preserves homotopy type.

**4. The six cases.** The units \(U(14)=\{1,3,5,9,11,13\}\) act on step sets by multiplying every step and reducing to undirected cyclic distance. Applied to \(\{1,3,4\}\), the orbit is \(\{1,3,4\},\{1,5,6\},\{2,3,5\}\). Applied to \(\{1,2,5,7\}\), the orbit is \(\{1,2,5,7\},\{1,3,6,7\},\{3,4,5,7\}\). Each multiplier defines a graph isomorphism. The representatives have different valences, six and seven, so no isomorphism joins the two orbits.

## Verification
The executable `verify_census.py` uses integer Smith normal form over \(\mathbb Z\) and re-enumerates the entire connected census, comparing its complete records against `census.json`. The standalone `verify_surface.py` instead enumerates independent sets by direct combinations, checks each free-face collapse in `surface_certificate.json`, verifies surface vertex links, detects the nonorientability obstruction, checks the two unit orbits, and verifies the published \(Q_{7,2}\) triangle identification. Both programs were run successfully from the embedded files with Python 3 and SymPy; they perform different checks and do not rely on finite-field heuristics.

Reproduce with `python verify_census.py census.json` and `python verify_surface.py surface_certificate.json`. Both commands require the files in this package; the former requires SymPy and the latter requires only the Python standard library.

## Relationship to prior work
Datta and Upadhyay (2004), Example 6 and Theorem 6, explicitly construct and classify the weakly regular fourteen-vertex Klein-bottle triangulation \(Q_{7,2}\). Under the direct label multiplication above, their published complex **is** the seven-regular representative; hence that individual homotopy identification and its torsion are not new. The sharp absence of circulant torsion below fourteen, complete six-step-set classification at fourteen, and elementary collapse for the distinct six-regular nonpure type are additional statements not implied by their manifold classification.

Adamaszek (2012) determines torsion constraints for all flag complexes up to twelve vertices. That stronger-in-class result applies below thirteen but does not settle the two circulant orders thirteen and fourteen or classify the six exceptional step sets. Earl, Vander Meulen and Van Tuyl (2015) tabulate well-covered circulants through sixteen vertices; their table names \(C_{14}(\{1,2,5,7\})\) and classifies its Buchsbaum/Cohen--Macaulay properties, not the exact integral torsion threshold for **all** circulants or the nonpure six-regular orbit. The published table is therefore acknowledged as partial coverage, not treated as evidence of novelty for that graph.

## Limitations
The classification stops at graph order fourteen. It neither asserts that every circulant with more vertices is torsion-free nor extends to noncirculant graphs. The six step sets are presentations relative to a fixed cyclic labeling; their groupings into two graph isomorphism types are established only for the exceptional set. Full homotopy type is shown for those six complexes, not for the remaining 332 connected cases. Priority over unavailable or unindexed literature cannot be certified from search nonretrieval.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433 (first posted 2004-03-25), especially Example 6 and Theorem 6. https://arxiv.org/abs/math/0403433
2. M. Adamaszek, *Small Flag Complexes with Torsion*, arXiv:1208.3892 (first posted 2012-08-19). https://arxiv.org/abs/1208.3892
3. J. Earl, K. N. Vander Meulen and A. Van Tuyl, *Independence Complexes of Well-Covered Circulant Graphs*, arXiv:1505.02837 (first posted 2015-05-11), especially Table 1. https://arxiv.org/abs/1505.02837
