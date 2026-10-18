# The sign-twisted standard homology of the six-point two-cover complex

## Finding

Let \(K=\operatorname{Cov}_{6,2}\) be the simplicial complex whose fifteen vertices are the unordered edges of the complete graph on \([6]\); an edge family is a face if its graph vertex-cover number is at most two. Relabeling the six graph vertices gives a natural \(S_6\)-action. Then

\[
\widetilde H_3(K;\mathbb Q)\cong\operatorname{sgn}\otimes\operatorname{Std}_6
\cong S^{(2,1,1,1,1)}.
\]

Here \(\operatorname{Std}_6=\{(a_1,\dots,a_6)\in\mathbb Q^6:\sum a_i=0\}\). In particular,

\[
\operatorname{tr}(g\mid\widetilde H_3(K;\mathbb Q))
=\operatorname{sgn}(g)(\#\operatorname{Fix}_{[6]}(g)-1)
\qquad(g\in S_6).
\]

Six natural Hamilton-path cycles on the five-vertex subsets span this five-dimensional module, with exactly one rational linear relation (an alternating six-term relation). This is a statement about the *third rational homology representation* in the first six-point case, not about the previously known Betti numbers, degree-four homology, or a uniform classification for larger ground sets.

## Assumptions and scope

Every graph has the fixed vertex set \([6]=\{1,2,3,4,5,6\}\). A simplex is a family \(F\) of unordered graph edges with a subset \(C\subset[6]\), \(|C|\le2\), meeting every edge of \(F\). Orient each simplicial face by the increasing lexicographic list of its graph-edge vertices; use reduced integral chains, then extend scalars to \(\mathbb Q\). All assertions concern this finite simplicial complex and the obvious vertex-permutation action of \(S_6\), not a quotient space.

For an ordered five-tuple \(T=(t_1<\cdots<t_5)\), and a permutation \(\pi\) of those five vertices, let \(e_i(\pi)=\{\pi_i,\pi_{i+1}\}\) for \(1\le i\le4\). The bracket \([e_1,e_2,e_3,e_4]\) denotes the oriented three-simplex in *path-edge order*, converted to the standard increasing-edge orientation with the appropriate sign. Define the integral three-chain

\[
z_T=\tfrac12\sum_{\pi\in S_T}\operatorname{sgn}_T(\pi)
[e_1(\pi),e_2(\pi),e_3(\pi),e_4(\pi)].
\]

The two-vertex cover of any four-edge spanning path is given by its second and fourth path vertices, so each summand is a face. The half-integer-looking normalization is integral: reversing a path produces the same ordered oriented three-simplex with the same signed coefficient, hence each distinct simplex coefficient is even before division by two. Write \(T_i=[6]\setminus\{i\}\) with its induced increasing order.

## Proof

**Finite chain reduction.** Enumerate, for each pair \(\{a,b\}\subset[6]\), all subsets of the nine graph edges incident to \(a\) or \(b\). Deduplicating gives exactly \(5{,}142\) faces including the empty face; the numbers of nonempty faces in dimensions zero through eight are

\[
(15,105,440,1125,1566,1200,540,135,15).
\]

The accompanying verifier implements an elementary lexicographic vertex-toggle matching on the *augmented* face poset: at each graph-edge vertex, pair every still-unmatched lower face not containing that vertex with its upper face obtained by adding it, whenever both remain. The program enumerates **all** oriented codimension-one face incidences and checks that reversing matched incidences produces an acyclic directed graph by an exhaustive topological sort. It finds exactly \(2{,}561\) matching pairs and exactly twenty critical cells: five in dimension three and fifteen in dimension four. Standard acyclic Morse reduction therefore supplies a chain complex with no generators in any other degree and with the indicated critical generators. The augmented matching is used only to compute reduced homology.

**Exact cycle images.** The verifier independently computes the simplicial boundary of each of the six chains \(z_{T_i}\) and checks coefficient-by-coefficient that it is zero. To project an oriented face into the critical Morse chain group, replace a paired lower face \(f\), paired with \(u\), by the exact signed identity obtained from \(\partial u=0\) modulo its paired incidence; a paired upper face projects to zero and a critical face to itself. Every paired incidence coefficient is \(\pm1\), so recursion uses exact integers. The acyclicity check guarantees that these replacements terminate and define the integral Morse projection. In a suitable ordering of critical three-cells, the images of the six five-subset cycles are

\[
-12\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1\\
1&-1&1&-1&1
\end{pmatrix}.
\]

Thus their images have rank five, and their only rational linear relation is

\[
\sum_{i=1}^6(-1)^{i-1}[z_{T_i}]=0.
\]

For an independent check of the Morse boundary, consider each four-subset \(U\subset[6]\): among the six graph edges within \(U\), the five-element subsets form simplices, while the full six-edge set does not (its minimum vertex cover has size three). Hence the oriented boundary of the formal five-simplex on those six edge vertices gives a four-cycle in \(K\). The verifier projects these fifteen four-cycles to the fifteen critical degree-four generators; the resulting integer \(15\times15\) matrix has determinant \(-1\). Since the images of cycles span the entire degree-four Morse chain group, the Morse differential from degree four to degree three is zero. Therefore \(\widetilde H_3(K;\mathbb Q)\) has dimension exactly five, and the five-subset cycles exhaust it.

**The symmetry module.** The alternating path sum is natural under graph-vertex relabeling: for \(g\in S_6\), \(g_*z_T\) is the sign of the induced ordering permutation of \(T\) times \(z_{gT}\). Thus the assignment \(t_1\wedge\cdots\wedge t_5\mapsto[z_T]\), with ordered ground-set basis vectors, defines an \(S_6\)-equivariant surjection

\[
\bigwedge{}^5\mathbb Q^6\longrightarrow\widetilde H_3(K;\mathbb Q).
\]

By the exact rank-five image calculation, its kernel is the sign line generated by the alternating deletion from \(1\wedge2\wedge\cdots\wedge6\). Since \(\bigwedge^5\mathbb Q^6\cong\operatorname{sgn}\otimes\mathbb Q^6\) and the deleted-vector line corresponds to \(\operatorname{sgn}\) times the constant vector, the quotient is \(\operatorname{sgn}\otimes\operatorname{Std}_6\), as claimed. The trace formula follows from the usual permutation character on six points.

## Verification

Run `python3 verify.py` with Python 3 (standard library only). The program exhaustively constructs all faces, recomputes the lexicographic toggle matching, proves its acyclicity on the complete directed Hasse diagram, and checks reduced Morse critical counts. It reconstructs the six alternating Hamilton-path cycles, confirms their signed boundaries vanish, checks the displayed six-by-five integer image matrix and one relation, and computes the fifteen-by-fifteen four-cycle image determinant via exact Bareiss elimination. It also enumerates all eleven conjugacy classes of \(S_6\), computes the reduced Lefschetz number by fixed-face orbit counting, and independently verifies

\[
\operatorname{tr}_{H_3}(g)=\operatorname{tr}_{H_4}(g)-\widetilde L(g)
=\operatorname{sgn}(g)(\#\operatorname{Fix}(g)-1).
\]

It also verifies the five generating adjacent transpositions on all six Hamilton-path cycles, giving thirty exact chain-level equivariance tests. The check ends with `VERIFY_OK`. These are exhaustive finite certificates for exactly six ground vertices, not extrapolations to larger complexes. The acyclic matching's chain equivalence and the abstract exterior-power identity supply the logical connection from the checked integers to the representation theorem.

## Relationship to prior work

Jonsson [1] established the integral homology ranks of covering-number-two complexes, including the degrees three and four; these ranks are **not** claimed as new. Biswas [2] recognized the two-subset covering complex as a finite-set Čech complex and investigated its nonequivariant homotopy type, including this six-point case. A published equivariant calculation [3] gives the complete rational \(S_m\)-action **in degree four**, using the four-subset sphere cycles. That result explicitly leaves the degree-three representation and its generators unresolved. Neither the known nonequivariant ranks nor the degree-four permutation module implies the sign-twisted degree-three module found here. An equivariant homology calculation for the *Kneser graph* on two-subsets concerns a different simplicial complex; shared symmetric-group action or a fifteen-vertex count does not make its theorem applicable [4].

## Limitations

The asserted module is over \(\mathbb Q\), for precisely \(m=6\); the displayed cycles need not be an integral basis, and no result for \(m\ge7\), an equivariant homotopy splitting, or the homology of a different Čech model is asserted. The 2005 covering-number source was accessible as a full publisher abstract and searchable indexed author-preprint excerpt, but its full source PDF could not be obtained for a page-by-page comparison; the indexed author-preprint location returned a not-found response and institutional retrieval was unavailable. A hidden equivariant theorem in that full text or another unindexed source remains a named originality risk. Computational conclusions rest on the attached complete deterministic program; they were not inferred from finite sampling.

## References

[1] Jakob Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM Journal on Discrete Mathematics 19 (2005), 633–650, DOI 10.1137/S0895480104443680.

[2] Anamitro Biswas, *Čech complexes for finite sets*, arXiv:2609.32786v1 (first posted 2026-09-26), especially the covering-complex construction and final examples.

[3] *Four-subset sphere cycles give the rational top-homology permutation character of covering complexes*, research record `2026/10/11/SCOPE-four-subset-sphere-cycles-give-the-rational-top-homology-permuta--d06d65e27c16`, full `RESULT.md`.

[4] *The scale-two Čech complex of \(KG(6,2)\): 64 spheres and a multiplicity-free \(S_6\)-character*, research record `2026/10/11/SCOPE-the-scale-two-ech-complex-of-kg-6-2-64-spheres-and-a-multiplicit--a413c6a778e4`.
