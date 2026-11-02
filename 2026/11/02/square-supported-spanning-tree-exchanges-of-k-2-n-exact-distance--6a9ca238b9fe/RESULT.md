# Square-supported spanning-tree exchanges of \(K_{2,n}\): exact distances and Laplacian spectrum

## Finding
For every integer \(n\ge2\), consider the graph \(\mathcal R_n\) whose vertices are the spanning trees of the complete bipartite graph \(K_{2,n}\). Two trees are adjacent when one can be obtained from the other by replacing exactly one edge and the unique fundamental cycle of the inserted edge in the first tree has length four. This is **one-edge exchange restricted to a square**, not a simultaneous two-edge switch.

The reconfiguration graph has \(n2^{n-1}\) vertices, is regular of degree \(3(n-1)\), and has \(3n(n-1)2^{n-2}\) edges. Encode a tree by a word \(w\in\{0,1,*\}^n\) having exactly one wildcard: the wildcard identifies the unique vertex of degree two on the \(n\)-vertex side; the other coordinates specify which of the two left vertices is incident to the corresponding tree edge. If the wildcard coordinates of \(u,v\) are \(j,k\), respectively, then the exact distance is
\[
 d_{\mathcal R_n}(u,v)=\mathbf 1_{j\ne k}+\#\{i\notin\{j,k\}:u_i\ne v_i\}.
\]
In particular every vertex has eccentricity \(n-1\). For every \(0\le d\le n-1\), the distance-\(d\) sphere around any vertex has size
\[
 \binom{n-1}{d}+2(n-1)\binom{n-2}{d-1},
\]
where a binomial coefficient with an inadmissible lower index is zero. The Wiener index (sum of distances over unordered distinct pairs) is
\[
 W(\mathcal R_n)=n(n^2-1)2^{2n-4}.
\]
The complete combinatorial Laplacian spectrum, with multiplicities understood additively if numerical eigenvalues coincide, is
\[
 \begin{array}{ll}
 4r & \text{with multiplicity }\binom nr,\quad 0\le r\le n-1,\\
 2(n+r)&\text{with multiplicity }(n-r-1)\binom nr,\quad 0\le r\le n-2.
 \end{array}
\]
Consequently the spectral gap equals \(4\), independently of \(n\), and the exact spanning-tree count of the connected reconfiguration graph is
\[
 \tau(\mathcal R_n)=\frac1{n2^{n-1}}
 \prod_{r=1}^{n-1}(4r)^{\binom nr}
 \prod_{r=0}^{n-2}\bigl(2(n+r)\bigr)^{(n-r-1)\binom nr}.
\]

## Assumptions and scope
The two vertices on one side of \(K_{2,n}\) are distinguished as \(a,b\), and the other side is indexed by \(1,\ldots,n\). A spanning tree is a connected acyclic spanning subgraph. If \(e\) is an edge outside a tree \(T\), its fundamental cycle is the unique cycle of \(T+e\). An allowed move is \(T\mapsto T+e-f\) for an edge \(f\) on that fundamental cycle, only when that cycle is a four-cycle. Edges outside these moves do not appear in \(\mathcal R_n\). All statements hold for every integer \(n\ge2\), without limits on the permitted number of moves. The eigenvalues concern the unnormalized combinatorial Laplacian \(L=D-A\), not the random-walk or normalized Laplacian.

## Proof
Every tree must contain a unique right-side vertex adjacent to both \(a\) and \(b\): existence follows because their unique connecting path has length two in \(K_{2,n}\), and uniqueness follows because two such vertices would create a four-cycle. The other right-side vertices have exactly one incident tree edge, proving the wildcard encoding and the count \(n2^{n-1}\). The encoding and this count are known from Shier (2000), not asserted as new.

Fix a tree word with wildcard at \(j\). For every \(k\ne j\), the four edges incident to \(a,b\) and the two right-side vertices \(j,k\) form a square; exactly three are in the tree. Inserting the missing edge creates this square as the fundamental cycle, and each of the other three edges may be removed. One choice leaves the wildcard at \(j\) and flips bit \(k\). Two choices move the wildcard from \(j\) to \(k\), setting the newly fixed bit at \(j\) to either value; all other bits remain unchanged. Conversely every admissible exchange has this form. Thus every vertex has exactly \(3(n-1)\) neighbors, giving the edge count.

Let \(u,v\) have wildcard positions \(j,k\). If \(j=k\), individually flip each differing fixed bit, using exactly the stated distance. If \(j\ne k\), move the wildcard directly from \(j\) to \(k\), choosing the newly fixed bit \(j\) to equal the target bit, then individually flip the differing bits outside \(\{j,k\}\). This realizes the formula. For the lower bound fix target \(v\) and call the displayed right-hand side \(\delta(w)\). A bit-flip move changes \(\delta\) by at most one. Under a wildcard move \(j\to k\), if the target wildcard is neither \(j\) nor \(k\), the wildcard indicator remains one and at most one mismatching coordinate is exchanged in the mismatch count; if the target wildcard equals \(j\) or \(k\), the wildcard indicator changes by one while exactly one mismatch term is removed or introduced. In all cases \(|\delta(w')-\delta(w)|\le1\). Since \(\delta(v)=0\), no shorter path is possible.

With the wildcard fixed, there are \(\binom{n-1}{d}\) configurations at distance \(d\). For each of the \(n-1\) different target wildcard positions, the previously wildcard coordinate has two choices and exactly \(d-1\) of the remaining \(n-2\) fixed bits differ, giving \(2(n-1)\binom{n-2}{d-1}\). Hence the sphere formula. Its highest nonempty level is \(n-1\). The total distance from a vertex is \((n^2-1)2^{n-2}\), by summing the two binomial first moments. Multiplying by \(n2^{n-1}/2\) proves the Wiener formula.

For the spectrum, fix a subset \(S\subseteq\{1,\ldots,n\}\) of size \(r\le n-1\). For each wildcard position \(j\notin S\), define the character \(\chi_{S,j}(w)=(-1)^{\sum_{i\in S}w_i}\) on words with wildcard \(j\), and zero on all other words. All these characters, over all \(S\) and \(j\notin S\), form an orthogonal basis, by the Walsh character basis on each Boolean slice. Holding \(S\) fixed gives an invariant subspace of dimension \(n-r\). The same-wildcard bit flips contribute the scalar \(n-1-2r\) to each basis vector; cross-wildcard moves contribute \(2\) from each of the other \(n-r-1\) wildcard positions. Thus the adjacency operator on this subspace is represented by
\[
 (n-3-2r)I_{n-r}+2J_{n-r}.
\]
Its eigenvalues are \(3(n-1)-4r\) once and \(n-3-2r\) with multiplicity \(n-r-1\). Subtracting from the degree \(3(n-1)\) yields exactly the claimed Laplacian spectrum. The total multiplicity equals \(\sum_{r=0}^{n-1}\binom nr(n-r)=n2^{n-1}\). Only the eigenvalue \(4r\) with \(r=0\) is zero. The least positive eigenvalue is \(4\) for every \(n\ge2\). Kirchhoff's matrix-tree theorem divides the product of the nonzero eigenvalues by the number of vertices and gives the displayed tree-complexity formula.

## Verification
The standalone Python checker `verify_primary.py` independently enumerates actual edge subsets of \(K_{2,n}\), tests spanning-tree connectivity and acyclicity, constructs square-supported one-edge exchanges, and exhaustively compares all-pairs distances and distance spheres for \(2\le n\le5\). It checks symbolic characteristic polynomials for \(2\le n\le4\) and determinant-based spanning-tree counts for \(n=2,3\). The independently implemented C++17 checker `verify_secondary.cpp` builds wildcard configurations and independently computes all-pairs graph distances and distance spheres for \(2\le n\le7\). Both passed from their delivered source files. These finite calculations corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
Shier (2000) explicitly identifies spanning trees of \(K_{2,n}\) with the one-wildcard binary words (equivalently hypercube edges) and counts them. Neither the encoding nor this count is claimed here. Maurer (1973) develops unrestricted matroid basis-exchange graphs: allowing all fundamental-cycle lengths gives a different graph. Bousquet and collaborators (2020) study spanning-tree reconfiguration under conditions on leaves; their elementary edge flips are not restricted to fundamental four-cycles, and their simultaneous square switches are not the one-edge move defined here. The result presented here is the exact restricted-exchange metric, complete distance enumeration, full Laplacian spectrum, and resulting graph complexity of this particular reconfiguration graph.

## Limitations
Only one-edge exchanges with a fundamental four-cycle are allowed. No claim is made for other underlying complete bipartite graphs, other cycle-length restrictions, or weighted transitions. Independently known hypercube-edge or 1-face graphs may admit equivalent descriptions; the accessible literature comparison did not establish exhaustive priority. The formulas are proved mathematically here, but no independent scholarly audit has been performed.

## References
1. D. R. Shier, “Spanning Trees: Let Me Count the Ways,” *Mathematics Magazine* **73**(5), December 2000, pp. 377–382. Relevant original exposition: https://www.scribd.com/document/522129195/Mathematics-Magazine-Vol-73-No-5-December-2000.
2. S. B. Maurer, “Matroid basis graphs. I,” *Journal of Combinatorial Theory, Series B* **14**(3), 1973, pp. 216–240. DOI: https://doi.org/10.1016/0095-8956(73)90005-1.
3. N. Bousquet and collaborators, “Reconfiguration of Spanning Trees with Many or Few Leaves,” first arXiv version 2020. https://arxiv.org/abs/2006.14309.
4. G. Kirchhoff, matrix-tree theorem, as used through the standard product formula for nonzero Laplacian eigenvalues.
