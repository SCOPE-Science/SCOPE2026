# Sharp corner-refinement depth and orbit partition for square king graphs

## Finding
Let \(n\ge3\) and let \(K_n=P_n\boxtimes P_n\) be the king graph of the square board \(\{0,\ldots,n-1\}^2\): distinct vertices \((i,j)\) and \((a,b)\) are adjacent exactly when \(\max(|i-a|,|j-b|)=1\). Initially give \((0,0)\) one distinguished color and every other vertex the same second color. In each synchronous counting-color-refinement round, the next color records the previous color and the multiset of previous colors of the neighbors.

**Theorem.** The stable classes are exactly \(O_{ij}=\{(i,j),(j,i)\}\), with \(0\le i\le j<n\). They are attained after **exactly \(n-1\) strict refinement rounds**. Thus there are precisely \(n(n+1)/2\) stable classes, of which \(n\) are singletons and \(n(n-1)/2\) have size two. In particular, the stable partition is the orbit partition of the automorphisms fixing the corner: the coordinate swap itself realizes each pair, while color refinement separates distinct pairs.

## Assumptions and scope
All graphs here are finite, undirected and simple. A strict refinement round means a synchronous update that strictly splits the prior partition. The initial distinguished color at the corner is retained because each new color includes its previous color. The theorem holds for all integers \(n\ge3\) and does not assert anything about rectangular boards or arbitrary marked vertices. At \(n=2\), the king graph is complete and its one-marked partition is already stable at round zero, so the asserted depth would be false.

## Proof
Write \(c_r(v)\) for the vertex color after \(r\) updates, and \(Q_r=\{(i,j):0\le i,j\le r\}\) for \(0\le r<n\). The coordinate-interchange map \(\sigma(i,j)=(j,i)\) fixes the marked corner and preserves king adjacency, hence every \(c_r\) is constant on \(O_{ij}\).

We prove by induction on \(r\) the stronger assertion that the orbits meeting \(Q_r\) have pairwise different colors at round \(r\), and that none of those colors occurs outside the same orbit anywhere on the board. For \(r=0\), the single marked vertex has its own color.

Suppose the assertion holds at \(r<n-1\), and put \(k=r+1\). Every new vertex in \(Q_k\setminus Q_r\) is adjacent to a vertex of \(Q_r\); every vertex outside \(Q_k\) has no neighbors in \(Q_r\). The color signature at round \(r+1\) therefore distinguishes all new-layer vertices from all vertices outside \(Q_k\), since each old orbit color appearing on \(Q_r\) is globally unique. It also retains the separate colors of the older orbits.

The new layer has exactly the orbit representatives \((i,k)\), \(i=0,\ldots,k\). Their neighbors inside \(Q_r\) are precisely \((a,r)\) for integers \(a\) in
\[
I_i=\{a:0\le a\le r,\ |a-i|\le1\}.
\]
For each \(a\le r\), the old color of \((a,r)\) uniquely identifies \(O_{a,r}\). Thus, whenever \(I_i\ne I_j\), counting neighbors of old colors distinguishes \((i,k)\) and \((j,k)\) at the next round. For \(r\ge2\) the sets \(I_0,\ldots,I_{r+1}\) are pairwise distinct: their left and right endpoints, clipped to \([0,r]\), form respectively the initial interval \(\{0,1\}\), the consecutive length-three intervals, the terminal length-two interval and the terminal singleton. Hence the induction holds for \(r\ge2\).

Two small induction steps require degree information. When \(r=0\), the vertices \((0,1)\) and \((1,1)\) both meet the marked root, but have degrees \(5\) and \(8\) for \(n\ge3\), respectively, and are distinguished at round one. When \(r=1\), the old-neighbor sets \(I_0\) and \(I_1\) are equal, while \(I_2\) is different. But \((0,2)\) is an edge or corner vertex of degree at most \(5\), whereas \((1,2)\) is an interior vertex of degree \(8\) if \(n>3\), and for \(n=3\) they have degrees \(3\) and \(5\), respectively. Their round-one colors already reflect this degree difference, so their round-two colors differ. The stronger induction follows for all \(r\le n-1\).

At round \(n-1\), \(Q_{n-1}\) is the whole board; thus every coordinate-swap orbit has a distinct color. Conversely no orbit could have split because \(\sigma\) is a corner-fixing automorphism. Every orbit partition of a graph automorphism group is equitable, and in this case the swap orbit partition is equitable directly because \(\sigma\) preserves neighbor counts. Hence no later round splits any class; the stable coloring is reached by round \(n-1\), and has the asserted class numbers.

For sharpness, consider \(x=(0,n-1)\) and \(y=(n-1,n-1)\). They have distinct coordinate-swap orbits, but both are at graph distance \(n-1\) from the individually colored corner. The uncolored square king graph has a coordinate reflection taking \(x\) to \(y\). For every \(r<n-1\), the rooted radius-\(r\) neighborhoods of \(x\) and \(y\) have identical initial color patterns (the sole exceptional initial color lies outside both), so their color-refinement signatures through round \(r\) are equal. In particular \(c_{n-2}(x)=c_{n-2}(y)\), whereas \(c_{n-1}(x)\ne c_{n-1}(y)\) by the induction. Stabilization therefore requires at least \(n-1\) strict rounds, proving equality.

## Verification
The standalone Python 3 program `verify_king.py` constructs king adjacencies from their coordinate definition, performs synchronous multiset color refinement, and verifies for each \(3\le n\le15\) that every orbit in \(Q_r\) has a globally unique color by round \(r\), that the final partition agrees exactly with coordinate-swap orbits, that the two outer corners remain indistinguishable through round \(n-2\), and that an additional round makes no further split. Run `python3 verify_king.py`. The captured output `verify_output.txt` includes the complete round-by-round class counts and reports `ALL_TESTS_PASS`. Computation corroborates, but does not replace, the all-\(n\) proof above.

## Relationship to prior work
The square king graph is the strong product of two path graphs, as recorded in Weisstein's *King Graph*. Kersting, Mladenov, Garnett and Grohe (2014) analyze the general color-refinement procedure. Arvind, Köbler, Rattan and Verbitsky (2015) develop general refinability and automorphism-orbit concepts; Kiefer and McKay (2020) study extremal stabilization iteration counts. Their inspected full texts do not state this square king-graph, single-corner orbit classification or exact depth. A related result for the **Cartesian** path-grid (without diagonal edges) has a different refinement-depth expression; adding diagonal adjacency changes the neighbor signatures, so that result does not logically imply the present theorem. This theorem is a special-purpose calculation and not a claim that all strong-product graphs are refinable or that arbitrary individualizations behave similarly.

## Limitations
The proof assumes \(n\ge3\) and marks exactly one corner. It does not address rectangular king boards or other marked configurations. Exhaustive finite tests through \(n=15\) do not establish publication priority, and specialized prior work on king grids or equitable partitions may exist beyond inspected sources. No independent validation or external certification is claimed.

## References
1. K. Kersting, M. Mladenov, R. Garnett and M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, DOI: 10.1609/aaai.v28i1.8992 (published 2014-06-21).
2. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public 2015-02-04).
3. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182 (first public 2020-05-20).
4. E. W. Weisstein, *King Graph*, MathWorld, https://mathworld.wolfram.com/KingGraph.html (webpage consulted for the strong-product identification; no reliable first-public date inferred).
