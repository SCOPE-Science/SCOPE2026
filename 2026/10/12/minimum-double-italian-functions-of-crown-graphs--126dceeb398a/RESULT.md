# Minimum double Italian functions of crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph for \(n\ge4\), with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted perfect matching \(M=\{a_i b_i:1\le i\le n\}\). Then
\[
\gamma_{dI}(\operatorname{Cr}_n)=6.
\]
Every minimum double Italian dominating function is obtained from a vector \(x=(x_1,\ldots,x_n)\in\{0,1,2,3\}^n\) satisfying \(\sum_i x_i=3\), by setting \(f(a_i)=f(b_i)=x_i\). Hence the exact number of minima is
\[
\binom{n+2}{3}.
\]
## Assumptions and scope
A double Italian dominating function is a map \(f:V(G)\to\{0,1,2,3\}\) such that a vertex labeled \(0\) has neighbor-label sum at least \(3\), while a vertex labeled \(1\) has neighbor-label sum at least \(2\). Equivalently, \(f(N[v])\ge3\) whenever \(f(v)\le1\). The theorem is stated for \(n\ge4\); the two smaller crowns have extra weight-six minima.
## Proof
Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), \(X=\sum_i x_i\), and \(Y=\sum_i y_i\). Since \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), feasibility is exactly
\[
x_i+Y-y_i\ge3
\]
whenever \(x_i\le1\), and symmetrically
\[
y_i+X-x_i\ge3
\]
whenever \(y_i\le1\).

Suppose \(X+Y\le5\). One side has weight at most \(2\); assume \(X\le2\). Since \(n\ge4\), some \(x_i=0\). If \(Y\le3\), the first inequality forces \(Y=3\) and \(y_i=0\), while the second then forces \(X\ge3\), contradiction. Hence \(Y\ge4\), so \(X\le1\). If \(X=0\), every \(y_i\ge2\), giving \(Y\ge8\). If \(X=1\), at least three zero entries of \(x\) each force the corresponding \(y_i\ge2\), giving \(Y\ge6\). Thus weight below \(6\) is impossible.

Conversely, take any \(x_i\in\{0,1,2,3\}\) with total \(3\), and put \(y_i=x_i\). Then \(X=Y=3\), and every required inequality holds with equality, so the weight is \(6\).

Now let a minimum function have weight \(6\). If \(X\le1\), the preceding argument contradicts \(Y=6-X\). If \(X=2\) and the side labels are two \(1\)'s, every zero coordinate forces \(y_i\ge1\) and each \(1\)-coordinate forces \(y_i\ge2\), so \(Y\ge n+2>4\). If instead the side labels are one \(2\) and zeros, each zero coordinate must have \(y_i=1\). For \(n\ge6\) this already exceeds \(Y=4\); for \(n=4,5\), the remaining coordinate has \(y_i\le1\), contradicting the second inequality at the coordinate carrying \(x_i=2\). Thus \(X\ge3\); by symmetry \(Y\ge3\), and hence \(X=Y=3\).

With these side totals, whenever one of \(x_i,y_i\) is at most \(1\), the two inequalities force \(x_i=y_i\). If both are at least \(2\), every other coordinate has side weight at most \(1\) and is already equal, so equality of the side totals forces equality there too. Thus \(x_i=y_i\) for every \(i\). The common vector is a weak composition of \(3\) into \(n\) parts, counted by \(\binom{n+2}{3}\).
## Verification
The included checker exhausts all quaternary labelings for \(2\le n\le5\), directly tests the defining inequalities, and for \(n=4,5\) compares the entire minimum-function set with the copied-composition family.
## Relationship to prior work
Roman \(\{3\}\)-domination, also called double Italian domination, was introduced in 2020. The introducing primary paper establishes the definition, MSC ownership, general relations with other Roman variants, bipartite complexity, and exact values for complete multipartite graphs. A contemporary survey also records complete \(r\)-partite graphs among the solved families.

A crown graph is obtained from a balanced complete bipartite graph by deleting a perfect matching, so the complete-multipartite theorem no longer applies. The result here shows a rigid synchronization law across each deleted matched pair: every optimum has side weights \(3\) and \(3\) and copies the same composition on both sides. Later general lower and probabilistic upper bounds do not determine this equality structure or count all minima.
## Limitations
The theorem treats balanced crowns for \(n\ge4\). The smaller crowns have extra weight-six minima. The finite checker through \(n=5\) is corroborative; the all-orders result is analytic. A differently phrased or non-indexed crown result may exist.
## References
1. D. A. Mojdeh, L. Volkmann, “Roman \(\{3\}\)-domination (double Italian domination),” Discrete Applied Mathematics 283 (2020), 555–564, DOI 10.1016/j.dam.2020.02.001.
2. Z. Shao, D. A. Mojdeh, L. Volkmann, “Total Roman \(\{3\}\)-domination in Graphs,” Symmetry 12 (2020), 268, DOI 10.3390/sym12020268; published 9 February 2020.
3. F. Azvin, N. Jafari Rad, “Bounds on the double Italian domination number of a graph,” Discussiones Mathematicae Graph Theory 42 (2022), 1129–1137, DOI 10.7151/DMGT.2330.
4. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, L. Volkmann, “Varieties of Roman domination II,” AKCE International Journal of Graphs and Combinatorics 17 (2020), 966–984, DOI 10.1016/j.akcej.2019.12.001.
