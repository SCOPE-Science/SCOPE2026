# Exact Littlestone dimension of rank-two Kneser graph neighborhoods

## Finding
For every integer \(n\ge 3\), let \(\operatorname{KG}(n,2)\) be the graph on the two-element subsets of \([n]=\{1,\ldots,n\}\), with distinct vertices adjacent exactly when they are disjoint. Its open-neighborhood concept class is
\[
\mathcal H_n=\{\,N(Y)=\{X\in\tbinom{[n]}2:X\cap Y=\varnothing\}:Y\in\tbinom{[n]}2\,\}.
\]
Then its (deterministic, realizable) Littlestone dimension is exactly
\[
\operatorname{Ldim}(\mathcal H_n)=\min\{4,n-3\}\qquad(n\ge3).
\]
Thus the exact values are \(0,1,2,3\) for \(n=3,4,5,6\), respectively, and the dimension stabilizes at \(4\) for all \(n\ge7\). In online prediction, this gives the exact optimal worst-case number of mistakes for this concept class.

## Assumptions and scope
A binary decision tree of depth \(d\) has a query \(X\in\tbinom{[n]}2\) at every internal node. It is **shattered** by \(\mathcal H_n\) if for each of its \(2^d\) binary paths there is a single hypothesis \(N(Y)\) assigning every encountered query its requested label, with label \(1\) meaning \(X\cap Y=\varnothing\). Repeated queries across distinct nodes are permitted. A concept class with no depth-one shattered tree has dimension \(0\).

For convenience the finite certificates encode the complementary *intersection* labels: `overlap` means \(X\cap Y\ne\varnothing\) and `disjoint` means \(X\cap Y=\varnothing\). Complementing all labels exchanges the children at every node and leaves Littlestone dimension unchanged. No graph loops are inserted: a vertex \(Y\) is not in its own open neighborhood, because it is not disjoint from itself.

## Proof
**Uniform upper bound of four.** Fix an unknown target pair \(Y\). Work with the complementary intersection predicate. Maintain a subset \(S\subseteq[n]\), initially empty, and predict that a queried pair \(X\) intersects \(Y\) exactly when \(X\cap S\ne\varnothing\). After an erroneous prediction of *disjoint* on an intersecting pair, update \(S\leftarrow S\cup X\). At least one previously unmarked member of \(Y\) enters \(S\); no previously marked true member is removed by any update. Consequently there are at most two such errors. Each introduces at most one non-target member of \(S\). After an erroneous prediction of *intersecting* on a disjoint pair, update \(S\leftarrow S\setminus X\). At least one marked non-target member is removed and no target member is removed. Therefore there are at most two errors of this second kind. The learner makes at most four mistakes on every realizable adaptive sequence. If a depth-five shattered decision tree existed, an adversary could follow the branch opposite each deterministic prediction, forcing five mistakes while the chosen path remains realizable. Thus \(\operatorname{Ldim}(\mathcal H_n)\le4\) for all \(n\).

**Sharper small-order upper bounds.** At the root, fix an arbitrary query \(X\). Exactly \(\binom{n-2}{2}\) target pairs are disjoint from \(X\), and exactly \(2n-3\) intersect \(X\). Every complete depth-\(d\) shattered subtree needs at least \(2^d\) distinct target hypotheses: distinct binary paths cannot be realized by the same hypothesis. For \(n=3\) the disjoint root branch is empty, so depth one is impossible. For \(n=4,5,6\), the disjoint branch has respectively \(1,3,6\) target pairs, ruling out depths \(2,3,4\), respectively. This yields the upper bounds \(0,1,2,3\) in those cases.

**Matching lower bounds.** The file `witness_trees.json` gives explicit complete shattered trees of depths \(1,2,3,4\) for \(n=4,5,6,7\), respectively. An internal node gives its query pair and its two child nodes. Each leaf explicitly supplies a target pair realizing all the labels on that path. The independent verifier `verify.py` checks the node formats, depth, all paths and every leaf's disjointness/intersection assertions. For \(n=3\), dimension \(0\) is attained automatically. For \(n>7\), all queries and targets in the depth-four tree on \([7]\) remain valid pairs on \([n]\) with unchanged intersections. These lower bounds match the two upper bounds for every \(n\ge3\).

## Verification
From the directory containing the two standalone artifacts, execute `python3 verify.py` using only Python's standard library. It verifies \(2+4+8+16=30\) terminal paths and every query/target condition. It also exhaustively checks that none of the \(\binom{21}{4}=5985\) four-vertex subsets of \(\operatorname{KG}(7,2)\) is shattered by the ordinary, nonadaptive open-neighborhood VC test. This latter finite comparison illustrates the distinction between the two dimensions; it is not needed for the Littlestone-dimension theorem. The uniform upper bound and all lower-bound extensions beyond \(n=7\) are proved mathematically above, not inferred from finite experimentation.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1] determine VC bounds and VC density for adjacency in Johnson and Hamming graphs. Their Johnson adjacency at rank two is **one-point intersection**, whereas the present Kneser adjacency is **disjointness**; they do not give adaptive Littlestone dimensions for these graphs. Guingona, Kolesnikov, Nierwinski and Soucy [2] compute Littlestone dimensions of zero-set classes of linear combinations, not pair-disjointness neighborhoods. Filmus, Hanneke, Mehalel and Moran [3] explain why Littlestone dimension exactly controls deterministic realizable mistake bounds but do not supply this family-specific value. The present theorem gives the exact finite-order transition \(0,1,2,3,4\) and the explicit sharp adversarial depth-four witness. These cited general results motivate but do not, as stated, imply the formula. Priority against unindexed equivalent sparse-disjunction results remains a residual risk.

## Limitations
The theorem concerns ordinary (non-randomized) Littlestone dimension for open neighborhoods and rank exactly two. It does not determine the corresponding dimensions for \(\operatorname{KG}(n,k)\) with \(k\ge3\), randomized optimal mistake counts, or unrelated neighborhood operators. The tree certificate establishes the finite lower bounds, while the all-order upper bound is a separate proof. No claim of exhaustive literature priority or independent external validation is made.

## References
1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (initial posting 2020-07-31), https://arxiv.org/abs/2007.16042.
2. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (initial posting 2021-09-10), https://arxiv.org/abs/2109.04805.
3. Y. Filmus, S. Hanneke, I. Mehalel, S. Moran, *Optimal Prediction Using Expert Advice and Randomized Littlestone Dimension*, arXiv:2302.13849 (initial posting 2023-02-27), https://arxiv.org/abs/2302.13849.
