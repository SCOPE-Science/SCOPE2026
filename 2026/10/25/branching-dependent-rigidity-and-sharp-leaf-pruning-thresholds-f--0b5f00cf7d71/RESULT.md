# Branching-dependent rigidity and sharp leaf-pruning thresholds for minimum domination of complete rooted trees

## Finding
Let \(T_{d,h}\) be the rooted perfect \(d\)-ary tree of height \(h\), with each internal vertex having exactly \(d\) children; assume integers \(d\ge 2\) and \(h\ge 1\). Write \(L_j\) for its depth-\(j\) level, \(\gamma(G)\) for the domination number, and \(\zeta(G)\) for the number of dominating sets of cardinality \(\gamma(G)\).

**Theorem (complete optimum census and a sharp boundary transition).** Put
\[
F_{d,h}=\sum_{j=0}^{\lfloor (h-1)/3\rfloor}d^{h-1-3j}+\mathbf 1_{\{3\mid h\}}.
\]
Then
\[
\gamma(T_{d,h})=F_{d,h},\qquad
\zeta(T_{d,h})=\begin{cases}d+1,&3\mid h,\\1,&3\nmid h.\end{cases}
\]
Every optimum is described explicitly as follows; the indicated unions contain all vertices on the specified levels:

1. If \(h\equiv1\pmod 3\), there is a unique optimum, \(L_{h-1}\cup L_{h-4}\cup\cdots\cup L_0\).
2. If \(h\equiv2\pmod 3\), there is a unique optimum, \(L_{h-1}\cup L_{h-4}\cup\cdots\cup L_1\).
3. If \(3\mid h\), every optimum consists of \(L_{h-1}\cup L_{h-4}\cup\cdots\cup L_2\), together with exactly one vertex chosen from \(L_0\cup L_1\). Thus there are \(d+1\) optima.

Let \(X\subseteq L_h\) be any collection of deleted leaves such that **each vertex of \(L_{h-1}\) retains at least two children** in \(T_{d,h}-X\). Then \(T_{d,h}-X\) has exactly the same minimum dominating sets (viewed as subsets of its retained vertices) as \(T_{d,h}\):
\[
\gamma(T_{d,h}-X)=\gamma(T_{d,h}),\qquad
\zeta(T_{d,h}-X)=\zeta(T_{d,h}).
\]
This includes simultaneous deletion of up to \(d-2\) leaves in *every* bottom sibling group—up to \((d-2)d^{h-1}\) terminal vertices overall—without changing a single optimum, giving nontrivial boundary resilience for every \(d\ge3\).

The retention threshold is sharp. If \(X\) consists of exactly \(d-1\) children of a *single* vertex of \(L_{h-1}\) (and no other deletions), then
\[
\gamma(T_{d,h}-X)=\gamma(T_{d,h}),\qquad
\zeta(T_{d,h}-X)=2\zeta(T_{d,h}).
\]
For \(d=2\), the one-leaf doubling agrees with the known binary-tree result. The new uniform higher-branching law exhibits a qualitative distinction: single leaf deletion changes no optimum for \(d\ge3\), whereas deletion of all but one sibling leaf creates precisely one binary choice per original optimum.

## Assumptions and scope
Graphs are finite, simple, undirected, and unweighted. A dominating set \(D\subseteq V(G)\) satisfies \(V(G)=\bigcup_{v\in D}N[v]\), where \(N[v]\) is the closed neighborhood. Vertices are distinct, so minimum sets are counted as actual vertex subsets, not up to automorphism. Height counts edges from root to leaves, and only last-level leaves are deleted. The theorem holds for all integers \(d\ge2\), \(h\ge1\). The first closed formula is not claimed as a new result restricted to \(d=2\); the known binary case is credited below.

## Proof
**1. Exact dynamic-programming states.** For a rooted subtree of height \(t\), define three mutually exclusive boundary states. State \(A_t\): the root is selected and all vertices are dominated. State \(B_t\): the root is unselected, dominated by at least one selected child, and every vertex is dominated. State \(C_t\): the root and all its children are unselected, all other vertices are dominated, and the root awaits domination by its parent. In each state record the minimum selected cardinality and the count of minimum configurations; impossible states have cardinality \(+\infty\) and count zero.

At height zero, the cost-count pairs for \((A_0,B_0,C_0)\) are \(((1,1),(+\infty,0),(0,1))\). For larger height, let child state costs be \((a,b,c)\) and optimum counts \((\alpha,\beta,\chi)\). The root-included cost is \(1+d\min(a,b,c)\); its count is the \(d\)-th power of the sum of counts of all children states attaining this minimum. The root-undominated cost is \(db\), with count \(\beta^d\). The root-excluded-but-dominated cost minimizes \(ja+(d-j)b\) over integers \(1\le j\le d\); the count sums \(\binom dj\alpha^j\beta^{d-j}\) over minimizing \(j\). These formulas are exact because disjoint child subtrees are independent after conditioning on the root state, and in state \(B\) at least one child must be selected.

The first positive heights give the following costs:
\[
\begin{array}{c|ccc|c}
 t&A_t&B_t&C_t&\gamma(T_{d,t})\\\hline
 1&1&d&+\infty&1\\
 2&d+1&d&d^2&d\\
 3&d^2+1&d^2+1&d^2&d^2+1
\end{array}
\]
At height three, the minimizing counts for \(A_3,B_3,C_3\) are respectively \(1,d,1\).

**2. Three-phase induction.** Write \(g_t=\min(A_t,B_t)\). For all \(t\ge3\), induction using the recurrences yields this exact state-cost-and-count profile:

- For \(t\equiv0\pmod3\): costs \((g_t,g_t,g_t-1)\), with minimizing counts \((1,d,1)\).
- For \(t\equiv1\pmod3\): costs \((g_t,g_t+d-1,g_t+d-1)\), with the \(A\)-state uniquely minimized (its count is one).
- For \(t\equiv2\pmod3\): costs \((g_t+1,g_t,g_t+d(d-1))\), with counts one in each of states \(A\) and \(B\).

For clarity, the three inductive transitions are explicit. From the first profile, the next costs are \((1+d(g_t-1),dg_t,dg_t)\); thus the next root-selected state is uniquely optimal, because its children must all be in the unique root-undominated state. From the second profile, the next costs are \((1+dg_t,dg_t,d(g_t+d-1))\), with the next root-excluded-but-dominated state uniquely optimal because all children are in their unique root-selected state. From the third profile, the next costs are \((1+dg_t,1+dg_t,dg_t)\): the first state has one minimizer, while the second has exactly \(d\), corresponding to the choice of the unique selected child. This establishes the asserted profiles for all heights.

Only states \(A\) and \(B\) dominate the *entire* tree, so the optimal cardinalities are \(g_t\) and the numbers of optimum sets are \(1,1,d+1\) according to \(t\bmod3\). The corresponding cardinalities satisfy \(g_1=1\), \(g_2=d\), \(g_3=d^2+1\), and \(g_t=d^{t-1}+g_{t-3}\) for \(t\ge4\). Solving this recurrence gives \(F_{d,h}\).

**3. Exhaustive structural description.** The level sets listed in the theorem dominate: selecting a level dominates that level and its immediate predecessor and successor; these level neighborhoods partition all depths in successive blocks of three. For \(3\mid h\), the final root is dominated by any chosen vertex of \(L_0\cup L_1\). Their sizes are \(F_{d,h}\), so they are minimum. There is exactly one such set in the first two congruence classes and exactly \(d+1\) in the third; by the proven exact optimum counts, there cannot be any others.

**4. Retaining two children per bottom parent.** In any graph, if a vertex \(p\) has at least two pendant neighbors, then every minimum dominating set contains \(p\): otherwise all these leaves must be selected, and replacing them by \(p\) gives a smaller dominating set. No minimum set contains such a leaf along with \(p\), since deleting that leaf preserves domination. Apply this fact to every vertex of \(L_{h-1}\) in both the full and the pruned tree. Every minimum set in either graph contains all of \(L_{h-1}\), contains no depth-\(h\) leaf, and satisfies precisely the same domination constraints on the unchanged internal vertices. Thus the families of minimum dominating sets, not only their sizes, coincide.

**5. Sharp single-group transition.** Let \(p\in L_{h-1}\) be the only bottom parent left with just one child \(u\) after pruning its other \(d-1\) leaves. Every other bottom parent is still forced into every minimum set. Every optimum \(S\) of the original graph contains \(p\). Both \(S\) and \((S\setminus\{p\})\cup\{u\}\) dominate the pruned graph: the latter dominates \(p\) with \(u\), and, if \(h\ge2\), the parent of \(p\) is dominated by another (still selected) sibling of \(p\) because \(d\ge2\). When \(h=1\), \(p\) is the root and is directly dominated by \(u\). Their cardinalities equal \(\gamma(T_{d,h})\), showing that pruning does not raise the minimum.

Conversely, any minimum set of the pruned graph must choose \(p\) or \(u\), because \(u\) is a leaf. It cannot choose both, as \(u\) would be redundant. Replace \(u\) by \(p\) if necessary; the resulting set has the same size and dominates the *original* tree, since \(p\) covers every reattached leaf. This proves that pruning cannot reduce the minimum, and that every pruned optimum maps to an original optimum, with at most the two stated preimages. The two constructions supply both preimages for every original optimum. Hence the optimum count is exactly doubled. \(\square\)

## Verification
The included standalone file `verify.py` builds explicit rooted trees and independently evaluates the minimum-cardinality/count pairs by bottom-up dynamic programming on the actual adjacency structures. It compares the theorem against 25 full-tree instances, 75 independent multi-group leaf-pruning instances, and 25 one-group threshold instances. It additionally exhaustively enumerates subsets below and at optimum size for 18 small full/pruned instances, checking both minimality and exact counts, and explicitly compares every minimum vertex set in nine instances with the closed structural classification. Reproduce using `python3 verify.py` (Python standard library only); the expected terminal marker is `VERIFY_OK`. The finite checks corroborate but do not substitute for the preceding all-parameter proof.

## Relationship to prior work
Allagan, Gray, Sawyer and Morgan (arXiv:2601.03485, first version January 7, 2026), Theorem 10, establish the binary \(d=2\) period-three dominion law, and their Corollary 12 establishes doubling under deletion of one leaf in that binary case. Their Theorem 14 describes a general three-state dynamic program for arbitrary trees. The present result specializes that method analytically to **all branching degrees**, supplies a complete optimum classification, and proves a new sharp **two-surviving-leaves** resilience threshold for arbitrary simultaneous last-level deletions.

Oyewumi, Roux and Wagner (2025) consider the number of **all** dominating sets across \(d\)-ary tree shapes, including extremal caterpillars; that quantity and their extremal problem differ from the minimum-set count here. Neither source is claimed to have introduced the simple support-vertex exchange observation. The novelty claimed is only the complete higher-branching classification and the sharp structured-pruning law, not the binary theorem, general tree dynamic programming, or the elementary local exchange principle.

## Limitations
The structural census assumes a perfect rooted tree with uniform integer branching \(d\ge2\). The invariance theorem permits multiple deleted *terminal* leaves provided each bottom parent retains at least two; it does not extend to internal deletions, arbitrary nonuniform trees, or arbitrary deletion patterns leaving zero or one leaf in multiple sibling groups. The doubling result addresses exactly one sibling group reduced to one leaf, not simultaneous exceptional groups. Independent mathematical and priority assessment remain outstanding.

## References
1. J. Allagan, E. Gray, J. Sawyer, and G. Morgan, *Four Dominion Growth Regimes in Trees: Forcing, Fibonacci Enumeration, Periodicity, and Stability*, arXiv:2601.03485v1 (January 7, 2026), https://arxiv.org/html/2601.03485v1 . Relevant material: Theorems 10, 11, 14; Corollary 12.
2. O. Oyewumi, A. Roux, and S. Wagner, *The number of dominating sets in d-ary trees*, Afrika Matematika 36, article 142 (2025), https://doi.org/10.1007/s13370-025-01360-3 . The focus is total dominating-set enumeration across tree shapes, not the number of cardinality-minimizing dominating sets.
