# Optimal edge-locating colorings of crown graphs from two-hole Latin rectangles

## Finding
For every integer \(n\ge6\), the crown graph \(\operatorname{Cr}_n=K_{n,n}-M_n\), with vertex classes \(\{x_0,\ldots,x_{n-1}\}\) and \(\{y_0,\ldots,y_{n-1}\}\) and edges \(x_i y_j\) precisely when \(i\ne j\), has edge-locating chromatic number
\[
\boxed{\chi'_L(\operatorname{Cr}_n)=n+1.}
\]
The proof gives an explicit optimal proper edge coloring using only modular addition and, in one congruence class, two transpositions. By comparison, the known result for the undeleted balanced biclique is \(\chi'_L(K_{n,n})=n+2\) [1, Theorem 2.4]. Thus deletion of a perfect matching saves one edge-locating color throughout the stated infinite family.

## Assumptions and scope
All graphs are finite, simple and connected; \(n\ge6\). A proper \(k\)-edge coloring partitions the edges into \(k\) nonempty matchings \(C_0,\ldots,C_{k-1}\). Define \(d(v,C)=\min\{d(v,a),d(v,b):ab\in C\}\). The code of \(v\) is \((d(v,C_0),\ldots,d(v,C_{k-1}))\). A coloring is *edge-locating* when all vertex codes are different. The minimum possible \(k\) is \(\chi'_L\). The deleted matching is \(\{x_i y_i:0\le i<n\}\), and all modular residues below use representatives in \(\{0,\ldots,m-1\}\).

## Proof
**1. Universal lower bound.** Every vertex of \(\operatorname{Cr}_n\) has degree \(n-1\). A proper coloring with \(n-1\) colors makes every vertex incident with all colors, so it is not edge-locating. Suppose there are \(n\) nonempty colors. Every vertex is then incident to \(n-1\) different colors and misses exactly one. Every color class is a matching of at most \(n\) edges; since the graph has \(n(n-1)\) edges, the total deficiency \(\sum_c(n-|C_c|)\) equals \(n\). Therefore at most one color class can be a singleton, because two singleton classes would contribute \(2(n-1)>n\).

For any matching of at least two edges, a vertex not incident with that matching has distance exactly one from it: of its at least two opposite-side endpoints, at most one is the vertex's deleted-match nonneighbor. For a singleton \(\{x_a y_b\}\), the only vertices possibly at distance two rather than one are \(x_b\) and \(y_a\); its endpoints have distance zero. Thus apart from at most two exceptional vertices, the distance code of every vertex is determined by its one missing color, yielding at most \(n\) different codes among at least \(2n-2>n\) vertices. This is impossible. Therefore \(\chi'_L(\operatorname{Cr}_n)\ge n+1\), in fact for every \(n\ge3\).

**2. The coloring and its two-hole signatures.** Put \(m=n+1\). Choose a permutation \(\sigma\) of \(\{0,\ldots,n-1\}\), and color the edge \(x_i y_j\), \(i\ne j\), by
\[
\operatorname{col}(x_i y_j)\equiv i+\sigma(j)\pmod m.
\]
Every row and column has pairwise different entries, so the coloring is proper. When the deleted diagonal is temporarily restored, row \(i\) misses only color \(i-1\pmod m\), and column \(j\) misses only color \(\sigma(j)-1\pmod m\). Deleting its diagonal entry \(i+\sigma(i)\) gives exactly the two missing-color sets
\[
R_i=\{i-1,i+\sigma(i)\}\pmod m,\qquad
Q_i=\{\sigma(i)-1,i+\sigma(i)\}\pmod m.
\]
If all \(2n\) sets \(R_i,Q_i\) are different and each has size two, the coloring is edge-locating: vertices with different missing incident-color sets necessarily have different zero coordinates in their distance codes. Every color is used, since if one color were unused it would lie in all \(2n\) distinct missing pairs, but there are only \(m-1=n\) two-element pairs containing any given color.

For \(n=6,7,8\), use respectively these zero-indexed sequences \((\sigma(0),\ldots,\sigma(n-1))\):
\[
\begin{array}{c|l}
6&(1,2,3,5,0,4)\\
7&(1,2,4,5,3,6,0)\\
8&(4,3,5,6,7,0,1,2).
\end{array}
\]
Substitution in the two displayed formulas gives respectively \(12,14,16\) distinct two-element sets. The complete list and a graph-distance cross-check are independently reproducible using `verify.py`.

For every \(n\ge9\), initially put \(\sigma(i)=(i+3)\bmod n\). When \(n\equiv2\pmod3\), write \(n=3k+2\) (so \(k\ge3\)) and interchange the two values at positions \(k-3,k-2\), and then those at positions \(k-1,k\). In the other two congruence classes make no change. These are permutations.

**3. Arithmetic verification for all \(n\ge9\).** Let \(m=n+1\). For the unmodified three-step shift, call indices \(0\le i\le n-4=m-5\) *bulk*. For them the missing-color edges, written as unordered pairs of residues, are
\[
R_i=\{i-1,2i+3\},\qquad Q_i=\{i+2,2i+3\}\pmod m.
\]
For the three terminal indices \(n-3,n-2,n-1\), the six edges are, respectively,
\[
\begin{array}{c|ccc}
&n-3&n-2&n-1\\
R&\{m-5,m-4\}&\{m-4,m-2\}&\{m-3,0\}\\
Q&\{m-1,m-4\}&\{0,m-2\}&\{1,0\}.
\end{array}
\]
They are distinct for \(m\ge10\). None equals a bulk pair: the bulk first entry lies in \(\{m-1,0,\ldots,m-6\}\) for \(R\), or \(\{2,\ldots,m-3\}\) for \(Q\); testing the allowed endpoint of each of the six displayed terminal pairs against the bulk second entry \(2i+3\) gives a nonzero residue (only the excluded moduli at most eight could yield equality). Bulk pairs themselves have two different entries, since equality would force \(i=m-4\) for \(R\), or \(i=m-1\) for \(Q\), both outside the bulk range.

For distinct bulk pairs, equality of unordered pairs admits the following complete congruence test. In the same-type comparisons equality requires exchanging the two entries; in the cross-type comparison the same-order alternative would force \(m\mid6\), impossible here:
\[
\begin{array}{c|c|c}
\text{comparison}&\text{necessary congruence for the second index }j&\text{collisions if }m=3k+3\\
R_i=R_j&3(j+4)\equiv0\pmod m&(i,j)=(2k-2,k-3)\text{ or reversed}\\
Q_i=Q_j&3(j+1)\equiv0\pmod m&(i,j)=(2k+1,k)\text{ or reversed}\\
R_i=Q_j&3(j+3)\equiv0\pmod m&(i,j)=(2k,k-2),(k-1,2k-1).
\end{array}
\]
For example, \(R_i=R_j\) with exchanged entries gives \(i\equiv2j+4\) and \(2i\equiv j-4\), hence \(3(j+4)\equiv0\pmod m\). The other two rows follow identically by substitution. Because \(0\le j\le m-5\), all three congruences have no solutions when \(3\nmid m\). When \(m=3k+3\), exactly the four unordered collisions listed in the table occur. All eight affected signatures involve a position in \(\{k-3,k-2,k-1,k\}\).

In this last case, the prescribed swaps replace the eight signatures at those four positions by
\[
\begin{array}{c|cc}
\text{index}&R&Q\\
k-3&\{k-4,2k-2\}&\{k,2k-2\}\\
k-2&\{k-3,2k-2\}&\{k-1,2k-2\}\\
k-1&\{k-2,2k+2\}&\{k+2,2k+2\}\\
k&\{k-1,2k+2\}&\{k+1,2k+2\}.
\end{array}
\]
The eight new edges are pairwise distinct: within each four-edge group their first entries are distinct; across the two groups the shared second entries are different and could only make an equality by exchanging both endpoints, whereas \(2k+2\) is not a first entry in the first group (also directly when \(k=3\)). They do not collide with unchanged bulk signatures. Indeed, for a candidate edge \(\{u,v\}\) to be an unmodified bulk \(R\) or \(Q\), at least one of
\[
v-2u-5,\quad u-2v-5,\quad v-2u+1,\quad u-2v+1
\]
must vanish modulo \(3k+3\). For the eight rows of the preceding table, the respective residues (writing negative representatives for clarity) are
\[
\begin{array}{c|rrrr}
R_{k-3}&1&-2&7&4\\ Q_{k-3}&-7&2&-1&8\\
R_{k-2}&-1&-1&5&5\\ Q_{k-2}&-5&1&1&7\\
R_{k-1}&1&-8&7&-2\\ Q_{k-1}&-7&-4&-1&2\\
R_k&-1&-7&5&-1\\ Q_k&-5&-5&1&1.
\end{array}
\]
All are nonzero modulo \(3k+3\ge12\). Finally no new edge equals a terminal edge: for \(k\ge5\), the terminal-pair endpoints outside \(\{0,1\}\) are at least \(3k-2\), while every new second entry is at most \(2k+2<3k-2\) and every nonnegative new first entry is at most \(k+2\); the terminal pair \(\{0,1\}\) is also excluded. Cases \(k=3,4\) follow by direct substitution in the six terminal pairs; in the \(k=3\) case the exceptional entry \(k-4=-1\) is reduced modulo \(m\). Thus all \(2n\) missing-color edges are distinct after the swaps, including the modulus divisible by three.

Together with the lower bound, this proves \(\chi'_L(\operatorname{Cr}_n)=n+1\) for every \(n\ge6\). \(\square\)

## Verification
`verify.py` first checks all stated permutations and verifies pairwise distinction of the two-hole signatures for every integer \(6\le n\le5000\). It then independently builds the original crown graphs, computes shortest-path distances to the actual colored edge classes, verifies properness, and verifies all \(2n\) distance codes are different for \(6\le n\le13\). These finite tests support, but do not replace, the modular arithmetic proof of the infinite result. The script has no external dependencies.

## Relationship to prior work
Korivand, Mojdeh, Baskoro and Erfanian [1] introduced edge-locating coloring, proved its basic properties and established \(\chi'_L(K_{n,n})=n+2\) (Theorem 2.4). Their Section 3 treats deleting matchings from *complete graphs* \(K_n\), not from complete bipartite graphs. Their full publicly accessible preprint was inspected in Sections 1–3, 6–7; its theorems do not state the crown-graph result. The new proof uses a two-hole Latin-rectangle construction and a separate sharp lower-bound argument for the deleted-matching bipartite graphs. General edge-coloring and distinguishing-coloring results, and edge-metric bases of crown graphs, concern different constraints and do not imply this distance-to-color-class minimum.

## Limitations
The theorem is not claimed for \(n=4,5\), and does not enumerate all optimal colorings. The lower bound alone holds from \(n=3\). No claim of exhaustive priority over unpublished or unindexed literature is made. The graph-distance computations cover finite orders only; the unbounded statement relies on the explicit arithmetic case analysis.

## References
[1] M. Korivand, D. A. Mojdeh, E. T. Baskoro, A. Erfanian, *Edge-Locating Coloring of Graphs*, arXiv:2310.05609v1, first publicly submitted 2023-10-09, Sections 1–3 and Theorem 2.4, https://arxiv.org/html/2310.05609v1 ; subsequently *Electronic Journal of Graph Theory and Applications* 12(1) (2024), 55–73, DOI:10.5614/EJGTA.2024.12.1.6.
