# Double Roman weight enumerator of complete split graphs
## Finding
For integers \(r,n\ge 2\), let \(S_{r,n}=K_ree\overline{K_n}\), with clique part \(C\) of size \(r\) and independent part \(I\) of size \(n\). A double Roman dominating function is a map \(f:V(S_{r,n})	o\{0,1,2,3\}\) such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), and every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\). Write \(\omega(f)=\sum_v f(v)\) and
\[
\mathcal D_{r,n}(x)=\sum_f x^{\omega(f)}.
\]
Put
\[
A=1+x+x^2+x^3,\qquad B=1+x,\qquad C_1=x+x^2+x^3,\qquad D=x^2+x^3.
\]
Then
\[
\mathcal D_{r,n}(x)=igl(A^r-B^r-rx^2B^{r-1}igr)A^n
+rx^2\Bigl(B^{r-1}C_1^n-igl(B^{r-1}-x^{r-1}igr)x^n\Bigr)
+B^rD^n.
\]
In particular, \(\gamma_{dR}(S_{r,n})=3\), exactly \(r\) minimum-weight functions exist, and the total number of double Roman dominating functions is
\[
igl(4^r-2^r-r2^{r-1}igr)4^n+r\Bigl(2^{r-1}3^n-igl(2^{r-1}-1igr)\Bigr)+2^{r+n}.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The parameters satisfy \(r,n\ge 2\). The restriction \(n\ge2\) is used only in the final case of the proof, where two independent vertices labeled \(2\) can jointly defend a clique vertex labeled \(0\). The polynomial counts every double Roman dominating function, not merely minimum-weight functions.

The clique part is complete and every clique vertex is adjacent to every independent vertex; independent vertices have no neighbors inside \(I\).

## Proof
Let \(a\) and \(b\) be the numbers of clique vertices labeled \(2\) and \(3\), respectively. We partition all labelings into three disjoint cases.

**Case 1: \(b\ge1\) or \(a\ge2\).** Every clique vertex labeled \(0\) is already defended inside the clique, every clique vertex labeled \(1\) sees a clique label at least \(2\), and every independent vertex labeled \(0\) or \(1\) is also defended from the clique. Hence every labeling of \(I\) is allowed. The clique-label generating polynomial for this case is obtained from \(A^r\) by removing the cases with no clique label \(3\) and at most one clique label \(2\):
\[
A^r-B^r-rx^2B^{r-1}.
\]
Thus this case contributes
\[
igl(A^r-B^r-rx^2B^{r-1}igr)A^n.
\]

**Case 2: \(b=0\) and \(a=1\).** An independent vertex cannot be labeled \(0\), because it sees only one clique vertex labeled \(2\); labels \(1,2,3\) are allowed. Choose the unique clique vertex labeled \(2\), contributing \(rx^2\), and label the other \(r-1\) clique vertices by \(0\) or \(1\). If none of those vertices is labeled \(0\), then no extra condition is imposed on \(I\), giving \(x^{r-1}C_1^n\). If at least one clique vertex is labeled \(0\), then some independent vertex must be labeled \(2\) or \(3\) so that this clique zero sees either a second label \(2\) or a label \(3\). Hence the contribution is
\[
rx^2\left[x^{r-1}C_1^n+igl(B^{r-1}-x^{r-1}igr)igl(C_1^n-x^nigr)ight],
\]
which equals
\[
rx^2\Bigl(B^{r-1}C_1^n-igl(B^{r-1}-x^{r-1}igr)x^n\Bigr).
\]

**Case 3: \(a=b=0\).** Every independent vertex must be labeled \(2\) or \(3\): an independent label \(0\) or \(1\) would have no suitable neighbor in the clique. The clique vertices may independently receive labels \(0\) or \(1\). Since \(n\ge2\), any clique vertex labeled \(0\) sees either an independent label \(3\), or, if no independent vertex is labeled \(3\), at least two independent vertices labeled \(2\). Clique vertices labeled \(1\) see an independent label at least \(2\). Therefore this case contributes \(B^rD^n\).

The three cases are exhaustive and disjoint, proving the polynomial identity.

For the minimum, one clique vertex labeled \(3\) with all other vertices labeled \(0\) has weight \(3\), so \(\gamma_{dR}\le3\). A nontrivial graph cannot admit a double Roman dominating function of weight below \(3\): a lone label \(2\) cannot defend a label \(0\), while labels of total weight at most \(2\) cannot provide either a label \(3\) or two labels \(2\). Thus \(\gamma_{dR}=3\). A weight-\(3\) function must consist of one label \(3\) and zeros elsewhere; the label \(3\) must be universal, hence it must lie in \(C\). There are exactly \(r\) choices.

Finally, substituting \(x=1\) into the polynomial gives the displayed total count.

## Verification
The accompanying `verify.py` exhaustively enumerates every labeling in \(\{0,1,2,3\}^{r+n}\) for all \((r,n)\in\{2,3,4\}^2\). It checks the defining double Roman conditions directly from adjacency, compares every weight coefficient with the closed formula, checks the minimum weight and the number of minimum functions, and checks the total-count specialization. The finite replay is a boundary and algebra check; the all-orders conclusion comes from the case proof above.

## Relationship to prior work
Beeler, Haynes, and Hedetniemi introduced double Roman domination in 2016. A later threshold-graph paper gives algorithms for the scalar double Roman domination number on threshold graphs, a class containing complete split graphs, but does not enumerate all feasible functions by weight. Cariaga and Jamil prove general scalar results for joins and, in particular, that a nontrivial connected graph has double Roman domination number \(3\) exactly when its ordinary domination number is \(1\). Since every \(S_{r,n}\) has universal clique vertices, the scalar equality \(\gamma_{dR}(S_{r,n})=3\) is prior-covered and is not the originality-bearing part of this result.

Searches for the exact phrase “double Roman domination polynomial”, for complete split graphs, threshold graphs, join graphs, weight enumerators, and counts of all double Roman dominating functions did not locate an all-weight formula for \(K_ree\overline{K_n}\). Semantic comparison searches returned neighboring results on Roman, Roman \(\{2\}\), weak Roman, total Roman, and signed Roman weight enumerators on complete multipartite graphs, but none has the same invariant and object class.

## Limitations
The theorem is stated only for \(r,n\ge2\); the boundary cases with a one-vertex clique or a one-vertex independent part require separate formulas because Case 3 changes. The originality assessment cannot exclude poorly indexed or differently named equivalent literature. The computational replay covers only \(2\le r,n\le4\) and is not used as an infinite proof.

## References
1. R. A. Beeler, T. W. Haynes, S. T. Hedetniemi, “Double Roman domination,” *Discrete Applied Mathematics* 211 (2016), 23–29. DOI: 10.1016/j.dam.2016.03.017.
2. C. Padamutham, V. S. R. Palagiri, “Complexity of Roman \(\{2\}\)-domination and the double Roman domination in graphs,” *AKCE International Journal of Graphs and Combinatorics* 17 (2020), 1081–1086. DOI: 10.1016/j.akcej.2020.01.005.
3. J. B. G. Cariaga, F. P. Jamil, “On Double Roman Dominating Functions in Graphs,” *European Journal of Pure and Applied Mathematics* 16 (2023), 847–863. DOI: 10.29020/nybg.ejpam.v16i2.4653.
4. D. Rupnik Poklukar, J. Žerovnik, “Double Roman Domination: A Survey,” *Mathematics* 11 (2023), 351. DOI: 10.3390/math11020351.
