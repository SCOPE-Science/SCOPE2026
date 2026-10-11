# The largest simplex in every five-dimensional simplex-generated zonotope

## Finding

For every nondegenerate simplex \(\Delta=\operatorname{conv}\{a_0,\ldots,a_5\}\subset\mathbb R^5\) with \(\sum_{i=0}^5 a_i=0\), let
\[
Z_\Delta=\sum_{i=0}^5[0,a_i].
\]
Every five-dimensional simplex \(T\subseteq Z_\Delta\) satisfies the **sharp volume inequality**
\[
\operatorname{vol}_5(T)\le\frac1{40}\operatorname{vol}_5(Z_\Delta).
\]
There are **exactly \(30\) maximizing simplices**, with no additional maximizers whose vertices lie in the relative interiors of positive-dimensional faces. Their vertices are given by the following intrinsic classification. Partition the labels \(\{0,1,2,3,4,5\}\) into three unordered pairs \(P_0,P_1,P_2\); choose one of the two cyclic orientations of these three pairs. For each ordered successor relation \(P_i\to P_j\), take the two triple sums
\[
z_{P_i\cup\{q\}}=\sum_{\nu\in P_i\cup\{q\}}a_\nu,\qquad q\in P_j.
\]
The six sums determined by the three successor relations are the vertices of a maximizing simplex. Fifteen pairings and two orientations yield all \(30\) distinct maximizers.

## Assumptions and scope

Volumes are ordinary five-dimensional Euclidean volumes. The generating simplex need not be regular: any nondegenerate centered simplex is allowed. The **dimension is exactly five**; no dimension-independent volume-ratio assertion is made. Any simplex contained in the zonotope is admissible, whether or not its vertices are zonotope vertices.

For a nonempty proper subset \(S\subsetneq\{0,1,2,3,4,5\}\), set \(z_S=\sum_{i\in S}a_i\). All \(62\) such sums are different exposed vertices of \(Z_\Delta\). Indeed, the six generating vectors span a five-dimensional space and have the unique linear dependence \(\sum a_i=0\). Their scalar products with an arbitrary linear functional range over all real six-vectors whose entries sum to zero. Thus every sign choice involving both signs can be realized strictly, exposing the corresponding subset sum. Conversely, an exposed zonotope vertex is a subset sum; the empty/full choices both give the origin, which is interior and not a vertex.

## Proof

**1. Affine normalization and zonotope volume.** Since \(a_0=-\sum_{i=1}^{5}a_i\), use \(a_1,\ldots,a_5\) as a basis and put \(D=|\det(a_1,\ldots,a_5)|>0\). Each of the six parallelotopes in the standard cubulation obtained by omitting one generator has volume \(D\). These parallelotopes cover the zonotope with pairwise disjoint interiors. Hence
\[
\operatorname{vol}_5(Z_\Delta)=6D.
\]
This is also the usual determinant-sum formula for zonotope volume.

**2. Exact finite certificate for all vertex simplices.** Index subsets by binary masks \(m\in\{1,\ldots,62\}\), with bit \(i\) indicating membership of \(i\). In the chosen basis, the vertex of mask \(m\) has integer coordinates
\[
b(m)=\bigl(\mathbf1_{\{1\in S\}}-\mathbf1_{\{0\in S\}},\ldots,\mathbf1_{\{5\in S\}}-\mathbf1_{\{0\in S\}}\bigr).
\]
For six distinct masks \(m_0,\ldots,m_5\), the corresponding simplex volume is
\[
\frac{D}{5!}\bigl|\det[b(m_j)-b(m_0)]_{j=1}^{5}\bigr|.
\]
Permuting the six generator labels induces a volume-preserving linear automorphism in the normalized coordinates; complementing every subset induces central inversion. It is therefore enough to enumerate five additional vertices when the first subset has size \(1\), \(2\), or \(3\). There are precisely \(\binom{61}{5}=5{,}949{,}147\) unordered choices for each of these three representatives. Exact signed-integer Bareiss elimination gives maximum absolute determinants \(14\), \(17\), and \(18\), respectively. The size-three representative belongs to exactly \(9\) determinant-\(18\) simplices; the other two representatives belong to none. Thus the global determinant upper bound is \(18\) and **every** maximizing vertex simplex uses six subset masks of cardinality exactly \(3\).

An independent enumeration of the \(\binom{20}{6}=38{,}760\) six-element selections from the \(20\) size-three subsets finds exactly \(30\) determinant-\(18\) selections. On each, the determinant was also evaluated by the independent \(120\)-term Leibniz expansion. The verifier enumerates the \(15\) perfect matchings and two pair-cycle directions directly; their \(30\) mask collections agree **as sets** with those \(30\) determinant maximizers. Finally, no two maximizing six-mask collections have five masks in common, as confirmed by exact insertion of all \(180\) five-mask deletion sets into a distinct-key container. These statements are finite lemmas proved by the complete source code `verify.cpp`, with all ranges and invariant checks specified there; no random trials or floating-point judgments are used.

**3. Passage from vertex simplices to all inscribed simplices and rigidity.** For arbitrary points \(x_0,\ldots,x_5\in Z_\Delta\), their oriented determinant is multi-affine in the six entries. Fix an orientation for which it is nonnegative. Writing each point as a convex combination of zonotope vertices and expanding the determinant gives a convex combination of vertex-tuple determinants, all at most \(18D\) in the chosen normalization. Therefore the volume of any inscribed simplex is at most \(18D/5!\).

Suppose equality holds and some vertex \(x_j\) of that simplex is not a zonotope vertex. Its convex representation involves at least two distinct exposed vertices. Equality in the determinant convex average forces both corresponding replacement tuples to attain the global bound with the **same orientation**. Sequentially expanding the remaining five entries and using the same equality condition yields two maximizing all-vertex tuples sharing those five vertices. This contradicts the finite certificate's no-shared-five condition. Hence every maximizing simplex is an all-vertex simplex, and the matching-cycle classification is exhaustive.

Combining the determinant maximum and the zonotope volume yields
\[
\frac{\max_T\operatorname{vol}_5(T)}{\operatorname{vol}_5(Z_\Delta)}
=\frac{18D/120}{6D}=\frac1{40}.
\]

## Verification

The standalone file `verify.cpp` requires only a standard C++17 compiler. From the directory containing that file run:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify
./verify
```

The verifier reconstructs the \(62\) vertices, evaluates all \(3\binom{61}{5}=17{,}847{,}441\) orbit-representative five-vertex completions by exact integer elimination, and independently evaluates all \(38{,}760\) size-three-mask six-tuples by both elimination and permutation expansion. It checks the \(30\)-member matching-cycle description and the \(180\) distinct five-face deletion keys. A successful execution prints `VERIFY_OK` after numerical assertions pass. The finite enumeration is exhaustive **only for the specified finite configurations**; the extension to arbitrary points of the convex body is furnished by the multi-affinity argument above.

## Relationship to prior work

Živaljević defined the simplex-generated \(\Delta\)-zonotope and its standard cubulation, and explained its connection to rhombic dodecahedra, the dual of a simplex difference body, and polyhedral-curtain constructions [1]. That gives the canonical underlying object and its zonotope volume, but the inspected article does not determine its maximum-volume contained simplex. Work on largest simplices in cubes [2] has a related determinant optimization, but an inscribed simplex of a **projection** of a cube is not, without additional analysis, a simplex contained in the original cube. The classical maximum absolute determinant \(9\) for a \(6\times6\) binary matrix [4] already yields the numerical determinant \(18\) **when restricted to the constant-three-subset layer**, by the identity between projected volume determinant and twice the determinant of that binary incidence matrix; that numerical component is therefore not claimed as new. The theorem additionally requires a strict comparison with all other layers, a complete geometric equality classification, and rigidity against arbitrary nonvertex maximizers. The hypersimplex \(\Delta(3,6)\), whose vertices constitute the middle layer used in the equality classification, has been studied through regular subdivisions [3]; those subdivision counts are not the present maximum-volume theorem.

## Limitations

The classification is restricted to five-dimensional simplex-generated zonotopes. It says nothing about optimality among all zonotopes or about analogous dimension-six thresholds. The numerical certificate is an exhaustive finite proof only because the exact vertex reduction and the all-point rigidity step were proved separately. Possible overlap with older maximal-determinant or cube-projection classifications remains a historical-priority risk; the full text of one especially relevant 1996 paper was not available for comparison. No independent validation has been performed.

## References

1. R. T. Živaljević, *Illumination complexes, \(\Delta\)-zonotopes, and the polyhedral curtain theorem*, arXiv:1307.5138, first posted 2013-07-19; especially Definition 5 and Section 3. https://arxiv.org/abs/1307.5138
2. M. Hudelson, V. Klee, D. Larman, *Largest \(j\)-simplices in \(d\)-cubes: Some relatives of the Hadamard maximum determinant problem*, Linear Algebra Appl. 241–243 (1996), 519–598. DOI:10.1016/0024-3795(95)00541-2.
3. L. Casabella, M. Joswig, L. Kastner, *Subdivisions of Hypersimplices: With a View Toward Finite Metric Spaces*, arXiv:2402.17665, first posted 2024-02-27. https://arxiv.org/abs/2402.17665
4. POLIP, *hadamard_6* exact binary determinant optimization benchmark, maximum absolute determinant \(9\) for \(6\times6\) binary matrices. https://polip.zib.de/hadamard/hadamard_6.php
