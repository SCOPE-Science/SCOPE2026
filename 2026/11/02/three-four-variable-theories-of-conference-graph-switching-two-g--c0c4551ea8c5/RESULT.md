# Three four-variable theories of conference-graph switching two-graphs with sharp deletion tolerance

## Finding
Let \(G\) be any finite conference graph on \(v\ge5\) vertices, meaning a strongly regular graph with parameters
\[\left(v,\frac{v-1}{2},\frac{v-5}{4},\frac{v-1}{4}\right).\]
Put \(s_{ab}=1\) for adjacent distinct vertices and \(s_{ab}=-1\) for nonadjacent distinct vertices. Define a ternary relation on its vertices by
\[R(a,b,c)\ \Longleftrightarrow\ a,b,c\text{ are pairwise distinct and }s_{ab}s_{ac}s_{bc}=1.\]
Denote the resulting one-sorted structure by \(\mathcal T(G)\). All logic below is ordinary first-order logic with equality and just this ternary relation, without counting quantifiers.

**Theorem.** (i) Every two conference-graph structures \(\mathcal T(G)\) are equivalent in unrestricted-depth three-variable logic \(\mathrm{FO}^{3}\).

(ii) There are exactly three unrestricted-depth four-variable theories \(\mathrm{FO}^{4}\), indexed by the conference-graph order \(v=5\), \(v=9\), or \(v\ge13\). In particular all conference graphs of orders at least \(13\), including nonisomorphic examples, have the same \(\mathrm{FO}^{4}\) theory. Quantifier rank four already distinguishes the three theories, while rank at most three does not. The least representatives have \(5\), \(9\), and \(13\) elements; hence the sharp uniform least-representative bound is \(13\).

(iii) For every \(v\ge13\), deletion of **any** set of at most \((v-13)/4\) vertices leaves a structure \(\mathrm{FO}^{4}\)-equivalent to \(\mathcal T(G)\). This cutoff is sharp: a set of exactly \((v-9)/4\) vertices can be deleted so that the reduct is no longer \(\mathrm{FO}^{4}\)-equivalent.

The exact local invariant underlying (ii) and (iii) is as follows. For three distinct anchors \(a,b,c\), write \(\tau=s_{ab}s_{ac}s_{bc}\), and fix \(\epsilon_{ab},\epsilon_{ac},\epsilon_{bc}\in\{\pm1\}\) with \(\epsilon_{ab}\epsilon_{ac}\epsilon_{bc}=\tau\). The number \(N_G\) of vertices \(x\notin\{a,b,c\}\) satisfying \(s_{ab}s_{ax}s_{bx}=\epsilon_{ab}\), \(s_{ac}s_{ax}s_{cx}=\epsilon_{ac}\), and \(s_{bc}s_{bx}s_{cx}=\epsilon_{bc}\) is
\[\boxed{N_G=\frac{v-3-\sum_{e\in\{ab,ac,bc\}}(s_e+\tau)\epsilon_e}{4}.}\]
For \(v\ge9\), its minimum over all triples and compatible sign requests is exactly \((v-9)/4\).

## Assumptions and scope
A conference graph is simple, undirected and satisfies the displayed strongly regular parameters. These parameters force \(v\equiv1\pmod4\); no assumption of vertex transitivity, Paley construction, or prime-power order is made. The relation is the **odd-edge-parity two-graph relation**: a triple has \(R\) precisely when it spans an odd number of edges. It is invariant under Seidel switching. A compatible request is one obeying the necessary four-point even-parity identity; an incompatible request has no possible realization in *any* graph-derived two-graph.

An induced reduct means restricting the universe and the same ternary relation, without adding order, adjacency, or graph-representative symbols. \(\mathrm{FO}^{k}\)-equivalence means agreement on every sentence with at most \(k\) variable names, reused arbitrarily often, without any depth bound.

## Proof
**1. The signed-matrix identity.** Let \(S\) have zero diagonal and \(S_{ab}=s_{ab}\) off diagonal. For any two distinct vertices, strong regularity gives \(\sum_{x\notin\{a,b\}}s_{ax}s_{bx}=-1\): for adjacent \(a,b\), the common-neighbor, common-nonneighbor and mixed counts obtained from \(\lambda=(v-5)/4\) give the same answer as for nonadjacent \(a,b\), where \(\mu=(v-1)/4\). Consequently
\[S^2=vI-J.\]
For a fixed pair \(a,b\), the two possible values of \(\tau_{abx}=s_{ab}s_{ax}s_{bx}\) are each attained: summing gives \(\sum_{x\notin\{a,b\}}\tau_{abx}=-s_{ab}\), so their counts are \((v-2-s_{ab})/2\) and \((v-2+s_{ab})/2\), both positive for \(v\ge5\). Every point also has a distinct companion. This proves the needed one-point extensions over zero, one or two anchors.

**2. Exact three-anchor count.** For distinct anchors \(a,b,c\), set \(\tau=s_{ab}s_{ac}s_{bc}\). Four-point parity forces \(\epsilon_{ab}\epsilon_{ac}\epsilon_{bc}=\tau\). Conversely this condition allows signs \(t_a,t_b,t_c\in\{\pm1\}\) with \(\epsilon_{ab}=s_{ab}t_at_b\), etc. An outside vertex realizes the request exactly when its three signs \((s_{ax},s_{bx},s_{cx})\) equal \((t_a,t_b,t_c)\) or its global negative. The indicator of that two-element sign-pair is
\[\frac{1+t_at_bs_{ax}s_{bx}+t_at_cs_{ax}s_{cx}+t_bt_cs_{bx}s_{cx}}4.\]
By Step 1, \(\sum_{x\notin\{a,b,c\}}s_{ax}s_{bx}=-1-s_{ac}s_{bc}\), and similarly for the other pairs. Since \(t_at_b=\epsilon_{ab}s_{ab}\), this yields the boxed exact formula. Each summand \((s_e+\tau)\epsilon_e\) is at most \(2\), giving
\[N_G\ge\frac{v-9}{4}.\]
For \(v\ge9\), \(\lambda=(v-5)/4\ge1\), so some triangle \(a,b,c\) has all three edges. For that triple, \(s_e=\tau=1\); taking all three requested signs equal to \(1\) gives equality. Thus the minimum is **exactly** \((v-9)/4\) at every admissible order \(v\ge9\).

**3. Unbounded-depth pebble equivalence.** In the three-pebble game, a move leaves at most two distinct fixed anchors. Step 1 supplies every permissible third-vertex relation on the other side, preserving equality and all values of \(R\) on occupied triples. Duplicator therefore wins any number of rounds, proving (i). In a four-pebble game, a move leaves at most three distinct anchors. For \(v\ge13\), Step 2 supplies each compatible one-point extension over three anchors; steps for fewer anchors follow from Step 1. Duplicator's maintained partial isomorphism is thus extendible for arbitrarily many rounds, giving the common unrestricted \(\mathrm{FO}^{4}\) theory.

**4. Small orders and exact separation.** For \(v=5\), the conference graph is the five-cycle. Each four-element induced subgraph is a four-vertex path; it has two, not four, triples of odd edge-parity. Consequently the rank-four sentence requiring four distinct vertices with \(R\) on *each* of their four triples is false.

For \(v=9\), the strongly regular parameters are \((9,4,1,2)\); there is just one such graph, the three-by-three rook graph. To see this, every edge lies in exactly one triangle and every vertex in exactly two triangles. Make an auxiliary graph whose six vertices are these triangles and whose nine edges are the original vertices, each joining its two triangles. Distinct original triangles share at most one vertex, so this is a simple cubic six-vertex graph. It is triangle-free, since a three-cycle would create two distinct triangles of the original graph on an edge. The only triangle-free cubic graph on six vertices is \(K_{3,3}\), whose line graph is the rook graph. The rook graph has an induced disjoint union of two edges, and all four triples of such a set have odd edge-parity. Thus the rank-four all-positive-four-set sentence is true for \(v=9\), and by Step 2 also for \(v\ge13\).

Still for \(v=9\), select a triangle \(a,b,c\). The all-positive fourth-point request has exactly \((9-9)/4=0\) witnesses, whereas every positive triple for \(v\ge13\) has an all-positive fourth-point witness by Step 2. Therefore the rank-four sentence
\[\exists a\exists b\exists c\bigl(\text{distinct}(a,b,c)\land R(a,b,c)\land\neg\exists d\,(\text{distinct}(d,a,b,c)\land R(a,b,d)\land R(a,c,d)\land R(b,c,d))\bigr)\]
is true for \(v=9\) and false for \(v\ge13\). All three possible orders exist: the Paley graphs of orders \(5\), \(9\), \(13\). No rank at most three can distinguish them because three-pebble equivalence implies agreement on all sentences of rank at most three. Thus (ii), including the sharp representative bound, follows.

**5. Exact deletion threshold.** Let \(v\ge13\) and \(w=(v-9)/4\). Every compatible three-anchor extension request has at least \(w\) witnesses in the original structure. Deleting at most \(w-1=(v-13)/4\) vertices leaves at least one witness for every request whose anchors survive, and also preserves the one- or two-anchor extension property. The four-pebble back-and-forth argument of Step 3 still applies to the reduct. Conversely choose a graph triangle and delete precisely the \(w\) vertices realizing its all-positive fourth-point request. The three anchors survive; the displayed rank-four sentence becomes true in the reduct, though it is false in the original. Hence no larger uniform deletion guarantee holds, proving (iii).

## Verification
The reproducible standard-library program `verify_conference_reduct.py` directly constructs Paley conference graphs over the prime fields of sizes \(5,13,17,29\) and extension fields of sizes \(9,25\). It checks the conference-matrix identity, **every** compatible request over all three-element sets against the exact formula, the minimum witness count, the two rank-four separating configurations, and sharp deletion at orders at least \(13\). Its recorded output is `verify_conference_reduct_output.txt`. The checked counts of compatible extensions are \(40,336,1144,2720,9200,14616\), respectively, and all tests pass. The infinite and non-Paley cases rest on Steps 1–5, not on finite experiments.

## Relationship to prior work
Two-graphs, switching equivalence and Seidel matrices are classical; Seidel's 1976 survey is an important historical source. Hoffman and Solazzo's *Complex Two-Graphs via Equiangular Tight Frames* (arXiv:1408.0334, 2014) discusses the correspondence of ordinary two-graphs to switching classes and their generalized frame analogues. Macpherson's *A survey of homogeneous structures* discusses the homogeneous countable two-graph and related first-order homogeneity, but does not state the present finite conference-graph classification or deletion threshold in the inspected text. Existing four-existential-closure results for Paley **graphs** refer to the binary adjacency signature and do not supply these sharp two-graph extension counts or the classification for arbitrary conference graphs.

## Limitations
The assumption of a conference graph is essential; no claim is made for arbitrary switching two-graphs or arbitrary strongly regular graphs. The deletion threshold refers to the reduct in the **ternary two-graph language**, not persistence of conference-graph parameters after deletion. No statement is made for counting logic, five or more variables, or signatures also naming graph adjacency. Searches of known literature and comparison with accessible full texts do not establish exhaustive historical priority: a stronger classical result about two-graph configurations might imply portions of this theorem. The paper by Seidel (1976) was accessible bibliographically but its complete contents were not retrieved.

## References
1. J. J. Seidel, *A survey of two-graphs*, Atti Convegno Internazionale Teorie Combinatorie (1976), pp. 481–511. https://research.tue.nl/en/publications/a-survey-of-two-graphs/
2. T. R. Hoffman and J. P. Solazzo, *Complex Two-Graphs via Equiangular Tight Frames*, arXiv:1408.0334, first public preprint August 2, 2014. https://arxiv.org/abs/1408.0334
3. D. Macpherson, *A survey of homogeneous structures*, Discrete Mathematics 311 (2011), 1599–1634. https://paperzz.com/doc/9426993/a-survey-of-homogeneous-structures
4. SageMath combinatorics documentation, *Two-graphs*: standard correspondence between odd-edge-parity triple systems and Seidel switching classes. https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/designs/twographs.html
