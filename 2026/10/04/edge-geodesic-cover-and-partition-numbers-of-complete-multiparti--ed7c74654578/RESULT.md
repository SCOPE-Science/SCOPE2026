# Edge-geodesic cover and partition numbers of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), all \(n_i\ge1\), and \(o=|\{i:n_i\text{ is odd}\}|\). Then \[\operatorname{gcover}_{e}(G)=\operatorname{gpart}_{e}(G)=\sum_{1\le i<j\le r}\left\lceil\frac{n_i n_j}{2}\right\rceil=\frac{|E(G)|+\binom{o}{2}}{2}.\] Moreover \(\operatorname{gp}_{e}(G)=|E(G)|\), and hence \(\operatorname{gp}_{e}(G)=2\operatorname{gcover}_{e}(G)\) holds exactly when \(o\le1\).

## Assumptions and scope
All graphs are finite, simple, and connected. An edge-geodesic cover is a family of geodesics whose edge sets cover \(E(G)\); its minimum cardinality is \(\operatorname{gcover}_e(G)\). An edge-geodesic partition is such a family in which every edge belongs to exactly one selected geodesic; its minimum cardinality is \(\operatorname{gpart}_e(G)\). An edge general-position set contains no three edges on a common geodesic.

Let \(G=K_{n_1,\ldots,n_r}\), where \(r\ge2\), every \(n_i\ge1\), and \(X_i\) is the part of size \(n_i\).

## Proof
Every geodesic of \(G\) has at most two edges. A two-edge geodesic has the form \(x-y-z\) with \(x,z\in X_i\) and \(y\in X_j\) for some \(i\ne j\). Thus both of its edges lie in the single complete bipartite block \(E(X_i,X_j)\), and no geodesic can cover edges from two different unordered pairs of parts.

The block \(E(X_i,X_j)\) has \(n_i n_j\) edges and one geodesic covers at most two of them, so every edge-geodesic cover requires at least
\[
\left\lceil\frac{n_i n_j}{2}\right\rceil
\]
geodesics for this block. Summing gives the corresponding lower bound.

It remains to partition \(K_{a,b}\) into \(\lceil ab/2\rceil\) geodesics. If \(b\) is even, pair the \(b\) incident edges at each vertex of the \(a\)-side. If \(b\) is odd and \(a\) is even, reverse the roles of the two sides. If both are odd, label the first side \(u_1,\ldots,u_a\), choose \(v_1\) on the second side, and for each \(u_s\) with \(s<a\) pair the \(b-1\) edges other than \(u_sv_1\). The \(a-1\) temporarily unpaired edges \(u_sv_1\) can be paired at \(v_1\). At \(u_a\), pair the \(b-1\) edges other than \(u_av_1\), leaving \(u_av_1\) as the unique one-edge geodesic. Hence every block has an optimal geodesic partition, and the block partitions combine to prove
\[
\operatorname{gcover}_e(G)=\operatorname{gpart}_e(G)
=\sum_{i<j}\left\lceil\frac{n_i n_j}{2}\right\rceil.
\]

The product \(n_i n_j\) is odd exactly when both part sizes are odd. There are \(\binom{o}{2}\) such pairs, so
\[
\sum_{i<j}\left\lceil\frac{n_i n_j}{2}\right\rceil
=\frac{|E(G)|+\binom{o}{2}}2.
\]

Finally, because no geodesic contains three edges, the whole edge set is in edge general position, so \(\operatorname{gp}_e(G)=|E(G)|\). The equality \(\operatorname{gp}_e(G)=2\operatorname{gcover}_e(G)\) therefore holds exactly when \(\binom{o}{2}=0\), equivalently \(o\le1\).

## Verification
The included checker independently constructs every complete multipartite graph represented by an integer partition of orders two through six. It enumerates all one- and two-edge geodesics from the graph definition, solves the minimum edge-geodesic cover and minimum edge-geodesic partition separately by exact bitmask dynamic programming, and compares both optima with the theorem. It also checks the parity form. The all-orders theorem is proved above.

## Relationship to prior work
Manuel, Prabha, and Klavžar introduced the edge \(k\)-general-position framework together with the edge-geodesic cover/partition dual inequalities. The full 2022 preprint develops exact results for torus graphs, hypercubes, and Beneš networks; searches within that text found no complete-bipartite or complete-multipartite result. Its conclusion likewise lists those network families. The later journal description names the same families.

A 2018 path-cover survey reports vertex isometric-path-cover results for complete bipartite and complete multipartite graphs. That is a different object: it covers vertices rather than edges. Targeted searches for the exact complete-bipartite specialization, complete-multipartite sum, parity correction, and edge-geodesic-partition aliases did not locate an equivalent statement.

## Limitations
The theorem is specific to complete multipartite graphs and uses the fact that every two-edge geodesic is confined to one bipartite block. The exhaustive computation is finite corroboration only. Search coverage cannot exclude differently phrased or non-indexed prior work. The final journal version of the motivating paper was compared through its public description in addition to full-text inspection of the arXiv version.

## References
1. P. Manuel, R. Prabha, S. Klavžar, “Generalization of edge general position problem,” arXiv:2207.07357v1, 15 July 2022; later published in The Art of Discrete and Applied Mathematics 8 (2025), DOI 10.26493/2590-9770.1745.5f4.
2. P. Manuel, “Revisiting path-type covering and partitioning problems,” arXiv:1807.10613v1, 25 July 2018.
