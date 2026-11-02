# Connected regular exchange and slide graphs on minimum total dominating sets of triangular graphs

## Finding

For every integer \(q\ge1\), let \(n=3q+1\) and let \(T_n=J(n,2)=L(K_n)\) be the triangular graph. Its vertices correspond to the edges of \(K_n\), with adjacency exactly when those edges share a ground vertex. A *total dominating set* \(S\) meets the open neighborhood of every vertex, including every selected vertex.

Write \(\mathcal R_{\mathrm E}(T_n)\) for the reconfiguration graph on **minimum-cardinality** total dominating sets, with adjacency when precisely one selected vertex is exchanged. Let \(\mathcal R_{\mathrm S}(T_n)\) restrict an exchange to adjacent old and new vertices of \(T_n\). Put
\[
N=\frac{n!}{2^q q!}.
\]
**Theorem.** Both reconfiguration graphs are connected and vertex-transitive on exactly \(N\) configurations. The exchange graph is \(6q\)-regular and has \(3qN\) edges. The slide graph is \(4q\)-regular and has \(2qN\) edges. The \(qN\) exchange edges absent from the slide graph correspond to one specific nonincident replacement per selected original edge.

The previously established minimum-set characterization and count are recalled in the proof and are **not claimed as new**. The result here concerns all allowed single replacements, the two degrees, and connectivity under the more restrictive slide rule.

## Assumptions and scope

All graphs are finite, simple, undirected. The ground set of \(K_n\) is labeled \([n]\); selected vertices of \(T_n\) are thus identified with selected edges of \(K_n\). The theorem covers precisely \(n\equiv1\pmod 3\), with \(n\ge4\); it does not assert anything about the other congruence classes. Exchange and slide steps preserve the number \(\gamma_t(T_n)\) of selected vertices and must preserve total domination after each step.

A three-vertex path \(a-b-c\) denotes the selected ground edges \(ab\) and \(bc\), with center \(b\). A configuration of \(q\) disjoint paths and one isolated ground vertex has \(2q\) selected edges.

## Proof

**1. Criterion and optimal structure.** Regard any set \(S\subseteq E(K_n)\) as a spanning subgraph \(H=([n],S)\). Total domination in \(L(K_n)\) requires every original edge to intersect a *different selected edge*. Therefore, \(S\) is total dominating if and only if (i) at most one ground vertex is isolated in \(H\), and (ii) no connected component of \(H\) is a single selected edge on two vertices. Indeed, two isolated ground vertices give their connecting edge no selected neighbor, and a single-edge component gives that selected edge none. Conversely, every unselected original edge has an endpoint incident with a selected edge when there is at most one ground isolate; any selected edge has a different neighboring selected edge unless it is a two-vertex component.

Let \(s\le1\) be the number of isolates and \(r\) the number of nontrivial connected components of \(H\). Each such component contains at least three vertices, so \(r\le\lfloor(n-s)/3\rfloor\), and the forest bound gives \(|S|\ge(n-s)-r\). For \(n=3q+1\), when \(s=0\), this is at least \(2q+1\); when \(s=1\), it is at least \(2q\). Equality at \(2q\) forces \(s=1\), exactly \(q\) three-vertex components, each with two edges, hence disjoint paths \(P_3\). Such a configuration meets the criterion. Thus \(\gamma_t(T_n)=2q\), and its entire family of minimum sets is the already recorded family of one isolate and \(q\) disjoint \(P_3\)'s [1]. Selecting the isolate, partitioning the remaining labels into unordered triples, and selecting one of three centers per triple gives exactly \(N=n!/(2^q q!)\) configurations, agreeing with [1].

**2. All neighboring minimum sets.** Fix one configuration, choose one of its \(2q\) selected edges \(ab\) in a path \(a-b-c\), and let \(u\) be the unique ground isolate. Removing \(ab\) leaves the selected edge \(bc\), the two ground isolates \(a,u\), and all other intact paths. For the replacement to yield again one isolate and disjoint \(P_3\)'s, the added edge must use one endpoint from \(\{a,u\}\) and one endpoint from \(\{b,c\}\). The four possibilities are \(ab,ac,ub,uc\). The first is the deleted original edge, so there are exactly three admissible exchanges:
\[
 ab\longrightarrow ac,\qquad ab\longrightarrow ub,\qquad ab\longrightarrow uc.
\]
Among them, \(ac\) and \(ub\) intersect \(ab\), while \(uc\) does not. No edge involving another path can work, since the resulting component-size profile would not be one isolate together with \(q\) three-vertex paths. Exchanged pairs have a uniquely determined deleted edge, so no neighbors are double-counted. Therefore the exchange degree is \(3(2q)=6q\) and the slide degree is \(2(2q)=4q\).

**3. Connectivity of the slide graph.** Within any one path \(a-b-c\), the slide \(ab\mapsto ac\) changes the center from \(b\) to \(c\) without changing the triple or the isolated vertex. Repeating such moves permits any desired center in every triple. If the isolated ground vertex is \(u\), and \(a\) is a leaf of some path \(a-b-c\), then the slide \(ab\mapsto ub\) replaces that leaf with \(u\) and makes \(a\) the new isolate, leaving the center \(b\) fixed. By first changing the center, any chosen vertex \(v\) in any triple can be made a leaf. Thus, disregarding center choices, the permitted slide steps implement a transposition of the isolated label with **any other label**, while retaining a partition into triples.

The transpositions exchanging the current isolated label with one arbitrary label generate every permutation of the ground labels: in particular a transposition of two non-isolated labels is the composition of three transpositions through the isolate. Equivalently, in a sequence of rooted triple partitions, swaps with the singleton can transform any allocation of labels to the triple blocks into any other. After realizing the desired partition, use the internal-center slides to match the desired centers. Hence \(\mathcal R_{\mathrm S}(T_n)\) is connected. Since \(\mathcal R_{\mathrm S}\) is a spanning subgraph of \(\mathcal R_{\mathrm E}\), the exchange graph is connected as well.

**4. Symmetry and sizes.** Every permutation of \([n]\) induces an automorphism of both reconfiguration graphs. The minimum configurations are precisely rooted partitions into one singleton and \(q\) unordered triples with one center designated in each triple, so \(S_n\) acts transitively. Both graphs are therefore vertex-transitive. The handshake lemma gives \(|E(\mathcal R_{\mathrm E})|=6qN/2=3qN\) and \(|E(\mathcal R_{\mathrm S})|=4qN/2=2qN\). Their edge-count difference is \(qN\), as asserted.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It constructs \(J(n,2)\) directly from pair intersections, evaluates the original open-neighborhood total domination test, exhaustively enumerates all candidate \(2q\)-sets and their valid single replacements for \(n=4\) and \(n=7\), and checks both degree distributions, connected components, vertex counts, and edge counts. It independently checks all valid one-edge replacements of an explicit optimum for \(n=10,13,16\). Run `python3 verify.py`. The expected final marker is `VERIFY_OK`. These computations are corroboration; the four proof steps establish the statement for all \(q\ge1\).

## Relationship to prior work

The 2018 OEIS A304561 entry by Weisstein and Howroyd [1] explicitly characterizes and counts minimum total dominating sets of triangular graphs, including the one-isolate/path-partition structure for \(n\equiv1\pmod3\). Accordingly, neither the count \(N\), the scalar minimum, nor the minimum-family description is claimed as new here. Alikhani, Fatehi, and Mynhardt [2] introduced addition/deletion reconfiguration graphs of total dominating sets of size at most a threshold; that adjacency is different from fixed-cardinality exchanges or slides. Mynhardt and Nasserasr [3] survey jump/slide reconfiguration for domination and distinguish it from addition/deletion models; the inspected material does not state the two triangular-graph total-domination reconfiguration structures established here.

The new contribution is the complete local move classification, both regular degrees, their precise edge-count separation, and connectivity despite restricting to slides. Direct implication from the earlier minimum-set count would be unwarranted: cardinality alone contains no information about one-step feasibility or component structure.

## Limitations

The theorem covers only \(n\equiv1\pmod3\). It does not determine shortest-path distances, diameters, Hamiltonicity, or spectral properties of these reconfiguration graphs. No publication-priority claim is made against unindexed equivalent rooted-triple reconfiguration results. The verification enumerates finitely many sizes and is not a substitute for the proof. Independent mathematical audit has not been performed.

## References

[1] E. W. Weisstein and A. Howroyd, OEIS A304561, “Number of minimum total dominating sets in the n-triangular (Johnson) graph,” May 2018. https://oeis.org/A304561

[2] S. Alikhani, D. Fatehi, C. M. Mynhardt, “On k-Total Dominating Graphs,” arXiv:1711.04363, first posted 2017-11-12; Austral. J. Combin. 73(2) (2019), 313–333. https://arxiv.org/abs/1711.04363 ; https://ajc.maths.uq.edu.au/pdf/73/ajc_v73_p313.pdf

[3] C. M. Mynhardt and S. Nasserasr, “Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey,” arXiv:2003.05956, 2020-03-12. https://arxiv.org/pdf/2003.05956
