# The first rainbow-triangle deficit occurs at ten edges

## Finding

For an integer \(m\ge0\), let \(R(m)\) be the maximum number of triangles whose three edges have pairwise different colors in any finite simple graph having exactly \(m\) edges, each assigned one of three available colors. There is no bound on the vertex count; isolated vertices are irrelevant. Then the complete initial profile is
\[
\bigl(R(0),R(1),\ldots,R(11)\bigr)=(0,0,0,1,1,2,4,4,5,7,7,8).
\]
In particular, ten is the first edge budget at which the three-color rainbow-triangle extremum is strictly below the ordinary maximum number of triangles: \(R(10)=7<10\). Also \(R(11)=8<10\). The equality \(R(9)=R(10)=7\) gives the first plateau as the budget passes the first ordinary ten-triangle configuration.

## Assumptions and scope

Graphs are finite, simple and undirected. A triangle is counted once per three-element vertex set. The edge coloring need not be proper or use all three colors. Each edge counts toward \(m\), even if no triangle contains it. The maximum ranges over arbitrary graphs, not just complete graphs or a prescribed vertex order. Write \(t(G)\) for the number of ordinary triangles in \(G\), and \(r(G)\) for the rainbow-triangle count of a chosen three-edge-coloring. The upper bounds use the classical Kruskal--Katona triangle shadow bound: if \(m=\binom a2+b\) with \(0\le b<a\), then
\[
 t(G)\le Q(m):=\binom a3+\binom b2.
\]
Here \(Q(0),\ldots,Q(11)=(0,0,0,1,1,2,4,4,5,7,10,10)\).

## Proof

**Low budgets.** Since \(r(G)\le t(G)\le Q(m)\), the displayed values through \(m=9\) have the stated upper bounds. They are attained by edge subgraphs of a properly three-edge-colored \(K_4\) and a partially adjacent fifth vertex. Explicit colored witnesses at every \(m\le11\) are encoded and checked by the standalone `verify.cpp` file: vertices \(0,1,2,3\) form \(K_4\) with edges \(01,02,03,12,13,23\) colored \(0,1,2,2,1,0\); the extra vertex \(4\) joins \(0,1,2\) with colors \(2,1,0\). These nine edges yield seven rainbow triangles. The first six, smaller profiles are supplied explicitly by the verifier. At \(m=10\) add a pendant edge \(50\), creating no triangles; at \(m=11\) instead add \(50,51\) colored \(1,2\), adding exactly one rainbow triangle. Therefore \(R(10)\ge7\) and \(R(11)\ge8\).

**A small-support reduction.** We show for \(m=10\) that \(t(G)\ge8\) forces a \(K_5\), and for \(m=11\) that \(t(G)\ge9\) forces a \(K_5\). Discard all edges in no triangle, then discard isolated vertices. Each remaining nonempty connected component has at least three edges, and no vertex has degree one. If there are at least two components, applying \(Q\) to their edge budgets gives at most six triangles for a total of at most eleven edges: the maximal two-component splits are bounded by \(Q(3)+Q(8)=6\), \(Q(5)+Q(6)=6\), and their intervening cases; adding more components cannot increase the bound. Thus the triangle-bearing core may be assumed connected.

If this core has at least eight vertices, its average degree is at most \(22/8<3\). It has minimum degree at least two and hence a vertex of degree exactly two. Both incident edges lie in triangles, forcing its two neighbors to be adjacent; hence the vertex belongs to exactly one triangle. Deleting it removes two edges and just one triangle. If the initial edge budget is at most ten, \(t(G)\le1+Q(8)=6\); if at most eleven, \(t(G)\le1+Q(9)=8\). So the claimed high triangle thresholds can occur only in triangle-bearing cores of at most seven vertices. A core with fewer than ten edges has at most \(Q(9)=7\) triangles. It therefore suffices to check simple graphs on at most seven vertices with exactly ten or eleven edges.

The supplied exact enumerator iterates every labeled graph on \(3\le n\le7\) vertices and ten or eleven edges (709801 labeled profiles, without using isomorphism pruning). It counts triangles directly from edge masks and identifies every \(K_5\). It verifies the two implications above; among graphs without a \(K_5\), the maxima are seven triangles with ten edges and eight triangles with eleven edges. These finite exhaustive statements, not mere random tests, complete the small-support reduction.

**Rainbow obstruction inside a \(K_5\).** Any three-coloring of the ten edges of a \(K_5\) has at least three nonrainbow triangles. If at most two triangles were nonrainbow, each vertex would lie on at least one of them: among its four incident edges, two have the same color, and the edge between their opposite endpoints completes a nonrainbow triangle. Covering five vertices with two triples forces the triples to meet at one vertex. Label them \(123\) and \(145\). Each of vertices \(2,3\) is contained in only one nonrainbow triangle, so edges \(12,13,23\) must have a common color \(A\). Similarly edges \(14,15,45\) share a color \(B\). If \(A=B\), triangle \(124\) would be nonrainbow as well; therefore \(A\ne B\). All four cross edges \(24,25,34,35\) must now have the third color \(C\), because each belongs to a triangle with one \(A\)-edge and one \(B\)-edge which is assumed rainbow. But \(234\) has edge colors \(A,C,C\), a third nonrainbow triangle, contradiction. Thus a colored \(K_5\) has at most seven rainbow triangles. The upper bound is attained by the nine-edge witness after its missing tenth edge is supplied with any color without creating additional rainbow triangles (the verifier also checks all \(3^{10}=59049\) colorings).

Finally, a graph with at most eleven edges containing \(K_5\) has at most one edge outside that clique, hence no triangle outside the clique. Such a graph has at most seven rainbow triangles. A graph without \(K_5\) has at most seven ordinary triangles if it has ten edges, and at most eight if it has eleven. Hence \(R(10)\le7\) and \(R(11)\le8\), matching the witnesses. This proves the profile.

## Verification

Compile and execute `verify.cpp` with, for example, `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`. The independent output is recorded in `verification.log`. A corroborating `verify_atlas.py` script (NetworkX 3.x required) records its result in `atlas_verification.log`. The search exhausts every simple graph with exactly ten or eleven edges on three through seven labeled vertices and every three-coloring of \(K_5\); the code checks all twelve constructive witnesses. The graph search also reports the maximum ordinary triangle count when no \(K_5\) occurs. Exact integer enumeration is used throughout. The general reduction to at most seven vertices and the colored-\(K_5\) proof are mathematical arguments, not extrapolations from finite experiments.

## Relationship to prior work

The classical Kruskal--Katona theorem supplies the uncolored bound \(Q(m)\), but makes no assertion that each of those triangles can be rainbow under only three edge colors. Chao--Sankar--Yu (2026) establish a general colorful Kruskal--Katona inequality giving the three-color rainbow triangle upper bound \(r(G)\le\sqrt{2/27}\,m^{3/2}\), sharp for appropriate proper-color \(K_4\) blowups, but their result alone yields only the bounds \(R(10)\le8\) and \(R(11)\le9\) after taking integer parts. Balogh--Bradshaw--Garcia--Lidický (arXiv:2511.21061, first public in 2025) review and re-prove the sharper color-class statement \(T^2\le 2RGB\) and characterize equality. Optimizing \(RGB\) at total edge budgets ten and eleven still permits respectively eight and nine triangles, so their upper bound does not imply the present sharp counts. Balogh--Hu--Lidický--Pfender--Volec--Young (2014) study maximum rainbow triangles for complete graphs with a given number of vertices; their five-vertex construction supplies the seven-rainbow-triangle \(K_5\) witness and is not claimed new here. The claim here is the exact **edge-budget** sequence and the location of its first strict deficit, not a new construction of the \(K_5\) color pattern or a new asymptotic inequality.

## Limitations

This theorem determines only the first twelve budgets \(0\le m\le11\). It does not classify all extremizing colored graphs or determine \(R(m)\) for larger budgets. The exact finite search is a reproducible computational part of the proof and assumes the displayed program implements the specified complete enumeration; independently implemented exhaustive small-graph census and direct witness checks corroborate it. No claim of independent external audit is made. There remains some risk of an earlier equivalent edge-budget statement that is not indexed in the literature reviewed.

## References

1. H. Chao, M. Sankar, and S. Yu, *On Colorful Kruskal--Katona Theorems*, arXiv:2610.02165v1, first public 1 October 2026. https://arxiv.org/abs/2610.02165
2. J. Balogh, P. Hu, B. Lidický, F. Pfender, J. Volec, and M. Young, *Rainbow triangles in three-colored graphs*, arXiv:1408.5296v1 (2014). https://arxiv.org/abs/1408.5296
3. J. Balogh, P. Bradshaw, R. I. Garcia, and B. Lidický, *Density of rainbow triangles and properly colored \(K_4\)'s*, arXiv:2511.21061 (first public 26 November 2025; version 3 reviewed). https://arxiv.org/abs/2511.21061
4. J. B. Kruskal, *The number of simplices in a complex* (1963); G. O. H. Katona, *A theorem of finite sets* (1968). Classical triangle-shadow form used above.
