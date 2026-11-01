# Full icosahedral symmetry on two-particle configuration homology
## Finding
Let \(I\) be the 12-vertex, 30-edge icosahedral graph and \(X=\operatorname{UConf}_2(|I|)\), the space of two unordered distinct particles on its geometric realization. Its full automorphism group is \(G\cong A_5\times C_2\). Write \(V_4,V_5,V_6\) for the rational irreducible \(A_5\)-representations of dimensions \(4,5,6\); \(V_6\) is the rational form of the pair of complex-conjugate three-dimensional representations. Superscripts \(+\) and \(-\) specify the eigenvalue of the central inversion. Then
\[
H_1(X;\mathbb Q)\cong(V_4\oplus V_6)^+\oplus(\mathbf 1\oplus V_4\oplus V_5)^-,
\]
\[
H_2(X;\mathbb Q)\cong(3V_4\oplus3V_5\oplus3V_6)^+\oplus(4V_4\oplus3V_5\oplus4V_6)^-.
\]
Moreover \(H_0(X;\mathbb Q)\cong\mathbb Q\), and \(H_i(X;\mathbb Q)=0\) for every \(i\ge3\). In particular \((\beta_0,\beta_1,\beta_2)=(1,20,100)\).

The 20 triangular faces yield exactly 100 unordered pairs of faces with disjoint vertex sets. Their oriented product tori give a **rational basis of second homology**. The full automorphism group permutes this basis with signs. Averaging the complete character gives
\[
\widetilde H_i(X/G;\mathbb Q)=0\quad\text{for all }i,
\]
while for the rotational subgroup \(G^+\cong A_5\), the quotient has \(\widetilde H_1(X/G^+;\mathbb Q)\cong\mathbb Q\) and all other reduced rational homology zero.

## Assumptions and scope
The graph is the standard finite simple icosahedral graph, with vertex labels \(0,\ldots,11\) and the 30 edges listed explicitly in `verify_icosahedron.py`. Two particles are unordered and may occupy distinct open edges, or distinct vertices, but cannot collide. The rational homology of the actual topological configuration space is computed using the unordered Abrams cubical model, valid because every essential vertex is separated from any other by at least one edge and every nontrivial graph cycle has at least three edges (Prue–Scrimshaw's two-particle stable-equivalence criterion).

The central involution is the antipodal graph automorphism; the rotational subgroup has order 60. The representation concerns rational homology; no integral first-homology torsion classification is claimed.

## Proof
**Exact cellular model.** Put \(V=V(I)\), \(E=E(I)\). The unordered two-particle cube complex has 0-cells \(\{u,v\}\) for distinct vertices, 1-cells \((e,v)\) for an edge and a vertex not incident with it, and 2-cells \(\{e,f\}\) for disjoint edges. Its cell counts are \((66,300,315)\). Orient graph edges by increasing label, and orient each square by increasing edge indices. With \(e=(a,b)\), \(f=(c,d)\), \(a<b\), \(c<d\), the square boundary is
\[
\partial_2[e,f]=[(f,b)]-[(f,a)]-[(e,d)]+[(e,c)].
\]
The supplied verifier constructs every column and verifies \(\partial_1\partial_2=0\). The connected cubical 1-skeleton gives \(\operatorname{rank}\partial_1=65\), also confirmed by exact binary elimination.

**Product-torus basis and sharp rank.** The graph has precisely 20 triangles. Exactly 100 unordered pairs \(\{F_i,F_j\}\) have disjoint vertex sets. Orient the boundary cycle of each triangle \(F_i\) and form the unordered oriented product 2-cycle \(z_{ij}\) supported on its nine edge-pair squares, with the sign reversed whenever the two edge coordinates are exchanged. Every \(z_{ij}\) has zero integer boundary. Explicit binary elimination on their 315-coordinate columns gives rank 100 over \(\mathbb F_2\), so they are linearly independent over \(\mathbb Q\). Independently, elimination on all 315 cellular boundary columns gives \(\operatorname{rank}_{\mathbb F_2}\partial_2=215\), a lower bound for the rational rank. As the 100 rationally independent cycles lie in the kernel, the rational rank is at most \(315-100=215\). Therefore it equals 215, the 100 facial product cycles form a rational basis of \(H_2\), and \(\dim H_1=300-65-215=20\). As the cubical model has no cells above dimension two, all higher rational homology vanishes. This rank argument is exhaustive over the finite chain complex; it does not infer an infinite statement from samples.

**Complete automorphism action.** A constrained adjacency-preserving enumeration finds exactly 120 automorphisms. On an oriented edge \([a,b]\), an automorphism contributes \(+1\) or \(-1\) according to the image edge orientation. On an oriented square, the sign also changes if the edge-coordinate order is reversed. Applying these rules to each of the 100 explicit \(z_{ij}\) verifies, for all 120 automorphisms and every basis element, that its image is exactly a signed image of another face-pair cycle. This gives the complete \(H_2\) representation, not merely its dimension.

The rotational \(A_5\) classes have sizes \(1,15,20,12,12\) for element orders \(1,2,3,5_A,5_B\). The following table records characters on each rotation and on its product with central inversion \(\iota\):

| Rotation order | Class size | \(\chi_{H_1}(g)\) | \(\chi_{H_1}(\iota g)\) | \(\chi_{H_2}(g)\) | \(\chi_{H_2}(\iota g)\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 20 | 0 | 100 | -10 |
| 2 | 15 | 0 | -4 | -8 | 2 |
| 3 | 20 | 2 | 0 | 1 | -1 |
| 5, first class | 12 | 0 | 0 | 0 | 0 |
| 5, second class | 12 | 0 | 0 | 0 | 0 |

The \(H_2\) traces come from the signed face-pair permutation matrix. For every group element, \(H_1\) follows from the cellular Lefschetz identity
\[
1-\chi_{H_1}(g)+\chi_{H_2}(g)=\chi_{C_0}(g)-\chi_{C_1}(g)+\chi_{C_2}(g).
\]
The verifier calculates all three cellular traces for every automorphism. After separating the central \(+\) and \(-\) sectors, inner products with the rational \(A_5\) characters \(\mathbf1=(1,1,1,1)\), \(V_4=(4,0,1,-1)\), \(V_5=(5,1,-1,0)\), and \(V_6=(6,-2,0,1)\), with rational-character squared norms \(1,1,1,2\), give exactly the decompositions in the Finding.

**Quotient consequence.** The trivial \(A_5\)-module occurs precisely once in degree one, and it lies in the central \(-\) sector; there are no trivial constituents in degree two. Rational transfer for finite group actions on a triangulated CW complex identifies quotient rational homology with invariant rational homology, proving both quotient statements.

## Verification
Run `python3 verify_icosahedron.py` in the same directory as this document. It requires only the Python standard library and prints deterministic results recorded in `verify_icosahedron_output.txt`. Its explicit combinatorial reconstruction checks all 66 vertices, 300 edges, 315 squares and their boundaries, 20 triangular faces, 100 disjoint face pairs and product cycles, both independent mod-two rank calculations, all 120 graph automorphisms, 12,000 signed cycle images, the full Lefschetz characters, central eigenspaces, rotation subgroup and irreducible multiplicities. The final line is `IRREDUCIBLE DECOMPOSITIONS VERIFIED`. These are finite exhaustive calculations with their algorithms provided, not proof by unreported numerical logs.

## Relationship to prior work
Barnett and Farber's Theorem 6.1 already gives a general *ordered* planar-graph face-torus basis for second homology; this foundational structural theorem is acknowledged and **not** claimed as new. The unordered configuration space, its full icosahedral automorphism action on both degrees, the exact ten-class rational characters, decompositions and distinct rotation/full-quotient invariants are the specific contribution. Prue and Scrimshaw supply the sufficient-subdivision equivalence used to justify the cubical model.

The closest available full equivariant two-particle computations concern the **dodecahedral** and **cuboctahedral** graphs. Their graph objects and group representations differ; although the dodecahedron has the same abstract full symmetry group, it has rational Betti vector \((1,12,36)\), not \((1,20,100)\). Icoshedral matching, neighborhood and Rips complexes concern different functors and do not imply this configuration-space result. Comparisons were made by objects, parameters and statement implications, not matching titles alone. Searches cannot exclude an unindexed equivalent calculation; absolute publication priority is not asserted.

## Limitations
The basis and decomposition are for rational homology; the calculation does not determine the integral first-homology torsion, any integral representation-lattice decomposition, cohomology ring, graph-braid group presentation or quotient homotopy type. The direct chain computation is specific to the icosahedral graph and does not classify all Platonic or five-regular graphs. Publication-priority uncertainty remains for unindexed and inaccessible literature; no independent mathematical audit has been performed.

## References
1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, first public 2009-03-12, Theorem 6.1 and Section 7.
2. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, first public 2009-09-30, Theorem 3.2.
3. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first public 2010-05-13.

