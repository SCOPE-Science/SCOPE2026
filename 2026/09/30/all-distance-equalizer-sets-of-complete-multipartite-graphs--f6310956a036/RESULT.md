# All distance-equalizer sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite sets \(A_1,\ldots,A_r\), \(n_i=|A_i|\ge1\), and \(N=\sum_i n_i\). For \(S\subseteq V(G)\), put
\[
\operatorname{supp}(S)=\{i:S\cap A_i\ne\varnothing\}.
\]
Then \(S\) is a distance-equalizer set if and only if at least one of the following conditions holds:

1. \(A_i\subseteq S\) for some \(i\);
2. \(|\operatorname{supp}(S)|\ge3\).

Hence the complete selection-profile enumeration is explicit. For integers \(0\le s_i\le n_i\), the number of distance-equalizer sets satisfying \(|S\cap A_i|=s_i\) for every \(i\) is
\[
\begin{cases}
\prod_i\binom{n_i}{s_i},&\text{if some }s_i=n_i\text{ or }|\{i:s_i>0\}|\ge3,\\
0,&\text{otherwise}.
\end{cases}
\]
Equivalently, with
\[
B_i(x_i)=(1+x_i)^{n_i}-1-x_i^{n_i},
\]
the multivariate cardinality enumerator is
\[
\mathcal E_G(x_1,\ldots,x_r)
=\prod_{i=1}^r(1+x_i)^{n_i}
-\left(1+\sum_i B_i(x_i)+\sum_{i<j}B_i(x_i)B_j(x_j)\right).
\]
Setting every \(x_i=x\) gives the ordinary size enumerator
\[
E_G(x)=(1+x)^N-\left(1+\sum_i B_i(x)+\sum_{i<j}B_i(x)B_j(x)\right),
\qquad B_i(x)=(1+x)^{n_i}-1-x^{n_i}.
\]
In particular, the total number of distance-equalizer sets is
\[
E_G(1)=2^N-\left(1+\sum_i(2^{n_i}-2)+\sum_{i<j}(2^{n_i}-2)(2^{n_j}-2)\right).
\]

The classification also determines every minimum distance-equalizer set. If \(r=2\) and \(m=\min\{n_1,n_2\}\), then \(\operatorname{eqdim}(G)=m\), and the minimum sets are exactly the parts of size \(m\). If \(r\ge3\) and \(m=\min_i n_i\), then
\[
\operatorname{eqdim}(G)=\min\{m,3\}.
\]
For \(m=1\), the minimum sets are exactly the singleton parts; for \(m=2\), they are exactly the 2-vertex parts; and for \(m\ge3\), every minimum set has size three and is either an entire 3-vertex part or consists of one vertex from each of three distinct parts. Therefore, writing \(\nu_t=|\{i:n_i=t\}|\), the number of minimum distance-equalizer sets for \(r\ge3\) is
\[
\begin{cases}
\nu_1,&m=1,\\
\nu_2,&m=2,\\
\nu_3+\displaystyle\sum_{i<j<k}n_i n_j n_k,&m\ge3.
\end{cases}
\]
The dimension formula itself is prior work; the contribution here is the all-set structural characterization together with the profile, multivariate, univariate, total-count, and minimum-set enumerations.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. The complete multipartite graph has at least two nonempty parts. A set \(S\subseteq V(G)\) is a distance-equalizer set when, for every pair of distinct vertices \(x,y\in V(G)\setminus S\), some \(w\in S\) satisfies \(d(w,x)=d(w,y)\). The result concerns this standard definition introduced by González, Hernando, and Mora.

The classification includes complete graphs, stars, complete bipartite graphs, balanced and unbalanced multipartite graphs, and parts of size one. No probabilistic, asymptotic, or generic-position assumptions are used.

## Proof
For distinct vertices of a complete multipartite graph, the distance is one when they lie in different parts and two when they lie in the same part.

First consider two outside vertices \(x,y\in V(G)\setminus S\) lying in the same part \(A_i\). Every selected vertex \(w\in S\) is equidistant from them: if \(w\in A_i\), then \(d(w,x)=d(w,y)=2\), and if \(w\notin A_i\), then \(d(w,x)=d(w,y)=1\). Thus same-part pairs never create an obstruction once \(S\) is nonempty; the only essential pairs lie in different parts.

Now let \(x\in A_i\setminus S\) and \(y\in A_j\setminus S\) with \(i\ne j\). A selected vertex \(w\) is equidistant from \(x\) and \(y\) exactly when \(w\) lies in a third part. Indeed, a vertex of \(A_i\) has distance two to \(x\) and one to \(y\), a vertex of \(A_j\) has distances one and two, while a vertex of any \(A_k\) with \(k\notin\{i,j\}\) has distance one to both.

Suppose first that some part \(A_k\) is contained in \(S\). No outside vertex lies in \(A_k\). Every cross-part outside pair therefore uses two parts different from \(A_k\), and any \(w\in A_k\) equalizes the pair. Hence \(S\) is a distance-equalizer set.

Suppose next that no part is contained in \(S\). Then every part contains an outside vertex. If \(S\) meets at least three parts, every pair of distinct part indices \(i,j\) has a selected vertex in a third supported part, so every cross-part outside pair is equalized. Conversely, if \(S\) meets at most two parts, choose outside vertices in those two supported parts when two are supported, or in the unique supported part and any other part when one is supported; when no part is supported, choose any cross-part pair. Because no selected vertex lies in a third part, the chosen pair has no equalizer in \(S\). Therefore \(S\) is not a distance-equalizer set. This proves the characterization.

For the enumerator, an invalid set has no fully selected part and has support size zero, one, or two. The polynomial \(B_i(x_i)\) enumerates the nonempty proper subsets of \(A_i\). The invalid sets therefore have multivariate enumerator
\[
1+\sum_i B_i(x_i)+\sum_{i<j}B_i(x_i)B_j(x_j).
\]
Subtracting this from the enumerator \(\prod_i(1+x_i)^{n_i}\) of all subsets gives \(\mathcal E_G\); the univariate and total-count formulas follow by specialization.

For minimum sets, when \(r=2\) the second characterization alternative is impossible, so a distance-equalizer set must contain an entire part. When \(r\ge3\), the least possible size is \(\min\{\min_i n_i,3\}\). The structural characterization then gives the stated basis classifications and counts directly.

## Verification
A standalone exact checker constructs the distance matrix of each complete multipartite graph and tests the definition independently of the structural criterion. It exhaustively covers all 58 complete multipartite isomorphism types of orders two through eight. Across these graphs it checks 8084 vertex subsets against the classification, compares 58 full size-distribution coefficient vectors against the displayed polynomial, and checks 58 minimum-size/minimum-count predictions. The included output terminates with `VERIFY_OK`.

These computations corroborate the proof and its edge cases; they are not a substitute for the argument above and do not constitute an independent audit or formal proof-assistant verification.

## Relationship to prior work
González, Hernando, and Mora introduced distance-equalizer sets and the equidistant dimension. Their complete-multipartite result gives the minimum cardinality: for complete bipartite graphs the smaller part size, and for complete multipartite graphs with at least three parts the minimum of three and the smallest part size. The present result recovers that formula but does not claim it as new.

The later work of Gispert-Fernández and Rodríguez-Velázquez studies computational complexity and lexicographic products. Current literature searches also covered later equidistant-dimension papers on other graph families and graph products. No checked source supplied the all-distance-equalizer-set criterion above, the corresponding multivariate or univariate enumerator, or the complete count of minimum sets for arbitrary complete multipartite graphs. The originality claim is therefore restricted to those structural and enumerative refinements, on a best-of-knowledge basis.

## Limitations
The originality assessment is literature-based rather than a formal proof of nonexistence of prior publication. A semantically equivalent characterization could appear under different terminology or inside a source not indexed by the checked databases. The result is specific to complete multipartite graphs and does not by itself extend to arbitrary diameter-two graphs, multipartite graphs with edges deleted, or graph products.

The finite checker covers all complete multipartite isomorphism types only through order eight. Its purpose is to test the proof against small edge cases and coefficient identities; the theorem for arbitrary order rests on the exact distance argument.

## References
1. A. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs*, arXiv:2107.10805v1, first public version 2021-07-22; later published in *Bulletin of the Malaysian Mathematical Sciences Society* 45 (2022), 1757–1775, DOI 10.1007/s40840-022-01295-z.
2. A. Gispert-Fernández, J. A. Rodríguez-Velázquez, *The equidistant dimension of graphs: NP-completeness and the case of lexicographic product graphs*, *AIMS Mathematics* 9 (2024), 15325–15345, DOI 10.3934/math.2024744.
