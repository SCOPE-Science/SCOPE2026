# Vertex–edge Roman \(\{2\}\) weight enumerator of crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph for \(n\ge3\), with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(a_i b_i\). A vertex–edge Roman \(\{2\}\)-dominating function is a map \(f:V(\operatorname{Cr}_n)\to\{0,1,2\}\) such that every edge with two zero-labeled endpoints sees total label at least \(2\) on the union of the endpoints' open neighborhoods. Define its all-function weight enumerator by
\[
V_n(z)=\sum_f z^{w(f)},\qquad w(f)=\sum_{v}f(v),
\]
where the sum runs over all vertex–edge Roman \(\{2\}\)-dominating functions. Then
\[
\begin{aligned}
V_n(z)={}&(1+z+z^2)^{2n}-1-2nz-2n^2z^2\\
&-n(n-1)(n+2)z^3-n(n-1)(3n-5)z^4\\
&-2n(n-1)(n-2)z^5.
\end{aligned}
\]
In particular,
\[
\gamma_{veR2}(\operatorname{Cr}_n)=2,
\]
and the minimum functions are exactly the \(n\) functions that put label \(1\) on both endpoints of one deleted matching pair and label \(0\) everywhere else.

For comparison, every labeling of \(K_{n,n}\) of weight at least \(2\) is vertex–edge Roman \(\{2\}\)-dominating, so its enumerator is \((1+z+z^2)^{2n}-1-2nz\). Deleting one perfect matching therefore changes feasibility only in weights \(2,3,4,5\), while leaving the minimum weight equal to \(2\).
## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem is stated for \(n\ge3\). The disconnected graph \(\operatorname{Cr}_2\cong2K_2\) is deliberately excluded because its low-weight orbit structure has extra boundary coincidences.

Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), and \(W=w(f)\). All labels lie in \(\{0,1,2\}\). The theorem counts labeled functions, not functions modulo graph automorphisms.
## Proof
For an edge \(a_i b_j\) with \(i\ne j\),
\[
N(a_i)\cup N(b_j)=\bigl(B\setminus\{b_i\}\bigr)\cup\bigl(A\setminus\{a_j\}\bigr).
\]
Hence, if \(x_i=y_j=0\), the vertex–edge Roman \(\{2\}\) condition on this edge is exactly
\[
W-x_j-y_i\ge2.
\]
Therefore a labeling is invalid if and only if there exist distinct indices \(i,j\) such that
\[
x_i=y_j=0,\qquad x_j+y_i\ge W-1.
\]
Because \(x_j+y_i\le4\), every labeling of weight \(W\ge6\) is automatically valid. Thus all failures occur at weights at most \(5\).

The invalid low-weight labelings can now be classified completely. In the following list, a pair \((p,q)\) means that one deleted matching pair receives labels \(p\) on its \(A\)-vertex and \(q\) on its \(B\)-vertex; all displayed pair indices are distinct, and the listed counts already include interchange of the two shores.

| Weight | Invalid nonzero pair patterns | Total invalid count |
| --- | --- | ---: |
| \(0\) | no nonzero labels | \(1\) |
| \(1\) | \((1,0)\) | \(2n\) |
| \(2\) | \((2,0)\); \((1,0),(1,0)\); \((1,0),(0,1)\) | \(2n^2\) |
| \(3\) | \((2,0),(1,0)\); \((2,0),(0,1)\); \((1,0),(1,0),(0,1)\) | \(n(n-1)(n+2)\) |
| \(4\) | \((2,0),(0,2)\); \((2,0),(1,0),(0,1)\); \((2,0),(0,1),(0,1)\) | \(n(n-1)(3n-5)\) |
| \(5\) | \((2,0),(0,2),(1,0)\) | \(2n(n-1)(n-2)\) |

To see that the table is exhaustive, fix a violating edge \(a_i b_j\). The two labels omitted from its neighborhood union are \(x_j\) and \(y_i\), and they must sum to at least \(W-1\). For \(W=5\) this forces \((x_j,y_i)=(2,2)\); for \(W=4\) it forces sums \(4\) or \(3\); for \(W=3\) it forces a sum at least \(2\); and the weights \(0,1,2\) follow similarly. The endpoint conditions \(x_i=y_j=0\) force the remaining positive labels onto the distinct matching-pair patterns shown. Conversely, each displayed pattern has an evident violating edge, so no pattern is spurious.

The counts are direct. For example, at weight \(3\), the first two patterns contribute \(2n(n-1)\) each, and the three-one pattern contributes \(n(n-1)(n-2)\), totaling \(n(n-1)(n+2)\). At weight \(4\), the three pattern counts are \(n(n-1)\), \(2n(n-1)(n-2)\), and \(n(n-1)(n-2)\), totaling \(n(n-1)(3n-5)\). The weight-\(5\) count is \(2n(n-1)(n-2)\).

There are \((1+z+z^2)^{2n}\) total labelings by weight. Subtracting exactly the invalid counts from weights \(0\) through \(5\) gives the displayed polynomial. Its coefficient at \(z^2\) is
\[
\left(2n+\binom{2n}{2}\right)-2n^2=n,
\]
which proves both \(\gamma_{veR2}(\operatorname{Cr}_n)=2\) and the stated classification of all minimum functions.
## Verification
The standalone checker `verify.py` reconstructs the graph condition directly. For every \(3\le n\le6\), it exhaustively enumerates all \(3^{2n}\) labelings, compares the complete weight distribution with the polynomial formula, and verifies that the weight-\(2\) functions are exactly the deleted-matching pairs labeled \((1,1)\). It also checks the six closed-form invalid-count coefficients for \(3\le n\le30\) against an independent low-weight combinatorial enumeration.

The stored replay output is:

`ALL CHECKS PASSED; exhaustive_orders=[3, 4, 5, 6]; exhaustive_labelings=597780; low_weight_orders=28; minimum_functions_checked=18`

These computations are finite stress tests. The proof for arbitrary \(n\ge3\) is the neighborhood-union reduction and exhaustive symbolic classification above.
## Relationship to prior work
Almulhim and Mondal introduced vertex–edge Roman \(\{2\}\)-domination in 2025. Their definition is exactly the one used here. Their paper determines exact values for paths and cycles, proves tree bounds, and proves NP-completeness for bipartite graphs. The inspected full article contains no crown-graph, complete-bipartite, polynomial, or enumerator treatment. Thus the present result supplies a canonical dense regular bipartite family and, more strongly, counts every feasible labeling by weight rather than only determining the minimum.

Ordinary Roman \(\{2\}\)-domination, also called Italian domination, imposes the label-sum condition separately at every zero vertex and is strictly stronger than the edge-based condition. The minimum functions exhibited here are not ordinary Roman \(\{2\}\)-dominating functions: a zero vertex off the selected deleted pair sees only one unit of positive weight. Thus vertexwise Roman \(\{2\}\) results do not imply the edge-based enumerator.

A recent indexed result gives the all-weight Roman \(\{2\}\) enumerator for complete multipartite graphs, but it concerns the vertexwise invariant and a different graph class: \(\operatorname{Cr}_n\) is not complete multipartite for \(n\ge3\). Other indexed crown-graph results concern restrained domination and unrelated invariants, so they do not imply the low-weight defect polynomial above.
## Limitations
The theorem treats crown graphs with \(n\ge3\) only. It does not claim an all-function formula for arbitrary matching-deleted bicliques or general bipartite graphs. The originality search cannot exclude an unindexed equivalent enumerator under different terminology, although targeted searches under vertex–edge Roman \(\{2\}\), veR2DF, crown graph, complete bipartite graph, and matching-deleted biclique found no covering statement. The finite verifier is not an infinite proof.
## References
1. A. Almulhim and S. R. Mondal, “Vertex–Edge Roman \(\{2\}\)-Domination,” *Mathematics* 13 (2025), 2169, DOI 10.3390/math13132169, published 2 July 2025.
