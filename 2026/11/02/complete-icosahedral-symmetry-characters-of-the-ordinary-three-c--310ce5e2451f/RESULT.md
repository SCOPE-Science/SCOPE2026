# Complete icosahedral symmetry characters of the ordinary three-cut complex

## Finding
Let \(I\) be the one-skeleton of the regular icosahedron, and let \(X=\Delta_3(I)\) be its **ordinary** three-cut complex: a set \(\sigma\) of vertices is a simplex precisely when its complement contains three vertices inducing a disconnected subgraph. The full graph automorphism group is \(G\cong A_5\times C_2\), where \(A_5\) acts by rotations and the central involution \(a\) exchanges each vertex with its opposite.

Let \(\varepsilon\) be the one-dimensional rational character of \(G\) that is trivial on \(A_5\) and has \(\varepsilon(a)=-1\). Let \(W\) be the six-dimensional rational irreducible representation of \(A_5\) whose character on its classes \((1,2,3,5A,5B)\) is \((6,-2,0,1,1)\). Its complexification is the direct sum of the two nonisomorphic three-dimensional icosahedral representations. Extend \(W\) trivially across the central \(C_2\). Then, as rational \(G\)-modules,
\[
\boxed{\widetilde H_7(X;\mathbb Q)\cong\varepsilon,\qquad \widetilde H_8(X;\mathbb Q)\cong\varepsilon\otimes_{\mathbb Q} W.}
\]
Every other reduced rational homology group vanishes. In particular, \(X/G\) is rationally acyclic, while \(X/A_5\) has precisely one reduced rational homology generator, in degree seven. The antipodal quotient \(X/\langle a\rangle\) is rationally acyclic.

## Assumptions and scope
The graph has twelve vertices and thirty edges. The exact numbered edge list is included in `verify.py` and specifies the object without reference to coordinates. A triple is disconnected if its induced graph has zero or one edge, not merely when it is independent. Thus this is **not** the total three-cut complex. Homology is reduced simplicial homology over \(\mathbb Q\); all group actions are induced by vertex permutations with the standard signs on oriented simplices. Statements about quotients concern rational homology, not contractibility or integral homology.

## Proof
**1. Homological degrees and dimensions.** There are exactly \(140\) disconnected triples. Their complements generate the complex with face counts, in dimensions zero through eight,
\[
(12,66,220,495,792,924,792,465,140).
\]
Let \(K\) be the simplicial complex of all vertex subsets containing no disconnected triple. Its face counts through dimension three are \((12,66,80,30)\), and it has no larger faces. Its integer signed boundary matrices have **exact rational ranks** \(11,49,30\) in dimensions one, two and three, respectively. Hence \(K\) has reduced rational cohomology \(\mathbb Q^6\) in degree one and \(\mathbb Q\) in degree two, and zero elsewhere. By the definition of the combinatorial Alexander dual, \(X=K^\vee\). Combinatorial Alexander duality on twelve vertices gives \(\widetilde H_j(X;\mathbb Q)\cong\widetilde H^{9-j}(K;\mathbb Q)\), so only the claimed dimensions six and one occur, in degrees eight and seven.

**2. Rotational characters.** Since \(A_5\) is perfect and \(\widetilde H_7\) is one-dimensional over \(\mathbb Q\), every rotation acts trivially on \(\widetilde H_7\). For each graph automorphism \(g\), the reduced Lefschetz number is calculated directly from all stable simplices:
\[
\widetilde L(g)=-1+\sum_{\substack{\emptyset\ne\sigma\in X\\g\sigma=\sigma}}(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma).
\]
All rotations fall into classes of orders \(1,2,3,5\), with respective element counts \((1,15,20,24)\). For the two order-five classes the following values coincide. The reduced Lefschetz numbers are \((5,-3,-1,0)\). Since \(\widetilde L=\chi_8-\chi_7\), the degree-eight rotational character equals \((6,-2,0,1,1)\). Comparison with the standard \(A_5\) character table gives \(W\): over \(\mathbb C\) it is the sum of both distinct three-dimensional irreducibles, and over \(\mathbb Q\) their Galois pair is irreducible.

**3. Central inversion.** The antipodal involution \(a\) commutes with every rotation. Because the rational \(A_5\)-module \(W\) is irreducible, the two rational eigenspaces of \(a\) on \(\widetilde H_8\) cannot both be nonzero. Thus \(a\) acts as either \(+\mathrm{id}\) or \(-\mathrm{id}\), and \(\chi_8(a)\in\{6,-6\}\). Independently, the fixed-simplex calculation gives \(\widetilde L(a)=-5\). The one-dimensional action \(\chi_7(a)\) is \(\pm1\), and \(\chi_8(a)-\chi_7(a)=-5\). The unique possibility is \(\chi_7(a)=-1\) and \(\chi_8(a)=-6\). Centrality now determines both entire \(G\)-characters, exactly as stated. As a check, the reduced Lefschetz numbers on \(a\) times a rotation of order \(1,2,3,5\) are \((-5,3,1,0)\), agreeing with the predicted character.

**4. Quotients.** After barycentric subdivision, a finite simplicial group action has quotient rational chain homology equal to the invariant part of the original rational homology. The \(A_5\)-invariant dimension of \(W\) is \((6+15(-2)+20(0)+24(1))/60=0\); the one-dimensional degree-seven module is rotationally trivial. Thus the rotation quotient has one degree-seven rational class. The central involution acts by \(-1\) on both homology representations, so its quotient and the full quotient have zero reduced rational homology.

## Verification
Running `python3 verify.py` using only the Python standard library reconstructs the complete face complexes from the displayed thirty edges, computes the Alexander-dual rational boundary ranks with exact fractions, enumerates every one of the \(120\) graph automorphisms, and reproduces all eight rotational/inversion class-trace groups using signed fixed simplices. It additionally computes boundary ranks over the prime field of characteristic \(1009\), exhibits a nonboundary degree-seven cycle, and verifies its actual transformation under all \(120\) automorphisms. The deterministic success marker is `ICOSAHEDRAL_THREE_CUT_FULL_EQUIVARIANT_EXACT_OK`. The mathematical argument uses exact rational ranks and finite character theory; the finite-field calculation is an independent corroborating check, not a replacement for rational proof.

## Relationship to prior work
Bayer and collaborators introduced ordinary cut complexes, treated many graph families, and developed equivariant calculations for complete multipartite graphs and cycles [1]. Their sequel covers disjoint unions, squared paths and grids [2]. Their separate total-cut construction uses independent triples and is a different simplicial complex [3]. A published calculation of the icosahedral ordinary three-cut complex [4] already establishes its **nonequivariant** homotopy type \(S^7\vee\bigvee^6S^8\) and the same face vector; those properties are not claimed as discoveries here. The present claim is the complete representation of the full icosahedral group on both nonzero homology degrees and the resulting distinction among natural symmetry quotients. The cited primary constructions and the prior icosahedral homotopy calculation do not imply these characters without further equivariant information.

## Limitations
This concerns exactly the twelve-vertex icosahedral graph, the ordinary three-cut complex, rational homology representations and rational homology of specified quotients. It does not claim a full integral module classification, contractibility of the rationally acyclic quotients, or a family-wide result. The originality comparison is limited to accessible primary literature, a published close nonequivariant calculation, and indexed searches; an equivalent unindexed calculation remains possible. Independent validation has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first posted 2024-07-11.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27.
4. *The icosahedral three-cut complex is a mixed-dimensional sphere wedge*, public computational mathematical record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-icosahedral-three-cut-complex-is-a-mixed-dimensional-sphere--fb104995d472 .
