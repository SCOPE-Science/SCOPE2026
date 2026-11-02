# Exact static and online shattering of complete hierarchical frontiers

## Finding

Let \(h\ge1\) and let \(b_1,\ldots,b_h\) be arbitrary **positive integers**. Construct a finite rooted tree \(T\) in which every vertex at depth \(i-1\) has exactly \(b_i\) children, for \(1\le i\le h\). Let \(\mathcal F(T)\) be the set of all maximal antichains in the ancestor poset of \(T\), represented as Boolean subsets of the **whole vertex set**. Equivalently, each hypothesis is a *complete prefix code*, or a frontier meeting every root-to-leaf path in exactly one vertex. The only permitted binary query is whether a vertex lies in the unknown frontier.

**Theorem.** For every such tree, with no lower bound on any \(b_i\) beyond positivity,
\[
\operatorname{VCdim}(\mathcal F(T))
=\operatorname{Ldim}(\mathcal F(T))
=\prod_{i=1}^{h-1} b_i.
\]
The empty product equals \(1\), so the height-one case has both dimensions \(1\). The common value is exactly the number of parents of leaves, independent of the number \(b_h\) of children of each such parent. In realizable online vertex-membership prediction this also gives the optimal worst-case mistake budget.

For the complete binary tree of height \(h\), put \(N_h=|\mathcal F(T)|\). Then \(N_0=1\) and \(N_h=1+N_{h-1}^{2}\). In particular, \((N_1,N_2,N_3,N_4,N_5)=(2,5,26,677,458330)\). For every \(h\ge2\), the entropy upper bound exceeds the optimal online mistake budget by at least
\[
\lfloor\log_2 N_h\rfloor-2^{h-1}
\ge \left\lfloor\left(\frac{\log_2 5}{2}-1\right)2^{h-1}\right\rfloor.
\]
Thus this elementary hierarchical concept class has an exponentially increasing additive gap between its hypothesis-count bound and its true Littlestone dimension, **without any gap between VC and Littlestone dimensions**. At height four there are \(677\) hypotheses but both dimensions are \(8\), not the entropy ceiling \(9\).

## Assumptions and scope

All trees and all concept classes are finite. Tree depth is measured in edges, with root at depth \(0\) and leaves at depth \(h\); the convention for maximal antichains includes the root singleton and leaf-level frontier. For every nonempty finite class \(\mathcal C\), \(\operatorname{Ldim}(\mathcal C)\) is the maximum depth of a full binary membership-query tree all of whose paths are realizable by a concept in \(\mathcal C\). The Littlestone dimension of a singleton concept class is \(0\). The VC dimension concerns fixed sets of vertex coordinates. These are **not** classes of arbitrary downsets, all antichains, fixed-size frontiers, or hypotheses queried by their induced leaf partitions.

## Proof

**1. The VC dimension.** Write \(m=\prod_{i=1}^{h-1}b_i\), and let \(P\) be the \(m\) vertices at depth \(h-1\). For every binary labeling of \(P\), form a frontier by taking the labeled-one vertices of \(P\), and for each labeled-zero vertex of \(P\), taking all its children. These choices are independent and meet each root-to-leaf path exactly once. Hence \(P\) is shattered, so \(\operatorname{VCdim}\ge m\).

Conversely, a shattered set \(S\) is necessarily an antichain: a frontier cannot contain two comparable vertices, yet shattering must realize the all-one labeling on \(S\). For each \(p\in P\), write \(B_p\) for the block consisting of \(p\) and its children. Two members of \(B_p\) cannot lie together in \(S\): a parent and child are comparable, whereas two distinct children of \(p\) always occur together whenever either occurs in any complete frontier (otherwise that parent's other leaf-path would be missed). For each \(s\in S\) above depth \(h-1\), consider the nonempty set of blocks \(B_p\) below \(s\). If \(s\in P\) or is a leaf, take its own single block. Sets of blocks so assigned to distinct elements of \(S\) are disjoint: comparability excludes shared ancestral blocks, and the two-leaves-in-one-block exception was just ruled out. Picking a block from each assigned nonempty set injects \(S\) into \(P\). Thus \(|S|\le m\), proving \(\operatorname{VCdim}=m\).

**2. A product lemma for the online dimension.** For finite nonempty concept classes \(\mathcal A\subseteq2^X\) and \(\mathcal B\subseteq2^Y\), with disjoint query domains \(X,Y\), the direct product \(\mathcal A\otimes\mathcal B=\{A\cup B:A\in\mathcal A,B\in\mathcal B\}\) satisfies
\[
\operatorname{Ldim}(\mathcal A\otimes\mathcal B)
=\operatorname{Ldim}(\mathcal A)+\operatorname{Ldim}(\mathcal B).
\]
The lower bound grafts a complete shattered tree for \(\mathcal B\) to every leaf of one for \(\mathcal A\). For the upper bound, use the standard rank recurrence: a nonconstant query contributes \(1+\min\{d(\mathcal C_{x=0}),d(\mathcal C_{x=1})\}\), maximized over queries, and both restrictions are strict subfamilies. At an \(X\)-query, at least one restriction of \(\mathcal A\) has rank strictly below \(d(\mathcal A)\), and no restriction has greater rank. Induction on the number of pairs of concepts bounds the product's two branches by the corresponding restricted ranks plus \(d(\mathcal B)\), so their minimum is at most \(d(\mathcal A)+d(\mathcal B)-1\). The same argument applies at a \(Y\)-query. This proves the upper bound, including singleton factors.

**3. The online upper bound.** Induct on height. A height-zero tree has a single frontier and online dimension \(0\). At height one the two frontiers (root, or every child) have online dimension \(1\). At general height \(h\), fix a query vertex \(v\) at depth \(d\) and restrict to frontiers that contain \(v\). Such a frontier contains no other vertex on the root-to-\(v\) path, and consists independently of one maximal frontier in each *sibling subtree* hanging off that path. There are \(b_i-1\) such sibling subtrees at level \(i\), each having remaining branching sequence \(b_{i+1},\ldots,b_h\). By induction and the product lemma, the online dimension of this positive restriction is
\[
D_v=\sum_{i=1}^{\min(d,h-1)}(b_i-1)\prod_{j=i+1}^{h-1}b_j.
\]
(The last-level sibling subtrees are leaves of dimension \(0\).) Every term is nonnegative, and the full sum telescopes to
\[
D_v\le\sum_{i=1}^{h-1}(b_i-1)\prod_{j=i+1}^{h-1}b_j
=\prod_{i=1}^{h-1}b_i-1=m-1.
\]
For a nonempty finite class the first-query recurrence implies that every shattered decision tree of positive depth has dimension at most one plus the largest dimension of one of its positive first-query restrictions. Therefore \(\operatorname{Ldim}(\mathcal F(T))\le1+(m-1)=m\). The general inequality \(\operatorname{VCdim}\le\operatorname{Ldim}\) and Step 1 give the reverse inequality.

**4. Entropy slack.** In the binary case the root-only frontier and the independent two child frontiers yield \(N_h=1+N_{h-1}^2\). For \(h\ge3\), \(\log_2 N_h>2\log_2 N_{h-1}\). Starting from \(N_2=5\), it follows that \(\log_2N_h\ge(\log_2 5/2)\,2^{h-1}\) for all \(h\ge2\). Subtract the integer \(2^{h-1}\) and take floors to obtain the stated bound. It is strictly positive from \(h=4\) onward and grows linearly with the true online dimension. The lower height examples follow directly from the recurrence.

## Verification

The standalone `verify_frontiers.py` constructs frontiers recursively **without relying on the formula**, evaluates exact VC shattering by subset projections, and evaluates the complete Littlestone rank recurrence on the resulting finite class. It checks 29 level-branching profiles of height at most three, including unary levels. For the complete binary height-four tree and two mixed profiles it repeats the exact online recurrence and independently checks an explicit shattered last-parent support and the local block obstruction. It also checks the binary frontier-count recurrence and entropy-slope examples through height ten. Execute with `python3 verify_frontiers.py`. Its output is not needed to establish the universal theorem, whose proof above covers all positive integer branching profiles.

## Relationship to prior work

Bhaskar's *Thicket Density* (first publicly submitted 2017-02-13), Sections 2–3, supplies the general adaptive-shattering definition and basic recursive viewpoint; it does not classify maximal-antichain frontiers of level-regular trees. Walker's *Tree Dimension and the Sauer–Shelah Dichotomy* (2022), Sections 1–2, studies the combinatorial complexity of **leaf subsets of decision trees**, not the membership-query concept class whose **hypotheses are maximal prefix-code frontiers**. Darnstädt, Ries and Simon's *Hierarchical Design of Fast Minimum Disagreement Algorithms* (2017 preprint, 2018 journal), Sections 2.3 and 4, explicitly represents hierarchical partitions by maximal antichains and describes the root-versus-product recursion, but investigates weighted empirical-error optimization rather than the exact VC/Littlestone dimensions of the frontier family. Ghazi et al.'s *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions* (2020), Sections 2--3, establishes general aggregation bounds of order \(O(kd\log k)\) and threshold-dimension bounds; these do not specialize to an exact all-height frontier formula. Standard product additivity and the fact that Littlestone dimension equals the optimal realizable mistake budget are used as established learning-theoretic tools, not claimed as new.

## Limitations

The exact equality requires all vertices at a given depth to have the same number of children, and **membership queries on the original tree vertices**. It does not assert the analogous equality for arbitrary nonuniform rooted trees; neither fixed-frontier-cardinality subfamilies nor more expressive queries are covered. An independently conducted mathematical audit and an exhaustive historical-priority audit have not been performed. The online-dimension claim is a theorem of the explicit definitions and proof above, not a claim of independent certification.

## References

1. Siddharth Bhaskar, *Thicket Density*, arXiv:1702.03956, first public version 2017-02-13, https://arxiv.org/abs/1702.03956 .
2. Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first public version 2022-03-23, https://arxiv.org/html/2203.12211v2 .
3. Malte Darnstädt, Christoph Ries, Hans Ulrich Simon, *Hierarchical Design of Fast Minimum Disagreement Algorithms*, Theoretical Computer Science 716 (2018), 70–88; preprint https://www.ruhr-uni-bochum.de/lmi/ries/MinDis_TCS2018.pdf .
4. Badih Ghazi, Noah Golowich, Ravi Kumar, Pasin Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, arXiv:2007.03668, https://arxiv.org/abs/2007.03668 .
