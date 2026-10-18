# Nine line-graph phases of eight-vertex paired domination on the Pappus graph

## Finding
Let \(P\) be the Pappus graph, realized as the bipartite incidence graph of the nine points \(p_{x,y}\) and nine lines \(\ell_{m,b}\), with \(x,y,m,b\in\mathbb F_3\) and
\[
p_{x,y}\sim\ell_{m,b}\quad\Longleftrightarrow\quad y=mx+b.
\]
A **paired-dominating set** is a dominating vertex set whose induced subgraph admits a perfect matching. Let \(R_k(P)\) join two paired-dominating sets of cardinality \(k\) when their symmetric difference contains exactly two vertices (one vertex is replaced, with feasibility preserved).

Then
\[
\gamma_{\rm pr}(P)=6,\qquad R_6(P)\cong9K_1,
\]
and, at the first larger feasible even cardinality,
\[
\boxed{R_8(P)\cong\bigsqcup_{i=1}^{9}L(K_{6,6}-C_{12}).}
\]
Here \(C_{12}\) is a spanning cycle of \(K_{6,6}\), and \(L\) denotes the line-graph construction. The nine copies are the connected components. Consequently \(R_8(P)\) has exactly \(216\) vertices, \(648\) edges, is regular of degree \(6\), and each connected component has \(24\) vertices, \(72\) edges, and diameter \(3\).

More precisely, every eight-vertex paired-dominating set contains a **unique** six-vertex paired-dominating core
\[
C_{c,m}=\{p_{c,y}:y\in\mathbb F_3\}\cup\{\ell_{m,b}:b\in\mathbb F_3\},
\quad(c,m)\in\mathbb F_3^2.
\]
The core cannot change under one-vertex replacement. For each core there are exactly \(24\) feasible eight-vertex extensions, and the replacement graph on those extensions is the displayed line graph.

## Assumptions and scope
All graphs are simple and undirected; a perfect matching of the *induced* graph on a selected set is required, without storing or distinguishing a particular matching. Labels in \(\mathbb F_3\) are interpreted modulo three. A single replacement need not use an edge of the original graph (the token-jumping rather than token-sliding convention). The statement concerns precisely cardinalities \(6\) and \(8\) on this specified eighteen-vertex graph, not all cardinalities, not an arbitrary incidence graph, and not replacement of entire matched pairs.

## Proof
**1. Optimal size and the six-vertex cores.** The graph is cubic on eighteen vertices, so a dominating set has size at least \(\lceil18/4\rceil=5\). A paired-dominating set must have even cardinality. Thus \(\gamma_{\rm pr}(P)\ge6\). For fixed \(c,m\), every line meets the full vertical point triple \(\{p_{c,y}\}\), and every point meets exactly one line of slope \(m\). The six vertices of \(C_{c,m}\) therefore dominate the graph. Their induced graph is exactly three independent matching edges, proving equality.

The exhaustive finite lemma in Step 2, applied also to balanced three-point/three-line subsets, gives **precisely these nine** six-vertex paired-dominating sets. Their pairwise intersections have at most three vertices, so no single replacement joins them: \(R_6(P)\cong9K_1\).

**2. Complete eight-vertex classification, including the finite lemma.** Bipartiteness and the existence of an induced perfect matching force any eight-vertex paired-dominating set to contain four point vertices and four line vertices. There are exactly \(\binom94^2=15{,}876\) candidate pairs \((Q,T)\). For any candidate, feasibility is equivalent to these three explicit predicates:

(a) every point outside \(Q\) is incident to some line of \(T\);

(b) every line outside \(T\) is incident to some point of \(Q\);

(c) at least one of the \(4!=24\) bijections \(Q\to T\) consists solely of incidences.

These are, respectively, the point-domination condition, line-domination condition, and induced perfect-matching condition; hence the test is *necessary and sufficient*, not a heuristic. The standalone programs `verification/verify_geometry.py` and `verification/verify_incidence.py` exhaust the domain using independently implemented feasibility tests.

There is a shorter symmetry-reduced finite certificate. The \(108\) affine transformations
\[
(x,y)\longmapsto(ax+c,dy+ex+f),\qquad
 a,d\in\mathbb F_3^{\times},\quad c,e,f\in\mathbb F_3,
\]
preserve the vertical point classes and permute the three nonvertical line slopes; their induced line maps preserve incidence. They have exactly four orbits on four-point subsets. The table gives orbit size and the number of compatible four-line subsets for one representative; for each row the latter is computed by the three exact predicates above over all \(\binom94=126\) line choices. `verification/verify_orbits.py` generates all \(108\) maps and checks that these four orbits are disjoint and exhaust all \(126\) point subsets.

| Four-point representative \(Q\) (coordinate pairs) | Orbit size | Compatible \(T\) for each \(Q\) |
|---|---:|---:|
| \(\{(0,0),(0,1),(0,2),(1,0)\}\) | 18 | 12 |
| \(\{(0,0),(0,1),(1,0),(1,1)\}\) | 27 | 0 |
| \(\{(0,0),(0,1),(1,0),(2,0)\}\) | 54 | 0 |
| \(\{(0,0),(0,1),(1,0),(2,1)\}\) | 27 | 0 |

Therefore there are \(18\cdot12=216\) feasible eight-vertex sets, and every one has all three points of one vertical class. The exact enumeration also checks that its four chosen lines include all three lines of one slope, uniquely. Equivalently, comparing the \(216\) tested sets with the \(9\cdot24\) explicit constructions of Step 3 proves that there are **no exceptions**. Both directions of this equality are explicitly asserted in `verification/verify_geometry.py`; thus this finite lemma is completely checkable, not an extrapolation from sample sizes.

**3. Extensions and the small bipartite graph.** Fix \(C_{c,m}\). Every eight-vertex superset with four vertices on each side uniquely adds a point \(p_{x,y}\) with \(x\ne c\) and a line \(\ell_{u,b}\) with \(u\ne m\). Domination is automatic because the core already dominates. The six core vertices induce a perfect matching, so the enlarged induced graph has a perfect matching if and only if either
\[
\text{(direct)}\quad y=ux+b,
\]
or
\[
\text{(crossed)}\quad y-m(x-c)=uc+b.
\]
For the crossed case, pair the new point to its unique slope-\(m\) core line, and pair the new line to the core point formerly matched to that line. These are the only possibilities: each new vertex has just one neighbour in the opposite-side core, and, after those two are paired, the remaining core vertices must retain their existing matching. The direct and crossed conditions are mutually exclusive because \((u-m)(x-c)\ne0\). For each external point and each of the two external slopes exactly two of the three possible offsets satisfy one condition; consequently there are \(6\cdot4=24\) extensions.

Define the bipartite graph \(B_{c,m}\) with its two parts consisting of the six external points and six external lines, joining a pair precisely when one of the two conditions above holds. Its \(24\) edges index the extensions. Each vertex of \(B_{c,m}\) has degree four. By an affine change of coordinates it suffices to consider \(c=m=0\). Then the complement of \(B_{0,0}\) in \(K_{6,6}\) consists of the pairs
\[
((x,y),(u,b)):\quad x,u\in\{1,2\},\quad b=y+ux\pmod3.
\]
Every one of its twelve vertices has degree two. A single cycle through all twelve is
\[
\ell_{1,1},p_{1,0},\ell_{2,2},p_{2,1},\ell_{1,0},p_{1,2},
\ell_{2,1},p_{2,0},\ell_{1,2},p_{1,1},\ell_{2,0},p_{2,2},\ell_{1,1}.
\]
Thus \(B_{c,m}\cong K_{6,6}-C_{12}\), with the cycle spanning the bipartition.

**4. Reconfiguration and metric.** Within a fixed core, changing exactly one selected vertex means retaining one of the two external choices and changing the other. This is exactly the condition that the corresponding edges of \(B_{c,m}\) share an endpoint, so the component is \(L(B_{c,m})\). A feasible one-vertex replacement cannot change the unique vertical point triple or the unique slope-line triple: four selected points (respectively lines) cannot acquire a *different* full triple by replacing only one vertex while retaining a full triple before the move. Therefore there are no transitions between different cores.

Since \(B_{c,m}\) is four-regular with \(12\) vertices and \(24\) edges, its line graph has \(24\) vertices and degree \(2(4-1)=6\), giving \(72\) edges. To see its diameter is at most three, take any edges \((p,\ell)\) and \((q,t)\) of \(B\). If they do not meet, any two point-side vertices \(p,q\) in \(B\) have a common line-side neighbour \(s\), since each has four neighbours among six; hence the path
\[
(p,\ell),\ (p,s),\ (q,s),\ (q,t)
\]
is a line-graph path of length at most three. The bound is sharp: for \(c=m=0\), the two allowed edges
\[
(p_{1,0},\ell_{1,2})\quad\text{and}\quad(p_{1,1},\ell_{1,1})
\]
are disjoint, and both crossed endpoint incidences are forbidden; their distance is three. Every component thus has diameter three. Summing across nine components gives \(216\) vertices and \(648\) edges.

## Verification
Three standalone Python 3 scripts, requiring only the standard library, are included with exact outputs. From the directory containing this file run:

```
python verification/verify_incidence.py
python verification/verify_geometry.py
python verification/verify_orbits.py
```

`verify_incidence.py` constructs the full 18-vertex incidence graph by bit masks, exhaustively tests balanced selected subsets using recursive perfect matching, constructs the actual jump graph and recomputes connected components and all component diameters. `verify_geometry.py` starts instead from the coordinate incidence predicate, enumerates all bijections to test matching, independently enumerates the candidate pairs, and compares them with the explicit core/extension construction and the line graphs of the nine small bipartite graphs. `verify_orbits.py` independently checks the four affine orbits and all their line-subset feasibility counts. Recorded terminal outputs end with `VERIFY_OK`. The correctness of the finite exhaustive assertion follows from the complete combinatorial loop ranges and matching predicates, not from a statistical sample.

## Relationship to prior work
Haynes and Slater introduced paired domination and its perfect-matching condition in 1998. Mynhardt and Teshima (2017) considered a related \(\gamma_{\rm pr}\)-graph based on **minimum** paired-dominating sets with **sliding** moves, proving broad realization results for arbitrary target graphs. Their constructions do not imply the eight-vertex, jumping-move configuration structure of the fixed Pappus graph. A 2023 dissertation by Eakawinrujee surveys and determines \(\gamma\)-paired dominating graphs for paths, cycles, and several named graph families; its listed classes and searchable text do not give the Pappus classification. Published graph reference material identifies the Pappus graph with \(\operatorname{Biaff}(3)\), the three-nonvertical-direction incidence graph used here. The ordinary domination number \(5\) appears in existing graph software documentation and is not asserted as new.

The new claim is the *nine exact eight-vertex reconfiguration components and their line-graph/diameter structure*, alongside the boundary of nine frozen minimum configurations. Literature searches and relevant mathematical-record comparisons have not identified an equivalent statement, but absence from those searches is not a uniqueness proof.

## Limitations
The finite enumeration is a valid exhaustive certificate for the stated eighteen-vertex incidence graph only; it is not a theorem for other \(\operatorname{Biaff}(q)\). Paths in the component line graphs correspond to token-jumping replacements, **not** to token slides along edges of the Pappus graph. Neither all ten-vertex placements nor attack-response games are studied. Independent external scientific review has not been performed. Undiscovered equivalent or stronger literature, including unindexed sources, is a residual priority risk. The 1998 publisher landing page makes the original definition and date available but not the complete paper text in the inspected access path; its abstract alone was not used to infer absence of a covering theorem.

## References
1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206. Publisher first-online date 1998-12-07. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0037%28199810%2932%3A3%3C199%3A%3AAID-NET4%3E3.0.CO%3B2-F
2. C. M. Mynhardt and L. E. Teshima, *A note on some variations of the \(\gamma\)-graph*, arXiv:1707.02039 (2017), https://arxiv.org/html/1707.02039v1
3. P. Eakawinrujee, *Total and Paired Domination Numbers and \(\gamma\)-Total and \(\gamma\)-Paired Dominating Graphs of Some Graphs*, doctoral dissertation (2023), https://ethesisarchive.library.tu.ac.th/thesis/2023/TU_2023_6109320413_17206_27705.pdf
4. A. E. Brouwer, *Incidence matrices and distance-regular graphs*, table of biaffine graphs identifying the 18-vertex Pappus graph as \(\operatorname{Biaff}(3)\), https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf
5. SageMath, *Generic graphs* reference, example `graphs.PappusGraph().dominating_set(value_only=True)` returning \(5\), https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generic_graph.html
