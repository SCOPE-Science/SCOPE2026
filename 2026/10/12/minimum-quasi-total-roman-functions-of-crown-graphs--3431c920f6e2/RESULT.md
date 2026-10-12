# Minimum quasi-total Roman functions of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M,\qquad n\ge4,
\]
with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where \(M=\{a_i b_i:1\le i\le n\}\) is the deleted perfect matching. Then
\[
\gamma_{qtR}(\operatorname{Cr}_n)=6.
\]

Every minimum quasi-total Roman dominating function has exactly one label \(2\) and one label \(1\) in each bipartition class. Write
\[
f(a_i)=2,\qquad f(a_j)=1,\qquad f(b_k)=2,\qquad f(b_\ell)=1,
\]
and label all remaining vertices \(0\). Such a labeling is minimum exactly in one of these two cases:

\[
k=i,\qquad j\ne i,\qquad \ell\ne i,
\]
or
\[
k=j,\qquad \ell=i,\qquad i\ne j.
\]

Thus the two label-\(2\) vertices either occupy the same deleted matched pair, with independently chosen supporting label-\(1\) vertices off that pair, or they are crossed across two indices with the label-\(1\) vertices occupying the opposite matched positions.

The two families have respectively
\[
n(n-1)^2
\quad\text{and}\quad
n(n-1)
\]
members. Hence the exact number of minimum functions is
\[
n^2(n-1).
\]

## Assumptions and scope
A quasi-total Roman dominating function is a labeling
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex labeled \(0\) has a neighbor labeled \(2\), and every vertex labeled \(2\) has a positive-labeled neighbor. Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{qtR}(G)\) is the minimum weight.

The theorem is stated for \(n\ge4\). The boundary \(\operatorname{Cr}_3\cong C_6\) also has value \(6\), but that scalar case is covered by prior general theory for cycles and is not part of the originality claim.

## Proof
Suppose first that one bipartition class, say \(A\), contains no label \(2\). Then every vertex of \(B\) must be positive, since a zero in \(B\) would have no adjacent label \(2\). If \(B\) also contains no label \(2\), then every vertex of \(A\) must be positive, giving weight at least \(2n\).

If \(B\) contains a label \(2\), then \(B\) has weight at least \(n+1\), and some positive vertex in \(A\) is needed to support that label \(2\). Thus the total weight is at least \(n+2\ge6\). Equality at \(n=4\) is impossible: with one label \(2\) at \(b_i\), the sole positive vertex in \(A\) would have to be \(a_i\) to prevent \(a_i\) from being an undominated zero, but \(a_i\) is not adjacent to \(b_i\), leaving that label \(2\) unsupported. The same argument applies with the two sides interchanged.

Hence any function of weight at most \(6\) has a label \(2\) on each side.

If a weight-\(6\) function had at least three label-\(2\) vertices, then it would have no label \(1\). With two label \(2\)'s on one side and one on the other, the matched partner of the unique defender must itself be a label \(2\); that defender then has no positive neighbor outside its deleted matched partner. Thus three label-\(2\) vertices cannot realize weight \(6\).

Therefore every weight-\(6\) function has exactly one label \(2\) on each side and exactly two label \(1\)'s. Let
\[
f(a_i)=2,\qquad f(b_k)=2.
\]
Because \(a_i\) is the unique label \(2\) in \(A\), \(b_i\) cannot be \(0\). Similarly \(a_k\) cannot be \(0\).

If \(k=i\), these forced-positive vertices are already the two label-\(2\) vertices. Each label \(2\) must still have a positive neighbor away from the deleted matched edge, so the remaining two units must be one label \(1\) in each side at arbitrary indices
\[
j\ne i,\qquad \ell\ne i.
\]

If \(k\ne i\), then \(a_k\) and \(b_i\) are distinct from the two label-\(2\) vertices. Since exactly two units remain, they must be the two label-\(1\) vertices, so
\[
j=k,\qquad \ell=i.
\]

Conversely, every labeling in either family satisfies the quasi-total Roman conditions. This proves the classification, the value \(6\), and the count \(n^2(n-1)\).

## Verification
The included checker tests every ternary labeling for every crown graph with
\[
3\le n\le7.
\]
For \(4\le n\le7\), it independently confirms minimum weight \(6\), the two-family classification, and the count \(n^2(n-1)\). It examines \(5{,}380{,}749\) ternary labelings in total.

## Relationship to prior work
Quasi-total Roman domination was introduced in 2019 as an intermediate condition between Roman and total Roman domination. The introducing paper gives general inequalities and extremal characterizations; its inspected searchable full text contains no crown or complete-bipartite occurrence.

For complete multipartite graphs, a prior all-function theorem yields
\[
\gamma_{qtR}(K_{n,n})=4.
\]
Crown graphs arise by deleting a perfect matching from \(K_{n,n}\). That deletion removes exactly the adjacencies that support the weight-\(4\) complete-bipartite optimizers. The present theorem shows that the minimum rises to \(6\) for every \(n\ge4\) and classifies every optimizer after the deletion.

A 2022 paper studies quasi-total Roman bondage, including bipartite complexity and edge-deletion sensitivity, but the inspected material does not state this crown value or optimizer classification. Targeted searches under crown graph and complete-bipartite-minus-perfect-matching terminology did not locate an equivalent theorem.

## Limitations
The theorem classifies minimum functions, not all higher-weight quasi-total Roman functions. The boundary \(\operatorname{Cr}_3\) is exceptional: exhaustive verification gives \(37\) minimum functions of weight \(6\), while the scalar value itself is already covered by prior cycle theory. The finite computation is corroborative only; the arbitrary-\(n\) result follows from the proof. A differently phrased or non-indexed crown result may exist.

## References
1. S. Cabrera-García, A. Cabrera-Martínez, I. G. Yero, “Quasi-total Roman domination in graphs,” arXiv:1903.09789v1, 23 March 2019; Results in Mathematics 74 (2019), 173, DOI 10.1007/s00025-019-1097-5.
2. H. Jiang, Z. Shao, “Quasi-total Roman bondage number in graphs,” AKCE International Journal of Graphs and Combinatorics 19 (2022), 221–228, DOI 10.1080/09728600.2022.2098876.
