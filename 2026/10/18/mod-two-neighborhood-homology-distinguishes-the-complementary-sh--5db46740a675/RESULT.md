# Mod-two neighborhood homology distinguishes the complementary Shrikhande and rook graphs

## Finding
Let \(S\) be the Shrikhande graph, and let \(R=K_4\square K_4\) be the four-by-four rook graph. Although both graphs have strongly regular parameters \((16,6,2,2)\) and the same adjacency spectrum, the reduced mod-two homology of their complementary open-neighborhood complexes is different:

\[
\widetilde H_i\bigl(\mathcal N(\overline S);\mathbb F_2\bigr)
\cong\begin{cases}\mathbb F_2^{11}&i=4,\\0&\text{otherwise,}\end{cases}
\qquad
\widetilde H_i\bigl(\mathcal N(\overline R);\mathbb F_2\bigr)
\cong\begin{cases}\mathbb F_2^2&i=2,\\\mathbb F_2&i=4,\\0&\text{otherwise.}\end{cases}
\]

In particular the rook complement produces nonzero degree-two homology, while the Shrikhande complement does not. This describes the complete reduced mod-two homology of both complexes, not their homotopy or integral homology.

## Assumptions and scope
The vertex sets are both \(V=(\mathbb Z/4\mathbb Z)^2\). Distinct vertices \((a,b)\) and \((c,d)\) are adjacent in \(S\) exactly when \((a-c,b-d)\) modulo four belongs to \(\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\); they are adjacent in \(R\) exactly when they agree in precisely one coordinate. The complement \(\overline G\) is the simple complement, with no loops. Its open neighborhood is \(N_{\overline G}(v)=V\setminus(\{v\}\cup N_G(v))\). The ordinary Lovász open-neighborhood complex \(\mathcal N(\overline G)\) comprises all nonempty subsets of one of these neighborhoods, together with the empty simplex in the augmented chain complex. Thus it is equivalently the simplicial complex of subsets that fail to dominate \(G\). The coefficient field is exactly \(\mathbb F_2\). All dimensions are ordinary simplex dimensions.

## Proof
Both graphs have sixteen vertices of degree six; direct inspection of the stated adjacency predicates gives exactly two common neighbors for any two distinct vertices, regardless of whether they are adjacent. Consequently the two graphs have the same strongly regular parameters and therefore the same adjacency eigenvalue multiplicities. Their complementary open neighborhoods are sixteen distinct nine-vertex sets, each a facet of the corresponding complex: distinct facets have equal size and thus cannot properly contain each other.

For each \(G\in\{S,R\}\), enumerate all \(2^{16}-1\) nonempty vertex subsets and retain a subset \(A\) if and only if there is a vertex \(v\) satisfying \(A\subseteq V\setminus(\{v\}\cup N_G(v))\). This equivalence both proves that the enumeration is exhaustive and characterizes every simplex without appeal to heuristics. Sort each surviving subset by its size. The resulting numbers of simplices in dimensions \(0,1,\ldots,8\) are

\[
(f_0,\ldots,f_8)_S=(16,120,528,1292,1728,1296,576,144,16),
\]
\[
(f_0,\ldots,f_8)_R=(16,120,560,1332,1728,1296,576,144,16).
\]

Use augmented simplicial chains over \(\mathbb F_2\), with \(\partial_0\) sending each vertex to the unique empty simplex. For an indexed \(d\)-face \(\{v_0,\ldots,v_d\}\), the column of \(\partial_d\) has a one in each row indexed by the codimension-one face obtained by deleting one vertex. Signs disappear over \(\mathbb F_2\). The integer-bit-vector Gaussian elimination in `check_columns.py` computes each rank exactly, by reducing every column against an echelon pivot basis. Independently, `check_rows.py` constructs the transposed matrices from a second Cayley presentation of \(S\), directly examines every vertex mask, and uses a different pivot convention. The two Shrikhande Cayley presentations are isomorphic via the invertible linear map \((x,y)\mapsto(x+y,2x+3y)\) modulo four, whose determinant is odd. Both programs verify the same ranks

\[
(r_0,\ldots,r_8)_S=(1,15,105,423,869,848,448,128,16),
\]
\[
(r_0,\ldots,r_8)_R=(1,15,105,453,879,848,448,128,16).
\]

Here \(r_d=\operatorname{rank}_{\mathbb F_2}(\partial_d)\), so \(r_0=1\) and \(r_9=0\). Since \(\partial_d\partial_{d+1}=0\), rank-nullity gives the exact identity

\[
\dim_{\mathbb F_2}\widetilde H_d=f_d-r_d-r_{d+1}.
\]

Substituting the entire displayed vectors yields respectively \((0,0,0,0,11,0,0,0,0)\) and \((0,0,2,0,1,0,0,0,0)\), proving the theorem for every degree. No statistical sampling, numerical approximation, or passage from finite tests to an infinite family occurs: both objects are fixed finite complexes, and both computations exhaust their entire chain complexes.

## Verification
Run `python3 check_columns.py` and `python3 check_rows.py` using an ordinary Python 3 interpreter. Neither program imports third-party packages or external data. Each asserts the valency and two-common-neighbor conditions, enumerates the entire complex, computes all augmented boundary ranks in exact binary arithmetic, asserts the stated vectors, and prints `PASS`. They enumerate faces by different methods and eliminate different transposed presentations; these are reproducible complete calculations, not unexplained numerical logs. To reconstruct the claimed groups use the displayed rank-nullity formula. The high-dimensional homology ranks are checked in all degrees, including the augmented degree-zero boundary.

## Relationship to prior work
Classical work on the strongly regular parameter set \((16,6,2,2)\) identifies \(S\) and \(R\) as the nonisomorphic models. Matoušek and Ziegler analyze Lovász neighborhood complexes as topological graph invariants; Kahle analyzes their random-graph behavior. Matsushita and Wakatsuki prove the general combinatorial Alexander-duality identification of \(\mathcal N(\overline G)\) with the Alexander dual of the dominance complex of \(G\); this general identity is not new here and alone does not give the displayed binary boundary ranks. Cioabă, Guo, Ji, and Mim distinguish the same two strongly regular graphs by cohomological or spectral properties of their *clique complexes*; their result concerns a different functor and does not yield the numerical mod-two homology asserted here. Rook-graph domination polynomials encode face counts of its non-dominating complex, not the ranks of its simplicial differentials. The contribution is the exact topological computation for both complementary neighborhood complexes, not a claim that these graphs had never before been distinguished.

## Limitations
These exact results concern reduced homology over \(\mathbb F_2\) only. They do not establish integral homology, absence of torsion, wedge decompositions, or full homotopy types. The statement is limited to the specified pair of sixteen-vertex graphs and does not imply a theorem for all strongly regular graphs. An equivalent calculation in unindexed literature remains possible; no absolute claim of publication priority is made.

## References
1. S. S. Shrikhande, *The uniqueness of the \(L_2\) association scheme*, Annals of Mathematical Statistics 30 (1959), 781–798, DOI `10.1214/aoms/1177706207`.
2. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first arXiv public release 2002-08-09.
3. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077.
4. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639.
5. S. M. Cioabă, F. Guo, W. Ji, and A. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871.
6. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024).
