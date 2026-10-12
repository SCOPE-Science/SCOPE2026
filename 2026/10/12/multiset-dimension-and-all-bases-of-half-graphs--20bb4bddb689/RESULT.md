# Multiset dimension and all bases of half graphs
## Finding
Let \(H_n\) be the half graph with \(n\ge2\), bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and \(a_i b_j\in E(H_n)\) exactly when \(i\le j\). Then
\[
\operatorname{md}(H_n)=
\begin{cases}
n-1,&n\text{ even},\\
n,&n\text{ odd}.
\end{cases}
\]

If \(n=2m\), the two multiset bases are
\[
E_1=\{a_{2r}:1\le r\le m\}\cup\{b_{2r}:1\le r\le m-1\}
\]
and
\[
E_2=\{a_{2r+1}:1\le r\le m-1\}\cup\{b_{2r-1}:1\le r\le m\}.
\]

If \(n=2m-1\), define
\[
A_d=\{a_i:i\text{ even},\,i\le2d\}\cup\{a_i:i\text{ odd},\,i\ge2d+1\},
\quad 0\le d\le m-1,
\]
and
\[
B_c=\{b_i:i\text{ even},\,i\le2c-2\}\cup
\{b_i:i\text{ odd},\,2c-1\le i\le n-1\},
\quad 1\le c\le m.
\]
One orientation of the bases is
\[
A_d\cup B_c,\qquad 0\le d<c\le m,
\]
and the other is obtained by the automorphism
\[
a_i\longleftrightarrow b_{n+1-i}.
\]
Hence the number of odd-order bases is
\[
m(m+1)=\frac{(n+1)(n+3)}4.
\]

## Assumptions and scope
For \(W\subseteq V(G)\), the multiset representation of \(v\) is
\[
r_m(v\mid W)=\{d(v,w):w\in W\},
\]
with multiplicities retained. A set is multiset-resolving if these multisets are pairwise distinct; a minimum such set is a multiset basis.

## Proof
Write
\[
p=|W\cap A|,\qquad q=|W\cap B|,
\]
and let \(x_i\) and \(y_j\) indicate membership of \(a_i\) and \(b_j\) in \(W\). Put
\[
R_i=\sum_{j=i}^n y_j,\qquad S_j=\sum_{i=1}^j x_i.
\]
Distances in \(H_n\) satisfy
\[
d(a_i,b_j)=1\quad(i\le j),\qquad d(a_i,b_j)=3\quad(i>j),
\]
and distinct same-side vertices are at distance \(2\). Therefore
\[
r_m(a_i\mid W)=
\begin{cases}
\{0,2^{p-1},1^{R_i},3^{q-R_i}\},&a_i\in W,\\
\{2^p,1^{R_i},3^{q-R_i}\},&a_i\notin W,
\end{cases}
\]
with the symmetric formula for \(b_j\) using \(S_j\).

Hence vertices on the same side and with the same membership status must have distinct cumulative counts. Since \(R_i\in\{0,\ldots,q\}\) and \(S_j\in\{0,\ldots,p\}\),
\[
p\le q+1,\qquad n-p\le q+1,\qquad
q\le p+1,\qquad n-q\le p+1.
\]
Thus every multiset-resolving set has size at least \(n-1\).

For odd \(n=2m-1\), equality would force \(p=q=m-1\). The omitted vertices on each side would then each realize all count values \(0,\ldots,m-1\). Because \(p=q\), an omitted \(A\)-vertex and an omitted \(B\)-vertex with the same count would have identical multisets, a contradiction. Hence \(\operatorname{md}(H_n)\ge n\).

Now take \(p=m,q=m-1\). Cross-side collisions are impossible because the multiplicity of distance \(2\) differs. The selected \(A\)-vertices must realize all \(m\) possible \(R\)-values. Thus the constant-\(R\) blocks consist of one singleton block and \(m-1\) two-vertex blocks, each containing exactly one selected \(A\)-vertex. If the singleton is the \(c\)-th block, the \(B\)-part is exactly \(B_c\).

In a two-vertex block, selecting the right \(A\)-vertex gives the preceding cumulative \(S\)-value at the unselected \(B\)-position, while selecting the left gives the succeeding value. Repetition among unselected \(B\)-vertices occurs exactly at a left-to-right transition between consecutive two-vertex blocks. Before the singleton the legal choices are therefore an initial run of right choices followed by left choices; after the singleton the final omitted \(B\)-vertex forces all remaining two-vertex blocks to use the right choice. Hence there is a unique \(d\) with \(0\le d<c\), and the \(A\)-part is \(A_d\). This proves the odd classification and its count.

For even \(n=2m\), equality gives \(\{p,q\}=\{m,m-1\}\). Assume \(p=m,q=m-1\). Both selected and omitted \(A\)-vertices then have size \(q+1\), so every constant-\(R\) block has length two with one selected vertex. This forces the selected \(B\)-indices to be \(2,4,\ldots,2m-2\). The omitted \(B\)-vertices must realize all \(p+1\) prefix counts, which forces the selected \(A\)-vertex in each pair to be the even-indexed one. Thus \(W=E_1\). The side-reversed case gives \(E_2\). Direct substitution in the representation formulas verifies both sets.

## Verification
The included checker constructs \(H_n\) for \(2\le n\le9\), computes all-pairs distances, and exhaustively tests every subset up to the claimed minimum size. It compares the complete set of minimum multiset-resolving sets with the formulas above.

## Relationship to prior work
Multiset dimension was introduced in 2017 as a variation of metric dimension that discards the order of landmark distances. The foundational paper proves general bounds, finiteness conditions, and small-dimension examples, but its searchable full text contains no half, chain, or bipartite occurrence.

A 2021 follow-up develops further general properties of multiset dimension. Its accessible journal scope does not identify half graphs or chain graphs. Targeted searches under half graph, chain graph, Ferrers graph, and multiset-resolving terminology did not locate the parity theorem or the complete basis classification above.

## Limitations
The theorem concerns canonical half graphs and does not state a formula for arbitrary chain graphs with repeated twin classes. The finite verification through \(n=9\) is corroborative only. A differently phrased or non-indexed half-graph result may exist.

## References
1. R. Simanjuntak, P. Siagian, T. Vetrík, “The multiset dimension of graphs,” arXiv:1711.00225v1, 1 November 2017.
2. N. H. Bong, Y. Lin, “Some properties of the multiset dimension of graphs,” Electronic Journal of Graph Theory and Applications 9(1) (2021), DOI 10.5614/ejgta.2021.9.1.19.
