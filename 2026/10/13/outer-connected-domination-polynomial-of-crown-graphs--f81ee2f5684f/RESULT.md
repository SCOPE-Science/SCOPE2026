# Outer-connected domination polynomial of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) have bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with deleted matching \(a_i b_i\). Define
\[
F_n(x)=(1+x)^n-1-nx.
\]
Using the standard convention that \(V(G)\) is itself outer-connected dominating, the complete outer-connected domination polynomial is
\[
D_{\mathrm{oc}}(\operatorname{Cr}_n;x)=F_n(x)^2+2n x^2(1+x)^{n-1}-n x^2+2x^n
-2x^n\big((1+x)^n-nx^{n-1}-x^n\big)
-2n x^{n-1}\big((1+x)^{n-1}-1\big)
+n x^{2n-2}-\binom{n}{2}x^{2n-4}.
\]
Hence
\[
D_{\mathrm{oc}}(\operatorname{Cr}_n;1)
=(2^n-n-1)^2-2^{n+1}+4n+4-\binom{n}{2}.
\]
There is a sharp small-order transition:
\[
\gamma_{\mathrm{oc}}(\operatorname{Cr}_3)=4,
\]
with exactly six minimum sets, whereas for every \(n\ge4\),
\[
\gamma_{\mathrm{oc}}(\operatorname{Cr}_n)=2,
\]
and the minimum sets are exactly the \(n\) deleted-matching pairs \(\{a_i,b_i\}\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The crown graph \(\operatorname{Cr}_n\) is connected for \(n\ge3\). A set \(S\subseteq V(G)\) is outer-connected dominating when it is dominating and either \(S=V(G)\) or \(G[V(G)\setminus S]\) is connected. The claim is restricted to \(n\ge3\); the disconnected graph \(\operatorname{Cr}_2\) is outside scope.

## Proof
Write \(I=\{i:a_i\in S\}\), \(J=\{i:b_i\in S\}\), and put \(a=|I|\), \(b=|J|\). First classify domination. If \(a,b\ge2\), every vertex outside \(S\) has a selected neighbor on the opposite side. If \(a=1\), say \(I=\{i\}\), then the only possible undominated vertex on the \(B\)-side is \(b_i\), so domination holds exactly when \(i\in J\); the symmetric statement holds when \(b=1\). Finally, a set contained in one bipartition side dominates exactly when it is that entire side. Thus the domination polynomial is
\[
F_n(x)^2+2n x^2(1+x)^{n-1}-n x^2+2x^n.
\]
The subtraction \(-n x^2\) corrects the double count of the \(n\) matched two-vertex sets.

Now put \(X=A\setminus S\), \(Y=B\setminus S\), with \(p=|X|\), \(q=|Y|\), and \(c=|\{i:a_i\in X,\ b_i\in Y\}|\). When \(p,q>0\), the complement induced by \(X\cup Y\) is \(K_{p,q}\) with a matching of size \(c\) deleted. It is disconnected exactly in either of the following mixed cases: one side is a singleton and its deleted mate lies on the other side, or \(p=q=c=2\). If one of \(p,q\) is zero, the complement is connected exactly when the other equals one.

Intersect these connectivity obstructions with the domination classification. Dominating sets with complement contained in one side and of size at least two contribute
\[
2x^n\big((1+x)^n-nx^{n-1}-x^n\big).
\]
Mixed complements with a singleton side and its mate omitted contribute, with orientation counted twice,
\[
2n x^{n-1}\big((1+x)^{n-1}-1\big),
\]
and the \(n\) complements consisting of one matched pair were subtracted twice, so \(n x^{2n-2}\) is restored. Finally, complements formed by two deleted-matching pairs contribute \(\binom{n}{2}x^{2n-4}\). Subtracting exactly these disjointness-corrected classes from the domination polynomial proves the displayed formula.

For a two-vertex dominating set, the domination classification forces a deleted-matching pair. Its complement is \(\operatorname{Cr}_{n-1}\), connected exactly when \(n-1\ge3\). This gives the minimum transition at \(n=3\). When \(n=3\), a four-vertex set is minimum precisely when its two-vertex complement is an edge; \(\operatorname{Cr}_3\) has six edges.

## Verification
The standalone checker `verify.py` independently enumerates every subset of \(\operatorname{Cr}_n\) for \(3\le n\le8\). It separately checks the domination classification, the complement-connectivity classification, every polynomial coefficient, the minimum cases, and the closed total-count formula. Its successful output is:

`VERIFY_OK n_range=3..8 subset_checks=87360 structural_checks=174714 coefficient_checks=72 minimum_checks=6 max_order=16`

This finite enumeration checks the formulas on small orders; it is not used as the proof for arbitrary \(n\).

## Relationship to prior work
Outer-connected domination was studied before the polynomial was introduced. The 2010 Utilitas Mathematica article *Outer-connected domination in graphs* supplies an exact day-level archival source for the parameter. The later paper *On the number of outer connected dominating sets of graphs* introduces the outer-connected domination polynomial and gives formulas for paths, cycles, stars, joins, and wheels; it also recalls the minimum outer-connected domination number for complete multipartite graphs. Full-text inspection of arXiv:1112.0846 found no occurrence of `crown` or `matching`, and no coefficient formula for a complete bipartite graph with a perfect matching deleted.

The complete-multipartite result does not imply the present claim: \(\operatorname{Cr}_n\) is not complete multipartite for \(n\ge3\), and deleting a perfect matching can change the outer-connectivity requirement. In fact \(K_{3,3}\) has outer-connected domination number \(2\), while the theorem above gives \(\gamma_{\mathrm{oc}}(\operatorname{Cr}_3)=4\).

## Limitations
The theorem treats only the standard crown family and the standard convention that the full vertex set is admissible. It does not address arbitrary matching deletions from \(K_{m,n}\), weighted variants, or roots/unimodality of the polynomial. An earlier 2007 paper introduced the parameter, but only year-level public date evidence was verified for that item in this review; the stored first-public date therefore uses the earliest inspected source with an exact day-level public date. The finite checker covers only \(3\le n\le8\), while the symbolic proof is the justification for all \(n\ge3\).

## References
1. J. Cyman, *The outer-connected domination number of a graph*, Australasian Journal of Combinatorics 38 (2007), 35–46.
2. H. Jiang and E. Shan, *Outer-connected domination in graphs*, Utilitas Mathematica 81 (2010), 265–274. Publisher record reports publication on 2010-05-09.
3. S. Alikhani, M. H. Akhbari, C. Eslahchi, and R. Hasni, *On the number of outer connected dominating sets of graphs*, arXiv:1112.0846; the inspected full text defines the polynomial and treats paths, cycles, stars, joins, and wheels.
4. B. Panda and A. Pandey, *Algorithm and Hardness Results for Outer-connected Dominating Set in Graphs*, Journal of Graph Algorithms and Applications 18 (2014), 473–500, DOI:10.7155/jgaa.00334.
