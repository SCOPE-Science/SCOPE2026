# Seven vertices are the sharp unique-leader split for degree and eigenvector centrality
## Finding
Let \(G=(V,E)\) be a connected finite simple undirected graph. Degree centrality ranks a vertex \(v\) by
\[
d(v)=\deg(v).
\]
Eigenvector centrality is the positive Perron eigenvector \(x\) of the adjacency matrix \(A\):
\[
Ax=\lambda x,
\]
where \(\lambda\) is the spectral radius. Since \(G\) is connected, Perron--Frobenius gives a unique positive eigenvector up to scaling, so its maximizing set is well defined.

Assume that both centralities have unique maximizing vertices.

If
\[
|V|\le 6,
\]
then the degree maximizer and eigenvector-centrality maximizer are the same vertex.

The bound is sharp. At order \(7\), exactly five connected unlabeled graph classes have distinct unique maximizers. Their labeled orbit sizes are
\[
420,\quad2520,\quad2520,\quad1260,\quad2520,
\]
for a total of
\[
9240
\]
labeled first-conflict graphs.

Using vertices \(0,\ldots,6\), representatives are:

\[
\begin{array}{c|l|c|c|c}
& E & \text{degree leader} & \text{eigenvector leader} & \text{orbit}\\ \hline
1&\{01,12,13,14,25,26,56\}&1&2&420\\
2&\{01,04,12,14,23,25,26,45\}&2&1&2520\\
3&\{01,04,12,15,16,23,34,35,45\}&1&5&2520\\
4&\{02,12,13,14,23,25,26,34,35,45\}&2&3&1260\\
5&\{01,02,13,14,15,23,24,25,26,35,45\}&2&5&2520
\end{array}
\]

The first class gives the simplest structural picture. Its degree vector is
\[
(1,4,3,1,1,2,2).
\]
Vertex \(1\) has three leaves and one link to vertex \(2\), while vertices \(2,5,6\) form a triangle. The local hub \(1\) therefore has the largest degree, but the recursively weighted neighborhood of vertex \(2\) makes \(2\) the unique eigenvector-centrality leader.

Hence seven vertices are necessary and sufficient for two unambiguous notions of network leadership—raw degree and adjacency eigenvector centrality—to choose different vertices.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

Eigenvector centrality means the Perron eigenvector of the unweighted adjacency matrix. Positive scalar normalization is irrelevant to the maximizing vertex.

The theorem requires both maximizing sets to be singletons. There are smaller graphs in which a unique degree leader belongs to a tied eigenvector-centrality maximizing set; those do not constitute two different unambiguous choices.

The exhaustive classification ends at seven vertices. No frequency or structural claim is made for larger graphs, directed networks, weighted networks, or other spectral centralities.

## Proof
The proof is a finite exact classification over the standard Read--Wilson Graph Atlas domain through seven vertices.

The embedded atlas table contains every connected unlabeled graph on \(2\) through \(7\) vertices, with counts
\[
1,\ 2,\ 6,\ 21,\ 112,\ 853.
\]
The external Graph Atlas documentation states that the underlying atlas contains all graphs with at most seven vertices.

For each graph, degree maximizers are read directly from the adjacency matrix. Eigenvector maximizers are determined exactly, without floating-point eigenvectors, as follows.

Let
\[
p(t)=\det(tI-A)
\]
and, for vertex \(i\), let
\[
q_i(t)=\det(tI-A_{-i}),
\]
where \(A_{-i}\) deletes row and column \(i\). If \(\lambda\) is the Perron root and \(x\) a Perron eigenvector, the adjugate identity for a simple eigenvalue gives
\[
q_i(\lambda)=\frac{p'(\lambda)}{\lVert x\rVert^2}x_i^2.
\]
Because \(\lambda\) is the largest simple eigenvalue,
\[
p'(\lambda)>0.
\]
Therefore
\[
x_i>x_j
\quad\Longleftrightarrow\quad
q_i(\lambda)>q_j(\lambda).
\]

The verifier computes every characteristic polynomial with exact integer arithmetic. It isolates the Perron root by Sturm sequences over rational intervals and compares the values \(q_i(\lambda)-q_j(\lambda)\) exactly. Common polynomial factors are handled explicitly, so equality of eigenvector coordinates is detected rather than numerically approximated.

No connected graph of orders \(2,\ldots,6\) has two distinct unique leaders. Exactly five connected unlabeled graphs of order \(7\) do.

For each of those five graphs, all \(7!\) vertex permutations are checked to obtain its automorphism-group order and labeled orbit. The automorphism orders are
\[
12,\ 2,\ 2,\ 4,\ 2,
\]
so the orbit sizes are
\[
\frac{7!}{12}=420,\quad
\frac{7!}{2}=2520,\quad
\frac{7!}{2}=2520,\quad
\frac{7!}{4}=1260,\quad
\frac{7!}{2}=2520.
\]
Their sum is \(9240\).

## Verification
The embedded `verify_degree_eigenvector_boundary.py` uses only the Python standard library and the embedded `graph_atlas_connected_2to7.json` table.

It verifies:
- connected unlabeled graph counts \(1,2,6,21,112,853\) for orders \(2,\ldots,7\);
- exact degree maximizers;
- characteristic polynomials by integer Newton identities;
- Perron-root isolation by rational Sturm sequences;
- exact pairwise ordering of eigenvector coordinates through principal cofactors;
- zero distinct-unique conflicts through order \(6\);
- exactly five conflict classes at order \(7\);
- the five displayed representatives and their two distinct leaders;
- automorphism-group orders \(12,2,2,4,2\);
- labeled orbit sizes \(420,2520,2520,1260,2520\);
- total labeled first-conflict count \(9240\).

Run:

`python3 verify_degree_eigenvector_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Grassi, Stefani, and Torriero directly compare degree centrality with eigenvector centrality in undirected social networks and derive spectral-radius conditions under which highest-degree nodes are also most eigencentral. Their paper therefore owns the central comparison motivating this question.

Bonacich likewise emphasizes that eigenvector centrality is deliberately different from degree because a vertex inherits importance from the importance of its neighbors, not merely their number.

Pradhan, Angeliya, and Jalan study failure and localization phenomena for adjacency eigenvector centrality in connected undirected networks. Their open full text explicitly contrasts degree with eigenvector centrality and discusses situations in which principal-eigenvector ranking can be misleading.

The inspected literature establishes that degree and eigenvector rankings can differ and studies sufficient conditions and mechanisms. It does not, in the material inspected, give the smallest connected graph order at which two unique leaders disagree, nor a complete classification of the first disagreement layer.

Targeted searches using degree/eigenvector terminology, unique-maximizer and unique-leader formulations, smallest-graph language, seven-vertex restrictions, and the exact first-layer count did not locate an equivalent theorem or table.

## Limitations
The result concerns unweighted adjacency eigenvector centrality on connected simple undirected graphs.

The uniqueness requirement is essential to the exact boundary stated.

The finite Atlas input is externally curated rather than regenerated from first principles inside the verifier; its completeness through seven vertices is separately documented by the Graph Atlas reference.

An unindexed teaching example, thesis, software corpus, or atlas annotation could contain one or more of the same seven-vertex examples.

The full text of the 2007 Grassi--Stefani--Torriero paper was not accessible in the inspected source; its abstract and bibliographic record were inspected, and this access limitation remains a residual literature risk.

## References
1. R. Grassi, S. Stefani, and A. Torriero, “Some New Results on the Eigenvector Centrality,” *The Journal of Mathematical Sociology* 31(3), 237–248, 2007. DOI: 10.1080/00222500701373251.
2. P. Bonacich, “Some unique properties of eigenvector centrality,” *Social Networks* 29(4), 555–564, 2007. DOI: 10.1016/j.socnet.2007.04.002.
3. P. Pradhan, A. C. U., and S. Jalan, “Principal eigenvector localization and centrality in networks: revisited,” arXiv:1909.08696, 2019.
4. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998.
