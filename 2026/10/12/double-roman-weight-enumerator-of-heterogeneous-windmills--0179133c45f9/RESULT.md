# Double Roman weight enumerator of heterogeneous windmills
## Finding
Let
\[
W(m_1,\ldots,m_r)=K_1\vee\bigl(K_{m_1}\cup\cdots\cup K_{m_r}\bigr),
\qquad r\ge2,\quad m_i\ge2,
\]
with center vertex \(c\) and peripheral clique blades \(B_1,\ldots,B_r\), where \(|B_i|=m_i\). A double Roman dominating function is a map \(f:V(W)\to\{0,1,2,3\}\) such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), and every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\). Its weight is \(w(f)=\sum_{v\in V(W)}f(v)\).

For every integer \(m\ge2\), put
\[
A_m(x)=(1+x+x^2+x^3)^m,
\]
\[
B_m(x)=A_m(x)-(1+x)^m+x^m,
\]
and
\[
C_m(x)=A_m(x)-(1+x)^m-mx^2\bigl((1+x)^{m-1}-x^{m-1}\bigr).
\]
Then the complete weight enumerator of double Roman dominating functions on \(W(m_1,\ldots,m_r)\) is
\[
\mathcal D_W(x)
=x^3\prod_{i=1}^r A_{m_i}(x)
+x^2\prod_{i=1}^r B_{m_i}(x)
+(1+x)\prod_{i=1}^r C_{m_i}(x).
\]

In particular, the unique minimum-weight function assigns \(3\) to the center and \(0\) to every peripheral vertex, so \(\gamma_{dR}(W)=3\). This scalar minimum is not claimed as new: it follows from previously published scalar theory because \(W\) has a universal vertex. The new statement is the all-weight structural factorization above. Evaluating at \(x=1\) gives the exact total number of double Roman dominating functions,
\[
\prod_{i=1}^r4^{m_i}
+\prod_{i=1}^r\bigl(4^{m_i}-2^{m_i}+1\bigr)
+2\prod_{i=1}^r\bigl(4^{m_i}-2^{m_i}-m_i(2^{m_i-1}-1)\bigr).
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem concerns heterogeneous windmills formed by joining one center to at least two pairwise anticomplete peripheral cliques, each of order at least two. Labels \(0,1,2,3\), the defense requirements, and the weight convention are exactly those of double Roman domination. The result counts all feasible functions at every weight; it does not concern signed, independent, total, perfect, or Italian variants.

## Proof
Partition all labelings by the label \(s=f(c)\) of the center.

If \(s=3\), the center itself defends every peripheral vertex labeled \(0\) or \(1\). Hence every assignment on every blade is legal, and a blade of order \(m\) contributes \(A_m(x)\). This gives
\[
x^3\prod_i A_{m_i}(x).
\]

If \(s=2\), every peripheral vertex labeled \(1\) is already defended by the center. A peripheral vertex labeled \(0\) has one neighboring \(2\), namely the center, and therefore needs either a blade neighbor labeled \(2\) or a blade neighbor labeled \(3\). Thus a blade assignment is illegal exactly when it uses only labels \(0,1\) and contains at least one \(0\). The weight enumerator of these illegal assignments is
\[
(1+x)^m-x^m.
\]
Subtracting them from all assignments yields \(B_m(x)\), and the contribution for \(s=2\) is
\[
x^2\prod_i B_{m_i}(x).
\]

Now suppose \(s\in\{0,1\}\). The center no longer supplies a label at least \(2\) to a blade. If a blade contains a label \(3\), all its vertices labeled \(0\) or \(1\) are defended. If it has no label \(3\), then a blade with no label \(2\) is illegal, contributing \((1+x)^m\). A blade with exactly one label \(2\) is illegal precisely when at least one of its remaining vertices is labeled \(0\); these assignments contribute
\[
mx^2\bigl((1+x)^{m-1}-x^{m-1}\bigr).
\]
With at least two labels \(2\), every zero has two such neighbors and every one has at least one. Hence the legal blade enumerator is exactly \(C_m(x)\).

Every assignment counted by \(C_m(x)\) contains at least one blade vertex labeled \(2\) or \(3\). Therefore, when \(s=1\), the center automatically has a neighbor labeled at least \(2\). When \(s=0\), either some blade contains a \(3\), or else each of the \(r\ge2\) blades contains at least one \(2\); in the latter case the center has at least two neighbors labeled \(2\). Thus there is no additional global restriction. The cases \(s=0\) and \(s=1\) together contribute
\[
(1+x)\prod_i C_{m_i}(x).
\]
Adding the three disjoint center-label regimes proves the formula.

For the minimum, the center-label-3 regime contains the function with center label \(3\) and all peripheral labels \(0\), of weight \(3\). In the center-label-2 regime each blade must have weight at least \(2\), and in the center-label-0 or center-label-1 regimes each blade must have weight at least \(3\). Since \(r\ge2\), no other function has weight \(3\), proving uniqueness. Substituting \(x=1\) into the three blade factors gives the displayed total count.

## Verification
The accompanying program `artifacts/verify.py` independently constructs the graph and tests the double Roman definition directly, without using the structural criterion from the proof. It exhaustively enumerates all \(4^{|V|}\) labelings for six heterogeneous blade profiles through order \(9\), compares every weight coefficient with the closed product formula, and checks that the unique minimum function has weight \(3\). The finite replay is corroborative only; the universal theorem rests on the symbolic case analysis above.

## Relationship to prior work
Beeler, Haynes, and Hedetniemi introduced double Roman domination and its minimum-weight invariant. Their foundational public record gives the standard definition used here. Later work by Cariaga and Jamil studies the minimum double Roman domination number under graph operations including joins. In particular, their scalar theory implies \(\gamma_{dR}(W)=3\) because a heterogeneous windmill has domination number \(1\); that scalar equality is therefore treated as prior work.

The closest inspected join theorem concerns only the minimum weight. Its full text contains no occurrence of “windmill,” “friendship,” “polynomial,” or “enumerat,” and it does not classify all double Roman functions or give their weight distribution. Searches under generalized-windmill, friendship-graph, join-of-cliques, polynomial, and enumerator terminology likewise found no statement implying the factorization above. This comparison supports originality but is not a logical proof that no differently indexed source exists.

## Limitations
The factorization requires the stated heterogeneous-windmill structure and \(r\ge2\); it does not claim an analogous product for arbitrary block graphs or arbitrary joins. The finite checker only reaches order \(9\) and is not used to justify the infinite quantifiers. Bibliographic indexing is incomplete, so an unindexed or differently named all-function enumeration remains a residual originality risk.

## References
R. A. Beeler, T. W. Haynes, and S. T. Hedetniemi, “Double Roman Domination,” Discrete Applied Mathematics 211 (2016), 23–29, DOI: 10.1016/j.dam.2016.03.017.

J. Cariaga and M. Jamil, “Double Roman domination number of the join, corona, complementary prism and graph compositions,” European Journal of Pure and Applied Mathematics 16(2) (2023), DOI: 10.29020/nybg.ejpam.v16i2.4653.
