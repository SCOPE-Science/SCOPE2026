# Perfect Roman domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). For a perfect Roman dominating function \(f:V(G)\to\{0,1,2\}\), let \(t_i\) be the number of vertices of \(X_i\) labeled \(2\), and \(T=\sum_i t_i\). A zero-labeled vertex in \(X_i\) is valid exactly when \(T-t_i=1\). Consequently every perfect Roman dominating function belongs to exactly one of four structural families: (i) it has no zero labels; (ii) \(T=1\), the unique \(2\) lies in a part containing no zeros, and every other part uses only \(0,1\); (iii) \(T=2\), the two \(2\)-labels lie in distinct parts, zeros occur only in those two parts, and all remaining parts are entirely \(1\); or (iv) \(T\ge3\), exactly one part contains zeros, that part contains \(T-1\) vertices labeled \(2\), exactly one \(2\)-label lies outside it, and every other outside vertex is labeled \(1\). Therefore the weight enumerator is \[\mathcal P_G(z)=z^N(1+z)^N+\sum_i n_i z^{n_i+1}\big((1+z)^{N-n_i}-z^{N-n_i}\big)+\sum_{i<j}n_i n_j z^{N-n_i-n_j+4}\big((1+z)^{n_i+n_j-2}-z^{n_i+n_j-2}\big)+\sum_i (N-n_i)\sum_{t=2}^{n_i-1}\binom{n_i}{t}z^{N-n_i+2t+1}\big((1+z)^{n_i-t}-z^{n_i-t}\big).\]If \(a_1\le\cdots\le a_r\) are the ordered part sizes, then \[\gamma_R^p(G)=\min\{N,\ a_1+1,\ N-a_r-a_{r-1}+4\}.\]

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). A perfect Roman dominating function is a function \(f:V(G)\to\{0,1,2\}\) such that every zero-labeled vertex has exactly one neighbor labeled \(2\). The polynomial \(\mathcal P_G(z)=\sum_f z^{\omega(f)}\) sums over all perfect Roman dominating functions, where \(\omega(f)=\sum_v f(v)\).

## Proof
Let \(t_i\) denote the number of vertices labeled \(2\) in \(X_i\), and put \(T=\sum_i t_i\). A vertex of \(X_i\) is adjacent to every vertex outside \(X_i\) and to none inside \(X_i\). Hence a zero-labeled vertex in \(X_i\) has exactly \(T-t_i\) neighbors labeled \(2\). Therefore a zero can occur in \(X_i\) if and only if
\[
T-t_i=1.
\]

If there are no zeros, every vertex independently receives label \(1\) or \(2\), contributing \(z^N(1+z)^N\).

Suppose zeros occur. If \(T=1\), the unique \(2\)-label lies in some part \(X_i\). That part cannot contain a zero, so its other \(n_i-1\) vertices are forced to label \(1\); every vertex outside it may independently be \(0\) or \(1\), but at least one must be zero to avoid the zero-free family. This gives
\[
n_i z^{n_i+1}\big((1+z)^{N-n_i}-z^{N-n_i}\big).
\]

If \(T=2\), a zero-containing part must satisfy \(t_i=1\). Thus the two \(2\)-labels must lie in distinct parts \(X_i,X_j\); zeros may occur only in those two parts, while every vertex outside them is forced to label \(1\). Excluding the all-ones choice among the remaining vertices of \(X_i\cup X_j\) gives
\[
n_i n_j z^{N-n_i-n_j+4}\big((1+z)^{n_i+n_j-2}-z^{n_i+n_j-2}\big).
\]

Now let \(T\ge3\). If two distinct parts containing zeros existed, each would contain \(T-1\) vertices labeled \(2\), impossible because \(2(T-1)>T\). Hence there is exactly one zero-containing part \(X_i\). It contains \(t=T-1\ge2\) vertices labeled \(2\), exactly one \(2\)-label lies outside it, every other outside vertex is forced to label \(1\), and the remaining \(n_i-t\) vertices in \(X_i\) are labeled \(0\) or \(1\) with at least one zero. Choosing the labels gives
\[
(N-n_i)\binom{n_i}{t}z^{N-n_i+2t+1}
\big((1+z)^{n_i-t}-z^{n_i-t}\big),
\]
summed over \(2\le t\le n_i-1\). The four families are disjoint and exhaustive, proving the polynomial.

For the minimum weight, the zero-free family has minimum \(N\). The \(T=1\) family has minimum \(n_i+1\), minimized at \(a_1+1\). The \(T=2\) family has minimum \(N-n_i-n_j+4\), minimized by the two largest parts. In the \(T\ge3\) family, the minimum for part \(X_i\) is \(N-n_i+5\), which is never smaller than the preceding \(T=1\) or \(T=2\) candidates. This proves the displayed formula for \(\gamma_R^p(G)\).

## Verification
The included checker constructs complete multipartite graphs from their part labels. It examines every function \(V(G)\to\{0,1,2\}\), tests the perfect Roman condition directly at each zero-labeled vertex, and compares the resulting weight distribution with the closed formula. It also compares the smallest observed weight with the minimum formula.

## Relationship to prior work
The foundational work on perfect Roman domination introduced the parameter and established tree and regular-graph bounds. A later algorithmic study proved NP-completeness on chordal, planar, and bipartite graphs and gave linear-time algorithms on cographs, which include complete multipartite graphs. That algorithm computes the minimum weight but does not provide an all-function classification or a closed weight enumerator for complete multipartite graphs.

More recent enumeration work studies pointwise-minimal perfect Roman dominating functions and polynomial-delay enumeration. That is a different output object: the polynomial here counts every feasible perfect Roman dominating function by weight, including nonminimal functions. Targeted searches did not locate an arbitrary complete-multipartite weight enumerator.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The cograph algorithm in prior work already gives broader algorithmic coverage of the minimum-weight problem, and the present minimum formula is a closed-form specialization. The finite computation is corroborative only; the all-orders result follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed prior enumerator.

## References
1. M. A. Henning, W. F. Klostermeyer, G. MacGillivray, “Perfect Roman domination in trees,” Discrete Applied Mathematics 236 (2018), 235–245, DOI 10.1016/j.dam.2017.10.027.
2. S. Banerjee, J. M. Keil, D. Pradhan, “Perfect Roman domination in graphs,” Theoretical Computer Science 796 (2019), 1–21, DOI 10.1016/j.tcs.2019.08.017.
3. K. Mann, H. Fernau, “Perfect Roman Domination: Aspects of Enumeration and Parameterization,” Algorithms 17 (2024), 576, DOI 10.3390/a17120576.
