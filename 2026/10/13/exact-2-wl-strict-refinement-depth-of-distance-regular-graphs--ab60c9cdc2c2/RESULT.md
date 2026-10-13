# Exact 2-WL strict-refinement depth of distance-regular graphs
## Finding
Let \(G\) be a finite connected distance-regular graph of diameter \(D\). Start ordered-pair 2-dimensional Weisfeiler--Leman refinement with the atomic coloring that distinguishes equality, adjacency, and nonadjacency. Write \(\rho_2(G)\) for the number of refinement rounds in which the partition of ordered pairs strictly changes before it first becomes stable. Then

\[
\rho_2(G)=
\begin{cases}
0,&D\le 2,\\
\lceil\log_2(D-1)\rceil,&D\ge 3.
\end{cases}
\]

More precisely, after \(r\) strict rounds, as long as the coloring has not yet stabilized, its color classes are exactly the graph-distance classes \(0,1,\ldots,2^r\) and one additional class containing all distances greater than \(2^r\). Thus the terminal 2-WL coloring is exactly the distance partition.

For the Hamming graph \(H(d,q)\), whose diameter is \(d\), this gives \(\rho_2(H(d,q))=0\) for \(d\le2\) and \(\rho_2(H(d,q))=\lceil\log_2(d-1)\rceil\) for \(d\ge3\). For fixed \(q\), the depth is therefore \(\Theta(\log d)=\Theta(\log\log |V(H(d,q))|)\).

## Assumptions and scope
A finite connected graph is distance-regular here in the standard intersection-number sense: for vertices \(x,y\) with \(d(x,y)=k\), the number of vertices \(z\) satisfying \(d(x,z)=i\) and \(d(z,y)=j\) depends only on \(i,j,k\), not on the particular pair \(x,y\). The 2-WL update is the standard ordered-pair rule

\[
c_{r+1}(x,y)=\operatorname{Hash}\!\left(c_r(x,y),\;\multiset_{z\in V(G)}(c_r(x,z),c_r(z,y))\right).
\]

The theorem counts only rounds that strictly refine the pair partition. Conventions that count the final no-change comparison add one to this quantity. No claim is made for arbitrary regular graphs or for disconnected graphs.

## Proof
For an integer \(m\ge1\), let \(P_m\) denote the partition of ordered pairs in which distances \(0,1,\ldots,m\) are individual classes and all distances greater than \(m\) form one final class \(F\). The atomic coloring is \(P_1\).

First, every color produced by 2-WL is a function of graph distance. This follows inductively from distance-regularity: if the old colors depend only on distances, then every multiplicity in the new 2-WL signature is a sum of intersection numbers \(p^k_{ij}\), hence depends only on \(k=d(x,y)\). Thus no two ordered pairs at the same distance are ever separated.

Now suppose the current partition is \(P_m\) and it is not yet stable. Consider a pair \(x,y\) at distance \(k\).

If \(m<k\le2m\), a shortest \(x\)-to-\(y\) path contains a vertex \(z\) with \(d(x,z)=i\le m\), \(d(z,y)=j\le m\), and \(i+j=k\). Conversely, triangle inequality forces \(i+j\ge k\) whenever such a vertex exists. Hence the minimum value of \(i+j\) among singleton-color pairs \((i,j)\) occurring in the 2-WL multiset is exactly \(k\). Therefore each distance \(k=m+1,\ldots,2m\) receives its own new color.

If \(k>2m\), no vertex can lie within distance \(m\) of both \(x\) and \(y\). For each fixed \(i\le m\), every vertex at distance \(i\) from \(x\) is consequently in the far class relative to \(y\); its multiplicity is the sphere size at radius \(i\), which is constant in a distance-regular graph. The analogous statement holds with \(x,y\) reversed, and the remaining \((F,F)\) multiplicity is determined by the total order and those sphere sizes. Hence all distances greater than \(2m\) have the same new signature.

Old singleton distance classes remain distinct because refinement retains the old color. Consequently one strict refinement sends \(P_m\) to \(P_{2m}\), with the evident truncation at diameter \(D\). Starting from \(m=1\), after \(r\) strict rounds the threshold is \(m=2^r\).

The partition is stable exactly when its far class contains at most one distance, that is, when \(D\le 2^r+1\). For \(D\le2\) this already holds at \(r=0\). For \(D\ge3\), the least such \(r\) is \(\lceil\log_2(D-1)\rceil\). At that point every distance is individually colored, and distance-regularity shows that another refinement cannot split any distance class. This proves both the formula and the terminal distance-scheme statement.

## Verification
A standalone exact checker accompanies this result. It implements ordered-pair 2-WL directly, computes all-pairs graph distances, verifies the distance-regular intersection-number condition for each test graph, and checks both the round formula and equality of terminal colors with distance classes. The tested suite contains \(26\) graphs: cycles \(C_3\) through \(C_{14}\), balanced complete bipartite graphs \(K_{a,a}\) for \(2\le a\le5\), hypercubes \(Q_d\) for \(1\le d\le5\), the Petersen graph, and Johnson graphs \(J(n,2)\) for \(4\le n\le7\). The checker returns `VERIFY_OK graphs=26 max_vertices=32 families=cycles,balanced_complete_bipartite,hypercubes,Petersen,Johnson`.

The computation is supplementary; the proof above is uniform for every finite connected distance-regular graph.

## Relationship to prior work
The logical-complexity survey arXiv:1003.4865 gives the standard multidimensional Weisfeiler--Leman refinement framework and stabilization parameters, but does not state this distance-regular exact round law. Recent work on Cartesian products and coherent configurations (arXiv:2411.02689) identifies the stable coherent configuration of a Hamming graph with its Hamming scheme, which is consistent with the terminal-distance conclusion here; its inspected Hamming-graph discussion does not provide the exact number of strict refinement rounds.

A previously established cycle-specific formula is a special case of the present diameter theorem because cycles are distance-regular. The incremental content here is the uniform transition law \(P_m\mapsto P_{2m}\) for every finite connected distance-regular graph, and hence the exact depth as a function only of diameter.

## Limitations
The result concerns standard ordered-pair 2-WL with the stated atomic initial coloring and the strict-refinement counting convention. It does not assert an analogous diameter-only formula for higher-dimensional WL, arbitrary association schemes, arbitrary regular graphs, or disconnected unions. The originality search did not reveal an indexed source stating the exact distance-regular round formula, but an unindexed textbook exercise or coherent-configuration folklore statement remains a residual priority risk.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 25 March 2010.
2. J.-Y. Cai, H. Guo, A. L. Gavrilyuk, and I. Ponomarenko, *Cartesian products of graphs and their coherent configurations*, arXiv:2411.02689, first posted 5 November 2024.
