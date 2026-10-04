# Total weak Roman domination on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\). For a function \(f:V(G)\to\{0,1,2\}\), let \(p_i\) be the number of positive-labeled vertices in part \(X_i\) and let \(s_i=\sum_{v\in X_i}f(v)\). Then \(f\) is a total weak Roman dominating function if and only if either its positive support meets at least three parts, or it meets exactly two parts \(X_i,X_j\) and \[(p_i=n_i\text{ or }s_j\ge2)\quad\text{and}\quad(p_j=n_j\text{ or }s_i\ge2).\] Define \(A_i(z)=(1+z+z^2)^{n_i}-1\), \(F_i(z)=(z+z^2)^{n_i}\), \(Q_i(z)=A_i(z)-F_i(z)\), \(L_i(z)=n_i z\), and \(M_i(z)=\mathbf 1_{n_i\ge2}n_i z\). The weight enumerator of all total weak Roman dominating functions is \[\mathcal T_G(z)=(1+z+z^2)^N-1-\sum_i A_i(z)-\sum_{i<j}\big(Q_i(z)L_j(z)+Q_j(z)L_i(z)-M_i(z)M_j(z)\big),\] where \(N=\sum_i n_i\). If \(s\) and \(t\) denote the numbers of parts of sizes one and two, respectively, then for \(r\ge3\) the minimum weight is two when \(s\ge2\) and otherwise three; for \(r=2\) it is two for \(K_{1,1}\), three when the smaller part has size at most two but the graph is not \(K_{1,1}\), and four otherwise. Exact counts of minimum functions are given in the accompanying proof.

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). A total dominating function is a labeling \(f:V(G)\to\{0,1,2\}\) such that every vertex has a neighbor of positive label. A total weak Roman dominating function additionally requires every zero-labeled vertex to admit a transfer of one unit from an adjacent positive vertex after which the resulting labeling is still total dominating.

## Proof
Write \(p_i=|\{v\in X_i:f(v)>0\}|\) and \(s_i=\sum_{v\in X_i}f(v)\). In a complete multipartite graph, a labeling is total dominating exactly when its positive support meets at least two parts.

Suppose first that the support meets at least three parts. Let \(v\) be zero-labeled. Choose any positive neighbor \(u\), which lies in another part. If \(f(u)=2\), then \(u\) stays positive after transferring one unit to \(v\). If \(f(u)=1\), the part of \(u\) may disappear from the support, but at least two represented parts still remain after the transfer; if the part of \(v\) was previously unrepresented, it is simultaneously added. Thus every zero is totally protected.

Now suppose the support meets exactly two parts \(X_i,X_j\). A zero vertex in \(X_i\) can only receive from \(X_j\). Such a transfer preserves two represented support parts exactly when either there is no zero in \(X_i\), namely \(p_i=n_i\), or the donor side retains positive support after giving one unit. The latter happens exactly when the total label weight on \(X_j\) is at least two: either a label two remains positive after donating or at least two label-one vertices were present. Hence zeros in \(X_i\) are protected exactly when \(p_i=n_i\) or \(s_j\ge2\). The symmetric condition on \(X_j\) gives the stated criterion.

For enumeration, let \(A_i(z)=(1+z+z^2)^{n_i}-1\) count nonzero labelings on part \(X_i\), and let \(F_i(z)=(z+z^2)^{n_i}\) count labelings in which every vertex of that part is positive. Thus \(Q_i=A_i-F_i\) counts nonempty but non-full support on part \(i\). A two-part support \(X_i,X_j\) fails exactly when \(X_i\) is non-full and the total weight on \(X_j\) is one, or symmetrically. Weight one on part \(j\) has polynomial \(L_j(z)=n_jz\). The intersection of these two bad events occurs precisely when both sides have weight one and both supports are non-full, contributing \(M_i(z)M_j(z)\), where \(M_i(z)=\mathbf 1_{n_i\ge2}n_i z\). Starting from all \(3^N\) labelings, subtracting the zero-support and one-support cases and then these bad two-support cases gives
\[
\mathcal T_G(z)=(1+z+z^2)^N-1-\sum_i A_i(z)-\sum_{i<j}\big(Q_i(z)L_j(z)+Q_j(z)L_i(z)-M_i(z)M_j(z)\big).
\]

For the minimum, let \(s\) be the number of singleton parts and \(t\) the number of parts of size two. If \(r\ge3\), weight two is possible exactly by assigning label one to two singleton parts, so it occurs exactly when \(s\ge2\), with \(\binom{s}{2}\) minimum functions. Otherwise weight three is attained by one label-one vertex in each of three parts, or by using a full part of total weight two together with one label-one vertex elsewhere. Hence the number of minimum functions is
\[
\sum_{i<j<k}n_i n_j n_k+s(N-1)+t(N-2).
\]
If \(r=2\), then \(K_{1,1}\) has the unique weight-two function with both labels one. Weight three exists exactly when at least one part has size one or two; its number is \(s(N-1)+t(N-2)\). If both part sizes \(a,b\) are at least three, the minimum is four. Writing \(h(n)=n+\binom{n}{2}\), the number of weight-four minima is
\[
h(a)h(b)+\mathbf 1_{a=3}b+\mathbf 1_{b=3}a.
\]
The first term chooses weight two independently on each non-full side; the final terms cover the additional case in which a three-vertex part is fully labeled one and the opposite side contributes a single label-one vertex.

## Verification
The included checker reconstructs each graph from its part labels. For every ternary labeling it tests total domination vertex by vertex and, for every zero-labeled vertex, tries every adjacent positive donor and retests total domination after the transfer. It compares this definition-level decision with the structural criterion, every coefficient of the weight enumerator, and the minimum-weight/minimum-count formulas for every complete multipartite isomorphism type of orders two through nine.

## Relationship to prior work
Cabrera Martínez, Montejano, and Rodríguez-Velázquez introduced total weak Roman domination in 2019, established general inequalities and exact results for rooted products, and proved NP-hardness. Their full article does not state a complete multipartite classification or a weight enumerator. The parameter is naturally placed in MSC \(05C69\); a later paper by Cabrera Martínez and Rodríguez-Velázquez on total protection of lexicographic product graphs lists MSC \(05C69\) and \(05C76\).

The 2022 lexicographic-product paper proves that total weak Roman and secure total domination numbers coincide for lexicographic product graphs and gives formulas and bounds for those minimum parameters. This provides genuine prior minimum-value coverage for balanced complete multipartite graphs of the form \(K_r\circ\overline{K_n}\), but it does not enumerate all total weak Roman functions or treat arbitrary part-size vectors as a set system. The present theorem is therefore framed around the all-function classification and weight enumerator, with the minimum formulas included as consequences.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The exhaustive computation is finite corroboration only; the all-orders result follows from the proof. The lexicographic-product literature gives broader minimum-parameter coverage on its product class. Search coverage cannot exclude a differently phrased or non-indexed all-function enumeration.

## References
1. A. Cabrera Martínez, L. P. Montejano, J. A. Rodríguez-Velázquez, “Total Weak Roman Domination in Graphs,” Symmetry 11(6) (2019), 831, DOI 10.3390/sym11060831.
2. A. Cabrera Martínez, J. A. Rodríguez-Velázquez, “Total Protection of Lexicographic Product Graphs,” Discussiones Mathematicae Graph Theory 42(3) (2022), 967–984, DOI 10.7151/dmgt.2318.
