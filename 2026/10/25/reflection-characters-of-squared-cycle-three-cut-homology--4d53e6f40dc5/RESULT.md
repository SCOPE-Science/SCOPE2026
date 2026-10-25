# Reflection characters of squared-cycle three-cut homology

## Finding
Let \(n\ge9\), let \(W_n=C_n^2\) be the graph on \(\mathbb Z/n\mathbb Z\) with edges at cyclic distance one or two, and let \(K_n=\Delta_3(W_n)\) be its **ordinary** three-cut complex. A facet of \(K_n\) is the complement of a three-vertex set inducing a disconnected graph. The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\).

By the established shellability theorem, \(\widetilde H_j(K_n;\mathbb Q)=0\) for \(j\ne n-4\). The character \(\chi_n\) of the remaining representation \(\widetilde H_{n-4}(K_n;\mathbb Q)\) at **every reflection** \(s_a(i)=a-i\pmod n\) is
\[
\boxed{\chi_n(s_a)=
\begin{cases}
(-1)^{(n-1)/2}\,(7-n)/2,& n\text{ odd},\\[3pt]
(-1)^{(n-2)/2}\,(10-n)/2,& n\text{ even and }a\text{ even},\\[3pt]
(-1)^{n/2}\,(6-n)/2,& n\text{ even and }a\text{ odd}.
\end{cases}}
\]
These formulas, together with the previously determined rotation characters, determine the entire rational \(D_n\)-representation by its character. The difference between the two reflection conjugacy classes at even \(n\) is an essential part of the result.

## Assumptions and scope
Here \(n\) is any integer at least nine. The cut complex is **ordinary**, requiring a disconnected induced three-vertex graph, not the total cut complex (which requires three independent vertices). Chain groups use oriented increasing vertex lists. The reflection \(s_a\) fixes two vertices if \(n\) is even and \(a\) is even, and fixes none if \(n\) is even and \(a\) is odd; for odd \(n\) every reflection fixes exactly one vertex. All results are over rational homology, although the chain traces are integral.

## Proof
**1. The Alexander dual.** Let \(L_n=K_n^\vee\) be the combinatorial Alexander dual on the full set of \(n\) vertices. A set belongs to \(L_n\) precisely when **each** of its three-element subsets induces a connected subgraph of \(W_n\). Indeed, the nonfaces of \(K_n\) have complements containing no disconnected triple. The condition is vacuous on sets of size at most two. A connected three-vertex subgraph of \(W_n\) has a central vertex adjacent to the other two. Examining its possible offsets \(\pm1,\pm2\) shows that every such triple, for \(n\ge9\), is a cyclic translate of exactly one of the four distinct patterns
\[
\{0,1,2\},\quad\{0,1,3\},\quad\{0,2,3\},\quad\{0,2,4\}.
\]
A fourth vertex can extend these respective patterns while keeping every triple connected only at offsets \(\{-1,3\}\), \(\{2\}\), \(\{1\}\), and the empty set. This follows directly by intersecting the four-neighbor conditions for the three newly formed triples; no wraparound exception occurs for \(n\ge9\). Therefore every four-face is a cyclic block \(\{i,i+1,i+2,i+3\}\), and no five-face is possible. In particular, \(L_n\) consists of the empty face, all \(n\) vertices, all \(\binom n2\) edges, exactly \(4n\) triangles of the four types, and exactly \(n\) tetrahedra of the consecutive-block type.

**2. Fixed faces under a reflection.** Write \(f\) for the number of fixed vertices, \(t\) for the number of transposed vertex pairs, \(T\) for the number of reflection-invariant triangles, and \(Q\) for the number of reflection-invariant tetrahedra of \(L_n\). Because a reflection has at most two fixed vertices, every invariant triangle comprises one fixed vertex and one transposition pair; the induced orientation sign is \(-1\). Every invariant tetrahedron is two transposition pairs, with sign \(+1\) (it cannot contain two opposite fixed vertices and a transposition pair inside a block of four consecutive vertices when \(n\ge9\)). The invariant edges comprise \(\binom f2\) fixed-point pairs of sign \(+1\) and \(t\) transposition pairs of sign \(-1\).

The explicit four triangle patterns and single tetrahedron pattern from step 1 give the following exhaustive table:

| Reflection type | \(f\) | \(t\) | \(T\) | \(Q\) |
| --- | ---: | ---: | ---: | ---: |
| odd \(n\) (one fixed vertex) | \(1\) | \((n-1)/2\) | \(2\) | \(1\) |
| even \(n\), \(a\) even (two fixed vertices) | \(2\) | \((n-2)/2\) | \(4\) | \(0\) |
| even \(n\), \(a\) odd (no fixed vertices) | \(0\) | \(n/2\) | \(0\) | \(2\) |

For completeness: in the one-fixed-vertex case, the two triangles comprise that vertex and its pairs of neighbors at distances one and two, while the unique invariant four-block lies opposite the fixed vertex. In the two-fixed-vertex case there are two such triangles at each fixed vertex but no invariant four-block. In the no-fixed-vertex case there is no invariant triangle and exactly two four-blocks centered on the two fixed edges. These are direct counts in the displayed cyclic patterns, valid uniformly at the boundary \(n=9\).

**3. Lefschetz number of the dual.** Using the signed permutation action on oriented simplices, the ordinary (unreduced) Lefschetz number of a reflection on \(L_n\) is
\[
\Lambda(s_a;L_n)=f-\bigl(\binom f2-t\bigr)-T-Q.
\]
Substitution into the table yields respectively
\[
\Lambda(s_a;L_n)=
\begin{cases}
(n-5)/2,&n\text{ odd},\\
(n-8)/2,&n\text{ even},\ a\text{ even},\\
(n-4)/2,&n\text{ even},\ a\text{ odd}.
\end{cases}
\]
The previous nonequivariant homotopy theorem states that \(K_n\) is a wedge of spheres solely in degree \(n-4\). Equivariant combinatorial Alexander duality gives
\[
\widetilde H_{n-4}(K_n;\mathbb Q)
\cong\operatorname{sgn}_{\mathbb Z/n}\otimes H^1(L_n;\mathbb Q),
\]
where \(\operatorname{sgn}_{\mathbb Z/n}\) denotes the sign of the vertex permutation; the dual is connected since its one-skeleton is complete. Since \(L_n\) has rational cohomology only in degrees zero and one, the Lefschetz formula gives \(\operatorname{tr}(s_a\mid H^1(L_n;\mathbb Q))=1-\Lambda(s_a;L_n)\). The vertex-permutation sign of a reflection is \((-1)^t\). Combining these statements with the table gives precisely the displayed three cases.

## Verification
The standalone standard-library program `verify_reflections.py` reconstructs the dual directly from connected triples, separately reconstructs the four-pattern combinatorial model, and checks equality of their entire face sets for each \(9\le n\le22\). It enumerates all reflections, computes signed simplicial Lefschetz numbers, and verifies every predicted trace. It also independently constructs the ordinary cut complexes directly from disconnected triples for \(9\le n\le14\) and checks the character formulas on these larger chain complexes, without using Alexander duality in the computation.

The completed verifier printed `VERIFY_OK dual_graph_sizes=14 dual_symmetry_checks=217 direct_cut_symmetry_checks=69 independent_face_template_checks=14`. The finite checks independently stress-test the classification and signs; the all-integer proof is the structural face classification, exact orbit counts and equivariant Alexander duality above.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue established the cut-complex framework and determined cyclic and dihedral actions for **unpowered** cycles, and certain exceptional squared-cycle cut parameters; their Proposition 7.29 does not furnish reflection traces for these ordinary three-cut complexes in the present range. Chauhan, Shukla and Vinayak proved the nonequivariant shellability and sphere multiplicities for squared-cycle three-cut complexes with \(n\ge9\). Chauhan and Shukla's later cycle-power theorem includes this range, again determining nonequivariant topology rather than reflection representations. A separately available cyclic-rotation character calculation covers powered-cycle three-cut complexes but explicitly does not determine the reflection classes. None of those statements supplies the values proved here; the two even-length reflection classes are not recoverable from restricting a representation to rotations.

## Limitations
The formulas concern the full rational character **only at reflections**; rotational values are established in separate literature, and are not reproved here. No integral group-ring decomposition, equivariant homotopy type, or assertion for \(n\le8\) or higher cycle powers is claimed. The reflection formulas are exact for all \(n\ge9\), not an extrapolation from experiments. Independent external scientific validation has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, especially Section 7.4 and Proposition 7.29; SIAM J. Discrete Math. 38 (2024), 1630–1675. https://arxiv.org/abs/2304.13675
2. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, Theorem 1.4 (first available 2024-06-04). https://arxiv.org/abs/2406.01979
3. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, Theorem 1.4 (first available 2026-03-24). https://arxiv.org/abs/2603.23155
4. *Rational cyclic homology representations of three-cut complexes of cycle powers*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-rational-cyclic-homology-representations-of-three-cut-complexes--dc0f17aad16d/RESULT.md (rotation subgroup only).
