# A residue-three connectivity transition for maximum dissociation sets of triangular graphs

## Finding
For each integer \(n\ge3\), let \(T(n)=L(K_n)=J(n,2)\) be the triangular graph, with vertices the two-element subsets of \([n]\) and adjacency when two subsets intersect. A *dissociation set* \(S\subseteq V(T(n))\) has maximum induced degree at most one. Write \(\mathcal R_n\) for the reconfiguration graph whose vertices are all maximum-cardinality dissociation sets, with \(S\sim S'\) precisely when \(|S\setminus S'|=|S'\setminus S|=1\). The move must preserve maximum cardinality and the dissociation condition; no intermediate deletion-only state is admitted.

**Theorem (complete component transition).** The dissociation number is \(\operatorname{diss}(T(n))=\lfloor 2n/3\rfloor\), a scalar already implied by the general line-graph theorem of Orlovich et al. The following reconfiguration classification holds:

- If \(n=3k\), the graph \(\mathcal R_n\) has exactly \(n!/(6^k k!)\) components, each isomorphic to the Cartesian power \(K_3^{\square k}\), hence each has \(3^k\) vertices and degree \(2k\).
- If \(n=3k+1\), the graph \(\mathcal R_n\) is connected. Its maximum sets are of two types: \(k\) disjoint three-vertex paths plus one unused original vertex, or \(k-1\) such paths plus two disjoint original edges. Their counts are, respectively, \(n!/(2^k k!)\) and \(n!/(2^{k+2}(k-1)!)\). The two types have respective degrees \(8k\) and \(10k-2\) in \(\mathcal R_n\).
- If \(n=3k+2\), the graph \(\mathcal R_n\) is connected and regular of degree \(6k\). Its \(n!/(2^{k+1}k!)\) maximum sets each correspond to \(k\) disjoint three-vertex paths plus one disjoint original edge.

For the middle case, \(k\ge1\), and for the last case \(k\ge1\), as follows from \(n\ge3\). In all cases the original paths and edges are spanning subgraphs of \(K_n\), not induced paths. Thus the exchange graph is disconnected precisely when \(n\) is divisible by three and \(n\ge6\), and its number and shape of components are explicit.

## Assumptions and scope
All graphs are finite and simple; \(K_n\) has the labeled vertex set \([n]\). A selected vertex of \(T(n)\) is an edge of \(K_n\). Under this identification, \(T(n)[S]\) has maximum degree at most one if and only if the selected edge set in \(K_n\) is a vertex-disjoint union of two-edge paths \(P_3\), single edges \(K_2\), and unused vertices. This equivalence includes paths with an extra ambient chord: a selected two-edge path is a \(P_3\) subgraph even when \(K_n\) contains the third edge.

## Proof
**Structural reduction and extremal cases.** Suppose the selected-edge subgraph has \(a\) two-edge paths, \(b\) isolated edges, and \(c\) unused original vertices. Then
\[
3a+2b+c=n,\qquad |S|=2a+b.
\]
No selected edge can meet two other selected edges; conversely a union of the stated components has the required induced degree bound. Since \(2a+b\le\lfloor 2(3a+2b+c)/3\rfloor\), the maximum size is at most \(\lfloor2n/3\rfloor\). It is attained by taking as many vertex-disjoint \(P_3\)'s as possible, with a final \(K_2\) if the remainder is two. Solving these two integer equations at equality shows that \(n=3k\) requires \((a,b,c)=(k,0,0)\); \(n=3k+1\) permits exactly \((k,0,1)\) and \((k-1,2,0)\); and \(n=3k+2\) requires \((k,1,0)\). This independently confirms the extremal classification without extrapolating from experiments.

**Multiple of three: invariant and components.** When \(n=3k\), each optimum partitions all \(n\) labels into \(k\) three-element blocks, carrying one centered two-edge path on each block. Replacing one selected edge leaves one vertex of its path unused and leaves the other selected edge of that path. A replacement connecting this vertex to a different path would make an edge of that other path meet two selected edges, violating the dissociation condition. As there are no unused original vertices and every optimum is again a union of \(k\) paths, the inserted edge must be the third edge within the same triple. Thus the triple partition cannot change. Within each triple, the three choices of path center form a \(K_3\) under single-edge replacements; choices in separate blocks are independent. Hence each component is \(K_3^{\square k}\), and the number of partitions is \(n!/(6^k k!)\).

**One unused vertex: connectivity.** Let \(n=3k+1\). Optima with \(k\) paths and one unused vertex are connected among themselves. Indeed, the path on a fixed triple has three centers joined pairwise by one-edge replacements. Reorient a chosen triple to make any prescribed original vertex \(x\) one of its leaves. If \(z\) is unused, replace its incident selected edge \(ax\) by \(az\), where \(a\) is that triple's center. This exchanges the roles of \(x\) and \(z\), preserves an optimum, and changes no other block. Transpositions of the unused label with arbitrary other labels generate every permutation of \([n]\); therefore all partitions into \(k\) triples and one singleton, and all their center assignments, lie in one component. Any optimum of the second type, with two isolated edges \(ab\) and \(cd\), has an adjacent optimum of the first type: remove \(cd\) and insert \(bc\), obtaining the selected path \(ab,bc\) and the unused vertex \(d\), leaving other paths unchanged. Hence all optima are connected.

**One isolated edge: connectivity.** Let \(n=3k+2\). Every optimum comprises \(k\) paths and one single edge. For a path \(ab,ac\) with center \(a\) and a disjoint selected edge \(de\), the following two legal single-edge changes exchange the original labels \(c\) and \(d\) between the path block and the edge block:
\[
\{ab,ac,de\}\ \longrightarrow\ \{ab,ce,de\}\ \longrightarrow\ \{ab,ce,ad\}.
\]
The intermediate configuration has the path \(ce,de\) and isolated edge \(ab\); the final configuration has path \(ab,ad\) and isolated edge \(ce\). Any chosen vertex of a path can first be made a leaf by reorienting its center using legal single-edge replacements. Thus any specified label in the edge block can be exchanged with any specified label in any triple block. Two such exchanges through the edge block implement a transposition between labels in two different triple blocks by using a third exchange to restore the edge block. Together with internal reorientations, these operations connect all partitions into triples and a pair and all possible centers. This proves connectivity for every \(k\ge1\).

**Enumeration and degrees.** Unlabeled path blocks each carry three choices of center. Counting set partitions gives \(n!/(6^k k!)\cdot3^k=n!/(2^k k!)\) when \(n=3k\). When \(n=3k+1\), choosing \(k\) triples and a singleton yields \(n!/(2^k k!)\); choosing \(k-1\) triples and two unlabeled pairs yields \(n!/(2^{k+2}(k-1)!)\). When \(n=3k+2\), choosing \(k\) triples and a pair yields \(n!/(2^{k+1}k!)\).

For \(n=3k\), there are two center changes per path, hence degree \(2k\). For \(n=3k+2\), each path admits two center changes and four exchanges between its path and the lone pair, hence degree \(6k\). For \(n=3k+1\), a path-plus-singleton type has per path two center changes, four leaf/singleton rearrangements staying in that type, and two transitions to the two-pair type, giving degree \(8k\). A two-pair type has two center changes and eight pair/path exchanges for each of its \(k-1\) paths, plus eight moves from its two pairs to a path and singleton, giving \(10(k-1)+8=10k-2\). The local classification exhausts all possible one-edge replacements, so no uncounted neighbors exist.

## Verification
The self-contained program `check_exhaustive.py` generates feasible selected-edge subsets directly, without using the classification, and constructs the exchange graph. The separate program `check_structural.py` generates the states from labeled block partitions, then reconstructs their one-edge transitions. Execute, from the containing directory:

```text
python3 check_exhaustive.py
python3 check_structural.py
```

Both programs ran successfully on every \(3\le n\le9\). They independently returned optimum counts \(3,15,30,90,945,2520,7560\) and component counts \(1,1,1,10,1,1,280\). At \(n=6\) the ten components all have nine vertices; at \(n=9\) the 280 components all have 27 vertices. Their degree distributions agree with the formulas, including the two degree classes \(16\) and \(18\) at \(n=7\). The two recorded stdout files preserve complete small-order outputs. This finite verification supports but does not replace the universal proof above.

## Relationship to prior work
Orlovich, Dolgui, Finke, Gordon and Werner proved the broader scalar result \(\operatorname{diss}(L(G))=\lfloor2|V(G)|/3\rfloor\) when \(G\) has a Hamiltonian path, as well as the general correspondence between line-graph dissociation sets and disjoint three-vertex paths/single edges. Taking \(G=K_n\) already gives the scalar maximum and supplies the structural setup. Neither its scalar theorem nor that correspondence alone establishes the component-preserving invariant, the connectedness in the other residues, or the exact component graphs under optimum-preserving one-vertex exchange. These exchange assertions are the contribution assessed here. Published work on dissociation polynomials of other graph families and generic vertex-set reconfiguration uses different objects or different constraints and does not imply this residue-three classification by the inspected statements.

## Limitations
The theorem concerns only labeled triangular graphs and replacement of exactly one selected vertex while remaining at the maximum dissociation cardinality. It does not determine diameters of the connected cases, other token-sliding rules, arbitrary line graphs, or all nonmaximum dissociation sets. The scalar extremal value and the path/pair correspondence are existing results; originality is asserted only for the reconfiguration structure and connectedness transition, subject to possible unknown equivalent literature. Independently checked small examples are not universal certificates. No external independent mathematical audit has been performed.

## References
1. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, "The complexity of dissociation set problems in graphs," *Discrete Applied Mathematics* **159** (2011), 1352–1366, DOI: 10.1016/j.dam.2011.04.023 (primary full text, in particular the Hamiltonian-path line-graph theorem).
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, "On the Complexity and Inapproximability of Dissociation Set Problems in Graphs," dated February 7, 2010, preprint report 05/10 (earlier version; manuscript dating does not establish online release date).
