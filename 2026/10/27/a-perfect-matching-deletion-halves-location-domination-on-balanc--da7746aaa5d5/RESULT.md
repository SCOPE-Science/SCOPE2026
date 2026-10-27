# A perfect-matching deletion halves location-domination on balanced bicliques

## Finding
For every integer \(n\ge3\), let \(G_n=K_{n,n}-M\), the *crown graph* obtained from the labeled complete balanced bipartite graph by deleting the matching \(M=\{a_i b_i:1\le i\le n\}\). Let \(L_n(x,y)\) count locating-dominating vertex sets with \(i\) selected vertices on the \(a\)-side and \(j\) on the \(b\)-side, weighted by \(x^i y^j\). Then
\[
\begin{aligned}
L_n(x,y)={}&(x+y+xy)^n+n(x+y+xy)^{n-1}\\
&-n(x^{n-1}+y^{n-1})\\
&-n(x^{n-1}y+xy^{n-1})\\
&-n(n-1)(x^{n-2}y+xy^{n-2})\\
&+6\,\mathbf1_{n=3}xy.
\end{aligned}
\]
In particular, the ordinary location-domination polynomial is
\[
\boxed{L_n(z,z)=z^{n-1}(z+2)^{n-1}\bigl(z(z+2)+n\bigr)-2nz^n-2n^2z^{n-1}+6\,\mathbf1_{n=3}z^2.}
\]
Its minimum degree and the number of minimum sets are
\[
\boxed{\gamma_{LD}(G_n)=\begin{cases}n,&n=3,4,\\n-1,&n\ge5,\end{cases}\qquad
N_{LD}(G_n)=\begin{cases}14,&n=3,\\56,&n=4,\\n(2^{n-1}-2n),&n\ge5.\end{cases}}
\]
For \(n\ge5\), every minimum set omits one matched pair and selects exactly one endpoint from each remaining pair, with at least two selected vertices on each bipartition side. In particular, the number of minimum sets with \(i\) selected vertices on the \(a\)-side is exactly \(n\binom{n-1}{i}\) for \(2\le i\le n-3\), and zero for all other \(i\) at size \(n-1\). Since \(\gamma_{LD}(K_{n,n})=2n-2\), deleting a perfect matching halves the minimum for every \(n\ge5\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The matched vertices are distinct and individually labeled. A locating-dominating set \(S\subseteq V(G)\) has the property that the open signatures \(N_G(v)\cap S\), for all \(v\notin S\), are nonempty and pairwise distinct. No separation of vertices *inside* \(S\) is required; this is not an identifying code or a total locating code. The polynomial counts literal vertex subsets, not orbit classes. The theorem assumes \(n\ge3\); \(n=2\) has a disconnected exceptional structure.

## Proof
Write \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), \(X=\{i:a_i\in S\}\), \(Y=\{i:b_i\in S\}\), and \(I=[n]\setminus X\), \(J=[n]\setminus Y\). For unselected vertices,
\[
N(a_i)\cap S=\{b_j:j\in Y\setminus\{i\}\},\quad
N(b_j)\cap S=\{a_i:i\in X\setminus\{j\}\}.
\]
Two distinct unselected \(a\)-vertices have equal signatures if and only if both of their indices lie outside \(Y\). Therefore no two unselected vertices within \(A\) collide if and only if \(|I\cap J|\le1\). Exactly the same condition separates all unselected vertices within \(B\). An unselected \(a\)-vertex and an unselected \(b\)-vertex have signatures on disjoint vertex sides. Provided both signatures are nonempty, they cannot coincide. Thus *separation* is equivalent to the single bound \(|I\cap J|\le1\), together with domination.

For domination, if \(Y=\varnothing\), all \(a\)-vertices must be selected, while if \(Y=\{j\}\), the vertex \(a_j\) must be selected. If \(|Y|\ge2\), every unselected \(a\)-vertex has a selected neighbor. The symmetric statements with \(X\) and \(B\) are also necessary and sufficient. These conditions exactly describe every locating-dominating set.

Encode each matched pair \((a_i,b_i)\) as one of four states: neither selected, \(a_i\) only, \(b_i\) only, or both. Their respective weights are \(1,x,y,xy\). The condition \(|I\cap J|\le1\) permits at most one *neither* state. Its uncorrected generating polynomial is therefore
\[
P_n(x,y)=(x+y+xy)^n+n(x+y+xy)^{n-1}.
\]
We remove precisely the configurations violating domination. If \(Y=\varnothing\), there are exactly \(n\) invalid permitted words, each having one neither state and \(n-1\) \(a\)-only states, contributing \(nx^{n-1}\); the symmetric contribution is \(ny^{n-1}\). If \(Y=\{j\}\) but \(a_j\notin S\), then pair \(j\) is \(b\)-only, and all other pairs are \(a\)-only except for an optional single neither pair. These contribute \(nx^{n-1}y+n(n-1)x^{n-2}y\). Symmetrically, \(nx y^{n-1}+n(n-1)xy^{n-2}\) is removed. For \(n\ge4\) the two singleton-side obstruction families do not intersect. For \(n=3\), precisely six words consisting of one \(a\)-only, one \(b\)-only, and one neither state were subtracted twice, so \(6xy\) is restored. There are no other overlaps because any other two obstruction types would require at least two neither pairs. This proves the bivariate formula and, on substituting \(x=y=z\), the univariate formula.

The least possible number of selected vertices under \(|I\cap J|\le1\) is \(n-1\). To attain \(n-1\), there must be exactly one neither pair and all other pairs must be singly selected. Domination is then possible precisely when at least two \(a\)-only and at least two \(b\)-only pairs remain, since a singleton selected side has its unique chosen vertex's partner unselected. Such sets exist exactly for \(n\ge5\), and their full census is \(n\sum_{i=2}^{n-3}\binom{n-1}{i}=n(2^{n-1}-2n)\). For \(n=3,4\), the least exponent in the proved polynomial is \(n\), with coefficients \(14\) and \(56\), respectively (also obtainable by expanding the displayed formula). Finally, in \(K_{n,n}\) all vertices on the same side are open twins; a locating-dominating set may omit at most one vertex from each side. Taking all but one from each side is feasible, so \(\gamma_{LD}(K_{n,n})=2n-2\). Hence the exact halving statement follows.

## Verification
The included standalone `verify.py` independently constructs open-neighborhood signatures from actual graph adjacency, enumerates all vertex subsets for \(3\le n\le8\), and compares the full *bivariate* counts with the closed polynomial. It separately checks the minimum cardinality and its multiplicity, total counts, and the complete-biclique comparison. The total numbers of locating-dominating sets for \(n=3,4,5,6,7,8\) are respectively \(36,149,588,2103,7178,23913\); the minimum-set numbers are \(14,56,30,120,350,896\). All exact finite tests passed. These tests corroborate the symbolic proof; they are not used to infer the infinite statement.

## Relationship to prior work
The standard (undirected) location-domination definition and its relation to graph identification problems are treated by Bousquet, Deschamps, Lehtilä, and Parreau, *Locating-dominating sets: from graphs to oriented graphs*, arXiv:2112.01910 (first submitted 2021-12-03). That work focuses on the parameters optimized over graph orientations, and its accessible complete preprint does not supply the present crown-graph polynomial. Fazil, Hussain, Akbar, and Ali, *On some variations of dominating identification in graphs*, Kuwait Journal of Science 49(4) (2022), DOI 10.48129/kjs.13175, introduces the location-domination polynomial and gives a result for complete multipartite graphs. The known complete-bipartite formula is compatible with its twin-class argument, but a crown graph for \(n\ge3\) is not complete multipartite, and no monotonicity under deletion derives its polynomial. Related published crown-graph domination studies concern different conditions on vertex subsets. The claimed contribution is the entire bivariate crown-graph enumerator, including the optimum census and exact halving phenomenon, not the definition of location-domination or the complete-bipartite minimum.

## Limitations
The complete text of the 2022 polynomial article could not be inspected; its indexed theorem on complete multipartite graphs, abstract, and bibliographic record were checked, but a previously unindexed crown-specific passage cannot be ruled out. Searches of indexed literature and mathematical findings are not proof of global priority. The theorem does not address partial matching deletion or \(n=2\), and the finite verification is not a computer-assisted proof of the infinite formula. No independent audit has been performed.

## References
1. N. Bousquet, Q. Deschamps, T. Lehtilä, A. Parreau, *Locating-dominating sets: from graphs to oriented graphs*, arXiv:2112.01910, https://arxiv.org/abs/2112.01910 (2021 preprint; published 2023).
2. M. Fazil, I. F. Hussain, A. Akbar, U. Ali, *On some variations of dominating identification in graphs*, Kuwait Journal of Science 49(4) (2022), DOI:10.48129/kjs.13175, https://doi.org/10.48129/kjs.13175.
