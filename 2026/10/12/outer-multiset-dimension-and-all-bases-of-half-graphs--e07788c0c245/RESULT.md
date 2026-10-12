# Outer multiset dimension and all bases of half graphs
## Finding
Let \(H_n\) be the half graph with \(n\ge2\), bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]
Then
\[
\operatorname{dim}_{\mathrm{ms}}(H_n)=n-1.
\tag{1}
\]

For every subset
\[
T\subseteq\{1,\ldots,n-1\},
\]
define
\[
W_T=\{a_{k+1}:k\in T\}\cup\{b_k:k\notin T\}.
\tag{2}
\]
Every outer multiset basis is of this form. If \(n\) is even, every \(W_T\) is a basis, so the number of bases is
\[
2^{n-1}.
\tag{3}
\]
If \(n\) is odd, \(W_T\) is a basis exactly when
\[
|T|\ne\frac{n-1}{2},
\]
so the number of bases is
\[
2^{n-1}-\binom{n-1}{(n-1)/2}.
\tag{4}
\]

## Assumptions and scope
For \(W\subseteq V(G)\) and \(v\in V(G)\setminus W\), the outer multiset representation of \(v\) is the multiset
\[
r_m(v\mid W)=\{d(v,w):w\in W\},
\]
with multiplicities retained and landmark identities discarded. The set \(W\) is outer multiset resolving if the representations of all vertices outside \(W\) are pairwise distinct. The minimum cardinality of such a set is the outer multiset dimension \(\operatorname{dim}_{\mathrm{ms}}(G)\).

## Proof
Let \(W\subseteq V(H_n)\). Put
\[
p=|W\cap A|,\qquad q=|W\cap B|,
\]
and let
\[
x_i=\mathbf 1_{\{a_i\in W\}},\qquad y_j=\mathbf 1_{\{b_j\in W\}}.
\]
Define the cumulative landmark counts
\[
R_i=\sum_{j=i}^{n}y_j,
\qquad
S_j=\sum_{i=1}^{j}x_i.
\]

Two distinct vertices in the same bipartition class have distance \(2\), while
\[
d(a_i,b_j)=
\begin{cases}
1,&i\le j,\\
3,&i>j.
\end{cases}
\]
Hence, for vertices outside \(W\),
\[
r_m(a_i\mid W)=\{2^p,1^{R_i},3^{q-R_i}\},
\tag{5}
\]
and
\[
r_m(b_j\mid W)=\{2^q,1^{S_j},3^{p-S_j}\}.
\tag{6}
\]
Here the exponents record multiplicities.

Among omitted vertices of \(A\), the values \(R_i\) must be distinct. Since there are only \(q+1\) possible values, this gives
\[
n-p\le q+1.
\]
Similarly,
\[
n-q\le p+1.
\]
Adding yields
\[
|W|=p+q\ge n-1.
\tag{7}
\]

Assume equality in (7). Then both preceding inequalities are equalities. Thus the omitted vertices of \(A\) realize every value \(0,1,\ldots,q\) exactly once, and the omitted vertices of \(B\) realize every value \(0,1,\ldots,p\) exactly once.

Write
\[
X_k=\sum_{i=1}^{k}x_i,
\qquad
Y_k=\sum_{j=1}^{k}y_j,
\]
with \(Y_0=0\). Consider the omitted \(A\)-vertices among indices \(1,\ldots,k\). Their distinct prefix counts \(Y_{i-1}\) lie in \(\{0,\ldots,Y_{k-1}\}\), so
\[
k-X_k\le Y_{k-1}+1.
\tag{8}
\]
Now consider the omitted \(B\)-vertices among indices \(k,\ldots,n\). Their distinct values \(S_j=X_j\) lie in \(\{X_k,\ldots,p\}\), so
\[
(n-k+1)-(q-Y_{k-1})\le p-X_k+1.
\tag{9}
\]
Using \(p+q=n-1\), inequalities (8)--(9) force
\[
X_k+Y_{k-1}=k-1
\qquad(1\le k\le n).
\tag{10}
\]
At \(k=1\), (10) gives \(x_1=0\); at \(k=n\), it gives \(y_n=0\). Subtracting (10) at consecutive indices gives
\[
x_{k+1}+y_k=1
\qquad(1\le k\le n-1).
\tag{11}
\]
Therefore every size-\(n-1\) outer multiset resolving set must choose exactly one vertex from each shifted pair \(\{a_{k+1},b_k\}\), and no other vertices. This is precisely the family (2).

Conversely, fix \(T\) and take \(W_T\). Put \(p=|T|\) and \(q=n-1-p\). If the selected \(B\)-indices are
\[
k_1<\cdots<k_q,
\]
then the omitted \(A\)-vertices are
\[
a_1,a_{k_1+1},\ldots,a_{k_q+1},
\]
and their \(R\)-values are
\[
q,q-1,\ldots,0.
\]
Thus all omitted \(A\)-vertices have distinct representations. Symmetrically, all omitted \(B\)-vertices have distinct representations.

If \(p\ne q\), a cross-side collision is impossible because (5) and (6) contain different multiplicities of distance \(2\). If \(p=q\), then \(n\) is odd and the two always-omitted vertices \(a_1\) and \(b_n\) have the same multiset
\[
\{1^p,2^p\}.
\]
Thus \(W_T\) fails exactly in the balanced case
\[
p=q=\frac{n-1}{2}.
\]
This proves (1)--(4).

## Verification
The included checker constructs \(H_n\), computes all-pairs distances, and directly tests the outer multiset condition for every candidate subset of sizes \(n-2\) and \(n-1\) for
\[
2\le n\le10.
\]
It verifies that no size-\(n-2\) set works and that the complete set of size-\(n-1\) bases agrees with (2)--(4).

## Relationship to prior work
Outer multiset dimension was introduced in 2019 as an unordered-distance analogue of outer metric dimension. The foundational primary source develops the definition, general bounds, finiteness criteria, and examples; targeted full-text searches found no occurrence of half graphs, chain graphs, or Ferrers graphs.

A later primary paper develops further structural properties and explicitly places the subject in Mathematics Subject Classification \(05C12\) and \(05C76\). Its full text likewise contains no half, chain, or Ferrers occurrence. Its general results do not determine the nested-distance count structure used above.

The closest available exact-family comparison is complete multipartite graphs, whose outer multiset bases are governed by part sizes. Half graphs instead have strictly nested neighborhoods, and the shifted-pair classification (2) produces a parity obstruction absent from the complete-multipartite description.

## Limitations
The theorem treats the canonical half graph, not arbitrary chain graphs with repeated twin classes.

The exhaustive computation through \(n=10\) is corroborative only. The arbitrary-order result follows from the cumulative-count proof.

Targeted searches cannot exclude a differently phrased or non-indexed earlier treatment.

## References
1. M. Gil-Pons, Y. Ramírez-Cruz, E. Trujillo-Rasua, I. G. Yero, “Distance-based vertex identification in graphs: the outer multiset dimension,” arXiv:1902.03017v1, 8 February 2019; Applied Mathematics and Computation 363 (2019), 124612, DOI 10.1016/j.amc.2019.124612.
2. S. Klavžar, D. Kuziak, I. G. Yero, “Further contributions on the outer multiset dimension of graphs,” arXiv:2207.06834v1, 14 July 2022; Results in Mathematics 78 (2023), 50, DOI 10.1007/s00025-022-01829-8.
