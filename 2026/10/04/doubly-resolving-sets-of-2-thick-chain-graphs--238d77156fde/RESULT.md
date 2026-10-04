# Doubly resolving sets of 2-thick chain graphs

## Finding
Let \(G\) be a finite connected chain graph with canonical nonempty open-neighborhood twin classes
\[
A_1,\ldots,A_p,B_1,\ldots,B_p,
\]
where \(p\ge2\), every vertex of \(A_i\) is adjacent to every vertex of \(B_j\) exactly when \(j\le i\), and
\[
\alpha_i=|A_i|\ge2,\qquad \beta_i=|B_i|\ge2
\]
for every \(i\). Put \(N=\sum_i(\alpha_i+\beta_i)\).

A set \(S\subseteq V(G)\) is doubly resolving if and only if all three conditions hold:

1. \(|A_i\setminus S|\le1\) and \(|B_i\setminus S|\le1\) for every \(i\).
2. If \(\beta_1=2\), then \(S\) does not omit a vertex from both \(A_1\) and \(B_1\).
3. If \(\alpha_p=2\), then \(S\) does not omit a vertex from both \(A_p\) and \(B_p\).

Thus, among 2-thick non-complete chain graphs, all failures beyond the unavoidable twin-class obstruction are confined to the two ends of the nesting order.

Define
\[
f_m(x)=x^m+m x^{m-1},\qquad e_m(x)=m x^{m-1}.
\]
The factor \(f_m(x)\) records the two allowed choices for a class of size \(m\): omit no vertex or omit exactly one; \(e_m(x)\) records the second choice only. Set
\[
F(x)=\prod_{i=1}^{p}f_{\alpha_i}(x)f_{\beta_i}(x).
\]
When \(\beta_1=2\), define
\[
L(x)=e_{\alpha_1}(x)e_{\beta_1}(x)
\prod_{i=2}^{p}f_{\alpha_i}(x)
\prod_{j=2}^{p}f_{\beta_j}(x),
\]
and otherwise put \(L(x)=0\). When \(\alpha_p=2\), define
\[
R(x)=e_{\alpha_p}(x)e_{\beta_p}(x)
\prod_{i=1}^{p-1}f_{\alpha_i}(x)
\prod_{j=1}^{p-1}f_{\beta_j}(x),
\]
and otherwise put \(R(x)=0\). If both \(\beta_1=2\) and \(\alpha_p=2\), then, because \(p\ge2\), the two boundary pairs are disjoint and their intersection polynomial is
\[
I(x)=e_{\alpha_1}(x)e_{\beta_1}(x)e_{\alpha_p}(x)e_{\beta_p}(x)
\prod_{i=2}^{p-1}f_{\alpha_i}(x)f_{\beta_i}(x);
\]
otherwise put \(I(x)=0\). Therefore the full cardinality enumerator of doubly resolving sets is
\[
D_G(x)=F(x)-L(x)-R(x)+I(x).
\]

Writing
\[
\ell=\mathbf 1_{\{\beta_1=2\}},\qquad r=\mathbf 1_{\{\alpha_p=2\}},
\]
the minimum cardinality is
\[
\psi(G)=N-2p+\ell+r.
\]
The number of minimum doubly resolving sets is obtained from \(\prod_i\alpha_i\beta_i\) by replacing \(\alpha_1\beta_1\) with \(\alpha_1+\beta_1\) when \(\ell=1\), and replacing \(\alpha_p\beta_p\) with \(\alpha_p+\beta_p\) when \(r=1\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The chain graph is written in the canonical nested form above. The theorem assumes \(p\ge2\) and every canonical twin class has at least two vertices. The excluded case \(p=1\) is a complete bipartite graph and belongs to a separately studied family. Classes of size one are also excluded: singleton classes remove the guarantee that every class still contributes a landmark after one omission and produce additional interior obstructions.

A pair of vertices \(u,v\) is doubly resolved by landmarks \(x,y\) when
\[
d(u,x)-d(v,x)\ne d(u,y)-d(v,y).
\]
A set is doubly resolving when every pair of distinct vertices is doubly resolved by two vertices of the set.

## Proof
Necessity of the twin-class condition is immediate but important. If two distinct open twins \(u,v\) in the same canonical class are both omitted from \(S\), then every landmark has equal distance to \(u\) and \(v\). Hence they are not even singly resolved, so a doubly resolving set can omit at most one vertex from each class.

For the left endpoint, assume \(\beta_1=2\) and omit \(a\in A_1\) and \(b\in B_1\). Let \(b'\) be the unique selected vertex of \(B_1\). Since \(A_1\) is adjacent only to \(B_1\), while \(B_1\) is adjacent to every \(A\)-class, one checks for every \(s\in S\) that
\[
d(a,s)-d(b',s)=1.
\]
Indeed this is clear for \(s=b'\); for any selected \(A\)-vertex the distances are \(2\) and \(1\); and for any selected vertex in \(B_j\) with \(j>1\) they are \(3\) and \(2\). Thus \(a\) and \(b'\) are not doubly resolved. This proves condition 2. The right endpoint is symmetric: if \(\alpha_p=2\) and one vertex is omitted from each of \(A_p,B_p\), let \(a'\) be the unique selected vertex of \(A_p\) and let \(b\) be the omitted vertex of \(B_p\). Then
\[
d(a',s)-d(b,s)=-1
\]
for every \(s\in S\), proving condition 3.

For sufficiency, assume conditions 1--3. Every canonical class contains a selected vertex because every class has size at least two and at most one vertex is omitted.

If \(u,v\) lie in the same canonical class, condition 1 ensures that at least one of them is selected. Using that selected endpoint as one landmark gives distance difference \(\pm2\), whereas any selected landmark outside the class has equal distances to the two open twins and gives difference \(0\). Hence the pair is doubly resolved.

Suppose \(u\in A_i\) and \(v\in A_j\) with \(i<j\). A selected vertex of \(B_{i+1}\) has distances \(3\) and \(1\) to \(u,v\), while a selected vertex of \(B_1\) has distance \(1\) to both. Thus the two distance differences are \(2\) and \(0\). The case of two vertices \(B_i,B_j\) with \(i<j\) is symmetric: a selected vertex of \(A_{j-1}\) gives distances \(1\) and \(3\), while a selected vertex of \(A_p\) is adjacent to both.

It remains to consider \(u\in A_i\) and \(v\in B_j\). If \(j>i\), then the pair is nonadjacent. A selected landmark in \(A_i\) gives a negative difference, equal to \(-3\) when the landmark is \(u\) and \(-1\) otherwise, whereas a selected landmark in \(B_j\) gives a positive difference, equal to \(3\) when the landmark is \(v\) and \(1\) otherwise. Hence the pair is doubly resolved.

Now let \(j\le i\), so \(u,v\) are adjacent. If \(u\) is omitted and \(v\) is the unique selected vertex of \(B_j\), then \(\beta_j=2\). When \(j>1\), a selected vertex of \(A_{j-1}\) gives the opposite distance difference from \(v\); when \(j=1<i\), a selected vertex of \(B_2\) does so. Therefore a failure of this type can occur only at \(i=j=1\), exactly the obstruction excluded by condition 2. Dually, if \(v\) is omitted and \(u\) is the unique selected vertex of \(A_i\), a failure can occur only at \(i=j=p\), exactly the obstruction excluded by condition 3. In all remaining adjacent cases a second selected vertex in the relevant class, or one of the preceding landmarks, supplies a different distance difference. Hence every pair is doubly resolved.

The polynomial follows by inclusion-exclusion. Condition 1 alone gives the product \(F(x)\). The forbidden left and right endpoint events contribute \(L(x)\) and \(R(x)\), and because \(p\ge2\) their class pairs are disjoint, so their simultaneous occurrence contributes \(I(x)\). This gives \(D_G(x)=F(x)-L(x)-R(x)+I(x)\).

Finally, condition 1 permits at most \(2p\) omissions. A left endpoint obstruction with \(\beta_1=2\) forces one of \(A_1,B_1\) to be fully selected; a right endpoint obstruction with \(\alpha_p=2\) independently forces one of \(A_p,B_p\) to be fully selected. The two boundary pairs are disjoint, so the maximum number of omissions is \(2p-\ell-r\), proving the formula for \(\psi(G)\). At minimum cardinality, every unconstrained class contributes the choice of its omitted vertex, while a constrained boundary pair contributes the choice of one omitted vertex from either class, yielding the stated basis count.

## Verification
The accompanying `verify.py` constructs every 2-thick canonical chain-graph profile with \(p\ge2\) and order at most \(12\). For every vertex subset it computes all-pairs distances by breadth-first search and checks the literal doubly-resolving definition against the three-condition characterization. It separately expands the claimed polynomial and compares every coefficient with the brute-force count. It also checks the formula for \(\psi(G)\) and the number of minimum sets. The replay result is reported in `VERIFICATION.md`.

The finite census checks the implementation and the case analysis through the stated cutoff; it is not used as an infinite proof. The infinite theorem is established by the distance argument above.

## Relationship to prior work
Cáceres, Hernando, Mora, Pelayo, Puertas, Seara, and Wood introduced doubly resolving sets and proved their relationship to metric dimension of Cartesian products. Their publicly available full text develops complete graphs, Hamming graphs, paths and grids, cycles, and trees; a full-text search of that paper found no occurrence of “chain” or “Ferrers.”

Bhat, Hanif, and Sudhakara study ordinary metric dimension and related threshold-dimension questions for chain graphs. Their open-access paper gives the canonical double-nested representation, proves the basic twin-class lower bound for resolving sets, and derives metric-dimension bounds. The inspected sections do not formulate doubly resolving sets or the endpoint characterization above.

Kratica, Čangalović, and Kovačević-Vujčić treat the general minimum doubly resolving set problem computationally and prove NP-hardness; their abstract does not provide a chain-graph closed form. A separate published record gives an exact classification for complete multipartite graphs, whose chain-graph intersection is the complete-bipartite case \(p=1\); the present theorem assumes \(p\ge2\), so that result does not imply the claim.

## Limitations
The theorem does not cover canonical classes of size one. In that regime, an omitted singleton class can leave no landmark in that class, and additional interior obstructions appear. It also deliberately excludes \(p=1\), the complete-bipartite case. The literature search found no chain/Ferrers doubly-resolving theorem, but weak indexing or alternate terminology can never establish nonexistence of prior work; this remains the principal originality risk.

The polynomial counts vertex subsets by cardinality only. It does not enumerate ordered landmark pairs or address fault-tolerant, edge-based, strong, or other resolving variants.

## References
1. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara, and D. R. Wood, “On the Metric Dimension of Cartesian Products of Graphs,” arXiv:math/0507527, first public version 26 July 2005; SIAM Journal on Discrete Mathematics 21 (2007), 423–441, doi:10.1137/050641867.
2. K. Arathi Bhat, S. Hanif, and G. Sudhakara, “Metric dimension and its variations of chain graphs,” Proceedings of the Jangjeon Mathematical Society 24 (2021), 309–321, doi:10.17777/pjms2021.24.3.309.
3. J. Kratica, M. Čangalović, and V. Kovačević-Vujčić, “Computing minimal doubly resolving sets of graphs,” Computers & Operations Research 36 (2009), 2149–2159, doi:10.1016/j.cor.2008.08.002.
