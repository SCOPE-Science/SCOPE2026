# Exact width-depth coincidence for finite triangular graphs

## Finding
Let \(T_n=L(K_n)\) be the simple triangular graph with vertices the two-element subsets of an \(n\)-element set, where distinct vertices are adjacent exactly when they intersect. Take \(n\ge3\), and use only equality and undirected adjacency. For all integers \(p\ge2\) and \(m,n\ge3\),
\[
T_m\equiv_{\mathrm{FO}^{p}}T_n
\quad\Longleftrightarrow\quad
T_m\equiv_{\mathrm{FO},\,\operatorname{qr}\le p}T_n
\quad\Longleftrightarrow\quad
\min\{m,2p\}=\min\{n,2p\}.
\]
In the first equivalence, the unrestricted quantifier depth of an ordinary first-order sentence is allowed, but only \(p\) reusable variable symbols may occur. In the second, any number of variable symbols is allowed, but the quantifier rank is at most \(p\). Neither logic has counting quantifiers.

Thus the family has exactly \(2p-2\) theories for each resource restriction: each \(T_3,T_4,\ldots,T_{2p-1}\) stands alone, and the entire tail \(T_{2p},T_{2p+1},\ldots\) is one theory. The least representative in that tail has \(\binom{2p}{2}=p(2p-1)\) vertices, giving the sharp uniform minimum-representative bound. For \(3\le m<n\), the minimum distinguishing number of variables, and independently the minimum distinguishing quantifier rank, are both
\[
\left\lfloor\frac m2\right\rfloor+1.
\]
At resource level \(p=1\), all members of this family are equivalent for both restrictions.

## Assumptions and scope
The root graph is the complete simple graph \(K_n\); vertices of \(T_n\) are its unordered edges, with no named root vertices, no labels, and no additional relations. Equality of graph vertices means equality of unordered endpoint pairs. A pair of distinct graph vertices is adjacent if its underlying edges have a common endpoint. The classification compares only members of this family, not arbitrary finite graphs.

## Proof
**Unrestricted-depth upper bound with \(p\) variables.** Suppose \(m,n\ge2p\). In the usual \(p\)-pebble game, Duplicator maintains a bijection between the unions of the underlying root vertices appearing in currently pebbled edges. The bijection maps every currently pebbled edge onto its counterpart. Initially both unions are empty. When Spoiler moves a pebble, remove that edge from the list and restrict the bijection to the union belonging to the at most \(p-1\) remaining pebbles. At most \(2(p-1)\) root vertices remain used. The newly chosen edge in Spoiler's graph uses zero, one, or two previously unused root vertices. Duplicator carries the old endpoints through the current bijection and chooses the necessary zero, one, or two fresh root vertices in the other graph. At least \(2p-2(p-1)=2\) are available. Extend the bijection accordingly. This also handles repeated pebbles: two pebbles on the same graph vertex remain matched to the same edge. At every position, equality and adjacency among pebbled graph vertices are preserved, since both depend only on equality and incidence of their endpoint pairs. Duplicator can maintain the invariant indefinitely. Hence \(T_m\equiv_{\mathrm{FO}^{p}}T_n\).

**Quantifier-rank upper bound.** In the ordinary \(p\)-round Ehrenfeucht–Fraïssé game the same endpoint-union bijection is maintained without any need to recycle variables. After \(j<p\) moves, the union has at most \(2j\) root vertices, leaving at least two fresh points for the next move when both root sizes are at least \(2p\). Thus the same structures agree on all sentences of quantifier rank at most \(p\).

**Path-forest witnesses for every smaller cutoff.** Fix \(p\ge2\) and an integer \(s\) with \(4\le s\le2p\). Put
\[
r=\min\{p,s-1\},\qquad c=s-r.
\]
Then \(1\le c\le r\). Let \(F\) be a disjoint union of \(c\) nonempty paths consisting of one path with \(r-c+1\) edges and \(c-1\) paths with one edge each. It has exactly \(r\) edges and exactly \(s=r+c\) vertices. Label its edges \(e_1,\ldots,e_r\). The finite existential adjacency-diagram sentence
\[
\Phi_F:=\exists z_1\cdots\exists z_r\,\left(
\bigwedge_{1\le i<j\le r}z_i\ne z_j\;\land\;
\bigwedge_{\{i,j\}\in E(L(F))}E(z_i,z_j)\;\land\;
\bigwedge_{\substack{1\le i<j\le r\\\{i,j\}\notin E(L(F))}}\neg E(z_i,z_j)
\right)
\]
uses \(r\le p\) variables and has quantifier rank \(r\le p\).

We prove \(T_n\models\Phi_F\) exactly when \(n\ge s\). If \(n\ge s\), embed the forest \(F\) on \(s\) of the root vertices and select its \(r\) edges. Conversely, suppose \(r\) distinct edges of a simple root graph have intersection graph \(L(F)\). Each connected path component of \(L(F)\) on \(a\) selected edges forces these root edges themselves to form a path using exactly \(a+1\) root vertices. For \(a=1\) and \(a=2\) this is immediate. For \(a\ge3\), successive edges must meet, but any pair whose indices differ by two or more must be disjoint. Starting with two incident edges, the third must extend from the endpoint of the second not on the first, and inductively every later edge must extend from the latest unused endpoint to one new endpoint. Thus each component needs \(a+1\) vertices. Different components have no incident edge pairs, so their root vertex sets are disjoint. The whole selected system requires \(r+c=s\) root vertices. Therefore no \(T_n\) with \(n<s\) satisfies \(\Phi_F\).

**Completion.** Given \(3\le m<n\), if \(m<2p\), choose \(s=m+1\). The sentence \(\Phi_F\) exists within both resource bounds, holds in \(T_n\), and fails in \(T_m\). If both root sizes are at least \(2p\), the two upper-bound arguments apply. This proves both equivalences, all sharp cutoffs, and the formula for the least distinguishing rank or width. Every \(T_n\) is nonempty and loop-free, so the one-variable and one-round observations give the stated \(p=1\) case.

## Verification
Two standard-library-only Python programs accompany this statement. Run \(\texttt{python3 verify\_orbits.py}\) and \(\texttt{python3 verify\_forest.py}\) from their directory. The first constructs the orbit-compressed, count-free logical-type refinement for all triangular graphs on root orders \(3\) through \(7\), \(9\), and \(10\) as appropriate to widths \(2\), \(3\), and \(4\). It computes full stabilization of logical types with recycled variables and reproduces respectively the predicted cutoffs \(4\), \(6\), and \(8\). The second independently constructs path-forest witnesses and exhaustively checks their exact least root sizes for widths \(2\) through \(5\) (\(32\) finite truth checks). Results are recorded in \(\texttt{orbit\_results.txt}\) and \(\texttt{forest\_results.txt}\). The symbolic proof, not those finite experiments, establishes the theorem for all resource levels.

## Relationship to prior work
Pikhurko and Verbitsky's survey (arXiv:1003.4865, first posted 2010-03-25) develops logical depth, logical width, Ehrenfeucht–Fraïssé games and count-free type refinement, but its inspected account does not state this exact classification for \(L(K_n)\). Grohe and Otto (arXiv:1204.1990, first posted 2012-04-09; CSL 2012) treat general counting and count-free pebble equivalence, rather than the complete triangular-graph spectrum. Harvey and Wood (arXiv:1210.8205, first posted 2012-10-31) investigate the treewidth and pathwidth of these same line graphs; those invariants do not determine their bounded-variable theories.

The finite-support argument for rank-bounded formulas on fixed-size-subset intersection graphs supplies *eventual equivalence* once the root set is sufficiently large. The present claim is not just that upper bound: it specifies every exceptional class below the cutoff, proves equivalence at unrestricted depth with fixed variable width, and establishes exact equality of the width and rank distinguishability thresholds. No claim of historical priority beyond the inspected material is made.

## Limitations
There are no counting quantifiers, root-vertex constants, root labels or higher-order relations. Larger variable width can distinguish the formerly stable tail, and unrestricted first-order logic distinguishes any two nonisomorphic finite members. The classification does not automatically apply to line graphs of arbitrary root graphs or to other Johnson-scheme layers. The available literature search cannot rule out an implicit equivalent general theorem under different terminology. Independent mathematical validation has not been performed.

## References
- O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: A survey*, arXiv:1003.4865, first posted 2010-03-25, especially Sections 1, 3, and 4.
- M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first posted 2012-04-09; *Computer Science Logic* (2012), DOI 10.4230/LIPIcs.CSL.2012.289.
- D. J. Harvey and D. R. Wood, *Treewidth of the Line Graph of Complete and Complete Multipartite Graphs*, arXiv:1210.8205, first posted 2012-10-31, especially the introduction and Theorem 1.
