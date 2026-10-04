# Independent double Roman functions on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\). A function \(f:V(G)\to\{0,1,2,3\}\) is an independent double Roman dominating function if and only if there is a unique part \(X_i\) such that every vertex outside \(X_i\) has label \(0\), every vertex of \(X_i\) has label \(2\) or \(3\), and either \(n_i\ge2\) or the unique vertex of \(X_i\) has label \(3\). Consequently the all-function weight enumerator is \[\mathcal I_G(z)=\sum_{i=1}^r z^{2n_i}(1+z)^{n_i}-s z^2,\] where \(s=|\{i:n_i=1\}|\). Equivalently, the coefficient of \(z^k\) is \[\sum_{i=1}^r \binom{n_i}{k-2n_i}-s\mathbf 1_{k=2},\] with out-of-range binomial coefficients interpreted as zero. In particular, the total number of independent double Roman dominating functions is \(\sum_i 2^{n_i}-s\). If \(m=\min_i n_i\), then \(i_{dR}(G)=3\) when \(m=1\), and \(i_{dR}(G)=2m\) when \(m\ge2\); the number of minimum functions is the number of singleton parts in the first case and the number of parts of size \(m\) in the second.

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, with \(r\ge2\), partite classes \(X_1,\ldots,X_r\), and positive part sizes \(n_i\). An independent double Roman dominating function is a function \(f:V(G)\to\{0,1,2,3\}\) satisfying the double Roman conditions and having independent positive support \(\{v:f(v)>0}\).

The weight enumerator \(\mathcal I_G(z)\) counts every such function by its weight \(\omega(f)=\sum_v f(v)\).

## Proof
Because every two vertices in different parts are adjacent, the positive support of an independent double Roman dominating function is contained in a single part, say \(X_i\).

No vertex of \(X_i\) can have label \(0\). Indeed, every positive vertex lies in \(X_i\), and vertices within one part are nonadjacent, so a zero-labeled vertex in \(X_i\) would have no neighbor labeled \(2\) or \(3\).

No vertex of \(X_i\) can have label \(1\) either. A vertex labeled \(1\) must have a neighbor labeled \(2\) or \(3\), but all positive vertices lie in \(X_i\), where there are no edges, while every vertex outside \(X_i\) has label \(0\).

Thus every vertex of \(X_i\) has label \(2\) or \(3\), and every vertex outside \(X_i\) has label \(0\). Each outside vertex is adjacent to every vertex of \(X_i\). Hence its double Roman condition is satisfied exactly when either at least one vertex of \(X_i\) has label \(3\), or at least two vertices of \(X_i\) have label \(2\).

If \(n_i\ge2\), every assignment of labels \(2\) and \(3\) to \(X_i\) is therefore valid: assignments containing a \(3\) use the first alternative, while the all-\(2\) assignment supplies at least two neighbors labeled \(2\). If \(n_i=1\), only label \(3\) is valid.

For a fixed part of size \(n_i\), all \(2/3\)-assignments contribute
\[
(z^2+z^3)^{n_i}=z^{2n_i}(1+z)^{n_i},
\]
except that a singleton part contributes only \(z^3\), so its invalid \(z^2\) term must be removed. Different supporting parts give different functions. Summing proves
\[
\mathcal I_G(z)=\sum_i z^{2n_i}(1+z)^{n_i}-s z^2.
\]
The coefficient and total-count formulas follow immediately.

For the minimum weight, a singleton supporting part contributes the unique valid weight-\(3\) function. If no singleton part exists, every supporting part has size at least two, and its minimum contribution is the all-\(2\) labeling of weight \(2n_i\). Therefore the smallest part gives weight \(2m\). The stated minimum-function counts follow from the uniqueness of these minimum assignments on each eligible part.

## Verification
The included checker independently reconstructs each complete multipartite graph from its part labels and examines every map to \(\{0,1,2,3\}\). It checks independence of the positive support and the two double Roman neighborhood conditions directly, without using the theorem. It then compares the complete observed weight distribution with the closed enumerator and checks the minimum weight and number of minimum functions.

## Relationship to prior work
The 2019 arXiv paper by Mojdeh and Mansouri initiates independent double Roman domination and develops general bounds and realizability results. A 2020 full article by Maimani, Momeni, Rahimi Mahid, and Sheikholeslami studies the same parameter, records MSC \(05C69\), and proves broad inequalities involving independent domination, independent Roman domination, independent Roman \(\{2\}\)-domination, and independent \(3\)-rainbow domination.

Those general results already constrain the minimum on complete multipartite graphs. In particular, the published relation with independent domination and independent \(2\)-domination implies the value \(2m\) when the smallest part has size at least two, while the standard upper bound from an independent dominating singleton gives value \(3\) when a singleton part is present. The new content here is therefore not the minimum number by itself, but the classification of every feasible function, the complete weight distribution, the exact total function count, and the exact number of minimum functions for arbitrary part-size vectors.

Targeted database and literature searches for complete multipartite, complete bipartite, polynomial, enumerator, and all-function formulations did not locate an equivalent weight enumerator.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The minimum-value corollary is partly implied by previously published general inequalities and is included only as a consequence of the stronger all-function classification. The exhaustive computation is finite corroboration; the theorem for arbitrary part sizes follows from the proof. Search coverage cannot exclude differently phrased or non-indexed enumerative work.

## References
1. D. A. Mojdeh, Z. Mansouri, “Independent double Roman domination in graphs,” arXiv:1904.04788v1, 9 April 2019.
2. H. R. Maimani, M. Momeni, F. Rahimi Mahid, S. M. Sheikholeslami, “Independent double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics, published online 9 July 2020, DOI 10.1016/j.akcej.2020.02.001.
