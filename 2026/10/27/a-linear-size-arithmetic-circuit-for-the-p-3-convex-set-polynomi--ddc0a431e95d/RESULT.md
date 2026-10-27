# A linear-size arithmetic circuit for the \(P_3\)-convex-set polynomial of block graphs

## Finding
For a finite simple graph \(G\), let
\[
 P_G(z)=\sum_{\substack{S\subseteq V(G)\\\forall v\notin S:\ |N_G(v)\cap S|\le1}}z^{|S|}.
\]
A set in this sum is \(P_3\)-convex: no excluded vertex has two included neighbors. For every block graph \(G\), all coefficients of \(P_G(z)\) are determined by a uniform three-message recursion on the block–vertex incidence forest. The recursion has \(O(|V(G)|+|E(G)|)\) arithmetic-circuit gates (addition and multiplication in \(\mathbb Z[z]\)). In particular \(P_G(1)\), the number of \(P_3\)-convex sets, can be evaluated with linearly many integer arithmetic operations once the block decomposition is known.

For a one-vertex bouquet of \(k\ge1\) cliques of orders \(m_i\ge2\), the exact polynomial is
\[
 P_G(z)=1+\left(\sum_{i=1}^{k}(m_i-1)\right)z+z\prod_{i=1}^{k}\left(1+z^{m_i-1}\right).
\]
Unlike a scalar count, the polynomial gives the number of convex sets of **every** cardinality.

## Assumptions and scope
A *block* is a maximal 2-connected subgraph, with each bridge treated as a block of order two. A *block graph* has every block complete; isolated vertices are permitted as components. All graphs are finite, simple, and undirected. The incidence graph connecting each vertex to its containing blocks is a forest; within any connected nontrivial component it is a tree. Denote its vertex nodes by \(v\) and its clique-block nodes by \(Q\). Root each component at any vertex node. Every block node then has exactly one parent vertex and one or more child vertices. Empty components contribute the multiplicative identity \(1\).

A message \(A_v\) counts subsets of the vertices represented by the subtree below \(v\), with weight \(z\) per selected vertex, for which \(v\) is omitted and has **zero** selected neighbors among that subtree's blocks. The message \(B_v\) imposes **exactly one** such neighbor. The message \(C_v\) selects \(v\), including the factor \(z\). All other omitted vertices in the subtree must already obey the \(P_3\)-convexity rule. The only possible additional neighbors of \(v\) above the subtree belong to its parent block, and therefore are deliberately not counted in \(A_v\) or \(B_v\).

## Proof
**Clique-block message.** Let \(Q\) have parent vertex \(v\) and child vertices \(u_1,\ldots,u_t\), with \(t\ge1\). Suppress the indices on a product ranging over these children. Define
\[
\begin{aligned}
 X_Q&=\prod_{i=1}^{t}(A_{u_i}+B_{u_i}),\\
 Y_Q&=\sum_{j=1}^{t}C_{u_j}\prod_{i\ne j}A_{u_i},\\
 Z_Q&=\prod_{i=1}^{t}A_{u_i}+\prod_{i=1}^{t}C_{u_i}.
\end{aligned}
\]
If \(v\) is omitted, it may have at most one selected neighbor in \(Q\). With zero selected children, every child is omitted, and its descendant contributions are independently either zero or one: this is \(X_Q\). With exactly one selected child \(u_j\), every other child is omitted but already sees \(u_j\), so must have no selected descendant neighbor: this is \(Y_Q\).

If \(v\) is selected, any omitted child already sees \(v\). Therefore either **all** children are omitted, in which case each must have zero selected descendant neighbors, or **all** children are selected. A mixture of selected and omitted children would leave an omitted child adjacent to both \(v\) and a selected sibling, contradicting convexity. These two disjoint cases are the terms of \(Z_Q\). This remains valid for a two-vertex block, since its sole child is either omitted or selected.

**Vertex message.** If \(Q_1,\ldots,Q_s\) are the child blocks of vertex \(v\), then
\[
\begin{aligned}
 A_v&=\prod_{j=1}^{s}X_{Q_j},\\
 B_v&=\sum_{j=1}^{s}Y_{Q_j}\prod_{i\ne j}X_{Q_i},\\
 C_v&=z\prod_{j=1}^{s}Z_{Q_j}.
\end{aligned}
\]
Indeed the incident blocks contribute disjoint sets of neighbors of \(v\). When \(v\) is omitted, the total selected neighbor count must be zero or one, so respectively no block or exactly one block contributes a selected neighbor. When \(v\) is selected there is no restriction at \(v\); each child block uses its \(Z\)-case. For a vertex leaf, the empty product/sum convention gives \((A_v,B_v,C_v)=(1,0,z)\).

**Induction and completeness.** The block–vertex incidence graph is a tree in each connected component, so every child subtree is disjoint from every other except at its parent. The two preceding local case distinctions are necessary and sufficient for the defining outside-neighbor inequality. Every selected set has one unique restriction to each child subtree and thus contributes to exactly one product monomial. Inducting from leaves to a root \(r\) proves
\[
P_{G_{\mathrm{component}}}(z)=A_r+B_r+C_r.
\]
Distinct graph components impose independent inequalities, hence \(P_G(z)\) is the product of the root expressions; for the empty graph it is \(1\).

**Arithmetic bound.** A sum of the form \(\sum_j b_j\prod_{i\ne j}a_i\) is computable in linear arithmetic operations by maintaining \((p,q)\), initialized to \((1,0)\), and updating \((p,q)\mapsto(pa_j,qa_j+pb_j)\). The same recurrence computes the products and all one-selected-child terms above without division, including cases with zero coefficients. Every incidence-tree edge is processed a constant number of times; the total number of incidences is \(O(|V|+|E|)\). Standard block decomposition is also linear in \(|V|+|E|\). Thus the polynomial has a linear-size arithmetic circuit. This does **not** assert linear bit-time to expand all coefficients: exact integer sizes and polynomial multiplication costs are additional considerations.

**Clique-bouquet corollary.** At a bouquet center \(r\), each petal block has \(m_i-1\) private leaves, so its messages are \(X_i=1\), \(Y_i=(m_i-1)z\), and \(Z_i=1+z^{m_i-1}\). Substituting these in the root formulas proves the displayed closed form for all \(k\ge1\) and \(m_i\ge2\).

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The program independently enumerates every vertex subset on 937 block graphs generated by clique attachment (up to 16 vertices), and enumerates every labelled graph through six vertices whose biconnected blocks are cliques (8,367 such graphs). For every graph it compares each cardinality coefficient against direct evaluation of \(|N_G(v)\cap S|\le1\) for all omitted vertices. It also checks the bouquet formula for five clique-size patterns. The recorded output is `verify_output.txt`. The finite checks corroborate but do not replace the unrestricted induction.

## Relationship to prior work
Dourado, Grippo, Lin and Protti (arXiv:2603.04706v1, first posted 2026-03-05) introduced the general counting problem \(\operatorname{noc}(G)=P_G(1)\), proved \(\#\mathrm P\)-completeness already on split graphs, and established linear-time counting for trees and threshold graphs. Their full paper treats these classes and generic exponential-time algorithms, but does not present a block-graph counting theorem or a size-generating polynomial for block graphs. The present arithmetic circuit handles arbitrarily many overlapping clique blocks of unbounded size, and recovers the tree case when all blocks have two vertices. The 2012 Barbosa–Coelho–Dourado–Rautenbach–Szwarcfiter paper studies a different \(P_3\)-convexity invariant, the Carathéodory number, including on block graphs, not the size distribution of all convex subsets in its available abstract. Carr's 2020 thesis counts *digitally convex* sets on block graphs, a different convexity whose excluded-vertex condition involves private neighbors rather than a two-selected-neighbor threshold.

## Limitations
The result is restricted to block graphs: the clique-block incidence graph must be a forest. It is not an algorithm for general chordal or split graphs. It supplies an exact arithmetic circuit, not a uniform linear bit-complexity bound for expanded coefficient lists. The brute-force verification stops at its stated finite ranges. Relevant older full texts not inspected in entirety may contain equivalent recurrences under different convexity terminology; novelty should receive independent bibliographic review before publication. No independent mathematical audit has been conducted.

## References
1. M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first posted 2026-03-05), https://arxiv.org/abs/2603.04706.
2. R. M. Barbosa, E. M. M. Coelho, M. C. Dourado, D. Rautenbach, and J. L. Szwarcfiter, *On the Carathéodory Number for the Convexity of Paths of Order Three*, SIAM J. Discrete Math. 26 (2012), 929–939, https://doi.org/10.1137/110828678.
3. M. Carr, *Enumerating digitally convex sets in graphs*, MSc thesis, University of Victoria (2020), https://dspace.library.uvic.ca/items/e38136c4-f854-4103-b22e-1a3e78a1925f.
