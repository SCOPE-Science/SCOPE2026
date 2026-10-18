# The first circles in conjugation-fixed partition-graph clique complexes

## Finding

Let \(G_n\) be the graph of integer partitions of \(n\), with edges given by transferring one unit between parts and then sorting, and let \(K_n=\operatorname{Cl}(G_n)\). Conjugation of Ferrers diagrams induces an involution \(\tau\) of \(K_n\). Define the **geometric** fixed-point space \(F_n=|K_n|^\tau\); this is not generally the clique complex of the self-conjugate vertices.

For every \(n\geq1\), \(F_n\) is canonically PL homeomorphic to a finite orbit-compatibility flag complex \(|\operatorname{Cl}(H_n)|\) described below. Complete, reproducible elementary simplicial-collapse certificates classify its homotopy type for \(1\leq n\leq22\):

\[
F_n\simeq
\begin{cases}
\mathrm{point},&n\in\{1,2,3,4,5,6,7,9,11,13\},\\
\mathrm{point}\sqcup\mathrm{point},&n\in\{8,10,12,14,15,16,17,19,21\},\\
S^1\sqcup\mathrm{point},&n\in\{18,20\},\\
(S^1\vee S^1)\sqcup\mathrm{point},&n=22.
\end{cases}
\]

In particular, \(n=18\) is the **first** parameter with \(H_1(F_n;\mathbb Z)\ne0\). The established nonequivariant homotopy theorem \(K_n\simeq\bigvee S^2\) implies the exact character identity
\[
\operatorname{tr}\bigl(\tau_*\mid\widetilde H_2(K_n;\mathbb Q)\bigr)=\chi(F_n)-1.
\]
Consequently, among \(1\leq n\leq22\), the first **negative** conjugation trace occurs at \(n=22\), where it equals \(-1\). The values for \(n>22\) are not determined here.

## Assumptions and scope

A partition \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\vdash n\) is nonincreasing, with positive parts. Two distinct partitions are adjacent in \(G_n\) if one results from decrementing one part and incrementing another, possibly new zero part, deleting zeros and sorting. The transpose Ferrers diagram defines \(\lambda'\); the published conjugation-automorphism property is used. The complex \(K_n\) is the flag complex of all cliques of this graph. Its geometric realization has barycentric-coordinate action \(\tau\), and \(F_n\) consists of **all** fixed points, including midpoints of transposed edges. The general orbit model holds for every positive integer \(n\); the homotopy table and threshold claims are restricted to the exhaustively certified interval \(1\leq n\leq22\).

Define \(H_n\) as follows. An admissible vertex is either a singleton orbit \(\{\lambda\}\) with \(\lambda=\lambda'\), or a two-element orbit \(\{\lambda,\lambda'\}\) with \(\lambda\ne\lambda'\) and \(\lambda\sim\lambda'\) in \(G_n\). Two **distinct** admissible orbits are adjacent in \(H_n\) if every cross-pair of their constituent partitions is adjacent in \(G_n\). Self-conjugate singleton vertices are known to be pairwise nonadjacent; that earlier fact is not claimed as new.

## Proof

**Orbit model (all \(n\)).** Every point of a simplex of \(K_n\) has unique nonnegative barycentric coordinates at the simplex's vertices. It is fixed by conjugation exactly when those coordinates are constant on each conjugation orbit. A nonzero orbit must lie wholly in one clique of \(G_n\): a two-vertex orbit can appear only if its two vertices are adjacent; a collection of admissible orbits can coexist exactly if all their cross-pairs are adjacent. Such orbit collections are the simplices of \(\operatorname{Cl}(H_n)\). Sending an orbit vertex to the arithmetic barycenter of its one or two original vertices and extending affinely on each simplex is a continuous bijection of finite polyhedra onto \(F_n\), hence a PL homeomorphism.

**Ferrers characterization of paired orbits (all \(n\)).** If \(\lambda\ne\lambda'\) and \(\lambda\sim\lambda'\), their Ferrers diagrams differ by removing one corner and inserting another. Their intersection \(\nu=\lambda\cap\lambda'\) has \(n-1\) boxes and is invariant under transpose; hence \(\nu\) is self-conjugate. The two differing boxes are transposes of each other and are off the diagonal, so they are two transposed addable corners of \(\nu\). Conversely, adding either of two transposed off-diagonal addable corners to any self-conjugate Ferrers diagram of size \(n-1\) yields adjacent conjugate partitions. Therefore the paired vertices of \(H_n\) are obtained exhaustively from self-conjugate partitions of size \(n-1\) in this manner.

**Complete finite collapse (\(1\leq n\leq22\)).** The attached `certificate.json` specifies for every size the complete admissible-orbit list, the complete \(f\)-vector of \(\operatorname{Cl}(H_n)\), and an ordered sequence of pairs \((\sigma,\Sigma)\). In each pair \(\sigma\) is a codimension-one face contained in the **unique** remaining coface \(\Sigma\) of higher dimension. Deleting each pair is therefore an elementary simplicial collapse. The attached verifier `verify.py` independently regenerates the partitions, neighbors, involution, admissible orbits, orbit graph, and *all* clique faces, checks that each pair really is free at its prescribed step, and recomputes the final graph's connected components and first Betti numbers. It independently recomputes mod-two boundary ranks as an additional check.

After the listed collapses, the remaining graph for every \(n\leq22\) is a forest or a wedge-of-circles graph with the following connected-component signatures \((v,\beta_1)\): one \((1,0)\) component for the ten parameters in the first case; two \((1,0)\) components for the nine parameters in the second case; \((1,0)\) and \((8,1)\) for \(n=18,20\); and \((1,0)\) and \((15,2)\) for \(n=22\). A connected graph of cycle rank \(r\) has the homotopy type \(\bigvee^{r}S^1\). Since all simplex-removing steps were verified as actual elementary collapses, these are integral homotopy equivalences, not extrapolations from finite field homology. The certificate covers every integer \(1\leq n\leq22\), proving both asserted first-occurrence thresholds within that interval.

**Ambient conjugation character.** The published partition-graph clique-complex theorem gives connected homotopy type \(K_n\simeq\bigvee^{b_n}S^2\), with no reduced rational homology in other degrees. For any finite-order simplicial map, its Lefschetz number equals the Euler characteristic of the geometric fixed-point set; this also follows directly here by subdividing invariant simplices at orbit barycenters and taking the signed permutation trace on simplicial chains. Hence \(1+\operatorname{tr}(\tau_*|\widetilde H_2)=\chi(F_n)\). The collapse table gives \(\chi(F_{22})=2-2=0\), so the trace is \(-1\). For every smaller positive \(n\), the Euler characteristic is \(1\) or \(2\), and the trace is respectively \(0\) or \(1\).

## Verification

The standalone standard-library command is `python3 verify.py certificate.json`; its complete recorded stdout is `verification_output.txt`. The program reconstructs every partition and both independent descriptions of the conjugation-paired vertices, enumerates every orbit-complex face, replays **every** recorded free-face collapse, and performs separate mod-two boundary-matrix rank calculations. It reports `ALL_CERTIFICATES_VALID` and the first-nonzero first-homology threshold at \(n=18\). In the exceptional cases its original complex face counts by dimensions are: \(n=18\): \((15,18,4)\); \(n=20\): \((20,26,7)\); \(n=22\): \((25,35,11,1)\). For \(n=22\), eleven high-dimensional elementary collapses and nine leaf collapses leave a graph with \(16\) vertices and \(16\) edges in two components, hence first Betti rank two. The verifier checks all cases, not a sample.

## Relationship to prior work

F. B. Lyudogovskiy's `arXiv:2603.14370` establishes the nonequivariant wedge-of-two-spheres theorem for \(K_n\); no part of that result is claimed here as new. His `arXiv:2603.22546` establishes that conjugation is an involutive graph automorphism, that self-conjugate vertices form an edgeless induced subgraph, and studies axial neighborhoods and spines. Those **vertex-level** facts do not classify the geometric fixed-point space, which also contains fixed midpoints and higher-dimensional barycentric faces. `arXiv:2603.26656` studies Euler characteristics of the ordinary complexes; `arXiv:2606.20773` synthesizes the ordinary topological models and raises conjugation-equivariant modeling as an open direction. The new claims are the exact all-size geometric fixed-orbit model and the complete sharp finite range of fixed-space homotopy/character thresholds. No general classification beyond \(n=22\) is asserted.

## Limitations

The list of homotopy types is proved only for \(1\leq n\leq22\); the canonical orbit model, transposed-corner description and Lefschetz identity hold for every \(n\). The finite collapse certificate is finite, exhaustive over the stated domain and independently executable, but does not imply any recurrence or stabilization for larger \(n\). The homotopy classification is integral; the ambient character assertion concerns rational homology. The literature comparison cannot rule out unindexed or unpublished equivalent findings. No independent scientific audit has been performed.

## References

1. F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, `arXiv:2603.14370` (public March 15, 2026), https://arxiv.org/abs/2603.14370.
2. F. B. Lyudogovskiy, *Axial Morphology of the Partition Graph: Self-Conjugate Axis, Spine, and Concentration*, `arXiv:2603.22546` (public March 23, 2026), https://arxiv.org/html/2603.22546v1.
3. F. B. Lyudogovskiy, partition-graph Euler-characteristic study, `arXiv:2603.26656` (public March 27, 2026), https://arxiv.org/abs/2603.26656.
4. F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs: A Conceptual Synthesis*, `arXiv:2606.20773` (public June 18, 2026), https://arxiv.org/abs/2606.20773.
