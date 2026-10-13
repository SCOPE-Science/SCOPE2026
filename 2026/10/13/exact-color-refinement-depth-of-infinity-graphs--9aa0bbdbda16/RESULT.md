# Exact color-refinement depth of infinity graphs
## Finding
For integers \(p,q\ge3\), let \(F_{p,q}\) be the infinity graph (also called a figure-eight or tight-handcuff graph) obtained from cycles \(C_p\) and \(C_q\) by identifying exactly one vertex. Let \(\operatorname{Stab}(G)\) be the least round at which ordinary color refinement from the uniform coloring stops changing the induced vertex partition.

Then
\[
\operatorname{Stab}(F_{p,q})=
\begin{cases}
\left\lfloor p/2\right\rfloor,&p=q,\\
\max\!\left\{\left\lfloor p/2\right\rfloor,\left\lfloor q/2\right\rfloor,\min\{p,q\}\right\},&p\ne q.
\end{cases}
\]

Moreover, every infinity graph is refinable: its stable color-refinement partition is exactly the automorphism-orbit partition.

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. The shared vertex is denoted \(c\); it has degree \(4\), while every other vertex has degree \(2\). Round \(0\) is the uniform coloring. A graph is called refinable when the stable color-refinement partition equals its automorphism-orbit partition.

The convention \(F_{p,q}\) follows the standard infinity-graph definition: two cycles with exactly one common vertex.

## Proof
Round \(1\) separates the unique degree-\(4\) vertex \(c\) from every degree-\(2\) vertex. Regard each cycle, cut at \(c\), as a thread whose two endpoints are both \(c\). A vertex on a thread of length \(L\) at distances \(i\) and \(L-i\) from the two copies of \(c\) has, after round \(r\ge1\), a color determined exactly by the unordered clipped pair
\[
\left\{\min\{i,r\},\min\{L-i,r\}\right\}.
\]
This follows by induction on \(r\): round \(1\) records only whether a neighbor is \(c\), and each later round exposes one additional edge toward each endpoint.

Within one length-\(L\) thread, these pairs stop refining exactly at round
\[
\left\lfloor L/2\right\rfloor.
\]
Thus the two cycles contribute \(\lfloor p/2\rfloor\) and \(\lfloor q/2\rfloor\).

If \(p=q\), corresponding positions on the two cycles have identical clipped pairs forever, and the stated value follows.

Suppose \(p\ne q\), say \(p<q\). Vertices one edge from \(c\) on the two cycles remain color-equivalent through round \(p-1\): their clipped pairs are both \(\{1,r\}\). In round \(p\), the short-cycle position has pair \(\{1,p-1\}\), while the long-cycle position has pair \(\{1,p\}\), so the cycle types split. No cross-cycle collision can survive longer: once \(r\ge p\), equality of clipped pairs for positions on lengths \(p\) and \(q\) would force equality of the corresponding full endpoint-distance sums, hence \(p=q\), a contradiction. Therefore the last possible cross-cycle split occurs exactly in round \(\min\{p,q\}\), yielding the formula.

For orbit recovery, if \(p\ne q\), the two cycles cannot be interchanged by an automorphism. On each cycle, the orbit of a noncentral vertex is determined exactly by its unordered distance pair \(\{i,L-i\}\), corresponding to reflection of that cycle through \(c\). Stable colors give exactly these classes and distinguish the two cycle lengths. If \(p=q\), an automorphism may interchange the two cycles, and vertices with the same unordered distance pair across either cycle form one orbit. The stable colors merge exactly those vertices. Hence every \(F_{p,q}\) is refinable.

## Verification
The accompanying standalone program `verify.py` directly constructs \(F_{p,q}\), implements ordinary color refinement, evaluates the closed formula, and compares the stable partition with the explicit automorphism-orbit partition.

For every
\[
3\le p,q\le50,
\]
it verifies both claims. It returns:

`VERIFY_OK depth_checks=2304 orbit_checks=2304 p,q=3..50`

The finite computation is corroborative only. The proof above establishes the theorem for all \(p,q\ge3\).

## Relationship to prior work
Wang, Huang, Belardo, and Li Marzi study the same infinity-graph family in their 2010 spectral-characterization paper and define an infinity graph as two cycles having exactly one vertex in common. Their results concern graph spectra, not color refinement.

Krebs and Verbitsky formalize color-refinement stabilization and the universal-cover interpretation of refinement depth. Arvind, Köbler, Rattan, and Verbitsky define a graph to be refinable when its stable partition is its automorphism-orbit partition.

Targeted searches for infinity graphs, figure-eight graphs, and tight handcuffs together with color refinement, \(1\)-WL, Weisfeiler--Leman iteration depth, equitable partitions, and refinability did not locate the exact formula above or the all-parameter orbit-recovery statement. The present family is a different bicyclic core from dumbbell graphs: infinity graphs share one branch vertex, whereas dumbbells have two branch vertices joined by a connector.

## Limitations
The theorem is specific to the two-cycle one-vertex wedge. It does not classify arbitrary cactus graphs, bouquets of three or more cycles, higher-dimensional Weisfeiler--Leman refinement, or color refinement from nonuniform initial colorings. The literature search was targeted rather than exhaustive, so an unindexed equivalent computation remains a residual priority risk.

## References
1. J. Wang, Q. Huang, F. Belardo, and E. M. Li Marzi, *On the spectral characterizations of infinity-graphs*, 2010; institutional record HDL 11570/1903053.
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
3. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015.
