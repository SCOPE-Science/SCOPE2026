# Perfect Italian domination weight enumerator of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), \(N=\sum_i n_i\), and partite classes \(X_1,\ldots,X_r\). For a labeling \(f:V(G)\to\{0,1,2\}\), write \(W=\sum_v f(v)\) and \(s_i=\sum_{v\in X_i}f(v)\). Then \(f\) is a perfect Italian dominating function if and only if \(W-s_i=2\) for every part \(X_i\) containing a vertex labeled zero. Define \(A_n(z)=(1+z+z^2)^n-(z+z^2)^n\), let \(s\) and \(t\) be the numbers of parts of sizes \(1\) and \(2\), respectively, put \(u_i=n_i\) when \(n_i\ge2\) and \(u_i=0\) otherwise, and put \(v_i=0\) for \(n_i=1\), \(v_i=2\) for \(n_i=2\), and \(v_i=n_i+\binom{n_i}{2}\) for \(n_i\ge3\). The weight enumerator \(\Phi_G(z)=\sum_f z^{W(f)}\), summed over all perfect Italian dominating functions, is \[\Phi_G(z)=z^N(1+z)^N+z^2\sum_{i:\,1\le N-n_i\le2}A_{n_i}(z)+c_2z^2+c_3z^3+c_4z^4,\]where \[c_2=\mathbf 1_{r\ge3}(s+t)+\mathbf 1_{r\ge4}\binom{s}{2},\]\[c_3=\mathbf 1_{r=3}\left(u_1u_2u_3+\sum_{k:\,n_k=1}\prod_{i\ne k}u_i\right),\qquad c_4=\mathbf 1_{r=2}v_1v_2.\]

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\) and every \(n_i\ge1\). A perfect Italian dominating function is a labeling \(f:V(G)\to\{0,1,2\}\) such that every vertex labeled zero has neighbor-label sum exactly \(2\). Its weight is \(W(f)=\sum_v f(v)\). The enumerator \(\Phi_G(z)\) counts all such labelings by weight; vertices are labeled and distinct.

## Proof
For a part \(X_i\), let
\[
s_i=\sum_{v\in X_i}f(v),\qquad W=\sum_v f(v).
\]
Every vertex of \(X_i\) is adjacent to every vertex outside \(X_i\) and to no vertex inside \(X_i\). Hence every zero-labeled vertex in \(X_i\) has neighbor-label sum \(W-s_i\). Therefore \(f\) is perfect Italian dominating exactly when
\[
W-s_i=2
\]
for every part that contains a zero. This proves the all-function criterion.

Let \(Z\) be the set of parts containing a zero and write \(q=|Z|\). For every \(i\in Z\), the criterion gives \(s_i=W-2\). Let \(R\) be the total weight on parts outside \(Z\). Then
\[
R=W-q(W-2)=2q-(q-1)W.
\]

If \(q=0\), every vertex is labeled \(1\) or \(2\), giving
\[
(z+z^2)^N=z^N(1+z)^N.
\]

If \(q=1\), say \(Z=\{i\}\), then all vertices outside \(X_i\) are positive and their total weight is exactly \(2\). Thus there are either one or two vertices outside \(X_i\). Their labels are forced: a single outside vertex receives \(2\), while two outside vertices both receive \(1\). The assignments on \(X_i\) may be arbitrary except that at least one vertex is zero, which contributes
\[
A_{n_i}(z)=(1+z+z^2)^{n_i}-(z+z^2)^{n_i}.
\]
This gives the second term in the formula.

Assume now that \(q\ge2\). Since \(R\ge0\), the identity above implies \(W\le4\). For \(W=2\), every zero-containing part has weight zero and the positive complement has weight two. It is therefore either one singleton part labeled \(2\), one two-vertex part labeled \(1,1\), or two singleton parts each labeled \(1\). The requirement \(q\ge2\) yields exactly
\[
c_2=\mathbf 1_{r\ge3}(s+t)+\mathbf 1_{r\ge4}\binom{s}{2}.
\]

For \(W=3\), one has \(R=3-q\), so either \(q=3\) and \(R=0\), or \(q=2\) and \(R=1\). In the first case \(r=3\) and every part has weight one while containing a zero. In the second case \(r=3\), the unique part outside \(Z\) is a singleton labeled \(1\), and the other two parts again have weight one while containing a zero. A part of size \(n_i\ge2\) has exactly \(n_i=u_i\) such assignments, obtained by choosing its unique vertex labeled \(1\); a singleton has none. This gives the stated \(c_3\).

For \(W=4\), the identity forces \(q=2\) and \(R=0\), hence \(r=2\), and each part has weight two while containing a zero. The number of such assignments on a part of size \(n_i\) is the coefficient of \(z^2\) in \(A_{n_i}(z)\), namely \(v_i\). This gives \(c_4=v_1v_2\). For \(W\ge5\), the expression for \(R\) is negative, so no further cases occur. The cases are disjoint and exhaustive, proving the formula.

## Verification
The included checker reconstructs every complete multipartite graph from its part labels. It exhaustively tests every labeling \(f:V\to\{0,1,2\}\) by directly summing labels over the actual neighborhood of every zero-labeled vertex, without using the theorem. It compares this definition-level decision with the profile criterion and compares every observed weight count with the closed formula for all complete multipartite isomorphism types of orders two through nine.

The checker also verifies the already-published minimum-value theorem when every part has size at least three: the minimum weight is \(4\) for two parts, \(3\) for three parts, and \(N\) for at least four parts.

## Relationship to prior work
Lauri and Mitillos define perfect Italian domination, characterize the cases with minimum weight two and three, and determine the exact minimum for complete multipartite graphs whose parts all have size at least three. Their theorem gives minimum weights \(4\), \(3\), and \(N\) according as the number of parts is two, three, or at least four. The present result does not claim those minimum values as new; instead it classifies every perfect Italian dominating labeling, allows arbitrary positive part sizes, and counts all labelings by weight.

Banerjee, Henning, and Pradhan subsequently give a linear-time algorithm for the minimum perfect Italian domination number on cographs. Since complete multipartite graphs are cographs, this is genuine broader algorithmic coverage of the optimization problem. The accessible abstract describes minimum-value structure and computation, not a cardinality-by-weight enumeration of all perfect Italian dominating functions.

Targeted searches for the aliases “perfect Italian domination” and “perfect Roman \(\{2\}\)-domination,” together with complete multipartite, complete bipartite, polynomial, enumerator, and all-function terminology, did not locate an arbitrary-complete-multipartite weight enumerator.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The published minimum theorem for parts of size at least three and the cograph minimum algorithm are prior coverage and are not novelty claims here. The exhaustive computation through order nine is corroborative only; the all-orders result follows from the proof. Full text of the cograph paper was not available from the inspected lawful-access routes, so a differently phrased enumerative result there remains a residual access risk. Search coverage cannot exclude unindexed or differently named prior enumerations.

## References
1. J. Lauri, C. Mitillos, “Perfect Italian domination on planar and regular graphs,” arXiv:1905.06293v1, submitted 15 May 2019; later published in Discrete Applied Mathematics, DOI 10.1016/j.dam.2020.05.024.
2. S. Banerjee, M. A. Henning, D. Pradhan, “Perfect Italian domination in cographs,” Applied Mathematics and Computation 391 (2021), 125703, DOI 10.1016/j.amc.2020.125703.
3. T. W. Haynes, M. A. Henning, “Perfect Italian domination in trees,” Discrete Applied Mathematics 260 (2019), 164–177, DOI 10.1016/j.dam.2019.01.038.
