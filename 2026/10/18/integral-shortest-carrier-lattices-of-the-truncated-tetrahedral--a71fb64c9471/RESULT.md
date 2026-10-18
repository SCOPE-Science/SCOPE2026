# Integral shortest-carrier lattices of the truncated-tetrahedral matching complex

## Finding
Let \(G\) be the twelve-vertex truncated-tetrahedral graph and \(K=\mathcal M(G)\) its ordinary matching complex. The least number of vertices in an induced subcomplex whose third homology maps nontrivially to \(H_3(K;\mathbb Z)\) is **eight**. Exactly **111** vertex subsets attain it, and every induced subcomplex on such a subset is an octahedral three-sphere \((S^0)^{*4}\). Every fundamental class is nonzero and primitive in
\[
H_3(K;\mathbb Z)\cong\mathbb Z^{22}.
\]
Together these 111 classes generate the **entire integral group**, and a specified set of 22 forms an integral basis.

The full graph automorphism group \(\operatorname{Aut}(G)\cong S_4\) partitions the 111 supports into eight orbits. With orbit indices numbered from zero by lexicographically minimal path-factor representative, their sizes are
\[
(12,12,24,3,24,6,24,6),
\]
and their respective integral homology-span ranks are
\[
(8,11,14,3,13,6,16,6).
\]
Each single-orbit lattice is saturated in its rational span. Among 28 unions of two distinct orbits, exactly the four pairs \((1,6),(2,6),(5,6),(6,7)\) generate \(H_3(K;\mathbb Z)\) integrally. Among 56 unions of three distinct orbits, precisely 19 have full rational rank. Exactly one of these 19, the union \((3,4,6)\), has **index two** rather than one:
\[
H_3(K;\mathbb Z)/\langle\text{fundamental classes from orbits }3,4,6\rangle\cong\mathbb Z/2.
\]
The remaining 18 full-rank three-orbit unions generate integrally. Thus the minimum-support sphere generators expose a natural integral parity obstruction that is invisible from the ambient homotopy type or rational character.

## Assumptions and scope
Define the finite simple graph
\[
V(G)=\{(a,b):a,b\in\{0,1,2,3\},\ a\neq b\},
\]
with an edge between distinct \((a,b)\) and \((c,d)\) precisely if \(a=c\) or \((c,d)=(b,a)\). Number its twelve vertices by lexicographic order, then number its eighteen unordered graph edges by lexicographic endpoint indices, from \(0\) to \(17\). A face of \(K\) is any set of pairwise vertex-disjoint graph edges. An **induced carrier** means an eight-element set of matching-complex vertices (that is, graph edges) for which the induced subcomplex has nonzero integral third homology whose inclusion into \(K\) is nonzero.

For each partition of the twelve graph vertices into four vertex-disjoint paths of length two (a spanning \(P_3\)-factor), pair the two graph edges in each path. The induced matching subcomplex on those eight graph edges is exactly \((S^0)^{*4}\). Choose a deterministic orientation by sorting each of the four paired edge-index pairs, sorting the four pairs lexicographically, and taking the product of the four signed differences \(([b_i]-[a_i])\) in that order. The fundamental chain is the sum of sixteen oriented tetrahedra, including the simplex-order permutation signs. Its sign has no effect on primitiveness, lattice ranks, or indices.

The eight symmetry-orbit labels and the twenty-two basis-index labels are determined by `verify.py` without stored external tables. Orbit \(i\) means the \(i\)-th orbit when the complete list of path factors is lexicographically ordered and orbits are extracted by their least unused representatives.

## Proof
**1. Sharp support bound.** Every matching complex is flag. For a finite flag complex having nonzero reduced homology in degree \(d\ge0\), the smallest possible support has at least \(2d+2\) vertices. For \(d=0\), a disconnected complex needs two nonadjacent vertices. Inductively, let \(L\) be a minimal such induced support in degree \(d>0\). Deleting any vertex kills degree-\(d\) homology. The deletion–link long exact sequence therefore injects the nonzero group \(\widetilde H_d(L)\) into \(\widetilde H_{d-1}(\operatorname{lk}_L(v))\). The link requires at least \(2d\) vertices by induction. The vertex \(v\) has a nonneighbor (otherwise \(L\) is a cone), so \(|V(L)|\ge2d+2\).

In case of equality, the link has exactly \(2d\) vertices and by induction is the boundary of the \(d\)-dimensional cross-polytope. There is exactly one vertex \(w\) outside the link and \(v\). The fundamental \((d-1)\)-cycle of this link must bound in \(L-v\) for \(\widetilde H_d(L)\) to survive the deletion–link sequence. Since the link has dimension \(d-1\), any such filling consists of \(d\)-simplices with apex \(w\). The link sphere has a one-dimensional top-cycle group and its fundamental chain uses every facet; therefore \(w\) must be adjacent to every link vertex. Since \(v\) and \(w\) are not adjacent, \(L\) is the suspension of the link, hence the boundary of the \((d+1)\)-cross-polytope. For \(d=3\), all eight-vertex carriers must be octahedral spheres \((S^0)^{*4}\).

**2. Exhaustive octahedral classification.** In the matching complex, two of the eight carrier vertices form an opposite pair precisely when their graph edges meet at one graph vertex; graph edges from distinct opposite pairs are disjoint. As the graph is simple, each pair is a two-edge path on three distinct graph vertices. Four mutually disjoint pairs use twelve graph vertices, exactly \(V(G)\). Thus eight-vertex octahedral induced subcomplexes are in bijection with spanning \(P_3\)-factors. The exact checker enumerates all 36 unordered incident graph-edge pairs, examines every four-pair choice, and retains precisely those covering all twelve graph vertices. It obtains 111 different eight-edge supports. Every associated sixteen-tetrahedron alternating chain has zero integral simplicial boundary.

**3. Integral Morse model and actual homology classes.** Enumerating all matchings gives the face vector (dimensions zero through five)
\[
(18,117,332,390,144,8).
\]
Process graph-edge indices in ascending order, pairing each currently unmatched simplex missing index \(i\) with its one-index augmentation whenever both are still unmatched. The checker verifies all 3,558 oriented cover relations in the nonempty simplicial face poset and finds no directed cycle. Exactly 493 pairs and a critical zero-cell and 22 critical three-cells remain. Forman's discrete-Morse theorem yields \(K\simeq\bigvee^{22}S^3\) over the integers. This homotopy type itself was known previously and is not the claimed discovery.

For explicit integer homology coordinates, cancel the matched degree-\((3,4)\) cellular pairs using their integer boundary coefficients \(\pm1\). If a paired lower three-simplex is the \(p\)-th face of its matched upper four-simplex, replace its class by the signed sum of the other four faces, with coefficient \((-1)^{1+j-p}\) on face \(j\). Acyclicity guarantees termination. Set every matched upper three-simplex (paired to a lower two-simplex) to zero and send the 22 critical three-simplices to the standard basis. This is the degree-three map of the integral Morse chain equivalence and therefore induces an isomorphism on third homology. The checker also explicitly verifies that this map annihilates the signed boundary of **every** four-simplex, rather than relying on a rank calculation alone.

Applying this projection to all 111 alternating sphere cycles gives a \(22\times111\) integer coordinate matrix. Every column has content (gcd of its 22 coordinates) equal to one, proving all carriers represent primitive nonzero classes. Its Smith invariant factors are 22 copies of one, proving that the whole family generates integrally. In the lexicographic zero-based ordering of the 111 carriers, the 22 columns
\[
(99,36,47,97,94,110,84,1,53,74,11,33,16,32,96,37,22,68,61,30,65,86)
\]
have determinant \(+1\) in the displayed Morse coordinate basis and hence themselves form an integral basis.

**4. Full symmetry and exceptional lattice.** The four graph triangles with constant first coordinate are the only graph three-cycles. Every automorphism must permute them, and its action on the reversal edges then determines every vertex. Hence the automorphism group injects into \(S_4\); all symbol permutations act, so equality holds. The verifier reconstructs all 24 permutations, their action on all 111 path factors, and the eight orbits of the listed sizes. Exact Smith normal forms of their coordinate submatrices give individual orbit ranks \((8,11,14,3,13,6,16,6)\), with only unit nonzero Smith factors for each single orbit. It then checks every two- and three-orbit union. The four generating pairs and the unique full-rank index-two triple have precisely the indices asserted in the finding. In particular, the exceptional Smith normal form has 21 unit factors and one factor two, so its quotient is \(\mathbb Z/2\), not merely an unspecified index-two subgroup.

## Verification
Run `python3 verify.py` with `sympy==1.14.0`, as specified in `requirements.txt`. It reconstructs the graph and every simplex from first principles, checks the complete acyclic Morse matching and all 144 degree-four boundaries, enumerates all 111 alternating cycles and all 24 automorphisms, constructs the 22-row exact integer coordinate matrix, verifies primitiveness and a unit 22-column determinant, and uses exact Smith normal forms for all orbit-union claims. Successful output begins `VERIFY_OK_TRUNCATED_TETRA_SHORTEST_CARRIERS`. No random sampling, incomplete enumeration, floating-point linear algebra, external certificate, or unproved extrapolation is used.

## Relationship to prior work
Engström, *Independence complexes of claw-free graphs* (2005), studies general connectivity in a class containing line-graph independence complexes; its theorems do not compute this graph's induced carriers or integer orbit lattices. Barmak, *Star clusters in independence complexes of graphs* (2010), gives general homotopy and connectivity constructions, including a section on matching complexes; these do not specify the present natural finite graph or its integral path-factor classes. Bayer, Jelić Milutinović and Vega, *Matching Complexes of Outerplanar Graphs* (2024), prove a wedge-of-spheres theorem for outerplanar graphs; the truncated-tetrahedral graph has a \(K_4\) minor (contract its four triangles) and is not outerplanar.

The published calculation *Edge-orbit matching-complex homotopy of the truncated tetrahedron* identifies the same graph and proves its 22-sphere homotopy type and edge-deletion/link orbit splittings. That full result was compared: it contains no 111-carrier census, primitive-support classification, integral orbit-rank table, or exceptional orbit-union quotient. Existing rational \(S_4\) character information also does not determine integral generators or their saturation indices. The present claim concerns **the new minimum-support geometric homology lattice**, not the previously known homotopy type, dimension, or rational symmetry module.

## Limitations
All conclusions concern this specified finite graph and ordinary matching complex, not arbitrary planar graphs or a family of truncated polyhedra. The eight-vertex lower bound and its equality case are proved for arbitrary flag complexes, but the enumeration and the integral lattice table are specific to this graph. Computational statements are exact and exhaustively checked for this finite complex; they do not establish any general asymptotic assertion. The source comparisons cannot guarantee publication priority in inaccessible or unindexed literature. An independent external audit has not been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, 17 December 2005, https://arxiv.org/abs/math/0512420.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, 2 July 2010, https://arxiv.org/abs/1007.0418.
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, 7 November 2024, https://arxiv.org/abs/2411.04601.
4. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published-finding corpus 2026/10/11 identifier f5ae4a359c83, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83.
