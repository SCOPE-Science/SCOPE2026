# Sharp retractional constants for finite Cartesian products of trees

## Finding
Let \(d\ge 1\), and let \(T_1,\ldots,T_d\) be finite trees, each with at least two vertices and every edge of length one. Endow the Cartesian graph product \(G=T_1\square\cdots\square T_d\) with its shortest-path metric, namely \(\operatorname{dist}_G(x,y)=\sum_{i=1}^d\operatorname{dist}_{T_i}(x_i,y_i)\). Fix arbitrary roots \(o_i\in T_i\) and put \(o=(o_1,\ldots,o_d)\).

For any enumeration \(o=v_0,v_1,\ldots,v_{N-1}\) of the vertices, consider retractions \(R_k:G\to \{v_0,\ldots,v_k\}\) fixing their targets, with \(R_kR_j=R_jR_k=R_{\min(k,j)}\) for all indices. Define \(\kappa(G,o)\) as the minimum, over all such enumerations and systems, of \(\max_{0\le k<N}\operatorname{Lip}(R_k)\). Then
\[
\boxed{\kappa(G,o)=\begin{cases}1,&d=1\text{ or }d=2,\\2,&d\ge 3.\end{cases}}
\]
The optimum is independent of the chosen roots and the orders of the trees. In particular, adding a third nontrivial tree factor destroys the existence of any commuting nonexpansive one-vertex-at-a-time retraction filtration, while a uniform sharp constant two always suffices.

The induced real Lipschitz-free-space projections have the same operator norms as the underlying retractions. No claim is made about optimality among arbitrary linear bases not induced by retractions.

## Assumptions and scope
A rooted tree is supplied with any linear order in which each parent precedes all its descendants. The associated product order is lexicographic. For a finite rooted tree and an ancestor-closed set \(Q\) containing the root, write \(\pi_Q(a)\) for the last ancestor of \(a\) belonging to \(Q\). On graph vertices, \(\pi_Q\) is nonexpansive: on each edge, its images coincide or are adjacent. All distances in the theorem are integral. Singleton tree factors may be omitted; the statement concerns at least one nontrivial factor.

## Proof
**One factor.** Order the tree parent-before-descendants. On adding a vertex \(v\), fold it to its parent while fixing earlier vertices. For every earlier vertex \(w\), the path from \(v\) to \(w\) traverses its parent: \(d(p(v),w)=d(v,w)-1\). The elementary fold is nonexpansive. Composing the folds backward produces commuting prefix retractions, all nonexpansive.

**Two factors.** Order \(T\times S\) lexicographically, with parent-before-descendant orders in both coordinates. For the vertex \(v=(a,b)\) being added after its predecessors, choose an earlier target \(p(v)\) by
\[
p(v)=\begin{cases}(p_T(a),p_S(b)),&a\ne o_T,\ b\ne o_S,\\ (p_T(a),b),&a\ne o_T,\ b=o_S,\\ (a,p_S(b)),&a=o_T,\ b\ne o_S.\end{cases}
\]
Here \(p_T\) and \(p_S\) are tree parents. If a predecessor \(w=(a',b')\) has \(a'\) earlier than \(a\), the first-coordinate distance drops by one when passing from \(v\) to \(p(v)\); a parent step in the second coordinate increases its distance by at most one. If \(a'=a\), necessarily \(b'\) is earlier than \(b\); its distance from \(p_S(b)\) drops by one, exactly compensating for the first-coordinate parent step. The root-coordinate cases are simpler. Thus \(d(p(v),w)\le d(v,w)\) for every earlier \(w\), so the one-point fold on the current prefix is nonexpansive. Their backward compositions are therefore commuting nonexpansive retractions. Since the full identity has Lipschitz norm one, the optimum is exactly one for one or two factors.

**At most two for arbitrarily many factors.** Induct on \(d\). Write \(G=T\square H\), where \(T=T_1\) and \(H=T_2\square\cdots\square T_d\). Use a rooted ancestor order on \(T\), and, within each \(T\)-row, the same enumeration of \(H\) obtained inductively; order the rows lexicographically. When the first row, corresponding to the root of \(T\), is partial, apply the corresponding prefix retraction on \(H\) and set the first coordinate to the root. By induction this is at most two-Lipschitz (at most one if \(H\) has at most two factors).

Now suppose the current row is a nonroot vertex \(a_0\in T\). Let \(Q\) be the ancestor-closed set of earlier, fully included rows, and let \(U\subseteq H\) be the current row's initial segment. For each \(b\in H\), set \(Q_b=Q\cup\{a_0\}\) if \(b\in U\), and \(Q_b=Q\) otherwise. Define
\[
R(a,b)=(\pi_{Q_b}(a),b).
\]
The displayed map fixes exactly \((Q\times H)\cup(\{a_0\}\times U)\) and is a retraction onto that prefix. If \(a,a'\) are adjacent in \(T\), their projected first coordinates are adjacent or equal, because both use the same \(Q_b\); their other coordinates agree. If \(b,b'\) are adjacent in \(H\), their output second coordinates remain adjacent and \(Q_b\) and \(Q_{b'}\) differ at most by the one vertex \(a_0\). Accordingly \(\pi_{Q_b}(a)\) and \(\pi_{Q_{b'}}(a)\) are equal or adjacent, so their images are at distance at most two. Every edge of the graph product changes exactly one coordinate; shortest-path decomposition therefore gives \(\operatorname{Lip}(R)\le2\) on the whole product.

For commutativity, in a nonroot row give each newly inserted \((a,b)\) the predecessor \((p_T(a),b)\); in the first row use the predecessor specified by the inductive construction on \(H\). Every predecessor lies in the preceding prefix. Applying these elementary one-point folds backward from the full product gives precisely the maps just described: later rows are pushed to their deepest previously included ancestor, retaining \(b\); a partial root row instead uses the inductive map of \(H\). Backward fold compositions satisfy \(R_kR_j=R_{\min(k,j)}\) and their reverse compositions do too, since each fixes its prefix. This completes the sharp uniform two-Lipschitz construction.

**Three-factor obstruction.** Assume \(d\ge3\). For any vertex \(v\), select neighbors \(w_1,w_2,w_3\) differing from \(v\) in three distinct tree coordinates. The intersection of the radius-one closed balls about \(w_1,w_2,w_3\) is exactly \(\{v\}\). Indeed, a vertex within one unit of both \(w_1\) and \(w_2\) is either \(v\) or their opposite square corner, and the latter lies at distance three from \(w_3\). Let \(v\) be the last vertex of any purported prefix enumeration. The penultimate retraction fixes all its neighbors but must map \(v\) to a different vertex \(p\). If its Lipschitz constant were less than two, each unit edge \(vw_i\) would satisfy \(d(p,w_i)<2\). Integrality would force \(d(p,w_i)\le1\) for all three indices, contradicting the intersection property. Thus every system has a retraction of Lipschitz norm at least two. Together with the construction this proves the theorem.

## Verification
The proof is uniform in all finite tree sizes and degrees. The included standalone script `tree_product_check.py` constructs the stated predecessor maps, computes all resulting prefix retractions, and checks their Lipschitz norms directly on representative products of paths and stars with one through four factors. The finite checks support, but do not replace, the proofs for arbitrary tree products. All lower bounds come from the penultimate retraction, not from incomplete finite enumeration.

## Relationship to prior work
Novotný's 2019 study develops retractional Schauder bases and proves lower bounds for a distinct family of graph circles with a distant added basepoint [1, Corollary 2 and Theorem 5]. Hájek and Medina prove existence of retractional bases for nets and specified grids, with generally larger nonsharp bounds, without this precise finite tree-product dimensional threshold [2, Definition 1.2, Theorems 2.6 and 3.9]. A previous exact theorem for full Hamming products gives the constants one for the binary square and two for binary cubes of dimension at least three, but it does not cover products of branching trees or longer tree paths. The present proof gives sharp constants for *all* products of unit-edge trees and establishes the two-factor case by an explicit diagonal fold. The graph-theoretic literature on metric retractions and median products studies related existence questions but does not, in the inspected sources, supply the complete commuting one-vertex filtration constants [3].

## Limitations
The edge-length-one hypothesis is essential to the given proof; arbitrary weighted trees are not classified. The assertion is about retraction-induced projections, not arbitrary linear projections. The originality comparison covered the two primary retractional-basis papers and targeted searches; older or unindexed graph-folding literature may contain equivalent formulations and remains a bibliographic risk. No independent validation or publication review has occurred.

## References
[1] M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, first posted 2019-05-30. https://arxiv.org/abs/1905.13188

[2] P. Hájek and R. Medina, *Schauder bases in Lipschitz free spaces over nets in Banach spaces*, arXiv:2112.03095, first posted 2021-12-06. https://arxiv.org/abs/2112.03095

[3] H.-J. Bandelt and V. Chepoi, *Metric graph theory and geometry: a survey*, 2008 survey (graph-metric retractions and products). https://pageperso.lis-lab.fr/~victor.chepoi/survey_cm_bis.pdf
