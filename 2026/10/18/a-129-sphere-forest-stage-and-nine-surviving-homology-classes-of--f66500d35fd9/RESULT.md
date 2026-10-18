# A 129-sphere forest stage and nine surviving homology classes of the four-cube

## Finding

Let \(Q_4\) be the graph on the sixteen binary four-tuples, with two tuples adjacent exactly when they differ in one coordinate. For \(d\in\{0,1,2,\ldots,\infty\}\), define the *vertex forest complex* \(\mathcal F_d(Q_4)\) to have as its simplices the subsets \(S\subseteq V(Q_4)\) for which the induced graph \(Q_4[S]\) is acyclic and has maximum degree at most \(d\); the degree restriction is omitted at \(d=\infty\).

Put \(A=\mathcal F_2(Q_4)\) and \(B=\mathcal F_\infty(Q_4)\). Then

\[
\boxed{A\simeq\bigvee^{129}S^6.}
\]

Moreover, \(\widetilde H_i(B;\mathbb Q)=0\) for \(i\ne6\), and \(\widetilde H_6(B;\mathbb Q)\cong\mathbb Q^9\). The inclusion \(A\hookrightarrow B\) induces a **surjection**

\[
\boxed{\widetilde H_6(A;\mathbb Q)\longrightarrow\widetilde H_6(B;\mathbb Q)}
\]

with a \(120\)-dimensional kernel. This is a statement about rational persistence, not an assertion of integral surjectivity.

## Assumptions and scope

The graph, vertex set, edge relation, chain orientations, coefficient rings, and the two filtration levels are as stated. The graph has no loops or multiple edges. All homology is reduced except where explicitly indicated. Each simplex is oriented by increasing vertex labels \(0,1,\ldots,15\), identifying a binary tuple with its usual integer value. The result concerns this single, canonical Cartesian product \(Q_4=K_2\square K_2\square K_2\square K_2\); no arbitrary-dimensional hypercube theorem is claimed.

## Proof

**Complete face enumeration.** For each of the \(2^{16}\) vertex subsets, test the induced degrees and acyclicity by union-find: an edge connecting vertices already in the same disjoint-set component detects a cycle. Sort the admitted vertex sets by cardinality. The resulting lists of nonempty faces, in dimensions \(0\) through \(7\), have sizes

\[
(16,120,560,1732,3552,4616,3392,922)
\]

for \(A\), and in dimensions \(0\) through \(9\),

\[
(16,120,560,1796,4080,6488,6848,4090,1008,8)
\]

for \(B\). Each also contains the empty face. An independent depth-first-search oracle reproduces the face counts. In both complexes every triple of vertices is a face: \(Q_4\) is triangle-free, and an induced graph on at most three vertices has degree at most two and no cycles.

**Integral chain calculation for \(A\).** Write the signed simplicial boundary with the usual alternating deletion of vertices in increasing order. For degrees \(1\) through \(7\), an explicit integer elimination with elementary unimodular row and column operations extracts the respective numbers of unit pivots

\[
(15,105,455,1277,2275,2341,922),
\]

and leaves a zero residual matrix in **each** degree. Because every pivot is \(+1\) or \(-1\), each boundary has only unit nonzero Smith invariant factors. In particular, its image is a primitive sublattice in the chain group in the preceding degree. The reduced augmentation has rank one. The resulting integral reduced homology is

\[
\widetilde H_i(A;\mathbb Z)=
\begin{cases}\mathbb Z^{129},&i=6,\\0,&i\ne6.\end{cases}
\]

The executable verifier reconstructs the matrices rather than trusting a list of ranks, performs all individual integer operations, tests the boundary-square identity, and checks independent binary-field ranks. All intermediate matrices and pivot choices are generated deterministically by the included source code; no inaccessible computation or hidden certificate is used.

**Homotopy conclusion.** Since \(A\) contains the full two-skeleton of the fifteen-simplex, it is simply connected. The integral homology calculation and repeated application of the Hurewicz theorem show that \(A\) is five-connected. Choose representatives of a basis for \(\pi_6(A)\cong H_6(A;\mathbb Z)\), yielding a map from a wedge of \(129\) six-spheres to \(A\). It induces an isomorphism on every integral homology group. The homology version of Whitehead's theorem for simply connected CW complexes gives the claimed homotopy equivalence.

**Terminal rational homology.** Over \(\mathbb F_2\), the boundary ranks for \(B\) in degrees \(1\) through \(9\) are

\[
(15,105,455,1341,2739,3749,3090,1000,8).
\]

Thus \(\widetilde H_i(B;\mathbb F_2)\) vanishes except in degree \(6\), where it has dimension \(9\). The complete face counts give reduced Euler characteristic \(9\). Rational Betti numbers are bounded by mod-two Betti numbers, so the rational homology is supported only in degree six. Euler characteristic then forces its dimension to be exactly \(9\).

**Inclusion.** Use Gaussian elimination over \(\mathbb F_2\) on the \(3392\) six-dimensional faces of \(A\) to produce \(1051\) independent six-cycles; the remaining \(922\) independent boundaries account for the \(129\) source classes. Embed these cycles in the six-chain group of \(B\) and reduce against the \(3090\)-dimensional space of seven-boundaries there. Precisely \(9\) independent images remain. Hence the inclusion induces a mod-two homology map of rank \(9\).

The integral homology of \(A\) is free, while \(B\) has free rank \(9\) in degree six and mod-two Betti number \(9\) in that degree. By universal coefficients, \(H_6(B;\mathbb Z)\) and \(H_5(B;\mathbb Z)\) have no two-primary torsion contributing in degree six. Reduction modulo two therefore identifies the free rank-nine part with the target mod-two homology. A rank-nine mod-two map between these free parts has rank nine over \(\mathbb Q\). Since the rational target has dimension nine, the inclusion is surjective and its rational kernel has dimension \(129-9=120\).

## Verification

Execute `python3 verify.py` and `python3 independent_check.py` from a directory containing these two included files. The programs need only the Python standard library. The first reconstructs each signed boundary, exhausts integer unit reductions, computes target mod-two ranks and the inclusion rank, and terminates with `ALL_CHECKS_PASSED`. The second independently checks acyclicity via depth-first search, and terminates with `INDEPENDENT_FACE_CHECK_PASSED`. Recorded outputs are included. All \(2^{16}\) vertex subsets are considered; these are exhaustive finite computations, not extrapolations to arbitrary graphs or cube dimensions.

## Relationship to prior work

Carnero Bravo's *The Forest Filtration of a Graph* (first public version 25 July 2023, arXiv:2307.13271) defines the complexes and establishes structural properties, graph-join calculations, categorical-product calculations, and a result for Cartesian products of a two-vertex path with an arbitrary path. Those results do not give this four-cube's \(d=2\) homotopy type or the inclusion into the unrestricted induced-forest complex. The degree-bounded induced-forest optimization literature studies maximal cardinalities, not this homology persistence map. The previously studied independence complex \(\mathcal F_0(Q_4)\) is a different filtration level and its homotopy result does not determine \(\mathcal F_2(Q_4)\). Other topological complexes on the four-cube, including graph-metric Čech, Rips, and cut complexes, have different face definitions; matching numerical ranks do not imply equal complexes or a theorem about this inclusion.

## Limitations

This establishes one specific intermediate stage, the terminal rational homology, and one rational persistence map. It does not classify the homotopy type of \(B\), determine possible odd-primary torsion in its integral homology, determine the full forest-filtration barcode, or extend the formulas to \(Q_n\) with \(n\ne4\). Originality is based on the inspected literature and overlap comparisons; an unindexed equivalent calculation remains possible. No independent mathematical audit is represented.

## References

1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first public version 2023-07-25), Sections 1, 3 and 4, especially 4.2.1 and 4.2.2. https://arxiv.org/abs/2307.13271
2. G. G. Chappell and M. J. Pelsmajer, *Maximum Induced Forests in Graphs of Bounded Treewidth*, Electron. J. Combin. 20(4), P8 (2013), DOI:10.37236/3826. https://doi.org/10.37236/3826
3. A. Hatcher, *Algebraic Topology* (standard Hurewicz, universal-coefficient and homological Whitehead theorems; textbook results cited for use, not as claims of new topology).
