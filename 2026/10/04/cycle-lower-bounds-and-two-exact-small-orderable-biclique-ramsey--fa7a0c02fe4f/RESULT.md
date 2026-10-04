# Cycle lower bounds and two exact small orderable biclique Ramsey numbers
## Finding
For every integer \(t\ge 3\),
\[
r'_2(K_{2,t})\ge t+3,
\qquad
CR(K_{2,t},K_3)\ge t+3.
\]
Moreover,
\[
r'_2(K_{2,4})=CR(K_{2,4},K_3)=7
\]
and
\[
r'_2(K_{2,5})=CR(K_{2,5},K_3)=8.
\]
Here \(r'_2(G)\) is the least \(n\) such that every red-blue coloring of \(K_n\) contains an orderable copy of \(G\), and \(CR(G,K_3)\) is the least \(n\) such that every edge-coloring of \(K_n\) contains an orderable copy of \(G\) or a rainbow triangle.

## Assumptions and scope
All graphs are finite and simple. An edge-colored graph is orderable if its vertices admit a linear order such that, at every vertex, all incident edges going to later vertices have one common color. The universal lower bound above concerns the complete bipartite graph \(K_{2,t}\) for integers \(t\ge 3\). The exact evaluations for \(t=4,5\) additionally use the published 2026 upper bound of Li.

## Proof
Fix \(t\ge3\), put \(n=t+2\), and color the edges of \(K_n\) red exactly on a Hamilton cycle \(C_n\); color every other edge blue.

Fix a proposed two-vertex side \(\{x,y\}\) of a copy of \(K_{2,t}\). For each of the other \(n-2=t\) vertices, record the ordered pair of colors on its edges to \(x\) and \(y\). Call the four possible classes \(V_{rr},V_{rb},V_{br},V_{bb}\).

A colored \(K_{2,t}\) with two-vertex side \(\{x,y\}\) is orderable only if one of \(V_{rb}\) and \(V_{br}\) is empty. Indeed, if \(u\in V_{rb}\) and \(v\in V_{br}\), then the four-cycle on \(x,u,y,v\) alternates colors. No alternating colored four-cycle is orderable: whichever vertex is first in a proposed linear order has two later neighbors joined to it in different colors. Since induced vertex restrictions of an orderable coloring remain orderable, the whole biclique cannot be orderable.

Conversely, if one alternating class is empty, the biclique is orderable. For example, if \(V_{rb}=\varnothing\), order first the vertices of \(V_{rr}\cup V_{bb}\), then \(x\), then the vertices of \(V_{br}\), then \(y\). Each vertex sees only one color among its later incident biclique edges. Thus, for a fixed ordered pair \(x,y\), the largest orderable two-by-many biclique available from the remaining vertices has size
\[
n-2-\min\{|V_{rb}|,|V_{br}|\}.
\]

In the red cycle \(C_n\) with \(n\ge5\), every two distinct vertices \(x,y\) have incomparable red neighborhoods after the opposite endpoint is removed: there is a vertex other than \(x,y\) that is red-adjacent to \(x\) but not to \(y\), and another that is red-adjacent to \(y\) but not to \(x\). This is immediate by considering whether their cyclic distance is one, two, or at least three. Hence \(V_{rb}\neq\varnothing\) and \(V_{br}\neq\varnothing\) for every proposed two-vertex side. Therefore the red-cycle coloring of \(K_{t+2}\) contains no orderable \(K_{2,t}\), proving
\[
r'_2(K_{2,t})\ge t+3.
\]
Because this witness uses only two colors, it has no rainbow triangle, so the same coloring also proves
\[
CR(K_{2,t},K_3)\ge t+3.
\]

Li proves for every \(t\ge2\) that
\[
r'_2(K_{2,t})\le CR(K_{2,t},K_3)\le \left\lfloor\frac{4t}3\right\rfloor+2.
\]
For \(t=4\) and \(t=5\), this upper bound is respectively \(7\) and \(8\), exactly matching the cycle lower bound. This proves both exact evaluations.

## Verification
The accompanying verifier reconstructs the red-cycle colorings directly. It checks the two alternating classes for every choice of the two-vertex side for every \(3\le t\le50\). Independently of that criterion, it also enumerates all vertex orders for every proposed two-vertex side when \(3\le t\le5\), verifying directly from the definition that no corresponding \(K_{2,t}\) is orderable. Finally it checks the arithmetic match between the cycle lower bound and Li's stated upper bound at \(t=4,5\). These computations are finite stress tests; the proof above is the universal argument.

## Relationship to prior work
Li introduced the graph-parameter versions \(r'_2(G)\) and \(CR(G,H)\) in this setting and proved the complete-bipartite upper bound used above. His paper also obtains exact values for infinitely many parameters by strongly regular graph, Hadamard-matrix, and conference-matrix constructions. The full text was inspected for the specific \(K_{2,4}\), \(K_{2,5}\), and red-cycle lower-bound formulations; no statement covering the two exact small values above was located.

Brosch, Lidický, Miyasaki, and Puges study small ordered and canonical Ramsey numbers and include \(K_{2,4}\) among several small bipartite graphs in computations for other target pairs. Their inspected tables do not give \(CR(K_{2,4},K_3)\), and no \(K_{2,5}\) case was located there. Targeted semantic and exact-formula searches likewise found no prior statement implying the two exact values.

## Limitations
The universal cycle construction gives only the lower bound \(t+3\); for larger \(t\), Li's asymptotic theory is substantially stronger. The exact conclusion asserted here is only for \(t=4,5\). Literature searches cannot establish absolute uniqueness, so a residual risk remains that an unindexed or differently phrased source contains one of these small exact evaluations. No independent audit has been performed.

## References
1. Xihe Li, “Ramsey-type results for threshold graphs and beyond,” arXiv:2608.22350, first public 2026-08-23. In particular, Theorem 1.8 gives the complete-bipartite upper bound used here.
2. Daniel Brosch, Bernard Lidický, Sydney Miyasaki, and Diane Puges, “Lower and Upper Bounds for Small Canonical and Ordered Ramsey Numbers,” arXiv:2511.04364, first public 2025-11-06.
