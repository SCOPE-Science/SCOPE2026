# Edge general position sets of half graphs via Mantel's theorem
## Finding
For every integer \(n\ge2\), let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]
Then
\[
\operatorname{gp}_{e}(H_n)=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
\]

There is also a complete classification of the maximum sets. Map
\[
a_i b_j\longmapsto \{i,j+1\}
\]
from \(E(H_n)\) to the edges of the complete graph on the ordered vertex set \(\{1,\ldots,n+1\}\). A maximum edge general-position set is exactly the inverse image of the complete bipartite graph determined by a balanced bipartition of \(\{1,\ldots,n+1\}\) whose binary membership string has at most three runs.

Hence the exact number of maximum edge general-position sets is
\[
\begin{cases}
n+1,&n\text{ even},\\[3pt]
\dfrac{n+1}{2},&n\text{ odd}.
\end{cases}
\]

## Assumptions and scope
A set \(S\subseteq E(G)\) is in edge general position when no geodesic of \(G\) contains three edges of \(S\). The maximum cardinality of such a set is the edge general position number \(\operatorname{gp}_{e}(G)\).

The half graph convention used here has \(a_i b_j\) as an edge exactly when \(i\le j\). Relabeling the two nested sides reverses the usual alternative convention without changing the statement.

## Proof
Every edge of \(H_n\) has a unique index pair
\[
(i,j),\qquad 1\le i\le j\le n.
\]
Define a bijection
\[
\Phi:E(H_n)\longrightarrow E(K_{n+1}),\qquad
\Phi(a_i b_j)=\{i,j+1\}.
\tag{1}
\]

First we prove the upper bound. Let \(S\) be an edge general-position set and suppose that \(\Phi(S)\) contained a triangle on
\[
p<q<r.
\]
The three corresponding half-graph edges are
\[
a_p b_{q-1},\qquad a_p b_{r-1},\qquad a_q b_{r-1}.
\]
They occur consecutively on the path
\[
b_{q-1}-a_p-b_{r-1}-a_q.
\]
Because \(q>q-1\), the endpoints \(b_{q-1}\) and \(a_q\) are nonadjacent. They lie in opposite bipartition classes, so their distance is odd; the displayed path has length three, hence is a geodesic. This contradicts edge general position. Therefore \(\Phi(S)\) is triangle-free.

Mantel's theorem now gives
\[
|S|=|\Phi(S)|\le
\left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
\tag{2}
\]

For sharpness, take a balanced bipartition
\[
P\cup Q=\{1,\ldots,n+1\}
\]
whose membership string has at most three runs, and let \(S(P,Q)\) be the inverse image under \(\Phi\) of all crossing pairs between \(P\) and \(Q\). Its size is
\[
|P||Q|=
\left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
\tag{3}
\]
We show that it is edge general position.

Any geodesic containing three edges in \(H_n\) has length three. After orienting it from a \(B\)-vertex to an \(A\)-vertex, its three edges have the form
\[
a_\ell b_j,\qquad a_\ell b_k,\qquad a_i b_k,
\]
with
\[
\ell\le j<i\le k.
\tag{4}
\]
Under \(\Phi\), these become
\[
\{\ell,j+1\},\qquad \{\ell,k+1\},\qquad \{i,k+1\}.
\tag{5}
\]
If all three pairs crossed \(P,Q\), then the colors at \(\ell\) and \(i\) would agree, the colors at \(j+1\) and \(k+1\) would agree, and these two colors would be opposite. If \(j+1=i\), this is immediately impossible. Otherwise
\[
\ell<j+1<i<k+1
\]
would give an alternating four-term color subsequence. Such a subsequence requires at least four runs, contrary to the construction. Thus no geodesic contains three selected edges, and equality holds in (2).

It remains to classify equality. If \(S\) is maximum, then \(\Phi(S)\) is a triangle-free graph on \(n+1\) vertices with exactly \(\lfloor(n+1)^2/4\rfloor\) edges. The equality case of Mantel's theorem says that \(\Phi(S)\) is a complete balanced bipartite graph. Let its two parts color the ordered set \(1,\ldots,n+1\). If the color string had four runs, choose
\[
p<q<r<s
\]
from four consecutive runs. Then the crossing pairs
\[
\{p,q\},\qquad \{p,s\},\qquad \{r,s\}
\]
all belong to \(\Phi(S)\). Their inverse images are three consecutive edges of the geodesic
\[
b_{q-1}-a_p-b_{s-1}-a_r,
\]
contradicting edge general position. Hence the color string has at most three runs. The converse was proved above.

For the count, put \(N=n+1\). A binary string with prescribed positive color counts \(x,y\) and at most three runs has exactly
\[
2+(x-1)+(y-1)=N
\]
forms: two with two runs, \(x-1\) of type \(0\!\!\!\text{-}\!1\!\!\!\text{-}\!0\), and \(y-1\) of type \(1\!\!\!\text{-}\!0\!\!\!\text{-}\!1\). If \(N\) is odd, the balanced part sizes differ, so the smaller part canonically chooses one color and all \(N\) strings give distinct bipartitions. If \(N\) is even, the two part sizes are equal and complementary colorings describe the same bipartition, so the count is \(N/2\). Replacing \(N\) by \(n+1\) gives the stated formula.

## Verification
The included checker reconstructs shortest-path distances in \(H_n\) and independently enumerates every length-three geodesic triple. For \(2\le n\le6\), it exhausts every edge subset of the maximum size and of one larger size, thereby checking both optimality and the complete maximum-set classification. It also checks every predicted maximum construction through \(n=20\).

## Relationship to prior work
Edge general position was introduced in 2021. The foundational paper proves general tools, the exact hypercube value, the tree value, and grid results; its searchable full text contains no half-graph or chain-graph specialization. The present proof instead turns the half-graph problem into a sharp extremal problem on \(K_{n+1}\): edge general position forces triangle-freeness under the interval-pair bijection, and Mantel equality supplies the balanced bipartite structure.

Later work studies extremal values, block graphs, Fibonacci and Lucas cubes, cactus graphs, graph products, and integer-programming formulations. The inspected open 2024 extremal paper contains no half-graph or Ferrers-graph result; its occurrence of “chain” concerns a chain of cycles rather than chain graphs. A 2026 graph-product paper has an abstract centered on hierarchical, corona, and edge-corona products and does not state a half-graph formula in the accessible material.

The closest same-object results found in targeted searches concern edge metric dimension, mixed metric dimension, and other resolving parameters of half graphs. These use distance codes rather than the no-three-edges-on-a-geodesic condition and do not imply the Mantel reduction or the maximum-set count here.

## Limitations
The theorem concerns the canonical twin-free half graphs. It does not give the edge general position number for arbitrary chain graphs with repeated twin classes.

The finite exhaustive verification is corroborative only. The arbitrary-order result relies on the bijection (1), Mantel's theorem including its equality case, and the run characterization proved above.

Search coverage cannot rule out a differently phrased or non-indexed half-graph treatment. The 2026 graph-product paper was compared through its accessible abstract and bibliographic scope rather than full text.

## References
1. P. Manuel, R. Prabha, S. Klavžar, “Edge General Position Problem,” arXiv:2105.04292v1, 10 May 2021; Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 2997–3009, DOI 10.1007/s40840-022-01319-8.
2. J. Tian, S. Klavžar, E. Tan, “Extremal Edge General Position Sets in Some Graphs,” Graphs and Combinatorics 40 (2024), Article 40, DOI 10.1007/s00373-024-02770-z.
3. Y. Cao, S. Ji, L. Wang, “The Edge General Position Number of Some Graphs,” Bulletin of the Malaysian Mathematical Sciences Society 48 (2025), DOI 10.1007/s40840-025-01873-x.
4. Z. Hamed-Labbafian, M. A. Henning, M. Tavakoli, “Edge general position in graphs: Graph products, integer linear programming and some applications,” Discrete Applied Mathematics 386 (2026), 1–8, DOI 10.1016/j.dam.2026.01.008.
