# Exact weight enumerator of total Roman dominating functions on complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite sets \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). A total Roman dominating function is a labeling \(f:V(G)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\), and the subgraph induced by the positive-labeled vertices has no isolated vertex.

For each part, let \(z_i,o_i,t_i\) denote the numbers of labels \(0,1,2\) in \(V_i\), set \(p_i=o_i+t_i\), and put \(T=\sum_i t_i\). Then \(f\) is a total Roman dominating function if and only if
\[
|\{i:p_i>0\}|\ge2
\]
and
\[
z_i>0\quad\Longrightarrow\quad T-t_i>0
\]
for every \(i\). In words, positive labels must occur in at least two parts, and every part containing a zero must have a label \(2\) outside that part.

Define the weight enumerator
\[
R_{tR}(G;x)=\sum_{f\text{ total Roman}}x^{\omega(f)},\qquad \omega(f)=\sum_{v\in V(G)}f(v).
\]
For each \(i\), put
\[
A_i(x)=(1+x)^{n_i},\qquad B_i(x)=(1+x+x^2)^{n_i}-(1+x)^{n_i},
\]
and
\[
C_i(x)=(x+x^2)^{n_i}-x^{n_i}.
\]
Then
\[
R_{tR}(G;x)=(1+x+x^2)^N-(1+x)^N-\sum_{i=1}^r B_i(x)(1+x)^{N-n_i}+\sum_{i=1}^r C_i(x)\big((1+x)^{N-n_i}-1\big)+x^N.
\]
In particular, if \(m=\min_i n_i\), then
\[
\gamma_{tR}(G)=\min\{N,4,m+2\}.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The theorem assumes \(r\ge2\) and \(n_i\ge1\), so the complete multipartite graph is connected and has no isolated vertices. The total Roman definition is the ordinary \(\{0,1,2\}\)-label version: it is the \(a=1,b=2\) specialization of the more general total \((a,b)\)-Roman framework.

The displayed polynomial counts every total Roman dominating function by its weight; it is not merely a formula for the minimum weight. The scalar formula for \(\gamma_{tR}\) is recorded as a corollary and is not the novelty-bearing part of the result.

## Proof
Adjacency in a complete multipartite graph occurs exactly between distinct parts.

First consider the totality requirement. A positive-labeled vertex in \(V_i\) has a positive-labeled neighbor if and only if some other part \(V_j\), with \(j\ne i\), contains a positive label. Therefore the positive-induced subgraph has no isolated vertex if and only if positive labels occur in at least two parts. This is exactly \(|\{i:p_i>0\}|\ge2\).

Next consider the Roman requirement. A zero-labeled vertex in \(V_i\) is adjacent to every vertex outside \(V_i\) and to no vertex inside \(V_i\). Hence it has a neighbor labeled \(2\) if and only if at least one label \(2\) occurs outside \(V_i\), equivalently \(T-t_i>0\). If \(z_i=0\), there is no Roman condition to check in that part. This proves the structural characterization.

For the enumerator, partition all labelings into three disjoint cases according to the set of parts containing a label \(2\).

If labels \(2\) occur in at least two parts, both requirements hold automatically once a \(2\) exists in two distinct parts: every zero sees a \(2\) in another part, and the positive support meets at least two parts. The weight generating function for all labelings with labels \(2\) in at least two parts is
\[
(1+x+x^2)^N-(1+x)^N-\sum_i B_i(x)(1+x)^{N-n_i}.
\]
The subtracted \((1+x)^N\) term is the no-\(2\) case. For each \(i\), the product \(B_i(x)(1+x)^{N-n_i}\) counts labelings whose labels \(2\) occur in exactly the single part \(V_i\).

Suppose labels \(2\) occur in exactly one part \(V_i\). Any zero in \(V_i\) would have no \(2\)-neighbor, so every vertex of \(V_i\) must be positive; at least one of them is labeled \(2\). This contributes \(C_i(x)\). Totality additionally requires at least one positive vertex outside \(V_i\), contributing \((1+x)^{N-n_i}-1\). Summing over \(i\) gives
\[
\sum_i C_i(x)\big((1+x)^{N-n_i}-1\big).
\]

Finally, if no vertex receives label \(2\), the Roman condition forces every vertex to be positive, so the only valid labeling is the all-one labeling, contributing \(x^N\). Adding the three disjoint cases proves the formula.

For the minimum-weight corollary, the no-\(2\) case has weight \(N\). If \(2\)'s occur in at least two parts, weight at least \(4\) is necessary and is attained by assigning \(2\) to one vertex in each of two parts and \(0\) elsewhere. If \(2\)'s occur in exactly one part \(V_i\), that entire part is positive and at least one positive label is required outside it; the least possible weight is \(n_i+2\), attained by one \(2\), \(n_i-1\) labels \(1\) in \(V_i\), and one label \(1\) outside. Minimizing over \(i\) yields \(\min\{N,4,m+2\}\).

## Verification
The standalone verifier constructs every complete multipartite profile of order at most \(9\), checks every \(\{0,1,2\}\)-labeling against the literal graph definition and against the part-profile criterion, independently expands the displayed polynomial, compares every coefficient with brute-force counts, and checks the minimum-weight corollary. Its successful replay reports:

`VERIFY_OK profiles=87 labelings=748341 coefficient_checks=1369 minimum_checks=87 max_order=9`

This finite census is regression evidence only. The infinite statement is proved by the part-adjacency argument above.

## Relationship to prior work
Liu and Chang introduced total \((a,b)\)-Roman domination in a more general framework; their accessible abstract states complexity results on bipartite and chordal graphs and linear algorithms for ordinary and independent variants on strongly chordal graphs. Ahangar, Henning, Samodivkin, and Yero subsequently developed total Roman domination as the \(\{0,1,2\}\)-label invariant used here and proved general bounds and structural relations. The accessible full text of that paper contains no occurrence of “multipartite” or “complete bipartite.”

The closest exact published-database record found for complete multipartite graphs concerns total **strong** Roman domination, a different defensive rule. General minimum-value bounds and algorithms do not determine which nonminimum labelings are valid or the coefficient sequence of the all-function weight enumerator. Searches using the aliases “total Roman domination,” “total \((a,b)\)-Roman domination,” “complete bipartite,” and “complete multipartite” did not surface an ordinary complete-multipartite all-function formula.

## Limitations
The claim is restricted to connected complete multipartite graphs and ordinary total Roman domination. It does not claim a classification for total strong, signed total Roman, double Roman, or other Roman-type variants.

The full text of the 2013 Liu--Chang paper was not publicly available in the inspected sources; its abstract was inspected and does not expose an all-function complete-multipartite theorem. This leaves a residual bibliographic risk from special cases hidden in inaccessible older text or indexed under alternate terminology. The scalar minimum formula is not relied on as the originality-bearing contribution.

## References
1. C.-H. Liu and G. J. Chang, “Roman domination on strongly chordal graphs,” *Journal of Combinatorial Optimization* 26 (2013), 608–619. DOI: 10.1007/s10878-012-9482-y.
2. H. Abdollahzadeh Ahangar, M. A. Henning, V. Samodivkin, and I. G. Yero, “Total Roman domination in graphs,” *Applicable Analysis and Discrete Mathematics* 10 (2016), 501–517. DOI: 10.2298/AADM160802017A.
