# Edge-open-packing polynomial of triangular graphs via disjoint short paths

## Finding

Let \(n\geq0\) be an integer. The triangular graph \(T_n=L(K_n)=J(n,2)\) has the two-element subsets of \([n]\) as vertices, adjacent precisely when they intersect. An **edge-open packing** is a set \(S\) of edges of a graph such that no two distinct members admit a third edge (distinct from them) joining an endpoint of one to an endpoint of the other. Include the empty packing in the enumerator \(E_n(z)=\sum_S z^{|S|}\).

**Theorem.** Edge-open packings of \(T_n\) are in bijection with collections of pairwise vertex-disjoint, undirected edge-paths on \([n]\), each having either two edges (a \(P_3\) block) or three edges (a \(P_4\) block). A \(P_3\) block contributes one selected edge of \(T_n\), and a \(P_4\) block contributes two. Consequently,

\[
\boxed{\sum_{n\geq0}E_n(z)\frac{u^n}{n!}=\exp\!\left(u+\frac{u^3z}{2}+\frac{u^4z^2}{2}\right)}.
\]

Equivalently, for every \(n\geq0\),

\[
\boxed{E_n(z)=\sum_{\substack{a,b\geq0\\3a+4b\leq n}}\frac{n!}{(n-3a-4b)!\,a!\,b!\,2^{a+b}}z^{a+2b}}.
\]

For all \(n\geq0\), the maximum packing cardinality (with value zero for an edgeless graph) is

\[
\boxed{\rho_e^o(T_n)=\left\lfloor\frac n2\right\rfloor-\mathbf1_{\{n\equiv2\pmod4\}}}.
\]

Writing \(n=4q+r\) with \(q\geq0\) and \(r\in\{0,1,2,3\}\), the number \(M_n=[z^{\rho_e^o(T_n)}]E_n(z)\) of maximum packings is

\[
\boxed{M_n=\begin{cases}
\dfrac{n!}{2^q q!}, & r=0,1,\\[6pt]
\dfrac{n!}{2^{q+1}q!}+\mathbf1_{\{q\geq1\}}\dfrac{n!}{2^{q+2}(q-1)!}, & r=2,\\[6pt]
\dfrac{n!}{2^{q+1}q!}, & r=3.
\end{cases}}
\]

The second term for \(r=2\) represents a genuinely different extremal configuration: two disjoint \(P_3\) blocks replacing one \(P_4\) block and two unused vertices.

## Assumptions and scope

All graphs are finite, simple and undirected. A path block is specified by its **chosen edges**, not required to be an induced subgraph of the ambient complete graph \(K_n\). An undirected path and its reversal are the same block. Different path blocks share no original vertex label. The word “triangular graph” means specifically \(L(K_n)\), not the larger class of graphs in which every edge belongs to a triangle. We adjoin the empty edge set for polynomial enumeration even if the edge-open-packing number is elsewhere introduced only for nonempty edge sets.

## Proof

**1. The star-forest characterization.** For any graph \(G\) and any nonempty edge set \(S\), write \(V(S)\) for all endpoints of its edges. If \(S\) is edge-open, the selected-edge subgraph \((V(S),S)\) has no triangle and no three-edge path: the first and last edges of either forbidden configuration would have a common third edge. A connected graph with neither a triangle nor a three-edge path is a star. Moreover, every edge in the induced graph \(G[V(S)]\) belongs to \(S\). Otherwise that extra edge joins endpoints of two different selected edges (it cannot join the two endpoints of just one selected edge in a simple graph), contradicting edge openness. Thus \(G[V(S)]\) is exactly the disjoint union of the selected stars. Conversely, if \(G[V(S)]\) consists of stars whose whole edge sets are \(S\), there is no third edge joining endpoints of selected edges: within a star such an edge would join distinct leaves, and between stars it would join components. This proves the equivalence in both directions.

**2. Only two nontrivial star types in \(T_n\).** A vertex \(\{i,j\}\) of \(T_n\) has its neighbors partitioned into the clique of edges of \(K_n\) incident to \(i\) and the clique of edges incident to \(j\). An independent subset of its neighborhood therefore has size at most two. Every nontrivial induced star in \(T_n\) is consequently either \(K_2\) or \(P_3\). Two adjacent vertices of \(T_n\) represent two edges of \(K_n\) sharing exactly one endpoint, hence a chosen \(P_3\) on three original labels. In an induced \(P_3\) of \(T_n\), the first and third original edges are disjoint while each meets the middle original edge. Their union is therefore a chosen four-label \(P_4\). Different induced-star components have no adjacency in \(T_n\), so their represented original edges share no original label. The converse holds: any vertex-disjoint family of these original paths induces disjoint \(K_2\) and \(P_3\) components in \(T_n\), whose complete edge set is edge-open by step 1. No other packings exist; in particular the correspondence is bijective.

**3. Exact enumeration.** On three prescribed labels, there are exactly three undirected \(P_3\) paths (choice of middle vertex), each weighted \(z\). On four prescribed labels, there are exactly \(4!/2=12\) undirected \(P_4\) paths (linear orders up to reversal), each weighted \(z^2\). Unused labels form singleton blocks. The labeled exponential formula for a set of such blocks gives

\[
\exp\!\left(u+3z\frac{u^3}{3!}+12z^2\frac{u^4}{4!}\right)=\exp\!\left(u+\frac{u^3z}{2}+\frac{u^4z^2}{2}\right).
\]

Taking the coefficient of \(u^n/n!\) yields the displayed finite double sum. In particular, one may compute all coefficients recursively from \(E_0(z)=E_1(z)=E_2(z)=1\) and

\[
E_{n+1}(z)=E_n(z)+3\binom n2zE_{n-2}(z)+12\binom n3z^2E_{n-3}(z)
\]

for every \(n\geq2\), with the final term omitted when \(n<3\).

**4. Maximum cardinality and multiplicity.** A family with \(a\) three-label blocks and \(b\) four-label blocks uses \(3a+4b\leq n\) labels and contributes \(t=a+2b\) packed edges. For fixed \(t\), this requires at least \(2t\) labels when \(t\) is even and \(2t+1\) labels when \(t\) is odd: minimize \(3t-2b\) over integers \(0\leq b\leq\lfloor t/2\rfloor\). This minimum is attained and proves the displayed degree formula for every residue class of \(n\) modulo four. The pairs \((a,b)\) at maximum degree are precisely \((0,q)\) for \(r=0,1\); \((0,q)\) and, only when \(q\geq1\), \((2,q-1)\) for \(r=2\); and \((1,q)\) for \(r=3\). Substituting these pairs in the proven coefficient formula gives the displayed piecewise formula for \(M_n\). This covers \(n=0,1,2,3\) without exceptions.

## Verification

Run `python3 verify.py` from the directory containing `verify.py`; the expected output is recorded in `verification_output.txt`. The direct oracle constructs the adjacency of \(T_n\), tests the literal third-edge conflict relation, and enumerates **every** edge-open packing for \(2\leq n\leq8\) without using the claimed block formula to decide feasibility. It then checks the original-path profile of each enumerated set and compares the profile counts with the formula: 21,517 packings are checked in total. Separately, exact integer computations verify the generating-function recurrence, the coefficient formula, the maximal degree, and its coefficient for \(0\leq n\leq60\). All checks returned `VERIFY_OK`.

These finite computations are corroboration, not proof of the all-\(n\) theorem; the proof is the bijection and labeled counting above.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan (2022) introduced edge-open packing and determined its maximum for several standard graph families; their paper includes the induced-star observation. Brešar and Samadi (2024) analyze complexity and trees, while Brešar, Dravec, Hedžet and Samadi (2024) compare induced matching and edge-open packing for trees and graph products. Their “triangular graphs” in the complexity corollary means graphs whose every edge lies in a triangle, not specifically the graph \(T_n=L(K_n)\). Pandey and Santra (2025) give general graph characterizations. The inspected statements do not supply the complete all-cardinality enumerator, its short-path bijection on \(T_n\), or the piecewise extremal multiplicities claimed here. The induced-star observation and generic labeled-block exponential formula are standard ingredients, not separately asserted as original.

## Limitations

This theorem is restricted to triangular graphs \(T_n\), not arbitrary line graphs or arbitrary graphs with all edges in triangles. It counts all edge-open packings, not injective edge-coloring partitions. Exact formulas and finite verification do not establish publication priority; synonymous terminology or unindexed combinatorial enumerations could describe the same coefficient sequence. Independent validation has not been performed.

## References

1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, “Edge open packing sets in graphs,” *RAIRO Operations Research* **56** (2022), 3765–3776, doi:10.1051/ro/2022171. Public online date: 2022-11-01. https://www.numdam.org/item/10.1051/ro/2022171.pdf
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750v1 (2024-03-01). https://arxiv.org/pdf/2403.00750
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:2406.04020v2 (2024-06-07). https://arxiv.org/pdf/2406.04020
4. A. Pandey and K. Santra, “Edge open packing: further characterizations,” arXiv:2508.01935v1 (2025-08-03). https://arxiv.org/pdf/2508.01935
