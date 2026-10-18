# Complete tetrahedral symmetry characters of generalized discrete Morse matching complexes

## Finding
For \(K=\Delta^3\) or \(K=\partial\Delta^3\), form the **generalized discrete-Morse matching complex** \(\mathcal G(K)\): its vertices are cover incidences \((A,B)\) of nonempty faces of \(K\), where \(A\subset B\) and \(|B|=|A|+1\), and its simplices are sets of these incidences with pairwise disjoint endpoints. Acyclicity of the underlying partial matching is **not** imposed.

The natural action of the tetrahedral vertex-permutation group \(S_4\) on the only nonzero reduced rational homology, \(\widetilde H_4(\mathcal G(K);\mathbb Q)\), has the **same full character** for the simplex and its boundary. On the conjugacy classes with cycle types \((1^4),(2,1^2),(2^2),(3,1),(4)\), the character is respectively
\[
\boxed{(39,\ 1,\ -5,\ 0,\ 3).}
\]
As a rational representation, in both cases this is
\[
\boxed{2S^{(4)}\oplus5S^{(3,1)}\oplus2S^{(2,2)}\oplus6S^{(2,1,1)}.}
\]
No copy of the sign representation occurs. Consequently, for either \(K\), the geometric orbit space \(|\mathcal G(K)|/S_4\) has \(\widetilde H_4(-;\mathbb Q)\cong\mathbb Q^2\) and all its other reduced rational homology groups vanish.

## Assumptions and scope
The underlying simplex uses the four labels \(\{0,1,2,3\}\). Its face poset consists of all \(15\) nonempty subsets; its boundary removes only the full four-element subset. Thus the Hasse incidence graphs have respectively \(28\) and \(24\) edges. Their generalized matching complexes have respectively \(14{,}720\) and \(5{,}096\) nonempty faces. Here \(S^{\lambda}\) denotes the rational Specht module of the indicated partition of four. The statement concerns rational homology representations and rational homology of geometric quotients, not equivariant homotopy type, the integral action, or the map induced by the inclusion of the boundary.

The sole external topological premise is Scoville's established nonequivariant homotopy classification, \(\mathcal G(\Delta^3)\simeq\mathcal G(\partial\Delta^3)\simeq\bigvee^{39}S^4\) (Theorem 24 in the cited preprint). It provides the rational homology concentration and rank; the symmetry character is calculated below directly.

## Proof
**Signed fixed-simplex formula.** Let \(E(K)\) be the Hasse incidence edges, viewed as vertices of \(\mathcal G(K)\). Fix \(g\in S_4\), and partition \(E(K)\) into its orbits under \(g\). An orbit is *admissible* if its constituent Hasse edges have no shared endpoints. Define \(B_g\) to be the finite simple graph with admissible edge orbits as vertices, and join two such vertices precisely when their underlying Hasse edges have a shared endpoint. A set of Hasse edges is a \(g\)-invariant matching exactly when it is the union of an independent set of \(B_g\): an invariant set must contain every edge in any orbit it intersects; it is a matching exactly when each selected orbit is internally admissible and any two selected orbits do not conflict. This is a bijection that also includes the empty matching.

Let a nonempty fixed simplex correspond to an independent set of \(j\) orbit blocks, comprising \(k\) Hasse edges. Its dimension is \(k-1\). The induced permutation on its oriented simplex vertices has \(j\) cycles and therefore sign \((-1)^{k-j}\). Its contribution to the unreduced simplicial Lefschetz trace is consequently \((-1)^{k-1}(-1)^{k-j}=(-1)^{j-1}\). Including the reduced augmentation (empty matching, contribution \(-1\)) gives the exact **reduced** Lefschetz number
\[
\widetilde L(g;\mathcal G(K))=-\sum_{I\in\operatorname{Ind}(B_g)}(-1)^{|I|}.
\]
Here \(\operatorname{Ind}(B_g)\) is the set of all independent vertex subsets of the conflict graph, including the empty set. This formula is valid whether the action has fixed simplices pointwise or only setwise.

**Exact all-class enumeration.** The following complete independence-set size counts are obtained by a finite recursion that branches on the first remaining orbit: exclude it, or include it and remove every adjacent orbit. For an independent set of cardinality \(j\), its count is the \(j\)-th entry of the displayed vector, beginning at \(j=0\). The two independently executable programs supplied with this result implement respectively this orbit enumeration and a direct census of all matchings; both compute the same character on all \(24\) elements of \(S_4\).

| Cycle type | Counts for \(\mathcal G(\Delta^3)\) | Counts for \(\mathcal G(\partial\Delta^3)\) | Character |
| --- | --- | --- | ---: |
| \((1^4)\) | \([1,28,300,1560,4128,5328,2912,464]\) | \([1,24,216,912,1848,1632,464]\) | 39 |
| \((2,1^2)\) | \([1,10,36,56,36,8]\) | \([1,8,22,24,8]\) | 1 |
| \((2^2)\) | \([1,8,12]\) | \([1,8,12]\) | -5 |
| \((3,1)\) | \([1,7,11,5]\) | \([1,6,5]\) | 0 |
| \((4)\) | \([1,4]\) | \([1,4]\) | 3 |

For each row, taking minus its alternating sum proves the character column. Because Scoville's theorem concentrates reduced rational homology entirely in the **even** degree four, the reduced Lefschetz trace equals \(\operatorname{tr}(g\mid\widetilde H_4)\) with no further sign. The enumerations also establish conjugacy-class invariance directly.

**Representation and geometric orbit space.** The \(S_4\) conjugacy class sizes in the above order are \((1,6,3,8,6)\). Character inner products with the five irreducibles \((4),(3,1),(2,2),(2,1,1),(1^4)\) give multiplicities \((2,5,2,6,0)\), respectively. Their dimensions sum to \(2+15+4+18=39\) as required. In particular the multiplicity of the trivial representation is
\[
\frac{39+6\cdot1+3\cdot(-5)+8\cdot0+6\cdot3}{24}=2.
\]
For a finite group acting simplicially on a finite complex, barycentric subdivision provides a cellular action for which the rational cellular chains of the geometric quotient identify with the invariant cellular chains; invariants over \(\mathbb Q\) are exact by averaging. Thus \(H_*(|\mathcal G(K)|/S_4;\mathbb Q)\cong H_*(\mathcal G(K);\mathbb Q)^{S_4}\). The theorem follows.

## Verification
The file `gm_orbits.py` enumerates all \(24\) permutations, constructs the orbit conflict graphs, counts independent sets by cardinality and checks their signed evaluations, including the displayed Specht multiplicities. The independent file `gm_character.py` constructs the two Hasse graphs and all \(14{,}720\) and \(5{,}096\) nonempty matchings, respectively, and computes their signed fixed-simplex Lefschetz numbers directly. Both programs use only the Python standard library; run `python3 gm_character.py` and `python3 gm_orbits.py` in the directory containing these two files. Their exact output is supplied in `gm_character_output.txt` and `gm_orbit_output.txt`.

The finite enumerations verify the character calculation for the specified two complexes, not an infinite-dimensional assertion or a new proof of Scoville's homotopy classification.

## Relationship to prior work
Scoville, *The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results* (first public 20 April 2026), proves the nonequivariant wedge-of-39-four-spheres homotopy classifications used here. These Betti numbers do not imply the full \(S_4\)-characters or their coincidence. The cited paper treats generalized matchings as distinct from the *acyclic* discrete Morse matching complex; for the latter, separate symmetry calculations exist and must not be conflated with the present object. Chari and Joswig introduced the underlying discrete Morse complex formalism; their acyclic construction does not state the generalized complex's rational tetrahedral character. Knudson and Owens-White study strong matching complexes, another distinct notion.

## Limitations
The result is specific to the tetrahedron and its boundary and relies on Scoville's published nonequivariant homotopy theorem. Equality of rational characters does **not** prove that the natural inclusion induces an isomorphism in homology, nor an equivariant homotopy equivalence. No integral symmetry-lattice, torsion in quotient homology, or extension to higher simplices is asserted. The literature comparison does not rule out unindexed equivalent calculations.

## References
1. Nicholas A. Scoville, *The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results*, arXiv:2604.18172v1 (2026-04-20), especially the generalized-complex definition and Theorem 24. https://arxiv.org/abs/2604.18172
2. Manoj K. Chari and Michael Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (2000-11-28). https://arxiv.org/abs/math/0011234
3. Kevin Knudson and Abigail Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (2026-09-06). https://arxiv.org/abs/2609.06844
