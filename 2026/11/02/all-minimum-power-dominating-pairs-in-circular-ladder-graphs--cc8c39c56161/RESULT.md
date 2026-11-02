# All minimum power-dominating pairs in circular ladder graphs

## Finding
Let \(G_n=C_n\square K_2\) be the labelled circular ladder (cycle prism), with vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\), horizontal cycle edges in each row and rungs \(u_iv_i\). Define \(\delta(i,j)=\min\{|i-j|,n-|i-j|\}\), taking representatives \(0,\ldots,n-1\). The power-domination number is \(1\) at \(n=3\) and \(2\) for every \(n\ge4\). At \(n=3\), the six singleton vertices are precisely the minimum power-dominating sets. For every \(n\ge4\), all minimum power-dominating sets are **exactly** the following two disjoint classes:

* Two vertices in the same row, \(\{u_i,u_j\}\) or \(\{v_i,v_j\}\), where \(1\le\delta(i,j)\le3\).
* One vertex from each row, \(\{u_i,v_j\}\), where \(\delta(i,j)\le2\).

Thus the number \(M_n\) of minimum power-dominating sets is
\[
M_n=\begin{cases}6,&n=3,\\28,&n=4,\\45,&n=5,\\60,&n=6,\\11n,&n\ge7.\end{cases}
\]
In particular the first nonzero coefficient of the power-domination polynomial of the cycle prism is exactly \(11n\) from \(n=7\) onward.

## Assumptions and scope
Graphs are finite, simple and undirected. Power domination starts with the closed neighborhood \(N[S]\) observed and repeatedly observes the unique unobserved neighbor of any observed vertex, if such a neighbor exists. Vertices are labelled; unordered subsets, not orbits under graph automorphisms, are counted. The two rims are named; their interchange preserves the classification. The small graph \(G_3\) is the triangular prism, not the three-rung multigraph obtained from a degenerate cycle.

## Proof
**Propagation lemma.** Suppose two consecutive full rungs, numbered \(i\) and \(i+1\), are observed: all four of \(u_i,v_i,u_{i+1},v_{i+1}\). The observed vertices of rung \(i\) each have their neighbor in rung \(i+1\) and their rung partner already observed, so each can force its sole remaining horizontal neighbor in rung \(i-1\) if not observed. Symmetrically rung \(i+1\) forces rung \(i+2\). Repeating inductively in both directions observes the entire finite prism. Hence two consecutive fully observed rungs suffice.

For \(n\ge4\), one seed cannot power-dominate. Indeed, by vertex transitivity take \(S=\{u_0\}\). Its initial observed vertices are \(u_{-1},u_0,u_1,v_0\). The seed has no unobserved neighbor, while each of the other three observed vertices has two unobserved neighbors, so no forcing move is available. (The claim holds for \(n=4\), when \(u_{-1}\) and \(u_1\) share a horizontal neighbor.) By contrast when \(n=3\), selecting \(u_0\) observes all three \(u\)-vertices and \(v_0\); the two other observed \(u\)-vertices each force its rung neighbor, so any singleton succeeds by vertex transitivity.

**Sufficiency.** By rotation/reflection and row interchange, consider a same-row pair \(\{u_0,u_d\}\) or a cross-row pair \(\{u_0,v_d\}\), with \(d=\delta(0,d)\). For same-row \(d=1\), the initial observation contains full adjacent rungs \(0,1\). For \(d=2\), rung \(1\) has both horizontal neighbors observed and forces \(v_1\), making adjacent rungs \(0,1\) full. For \(d=3\), the two inner observed vertices \(u_1,u_2\) each have both horizontal neighbors observed and force \(v_1,v_2\), making adjacent rungs \(1,2\) full. In each case propagation completes by the lemma. For cross-row \(d=0\), the initial observation contains full rungs \(0,1\). For \(d=1\), it contains full rungs \(0,1\). For \(d=2\), it contains full rungs \(1,2\). Hence all listed pairs succeed.

**Necessity.** Consider two seeds in one rim with cyclic distance \(d\ge4\). Their closed neighborhoods are disjoint in the respective horizontal rim and each nonseed initially observed vertex has at least two unobserved neighbors: a horizontally adjacent rim vertex has its external horizontal neighbor and rung partner unobserved, while each observed rung partner has both horizontal neighbors unobserved. Each seed itself has none. Thus no initial forcing move exists. For opposite-rim seeds at cyclic distance \(d\ge3\), the two radius-one observed configurations again have no boundary vertex with just one unobserved neighbor: each observed nonseed vertex has two unobserved neighbors, and each seed has none. This can be checked directly on four types: the two horizontal neighbors of \(u_0\), the partner \(v_0\), the two horizontal neighbors of \(v_d\), and the partner \(u_d\); the cyclic distance threshold guarantees that none of the two unobserved neighbors belongs to the other seed's closed neighborhood. (At the maximal even-cycle separation the same statement remains valid.) Therefore no forcing can start, so these pairs fail. This proves the classification.

**Counting.** For \(n=4,5,6\), there are respectively \(6,10,15\) unordered same-rim pairs per rim with distance at most three, and respectively \(4,5,5\) cross-row choices for each \(u_i\). The totals are \(2\cdot6+4\cdot4=28\), \(2\cdot10+5\cdot5=45\), and \(2\cdot15+6\cdot5=60\). For every \(n\ge7\), each rim contains exactly \(3n\) unordered pairs of cyclic distance one, two, or three, and each of the \(n\) vertices \(u_i\) admits five cross-row partners, yielding \(2(3n)+5n=11n\). This finishes the proof.

## Verification
The standalone `verify.py` constructs the original graph and simulates closed-neighborhood monitoring followed by successive unique-neighbor propagation. It exhaustively classifies every singleton and unordered vertex pair for all \(3\le n\le60\), independently comparing the observed successful sets to the above cyclic-distance predicate and the exact counts. These finite checks support, but do not replace, the infinite proof.

## Relationship to prior work
Anitha and Rajasingh (2020, Theorem 3.4) proved that the circular ladder's power-domination number is two for \(n\ge4\), using one construction. That numerical value is **not** claimed as new. Their available full text does not classify or enumerate all attaining pairs. Bläsius, Göttlicher and Schirneck (arXiv:2610.24214v1, October 16, 2026) study the general enumeration of minimal power-dominating sets by implicit hitting sets; the accessible abstract does not state a formula for circular ladders. The present theorem gives the complete labelled first nonzero coefficient for this infinite family, with a local necessary-and-sufficient distance criterion.

## Limitations
This counts minimum sets, not all inclusion-minimal power-dominating sets or all coefficients of the power-domination polynomial. It concerns the two-row Cartesian cycle prism only, not higher-width cylindrical grids, Möbius ladders or arbitrary cubic graphs. Historical priority beyond the inspected literature remains provisional; the 2026 algorithm paper's complete primary text was not available to inspect. Independent audit has not been performed.

## References
1. J. Anitha and Indra Rajasingh, *Power Domination in Tree Derived Architectures*, Journal of Combinatorial Mathematics and Combinatorial Computing 112 (2020), 53–63, Theorem 3.4. Full public text: https://www.researchgate.net/publication/342096271_Power_Domination_in_Tree_Derived_Architectures ; journal: https://combinatorialpress.com/jcmcc-articles/volume-112/power-domination-in-tree-derived-architectures/.
2. Thomas Bläsius, Max Göttlicher and Martin Schirneck, *Implicit Hitting Set Enumeration for Power Dominating Sets*, arXiv:2610.24214v1, first posted October 16, 2026. https://arxiv.org/abs/2610.24214.
3. Boris Brimkov, Rutvik Patel, Varun Suriyanarayana and Alexander Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1, May 28, 2018. https://arxiv.org/abs/1805.10984.
