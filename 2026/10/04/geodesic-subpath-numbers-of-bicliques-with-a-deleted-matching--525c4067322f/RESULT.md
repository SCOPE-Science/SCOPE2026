# Geodesic subpath numbers of bicliques with a deleted matching
## Finding
For integers \(a,b\ge 3\) and \(0\le t\le \min\{a,b\}\), let \(G_{a,b,t}\) be obtained from \(K_{a,b}\) by deleting a matching of size \(t\). Then
\[
\operatorname{gpn}(G_{a,b,t})=a+b+\frac{ab(a+b)}{2}+t(ab-2a-2b+3)-t^2.
\]
If \(C=ab-2a-2b+3\), then among the graphs \(G_{a,b,t}\) with fixed \(a,b\), the maximizing values of \(t\) are exactly the integers in \([0,\min\{a,b\}]\) closest to \(C/2\).

For the balanced case \(a=b=n\), this gives a sharp transition: the maximizing deletion size is \(0\) for \(n=3\), either \(1\) or \(2\) for \(n=4\), \(4\) for \(n=5\), and the full perfect matching \(n\) for every \(n\ge6\). The crown graph satisfies
\[
\operatorname{gpn}(K_{n,n}-M_n)-\operatorname{gpn}(K_{n,n})=n(n^2-5n+3),
\]
so deleting a perfect matching strictly increases the invariant for every \(n\ge5\).

## Assumptions and scope
All graphs are finite, simple, and connected. The restriction \(a,b\ge3\) guarantees connectivity for every allowed matching deletion size. The geodesic subpath number is the number of shortest paths over all unordered vertex pairs, plus the \(a+b\) zero-length geodesics, following Knor, Sedlar, Škrekovski, and Zhang.

## Proof
Let the two parts be \(A=\{x_1,\ldots,x_a\}\) and \(B=\{y_1,\ldots,y_b\}\), and delete \(x_i y_i\) for \(1\le i\le t\).

Every surviving cross-part pair is adjacent and therefore contributes one geodesic; there are \(ab-t\) such pairs. For a deleted pair \(x_i,y_i\), bipartiteness rules out a path of length two, while every shortest path has the form
\[
x_i-y_j-x_k-y_i.
\]
Here \(j\ne i\) and \(k\ne i\). There are initially \((b-1)(a-1)\) choices. The middle edge fails exactly when \(j=k\le t\), and among the deleted indices there are \(t-1\) choices other than \(i\). Hence each deleted pair contributes
\[
(a-1)(b-1)-t+1
\]
geodesics.

For two vertices \(x_p,x_q\in A\), every geodesic has length two and is determined by a common neighbor in \(B\). Starting from \(b\) common neighbors in \(K_{a,b}\), one is lost when \(p\le t\) and one is lost when \(q\le t\). Summing over all pairs in \(A\) therefore gives
\[
b\binom{a}{2}-t(a-1).
\]
Similarly, pairs inside \(B\) contribute
\[
a\binom{b}{2}-t(b-1).
\]
Adding these four pair types and the \(a+b\) zero-length geodesics yields the stated formula after simplification.

For fixed \(a,b\), the only \(t\)-dependent term is
\[
t(C-t),\qquad C=ab-2a-2b+3.
\]
This is a strictly concave quadratic with real maximizer \(C/2\), so on the permitted integer interval its maximizers are exactly the nearest integer points after clipping to \([0,\min\{a,b\}]\). Substituting \(a=b=n\) gives the listed balanced cases. Setting \(t=n\) and subtracting the \(t=0\) value gives \(n(n^2-5n+3)\), which is positive exactly from \(n=5\) onward.

## Verification
A standalone verifier reconstructs \(G_{a,b,t}\), computes all shortest-path multiplicities by breadth-first search with dynamic path counting, and compares the resulting geodesic subpath number with the closed formula. It also checks the maximizing deletion sizes directly. The finite test covers every \(3\le a,b\le8\) and every admissible \(t\), totaling 199 parameter cases, plus the balanced transition for \(3\le n\le8\). The universal result does not depend on this finite experiment; it follows from the pair-type proof above.

## Relationship to prior work
Knor, Sedlar, Škrekovski, and Zhang introduced the geodesic subpath number in 2026. Their paper explicitly notes that removing a perfect matching from a balanced complete bipartite graph may increase the invariant and then asks for the maximal bipartite graphs of each order. The present formula resolves the entire one-parameter matching-deletion family around every complete bipartite graph and proves the suggested increase for all balanced orders \(2n\) with \(n\ge5\).

A separate 2026 result shows that balanced complete bipartite graphs maximize the geodesic subpath number among diameter-two graphs. That theorem does not imply the present result: as soon as \(t>0\), each deleted matched pair is at distance three in \(G_{a,b,t}\), so these graphs lie outside the diameter-two class.

Targeted searches for the invariant together with crown graphs, matching-deleted complete bipartite graphs, and arbitrary matching size did not locate a formula or a stronger theorem covering this statement.

## Limitations
This result optimizes only within graphs obtained from a fixed complete bipartite graph by deleting a matching. It does not characterize all bipartite maximizers, so the broader extremal problem remains open. The originality assessment is limited by the literature and semantic-index searches performed; an equivalent formula under terminology not surfaced by those searches remains a residual risk.

## References
1. M. Knor, J. Sedlar, R. Škrekovski, X.-D. Zhang, “Counting geodesic paths in graphs,” arXiv:2604.04907v1, first public 2026-04-06; Mediterranean Journal of Mathematics 23, Article 171 (2026), DOI 10.1007/s00009-026-03159-3.
2. “Balanced complete bipartite graphs uniquely maximize geodesic subpaths at diameter two,” public research record, 2026-09-17.
