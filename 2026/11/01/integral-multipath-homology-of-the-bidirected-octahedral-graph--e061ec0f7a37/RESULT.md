# Integral multipath homology of the bidirected octahedral graph

## Finding
Let \(O=K_{2,2,2}\) be the six-vertex octahedral graph. Replace each undirected edge with both directed arcs to obtain \(D=\overleftrightarrow O\). Let \(X(D)\) be the simplicial complex whose vertices are the 24 arcs of \(D\), with a simplex for each set of arcs forming a disjoint union of directed paths (isolated vertices are allowed in the underlying digraph). Then the complete reduced integral homology is
\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,&i=2,\\
\mathbb Z^{92},&i=3,\\
\mathbb Z^{32},&i=4,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, every integral homology group is torsion-free. This is a claim about homology, not a sphere-wedge homotopy equivalence.

## Assumptions and scope
Label vertices \(0,1,2,3,4,5\) and set the three antipodal pairs to \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5\}\). Every ordered pair of distinct vertices from different antipodal pairs is an arc; there are 24 such arcs. An admissible arc set has indegree and outdegree at most one at every vertex and contains no directed cycle. These are exactly the finite directed forests in which every component is a directed simple path. We take the ordinary geometric realization of the resulting abstract simplicial complex and augmented reduced simplicial homology with integer coefficients. No graph automorphism quotient is taken.

## Proof
**Exhaustive and independent face constructions.** Each multipath has at most five arcs: on six vertices, six arcs under the degree constraints would contain a directed cycle. Therefore all possible simplices are covered by arc subsets of sizes one through five. The standalone verifier enumerates these subsets, checks the in-/out-degree and directed-cycle conditions, and independently enumerates all \(5^6=15625\) outgoing-choice configurations (each of six vertices has four available outward arcs or no outward arc). It tests incoming uniqueness and absence of undirected cycles by an independent union-find algorithm. The two methods produce identical face sets. The resulting numbers of nonempty faces in dimensions \(0,1,2,3,4\) are
\[
(f_0,f_1,f_2,f_3,f_4)=(24,192,616,744,240).
\]
There are no faces in other nonnegative dimensions.

**Explicit acyclic matching.** List the 24 arcs in lexicographic order. Repeatedly pair any currently unpaired simplex \(\sigma\) not containing the pivot arc with \(\sigma\cup\{a\}\) whenever both are unpaired, advancing through the pivots. The included Python verifier fully specifies the enumeration and deterministic order. Exactly 835 pairs are formed, leaving 1 critical vertex, no critical 1-cells, 12 critical 2-cells, 101 critical 3-cells and 32 critical 4-cells. Reverse the 835 matched cover relations in the Hasse diagram of the full nonempty face poset. A complete topological sort on its 1,816 nodes and 6,408 cover incidences succeeds, certifying that the matching is acyclic. Acyclic-matching cancellation is an integral chain-homotopy equivalence.

**Integral cancellation, differential, and Smith factors.** With each simplex oriented by its ascending arc-index order, the verifier constructs its signed integral boundary. It performs 835 elementary unit Schur-complement cancellations in the Morse pairs, requiring the incidence coefficient to be \(+1\) or \(-1\) at every cancellation. The remaining chain dimensions are \((1,0,12,101,32)\) in degrees \(0\) through \(4\). Its only potentially nonzero boundary is a \(12\times101\) matrix in degree \(3\to2\), with 257 nonzero integer entries; the other remaining positive-degree boundaries vanish identically. Exact integer row/column operations exhibit nine unit pivots, with an entirely zero residual matrix. Thus the integer differential is equivalent to nine diagonal ones and zeros, so its kernel and cokernel are free and the three displayed reduced Betti numbers follow: \(12-9=3\), \(101-9=92\), and \(32\).

**Independent simplicial boundary cross-check.** A separate direct mod-two reduction, using all original simplices instead of the Morse-reduced chain complex, gives ranks \((23,169,444,208)\) for boundaries in degrees one through four. It independently reproduces reduced mod-two Betti ranks \((3,92,32)\) in degrees two through four. The simplicial Euler characteristic is \(-56\), hence reduced Euler characteristic \(-57=3-92+32\).

## Verification
Run `python3 verify_octahedral_multipath.py` under Python 3.10 or newer. No third-party Python packages are used. The program deterministically regenerates every face, all Morse pairs, the signed cancellation matrices, integer pivots and the independent mod-two homology ranks. The accompanying `verification_stdout.txt` contains output from an actual successful run; the standalone program is the reproducible evidence, and the output alone is not a proof. The program terminates with `OCTAHEDRAL_MULTIPATH_INTEGRAL_HOMOLOGY_VERIFIED` only after all assertions pass.

## Relationship to prior work
Caputi, Collari and Di Trani introduced the path-poset/multipath-complex viewpoint and its computational framework in their 2021 preprint [1]. Caputi, Collari, Di Trani and Smith classify several directed path, polygonal, grid and transitive-tournament cases [2], but their calculations do not cover this fully bidirected tripartite octahedral graph. In the terminology of Vrećica and Živaljević [3], the present complex is an **induced subcomplex** of the six-by-six cycle-free chessboard complex: remove the six rook vertices corresponding to the two orientations of each of the three antipodal nonedges. The connectivity results for the unrestricted cycle-free chessboard complex do not determine the integral homology of this deletion.

A previously recorded general result gives the top reduced integral homology of any loopless digraph's multipath complex as freely generated by directed Hamiltonian cycles. For this octahedral digraph it already predicts the top-degree rank \(32\). **Accordingly, the top-degree rank is not claimed as new in isolation.** The contribution here is the complete lower-degree integral computation, including ranks \(3\) and \(92\), and proof of absence of torsion. Existing complete bipartite, double-star, and transitive-tournament cases do not imply these lower groups. The newer work on bidirectional paths and polygons [4] concerns different underlying graphs.

## Limitations
The theorem is finite and applies only to this specifically defined 24-arc digraph. It does not prove a general formula for tripartite graphs, an integral homotopy decomposition, a cup-product structure, or symmetry characters. An equivalent result under the cycle-free-chessboard terminology might exist outside indexed records. The integer-chain proof relies on fully exhaustive, reproducible computation (including unit matrix operations); numerical Betti numbers alone would not establish torsion-freeness.

## References
[1] L. Caputi, C. Collari, S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206, first public October 21, 2021. https://arxiv.org/abs/2110.11206

[2] L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first public August 9, 2022. https://arxiv.org/abs/2208.04656

[3] S. Vrećica, R. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, first public October 27, 2007. https://arxiv.org/abs/0710.5252

[4] L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, 2026. https://arxiv.org/abs/2601.05670
