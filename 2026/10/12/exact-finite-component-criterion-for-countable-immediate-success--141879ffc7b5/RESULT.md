# Exact finite-component criterion for countable immediate-successor graphs

## Finding

Let \(G=(V,E)\) be a nonempty countable directed graph, functional and inverse-functional, without directed cycles, and with a positive finite number of weakly connected components. Write \(f\) for the number of **finite** path components (isolated vertices included), and \(z\) for the number of components that are **two-way infinite** directed paths (order type \(\mathbb Z\)). Then \(E\) is exactly the immediate-successor relation of a strict linear order on \(V\) if and only if
\[
\boxed{f\le z+1.}
\]
The number of additional disjoint \(\mathbb Z\)-path components needed to make such a graph an exact successor relation is exactly
\[
\boxed{\max\{0,f-z-1\}.}
\]
In the second assertion, extensions are restricted to adding whole, vertex-disjoint two-way infinite directed paths without changing existing vertices or edges.

## Assumptions and scope

"Exact immediate successor" means that there exists a strict total order \(<\) on the given vertex set satisfying, for every \(u,v\in V\),
\[
E(u,v)\quad\Longleftrightarrow\quad u<v\ \land\ \neg\exists w\in V\ (u<w<v).
\]
Functional means at most one outgoing edge per vertex; inverse-functional means at most one incoming edge; acyclic means no directed cycle of any positive length. Weak components are components after forgetting edge orientations. Every such weak component is a directed path of one of four types: finite nonempty, \(\omega\), \(\omega^{*}\), or \(\mathbb Z\). The classification concerns finitely many components, not arbitrary infinitely many component sets. The countability assumption follows from these path types and finite component number but is retained to state the intended semantic setting explicitly.

## Proof

**Path decomposition.** Each vertex has total undirected degree at most two. At a vertex with two distinct neighbors, the functional and inverse-functional assumptions force one incoming and one outgoing edge. An undirected cycle would therefore give a directed cycle, contrary to acyclicity. Every connected component is consequently a consistently directed finite path, one-sided infinite path, or two-sided infinite path.

**Convexity.** Suppose \(<\) realizes \(E\). Along any finite directed path segment, each edge joins two immediately consecutive elements of \(<\). If \(u,v\) belong to the same weak component, they are linked by such a segment, so every point between \(u\) and \(v\) in \(<\) belongs to this component. Thus each component is order-convex. Its internal order is precisely its directed path order. Since there are finitely many components, they occur as finitely many ordered convex blocks.

**The boundary rule.** Between two consecutive components \(A<B\), an unwanted immediate-successor pair arises exactly when \(A\) has a greatest element and \(B\) has a least element. If either endpoint is absent, every \(a\in A\), \(b\in B\) has a point strictly between them. Components of types finite, \(\omega\), \(\omega^{*}\), and \(\mathbb Z\) have the respective (least, greatest) endpoint flags \((1,1)\), \((1,0)\), \((0,1)\), and \((0,0)\). Hence a block sequence is valid exactly when no adjacent pair has the preceding block's greatest flag and the following block's least flag both equal to one.

**Necessity.** Consider two consecutive finite path blocks in their order among finite blocks. If no \(\mathbb Z\)-block separates them, the intervening blocks are entirely one-sided rays. Immediately after the earlier finite block a ray, if present, must have no least point and hence be of type \(\omega^{*}\). Every subsequent ray before the next finite block must again have no least point, since \(\omega^{*}\) has a greatest point. But a final \(\omega^{*}\)-block cannot precede the later finite block, because both supply an unwanted consecutive endpoint pair. If there are no intervening blocks, the two finite blocks themselves form such a pair. Thus at least one distinct \(\mathbb Z\)-block lies between each pair of consecutive finite blocks. There are \(f-1\) such gaps when \(f\ge1\), so \(z\ge f-1\). The inequality also holds if \(f=0\).

**Sufficiency.** Assume \(f\le z+1\). Linearly order the finitely many components by placing all \(\omega\)-components first, then the \(f\) finite components with one distinct \(\mathbb Z\)-component inserted between each successive pair, then every unused \(\mathbb Z\)-component, and finally all \(\omega^{*}\)-components. If \(f=0\), omit the finite-component portion. Every boundary is allowed: an \(\omega\) or \(\mathbb Z\) block has no greatest point, and an \(\omega^{*}\) or \(\mathbb Z\) block has no least point; all remaining finite-block boundaries have an intervening \(\mathbb Z\) block. Take the lexicographic sum of the intrinsic directed orders of these path components. Its immediate-successor relation is precisely \(E\).

**Sharp buffer number.** Adding \(t\) two-way infinite components changes \(z\) to \(z+t\) and leaves \(f\) fixed. By the criterion, this makes exact realization possible if and only if \(f\le z+t+1\). The least nonnegative such \(t\) is \(\max\{0,f-z-1\}\). No claim is made about minimal numbers of new individual vertices or about extensions allowing different new component types.

## Verification

The accompanying standalone Python program `verify_successor.py` checks the endpoint rule independently via an exact dynamic program counting admissible permutations of individually labelled components, and via brute-force permutation search over all four-type strings through length five. It tested 494 four-type component-count multisets through eight components, including 130 nonrealizable multisets, and 1,364 explicit type strings through five components. The exact existential criterion agreed in every case. For smaller configurations it also verified the minimum additional two-way-infinite-buffer count. These are finite sanity checks only; the proof above establishes the general countable assertion.

## Relationship to prior work

Tóth, Kuang, Zou, Kůla, Wang, Wang and Kuželka (2026), arXiv:2608.10877, study weighted first-order model counting on ordered domains, including an implicit immediate-successor axiom. Their available abstract treats finite-domain counting and does not give this finite-component countable representability criterion. Michaliszyn and Witkowski (arXiv:2610.09758v1, first posted October 7, 2026) prove in their Lemma 3 that a countable acyclic functional and inverse-functional graph **with infinitely many components** is an exact successor graph by densely ordering the components; they also note the obstruction of two isolated vertices. Their full online text does not state a necessary-and-sufficient criterion for the complementary class with finitely many components. The present statement concerns precisely that complementary class, and its sharp buffer count is not implied by the infinitely-many-components construction.

## Limitations

The result is about the existence of **some** linear order, not an effective recovery of a computable presentation, nor the ordered model-counting complexity for general logical theories. It assumes all indegrees and outdegrees are at most one and forbids directed cycles. It does not classify infinite component quotients; dense completion of countably infinitely many components is a separately known result. We did not exhaustively search all historical order-theory literature, and an equivalent older formulation under different terminology remains possible. The 2026 weighted-counting preprint could not be examined beyond its accessible abstract, so it is not treated as negative full-text evidence.

## References

1. J. Tóth, Q. Kuang, K. Zou, V. Kůla, Y. Wang, Y. Wang, O. Kuželka, *Weighted First-Order Model Counting over Ordered Domains*, arXiv:2608.10877, first posted August 11, 2026, https://arxiv.org/abs/2608.10877.
2. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1, first posted October 7, 2026, https://arxiv.org/html/2610.09758v1; especially Definition 2 and Lemma 3.
3. D. Figueira, *Satisfiability for two-variable logic with two successor relations on finite linear orders*, arXiv:1204.2495, April 11, 2012, https://arxiv.org/abs/1204.2495.
