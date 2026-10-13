# Mixed fault-tolerant metric bases of crown graphs
## Finding
For every integer \(n\ge4\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},
\qquad
B=\{b_1,\ldots,b_n\},
\]
where the deleted perfect matching consists of the nonedges
\[
a_i b_i,
\qquad
1\le i\le n.
\]
Write \(P_i=\{a_i,b_i\}\). Then
\[
\operatorname{mftdim}(\operatorname{Cr}_n)=n.
\]

Every minimum mixed fault-tolerant generator chooses exactly one vertex from every \(P_i\). If
\[
p=|S\cap A|,
\qquad
q=|S\cap B|=n-p,
\]
then such a transversal \(S\) is a basis exactly when
\[
p=0,
\qquad
q=0,
\qquad\text{or}\qquad
p,q\ge4.
\]

Hence for \(4\le n\le7\) there are exactly two bases, \(A\) and \(B\). For \(n\ge8\), the number of bases is
\[
2+\sum_{p=4}^{n-4}\binom{n}{p}
=
2^n-2\sum_{p=1}^{3}\binom{n}{p}.
\]

Thus mixed fault tolerance has a sharp structural threshold at \(n=8\): below it every minimum system is one-sided, while from \(n=8\) onward mixed-orientation minimum systems exist.

## Assumptions and scope
All graphs are finite, simple, and connected.

For a landmark \(w\), the distance to a vertex \(v\) is \(d(w,v)\), and the distance to an edge \(uv\) is
\[
d(w,uv)=\min\{d(w,u),d(w,v)\}.
\]
A mixed resolving set distinguishes every two distinct elements of
\[
V(G)\cup E(G)
\]
by their landmark-distance vectors.

A mixed resolving set \(S\) is mixed fault-tolerant when \(S\setminus\{s\}\) is still mixed resolving for every \(s\in S\). Equivalently, every two distinct mixed elements are distinguished by at least two landmarks of \(S\).

For crown graphs,
\[
d(a_i,a_j)=d(b_i,b_j)=2
\]
for \(i\ne j\),
\[
d(a_i,b_j)=1
\]
for \(i\ne j\), and
\[
d(a_i,b_i)=3.
\]

## Proof
We first classify mixed resolving transversals with one omitted matched pair.

Fix an index \(h\), omit \(P_h\), and choose exactly one vertex from every other \(P_s\). Call the resulting set \(T\), and put
\[
p=|T\cap A|,
\qquad
q=|T\cap B|,
\qquad
p+q=n-1.
\]

For an edge \(e_{ij}=a_i b_j\), with \(i\ne j\), the landmark coordinates have explicit forms. If \(a_s\in T\), then
\[
d(a_s,a_i)=
\begin{cases}
0,&s=i,\\
2,&s\ne i,
\end{cases}
\qquad
d(a_s,b_i)=
\begin{cases}
3,&s=i,\\
1,&s\ne i,
\end{cases}
\]
and
\[
d(a_s,e_{ij})=
\begin{cases}
0,&s=i,\\
2,&s=j,\\
1,&s\notin\{i,j\}.
\end{cases}
\]
If \(b_s\in T\), then
\[
d(b_s,a_i)=
\begin{cases}
3,&s=i,\\
1,&s\ne i,
\end{cases}
\qquad
d(b_s,b_i)=
\begin{cases}
0,&s=i,\\
2,&s\ne i,
\end{cases}
\]
and
\[
d(b_s,e_{ij})=
\begin{cases}
2,&s=i,\\
0,&s=j,\\
1,&s\notin\{i,j\}.
\end{cases}
\]

These formulas separate every two vertices. Same-side vertices are distinguished by a selected landmark from at least one of their two matched pairs. Opposite-side vertices with different indices are distinguished by a selected landmark from a third matched pair; such an index exists because \(n\ge4\) and only one pair is omitted. Matched opposite-side vertices are separated by any selected landmark from another pair.

They also separate every two edges. For \(e_{ij}\), the coordinates different from \(1\) occur exactly at selected endpoint indices in \(\{i,j\}\setminus\{h\}\). If both endpoint pairs are represented, the values \(0\) and \(2\) recover the orientation. If one endpoint index is \(h\), the remaining selected endpoint again has opposite \(0/2\) values for the two orientations. Hence distinct edges have distinct codes.

A nonincident vertex and edge are separated either at the vertex's own represented matched pair or, when that pair is \(P_h\), at a represented endpoint pair of the edge. Therefore a collision can occur only between an endpoint and its incident edge.

For \(a_i\) and \(e_{ij}=a_i b_j\), the complete set of distinguishing vertices is
\[
\{b_i,b_j\}\cup\{a_s:s\notin\{i,j\}\}.
\]
Hence \(T\) fails to distinguish \(a_i\) from \(e_{ij}\) exactly when all represented pairs indexed by \(i,j\) are oriented toward \(A\) and every other represented pair is oriented toward \(B\). Because exactly one pair is omitted, such a collision exists exactly when
\[
p\in\{1,2\}.
\]
Conversely, if \(p=1\), use the unique selected \(A\)-index together with the omitted index; if \(p=2\), use the two selected \(A\)-indices. By symmetry, a collision between a \(B\)-endpoint and an incident edge exists exactly when
\[
q\in\{1,2\}.
\]

Thus the one-hole transversal \(T\) is mixed resolving exactly when
\[
p=0,
\qquad
q=0,
\qquad\text{or}\qquad
p,q\ge3.
\]

Now let \(S\) be mixed fault-tolerant. For distinct \(i,j\), the only vertices that distinguish \(a_i\) from \(a_j\) are
\[
P_i\cup P_j.
\]
Since fault tolerance requires at least two distinguishers,
\[
|S\cap(P_i\cup P_j)|\ge2
\]
for every \(i\ne j\). Put
\[
x_i=|S\cap P_i|\in\{0,1,2\}.
\]
Then \(x_i+x_j\ge2\) for all \(i\ne j\). If every \(x_i\ge1\), then \(|S|\ge n\). If some \(x_h=0\), then every other \(x_j=2\), so
\[
|S|\ge2n-2>n
\]
for \(n\ge4\). Therefore
\[
\operatorname{mftdim}(\operatorname{Cr}_n)\ge n.
\]

If \(|S|=n\), equality forces \(x_i=1\) for every \(i\), so \(S\) is a full deleted-matching transversal. Let
\[
p=|S\cap A|,
\qquad
q=|S\cap B|.
\]
Deleting a selected \(A\)-vertex produces a one-hole transversal with counts \(p-1,q\); deleting a selected \(B\)-vertex produces one with counts \(p,q-1\). The one-hole classification shows that every deletion remains mixed resolving exactly when
\[
p=0,
\qquad
q=0,
\qquad\text{or}\qquad
p,q\ge4.
\]
The pure transversals \(A\) and \(B\) therefore give the upper bound \(n\), completing the dimension proof.

Finally, each choice of \(p\) indices oriented toward \(A\) determines one transversal. Besides the two pure transversals, mixed bases occur exactly for
\[
4\le p\le n-4,
\]
which gives the stated count.

## Verification
The included checker constructs \(\operatorname{Cr}_n\), computes all-pairs vertex distances by breadth-first search, forms every vertex-edge mixed element, and precomputes the exact landmark set distinguishing each pair of mixed elements.

For every \(4\le n\le9\), it exhaustively checks every vertex subset of size at most \(n\), rejects every smaller candidate, and compares every size-\(n\) candidate with the basis classification above.

Independently, for every omitted matched pair and every orientation of the remaining pairs, it checks the one-hole mixed-resolving lemma used in the proof.

## Relationship to prior work
Mixed metric dimension was introduced in 2016–2017 as simultaneous resolution of vertices and edges. The foundational paper develops the basic theory and treats cycles, complete bipartite graphs, trees, and grids, but not crown graphs.

Mixed fault-tolerant metric dimension was introduced in 2022 by requiring every one-landmark deletion to remain a mixed resolving set. That paper gives a general existence characterization and a construction for graphs of girth at least four, but its searchable text does not treat crown graphs.

The present result is not a specialization of the complete-bipartite mixed-dimension formula: deleting a perfect matching changes the metric from diameter \(2\) to diameter \(3\) and creates the matched-pair structure controlling all minimum fault-tolerant sets. It is also stronger than the general existence result because it gives the exact optimum, every minimum set, the exact basis count, and the \(n=8\) transition.

## Limitations
The theorem is stated for \(n\ge4\). The smallest crown \(\operatorname{Cr}_3\), which is a six-cycle, is excluded.

No claim is made for ordinary fault-tolerant metric dimension, fault-tolerant edge metric dimension, or higher deletion tolerance.

The exhaustive computation is corroborative only. The all-\(n\) conclusion follows from the one-hole transversal lemma and the two-distinguisher lower bound.

## References
1. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292v1, 14 November 2016; Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
2. U. Ahmad, S. Ahmed, M. Javaid, M. N. Alam, “Computing Fault-Tolerant Metric Dimension of Connected Graphs,” Journal of Mathematics 2022, Article 9773089, version of record online 28 May 2022, DOI 10.1155/2022/9773089.
3. M. Milivojević Danas, “The mixed metric dimension of flower snarks and wheels,” Open Mathematics 19 (2021), 629–640, DOI 10.1515/math-2021-0065.
