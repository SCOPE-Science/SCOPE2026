# Minimum positive semidefinite zero forcing sets of book graphs
## Finding
For every integer \(n\ge1\), let the book graph
\[
B_n=K_{1,n}\mathbin{\square}P_2
\]
have spine vertices \(a,b\) and, on page \(i\), vertices \(x_i,y_i\) with cycle \(a x_i y_i b a\). A two-vertex set \(S\subseteq V(B_n)\) is a minimum positive semidefinite zero forcing set if and only if it is one of the following:

1. the spine pair \(\{a,b\}\);
2. a same-page pair \(\{x_i,y_i\}\) for some \(1\le i\le n\);
3. a pair consisting of one spine vertex and one page vertex.

Hence
\[
Z_+(B_n)=2
\]
and the number of minimum positive semidefinite zero forcing sets is
\[
1+n+4n=5n+1.
\]
The equality \(Z_+(B_n)=2\) is known; the finding here is the complete classification and exact count of all minimum sets.

## Assumptions and scope
All graphs are finite, simple, and undirected. Positive semidefinite zero forcing uses the standard PSD color-change rule: if the current white graph has components \(W_1,\ldots,W_t\), a blue vertex may force a white vertex \(w\in W_j\) when \(w\) is its unique white neighbor inside \(W_j\).

The vertex set is
\[
\{a,b\}\cup\{x_i,y_i:1\le i\le n\},
\]
and the edge set consists of \(ab\) together with \(a x_i,x_i y_i,y_i b\) for every page \(i\). The statement includes \(n=1\), where \(B_1\cong C_4\).

## Proof
First, no singleton is a PSD forcing set. If the only blue vertex is a spine vertex, the white graph is connected and that blue vertex has at least two white neighbors. If the only blue vertex is a page vertex, the white graph is again connected and that blue vertex has its two cycle-neighbors white. Thus no first PSD force is available, so \(Z_+(B_n)\ge2\).

Each listed pair forces the graph.

For \(S=\{a,b\}\), the white graph has \(n\) components, namely the edges \(x_i y_i\). In each component, \(a\) has the unique white neighbor \(x_i\), so \(a\) can force \(x_i\); then \(y_i\) can be forced. Repeating page by page colors all vertices.

For \(S=\{x_i,y_i\}\), the blue vertex \(x_i\) has the unique white neighbor \(a\), and \(y_i\) has the unique white neighbor \(b\). After the spine is blue, the preceding page-by-page argument finishes the process.

Suppose \(S\) contains one spine vertex and one page vertex. By symmetry it is enough to use the spine vertex \(a\). If \(S=\{a,x_i\}\), then \(x_i\) has the unique white neighbor \(y_i\), so \(x_i\to y_i\), after which \(y_i\to b\). If \(S=\{a,y_i\}\), the vertex \(x_i\) is a singleton component of the initial white graph, so \(a\to x_i\); then \(y_i\to b\). In either case the spine becomes blue and all remaining pages clear.

It remains to exclude every other two-vertex set. The only unlisted possibility consists of page vertices from two distinct pages. After removing those two blue vertices, the white graph is connected: the white spine edge \(ab\) remains, and every white page vertex is joined to that edge through its surviving page path. Each of the two blue page vertices has both of its cycle-neighbors white, hence neither has a unique white neighbor. Therefore no first PSD force exists, so such a pair is not forcing.

These cases exhaust all two-vertex sets. Together with the singleton obstruction, they prove the classification and the count \(1+n+4n=5n+1\).

## Verification
The accompanying \(\texttt{verify.py}\) constructs \(B_n\) directly from the edge definition, implements the PSD color-change rule by recomputing the connected components of the current white graph, and exhausts every singleton and every two-vertex set for \(1\le n\le12\). It compares each pair against the structural classification and checks the count \(5n+1\) independently at every tested order.

The computation is a finite regression check only. The theorem for all \(n\ge1\) follows from the symbolic proof above, not from extrapolation.

## Relationship to prior work
Barioli, Barrett, Fallat, Hall, Hogben, Shader, van den Driessche, and van der Holst introduced positive semidefinite zero forcing in arXiv:1003.2028v1, first posted on 2010-03-10. The arXiv record lists primary MSC 05C50. Their paper supplies the general PSD forcing framework but does not name the book graph in its searchable full text.

Hogben, Lin, and Shader, *Inverse Problems and Zero Forcing for Graphs*, Example 9.53, explicitly records the same book graph \(B_n=K_{1,n}\mathbin{\square}P_2\) and the scalar value \(Z_+(B_n)=2\). That scalar is therefore not claimed as new. The present statement refines it by identifying every optimal initial pair and counting them exactly.

Searches for the same graph under the names “book graph,” “square book graph,” and \(K_{1,n}\mathbin{\square}P_2\), together with searches for PSD forcing bases and minimum sets, did not retrieve a prior all-minimum-set classification. This absence is evidence from the checked literature, not a proof that no unindexed source exists.

## Limitations
The result classifies only minimum PSD zero forcing sets; it does not enumerate larger PSD forcing sets or determine PSD propagation-time distributions. The literature comparison establishes that the scalar minimum is prior work and that no checked source stated the retained classification; an unindexed or inaccessible source could still contain an equivalent basis classification.

## References
1. F. Barioli, W. Barrett, S. M. Fallat, H. T. Hall, L. Hogben, B. Shader, P. van den Driessche, H. van der Holst, “Zero forcing parameters and minimum rank problems,” arXiv:1003.2028v1, 2010-03-10; DOI 10.1016/j.laa.2010.03.008.
2. L. Hogben, J. C.-H. Lin, B. L. Shader, *Inverse Problems and Zero Forcing for Graphs*, Mathematical Surveys and Monographs 270, American Mathematical Society, 2022, Example 9.53; DOI 10.1090/surv/270.
