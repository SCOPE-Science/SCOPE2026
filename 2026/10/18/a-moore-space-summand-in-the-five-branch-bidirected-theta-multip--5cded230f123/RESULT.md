# A Moore-space summand in the five-branch bidirected theta multipath complex

## Finding
Let \(D=\overleftrightarrow{K}_{2,5}\) have two hubs and five other vertices, with both directed arcs on every hub–leaf edge. The multipath complex \(X(D)\), whose simplices are arc sets forming disjoint directed simple paths, has integral homotopy type
\[
X(D)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{31}S^3.
\]
Here \(M(\mathbb Z/2\mathbb Z,2)\) is the Moore space obtained by attaching a three-cell to \(S^2\) by a degree-two map. In particular,
\[
\widetilde H_j(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&j=2,\\
\mathbb Z^{31},&j=3,\\
0,&\text{otherwise}.
\end{cases}
\]
This is a complete integral *homotopy* calculation for the specified digraph, not only a field-homology computation.

## Assumptions and scope
Vertices are \(0,1,2,3,4,5,6\), with hubs \(0,1\). The arc indices, in this precise order for leaf \(i=2,3,4,5,6\), are \((0,i),(i,0),(1,i),(i,1)\). The twenty arc indices constitute the vertex set of the abstract simplicial complex. An allowed arc set has indegree and outdegree at most one at every graph vertex and has no directed cycle, including cycles of lengths two and four. Isolated graph vertices are allowed. Simplicial chains use oriented faces whose arc indices increase; homology is reduced and integral unless specified.

Because each of the two hubs supports at most one outgoing and one incoming selected arc, every simplex has at most four vertices. Consequently the complex has dimension three, and exhaustive enumeration over cardinalities zero through four is exhaustive, rather than a bounded approximation.

## Proof
**1. Complete face enumeration.** Enumeration with the above degree and directed-cycle criteria gives exactly one empty face, \(20\) vertices, \(130\) edges, \(320\) triangles and \(240\) tetrahedra. A second construction independently generates all directed *simple paths* and all unions of vertex-disjoint such paths. It produces the identical \(711\)-element family including the empty face. The reduced Euler characteristic is therefore \(-1+20-130+320-240=-31\).

**2. Acyclic discrete-Morse matching.** Encode an arc subset by its twenty-bit integer mask. Initially all \(710\) nonempty faces are unmatched. For each arc index in increasing order, traverse the remaining masks in increasing integer order and match every available pair \((\tau,\tau\cup\{e\})\), deleting both from the unmatched set. This deterministic procedure produces \(297\) matched covering pairs. Exactly one critical zero-cell, one critical one-cell, \(42\) critical two-cells and \(72\) critical three-cells remain. Reverse each matched covering arrow and direct every other Hasse covering arrow upward. Exhaustive topological sorting of the resulting \(710\)-vertex, \(2180\)-edge directed graph visits all \(710\) vertices, verifying acyclicity and thus the applicability of discrete Morse theory.

**3. Integral Morse differentials.** The sign of deleting the \(j\)-th arc in increasing order is \((-1)^j\). For a matched lower face \(\tau\) and upper face \(\sigma\), the canonical projection of \(\tau\) into the critical chain group is calculated by eliminating the unit coefficient \([\sigma:\tau]\):
\[
P(\tau)=-[\sigma:\tau]^{-1}\sum_{\eta\subset\sigma,\,\eta\ne\tau}[\sigma:\eta]P(\eta).
\]
Matched upper faces project to zero, and critical faces project to themselves. The acyclic matching guarantees termination of the recursion. Applying this to all boundaries of critical cells gives integral matrices of sizes \(1\times1\), \(1\times42\), and \(42\times72\). The first vanishes; the second has \(24\) nonzero entries and Smith factor \(1\); the third has \(252\) nonzero entries and Smith factors \(1\) repeated forty times, \(2\) once and \(0\) once. The exact matrix product of the last two differentials vanishes. A separate elementary integral unit-pivot reduction removes forty pivots from the third matrix and leaves a rank-one residual row with entry-gcd \(2\), independently corroborating the nonunit Smith invariant. All data are recomputed by the attached programs, with fixed SHA-256 digests of the signed sparse matrices in their output.

**4. Upgrade from chains to homotopy.** The CW complex obtained from the acyclic matching has one zero-cell and one one-cell. Since an attaching map of a two-cell has degree \(\pm1\) on that one-cell, the fundamental group is trivial. Cancelling this one/two-cell pair gives a simply connected two-skeleton homotopy equivalent to a wedge of \(41\) two-spheres. The Hurewicz map \(\pi_2\to H_2\) of this two-skeleton is an isomorphism, so the attaching maps of the \(72\) three-cells are *completely* determined by the integral matrix from Step 3, restricted to the kernel of the second differential. Integer changes of basis on a wedge of two-spheres are realized by homotopy equivalences, while integer column operations correspond to changing the basis of three-cell attachments. The forty unit factors cancel forty pairs of two- and three-cells; the remaining degree-two attaching map yields \(M(\mathbb Z/2\mathbb Z,2)\), and the other thirty-one three-cells attach trivially. This proves the stated homotopy decomposition.

## Verification
Run `python VERIFY.py` and `python REDUCTION.py` with Python 3.10+ and SymPy 1.12+ in the directory containing these files. The archived `REPLAY_OUTPUT.txt` is the complete recorded output. The first program performs two independent complete face enumerations, checks the matching, sorts the full oriented Hasse graph, constructs exact signed Morse matrices, verifies their chain condition, and computes their integer Smith forms. The second independently reduces the last Morse matrix by forty elementary unit pivots and checks that the remaining nonzero row has gcd two. Rebuilding the claimed numerical data requires no external tables or opaque certificates. The finite enumeration is exhaustive here because the four-arc upper bound is proved above.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith's 2022 investigation defines the multipath complex, develops dynamical-region methods, computes one-way complete-bipartite Euler characteristics and addresses other graph families. It does not provide the integral homotopy type of this bidirected \(K_{2,5}\) complex. The earlier path-poset paper handles mainly directed paths and realization problems. The 2007 cycle-free chessboard work studies the complete directed-graph complex and its connectivity; a theorem for that ambient complex does not determine the homotopy of this prescribed-arc subcomplex. The 2024 quiver-minor paper establishes finite-generation/torsion bounds and an acyclic-digraph matching-complex comparison, rather than an exact bidirected \(K_{2,5}\) calculation.

Related calculations for the three- and four-branch bidirected theta digraphs concern different sizes: the four-branch case has degree-two torsion but no free degree-three homology, while the present five-branch complex has both kinds of nonzero groups. Neither smaller-size statement entails the new degree-three multiplicity or Moore-space splitting. Literature and database searches found no equivalent result, but unindexed equivalent work remains possible.

## Limitations
The theorem applies exactly to the specified seven-vertex bidirected digraph, not to every bidirected complete bipartite graph. The proof is complete for this finite object, with exact integer arithmetic; it makes no claim about stabilization or torsion disappearance for larger numbers of branches. The bibliographic searches do not prove absolute novelty.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first public 2022-08-09), §§1–5. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, arXiv:2110.11206, §§1, 5–6. https://arxiv.org/abs/2110.11206
3. L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248 (first public 2024-01-02), §4. https://arxiv.org/abs/2401.01248
4. S. T. Vrećica, R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, §§1–4. https://arxiv.org/abs/0710.5252
