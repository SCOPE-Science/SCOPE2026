# A five-state exact edge-open-packing enumerator for every tree

## Finding
For every finite simple tree \(T\), the complete edge-open-packing polynomial
\[
E_T(z)=\sum_{B\subseteq E(T)\, :\, B\text{ is an edge-open packing}}z^{|B|}
\]
is determined by the five disjoint-state recurrences below. In particular, for a tree on \(n\ge1\) vertices, **all coefficients** can be computed using \(O(n^2)\) integer-arithmetic operations and \(O(n^2)\) coefficient storage. Substituting \(z=1\) throughout the same recurrences counts all edge-open packings in \(O(n)\) integer-arithmetic operations. The empty set is included, so \(E_T(0)=1\); to count only nonempty edge-open packings, subtract one from the constant term. The highest nonzero exponent is the edge-open-packing number; its coefficient counts all maximum sets.

Root \(T\) at any vertex, and write \(C(v)\) for the children of \(v\). A polynomial stored at \(v\) counts choices among the edges of the descendant subtree \(T_v\), **excluding** the parent edge, if any. The parent edge is treated as present or absent as a boundary condition; it does not contribute a factor of \(z\) in the polynomial at \(v\).

Define \(a_v,b_v,c_v,d_v,e_v\) by the following exhaustive, mutually exclusive boundary cases:

* \(a_v\): parent edge absent, and zero selected child edges;
* \(b_v\): parent edge absent, and exactly one selected child edge;
* \(c_v\): parent edge absent, and at least two selected child edges;
* \(d_v\): parent edge present, and zero selected child edges;
* \(e_v\): parent edge present, and at least one selected child edge.

Each counts only choices extendable across the parent edge under the stated boundary condition. For each \(v\), form
\[
\begin{aligned}
H_v&=\prod_{u\in C(v)}(a_u+b_u+c_u),\\
P_v&=\prod_{u\in C(v)}a_u,\\
Q_v&=\prod_{u\in C(v)}(a_u+zd_u),\\
J_v&=z\sum_{u\in C(v)}d_u\prod_{w\in C(v)\setminus\{u\}}a_w,\\
K_v&=z\sum_{u\in C(v)}(d_u+e_u)\prod_{w\in C(v)\setminus\{u\}}a_w.
\end{aligned}
\]
The recurrences are
\[
\boxed{a_v=H_v,\quad b_v=K_v,\quad c_v=Q_v-P_v-J_v,\quad d_v=P_v,\quad e_v=Q_v-P_v.}
\]
Empty products are \(1\), empty sums \(0\); hence every leaf has \((a_v,b_v,c_v,d_v,e_v)=(1,0,0,1,0)\). If \(r\) is the root, then
\[
\boxed{E_T(z)=a_r+b_r+c_r.}
\]
All expressions are polynomials with nonnegative integer coefficients, despite the subtraction notation in the recurrence.

## Assumptions and scope
Graphs are finite, simple, undirected trees; the one-vertex tree is allowed. A pair of distinct selected edges \(e,f\) conflicts when a **third** edge, distinct from both, joins an endpoint of \(e\) to an endpoint of \(f\). An edge-open packing is a set of edges containing no conflicting pair. These are the conventions of the cited original papers, extended here by including the empty edge subset in the generating polynomial.

For a chosen edge subset \(B\), write \(d_B(v)\) for its degree at vertex \(v\). For each tree edge \(uv\), let \(\epsilon_{uv}=1\) if \(uv\in B\), and \(0\) otherwise. The exact local compatibility condition is
\[
\boxed{(d_B(u)-\epsilon_{uv})(d_B(v)-\epsilon_{uv})=0\qquad\text{for every }uv\in E(T).}
\]

## Proof
**Local compatibility lemma.** If both factors at an edge \(uv\) are positive, some selected edge other than \(uv\) is incident with \(u\), and a distinct selected edge other than \(uv\) is incident with \(v\). The middle edge \(uv\) is then a forbidden third edge between their endpoints. Conversely, every forbidden triple has a middle edge \(uv\), with the two selected edges respectively incident to \(u\) and \(v\) and distinct from \(uv\). Thus exactly the displayed product condition characterizes edge-open packings.

Now process the children of a rooted vertex \(v\). Write \(k\) for the number of selected edges joining \(v\) to its children.

If the parent edge is absent and \(k=0\), then no selected edge touches \(v\); every child subtree may independently use any configuration with its own parent edge absent. This gives \(a_v=H_v\).

If the parent edge is absent and \(k=1\), exactly one child \(u\) is joined by a selected edge. The vertex \(v\) has no other selected incident edge, so the chosen child can have any compatible continuation with its parent edge present, counted by \(d_u+e_u\). Every unchosen child \(w\) must have no selected child edge: otherwise the unselected edge \(vw\) would have selected edges at both ends besides itself. Such children contribute \(a_w\). Including the selected edge weight \(z\), this is precisely \(b_v=K_v\).

If the parent edge is absent and \(k\ge2\), then \(v\) has another selected edge besides each child edge. Every child, whether joined by a selected edge or not, must have no selected descendant edge. An unchosen child contributes \(a_u\), and a chosen child contributes \(zd_u\). Summing all choices of selected children yields \(Q_v\), and removing the \(k=0\) and \(k=1\) terms \(P_v,J_v\) gives \(c_v=Q_v-P_v-J_v\).

If the parent edge is present and \(k=0\), \(v\) is already incident to a selected edge. Every child edge is unselected and every child must have zero selected child edges. Thus \(d_v=P_v\). If the parent edge is present and \(k\ge1\), \(v\) has at least two selected incident edges, and every child is constrained to have zero selected descendant edges. The cases with one or more selected child edges contribute \(Q_v-P_v\), proving \(e_v=Q_v-P_v\).

These five cases are exhaustive and disjoint for the boundary edge status and the truncated selected-child count. Compatibility on edges strictly within each child subtree is inherited from its stored state; compatibility across different child subtrees can occur only through edges incident with \(v\), already covered by the local lemma and these cases. Induction on subtree order proves every recurrence with no omission or double counting. At the root the parent edge is absent, so the three possibilities for \(k\) sum to \(E_T(z)\).

**Complexity.** Maintain \(H_v,P_v,Q_v,J_v,K_v\) incrementally while adding children. For example, the single-chosen-child sums \(J_v\) and \(K_v\) update by the product rule, using a polynomial accumulator for the product of the preceding \(a_u\)'s; no division by polynomial factors is performed. With naïve polynomial multiplication, merging a child subtree of \(s\) vertices into already-processed child subtrees of total size \(p\) takes \(O((s+1)(p+1))\) coefficient operations for each of a constant number of products and sums. Across the entire tree, the cross terms \(sp\) charge unordered vertex pairs in distinct child subtrees to their unique lowest common ancestor, while the linear terms charge ancestor–descendant pairs. Each pair is charged at most a constant number of times. Hence the total is \(O(n^2)\) integer-arithmetic operations. Holding all subtree polynomial states requires at most \(O(n^2)\) coefficients. At \(z=1\), all operations are on scalars and each child is processed with constant work, giving \(O(n)\) arithmetic operations.

## Verification
The standalone `verify.py` independently enumerates all selected-edge subsets for every labeled tree on up to seven vertices, using Prüfer codes (with separate one- and two-vertex cases). It checks the original pairwise-conflict definition by testing all possible third edges, without using the local lemma to decide admissibility, and compares the resulting complete coefficient vector to the five-state recurrence. It checks 18,249 labeled trees and 1,119,263 edge subsets. It also checks 860 deterministic pseudorandom larger trees, on 8 through 50 vertices, for polynomial degree and positivity sanity. The recorded execution result is in `verification_output.txt`. All comparisons passed. Finite testing is corroborative only; the unrestricted result is established by the proof.

For orientation, the path on six vertices has \(E_{P_6}(z)=1+5z+7z^2+2z^3\), while the double star with two pendant edges at each of its two adjacent centers has \(1+5z+6z^2+2z^3\).

## Relationship to prior work
Chelladurai, Kalimuthu and Soundararajan (2022) introduced the edge-open-packing invariant and determined its maximum cardinality on standard families. Brešar and Samadi (2024) supplied a linear-time tree algorithm for the **maximum size**, using auxiliary optimization parameters. The present claim is not that maximum-size computation is new; it is the explicit disjoint five-state generating-function recurrence that counts **all cardinalities and all maximum-set multiplicities** on unrestricted trees. Brešar, Dravec, Hedžet and Samadi (2024) subsequently studied extremal equality on trees and graph products, not full tree enumeration. Pandey and Santra (2025) gave structural characterizations of possible maximum sizes, likewise different from coefficient enumeration. General finite-state tree-automata and bounded-treewidth counting frameworks can imply abstract tractability of such local configurations; the claim here is an explicit five-polynomial factorization, transparent state semantics, and its quadratic arithmetic bound, not priority for the bare existence of some polynomial algorithm.

## Limitations
Only trees (or multiplicatively, their disjoint unions) are covered; cycles may create additional interactions not captured by these recurrences. The \(O(n^2)\) bound is for integer-arithmetic operations, not bit complexity, since coefficients may have linear-in-\(n\) bit length. The result does not claim an optimal arithmetic bound, a real-rootedness property, or an algorithm for enumerating individual solutions with constant delay. The computer checks cover finitely many cases. Priority cannot be guaranteed against inaccessible or unindexed equivalently strong generating-function recurrences. No independent mathematical validation has been performed.

## References
1. G. Chelladurai, K. Kalimuthu, S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, https://doi.org/10.1051/ro/2022171 ; open PDF: https://www.numdam.org/item/10.1051/ro/2022171.pdf .
2. B. Brešar, B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1 (1 March 2024), https://arxiv.org/abs/2403.00750 .
3. B. Brešar, T. Dravec, J. Hedžet, B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (2024), https://arxiv.org/abs/2406.04020 .
4. A. Pandey, K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935 (2025), https://arxiv.org/abs/2508.01935 .
