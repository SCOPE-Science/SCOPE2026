# Minimal total domination in triangular graphs: short-legged spider forests

## Finding

Let \(n\geq3\), and let \(T(n)=L(K_n)=J(n,2)\) be the triangular graph: its vertices are the two-element subsets of \([n]\), with adjacency when two such subsets share exactly one element. Let \(i_{n,k}\) be the number of **inclusion-minimal total dominating sets** of \(T(n)\) containing exactly \(k\) vertices. A set is total dominating when every graph vertex, including each selected one, has an adjacent selected vertex; minimal means no proper subset remains total dominating.

Associate with a selected set \(S\subseteq V(T(n))\) the simple graph \(F=([n],S)\), regarding selected two-subsets as edges. Then \(S\) is inclusion-minimal total dominating if and only if **exactly one** of the following holds:

1. \(F\) is a vertex-disjoint union of three-vertex paths covering all \(n\) original vertices; or
2. \(F\) has exactly one isolated vertex and all of its nontrivial components are *short-legged spiders*: trees having a center of degree at least two with every leg of length one or two. In particular, no isolated-edge component is permitted.

The complete two-variable enumeration is, for every \(n\geq3\),
\[
\sum_{k\geq0}i_{n,k}z^k
=n!\,[x^n]\left(\exp\left(\frac{x^3z^2}{2}\right)+x\exp\bigl(H(x,z)\bigr)\right),
\]
where
\[
H(x,z)=x\left(\exp(xz+x^2z^2)-1-xz-x^2z^2\right)-\frac{x^4z^3}{2}.
\]
Here the variable \(x\) marks the \(n\) labeled vertices of the underlying complete graph, and \(z\) marks the number of selected edges. The auxiliary generating series is interpreted only for coefficients with \(n\geq3\).

Consequently, the smallest and largest cardinalities of inclusion-minimal total dominating sets are
\[
\gamma_t(T(n))=\left\lceil\frac{2(n-1)}3\right\rceil,
\qquad
\Gamma_t(T(n))=\max\{2,n-2\}.
\]
The minimum-cardinality identity is also independently stated in the 2026 work of Cornet, Dravec, and Torres and **is not claimed as new here**. The claimed advance is the characterization of **all** inclusion-minimal sets, the full cardinality enumerator, and the upper cardinality identity.

## Assumptions and scope

All graphs are finite, undirected, and simple. An isolated vertex of \(F\) refers to the original ground set \([n]\), **not** a vertex of \(T(n)\). A short-legged spider may have legs of both allowed lengths. The three-vertex path qualifies as a spider, and a four-vertex path has two possible choices of center; the latter ambiguity is removed in the generating function. No assertion is made about total dominating sets that are not inclusion-minimal, nor about \(J(n,r)\) for \(r\neq2\).

## Proof

**Step 1: the total-domination criterion.** Let \(U\) denote the vertices of \([n]\) incident with a selected edge of \(F\). An edge \(ab\) of \(K_n\) that is unselected has a selected adjacent edge precisely when at least one of \(a,b\) lies in \(U\). Thus all unselected edges are dominated if and only if the complement of \(U\) has size at most one. A selected edge \(ab\in F\) has a *different* selected edge meeting it precisely when \(\deg_F(a)+\deg_F(b)\geq3\), which is equivalent to saying that \(ab\) is not the sole edge of a two-vertex component. Consequently, \(S\) is total dominating in \(T(n)\) if and only if \(F\) has at most one isolated vertex and no connected component is an isolated edge. This condition is monotone when selected edges are added, as total domination must be.

**Step 2: acyclicity of an inclusion-minimal set.** Suppose a nontrivial component of \(F\) contains a cycle, and delete an edge on that cycle. Every vertex of this component stays incident with a selected edge; the component stays connected and has at least three vertices. No new isolated vertex or isolated-edge component is created, so the criterion from Step 1 is still satisfied. Hence an inclusion-minimal \(F\) is a forest, each of whose nontrivial components contains at least three vertices.

**Step 3: no isolated vertex.** Suppose \(F\) spans all \(n\) vertices. Delete a leaf edge from any tree component. A single vertex becomes isolated, which is allowed by Step 1. For minimality the remaining nontrivial part of that component must therefore be an isolated edge. This forces the original tree component to be a three-vertex path. Conversely, in a spanning disjoint union of such paths every selected-edge deletion leaves an isolated-edge component, violating Step 1. This proves the first alternative.

**Step 4: exactly one isolated vertex.** Suppose \(F\) has one isolated vertex. In any tree component, deletion of a leaf edge creates a second isolated vertex, so that edge is indispensable. Deletion of a non-leaf edge leaves the count of isolated vertices unchanged. By Step 1, it is indispensable precisely when removing it separates a two-vertex tree component. Therefore an allowed tree \(Q\) is exactly a tree of order at least three in which every edge with two non-leaf endpoints cuts off a two-vertex component.

We verify that these trees are exactly the short-legged spiders. A tree of diameter at least five has an edge between the third and fourth vertices on a diameter-six-vertex subpath; cutting that edge leaves at least three vertices on **each** side, contradicting the preceding condition. Thus its diameter is at most four. If the diameter is four, choose its unique center \(c\). Every neighbor of \(c\) has at most one child at distance two: two such children would make the branch at least three vertices, while a different diameter arm makes the other side of the center-to-neighbor edge at least three vertices. Thus every arm from \(c\) has length one or two. If the diameter is three, its central edge must cut off a two-vertex component; rooting at the other endpoint gives one arm of length two and all remaining arms of length one. Diameter at most two gives a star. In each case the root has at least two arms. Conversely, for any short-legged spider, each non-leaf edge joins the center to a length-two arm and its removal detaches an isolated edge; every leaf edge creates an additional isolated vertex. Hence precisely these components give inclusion-minimal \(F\) with one isolated vertex.

**Step 5: exact labeled counting.** A spanning forest of three-vertex paths has one component type, with exponential generating weight \(x^3z^2/2\) because exactly three labeled paths exist on any three-element set. The labeled set of these components therefore contributes \(\exp(x^3z^2/2)\).

For a spider rooted at its center, each arm is either a single labeled vertex with one selected edge (weight \(xz\)), or an **ordered** intermediate/leaf pair with two selected edges (weight \(x^2z^2\)). At least two arms are required, so the rooted component series is \(x(\exp(xz+x^2z^2)-1-xz-x^2z^2)\). For every spider other than a four-vertex path the center is unique; a four-vertex path has **two** centers and is counted twice in this rooted series. The labeled EGF for one copy of all four-vertex paths is \(x^4z^3/2\), because there are \(12\) distinct labeled four-vertex paths. Subtracting that copy gives \(H(x,z)\). An unordered collection of spider components gives \(\exp(H(x,z))\), and a distinguished unused vertex gives the extra factor \(x\). The two structural cases are disjoint, proving the formula.

**Step 6: size extrema.** Write \(s\) for the number of nonisolated vertices and \(c\) for the number of nontrivial tree components of a minimal \(F\). By the classification, \(c\leq\lfloor s/3\rfloor\) and the selected-edge count is \(s-c\). Every total dominating set has \(s\geq n-1\), so its size is at least \(\lceil2(n-1)/3\rceil\). Constructions achieving equality are: an all-three-vertex-path spanning forest when \(3\mid n\); otherwise use one isolated vertex and partition the remaining vertices into three-vertex paths, with at most one four- or five-vertex spider for the appropriate residue class. These constructions cover \(n=3\) as well. With one isolated vertex, every minimal forest has at most \(n-2\) edges, and a single star on the other \(n-1\) vertices attains this for \(n\geq4\). With no isolated vertex, all components are three-vertex paths, giving \(2n/3\) edges; this is at most \(n-2\) for \(n\geq6\). For \(n=3\) the only size is two. The formulas follow.

## Verification

Two standalone exact-arithmetic programs accompany this result. `verify_direct.py` constructs the **open neighborhoods of the triangular graph itself**, checks every possible selected-vertex subset and tests irredundancy via private open-neighborhood witnesses, for \(3\leq n\leq7\). `verify_species.py` separately uses rooted-arm labeled counting and an exact rational recurrence for the exponential formula, reporting coefficients for \(3\leq n\leq12\). Both programs reproduce, at \(n=3,4,5,6,7\), respectively the coefficients
\[
3z^2,\quad12z^2,\quad80z^3,\quad840z^4,\quad630z^4+3402z^5.
\]
These are finite cross-checks of the independently proved all-order classification, **not** substitutes for Steps 1–6. Run each with Python 3 from a directory containing the two files and compare standard output to the corresponding `*.out` files.

## Relationship to prior work

Kanté, Limouzy, Mary, and Nourine (2014, arXiv:1407.2053) study algorithmic reductions for enumerating minimal total dominating sets in general graphs, but their relevant sections do not state the all-cardinality classification for triangular graphs. Pan, Yang, Li, and Xu (2019, arXiv:1910.02431) study total **edge** domination, the equivalent interpretation on \(K_n\), with an algorithm for trees and general bounds; their inspected manuscript has no complete-graph enumeration. Cornet, Dravec, and Torres (2026, arXiv:2610.04675) explicitly determine the **minimum** total domination number of \(J(n,2)\); that portion is covered prior work and is credited above. Only its abstract was accessible for this comparison, so it remains possible that its unavailable body includes relevant structural observations. OEIS A290716 instead counts *ordinary* inclusion-minimal dominating sets in triangular graphs, a different property; those data cannot supply the present total-domination enumerator.

## Limitations

Publication priority for the all-minimal classification and refined enumerator is not guaranteed: the full text of arXiv:2610.04675 was inaccessible, and differently titled or unindexed statements may exist. The proof is self-contained but independent external checking has not been performed. The finite programs cover only the explicitly stated small orders; the theorem for arbitrary \(n\geq3\) rests on its structural proof. The formula does not enumerate *all* total dominating sets, only those minimal under deletion.

## References

1. M. M. Kanté, V. Limouzy, A. Mary, L. Nourine, “On the Enumeration of Minimal Dominating Sets and Related Notions,” arXiv:1407.2053v1, publicly posted 2014-07-08, https://arxiv.org/abs/1407.2053.
2. Z. Pan, Y. Yang, X. Li, S.-J. Xu, “The complexity of total edge domination and some related results on trees,” arXiv:1910.02431v2, 2019, https://arxiv.org/abs/1910.02431.
3. M. G. Cornet, T. Dravec, P. Torres, “Domination and Total Domination in Johnson graphs,” arXiv:2610.04675v1, posted 2026-10-03, https://arxiv.org/abs/2610.04675.
4. OEIS Foundation, A290716, “Number of minimal dominating sets in the n-triangular (Johnson) graph,” https://oeis.org/A290716 (ordinary domination, distinguished from total domination).
