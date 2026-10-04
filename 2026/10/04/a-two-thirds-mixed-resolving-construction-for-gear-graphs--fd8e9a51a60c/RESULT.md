# A two-thirds mixed-resolving construction for gear graphs
## Finding
Let \(G_n\) be the gear graph with center \(z\), rim vertices \(x_1,\ldots,x_n\), inserted vertices \(y_1,\ldots,y_n\), and edges \(zx_i,x_i y_i,x_{i+1}y_i\), with subscripts modulo \(n\), for \(n\ge4\). For \(J\subseteq\mathbb Z_n\), the inserted-vertex set \(S_J=\{y_j:j\in J\}\) is a mixed metric generator exactly when \[J\cap\{i-1,i\}\ne\varnothing\quad\text{and}\quad J\cap\{i-1,i+1\}\ne\varnothing\quad\text{for every }i\in\mathbb Z_n.\] Equivalently, omitted inserted vertices have cyclic pairwise distance at least \(3\). Hence \[\operatorname{mdim}(G_n)\le n-\lfloor n/3\rfloor=\lceil2n/3\rceil<n.\] Thus the published statement \(\operatorname{mdim}(G_n)=n\) for \(n\ge4\) is false throughout its stated range; moreover \(\operatorname{mdim}(G_4)=3\).

## Assumptions and scope
All graphs are finite, simple, and connected. For \(n\ge4\), the gear graph \(G_n\) has
\[
V(G_n)=\{z\}\cup\{x_i:i\in\mathbb Z_n\}\cup\{y_i:i\in\mathbb Z_n\},
\]
and edges \(zx_i\), \(x_i y_i\), and \(x_{i+1}y_i\). For a vertex \(s\) and edge \(uv\), the mixed distance is
\[
d(s,uv)=\min\{d(s,u),d(s,v)\}.
\]
A mixed metric generator makes all elements of \(V(G_n)\cup E(G_n)\) have distinct distance vectors.

## Proof
For an inserted landmark \(y_j\), direct shortest-path calculation gives
\[
\begin{array}{c|c}
\text{object}&d(y_j,\text{object})\\ \hline
z&2\\
x_i&1\text{ if }j\in\{i-1,i\},\text{ otherwise }3\\
y_i&0\text{ if }j=i;\ 2\text{ if }j\in\{i-1,i+1\};\ \text{otherwise }4\\
zx_i&1\text{ if }j\in\{i-1,i\},\text{ otherwise }2\\
x_i y_i&0\text{ if }j=i;\ 1\text{ if }j=i-1;\ 2\text{ if }j=i+1;\ \text{otherwise }3\\
x_{i+1}y_i&0\text{ if }j=i;\ 1\text{ if }j=i+1;\ 2\text{ if }j=i-1;\ \text{otherwise }3.
\end{array}
\]
If \(J\cap\{i-1,i\}=\varnothing\), then \(z\) and \(zx_i\) have identical vectors on \(S_J\). If \(J\cap\{i-1,i+1\}=\varnothing\), then \(x_i\) and \(x_{i+1}\) have identical vectors. Thus both conditions in the finding are necessary.

Assume both conditions hold. Comparing the six rows shows that the local value patterns identify every object: rim vertices and spokes are indexed by their nonempty value-\(1\) coordinate sets; inserted vertices are identified by a value \(0\) when selected and otherwise by their two selected cyclic neighbors carrying value \(2\); the two subdivided edges through the same \(y_i\) are distinguished because values \(1\) and \(2\) occur on opposite neighboring coordinates; distinct edge indices shift these local patterns; and the remaining cross-type pairs have different background values. Hence the conditions are sufficient.

The conditions are equivalent to saying that omitted indices have cyclic distance at least three. Omitting
\[
3,6,9,\ldots,3\lfloor n/3\rfloor
\]
therefore leaves a mixed metric generator of size
\[
n-\lfloor n/3\rfloor=\lceil2n/3\rceil.
\]
This is smaller than \(n\) for every \(n\ge4\), so the published formula fails throughout its stated range. For \(G_4\), three inserted landmarks suffice, and exhaustive testing of all two-vertex sets shows none resolves all vertices and edges; hence \(\operatorname{mdim}(G_4)=3\).

## Verification
The included checker rebuilds every tested gear graph from its edge set, computes distances by breadth-first search, and tests mixed signatures directly. It validates the construction through \(n=60\), validates the displayed distance table through \(n=40\), and exhaustively finds the first resolving layer for \(n=4,5,6,7,8\), obtaining dimensions \(3,4,4,5,6\). The finite tests corroborate the theorem; the all-parameter upper bound follows from the symbolic distance table.

## Relationship to prior work
The foundational 2016 paper introduced mixed metric dimension and lists primary classification \(05C12\). The 2022 wheel-like-graphs paper defines the same gear graph and states in Theorem 1 that \(\operatorname{mdim}(G_n)=n\) for \(n\ge4\). Its upper-bound construction takes all \(x_i\). Its lower-bound paragraph then assumes the specific \((n-1)\)-set \(\{x_1,\ldots,x_{n-1}\}\) and exhibits a collision; this does not rule out other smaller landmark sets. The construction above supplies such sets for every \(n\ge4\).

Targeted searches for the theorem, the gear graph, mixed resolving sets, corrections, and errata located the published equality and later general mixed-metric work, but no correction or stronger gear result covering this construction.

## Limitations
The exact all-\(n\) mixed metric dimension is not claimed. The theorem classifies mixed generators consisting only of inserted vertices, proves the uniform upper bound, and proves the exact first case \(G_4\). The exhaustive values through \(n=8\) are finite corroboration only. An unindexed or differently phrased correction may exist.

## References
1. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292v1, 14 November 2016; Applied Mathematics and Computation 314 (2017), 429–438.
2. Darmaji, N. Azahra, “The mixed metric dimension of wheel-like graphs,” Journal of Physics: Conference Series 2157 (2022), 012010, DOI 10.1088/1742-6596/2157/1/012010.
