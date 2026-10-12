# Dual mutual-visibility profiles of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), positive part sizes, and
\[
N=\sum_{i=1}^r n_i.
\]
For \(X\subseteq V(G)\), put \(Y=V(G)\setminus X\),
\[
x_i=|X\cap V_i|,
\qquad
y_i=|Y\cap V_i|=n_i-x_i.
\]
Then \(X\) is a dual mutual-visibility set if and only if
\[
Y\setminus V_i\ne\varnothing
\]
for every \(i\) for which \(x_i\ge2\) or \(y_i\ge2\).

Define the dual visibility polynomial by
\[
\mathcal V_d(G;z)=\sum_{X\text{ dual mutual-visibility}}z^{|X|}.
\]
Let
\[
p=|\{i:n_i\ge2\}|.
\]
If \(p=0\), then \(G\) is complete and
\[
\mathcal V_d(G;z)=(1+z)^N.
\]
If \(p\ge1\), then
\[
\mathcal V_d(G;z)
=(1+z)^N-
\sum_{i:n_i\ge2}D_i(z)
+(p-1)z^N,
\]
where
\[
D_i(z)=
\begin{cases}
z^N+z^{N-2},&n_i=2,\\
z^{N-n_i}(1+z)^{n_i},&n_i\ge3.
\end{cases}
\]

The dual mutual-visibility chromatic number is
\[
\chi_{\mu_d}(G)=
\begin{cases}
1,&G\text{ is complete},\\
\infty,&G\cong K_{1,n}\text{ with }n\ge3,\\
2,&\text{otherwise}.
\end{cases}
\]
Thus \(K_{1,2}\) is the exact star boundary: it admits a two-color dual mutual-visibility coloring, while every \(K_{1,n}\) with \(n\ge3\) admits none with any finite number of colors.

## Assumptions and scope

Graphs are finite, simple, connected, and nontrivial. A set \(X\subseteq V(G)\) is dual mutual-visibility when every pair of vertices both in \(X\), and every pair both in \(V(G)\setminus X\), has a shortest path whose internal vertices avoid \(X\). A dual mutual-visibility coloring is a vertex partition into dual mutual-visibility sets, and \(\chi_{\mu_d}(G)=\infty\) when no such finite partition exists.

The result concerns complete multipartite graphs themselves, not line graphs or Cartesian products of complete graphs.

## Proof

Vertices in different partite classes are adjacent, so they are \(X\)-visible for every \(X\). Two distinct vertices \(u,v\in V_i\) have distance two. Every shortest \(u,v\)-path has one internal vertex, and the possible internal vertices are exactly the vertices outside \(V_i\). Therefore
\[
u\text{ and }v\text{ are }X\text{-visible}
\quad\Longleftrightarrow\quad
Y\setminus V_i\ne\varnothing.
\]

For dual mutual-visibility, same-part pairs matter only when both endpoints lie in \(X\), which occurs exactly when \(x_i\ge2\), or both endpoints lie in \(Y\), which occurs exactly when \(y_i\ge2\). This proves the stated characterization.

We next count the invalid sets. If the characterization fails at part \(V_i\), then \(Y\subseteq V_i\) and either \(x_i\ge2\) or \(y_i\ge2\). A singleton part can never cause failure. If \(n_i=2\), failure occurs exactly for \(|Y\cap V_i|=0\) or \(|Y\cap V_i|=2\), contributing
\[
D_i(z)=z^N+z^{N-2}.
\]
If \(n_i\ge3\), then \(x_i+y_i=n_i\ge3\), so at least one of \(x_i,y_i\) is at least two for every \(Y\subseteq V_i\). Hence the full bad family at \(V_i\) contributes
\[
D_i(z)=\sum_{Y\subseteq V_i}z^{N-|Y|}
=z^{N-n_i}(1+z)^{n_i}.
\]
For two distinct non-singleton parts \(V_i,V_j\), the corresponding bad families intersect only at \(Y=\varnothing\), equivalently \(X=V(G)\). Thus inclusion-exclusion contributes a net correction of \((p-1)z^N\), giving the polynomial formula.

It remains to determine the chromatic number. If every part is a singleton, \(G\) is complete and every subset is dual mutual-visibility, so one color suffices. If \(G\) is noncomplete, the full set \(V(G)\) is not dual mutual-visibility, so at least two colors are required whenever a coloring exists.

Consider a star \(K_{1,n}\) and let \(c\) be its center. Suppose a dual mutual-visibility set \(X\) contains \(c\), and let \(t\) leaves lie in \(X\). Since \(Y\setminus V_{\rm leaf}=\varnothing\), the characterization forces both \(t\le1\) and \(n-t\le1\). This is possible exactly when \(n\le2\). Therefore, when \(n\ge3\), the center belongs to no dual mutual-visibility set and no dual coloring exists. For \(K_{1,2}\), the partition consisting of one class containing the center and one leaf and the other class containing the remaining leaf is a valid two-coloring.

Now suppose \(G\) is noncomplete and is not a star with at least three leaves. If \(r=2\) and both parts have order at least two, split each part nontrivially between two colors. Each color class and its complement then meet both parts, so the characterization makes both classes dual mutual-visibility. If \(r\ge3\) and at least two parts are non-singleton, split two such parts nontrivially between the colors; again both colors meet at least two parts. Finally, if \(r\ge3\) and exactly one part is non-singleton, split that part and assign two distinct singleton parts to opposite colors. In every case both color classes are dual mutual-visibility, proving the value two.

## Verification

The accompanying script `artifacts/verify.py` is a generic finite checker. It builds every nondecreasing complete-multipartite part profile of total order from two through eight. Visibility is checked by breadth-first shortest-path searches after deleting the forbidden internal vertices; the code does not use the closed characterization to decide visibility.

For every subset it compares the direct dual mutual-visibility definition with the structural criterion and compares the resulting cardinality counts with the polynomial formula. It then enumerates every set partition and independently computes the minimum number of valid dual classes, including the infinite cases. The finite computation is corroborative only; the proof above covers all positive part sizes.

## Relationship to prior work

Babu, Jakovac, Kuziak, Lakshmanan, and Yero introduced the dual mutual-visibility chromatic number in 2026. Their paper gives general finite/infinite criteria and exact results for block graphs, Hamming graphs, and strong grids. In particular, their convex-\(K_{1,3}\) criterion already implies the infinite branch for stars with at least three leaves. The inspected full text contains no occurrence of “multipartite”; its uses of complete bipartite graphs arise through the line-graph representation of Hamming graphs, not from colorings of complete multipartite graphs themselves.

Bujtás, Klavžar, and Tian introduced visibility-polynomial methods and observed for balanced complete bipartite graphs \(K_{n,n}\) that, for \(n\ge4\), the maximum dual, outer, and total mutual-visibility set sizes equal \(2(n-1)\). Their work also gives a general characterization of total mutual-visibility sets. It does not give the arbitrary-complete-multipartite dual set profile or dual coloring classification proved here.

Cicerone, Di Stefano, Klavžar, and Yero studied mutual-visibility parameters on diameter-two graphs and cographs. Their cograph theorem determines relationships among maximum visibility numbers; it does not classify all dual mutual-visibility subsets or partitions of complete multipartite graphs.

A recent Builder–Blocker mutual-visibility paper studies complete multipartite graphs, but for a game based on ordinary mutual-visibility sets rather than dual mutual-visibility colorings.

## Limitations

The theorem is specific to dual mutual-visibility. It does not assert analogous formulas for ordinary, outer, or total mutual-visibility colorings, and it does not address list versions or weighted colorings.

The literature comparison is extensive but cannot rule out an unindexed or concurrent equivalent result. Parts of the boundary behavior are known from more general results: notably, the star infinity branch follows from the 2026 convex-\(K_{1,3}\) obstruction. The originality claim concerns the complete arbitrary-part-size dual set characterization, exact dual visibility polynomial, and full dual coloring classification as a single theorem.

## References

1. S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., and I. G. Yero, “A variety of the mutual-visibility coloring problem for graphs,” arXiv:2609.31427v1, first public September 25, 2026.
2. C. Bujtás, S. Klavžar, and J. Tian, “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” arXiv:2412.03066v1; Aequationes Mathematicae 99 (2025), 1883–1901.
3. S. Cicerone, G. Di Stefano, S. Klavžar, and I. G. Yero, “Mutual-visibility problems on graphs of diameter two,” European Journal of Combinatorics 120 (2024), 103995.
4. V. Iršič Chenoweth, S. Klavžar, G. Rus, E. Tan, and J. Tian, “Builder-Blocker Mutual-Visibility Game,” Bulletin of the Malaysian Mathematical Sciences Society (2026), DOI 10.1007/s40840-026-02083-9.
