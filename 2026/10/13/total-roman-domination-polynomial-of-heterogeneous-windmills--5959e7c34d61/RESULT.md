# Total Roman domination polynomial of heterogeneous windmills
## Finding
For integers \(r\ge2\) and \(m_1,\ldots,m_r\ge2\), let
\[
W(m_1,\ldots,m_r)=K_1\vee\left(K_{m_1}\cup\cdots\cup K_{m_r}\right),
\]
with universal center \(c\), and put \(M=\sum_{i=1}^r m_i\). A total Roman dominating function is a map \(f:V(W)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\), and the subgraph induced by vertices of positive label has no isolated vertex. Define its weight by \(\omega(f)=\sum_{v\in V(W)}f(v)\), and define
\[
\mathcal T_W(x)=\sum_f x^{\omega(f)},
\]
where the sum ranges over all total Roman dominating functions.

For \(m\ge2\), set
\[
T_m(x)=(1+x+x^2)^m-(1+x)^m+x^m,
\qquad
U_m(x)=T_m(x)-m x^2.
\]
Then
\[
\mathcal T_W(x)
=x^2\bigl((1+x+x^2)^M-1\bigr)
+x\prod_{i=1}^r T_{m_i}(x)
+\prod_{i=1}^r U_{m_i}(x)-x^M.
\]
Consequently, the total number of total Roman dominating functions is
\[
3^M+
\prod_{i=1}^r\bigl(3^{m_i}-2^{m_i}+1\bigr)
+
\prod_{i=1}^r\bigl(3^{m_i}-2^{m_i}+1-m_i\bigr)-2.
\]
Moreover,
\[
\gamma_{tR}(W(m_1,\ldots,m_r))=3,
\]
and there are exactly \(M\) minimum-weight functions. They are precisely the functions with \(f(c)=2\), one peripheral vertex labeled \(1\), and every other peripheral vertex labeled \(0\).

## Assumptions and scope
The graph is finite, simple, and has at least two clique blades, each of order at least two. The result concerns the ordinary total Roman predicate with label set \(\{0,1,2\}\). No assertion is made for total Roman variants with different label sets, for one-blade complete graphs, or for blades of order one.

## Proof
Partition the functions by the label at the center.

If \(f(c)=2\), every peripheral zero is already defended by \(c\). The positive-support condition is then equivalent to requiring at least one positive peripheral vertex, because every positive peripheral vertex is adjacent to \(c\). Thus this case contributes
\[
x^2\bigl((1+x+x^2)^M-1\bigr).
\]

If \(f(c)=1\), a zero in a blade can only be defended by a label \(2\) in the same blade. For a blade of order \(m\), all \(3^m\) labelings are allowed except those using only labels \(0,1\) and containing at least one \(0\). Their weight polynomial is \((1+x)^m-x^m\), so the valid blade polynomial is \(T_m(x)\). Every such valid blade contains a positive vertex; therefore the center has a positive neighbor, and every positive peripheral vertex is adjacent to the positive center. Hence this case contributes
\[
x\prod_{i=1}^r T_{m_i}(x).
\]

If \(f(c)=0\), different blades do not help one another. Within each blade, every zero must have a local label \(2\), and the positive vertices in that blade may not contain an isolated vertex. Starting from \(T_m(x)\), the only additional forbidden blade states are those with exactly one positive vertex; the single positive must be a \(2\), giving \(m x^2\). Hence the admissible blade polynomial is \(U_m(x)\). The center itself must also have a neighbor labeled \(2\). Among products of admissible blade states, the unique global state containing no \(2\) is the all-ones peripheral labeling, of weight \(M\). Therefore this case contributes
\[
\prod_{i=1}^r U_{m_i}(x)-x^M.
\]
Summing the three disjoint center cases proves the polynomial formula. Substitution \(x=1\) gives the total count.

For the minimum, the center-\(2\) contribution has least weight \(3\), attained by choosing exactly one peripheral label \(1\), giving \(M\) functions. In the center-\(1\) case each blade has weight at least \(2\), so the total weight is at least \(1+2r\ge5\). In the center-\(0\) case each blade has at least two positive vertices or otherwise fails one of the two defining conditions, so weight \(3\) is impossible. Thus the minimum is exactly \(3\), with the stated complete classification.

## Verification
The symbolic proof is exhaustive in the three possible center labels. As a finite regression check, `verify.py` exhaustively enumerates all \(3^{|V|}\) labelings for six heterogeneous or homogeneous parameter tuples, compares every coefficient with the closed formula, checks the total count, and checks the complete weight-\(3\) layer. The replayed output is:

`VERIFY_OK cases=6 labelings=14094 valid_functions=7531 coefficient_checks=86 minimum_checks=6 total_checks=6 max_order=8`

The computation is not used as a proof for arbitrary parameters.

## Relationship to prior work
Liu and Chang introduced total \((a,b)\)-Roman domination in a general setting; for \((a,b)=(1,2)\) this is the predicate used here. Their published article establishes complexity results and related algorithms, but does not provide this all-function windmill enumerator. Ahangar, Henning, Samodivkin, and Yero subsequently developed total Roman domination as a graph parameter, giving bounds, relationships with other domination parameters, and extremal results. The inspected full text does not state the heterogeneous-windmill coefficient formula above.

A published-results search under the aliases “total Roman domination”, “total \((1,2)\)-Roman domination”, “windmill”, “friendship graph”, and \(K_1\) joined to disjoint cliques found the closest coefficientwise result for complete multipartite graphs. That theorem does not imply the present claim: a heterogeneous windmill with at least two nontrivial clique blades is not complete multipartite, since vertices inside a blade are adjacent while vertices in distinct blades are nonadjacent. Results for ordinary, weak, strong, or other Roman variants use different feasibility predicates and likewise do not imply this total-support classification.

## Limitations
The formula is proved only for \(r\ge2\) and \(m_i\ge2\). The literature search cannot exclude an unindexed family-specific result, so that remains the principal originality risk. The finite verifier checks orders only through eight vertices; correctness for the infinite family rests on the symbolic center-state proof.

## References
1. C.-H. Liu and G. J. Chang, “Roman domination on strongly chordal graphs,” *Journal of Combinatorial Optimization* 26 (2013), 608–619. Published online 10 April 2012. DOI: 10.1007/s10878-012-9482-y.
2. H. Abdollahzadeh Ahangar, M. A. Henning, V. Samodivkin, and I. G. Yero, “Total Roman Domination in Graphs,” *Applicable Analysis and Discrete Mathematics* 10 (2016), 501–517. DOI: 10.2298/AADM160802017A.
