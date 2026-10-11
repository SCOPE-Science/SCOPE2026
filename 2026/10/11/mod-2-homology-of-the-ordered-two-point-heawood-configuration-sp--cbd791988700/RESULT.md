# Mod-\(2\) homology of the ordered two-point Heawood configuration space
## Finding
For the Heawood graph \(H\), the ordered two-point configuration space \(F_2(H)=\{(x,y)\in H\times H:x\ne y\}\) has reduced mod-\(2\) homology \(\widetilde H_1(F_2(H);\mathbb F_2)\cong\mathbb F_2^{16}\), \(\widetilde H_2(F_2(H);\mathbb F_2)\cong\mathbb F_2^{29}\), and \(\widetilde H_i(F_2(H);\mathbb F_2)=0\) for every \(i\notin\{1,2\}\).

Equivalently, the ordinary mod-\(2\) Betti vector in dimensions \(0,1,2\) is \((1,16,29)\).

## Assumptions and scope
The graph \(H\) is the Heawood graph, realized as the point-line incidence graph of the Fano plane. Thus \(H\) is a connected cubic graph with \(14\) vertices, \(21\) edges, and girth \(6\). The space \(F_2(H)\) is the ordered configuration space of two distinct points on the geometric realization of \(H\).

The claim concerns homology with coefficients in \(\mathbb F_2\). It does not identify the integral homology, cohomology ring, fundamental group, unordered configuration space, or homotopy type.

## Proof
For two particles, the Abrams discrete configuration model \(D_2(H)\) has cells given by ordered products of vertices and open edges whose closures are pairwise disjoint. The sufficient subdivision conditions hold for the Heawood graph: every vertex has degree \(3\), every path between distinct essential vertices contains at least one edge, and every nontrivial loop contains at least three edges because the girth is \(6\). Hence \(F_2(H)\) deformation retracts onto \(D_2(H)\).

The discrete model has exactly \(182\) zero-cells, \(504\) one-cells, and \(336\) two-cells. Indeed, there are \(14\cdot13=182\) ordered pairs of distinct vertices. A one-cell chooses which coordinate moves along one of the \(21\) edges and a stationary vertex outside the two endpoints, giving \(2\cdot21\cdot12=504\). Each edge of the cubic Heawood graph has \(16\) disjoint partner edges, so the ordered two-cells number \(21\cdot16=336\).

Over \(\mathbb F_2\), the exact cellular boundary matrices have ranks
\[
\operatorname{rank}(\partial_1)=181,\qquad
\operatorname{rank}(\partial_2)=307.
\]
Therefore
\[
\beta_0=182-181=1,
\]
\[
\beta_1=504-181-307=16,
\]
and
\[
\beta_2=336-307=29.
\]
There are no cells above dimension \(2\), so all higher homology vanishes. The Euler characteristic check is \(182-504+336=14=1-16+29\).

## Verification
The bundled `verify.py` reconstructs the Fano-plane incidence graph from the cyclic line rule, independently enumerates every cell of \(D_2(H)\), builds both cellular boundary matrices over \(\mathbb F_2\), checks \(\partial_1\partial_2=0\) column by column, and performs exact Gaussian elimination on bit-vector columns. It reproduces cell counts \((182,504,336)\), boundary ranks \((181,307)\), Betti vector \((1,16,29)\), and Euler characteristic \(14\). The accompanying `certificate.json` records these exact values.

## Relationship to prior work
Agarwal, Banks, Gadish, and Miyata develop deletion and contraction operations on configuration spaces of graphs and explicitly treat generalized homology as a graph invariant; their work supplies a natural middle-period literature context for exact graph-configuration homology. The inspected paper contains no Heawood-graph or Fano-plane computation. The Abrams discrete model, in the sufficient-subdivision form used here, justifies replacing the continuous configuration space by the finite cubical complex \(D_2(H)\); that theorem does not determine the boundary ranks above.

Searches under the aliases “Heawood graph,” “Fano incidence graph,” “Fano Levi graph,” “two-point configuration,” “two-particle configuration,” and “graph braid group” did not locate an exact statement implying the Betti vector \((1,16,29)\). The closest located configuration-space results concern generalized theta graphs, finite crowns, minimal finite spheres, or a four-particle theta graph, not the ordered two-point Heawood space.

## Limitations
The result is an exact finite mod-\(2\) homology computation, not a homotopy classification. No assertion is made about torsion in integral homology, cup products, unordered configurations, or higher particle numbers. An unindexed computation under graph-braid-group terminology remains a residual originality risk.

## References
1. Sanjana Agarwal, Maya Banks, Nir Gadish, and Dane Miyata, “Deletion and contraction in configuration spaces of graphs,” arXiv:2005.13666; *Algebraic & Geometric Topology* 21 (2021), DOI 10.2140/agt.2021.21.3663.
2. A. Abrams, discrete configuration-space model for graph configuration spaces; the sufficient-subdivision statement is used only to identify \(F_2(H)\) with the finite model computed here.
