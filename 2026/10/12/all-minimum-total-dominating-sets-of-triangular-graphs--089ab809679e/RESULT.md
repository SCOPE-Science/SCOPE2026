# All minimum total dominating sets of triangular graphs

## Finding

For each integer \(n\ge4\), let the Johnson or triangular graph
\[
J(n,2)=L(K_n)
\]
have one vertex for each two-element subset of \([n]\), with two vertices adjacent exactly when their corresponding edges of \(K_n\) share an endpoint. A total dominating set is a selected vertex set such that *every* vertex, including selected vertices, has a selected neighbor.

The recently determined total domination number is
\[
\gamma_t(J(n,2))=\left\lceil\frac{2(n-1)}3\right\rceil.
\]
Here we classify **every** minimum total dominating set and count them exactly. Let \(M_n\) be their number (with vertices of \(K_n\) labeled). Writing \(n=3t+r\), \(r\in\{0,1,2\}\), the answers are
\[
\boxed{M_{3t+1}=\frac{(3t+1)!}{2^t t!}\quad(t\ge1),}
\]
\[
\boxed{M_{3t+2}=\frac{2(3t+2)!}{3\,2^{t-1}(t-1)!}\quad(t\ge1),}
\]
and
\[
\boxed{M_{3t}=\frac{(3t)!}{2^t t!}
+\mathbf 1_{t\ge2}\frac{25(3t)!}{24\,2^{t-2}(t-2)!}
+\mathbf 1_{t\ge3}\frac{2(3t)!}{9\,2^{t-3}(t-3)!}\quad(t\ge2).}
\]
The indicators in the last display mean that a summand is present only in its stated valid range; factorials with negative arguments are never evaluated.

The initial values for \(n=4,5,6,7,8,9\) are respectively \(12,80,840,630,13440,277200\). The sharp modular variation records the different spanning-forest types that are forced by optimality.

## Assumptions and scope

Graphs are finite and simple. For \(n\ge4\), a total dominating set of \(J(n,2)\) is a set \(D\subseteq V(J(n,2))\) such that every vertex has at least one *distinct* neighbor in \(D\). A minimum total dominating set has cardinality \(\gamma_t(J(n,2))\). In the line-graph identification, \(D\) corresponds bijectively to an edge set \(F\) of the labeled complete graph \(K_n\); the spanning subgraph \(H=([n],F)\) includes isolated vertices.

The result counts distinct vertex subsets, not orders of selection, graph-isomorphism classes, or automorphism orbits. The scalar minimum is acknowledged as existing literature; the final claim is the classification and exact number of all optimal sets.

## Proof

**Step 1: exact edge-set characterization.** Let \(F\subseteq E(K_n)\) be nonempty and put \(H=([n],F)\). An edge \(e\) of \(K_n\) is adjacent in \(J(n,2)\) to a selected edge precisely when it shares an endpoint with an edge of \(F\) different from itself.

If \(H\) has two isolated vertices \(u,v\), the edge \(uv\) has no selected neighbor. If \(H\) has a component consisting of one edge \(uv\) and no other incident selected edge, then that *selected* edge has no selected neighbor. Both situations contradict total domination.

Conversely, suppose \(H\) has at most one isolated vertex and no isolated-edge component. Every edge \(uv\) not in \(F\) has at least one endpoint incident to a selected edge; that selected edge is necessarily different from \(uv\). Every edge belonging to \(F\) has a selected adjacent edge because its component is not an isolated copy of \(K_2\). Hence \(F\) is a total edge dominating set, equivalently \(D\) totally dominates \(J(n,2)\).

Thus
\[
D\text{ totally dominates }J(n,2)
\quad\Longleftrightarrow\quad
\#\{\text{isolated vertices of }H\}\le1
\text{ and }H\text{ has no }K_2\text{ component}.
\]

**Step 2: the sharp edge bound and extremal acyclicity.** Suppose \(H\) has \(k\) selected edges, \(c\) nontrivial connected components, \(\varepsilon\in\{0,1\}\) isolated vertices, and total cycle rank \(s\ge0\). Since every nontrivial component contains at least two edges,
\[
c\le\left\lfloor\frac k2\right\rfloor.
\]
Counting vertices in its nontrivial components gives
\[
n-\varepsilon=k+c-s.
\]
Consequently
\[
n-1\le k+\left\lfloor\frac k2\right\rfloor,
\]
so
\[
k\ge\left\lceil\frac{2(n-1)}3\right\rceil.
\]
The forest constructions below attain this bound, proving the minimum without relying on prior results.

Write \(n=3t+r\). For \(r=1\), \(k=2t\) and the equation gives
\[
c=t+1-\varepsilon+s\le t,
\]
forcing \(\varepsilon=1\), \(s=0\), and \(c=t\). With \(2t\) edges spread over \(t\) components containing at least two edges apiece, every component is the three-vertex path \(P_3\).

For \(r=2\), \(k=2t+1\), so
\[
c=t+1-\varepsilon+s\le t.
\]
Again \(\varepsilon=1\), \(s=0\), and \(c=t\). Exactly one component has three edges and thus four vertices; it is an arbitrary tree on four vertices. The other \(t-1\) components are copies of \(P_3\).

For \(r=0\), \(k=2t\) and
\[
c=t-\varepsilon+s\le t.
\]
When \(\varepsilon=0\), necessarily \(s=0\), \(c=t\), and all components are copies of \(P_3\). When \(\varepsilon=1\), either \(s=0,c=t-1\) or \(s=1,c=t\). The latter is impossible: \(t\) nontrivial components and exactly \(2t\) edges would make every component a two-edge tree, giving \(s=0\). Thus \(s=0,c=t-1\). Relative to two edges per nontrivial component there are precisely two surplus edges. They can belong to one four-edge tree on five vertices, or to two three-edge trees on four vertices each. All remaining components are \(P_3\). The former pattern requires \(t\ge2\) and the latter \(t\ge3\).

All described forests satisfy the characterization in Step 1, and their edge counts equal the lower bound. This proves the complete minimum-set classification.

**Step 3: labeled enumeration.** Cayley's tree formula gives exactly \(v^{v-2}\) distinct labeled trees on any specified \(v\)-element vertex set. In particular, the respective counts for \(v=3,4,5\) are \(3,16,125\). A partition into repeated component sizes is counted by a multinomial coefficient divided by the factorials of the numbers of repeated components; each block is then independently given its labeled tree structure.

For \(n=3t+1\), choose a single isolated vertex and partition the remaining vertices into \(t\) unordered three-vertex blocks, each with one of three trees:
\[
M_{3t+1}=\frac{(3t+1)!}{(3!)^t t!}\,3^t
=\frac{(3t+1)!}{2^t t!}.
\]

For \(n=3t+2\), one vertex is isolated, one distinguished four-vertex block forms any of sixteen trees, and the other \(t-1\) blocks are three-vertex trees:
\[
M_{3t+2}=\frac{(3t+2)!}{4!\,(3!)^{t-1}(t-1)!}\,16\,3^{t-1}
=\frac{2(3t+2)!}{3\,2^{t-1}(t-1)!}.
\]

For \(n=3t\), there are three disjoint structural types. With no isolate and \(t\) three-vertex trees, the count is
\[
\frac{(3t)!}{(3!)^t t!}\,3^t=\frac{(3t)!}{2^t t!}.
\]
With one isolate, one five-vertex tree, and \(t-2\) three-vertex trees, the count (for \(t\ge2\)) is
\[
\frac{(3t)!}{5!\,(3!)^{t-2}(t-2)!}\,125\,3^{t-2}
=\frac{25(3t)!}{24\,2^{t-2}(t-2)!}.
\]
With one isolate, two unordered four-vertex trees, and \(t-3\) three-vertex trees, the count (for \(t\ge3\)) is
\[
\frac{(3t)!}{(4!)^2\,2!\,(3!)^{t-3}(t-3)!}\,16^2\,3^{t-3}
=\frac{2(3t)!}{9\,2^{t-3}(t-3)!}.
\]
The structural types are disjoint, so their sum gives the stated formula.

## Verification

The standalone `artifacts/verify.py` checks the defining *open-neighborhood* condition in \(J(n,2)\) directly: each vertex corresponds to an edge of \(K_n\), and its adjacency bitmask comprises the other edges with a shared endpoint. It enumerates every edge subset of cardinality \(\lceil2(n-1)/3\rceil\) for \(4\le n\le9\), compares direct total domination to the forest-type characterization, and counts all feasible subsets. The counts match the closed formulas for each order. It also checks integral positivity of the formulas through \(n=150\).

Reproduction command: `python artifacts/verify.py` with Python 3 and its standard library. The directly checked cases are \((n,k,M_n)=(4,2,12),(5,3,80),(6,4,840),(7,4,630),(8,5,13440),(9,6,277200)\).

The finite enumeration is not the proof of the arbitrary-order theorem; the counting and acyclicity arguments above are.

## Relationship to prior work

Cornet, Dravec, and Torres determine the exact *total domination number* of \(J(n,2)\) in their October 2026 preprint. Their stated scalar result is precisely the minimum cardinality used here. The contribution here is a classification of all extremizers and a closed formula for their number, with a sharp distinction between the three residues of \(n\) modulo three.

The earlier conference paper by the same authors treats *ordinary* domination in Johnson graphs. The June 2026 work of Lee and Oh resolves an ordinary-domination question for \(J(n,3)\). Neither abstract-level statement provides an enumeration of minimum total dominating sets in \(J(n,2)\).

The identification \(J(n,2)=L(K_n)\) also recasts the theorem in terms of *total edge dominating sets* of a complete graph. Older total edge domination research gives definitions and graph-class bounds, but the targeted literature and published-result searches did not locate the labeled optimal-set count given here.

## Limitations

The result concerns the second Johnson level \(J(n,2)\) and minimum total dominating sets only; it does not count total dominating sets of every size, or determine minimum counts for \(J(n,k)\) with \(k\ge3\).

The highly relevant 2026 arXiv primary article was available in the searched environment only through its metadata, abstract, and indexed summaries. Its full PDF was not retrievable through the available open channels, and the authorized institutional fallback required unavailable interactive input. Consequently, exact comparison against any supplementary enumeration hidden in its full text remains a residual originality risk. Its publicly stated theorem is a scalar minimum, not a minimum-set count; this is *not* taken as proof that its full text lacks such a count.

The 2025 conference paper was inspected through its institutional record and abstract, not by claiming to have read an unavailable complete PDF. The enumeration is independently derived and checked here, but literary noncoverage cannot be absolutely certified from search results.

## References

1. M. G. Cornet, T. Dravec, and P. Torres, “Domination and Total Domination in Johnson graphs,” arXiv:2610.04675v1, first publicly available October 3, 2026.
2. M. G. Cornet, T. Dravec, and P. Torres, “Domination in Johnson graphs,” *Procedia Computer Science* **273** (2025), 223–230, DOI 10.1016/j.procs.2025.10.302.
3. S.-A. Lee and S. Oh, “Domination in Johnson graphs \(J(n,3)\) for odd \(n\),” arXiv:2606.10326v1, June 9, 2026.
