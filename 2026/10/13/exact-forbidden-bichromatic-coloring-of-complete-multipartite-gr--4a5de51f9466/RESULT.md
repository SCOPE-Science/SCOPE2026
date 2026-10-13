# Exact forbidden-bichromatic coloring of complete multipartite graphs
## Finding
Let \(H\) be a finite connected bipartite graph with at least two edges. Write the sizes of its two bipartition classes as \(1\le s\le t\). For every finite connected complete multipartite graph
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge2,\qquad n_i\ge1,
\]
the exact \((2,H)\)-avoiding chromatic number depends only on \(s\) and \(t\), not on the internal edge structure of \(H\).

If \(s=1\), then
\[
\chi_{2,H}(G)=\sum_{i=1}^r\left\lceil\frac{n_i}{t-1}\right\rceil.
\]
If \(s\ge2\), then
\[
\chi_{2,H}(G)=\min\left\{
\sum_{i=1}^r\left\lceil\frac{n_i}{t-1}\right\rceil,
\;\min_{1\le j\le r}\left(1+\sum_{i\ne j}\left\lceil\frac{n_i}{s-1}\right\rceil\right)
\right\}.
\]

## Assumptions and scope
A \((2,H)\)-avoiding coloring is a proper vertex coloring with no copy of \(H\) whose vertices use exactly two colors. Copies are ordinary subgraphs, not required to be induced. Connectedness of \(H\) makes its bipartition unique up to swapping, so \(s\) and \(t\) are well defined. The hypothesis that \(H\) has at least two edges implies \(t\ge2\), so every denominator above is positive. The host is a connected complete multipartite graph, hence has at least two nonempty parts.

## Proof
In any proper coloring of a complete multipartite graph, a color can occur in only one multipartite part: vertices in distinct parts are adjacent. For part \(V_i\), let \(M_i\) be the largest color-class size occurring inside \(V_i\).

Take two colors that occur in distinct parts \(V_i\) and \(V_j\), with color-class sizes \(a\) and \(b\). Every vertex of the first class is adjacent to every vertex of the second, so the two classes induce \(K_{a,b}\). Since \(H\) is connected and bipartite with shore sizes \(s\) and \(t\), it is a subgraph of \(K_{a,b}\) exactly when
\[
(a\ge s\text{ and }b\ge t)\quad\text{or}\quad(a\ge t\text{ and }b\ge s).
\]
Therefore a proper coloring is \((2,H)\)-avoiding exactly when, for all distinct \(i,j\),
\[
\neg(M_i\ge s\text{ and }M_j\ge t)\quad\text{and}\quad
\neg(M_i\ge t\text{ and }M_j\ge s).
\]

This pairwise condition has only two possible regimes. If no \(M_i\) reaches \(t\), then every color class in every part has size at most \(t-1\). Part \(V_i\) consequently needs at least \(\lceil n_i/(t-1)\rceil\) colors, and partitioning each part into blocks of size at most \(t-1\) attains the sum of these lower bounds.

Otherwise some part \(V_j\) has \(M_j\ge t\). Then the pairwise condition forces \(M_i\le s-1\) for every \(i\ne j\). If \(s=1\), this is impossible because all other parts are nonempty, so only the first regime exists. If \(s\ge2\), each nonexceptional part \(V_i\) needs at least \(\lceil n_i/(s-1)\rceil\) colors. The exceptional part needs at least one color, and making all of \(V_j\) monochromatic attains this lower bound without violating the condition. Thus the best coloring in this regime uses
\[
1+\sum_{i\ne j}\left\lceil\frac{n_i}{s-1}\right\rceil
\]
colors. Minimizing over the two regimes and over the exceptional part proves the formula.

## Verification
A standalone checker enumerates all integer partitions of every multipartite part, interprets each partition as the multiset of color-class sizes in that part, and independently tests the pairwise forbidden-copy condition. It compares the brute-force optimum against the displayed formula for every nondecreasing part-size vector with \(2\le r\le4\), \(1\le n_i\le5\), and every \(1\le s\le t\le4\) with \(t\ge2\). All \(1080\) parameter cases agree.

The finite computation is a stress test only; the proof above establishes the formula for all permitted parameters.

## Relationship to prior work
Lu, Ying, and Song introduced the recent \((2,\mathcal F)\)-avoiding formulation and proved asymptotic bounds under bipartite exclusions. Their results motivate asking for exact behavior on canonical host classes. Earlier work of Aravind and Subramanian developed the broader forbidden-subgraph-coloring framework and maximum-degree bounds. Neither inspected source gives the exact complete-multipartite formula above.

When \(s=1\), the connected bipartite graph \(H\) is the star \(K_{1,t}\), and the formula becomes the proper \((t-1)\)-frugal chromatic number of a complete multipartite graph. That specialization is already represented in prior frugal-coloring literature, including Bard's work on multipartite graphs. The contribution here is the structural collapse for every connected bipartite \(H\): on complete multipartite hosts, the entire \((2,H)\)-avoiding problem is governed solely by the two bipartition sizes, with the stated two-regime exact formula. As further familiar specializations, \(H=P_3\) gives \(\chi_{2,H}(G)=|V(G)|\), while \(H=P_4\) gives \(\chi_{2,H}(G)=|V(G)|-\max_i n_i+1\).

## Limitations
The theorem is restricted to connected bipartite forbidden graphs and complete multipartite hosts. It does not address disconnected forbidden graphs, for which a bichromatic copy need not align with one global bipartition, or host graphs missing cross-part edges. Literature searches cannot prove global uniqueness; short structural statements of this type can occur under alternate terminology. Known frugal and star-coloring special cases are not claimed as new.

## References
1. Z. Lu, Q. Ying, and H. Song, “\((2,\mathcal F)\)-Avoiding Coloring and B-Coloring under Bipartite Exclusions,” arXiv:2609.39716v1, first public 2026-09-30.
2. N. R. Aravind and C. R. Subramanian, “Forbidden Subgraph Colorings and the Oriented Chromatic Number,” IWOCA 2009, pp. 60–71, doi:10.1007/978-3-642-10217-2_9.
3. S. Bard, “Complexity of frugal homomorphisms,” PhD thesis, University of Victoria, 2021, hdl:1828/13618.
