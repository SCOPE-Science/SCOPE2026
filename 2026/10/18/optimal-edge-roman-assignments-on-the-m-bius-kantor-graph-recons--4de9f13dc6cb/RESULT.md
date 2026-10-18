# Optimal edge Roman assignments on the Möbius–Kantor graph reconstruct a subdivided line graph

## Finding

Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph. The edge Roman domination number is
\[
\gamma'_R(M)=11.
\]
There are exactly \(72\) minimum-weight edge Roman dominating functions, each with five edges labeled \(2\), one edge labeled \(1\), and eighteen edges labeled \(0\).

Define the **double-guard exchange graph** \(X(M)\) as follows. Its vertices are these \(72\) optimal functions. Two distinct functions are adjacent precisely when their sets of edges labeled \(2\) differ by the removal of one edge and addition of one edge. The edge labeled \(1\) is not independently constrained to remain fixed: it is the uniquely necessary single guard once the new double-guard locations are chosen. Then
\[
\boxed{X(M)\cong S(L(M)),}
\]
where \(L(M)\) is the ordinary line graph of \(M\) and \(S\) subdivides **each** edge once. In particular, \(X(M)\) is connected, has \(72\) vertices and \(96\) edges, and has degree distribution \(4^{24}2^{48}\). Every vertex has eccentricity \(8\), so
\[
\boxed{\operatorname{rad}(X(M))=\operatorname{diam}(X(M))=8.}
\]
The subdivision statement is an isomorphism of abstract graphs, **not** an assertion that a naturally selected single-guard edge indexes the corresponding vertex of the line graph.

## Assumptions and scope

The graph \(M\) has vertices \(u_i,v_i\) for \(i\in\{0,\ldots,7\}\), with indices modulo \(8\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\) for all \(i\). It is a simple cubic graph with \(16\) vertices and \(24\) edges.

An **edge Roman dominating function** is \(f:E(M)\to\{0,1,2\}\) such that every edge labeled \(0\) shares an endpoint with at least one edge labeled \(2\). Its weight is \(\sum_{e\in E(M)}f(e)\). The edge Roman domination number is the minimum such weight. All edge sets and state labels refer to the fixed, explicitly enumerated graph; no infinite-family statement is asserted.

For any set \(T\subseteq E(M)\), denote by \(U(T)\) the set of edges disjoint from **every** edge of \(T\). Equivalently, both endpoints of any member of \(U(T)\) are outside the set of endpoints of \(T\). The word “exchange” refers only to replacing a single element of \(T=f^{-1}(2)\) and recomputing the forced \(1\)-labels, not to a permitted step of the classical single-coordinate relabeling model.

## Proof

**Canonical completion.** Fix the set \(T=f^{-1}(2)\). Every edge in \(U(T)\) must be labeled \(1\), because labeling it \(0\) violates Roman domination and it was stipulated not to have label \(2\). Any edge outside \(T\cup U(T)\) can be labeled \(0\). Therefore the least possible weight among functions having \(T\) as their exact label-\(2\) support is
\[
\Phi(T)=2|T|+|U(T)|.
\]
Any minimum-weight global function must use this canonical completion, since an extra \(1\) can be changed to \(0\) to reduce weight.

**Exhaustive finite minimum.** If \(|T|\ge6\), then \(\Phi(T)\ge12\). The independent verifiers enumerate all \(\sum_{k=0}^{5}\binom{24}{k}=55,455\) choices \(|T|\le5\) using two representations of \(M\), independently computing \(U(T)\) by (i) closed edge-neighborhood masks and (ii) the endpoints of selected edges. The smallest value found is \(11\), attained by exactly \(72\) supports and by no other supports with weight at most \(11\). Every one has \(|T|=5\) and \(|U(T)|=1\). Combining the \(|T|\ge6\) bound with this complete finite enumeration proves the minimum and state count, not merely an experimental lower bound.

**Reconfiguration construction.** From each of the \(72\) five-edge supports, replace each chosen edge in turn by each of the other \(19\) edges, retain the replacement if its canonical completion still has weight \(11\), and identify duplicate unordered pairs. The independent verifiers obtain precisely \(96\) exchanges. Their vertex degrees are \(4\) on \(24\) states and \(2\) on \(48\) states. Every degree-\(2\) state has two degree-\(4\) neighbors, and each degree-\(4\) state has four degree-\(2\) neighbors.

**Subdivision identification.** Contract each degree-\(2\) state to an edge joining its two degree-\(4\) neighbors. The included finite certificate gives a complete bijection from the \(24\) degree-\(4\) states to the \(24\) edges of \(M\). The verifier checks, for all \(48\) degree-\(2\) states, that their neighbor pairs map bijectively onto the \(48\) unordered pairs of incident edges of \(M\). These are exactly the edges of \(L(M)\). Thus the exchange graph is \(S(L(M))\), with no appeal to a visual resemblance or an unverified graph-isomorphism oracle.

**Distances.** Breadth-first search from each of the \(72\) configurations in the explicitly reconstructed exchange graph visits every configuration and returns eccentricity \(8\). The certificate also contains a length-\(8\) path between two configurations, and the verifier confirms its consecutive edges and the all-source breadth-first-search bound. The radius and diameter therefore both equal \(8\).

## Verification

The complete bounded enumeration, canonical labeling, \(96\) transitions, graph-isomorphism bijection and diameter checks are independently replayable with Python 3.10+ standard library only. Run `python verify_gp.py` and `python verify_lcf.py` from the directory containing `CERTIFICATE.json`. They reconstruct \(M\) respectively from the generalized-Petersen model and the independent LCF \([5,-5]^8\) model, verify the provided vertex-model isomorphism, and check the same finite claim with distinct enumeration logic.

`CERTIFICATE.json` lists the ordered original edges, all \(72\) labelings, all \(96\) reconfiguration edges, a complete \(24\)-entry branch-to-line-graph bijection, an isomorphism between the two representations of \(M\), and an explicit distance-\(8\) witness. The certificate is checked against independently generated graphs rather than taken as the truth of the result.

## Relationship to prior work

Pushpam and Mai introduced edge Roman domination in 2009. Chang, Chen and Liu studied the parameter systematically and established general upper bounds for connected graphs and subcubic graphs. In particular, their results do not specify all minimum functions of \(\operatorname{GP}(8,3)\) or the exchange graph defined here. Their observation that edge Roman domination is Roman domination on the line graph concerns the **input optimization problem**; it is distinct from the present, independently checked conclusion that the graph **of optimal configurations** is a subdivision of that line graph.

Samodivkin's later framework for reconfiguration graphs of ordinary (vertex) Roman dominating functions includes swaps that fix the label-\(1\) set or exchange a \(1\) with a \(2\). The rule in this theorem instead exchanges one edge carrying label \(2\) and recomputes its uniquely forced \(1\)-edge. In the present case, none of the \(96\) accepted exchanges preserves the label-\(1\) edge. The abstract framework and results for paths, cycles, and disjoint unions do not imply the present configuration classification.

## Limitations

This is an exact finite-graph theorem, not a claimed formula for generalized Petersen graphs as a family. Its structural isomorphism relies on the explicitly checked bijection; a canonical geometry-only bijection is not claimed. The exchange rule should not be conflated with Roman-function models that allow only a single label swap while holding the remaining labels fixed. The accessible research literature was checked for the same special graph, parameter, alternative formulations and stronger claims, but unindexed papers and tables might contain equivalent results. No assertion of independent validation is made.

## References

1. G. J. Chang, S.-H. Chen and C.-H. Liu, “Edge Roman domination on graphs,” arXiv:1405.5622, first publicly posted 2014-05-22; later *Graphs and Combinatorics* **32** (2016), 1731–1747. https://arxiv.org/abs/1405.5622
2. P. Roushini Leely Pushpam and T. N. M. Malini Mai, “Edge roman domination in graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **69** (2009), 175–182. Bibliographic listing: https://combinatorialpress.com/jcmcc/vol69/
3. V. Samodivkin, “Roman domination: changing, unchanging, \(\gamma_R\)-graphs,” arXiv:1709.05052, first posted 2017-09-15. https://arxiv.org/abs/1709.05052
4. E. W. Weisstein, “Möbius–Kantor Graph,” *MathWorld*; graph representations \(\operatorname{GP}(8,3)\) and LCF \([5,-5]^8\). https://mathworld.wolfram.com/Moebius-KantorGraph.html
