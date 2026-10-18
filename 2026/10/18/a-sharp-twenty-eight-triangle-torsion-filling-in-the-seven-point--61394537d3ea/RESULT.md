# A sharp twenty-eight-triangle torsion filling in the seven-point matching complex

## Finding
Let \(K=\mathcal M(K_7)\) be the ordinary matching complex of the complete graph on seven labelled vertices. The one-skeleton of \(K\) contains exactly \(945\) unoriented simple four-cycles. Precisely \(630\) are chordless, and each represents a generator of the order-three group \(\widetilde H_1(K;\mathbb Z)\cong\mathbb Z/3\); the other \(315\) have a chord and bound an integral two-chain of two triangles.

For any one of the \(630\) chordless four-cycles, choose a coherent integral orientation \(z\). Among **all real (and hence all integral)** simplicial two-chains \(c\) satisfying \(\partial c=3z\), the sharp \(\ell^1\)-filling norm is

\[
\min_{\partial c=3z}\sum_{\sigma\in K^{(2)}}|c_\sigma|=28.
\]

The minimum is achieved by an integral two-chain supported on exactly \(28\) distinct triangles with coefficients \(\pm1\). All \(630\) shortest essential four-cycles have the same minimum by the full label-permutation symmetry. Thus the first torsion matching complex has a complete classification of its shortest simple cycles, together with the sharp area needed to fill three times each shortest torsion cycle.

## Assumptions and scope
The seven ground vertices are \(0,1,\ldots,6\). A vertex of \(K\) is an unordered pair of distinct ground vertices, written \(ij\), and a simplex is a family of pairwise disjoint such pairs. Orient every simplex by lexicographic order of its vertices. We use nonaugmented simplicial chains with integral coefficients unless a field is specified. The \(\ell^1\) norm counts absolute coefficients of all two-simplices, **not** the number of simplices in an unrestricted topological disk diagram. A simple cycle means a cycle of four pairwise distinct vertices in the one-skeleton; reversal and cyclic shifts define the same unoriented cycle.

A canonical cycle is

\[
z=[01,34]-[01,35]-[02,34]+[02,35],
\]

where each bracket denotes the oriented one-simplex with the listed order. Under the declared lexicographic ordering every bracket is already oriented positively.

## Proof
**(1) Enumeration and orbit classification.** There are \(21\) matching-complex vertices, \(105\) edges and \(105\) triangular faces. The self-contained checker enumerates all four-cycles of the disjointness graph exactly once, canonically identifying cyclic rotations and reversals, and finds \(945\). A four-cycle using all seven ground labels has a diagonal edge (its opposite pairs of matching vertices are disjoint), and its oriented cycle is the signed sum of the boundaries of two triangular faces. There are \(315\) such cycles. All remaining four-cycles use six ground labels, have no diagonal, and are products of two two-edge stars supported on disjoint triples of ground labels. There are

\[
7\cdot \tfrac12\binom63\cdot3\cdot3=630
\]

of them: choose an omitted label, partition the remaining labels into two unordered triples, and mark one center in each triple. They constitute a single orbit under the permutation group on the seven ground labels, and each is a relabelling of \(z\), up to sign. The checker independently confirms all counts and chord tests by exhaustive iteration, so the structural count and enumeration cross-check one another.

**(2) Nontrivial order-three cycle.** The displayed \(z\) is a one-cycle. For the entire \(105\)-by-\(105\) second boundary matrix, exact elimination over \(\mathbb F_3\) gives rank \(84\). Row reduction of \(z\) modulo that column space gives a nonzero remainder, so \(z\) is not an integral boundary. The explicit two-chain below has \(\partial c=3z\); hence \(z\) has exact order three. The classical integral homology calculation identifies the full group with \(\mathbb Z/3\), so every chordless four-cycle represents a generator. Since \(K\) is flag, all simple triangles bound faces, making four the smallest length for a simple nontrivial homology cycle.

**(3) Sharp upper bound.** Let \(T\) list the \(105\) triangular faces lexicographically. The file `certificates/m7_filling.json` supplies a length-\(105\) integral vector `primal_coefficients`. The verifier reconstructs the signed matrix \(A=\partial_2\), checks \(Ac=3z\) entry-by-entry and checks that the sum of absolute coefficients is \(28\). Each of its \(28\) nonzero entries equals \(+1\) or \(-1\).

**(4) Sharp lower bound.** The same certificate supplies a length-\(105\) integer vector `dual_thirds`, defining a rational one-cochain \(y\) by dividing every entry by three. For every one of the \(105\) triangles \(\sigma\), the exact integer check verifies

\[
|\langle y,\partial\sigma\rangle|\le 1,
\qquad
\langle y,3z\rangle=28.
\]

For **every real** two-chain \(w\) satisfying \(\partial w=3z\), it follows that

\[
28=\langle y,\partial w\rangle
=\langle \delta y,w\rangle
\le\sum_\sigma|w_\sigma|.
\]

This establishes the matching lower bound without relying on a solver's optimum-status message. Relabelling ground vertices transports both primal and dual certificates to any chordless four-cycle, preserving their norms and pairing. The theorem follows.

## Verification
Run `python3 verify.py` beside the certificate directory, using only the Python standard library. It rebuilds the \(21\), \(105\), \(105\) chain modules; verifies the boundaries and rational dual constraints with exact integer arithmetic; computes the mod-three obstruction by independent column reduction; and enumerates all \(945\) simple four-cycles with exact chord tests. The expected terminal line is `VERIFY_OK 945_FOUR_CYCLES 630_TORSION_GENERATORS 315_BOUNDARIES SHARP_FILLING_28`. The certificate contains exact integer vectors rather than solver logs; neither the bound nor homological nontriviality depends on floating-point calculations.

## Relationship to prior work
Bouc's three-torsion class and the existence of a two-dimensional filling of three times a four-cycle were already known; Shareshian and Wachs reproduce an explicit surface of triangles in their Figure 1.1 and state \(\widetilde H_1(\mathcal M(K_7);\mathbb Z)\cong\mathbb Z/3\). Jonsson's exact-sequence treatment also identifies product-of-edge-differences generators. These results establish the relevant homology and existence of a filling, but the inspected passages do not prove the **minimum \(\ell^1\) filling area \(28\)** for every shortest torsion generator. The new part is the matching rational-cochain lower certificate and the complete shortest-cycle/filling classification. A known family of seven-vertex graphs with matching-complex torsion addresses which graphs have torsion, not how economically their torsion cycles fill in the complete-graph matching complex.

## Limitations
The result concerns the ordinary combinatorial chain norm on \(\mathcal M(K_7)\), not a metric area or a general asymptotic filling function. The explicit optimization concerns triples of shortest simple order-three representatives; it does not classify all optimal two-chains, nor arbitrary longer representatives of the torsion class. The theorem uses the known integral homology group only to identify a cyclic generator; the nontrivial order-three status of the displayed cycle follows independently from the supplied finite certificates. The literature check cannot guarantee absolute novelty against unindexed manuscripts.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first submitted 2004-09-03. See Figure 1.1 and Theorem 1.3. https://arxiv.org/abs/math/0409054
2. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, arXiv:1203.5641, submitted 2012-03-26, §4.1. https://arxiv.org/abs/1203.5641
3. S. Bouc, *Homologie de certains ensembles de 2-sous-groupes des groupes symétriques*, Journal of Algebra 150 (1992), 158–186, as cited and discussed by references 1–2.
