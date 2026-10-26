# Period-three rigidity of maximum edge open packings in complete rooted trees

## Finding

**Theorem.** Let \(b\ge 2\) and \(h\ge 1\) be integers. Let \(T_{b,h}\) be the complete rooted \(b\)-ary tree of height \(h\), with every internal vertex having exactly \(b\) children. The edge open packing number is
\[
\rho_e^o(T_{b,h})=\sum_{t=0}^{\lfloor(h-1)/3\rfloor}b^{h-3t}.
\]
There is **exactly one** maximum edge open packing. It consists of every edge whose parent endpoint is at a depth in
\[
\{h-1-3t:0\le t\le\lfloor(h-1)/3\rfloor\}.
\]
Thus the chosen edges occupy complete edge layers separated by two empty edge layers. The proportion of all edges selected converges, for fixed \(b\), to \(b^2/(b^2+b+1)\) as \(h\to\infty\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The root is at depth zero. Every vertex of depth less than \(h\) has exactly \(b\) children. In particular \(T_{b,h}\) contains \(\sum_{i=1}^h b^i\) edges. Edges sharing a center can coexist in an edge open packing. An edge set \(S\) is an **edge open packing** when, for every two different selected edges \(e,f\), no third edge of the ambient graph, different from both \(e\) and \(f\), connects an endpoint of \(e\) to an endpoint of \(f\). The optimum \(\rho_e^o\) maximizes \(|S|\). Distinct labeled edges and their fixed depths are not identified by automorphisms. The case \(h=0\) has the unique empty optimum and is included only as a boundary condition for the proof.

## Proof

**Local constraint.** For any edge \(uv\) of a tree, let \(d_S(v)\) be the number of selected edges incident to \(v\), and let \(\epsilon_{uv}=1\) when \(uv\in S\) and zero otherwise. Then \(S\) is an edge open packing **if and only if**
\[
(d_S(u)-\epsilon_{uv})(d_S(v)-\epsilon_{uv})=0\qquad\text{for every }uv\in E(T).
\]
Indeed, if both factors are nonzero, an edge selected at \(u\), an edge selected at \(v\), and the connecting edge \(uv\) form a forbidden pair with a third intervening edge. Conversely, in a tree any third edge connecting endpoints of two different selected edges has exactly such a witnessing orientation. The distinctness requirement rules out using the selected edge itself as the connecting edge.

**Exact boundary-state recurrence.** For a complete \(b\)-ary subtree of height \(k\), define \(D_k(x,j)\) as the largest number of selected edges **inside that subtree**, excluding its edge to the parent, among locally valid selections for which the parent edge has prescribed selection indicator \(x\in\{0,1\}\) and exactly \(j\) of the root's \(b\) child edges are selected. The parent edge is treated as a boundary edge in the local condition. Let impossible states have value \(-\infty\). For a leaf, \(D_0(0,0)=D_0(1,0)=0\); all other states are impossible. For \(k\ge1\), abbreviate the four numbers from height \(k-1\) by
\[
U=D_{k-1}(0,0),\quad X=D_{k-1}(1,0),\quad M_0=\max_j D_{k-1}(0,j),\quad M_1=\max_j D_{k-1}(1,j).
\]
The local constraint gives the following exhaustive recurrence:
\[
\begin{aligned}
D_k(0,0)&=bM_0,& D_k(1,0)&=bU,\\
D_k(0,1)&=1+M_1+(b-1)U,\\
D_k(0,j)&=j+jX+(b-j)U&& (2\le j\le b),\\
D_k(1,j)&=j+jX+(b-j)U&& (1\le j\le b).
\end{aligned}
\]
For the first line, an unselected root with no selected parent or child edges permits an unrestricted child optimum; a selected parent edge and no child edges require every child's root degree to vanish. With precisely one selected child and no parent edge, that child permits an unrestricted selected-parent continuation, but every unselected-child root must have degree zero. When at least two edges incident to the subtree root are selected, every child root must have degree zero, regardless of whether its connecting edge is selected. These cases partition every feasible selection.

**Closed form of every boundary state.** Put
\[
A_k=\sum_{t=0}^{\lfloor(k-1)/3\rfloor}b^{k-3t}\ (k\ge1),\qquad A_0=0.
\]
For all \(b\ge2\) and \(k\ge1\), we prove by induction, simultaneously for every \(x\) and \(0\le j\le b\), that
\[
D_k(x,j)=
\begin{cases}
A_k-b+j,&k\equiv1\pmod3,\\
A_k,&k\equiv2\pmod3,\ x=0,\ j=0,\\
A_k-(b^2-b-1),&k\equiv2\pmod3,\ x=0,\ j=1,\\
A_k-b^2+j,&k\equiv2\pmod3\text{ in every remaining state},\\
A_k,&k\equiv0\pmod3,\ x=0,\ j=0,\\
A_k-(b^2-b-1),&k\equiv0\pmod3,\ x=0,\ j=1,\\
A_k-j(b^2-1),&k\equiv0\pmod3\text{ in every remaining state}.
\end{cases}
\]
For \(k=1\), every state equals \(j\), agreeing with \(A_1=b\). To see the induction explicitly, at heights of residue \(1,2,0\), the preceding display yields, respectively, the quadruples \((U,X,M_0,M_1)\):
\[
\begin{array}{c|c}
k\pmod3&(U,X,M_0,M_1)\\\hline
1&(A_k-b,A_k-b,A_k,A_k)\\
2&(A_k,A_k-b^2,A_k,A_k-b^2+b)\\
0&(A_k,A_k,A_k,A_k).
\end{array}
\]
Substituting these three rows into the exhaustive recurrence gives exactly the next residue case; use \(A_{k+1}=bA_k\) if \(k+1\equiv0,2\pmod3\) and \(A_{k+1}=bA_k+b\) if \(k+1\equiv1\pmod3\). The latter also holds at \(k=0\), giving the base case directly. This proves every stated state value, including boundary effects.

**Optimality and uniqueness.** The root has no parent edge. Hence its feasible optimum is \(\max_jD_h(0,j)\). For \(h\equiv1\pmod3\), the unique maximizing child-edge count is \(j=b\). For \(h\equiv0,2\pmod3\), the unique maximizing count is \(j=0\): the alternatives lose at least \(b^2-b-1\ge1\) or a larger amount. Each maximum has value \(A_h\). The recurrence also forces the continuations uniquely. When a root's optimal count is \(b\), each child receives state \((1,0)\). When its optimal count is zero, its children receive independent unique state maxima of type \((0,\cdot)\). The state \((1,0)\) forces every child into \((0,0)\), and \((0,0)\) forces every child into its unique \((0,\cdot)\) optimum. Starting from the single feasible empty configuration at height zero, simultaneous induction proves uniqueness for the winning root state, as well as for these two forced states. Iterating down the tree selects all edges at depths \(h-1,h-4,h-7,\ldots\) and no others. Conversely this unique pattern satisfies the local constraint, so the optimum and classification follow.

**Density.** Since \(|E(T_{b,h})|=(b^{h+1}-b)/(b-1)\), the above finite geometric sum yields
\[
\lim_{h\to\infty}\frac{\rho_e^o(T_{b,h})}{|E(T_{b,h})|}=\frac{1-b^{-1}}{1-b^{-3}}=\frac{b^2}{b^2+b+1}.
\]

## Verification

The embedded standalone program `verify_eop_tree.py` uses the original third-edge definition to exhaustively test 1,069,183 edge subsets across 11 small parameter instances and confirms each optimal set and its uniqueness. Independently, boundary-state dynamic programming checks every state against the explicit formulas for all \(2\le b\le10\) and \(1\le h\le18\) (162 parameter pairs). The executable program and its full output are supplied; run `python3 verify_eop_tree.py` with Python 3.9 or later. Computation checks finite premises and stress-tests the induction; the all-height conclusion is proved by the recurrence and induction above.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan introduced edge open packing and studied standard graph families. Brešar and Samadi subsequently gave a general linear-time algorithm computing the edge open packing number of **any tree**. Their generic algorithm therefore already establishes that values for this family are computable. Brešar, Dravec, Hedžet, and Samadi compared induced matchings and edge open packings on trees. The present theorem instead specifies a closed two-parameter value, identifies the **only** maximizing edge set, and exhibits its rigid three-level structure and limiting density. It does not claim a new generic tree algorithm or the original definition. The 2022 foundational paper's full publisher PDF was inaccessible during this review; bibliographic equivalence remains a residual risk.

## Limitations

The tree must be exactly complete and uniformly \(b\)-ary, with \(b\ge2\). The theorem does not cover irregular rooted trees, leaves at mixed depths, or an arbitrary induced-star optimization. Exhaustive priority searches cannot rule out unindexed equivalent formulas, and no independent mathematical audit has been performed.

## References

1. Chelladurai, Kalimuthu, and Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, DOI: 10.1051/ro/2022171, https://doi.org/10.1051/ro/2022171.
2. Brešar and Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (first posted 2024-03-01), https://arxiv.org/abs/2403.00750.
3. Brešar, Dravec, Hedžet, and Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first posted 2024-06-06), https://arxiv.org/abs/2406.04020.
