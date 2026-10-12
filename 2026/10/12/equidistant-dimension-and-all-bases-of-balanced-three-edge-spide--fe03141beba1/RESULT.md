# Equidistant dimension and all bases of balanced three-edge spiders
## Finding
For every integer \(q\ge3\), let \(T_q\) be the balanced spider obtained from the star \(K_{1,q}\) by subdividing each edge twice. Write arm \(i\) as
\[
c-u_i-v_i-w_i,
\]
where \(c\) is the common center and \(w_i\) is a leaf. Then
\[
\operatorname{eqdim}(T_q)=2q.
\]

More strongly, the minimum distance-equalizer sets are exactly the following \(q+1\) sets. One is the odd bipartition class
\[
B=\{u_i,w_i:1\le i\le q\}.
\]
The other \(q\) are
\[
A\cup\bigl(U\setminus\{u_j\}\bigr),\qquad 1\le j\le q,
\]
where
\[
A=\{c,v_1,\ldots,v_q\},
\qquad
U=\{u_1,\ldots,u_q\}.
\]
Consequently \(T_q\) has exactly \(q+1\) equidistant bases.

## Assumptions and scope
All graphs are finite, simple, and connected. A set \(S\subseteq V(G)\) is a distance-equalizer set if for every two distinct vertices \(x,y\notin S\) there is some \(s\in S\) satisfying
\[
d(s,x)=d(s,y).
\]
The equidistant dimension \(\operatorname{eqdim}(G)\) is the minimum cardinality of a distance-equalizer set.

The graph \(T_q\) is bipartite with classes
\[
A=\{c,v_1,\ldots,v_q\}
\]
and
\[
B=\{u_i,w_i:1\le i\le q\}.
\]
Thus \(|A|=q+1\) and \(|B|=2q\).

## Proof
A general result for connected bipartite graphs says that every distance-equalizer set contains one entire bipartition class. We apply that dichotomy and then sharpen it using the tree geometry of \(T_q\).

First suppose that a distance-equalizer set \(S\) contains \(B\). Then automatically
\[
|S|\ge 2q.
\]
The class \(B\) itself is a distance-equalizer set when \(q\ge3\). The vertices outside \(B\) are precisely the vertices of \(A\). For the pair \(c,v_i\), the vertex \(u_i\) has distance one to both. For distinct \(i,j\), choose an index \(k\notin\{i,j\}\), possible because \(q\ge3\). Then
\[
d(u_k,v_i)=d(u_k,v_j)=3.
\]
Hence \(B\) is a distance-equalizer set of size \(2q\).

Now suppose that \(S\) contains \(A\). Write
\[
S=A\cup R,
\qquad R\subseteq B,
\]
and let
\[
I=\{i:u_i\notin R\}.
\]
We prove \(|R|\ge q-1\).

If \(|I|\le1\), then at least \(q-1\) of the vertices \(u_i\) lie in \(R\), so the claim is immediate.

Assume \(|I|\ge2\). Fix \(i\in I\) and choose \(i'\in I\setminus\{i\}\). If \(w_i\notin R\), then both \(u_{i'}\) and \(w_i\) lie outside \(S\). In the tree \(T_q\), the unique path between them is
\[
u_{i'}-c-u_i-v_i-w_i,
\]
which has length four and unique midpoint \(u_i\). Therefore the only vertex equidistant from \(u_{i'}\) and \(w_i\) is \(u_i\). But \(u_i\notin S\), contradicting that \(S\) is a distance-equalizer set. Hence every \(i\in I\) forces \(w_i\in R\).

Thus \(R\) contains all \(q-|I|\) vertices \(u_i\) with \(i\notin I\) and all \(|I|\) vertices \(w_i\) with \(i\in I\). Consequently
\[
|R|\ge q
\]
whenever \(|I|\ge2\). In every case \(|R|\ge q-1\), so
\[
|S|\ge(q+1)+(q-1)=2q.
\]
Together with the set \(B\), this proves
\[
\operatorname{eqdim}(T_q)=2q.
\]

It remains to classify equality. If a minimum set contains \(B\), then its size is already \(2q\), so it is exactly \(B\).

Suppose a minimum set contains \(A\). Then \(|R|=q-1\). The preceding argument rules out \(|I|\ge2\), because that would force \(|R|\ge q\). It also rules out \(|I|=0\), because then all \(q\) vertices \(u_i\) lie in \(R\). Hence \(|I|=1\), say \(I=\{j\}\). The \(q-1\) selected vertices \(u_i\) with \(i\ne j\) already exhaust the budget \(|R|=q-1\), so no \(w_i\) lies in \(R\). Thus
\[
R=U\setminus\{u_j\}.
\]

Conversely, fix \(j\) and set
\[
S_j=A\cup(U\setminus\{u_j\}).
\]
The vertices outside \(S_j\) are \(u_j,w_1,\ldots,w_q\). Any two leaves \(w_i,w_k\) are equalized by \(c\), since both are at distance three from \(c\). The pair \(u_j,w_j\) is equalized by \(v_j\), at distance one from both. Finally, for \(i\ne j\), the selected vertex \(u_i\) satisfies
\[
d(u_i,u_j)=d(u_i,w_i)=2.
\]
Hence every \(S_j\) is a distance-equalizer set. The complete basis list therefore consists of \(B\) and the \(q\) sets \(S_j\).

## Verification
The included checker constructs \(T_q\), computes all-pairs shortest-path distances by breadth-first search, and tests the distance-equalizer definition literally.

For every \(3\le q\le6\), it enumerates every vertex subset of size at most \(2q\), rejects every smaller set, and compares the entire family of size-\(2q\) equalizers with the predicted \(q+1\) bases.

## Relationship to prior work
The equidistant dimension was introduced in 2021. The foundational paper proves that every distance-equalizer set in a connected bipartite graph contains a whole bipartition class and studies complete graphs, complete multipartite graphs, bistars, paths, cycles, and Johnson graphs. It explicitly identifies the exact equidistant dimension of trees as an open direction and proposes a path-extremality conjecture. The balanced spiders treated here are not covered by the bistar formulas: every arm has three edges and the proof depends on unique midpoints across distinct arms.

A 2024 continuation proves complexity results and develops lexicographic-product formulas. Its stated scope does not include spiders, subdivided stars, or a general tree formula. Targeted searches under balanced spider, subdivided star, twice-subdivided star, and distance-equalizer terminology did not locate the value \(2q\) or the \(q+1\)-basis classification.

The present result also shows that the general bipartite lower bound can be far from sharp. The smaller bipartition class has size \(q+1\), while the actual equidistant dimension is \(2q\), a gap of \(q-1\).

## Limitations
The theorem is restricted to balanced spiders whose arms have exactly three edges and to \(q\ge3\). The boundary case \(q=2\) is the path \(P_7\) and has different basis structure. No claim is made for unequal arm lengths, longer balanced spiders, or the general tree-extremality conjecture.

The exhaustive computation for \(3\le q\le6\) is corroborative only. The all-\(q\) theorem follows from the bipartite-class dichotomy and the midpoint argument in the proof.

## References
1. A. González, C. Hernando, M. Mora, “The Equidistant Dimension of Graphs,” arXiv:2107.10805v1, 22 July 2021; Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 1757–1775, DOI 10.1007/s40840-022-01295-z.
2. A. Gispert-Fernández, J. A. Rodríguez-Velázquez, “The equidistant dimension of graphs: NP-completeness and the case of lexicographic product graphs,” AIMS Mathematics 9(6) (2024), 15404–15421, DOI 10.3934/math.2024744.
