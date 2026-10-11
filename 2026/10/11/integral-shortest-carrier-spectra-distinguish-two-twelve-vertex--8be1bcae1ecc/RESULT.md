# Integral shortest-carrier spectra distinguish two twelve-vertex projective-plane connected sums
## Finding
Let \(K_{+}\) and \(K_{\pm}\) be the published twelve-vertex triangulations of
\[
\mathbb{CP}^{2}\#\mathbb{CP}^{2}
\quad\text{and}\quad
\mathbb{CP}^{2}\#-\mathbb{CP}^{2},
\]
respectively. Both have
\[
f=(12,57,148,165,66)
\]
and
\[
H_2(-;\mathbb Z)\cong\mathbb Z^2.
\]

For both complexes, the minimum vertex support of a nonzero integral simplicial \(2\)-cycle is exactly \(4\). Exactly \(72\) four-vertex supports attain the minimum. Every minimum carrier is an induced tetrahedral sphere \(\partial\Delta^3\), and every such sphere represents a primitive integral homology class.

After identifying a class with its negative, the integral minimum-carrier spectra are different:
\[
K_{+}:\quad 33,\ 33,\ 3,\ 3,
\]
whereas
\[
K_{\pm}:\quad 33,\ 33,\ 6.
\]

The mod-two spectra are nevertheless identical. In each complex, the three nonzero classes of
\[
H_2(-;\mathbf F_2)\cong\mathbf F_2^2
\]
occur on
\[
33,\quad33,\quad6
\]
minimum supports.

Thus the integral lift refines a mod-two spectrum that cannot distinguish the two triangulations: in \(K_{+}\), the six carriers over the least-populated mod-two class split \(3+3\) between two distinct integral classes up to sign, while in \(K_{\pm}\) all six belong to one integral class up to sign.

## Assumptions and scope
The labelled complexes are the `CP^2#CP^2` and `CP^2#-CP^2` entries of the published `small_4_manifolds.txt` facet table. Vertices are \(1,\ldots,12\).

Vertex support means the union of vertices occurring with nonzero coefficient in a simplicial chain. Integral classes are compared up to reversal of the sphere orientation, so a class and its negative are counted together.

The displayed coordinate labels used by `verify.py` arise from deterministic unimodular chain reductions and are not asserted to be canonical intersection-form bases. The multiplicity multisets and the number of integral classes up to sign are basis-independent.

## Proof
For each facet list, exact reconstruction gives \(57\) edges, \(148\) triangles, \(165\) tetrahedra, and \(66\) four-simplices.

The integral triangle-to-edge boundary matrix has size \(57\times148\). The verifier performs only unimodular row and column operations and reduces it to an identity block of rank \(46\) with zero residual block. Hence the integral \(2\)-cycle lattice is free of rank
\[
148-46=102.
\]

The tetrahedron-to-triangle boundary map is then expressed in this exact integral cycle basis. A second unimodular reduction produces an identity block of rank \(100\) with zero residual block. Consequently, independently for each complex,
\[
H_2(-;\mathbb Z)\cong\mathbb Z^{102}/\mathbb Z^{100}\cong\mathbb Z^2.
\]
The same reduction provides exact integral coordinates for every \(2\)-cycle.

A nonzero simplicial \(2\)-cycle cannot be supported on fewer than four vertices. On four vertices, the only possible nonzero \(2\)-cycle is a scalar multiple of the oriented boundary of the tetrahedron, and it exists only when all four triangular faces are present.

The verifier exhausts all
\[
\binom{12}{4}=495
\]
four-vertex subsets. In each complex there are exactly \(72\) sets whose four triangular faces are present but whose tetrahedron is absent. For every actual tetrahedron, its boundary reduces to zero in \(H_2\). For every one of the \(72\) missing tetrahedra, the boundary has a nonzero primitive coordinate vector. Hence these \(72\) induced tetrahedral spheres are exactly the minimum-support nonzero integral classes.

In the verifier's integral bases, the up-to-sign class multiplicities are
\[
K_{+}:\quad
(1,0):33,\quad(0,1):33,\quad(1,-1):3,\quad(1,1):3,
\]
and
\[
K_{\pm}:\quad
(1,0):33,\quad(0,1):33,\quad(1,1):6.
\]
Example carriers for \(K_{+}\) are \(\{1,2,3,6\}\), \(\{1,3,5,9\}\), \(\{1,2,3,9\}\), and \(\{5,6,7,10\}\); for \(K_{\pm}\) they are \(\{1,2,3,4\}\), \(\{1,2,3,10\}\), and \(\{1,2,4,10\}\).

Reducing these exact integral coordinates modulo \(2\) gives, in both complexes, the identical nonzero-class multiplicities
\[
33,\quad33,\quad6.
\]
For \(K_{+}\), the two threefold integral classes become equal modulo \(2\), explaining the \(3+3\) merger.

## Verification
The standalone `verify.py` embeds all \(66\) four-simplices of each triangulation and uses only the Python standard library.

It reconstructs both face vectors, performs both integral unimodular chain reductions, exhausts every four-vertex subset, verifies all \(144\) minimum carriers across the pair are nonzero and primitive, and independently checks the integral and mod-two multiplicity spectra.

Exact successful output:

`VERIFY_OK f_both=12,57,148,165,66 H2_Z=Z^2 min_vertex_support=4 carriers=72_each all_primitive=yes integral_spectra=33,33,3,3|33,33,6 mod2_spectra=33,33,6|33,33,6 reps_pp=1236|1359|1239|56710 reps_pm=1234|12310|12410`

The minimum-support conclusion is exhaustive: supports of size below four are impossible for a nonzero simplicial \(2\)-cycle, and every four-vertex support is checked.

## Relationship to prior work
Lutz's survey gives both twelve-vertex connected-sum triangulations, their common face vector \((12,57,148,165,66)\), and their common integral homology rank in degree two; it links to the complete facet lists. The exact online table defines the two labelled complexes used here.

Classical smooth four-manifold literature studies which abstract second-homology classes can be represented by smoothly embedded \(2\)-spheres. In particular, Luo gives a representability theorem for the indefinite connected sum \(\mathbb{CP}^{2}\#-\mathbb{CP}^{2}\). That broader representability problem does not determine the shortest supports in these particular triangulations, their exact number \(72\), or the \(33,33,3,3\) versus \(33,33,6\) integral spectra.

Focused searches using both connected-sum names, twelve-vertex terminology, missing-tetrahedron language, shortest \(H_2\)-support language, and the numerical fingerprints did not locate a published statement of this comparative spectrum.

## Limitations
The result concerns vertex support in two specific labelled triangulations, not minimal genus or metric area in the underlying smooth four-manifolds.

The integral coordinate bases in the verifier are computational bases. Only the class counts up to sign, their multiplicities, and the reduction pattern to mod-two homology are claimed as basis-independent features.

An unindexed historical computation could contain the same finite carrier census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:`math/0506372v1`, submitted 2005-06-18; Section 5 and Proposition 42.
2. F. H. Lutz, *The Manifold Page*, `small_4_manifolds.txt`, entries `CP^2#CP^2` and `CP^2#-CP^2`.
3. F. Luo, *Representing homology classes of \(\mathbb{CP}^{2}\#-\mathbb{CP}^{2}\)*, Pacific Journal of Mathematics 133 (1988), 137--140, DOI `10.2140/pjm.1988.133.137`.
