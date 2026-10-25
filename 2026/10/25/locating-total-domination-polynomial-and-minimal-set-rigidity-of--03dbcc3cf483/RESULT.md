# Locating-total domination polynomial and minimal-set rigidity of crown graphs

## Finding

For every integer \(n\ge3\), let \(G_n=K_{n,n}-M_n\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\) and edges \(a_i b_j\) exactly when \(i\ne j\). A set \(S\subseteq V(G_n)\) is *locating-total dominating* if every vertex has a neighbor in \(S\), and distinct vertices outside \(S\) have different open-neighborhood intersections with \(S\).

Write \(a=|S\cap A|\), \(b=|S\cap B|\), and let \(t\) be the number of indices \(i\) for which neither \(a_i\) nor \(b_i\) belongs to \(S\). The complete characterization is
\[
S\text{ is locating-total dominating}\quad\Longleftrightarrow\quad a\ge2,\quad b\ge2,\quad t\le1.
\]

Let \(\mathcal L_n(x,y)\) count all such sets, with \(x\) marking vertices selected in \(A\) and \(y\) marking vertices selected in \(B\). If \(\Pi_{\ge2,\ge2}\) deletes every monomial whose \(x\)-degree or \(y\)-degree is below two, then
\[
\boxed{\mathcal L_n(x,y)=\Pi_{\ge2,\ge2}\bigl[(x+y+xy)^n+n(x+y+xy)^{n-1}\bigr].}
\]
Equivalently, for integers \(0\le a,b\le n\), the coefficient is zero if \(a<2\) or \(b<2\), and otherwise it is
\[
\boxed{[x^a y^b]\mathcal L_n(x,y)=
\sum_{t=0}^{1}\frac{n!}{t!\,(n-a-t)!\,(n-b-t)!\,(a+b-n+t)!},}
\]
where a summand with a negative factorial argument is understood to be zero. The ordinary cardinality polynomial \(L_n(z)=\mathcal L_n(z,z)\) therefore satisfies
\[
\boxed{\begin{aligned}
L_n(z)={}&(2z+z^2)^n+n(2z+z^2)^{n-1}\\
&-2n^2z^{n-1}-2(n^2+1)z^n-2nz^{n+1}
+6\mathbf 1_{\{n=3\}}z^2.
\end{aligned}}
\]

**Every inclusion-minimal locating-total dominating set has minimum cardinality.** These sets and their exact counts are:

* For \(n=3\), precisely the sets with \(a=b=2\): there are \(9\), each of size \(4\).
* For \(n=4\), precisely the sets with \(a=b=2\) and \(t\le1\): there are \(30\), each of size \(4\).
* For \(n\ge5\), precisely the sets omitting both endpoints of one matching index and selecting exactly one endpoint at every other index, with at least two selections from each side. They number \(n(2^{n-1}-2n)\) and each has size \(n-1\).

In particular,
\[
\boxed{\gamma_t^L(G_n)=\max\{4,n-1\},\qquad
N_{\min}(G_n)=\begin{cases}9,&n=3,\\30,&n=4,\\n(2^{n-1}-2n),&n\ge5.\end{cases}}
\]

## Assumptions and scope

All graphs are finite, simple and undirected. The two sides and missing matching are labeled. The locating condition compares only *unselected* vertices, unlike identifying codes that compare all vertices. Open neighborhoods are used, and total domination applies also to selected vertices. Every assertion holds for all integers \(n\ge3\). The special values \(n=3\) and \(n=4\) are the cycle \(C_6\) and the three-dimensional cube, respectively. Graphs with \(n\le2\) are outside the theorem.

## Proof

**1. Exact feasibility criterion.** Let \(A_S=S\cap A\) and \(B_S=S\cap B\). Every vertex \(a_i\) sees exactly \(B_S\setminus\{b_i\}\), and every \(b_i\) sees exactly \(A_S\setminus\{a_i\}\). If \(|B_S|=0\), nothing in \(A\) is totally dominated. If \(|B_S|=1\), the vertex matched to that sole selected neighbor has none. Conversely, \(|B_S|\ge2\) totally dominates all of \(A\). Symmetrically, total domination is equivalent to \(a,b\ge2\).

For distinct unselected \(a_i,a_j\), the two selected-neighborhood signatures coincide if and only if neither \(b_i\) nor \(b_j\) was selected. Since both \(a_i,a_j\) are unselected, this occurs precisely when indices \(i,j\) are both completely unrepresented. The same argument applies to distinct unselected vertices in \(B\). Across the bipartition the two signatures, when nonempty, lie in disjoint sides of \(S\), so cannot coincide. Consequently the locating condition under total domination is exactly \(t\le1\).

**2. Bivariate enumeration.** For a matched index there are four disjoint states, with weights \(1,x,y,xy\): neither endpoint selected, only \(a_i\), only \(b_i\), or both. The condition \(t\le1\) permits either zero empty indices, of total weight \((x+y+xy)^n\), or exactly one, of weight \(n(x+y+xy)^{n-1}\). Deleting monomials of \(x\)- or \(y\)-degree less than two imposes total domination and gives the stated bivariate polynomial. For selected side sizes \(a,b\) and empty-index count \(t\), the numbers of the other three index states are respectively \(n-b-t\), \(n-a-t\), and \(a+b-n+t\). Their multinomial coefficient yields the coefficient formula with the displayed nonnegativity convention.

**3. Univariate formula.** Before enforcing \(a,b\ge2\), the cardinality polynomial is \((2z+z^2)^n+n(2z+z^2)^{n-1}\). The polynomial of configurations with \(a\le1\) is exactly
\[
n^2z^{n-1}+(n^2+1)z^n+nz^{n+1}.
\]
Indeed, \(a=0\) contributes \(z^n+nz^{n-1}\); choosing the one selected \(A\)-vertex and distinguishing whether its matching \(B\)-vertex is selected and whether there is one empty index gives the remaining terms. By symmetry the same expression must be subtracted for \(b\le1\). Their intersection is empty for \(n\ge4\), because the condition \(t\le1\) requires at least \(n-1\ge3\) selections. For \(n=3\) the intersection consists of six configurations with one \(A\)-only index, one \(B\)-only index, and one empty index; restore \(6z^2\). This proves the formula for \(L_n(z)\).

**4. Minimum and complete minimal-set classification.** The inequalities \(a,b\ge2\) and \(t\le1\) require \(|S|\ge\max\{4,n-1\}\). This is attained for \(n=3,4\) by choosing two endpoints from each side with at most one completely omitted index. For \(n\ge5\), omit one matched pair and choose one endpoint in each other pair, assigning at least two of the selections to each side. This attains \(n-1\).

To show no larger locating-total dominating set is inclusion-minimal, take a feasible \(S\). When \(n\ge5\) and \(t=1\), any set larger than \(n-1\) has a doubly selected index; since \(|S|\ge n\ge5\), one side contains at least three selected vertices, and removing that side's endpoint from a doubly selected index preserves all three feasibility inequalities. If \(t=0\) and there is a doubly selected index, again one side has at least three selected vertices, and removing its endpoint at that doubly selected index preserves feasibility. If \(t=0\) and no index is doubled, then \(|S|=n\ge5\), one side has at least three selections, and deleting one such singleton selection creates exactly one empty index while retaining at least two selections on each side.

For \(n=3,4\), any feasible set of size greater than four has a side with at least three selected vertices. If \(t=0\), it also has a doubly selected index, and removing its endpoint from a side with at least three selections preserves feasibility. If \(t=1\), then the case \(n=3\) cannot have size greater than four, while for \(n=4\) size greater than four implies at least two doubled indices, so the same deletion is possible. Therefore every inclusion-minimal set has the stated minimum size, and every minimum set is trivially inclusion-minimal.

For \(n=3\) there are \(\binom32^2=9\) minimum sets. For \(n=4\) there are \(\binom42^2-\binom42=30\), since the excluded choices select the same two index pairs in both sides. For \(n\ge5\), choose the unique omitted index in \(n\) ways and assign the \(n-1\) remaining single selected endpoints to sides in \(2^{n-1}\) ways. Excluding assignments with zero or one selected endpoint on either side removes \(2[1+(n-1)]=2n\) assignments. This gives \(n(2^{n-1}-2n)\).

## Verification

The accompanying dependency-free program `check_crown_ltd.py` constructs the adjacency relation directly, tests nonempty open-neighborhood signatures for all vertices and distinct signatures for unselected vertices, tests every subset for \(3\le n\le9\), and independently checks the proposed structural criterion, complete bivariate and univariate coefficients, and the identity of the inclusion-minimal families. It examined \(349504\) vertex subsets. Its complete output is preserved in `verification_output.txt`; all tests passed. The program is finite corroboration only; the proof above establishes all integers \(n\ge3\).

## Relationship to prior work

Locating-total domination was studied by Henning and Jafari Rad (2012); Omamalin, Canoy and Rara (2014) determined the parameter for joins, coronas and compositions, and Foucaud and Henning (2016) established general bounds for twin-free graphs. Raza, Iqbal, Khan and Botmart (2021) examined cyclic and rotationally symmetric graph families. These sources motivate exact placement enumeration but the inspected material does not provide this crown-graph all-set polynomial or minimal-family classification. The crown graph also has the equivalent representation \(G_n\cong K_n\times K_2\), where \(\times\) denotes the direct (tensor) graph product. Iswadi's 2011 work on such products concerns *metric*-locating-total domination, a distinct requirement comparing graph distances for all vertex pairs; its abstract does not imply the present all-set formula. General numerical bounds alone also do not imply optimizer multiplicities or cardinality polynomials. Bibliographic priority remains subject to unindexed equivalent results.

## Limitations

The graph family has exactly two equal sides and exactly one deleted perfect matching. No claim is made for general partial-matching deletions, arbitrary direct products, or identifying codes that distinguish selected vertices too. Exhaustive computation covers only \(n\le9\). The proof is not independently audited, and a relevant older metric-locating-total source was available only through its abstract.

## References

1. H. Raza, N. Iqbal, H. Khan and T. Botmart, *Computing locating-total domination number in some rotationally symmetric graphs*, Science Progress 104 (2021), DOI: 10.1177/00368504211053417. First publicly available online 17 November 2021.
2. M. A. Henning and N. Jafari Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics 160 (2012), 1986–1993, DOI: 10.1016/j.dam.2012.04.004.
3. B. N. Omamalin, S. R. Canoy Jr. and H. M. Rara, *Locating Total Dominating Sets in the Join, Corona and Composition of Graphs*, Applied Mathematical Sciences 8 (2014), 2363–2374, DOI: 10.12988/ams.2014.43205.
4. F. Foucaud and M. A. Henning, *Locating-Total Dominating Sets in Twin-Free Graphs: a Conjecture*, Electronic Journal of Combinatorics 23 (2016), P3.9, DOI: 10.37236/5147.
5. H. Iswadi, *Locating and Total Dominating Sets of Direct Products of Complete Graphs*, ICOWOBAS 2011, pp. 585–589, institutional repository record `repository.ubaya.ac.id/274/` (abstract inspected; this work uses a different metric-locating definition).
