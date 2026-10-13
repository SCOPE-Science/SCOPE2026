# Unique minimum \([k]\)-Roman functions of half graphs
## Finding
For integers
\[
k\ge2,\qquad n\ge3,
\]
let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma_{[kR]}(H_n)=2(k+1).
\]

More strongly, the minimum \([k]\)-Roman dominating function is unique:
\[
f(a_1)=f(b_n)=k+1,
\]
and
\[
f(v)=0
\]
for every other vertex \(v\).

The scalar specialization \(k=2\), namely
\[
\gamma_{dR}(H_n)=6,
\]
is already covered by the published theorem for connected chain graphs. The new content here is the complete minimum-function rigidity at \(k=2\), together with the exact value and unique optimum for every \(k\ge3\).

## Assumptions and scope
For an integer \(k\ge1\), a \([k]\)-Roman dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,\ldots,k+1\}
\]
such that every vertex \(v\) with
\[
f(v)<k
\]
satisfies
\[
\sum_{u\in N[v]} f(u)\ge k+|AN(v)|,
\]
where
\[
AN(v)=\{u\in N(v):f(u)>0\}.
\]

Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{[kR]}(G)\) is the minimum possible weight.

The theorem assumes \(k\ge2\) and \(n\ge3\). The restriction is structural: for \(k=1\), the ordinary Roman case has additional minimum functions at \(H_3\); for \(n=2\), additional minimum functions also occur for \(k\ge2\).

## Proof
Write
\[
x_i=f(a_i),\qquad y_i=f(b_i).
\]

The vertices \(b_1\) and \(a_n\) are leaves, with support vertices \(a_1\) and \(b_n\), respectively. Put
\[
L=x_1+y_1,\qquad R=x_n+y_n.
\]

For a leaf-support pair, the \([k]\)-Roman condition gives
\[
L\ge k,\qquad R\ge k.
\tag{1}
\]
Moreover,
\[
L=k\quad\Longleftrightarrow\quad (x_1,y_1)=(0,k),
\tag{2}
\]
and
\[
R=k\quad\Longleftrightarrow\quad (x_n,y_n)=(k,0).
\tag{3}
\]
Indeed, if a leaf has value below \(k\), then its support must be active and the pair has total at least \(k+1\); equality \(k\) is therefore possible only when the leaf itself has value \(k\) and its support has value \(0\).

We first prove the lower bound. If both \(L\) and \(R\) are at least \(k+1\), then immediately
\[
\omega(f)\ge2(k+1).
\tag{4}
\]

Suppose instead that
\[
R=k.
\]
By (3),
\[
x_n=k,\qquad y_n=0.
\]
The condition at \(b_n\) becomes
\[
\sum_{\substack{i<n\\x_i>0}}(x_i-1)\ge1.
\tag{5}
\]
Hence some \(a_i\) with \(i<n\) has label at least \(2\).

If \(y_1\ge k\), then the vertices outside \(\{a_n,b_n\}\) already have weight at least
\[
k+2.
\]

Now suppose \(y_1<k\). The leaf condition at \(b_1\) gives
\[
x_1+y_1\ge k+1.
\tag{6}
\]
If the vertex supplied by (5) is not \(a_1\), then the outside weight is at least \(k+3\). If it is \(a_1\) and every other vertex outside the right leaf-support pair were zero, then \(a_2\) would have no active neighbor: \(b_1\) is not adjacent to \(a_2\), while \(b_2,\ldots,b_n\) would all be zero. Since \(a_2<k\), this is impossible. Thus at least one additional positive label occurs, and again the outside weight is at least \(k+2\).

Therefore
\[
R=k\quad\Longrightarrow\quad \omega(f)\ge2k+2.
\]
The symmetric argument applies when \(L=k\). Together with (4),
\[
\omega(f)\ge2(k+1).
\tag{7}
\]

For the matching upper bound, define
\[
f(a_1)=f(b_n)=k+1
\]
and assign zero to all other vertices. Every zero vertex of \(A\) is adjacent to \(b_n\), and every zero vertex of \(B\) is adjacent to \(a_1\). Hence every constrained zero vertex has exactly one active neighbor and closed-neighborhood weight \(k+1\), so equality holds in its defining inequality. Thus
\[
\gamma_{[kR]}(H_n)=2(k+1).
\]

It remains to prove uniqueness.

Let \(f\) have weight \(2k+2\). We first show that equality cannot occur with \(R=k\). As above,
\[
(x_n,y_n)=(k,0).
\]

If \(y_1\ge k\), equality in the lower-bound argument forces \(y_1=k\), exactly one vertex of \(A\setminus\{a_n\}\) to have label \(2\), and all other vertices outside \(\{a_n,b_n\}\) to have label \(0\). If that label \(2\) is at \(a_1\), then \(a_2\) has no active neighbor and fails the defining inequality. If it is not at \(a_1\), then \(a_1=0\) and its only active neighbor is \(b_1\) with label \(k\); its closed-neighborhood weight is then \(k\) while the right side of the defining inequality is \(k+1\). Both possibilities are impossible.

If \(y_1<k\), equality forces
\[
x_1+y_1=k+1
\]
and permits only one unit of weight outside the two leaf-support pairs. Condition (5) then forces its required excess to come from \(a_1\). If there is no additional positive vertex, \(a_2\) has no active neighbor and fails. If the single extra unit lies on the \(A\)-side, then all of \(b_2,\ldots,b_n\) are zero and \(a_2\), whether zero or labeled \(1\), again fails. If the single extra unit is some \(b_t\) with \(2\le t\le n-1\), then \(a_2\) sees at most that one active neighbor of label \(1\); its closed-neighborhood weight is at most \(1\), whereas the required lower bound is at least \(k+1\). This is impossible because \(k\ge2\).

Thus \(R\ne k\). By symmetry,
\[
L\ne k.
\]
Using (1) and the total weight \(2k+2\), we obtain
\[
L=R=k+1,
\]
and every interior vertex
\[
a_2,\ldots,a_{n-1},b_2,\ldots,b_{n-1}
\]
has label \(0\).

Now \(a_2\) is zero. Among its neighbors \(b_2,\ldots,b_n\), the only vertex that can be active is \(b_n\). Therefore the defining inequality at \(a_2\) forces
\[
y_n=k+1.
\]
Since \(R=k+1\),
\[
x_n=0.
\]

Symmetrically, \(b_{n-1}\) is zero and its only possible active neighbor is \(a_1\), so
\[
x_1=k+1,
\]
and then
\[
y_1=0.
\]
This is exactly the claimed function.

## Verification
The included checker constructs each half graph directly and evaluates the defining \([k]\)-Roman inequality at every constrained vertex.

For
\[
2\le k\le5,\qquad 3\le n\le5,
\]
it exhausts every labeling whose total weight is at most
\[
2(k+1).
\]
For every tested pair, it finds no feasible labeling below the claimed optimum and finds exactly one feasible labeling at the optimum, namely the endpoint labeling from the theorem.

## Relationship to prior work
A 2020 paper on Roman \(\{2\}\)-domination and double Roman domination proves that every connected non-complete-bipartite chain graph with both bipartition classes of size different from \(2\) has double Roman domination number \(6\). Hence, for \(n\ge3\), the scalar case
\[
\gamma_{[2R]}(H_n)=6
\]
is already known because \(H_n\) is such a chain graph. That theorem gives the value, not the complete family of minimum double Roman functions.

The 2023 general \([k]\)-Roman paper defines the same invariant for arbitrary \(k\), gives general bounds, tree results, and complexity results on bipartite and chordal graphs. Its inspected full text contains no half-graph or chain-graph specialization.

A 2024 continuation develops further general bounds and exact results for other graph classes, while a 2026 paper gives additional exact families and complexity results. Targeted inspection of those sources and searches under the aliases “half graph,” “chain graph,” “double Roman,” “triple Roman,” and “\([k]\)-Roman” did not locate the theorem proved here.

Thus the known double-Roman scalar value is explicitly excluded from the originality claim. The accepted contribution is the uniqueness of the double-Roman optimum on half graphs and the uniform exact value plus uniqueness for every \(k\ge3\).

## Limitations
The theorem does not classify nonminimum \([k]\)-Roman functions.

The cases \(k=1\) and \(n=2\) are excluded because the optimum is not rigid in the stated form.

The finite computation is corroborative only. The arbitrary-parameter theorem follows from the leaf-pair and nested-neighborhood proof.

A differently phrased or non-indexed treatment of the same optimizer classification may exist.

## References
1. C. Padamutham, P. V. S. Reddy, “Complexity of Roman \(\{2\}\)-domination and the double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics 17(3) (2020), 1081–1086, DOI 10.1016/j.akcej.2020.01.005; published online 4 May 2020.
2. N. Khalili, J. Amjadi, M. Chellali, S. M. Sheikholeslami, “On \([k]\)-Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics (2023), DOI 10.1080/09728600.2023.2241531; published online 4 August 2023.
3. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera Lopez, M. P. Álvarez-Ruiz, “Further Results on the \([k]\)-Roman Domination in Graphs,” Bulletin of the Iranian Mathematical Society 50 (2024), article 27, DOI 10.1007/s41980-024-00872-1; published 27 March 2024.
4. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, M. P. Álvarez-Ruíz, “Complexity and Exact Values for \([k]\)-Roman and Strong Roman Domination for Specific Graph Families,” Mathematics 14(9) (2026), 1535, DOI 10.3390/math14091535.
