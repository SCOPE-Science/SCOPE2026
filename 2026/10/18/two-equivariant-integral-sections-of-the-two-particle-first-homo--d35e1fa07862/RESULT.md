# Two equivariant integral sections of the two-particle first-homology projection for the complete five-vertex graph

## Finding
Let \(K_5\) be the complete graph on labeled vertices \(\{0,1,2,3,4\}\), let \(X=\operatorname{UConf}_2(|K_5|)\), and let \(S_5\) permute the graph vertices. The *total-motion* map sends a closed two-particle motion to the sum of its traversals of oriented graph edges. Its induced integral homology map satisfies
\[
0\longrightarrow\mathbb Z/2\longrightarrow H_1(X;\mathbb Z)
\xrightarrow{p_*}\bigwedge\!^2 A_4\longrightarrow0,
\qquad A_4=\{(a_0,\ldots,a_4)\in\mathbb Z^5:\sum a_i=0\}.
\]
This is a sequence of integral \(S_5\)-modules, with trivial action on the torsion kernel. It **splits equivariantly**, and there are **exactly two** integral \(S_5\)-equivariant sections. Consequently the integral first-homology module is \(\bigwedge^2 A_4\oplus\mathbb Z/2\), although the pair of splittings contains additional canonical information.

## Assumptions and scope
Here \(\operatorname{UConf}_2(Y)=(Y^2\setminus\Delta)/S_2\). No particles may coincide anywhere in the graph, and graph-edge subdivision does not change the space. The five-label symmetry permutes original vertices and sends each edge midpoint to the midpoint of its permuted edge. We use ordinary singular homology with integral coefficients. The map \(p_*\) sends the sum of particle trajectories, with an orientation sign for every traversed edge; this is well-defined even when a closed unordered motion exchanges particles. For the oriented edges \(i\to j\), the identity \(e_{ij}\mapsto e_i\wedge e_j\) identifies graph cycles with \(\bigwedge^2 A_4\) as integral \(S_5\)-lattices.

## Proof
**1. Finite cubical model and group structure.** Subdivide every one of the ten edges of \(K_5\) at its midpoint. A cubical discretization of the unordered two-particle configuration space has unordered distinct-vertex cells, vertex-edge cells with disjoint closures, and unordered pairs of disjoint open edges. This is a deformation-retract model under the standard sufficient-subdivision criterion for two particles. It contains exactly \(105\) zero-cells, \(260\) one-cells, and \(150\) square two-cells. Choose a spanning tree of its one-skeleton; the signed square boundary then gives a \(156\times150\) presentation matrix for \(H_1\). Exact integer Smith reduction has \(149\) diagonal entries equal to \(1\) and a single entry equal to \(2\), all remaining invariant factors absent. The one-skeleton is connected. Thus \(H_1(X;\mathbb Z)\cong\mathbb Z^6\oplus\mathbb Z/2\). The deterministic checker embedded here constructs the cell lists and boundary matrix and asserts these invariant factors rather than relying on an approximate rank.

**2. The canonical surjection.** Each of the ten oriented original edges contributes to total motion with its signed traversal number. Every triangular graph cycle can be traversed by one particle while the other remains at one of the two unused original vertices. As triangles generate the integral cycle lattice of a complete graph, \(p_*\) is onto. The graph cycle lattice has rank six, so the group calculation above forces \(\ker(p_*)\cong\mathbb Z/2\). Every automorphism fixes the unique nonzero torsion element, hence acts trivially on this kernel. With \(\mathbb Z^5=A_4\oplus\mathbb Z e_0\) as abelian groups, contraction by the sum functional identifies the kernel of the graph incidence map on \(\bigwedge^2\mathbb Z^5\) with \(\bigwedge^2 A_4\), naturally for the permutation action (the identification is canonical even though this displayed direct summand is not).

**3. Equivariant section calculation over two elements.** Let \(V=H_1(X;\mathbb F_2)\) and \(W=H_1(K_5;\mathbb F_2)\). The cubical presentation has \(\dim V=7\) and \(\dim W=6\). A spanning-tree quotient produces a basis in which the seven columns of the projection \(P:V\to W\), encoded as binary integers with the lowest bit giving row zero, are
`[7,25,42,4,16,1,3]`.
For the generators \(t=(0\ 1)\) and \(c=(0\ 1\ 2\ 3\ 4)\) of \(S_5\), the columns of the action on \(V\) are respectively
`[8,16,31,1,2,32,64]` and `[7,8,16,4,96,72,74]`,
while the columns on \(W\) are
`[1,2,7,8,25,42]` and `[7,25,42,1,2,8]`.
The checker recomputes all these values directly from cell permutations and signed boundaries reduced modulo two. Writing a section as a \(7\times6\) unknown matrix \(S\), the equations \(PS=I\), \(T_tS=SU_t\), and \(T_cS=SU_c\) form a linear system with \(42\) binary unknowns. The coefficient rank and augmented rank both equal \(41\). Therefore there are exactly two equivariant sections over \(\mathbb F_2\), with their six columns encoded by
`[32,41,65,50,89,86]` and `[105,96,8,123,16,31]`.
Both explicitly satisfy all three equations, as the verifier asserts.

**4. Lifting, and completeness over the integers.** Since \(p_*\) is onto a free abelian group, it has an ordinary integral section \(s_0\). Reduction modulo two is exact in this situation, yielding a short exact sequence \(0\to\mathbb F_2\to V\to W\to0\); the torsion kernel injects into \(V\) because the integral middle group is \(\mathbb Z^6\oplus\mathbb Z/2\). For either equivariant section \(\bar s\) over \(\mathbb F_2\), its difference from the reduction of \(s_0\) is a linear map from \(W\) into that one-dimensional torsion kernel, and this map lifts uniquely to a homomorphism from the integral graph cycle lattice into \(\mathbb Z/2\). Adding it to \(s_0\) gives an integral section \(s\). For each of the two generating permutations, its failure to be equivariant lies in the order-two kernel and reduces to zero in the injective mod-two kernel; it is therefore zero integrally. Conversely any integral equivariant section reduces to one of the two computed sections; two integral sections with the same mod-two reduction have zero difference because that difference lies in the torsion kernel, on which reduction is injective. There are exactly two integral equivariant sections, completing the proof.

## Verification
Run `python verify.py` with Python 3 and SymPy as in `requirements.txt`. The verifier reconstructs all cells, the integral signed boundary matrix, its exact Smith normal form, the \(S_5\)-generator actions on mod-two homology, the projection, the rank-\(41\) equivariant-section system, and both sections. Assertions check the claimed sizes and all recorded certificates. Its deterministic computation terminates on this finite complex; it is not a claim about arbitrary graph configuration spaces.

## Relationship to prior work
Ko and Park, *Characteristics of graph braid groups* (arXiv:1101.2648, initially posted 2011-01-13), Theorem 3.16, computes the abstract first-homology group for nonplanar triconnected graph braid groups. In particular, the underlying \(\mathbb Z^6\oplus\mathbb Z/2\) computation for \(K_5\) is already implied by that theorem, and is not claimed as new. Their published rank-and-torsion formula does not determine the vertex-permutation-equivariant sections of the canonical total-motion map. This result concerns the latter integral equivariant question, including the precise number of splittings.

## Limitations
The theorem concerns only two unordered particles on the topological realization of \(K_5\) and the natural vertex-permutation action. The proof uses exact finite computation for the equivariant section count; no formula for general nonplanar graphs, integral higher homology, or space-level equivariant splitting is asserted. Bibliographic overlap risk remains for unindexed or inaccessible literature on automorphism actions of graph braid groups.

## References
Ko, K. H., and Park, H. W., *Characteristics of graph braid groups*, arXiv:1101.2648 (first public version 2011-01-13), especially Theorem 3.16 and the cubical-model discussion, https://arxiv.org/abs/1101.2648.
