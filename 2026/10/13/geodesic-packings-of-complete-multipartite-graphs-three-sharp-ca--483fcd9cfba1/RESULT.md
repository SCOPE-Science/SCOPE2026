# Geodesic packings of complete multipartite graphs: three sharp capacity constraints

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\) and positive integer part sizes \(n_i\). Put
\[
N=\sum_{i=1}^r n_i,\qquad M=\max_i n_i,\qquad
P=\sum_{i=1}^r\left\lfloor\frac{n_i}{2}\right\rfloor,\qquad
s=|\{i:n_i=1\}|.
\]
A geodesic packing is a family of pairwise vertex-disjoint maximal shortest paths; its maximum cardinality is \(\operatorname{gpack}(G)\).

If \(M=1\), then \(G\) is complete and \(\operatorname{gpack}(G)=\lfloor N/2\rfloor\). If \(M\ge2\), then
\[
\boxed{\operatorname{gpack}(G)=
\max_{0\le e\le\lfloor s/2\rfloor}
\min\left\{
\left\lfloor\frac{N+e}{3}\right\rfloor,
N-M-e,
P+e\right\}.}
\]
More precisely, for every integer \(e\) between zero and \(\lfloor s/2\rfloor\), a packing with exactly \(e\) two-vertex maximal geodesics and exactly \(t\) three-vertex maximal geodesics exists **if and only if**
\[
0\le t\le
\min\left\{
\left\lfloor\frac{N-2e}{3}\right\rfloor,
N-M-2e,
P\right\}.
\]
Thus three transparent capacity bounds are jointly sufficient, not merely necessary. The formula gives a polynomial-time optimum and an explicit construction via bipartite matching.

## Assumptions and scope
The graph is finite, undirected, simple, connected, and complete multipartite, with at least two nonempty partite classes. Paths are counted as vertex sets with consecutive adjacency, and a *maximal geodesic* cannot be extended as a subpath of a longer shortest path. The theorem includes stars, all complete bipartite graphs, complete graphs, and arbitrary unequal class sizes with singleton parts. It makes no claim for arbitrary non-multipartite graphs or for edge-disjoint rather than vertex-disjoint packings.

## Proof
**1. The maximal paths.** For \(M\ge2\), the graph has diameter two. Every distance-two geodesic has endpoints in one part and its middle vertex in a different part, and is automatically maximal. An edge joining two singleton-part vertices cannot be extended into a distance-two geodesic, so it is maximal. Every other edge meets a part of size at least two and extends to a distance-two geodesic through its opposite endpoint. Hence maximal geodesics have precisely these two forms. If \(M=1\), all edges are maximal geodesics in the complete graph and a maximum matching supplies \(\lfloor N/2\rfloor\) paths.

**2. Necessity with a prescribed number of edges.** Fix \(M\ge2\). Any \(e\) pairwise disjoint two-vertex maximal geodesics consume \(2e\) distinct singleton vertices. They are possible only if \(0\le e\le\lfloor s/2\rfloor\). After choosing them, the remaining part sizes \(a_i\) have total \(Q=N-2e\), largest part \(M\), and the same pair capacity \(P=\sum_i\lfloor a_i/2\rfloor\). Every remaining three-vertex geodesic uses three vertices, at least one vertex outside a largest part, and a pair from one part. Thus its disjoint packing size \(t\) satisfies
\[
t\le\left\lfloor\frac Q3\right\rfloor,
\qquad t\le Q-M,\qquad t\le P.
\]

**3. Sharp triple-packing lemma.** Consider any nonnegative integer class sizes \(a_1,\ldots,a_r\) with sum \(Q\), and fix an integer \(t\ge0\) satisfying
\[
3t\le Q,\qquad t\le Q-\max_i a_i,\qquad
 t\le\sum_i\lfloor a_i/2\rfloor.
\]
We construct \(t\) vertex-disjoint triples with two endpoints in one class and one middle vertex in a different class. The case \(t=0\) is immediate. Set \(R=Q-2t\), and put \(L_i=\max\{0,a_i-R\}\). We claim there exist integers \(p_i\) with
\[
L_i\le p_i\le\left\lfloor\frac{a_i}{2}\right\rfloor,
\qquad \sum_i p_i=t.
\]
To see this, first \(R\ge\lceil Q/3\rceil\). If \(a_i\le2Q/3\), then \(\lceil a_i/2\rceil\le R\) and hence \(L_i\le\lfloor a_i/2\rfloor\). If \(a_i>2Q/3\), then \(b_i=Q-a_i<a_i/2\). Since \(t\le b_i\), we have \(R=Q-2t\ge a_i-b_i>a_i/2\), yielding the same conclusion.

At most two indices have \(L_i>0\), since \(R\ge Q/3\). If exactly one index \(i\) has positive lower bound, then \(L_i=2t-(Q-a_i)\le t\). If two indices \(i,j\) do, then
\[
L_i+L_j=a_i+a_j-2Q+4t\le4t-Q\le t.
\]
Thus \(\sum_i L_i\le t\); the assumed pair-capacity bound gives \(\sum_i\lfloor a_i/2\rfloor\ge t\). Filling integers between these lower and upper bounds supplies the required \(p_i\).

Choose \(p_i\) disjoint vertex-pairs from class \(i\), giving \(t\) pair-tokens. Exactly \(R\ge t\) unpaired vertices remain. Match each pair-token to a different unpaired vertex of another class. In the associated bipartite incidence graph, a set of tokens of at least two different classes has *every* unpaired vertex as a neighbor. A set consisting of tokens only from class \(i\) has \(R-(a_i-2p_i)\ge p_i\) neighbors, by \(p_i\ge L_i\). Hall's theorem therefore gives a matching saturating all pair-tokens. Its matched vertices are the centers of the desired \(t\) geodesics. This proves sufficiency for every allowed \(t\).

**4. Optimization.** Apply the lemma to the \(e\) chosen disjoint edges between singleton parts. For this fixed \(e\), the maximum total number of paths is
\[
e+\min\left\{\left\lfloor\frac{N-2e}{3}\right\rfloor,
N-M-2e,P\right\}
=\min\left\{\left\lfloor\frac{N+e}{3}\right\rfloor,
N-M-e,P+e\right\}.
\]
Optimizing over the finite integer range of \(e\) completes both statements.

## Verification
A standalone standard-library Python program, `verifier.py`, independently builds graph adjacency, enumerates every maximal geodesic of all complete multipartite graphs on \(2\) through \(13\) vertices, and computes the true optimum by exact subset dynamic programming. It checks all \(359\) such integer partitions, traversing \(116315\) memoized DP states and enumerating \(30412\) candidate geodesic paths across those instances. Separately, it constructs matching witnesses for all these inputs and for \(990\) reproducible larger random instances with up to \(34\) parts. Six boundary cases are checked. Run `python3 verifier.py` without dependencies. `verification_output.txt` contains the expected program output. These finite experiments are corroboration; the Hall-based argument proves the infinite family.

## Relationship to prior work
Manuel, Brešar and Klavžar introduced the geodesic-packing invariant and established its NP-completeness, including the complete-graph value \(\lfloor N/2\rfloor\) and the balanced complete-bipartite value \(\lfloor2n/3\rfloor\) (arXiv:2210.15325, Section 2). These special cases are not claimed as new. Their paper treats trees, rook graphs in the transversal discussion, and strong products of paths but does not give the heterogeneous complete-multipartite optimum or the exact joint edge/triple feasibility constraints. Their earlier geodesic-transversal paper (arXiv:2101.08042) studies a distinct hitting-set invariant. Boats and Kikas, *Complete Multipartite Graphs are Pansophical* (2019), study expected routing performance for assigned disjoint-path demands rather than vertex-disjoint inclusion-maximal shortest paths. Broere, Jonck and Voigt (1996) determine the **minimum number of induced paths needed to partition all vertices** of a complete multipartite graph, a different optimization. That single minimum-cover statistic does not determine the maximum number of disjoint maximal geodesics: both \(K_{2,1,1,1,1,1}\) and \(K_{3,3,1}\) have seven vertices and induced-path partition number three, but geodesic-packing numbers three and two respectively. Full text of the 1996 work was not retrieved; its publisher abstract and scholarly metadata were compared. The contribution here is the all-part-size mixed-geodesic packing and its sharp three-capacity characterization.

## Limitations
The result does not enumerate all optimal packings, and does not prove an analogous formula for arbitrary graph classes. The verifier explores only finite inputs. Literature searches cannot exclude an equivalent formula stated in older induced-path packing terminology, and independent validation has not been performed.

## References
1. P. Manuel, B. Brešar and S. Klavžar, *Geodesic packing in graphs*, 2022 preprint, arXiv:2210.15325, https://arxiv.org/abs/2210.15325; published *Applied Mathematics and Computation* **459** (2023), 128277.
2. P. Manuel, B. Brešar and S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042, https://arxiv.org/abs/2101.08042; published *Applied Mathematics and Computation* **413** (2022), 126621.
3. J. Boats and L. Kikas, *Complete Multipartite Graphs are Pansophical*, *Congressus Numerantium* **233** (2019), 21–30, https://combinatorialpress.com/cn-articles/volume-233/complete-multipartite-graphs-are-pansophical/.
4. I. Broere, E. Jonck and M. Voigt, *The induced path number of a complete multipartite graph*, *Tatra Mountains Mathematical Publications* **9** (1996), 83–88, https://www.sav.sk/?doc=journal-list&journal_article_no=1259&lang=en&part=article_response_page.
