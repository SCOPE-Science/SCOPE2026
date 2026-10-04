# Weight enumerator of covering Italian functions on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), \(N=\sum_i n_i\), and parts \(X_i\). A covering Italian dominating function \(f:V(G)\to\{0,1,2\}\) is characterized as follows. Either no vertex has label \(0\), or the nonempty zero set is contained in a unique part \(X_i\); every vertex outside \(X_i\) then has label \(1\) or \(2\), and if \(N-n_i=1\) the unique outside vertex is forced to have label \(2\), while if \(N-n_i\ge2\) there is no additional restriction. Writing \(P_m(z)=z^m(1+z)^m\), \(T_m(z)=(1+z+z^2)^m-P_m(z)\), and \[B_q(z)=\begin{cases}z^2,&q=1,\\z^q(1+z)^q,&q\ge2,\end{cases}\] the weight enumerator of all covering Italian dominating functions is \[\mathcal C_G(z)=P_N(z)+\sum_{i=1}^r B_{N-n_i}(z)T_{n_i}(z).\] Consequently, if \(M=\max_i n_i\), then the covering Italian domination number is \[\gamma_{cI}(G)=\max\{2,N-M\}.\]

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). A covering Italian dominating function is a function \(f:V(G)\to\{0,1,2\}\) such that the positive support is a vertex cover and every zero-labeled vertex has neighborhood-label sum at least \(2\). The polynomial \(\mathcal C_G(z)\) counts all such functions by total weight.

## Proof
The positive support of \(f\) is a vertex cover if and only if its zero set is independent. Every independent set of a complete multipartite graph is contained in a single part. Hence either there are no zeros, or there is a unique part \(X_i\) containing every zero.

If there are no zeros, every vertex independently receives label \(1\) or \(2\), so these functions contribute
\[
P_N(z)=z^N(1+z)^N.
\]

Now suppose the zero set is a nonempty subset of \(X_i\), and put \(q=N-n_i\). Every vertex outside \(X_i\) must be positive because all zeros lie in \(X_i\). A zero in \(X_i\) is adjacent to every vertex outside \(X_i\) and to no vertex of its own part, so its neighborhood-label sum is exactly the total weight assigned outside \(X_i\).

If \(q\ge2\), the outside vertices are all positive and therefore already contribute weight at least \(2\); the Italian condition is automatic. Their weight enumerator is \(z^q(1+z)^q\). Inside \(X_i\), labels \(0,1,2\) are arbitrary except that at least one zero must occur, contributing
\[
T_{n_i}(z)=(1+z+z^2)^{n_i}-z^{n_i}(1+z)^{n_i}.
\]

If \(q=1\), the unique outside vertex must itself supply neighborhood weight \(2\), so it is forced to carry label \(2\). Its contribution is \(z^2\), while the same factor \(T_{n_i}(z)\) describes the labels inside \(X_i\).

The zero-free family and the families indexed by the unique zero-containing part are pairwise disjoint and exhaustive. Summing their contributions proves
\[
\mathcal C_G(z)=P_N(z)+\sum_i B_{N-n_i}(z)T_{n_i}(z).
\]

For the minimum weight, put \(M=\max_i n_i\) and \(b=N-M\), the vertex-cover number of \(G\). If \(b\ge2\), choose a largest part as the zero set and label every outside vertex \(1\), obtaining weight \(b\); no covering Italian function can have smaller weight because its positive support is a vertex cover. If \(b=1\), the graph is a star or \(K_2\), and a nonempty zero set in the large part forces the unique outside vertex to label \(2\), giving weight \(2\); weight \(1\) is impossible. Thus \(\gamma_{cI}(G)=\max\{2,N-M\}\).

## Verification
The included checker reconstructs every complete multipartite graph of orders two through nine from its part labels. It exhaustively tests every map to \(\{0,1,2\}\): first whether the zero set is independent, then whether every zero has neighborhood-label sum at least \(2\). It compares the complete observed weight distribution with the closed polynomial and checks the minimum-weight formula. It also verifies that the specialization to complete bipartite graphs agrees with the published minimum formula for \(1\le q\le p\le10\).

## Relationship to prior work
Fan, Ye, Miao, Shao, Samodivkin, and Sheikholeslami introduced the same parameter under the name outer-independent Italian domination. Their paper determines, among other results, the minimum value on complete bipartite graphs: for \(K_{p,q}\) with \(p\ge q\), the value is \(2\) when \(q=1\) and \(q\) otherwise. The minimum formula above extends this value statement to arbitrary complete multipartite graphs, but the primary new content is the classification and weight enumeration of every feasible function.

Khodkar, Mojdeh, Samadi, and Yero later studied the parameter under the covering Italian terminology. Their full paper records subject classification \(05C69\), proves complexity and extremal results, and notes the general equality between the covering Italian number and the vertex-cover number when the minimum degree is at least two. That equality already implies the minimum formula above whenever \(N-M\ge2\). The paper does not state an all-function classification or weight enumerator for complete multipartite graphs.

Targeted literature and semantic-index searches for covering Italian, outer-independent Italian, complete multipartite, complete bipartite, polynomial, and enumerator formulations did not locate an equivalent arbitrary-multipartite weight census.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The minimum-value corollary is substantially covered by prior general and complete-bipartite results; novelty is claimed for the all-function structural classification and weight enumerator. The finite computation is corroborative only. Search coverage cannot exclude differently phrased or non-indexed enumerative work.

## References
1. W. Fan, A. Ye, F. Miao, Z. Shao, V. Samodivkin, S. M. Sheikholeslami, “Outer-Independent Italian Domination in Graphs,” IEEE Access 7 (2019), 22756–22765, DOI 10.1109/ACCESS.2019.2899875; published online 15 February 2019.
2. A. Khodkar, D. A. Mojdeh, B. Samadi, I. G. Yero, “Covering Italian domination in graphs,” Discrete Applied Mathematics 304 (2021), 324–331, DOI 10.1016/j.dam.2021.08.001; arXiv:2005.04200v1, 6 April 2020.
