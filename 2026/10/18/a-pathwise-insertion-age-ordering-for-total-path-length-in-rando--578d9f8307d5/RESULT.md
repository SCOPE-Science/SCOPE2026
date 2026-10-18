# A pathwise insertion-age ordering for total path length in random binary search trees

## Finding

Let \(n\ge2\). Fix any permutation \(\tau=(\tau_1,\ldots,\tau_{n-1})\) of \(\{1,\ldots,n-1\}\). For each insertion slot \(1\le t\le n\), insert the new maximum key \(n\) into \(\tau\) at slot \(t\), construct the ordinary (unbalanced) binary search tree by sequential key insertion, and write \(P_t\) for its **total internal path length**, the sum of depths of all keys with root depth zero. Write \(P_-\) for the path length of the tree built from \(\tau\) alone. Define \(R_0=L_0=0\); for \(s\ge1\), let \(R_s=\max\{\tau_1,\dots,\tau_s\}\) and let \(L_s\) count strict left-to-right record maxima in this prefix.

The exact, deterministic identity is
\[
P_t-P_-=L_{t-1}+n-1-R_{t-1},\qquad 1\le t\le n.\tag{1}
\]
Consequently the coupling of **all** conditioned trees via the same \(\tau\) satisfies
\[
P_t-P_{t+1}=\max\{0,\tau_t-R_{t-1}-1\}\ge0,\quad1\le t<n,\tag{2}
\]
so that \(P_1\ge P_2\ge\cdots\ge P_n\) for every \(\tau\), and \(P_{n-1}=P_n\) identically. If \(\tau\) is uniform, the law of \(P_t\) is precisely the law of total path length in a uniform random binary search tree of size \(n\), **conditioned on the maximum key being inserted in position** \(t\). Hence these complete conditional laws are ordered in usual stochastic order; the inequality is strict for \(1\le t\le n-2\) in the sense of a positive-probability strict difference in this coupling.

The distribution of each nonnegative successive gap is explicit. For \(1\le t<n\) and integers \(k\ge1\),
\[
\Pr(P_t-P_{t+1}\ge k)
=\frac{\binom{n-k-1}{t}}{(n-1)\binom{n-2}{t-1}},\tag{3}
\]
where out-of-range binomial coefficients are zero. In particular,
\[
\Pr(P_t>P_{t+1})=\frac{n-t-1}{(n-1)t},\qquad
\mathbb E(P_t-P_{t+1})=\frac{n-t-1}{t(t+1)}.\tag{4}
\]
This equality of the **final two conditional laws** is stronger than equality of expectations: the coupled total path lengths coincide individually for every base permutation.

For \(2\le t\le n\), the two summands in (1) are independent under a uniform \(\tau\), and their exact distributions give the generating function
\[
\mathbb E z^{P_t-P_-}=
\left[\prod_{h=1}^{t-1}\left(1+\frac{z-1}{h}\right)\right]
\sum_{g=0}^{n-t}\frac{\binom{n-g-2}{t-2}}{\binom{n-1}{t-1}}z^g.
\tag{5}
\]
For \(t=1\), the difference \(P_1-P_-=n-1\) deterministically. Equation (5) concerns the **increment** \(P_t-P_-\), not the full path length \(P_t\), because the increment need not be independent of \(P_-\).

## Assumptions and scope

All trees are ordinary unbalanced binary search trees formed by sequential insertion of distinct totally ordered keys. The insertion permutation is uniform when a probabilistic assertion is made. Every deterministic assertion holds for each fixed \(\tau\), and all formulas include the boundary case \(n=2\). Depth counts the number of edges from the root, so root depth is zero. The conditional event that the largest key is inserted at position \(t\) has probability \(1/n\) under a uniform permutation of \(\{1,\dots,n\}\). No equilibrium or asymptotic assumption is imposed.

## Proof

**Insertion/deletion lemma.** Consider the search tree made from the prefix \(\tau_1,\ldots,\tau_{t-1}\). Its rightmost path consists exactly of the left-to-right maximum records in that prefix, in their arrival order, so inserting the largest key \(n\) makes its depth exactly \(L_{t-1}\). Every subsequently inserted key whose value exceeds \(R_{t-1}\) passes through the newly inserted \(n\) and becomes its descendant: before \(n\) was present, such a key would have been routed to the right of the prefix maximum; in the augmented tree it enters the left subtree of \(n\). Keys at most \(R_{t-1}\) never pass through \(n\). There are exactly \(n-1-R_{t-1}\) distinct keys above the prefix maximum, all arriving later, because the prefix has already used every key \(\le R_{t-1}\) that it contains and no key above its maximum. Thus the descendant count of \(n\) in the completed tree is exactly \(n-1-R_{t-1}\).

The maximum node \(n\) has no right child. Deleting it and reconnecting its left child (if any) in its place yields exactly the tree made from \(\tau\) with \(n\) omitted: insertion of a key larger than the prefix maximum does not change the relative search-tree relationships among the remaining keys, but delays their placement one edge below \(n\). This can also be checked from the recursive definition of a search tree via its earliest-inserted root. The deletion reduces each descendant depth by one, leaves other previously present keys' depths unchanged, and removes the depth \(L_{t-1}\) of \(n\). Therefore (1) holds. For \(t=1\), the prefix is empty and all remaining \(n-1\) keys are descendants of the new root, giving \(P_1-P_-=n-1\) as required.

**Pathwise age ordering.** Put \(x=\tau_t\) and \(r=R_{t-1}\). If \(x\le r\), neither prefix record count nor prefix maximum changes between slots \(t\) and \(t+1\), hence (1) gives zero difference. If \(x>r\), record count increases by one and prefix maximum increases by \(x-r\), giving difference \(x-r-1\). This is (2). The last gap vanishes identically: if the last remaining key is a prefix record, its value is \(n-1\) and the preceding maximum is \(n-2\); otherwise it is not a record. Nonzero gaps occur with positive probability at all earlier slots (take the first \(t-1\) keys to be small and \(\tau_t\) at least two above their maximum). Conditioning a uniformly random full permutation on the insertion slot of \(n\) leaves \(\tau\) uniform, proving the stochastic-order claim.

**Exact decrement tails.** Under uniform \(\tau\), condition on \(\tau_t=x\), uniformly chosen from \(\{1,\dots,n-1\}\). The remaining \(t-1\) values before slot \(t\) form an unordered uniform subset of the other \(n-2\) values. For \(k\ge1\), (2) says that the gap is at least \(k\) exactly when all preceding values are at most \(x-k-1\). Its probability equals
\[
\frac{1}{(n-1)\binom{n-2}{t-1}}
\sum_{x=1}^{n-1}\binom{x-k-1}{t-1}
=\frac{\binom{n-k-1}{t}}{(n-1)\binom{n-2}{t-1}},
\]
using the hockey-stick identity and the zero-out-of-range convention. This proves (3) and its \(k=1\) specialization. For (4)'s mean, either sum (3) or subtract \(\mathbb E[P_t-P_-]\) from \(\mathbb E[P_{t+1}-P_-]\) as computed below. Thus no independence or stochastic-domination assumption is hidden in the argument.

**Increment distribution and mean.** A uniformly random prefix of length \(s=t-1\) has an unordered set uniformly distributed over the \(s\)-subsets of \(\{1,\ldots,n-1\}\), independent of the relative ordering of its elements. The record count \(L_s\) depends only on that relative ordering, whereas \(R_s\) depends only on the set, hence \(L_s\) and \(R_s\) are independent. The record indicators in the relative-order permutation are independent Bernoulli variables of respective probabilities \(1,1/2,\ldots,1/s\): insert each successive element into the relative ranking at its independently uniform relative rank, so being a new maximum depends only on that new rank. This gives the first factor in (5). The event \(n-1-R_s=g\) means that \(n-1-g\) is selected as the maximum and the other \(s-1\) values are smaller; therefore
\[
\Pr(n-1-R_s=g)
=\frac{\binom{n-g-2}{s-1}}{\binom{n-1}{s}},\quad0\le g\le n-1-s.
\]
The product of generating functions proves (5). By the classical sampling-without-replacement maximum formula, \(\mathbb E R_s=sn/(s+1)\); since \(\mathbb E L_s=H_s\),
\[
\mathbb E(P_t-P_-)=H_{t-1}+\frac{n-t}{t},\qquad
\mathbb E P_t=2nH_{n-1}-4(n-1)+H_{t-1}+\frac{n-t}{t}.
\tag{6}
\]
The second identity uses the classical mean total internal path length of a uniform binary search tree on \(n-1\) keys; it also follows from the usual root-splitting recurrence. Subtracting neighboring values in (6) gives the mean gap in (4), finishing the proof.

## Verification

Run `python check.py` with the Python standard library; no external packages are used. The supplied code independently constructs each binary search tree by insertion for **every** base permutation of lengths \(1\) through \(7\), corresponding to tree orders \(2\le n\le8\). It checks the deterministic identities (1)–(2), the exact rational formulas (3)–(4) for all relevant thresholds, the independence and distribution in (5), and the conditional mean in (6). All checks passed. Exhaustive checks at these finite orders are corroboration, not an infinite proof; the unrestricted result follows from the preceding combinatorial arguments.

## Relationship to prior work

The total internal path length of a random binary search tree is classical. Prodinger's 1999 preprint gives a general permutation-pair representation for path length and derives marginal moments; it provides a useful alternate route for individual identities, but the inspected material does not state the simultaneous **pathwise ordering across insertion ages of the maximum**, its complete exact decrement tails, or the final-two-slots identity. Holmgren and Janson's June 2014 probability treatment establishes broad limit theorems for fringe-subtree functionals of random binary search trees and recursive trees; its inspected principal results do not imply an exact ordering conditioned on the largest key's arrival slot. The work of Mahmoud and Pittel on insertion paths and comparisons is a plausible historical predecessor, but its full text was not available for direct comparison. These sources motivate careful assessment rather than a claim of priority certification.

## Limitations

This theorem concerns **unbalanced** binary search trees and distinct-key uniform random insertion order; it does not apply automatically to balancing schemes, weighted search trees, or other path-length conventions. The distribution formula (5) is for the incremental path length relative to the common base tree, not the entire conditional path length. The same-finite-sample coupling proves usual stochastic order but not statistical independence across conditioned variants. Earlier broad path-length enumeration may implicitly encode some formulas, and a relevant historical full text was inaccessible; independent literature-priority verification remains necessary.

## References

1. Cecilia Holmgren and Svante Janson, *Limit Laws for Functions of Fringe trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883v1 (first publicly available June 26, 2014), https://arxiv.org/abs/1406.6883.
2. Helmut Prodinger, *A q-Analogue of the Path Length of Binary Search Trees*, arXiv:math/9910070v1 (October 14, 1999), https://arxiv.org/abs/math/9910070.
3. Hosam M. Mahmoud and Boris Pittel, *On the joint distribution of the insertion path length and the number of comparisons in search trees*, Discrete Applied Mathematics, 1988, https://doi.org/10.1016/0166-218X(88)90080-7 (complete paper not accessed).
