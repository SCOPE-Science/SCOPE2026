# All positive semidefinite zero forcing sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\ge2\), \(n_i\ge1\), partite classes \(V_1,\ldots,V_r\), and \(N=\sum_{i=1}^r n_i\). For an initial blue set \(S\subseteq V(G)\), write
\[
W_i=V_i\setminus S,\qquad w_i=|W_i|.
\]
Then \(S\) is a positive semidefinite zero forcing set if and only if one of the following mutually compatible conditions holds:

1. at most one of the numbers \(w_i\) is positive; or
2. there is an index \(i\) for which \(0<w_i<n_i\) and
\[
\sum_{j\ne i}w_j=1.
\]

Thus, whenever white vertices occupy at least two parts, they occupy exactly two parts: one occupied part contains exactly one white vertex, while the other occupied part is only partially white.

Define the cardinality enumerator
\[
\mathcal Z_+(G;x)=\sum_{S\text{ PSD zero forcing}}x^{|S|},
\]
and put
\[
R_n(x)=(1+x)^n-1-x^n,
\]
\[
E_{a,b}(x)=a x^{a-1}R_b(x)+b x^{b-1}R_a(x)-\mathbf 1_{a\ge2,\,b\ge2}abx^{a+b-2}.
\]
Then
\[
\mathcal Z_+(K_{n_1,\ldots,n_r};x)
=x^N+\sum_{i=1}^r x^{N-n_i}\big((1+x)^{n_i}-x^{n_i}\big)
+\sum_{1\le i<j\le r}x^{N-n_i-n_j}E_{n_i,n_j}(x).
\]
If \(m=\max_i n_i\), this gives
\[
Z_+(G)=N-m.
\]
The scalar equality is known; the all-set characterization and enumerator are the finding here.

## Assumptions and scope
Graphs are finite, simple, and undirected. Positive semidefinite zero forcing uses the standard componentwise color-change rule: at each stage, form the connected components of the subgraph induced by the current white vertices; a blue vertex may force a white vertex inside a white component when it has exactly one white neighbor in that component. The theorem covers every complete multipartite graph with at least two nonempty parts, including singleton parts.

## Proof
Suppose first that the white vertices lie in at most one part, say \(V_i\). Because there are no edges inside a part, every current white vertex is a one-vertex component of the white induced graph. Every vertex outside \(V_i\) is blue, and any such blue vertex is adjacent to each white vertex in \(V_i\). Relative to a one-vertex white component, it therefore has exactly one white neighbor, so the white vertices can be forced one component at a time. Hence every configuration with white support in at most one part is positive semidefinite zero forcing.

Now suppose white vertices occupy at least two parts. Their induced subgraph is connected, since vertices in distinct partite classes are adjacent. Before the first force, a blue vertex \(u\in V_i\) has exactly
\[
\sum_{j\ne i}w_j
\]
white neighbors in this single white component. Therefore a first force exists exactly when \(V_i\) contains a blue vertex, equivalently \(w_i<n_i\), and
\[
\sum_{j\ne i}w_j=1.
\]
Because the white support contains at least two parts, the forcing part also has \(w_i>0\). The displayed equality says that all white vertices outside \(V_i\) consist of a single vertex, so exactly two parts are occupied by white vertices. After that unique outside white vertex is forced, all remaining white vertices lie in \(V_i\), which is the first case and can be cleared component by component. Conversely, if no such index \(i\) exists, the connected white component admits no first force, so the process is stalled. This proves the characterization.

For the enumerator, separate the forcing sets by the support of their white complements. The all-blue set contributes \(x^N\). If the white complement is nonempty and supported only in \(V_i\), every vertex outside \(V_i\) is blue and the blue subset inside \(V_i\) may be any proper subset; this contributes
\[
x^{N-n_i}\big((1+x)^{n_i}-x^{n_i}\big).
\]
If exactly two parts of sizes \(a\) and \(b\) contain white vertices, the characterization says either there is one white vertex in the first part and a nonempty proper white subset in the second, or conversely. The corresponding blue-set generating polynomial is
\[
a x^{a-1}R_b(x)+b x^{b-1}R_a(x).
\]
When \(a,b\ge2\), configurations with one white vertex in each part have been counted twice, contributing \(abx^{a+b-2}\); subtracting this term gives \(E_{a,b}(x)\). Multiplying by \(x^{N-a-b}\) accounts for the parts outside the pair, which are entirely blue. Summing over all parts and all unordered pairs proves the polynomial formula.

Finally, a forcing configuration can leave at most \(m=\max_i n_i\) white vertices. This is attained by leaving an entire largest part white. If whites occupy two parts, the characterization gives at most \((m-1)+1=m\) whites. Hence the minimum blue cardinality is \(N-m\).

## Verification
The accompanying script `artifacts/verify.py` directly implements the positive semidefinite color-change rule, independently implements the stated occupancy criterion, and compares them for every vertex subset of every ordered part-size profile with two through four parts, each part of size one through four, and total order at most eleven. It also compares every coefficient of the closed enumerator with exhaustive counts and checks the minimum-size corollary. Its replay output is:

`VERIFY_OK profiles=269 subset_checks=182540 criterion_checks=182540 coefficient_checks=2529 minimum_checks=269 max_order=11`

The finite computation is a stress test, not the proof for arbitrary part sizes; the arbitrary-size conclusion follows from the first-force analysis above.

## Relationship to prior work
Barioli et al. introduced positive semidefinite zero forcing. Peters subsequently proved for \(n_1\ge\cdots\ge n_r>0\) that
\[
Z_+(K_{n_1,\ldots,n_r})=n_2+\cdots+n_r=N-n_1,
\]
so the scalar minimum is prior work and is not claimed as new. The present result determines exactly which initial sets succeed, including all nonminimum cardinalities, and packages that classification as a closed cardinality enumerator.

Boyer et al. introduced the ordinary zero forcing polynomial, which counts initial sets under the ordinary color-change rule. Positive semidefinite forcing uses the white-component decomposition and can behave differently even on complete bipartite graphs, so ordinary zero-forcing-set formulas do not imply the classification here.

## Limitations
The theorem is confined to complete multipartite graphs and to the positive semidefinite color-change rule. The exhaustive verifier covers only finite instances of order at most eleven; it supports but does not replace the all-size proof. The literature search cannot rule out an unindexed thesis, note, or alternate terminology containing the same all-set classification, so residual bibliographic risk is nonzero.

## References
1. F. Barioli, W. Barrett, S. M. Fallat, H. T. Hall, L. Hogben, B. Shader, P. van den Driessche, and H. van der Holst, “Zero forcing parameters and minimum rank problems,” arXiv:1003.2028, first posted 2010-03-10.
2. T. Peters, “Positive semidefinite maximum nullity and zero forcing number,” Electronic Journal of Linear Algebra 23 (2012), 815–830. Proposition 3.4 gives the complete multipartite scalar value.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910, first posted 2018-01-26.
