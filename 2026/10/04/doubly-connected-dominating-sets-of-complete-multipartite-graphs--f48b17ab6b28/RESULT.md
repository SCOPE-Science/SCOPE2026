# Doubly connected dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\), partite sets \(V_1,\ldots,V_r\), and \(N=\sum_{i=1}^r n_i\). For \(D\subseteq V(G)\), put \(d_i=|D\cap V_i|\), \(d=|D|\), \(c=N-d\),
\[
p(D)=|\{i:d_i>0\}|,\qquad q(D)=|\{i:d_i<n_i\}|.
\]
Then \(D\) is a doubly connected dominating set if and only if
\[
\bigl(p(D)\ge2\ \text{or}\ (d=1\ \text{and}\ d_i=n_i=1\ \text{for some }i)\bigr)
\]
and
\[
\bigl(c=1\ \text{or}\ q(D)\ge2\bigr).
\]
Thus the complete family of doubly connected dominating sets is determined solely by the part-intersection profile.

Let
\[
P_{cc}(G;x)=\sum_{D\text{ doubly connected dominating}}x^{|D|}
\]
and let \(s=|\{i:n_i=1\}|\). Define
\[
A(x)=\sum_{i=1}^r\bigl((1+x)^{n_i}-1-n_i x\bigr),
\]
\[
B(x)=\sum_{i=1}^r\sum_{j=2}^{n_i}\binom{n_i}{j}x^{N-j},
\]
and
\[
I(x)=
\begin{cases}
x^{n_1}+x^{n_2},&r=2\text{ and }n_1,n_2\ge2,\\
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
P_{cc}(G;x)
=(1+x)^N-1-x^N-A(x)-B(x)+I(x)-(N-s)x.
\]

As a consequence,
\[
\gamma_{cc}(G)=
\begin{cases}
1,&r\ge3\text{ and }s\ge1,\\
1,&r=2\text{ and }n_1=n_2=1,\\
N-1,&r=2\text{ and exactly one part is a singleton},\\
2,&\text{otherwise}.
\end{cases}
\]
The scalar formula is included only as a consistency consequence; the all-set characterization and polynomial are the finding.

## Assumptions and scope
Graphs are finite, simple, and undirected. A doubly connected dominating set \(D\) is a dominating set for which both induced subgraphs \(G[D]\) and \(G[V(G)\setminus D]\) are connected. The empty graph is not treated as connected, while a one-vertex graph is connected. Hence every admissible \(D\) and its complement are nonempty.

The result applies to every connected complete multipartite graph, including complete graphs and complete bipartite graphs.

## Proof
For any nonempty \(X\subseteq V(G)\), the induced graph \(G[X]\) is connected exactly when either \(|X|=1\) or \(X\) meets at least two partite sets. Indeed, vertices in distinct parts are adjacent, and if at least two parts are met then any two vertices in the same part have a two-edge path through a vertex in another met part. Conversely, two or more vertices lying in one part induce an edgeless graph.

A set \(D\) dominates \(G\) exactly when either \(D\) meets at least two parts or \(D\) is an entire part. If \(D\) meets two parts, every vertex outside \(D\) is adjacent to a selected vertex in a different part. If \(D\) lies in one part \(V_i\), then an omitted vertex of \(V_i\) has no neighbor in \(D\), so domination holds precisely when \(D=V_i\).

Combining these two observations, \(D\) is simultaneously connected and dominating exactly when either \(p(D)\ge2\), or \(D\) is an entire singleton part. This is the first displayed condition. Applying the induced-connectivity observation to \(V(G)\setminus D\) gives the second condition: its size is one, or it meets at least two parts, which is precisely \(c=1\) or \(q(D)\ge2\). This proves the profile characterization.

For the polynomial, begin with all nonempty proper subsets, whose generating polynomial is \((1+x)^N-1-x^N\). A selected set is disconnected exactly when it contains at least two vertices and lies within one part; these subsets contribute \(A(x)\). A complement is disconnected exactly when at least two omitted vertices lie wholly within one part; these selected sets contribute \(B(x)\). The two bad classes intersect only when \(r=2\), both parts have size at least two, and \(D\) is exactly one whole part; inclusion-exclusion therefore restores \(I(x)\). Finally, a singleton selected from a non-singleton part is connected and has connected complement but fails to dominate; there are \(N-s\) such sets, producing the subtraction \((N-s)x\). The polynomial formula follows.

The minimum-size consequence follows directly from the profile criterion. A singleton works precisely when it is an entire singleton part and the remaining vertices induce a connected graph. This occurs for a singleton part when at least two other parts remain, and also for \(K_2\). With exactly two parts and exactly one singleton, connectedness of the complement forces all but one vertex of the other part into \(D\), giving size \(N-1\). In every remaining case, two vertices chosen from distinct parts satisfy both connectivity conditions.

## Verification
A standalone verifier exhaustively constructs every nondecreasing complete-multipartite profile of order \(2\) through \(9\). For every vertex subset it independently checks domination, connectivity of the selected induced subgraph, and connectivity of the complementary induced subgraph, then compares the result with the profile criterion and the polynomial coefficient formula.

The finite replay checks \(87\) part-size profiles and \(22{,}932\) subsets. It is a consistency check, not the proof of the infinite statement; the proof above establishes the theorem for arbitrary part sizes.

## Relationship to prior work
Cyman, Lemańska, and Raczek introduced doubly connected domination and studied general structural bounds. Their definition is the one used here.

Akhbari, Movahedi, and Arslanov later introduced the doubly connected domination polynomial and computed it for several families, with the accessible abstract specifically naming friendship graphs and cactus-chain families. The available material does not state an arbitrary complete-multipartite formula.

Ahamad, Aradais, and Laja determine the scalar doubly connected domination number of complete multipartite graphs. Their complete-multipartite theorem is therefore treated as prior coverage of the minimum-cardinality consequence. The present finding is the stronger all-set profile classification together with the exact polynomial.

## Limitations
The result is specific to complete multipartite graphs and does not assert a general graph decomposition theorem. The 2019 polynomial paper was not available in complete lawful full text during this check; its abstract and bibliographic record were inspected, so unobserved material in that paper remains a residual bibliographic risk. The 2024 complete-multipartite scalar theorem was inspected in available full text and does not state the all-set polynomial in the inspected section.

The exhaustive computation through order \(9\) supports implementation correctness only; it is not used as evidence for cases of unbounded order.

## References
1. J. Cyman, M. Lemańska, and J. Raczek, “On the doubly connected domination number of a graph,” *Central European Journal of Mathematics* 4 (2006), 34–45. DOI: 10.1007/s11533-005-0003-4.
2. M. H. Akhbari, F. Movahedi, and M. Arslanov, “On the doubly connected domination polynomial of a graph,” *Asian-European Journal of Mathematics* 12 (2019), 1950036. DOI: 10.1142/S1793557119500360.
3. S. R. Ahamad, A. A. Aradais, and L. S. Laja, “On doubly connected domination number of some special graphs,” *Advances and Applications in Discrete Mathematics* 41 (2024), 203–211. DOI: 10.17654/0974165824014.
