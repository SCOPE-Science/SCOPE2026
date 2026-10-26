# Sharp extremal online-shattering capacity of rooted-tree leaf paths

## Finding

Let \(T\) be a finite nonempty rooted tree, with \(L\) leaves and \(I\) nonleaf vertices. For each leaf \(\ell\), let \(P_\ell\subseteq V(T)\) be the full vertex set of the path from the root to \(\ell\), and put \(\mathcal H_T=\{\mathbf1_{P_\ell}:\ell\text{ is a leaf}\}\). A query is membership of a *vertex* in the unknown leaf path. For each pair of integers \(I,L\ge1\), the greatest Littlestone dimension among trees with exactly \(I\) nonleaf vertices and \(L\) leaves is

\[
\max_{T:\,I(T)=I,\ L(T)=L}\operatorname{Ldim}(\mathcal H_T)
=\min\left\{\left\lfloor\log_2 L\right\rfloor,\ 1+\left\lfloor\log_2 I\right\rfloor\right\}.
\]

In particular, for every integer \(d\ge1\), the smallest order of a rooted tree with \(\operatorname{Ldim}(\mathcal H_T)\ge d\) is exactly \(3\cdot2^{d-1}\). Equivalently, the maximum Littlestone dimension of such a class among rooted trees of order \(n\) is zero for \(n\le2\), and for \(n\ge3\) equals

\[
1+\left\lfloor\log_2(n/3)\right\rfloor.
\]

Every \(\mathcal H_T\) has VC dimension at most one, with equality whenever \(L\ge2\). The sharp exponential witness-size law therefore holds inside a VC-dimension-one family.

## Assumptions and scope

Trees are finite, undirected, connected and acyclic, with a distinguished root; unary vertices are allowed. A leaf is a vertex with no *children* in this rooted orientation (so the root of the one-vertex tree is a leaf). A nonleaf is a vertex with at least one child. All root-to-leaf paths include both endpoints. Distinct leaves give distinct concepts because a leaf belongs to its own path but no other leaf path. The Littlestone dimension is the largest depth \(d\) of a complete binary query tree whose every binary-labeled root-to-leaf history is consistent with at least one concept. For a singleton concept class its dimension is zero.

The bivariate formula is a **maximum over tree shapes** with the indicated parameters. It does not assert that every tree with \(I\) nonleaves and \(L\) leaves has that dimension. If \(I=0\), the tree consists of one vertex, \(L=1\), and its dimension is zero.

## Proof

**1. Laminar-query non-repetition.** For a vertex \(v\), let \(S_v\) be the set of leaves descending from \(v\). A query at \(v\) accepts precisely the concepts indexed by \(S_v\). For any two vertices \(u,v\), the leaf sets \(S_u,S_v\) are nested or disjoint. No vertex can label two distinct nodes in a completely shattered binary query tree: a repeat along one history has a previously fixed answer. If two occurrences are incomparable, let \(u\) label their least common ancestor in the query tree, and let \(v\) be the repeated queried vertex. If \(S_v\subseteq S_u\) or \(S_v\cap S_u=\varnothing\), the answer to \(v\) is fixed to zero on the negative or positive branch, respectively. If \(S_u\subseteq S_v\), the answer to \(v\) is fixed to one on the positive branch. Thus \(v\) cannot be a shattering query on both branches, a contradiction. This uses the actual laminarity of *subtree leaf sets*, not merely their sizes.

**2. Upper bounds.** A shattered complete depth-\(d\) binary query tree requires \(2^d\) distinct concepts, so \(L\ge2^d\). Suppose \(d\ge1\). All query nodes on levels \(0,\ldots,d-2\) have a positive branch with at least two consistent leaves; hence none can query a leaf vertex of \(T\), because membership at a leaf selects only its unique concept. They also cannot query the root, which is present in every concept and cannot split a nonempty version space. There are \(2^{d-1}-1\) such nodes, and step 1 makes their query vertices distinct. Therefore at least \(2^{d-1}-1\) internal nonroot vertices occur, in addition to the underlying root. Consequently \(I\ge2^{d-1}\). Combining the two inequalities gives

\[
\operatorname{Ldim}(\mathcal H_T)\le
\min\left\{\lfloor\log_2 L\rfloor,\ 1+\lfloor\log_2 I\rfloor\right\}
\]

when \(I\ge1\). The \(d=0\) case is automatic.

**3. Sharp recursive witnesses.** Define \(T_1\) to be a root with two leaf children. It has two leaves, one nonleaf and a shattered depth-one query (ask about either leaf). Inductively take disjoint copies \(A\) and \(B\) of \(T_d\); attach the root of \(A\) as one more child of the root of \(B\), retaining the latter as the new root. The leaves of \(A\) and \(B\) remain leaves; no former nonleaf changes status. Querying the root of \(A\) separates the two sets of leaf paths exactly. The positive and negative branches each simulate a depth-\(d\) shattered query tree in their respective copy, so the combined class shatters depth \(d+1\). At every depth \(d\ge1\), this construction has exactly \(2^d\) leaves, \(2^{d-1}\) nonleaves and \(3\cdot2^{d-1}\) vertices. The leaf-count bound gives the matching upper dimension \(d\).

**4. All bivariate parameter pairs.** Given arbitrary \(I,L\ge1\), set \(d=\min\{\lfloor\log_2 L\rfloor,1+\lfloor\log_2 I\rfloor\}\). If \(d\ge1\), begin with \(T_d\); add \(L-2^d\) new leaves as children of its root, and subdivide existing edges \(I-2^{d-1}\) times. The two operations preserve, respectively, the nonleaf count and the leaf count, and both retain all old membership-query responses on the original concepts and vertices. Hence the depth-\(d\) shattered tree survives. If \(d=0\) then necessarily \(L=1\), and a rooted path with \(I\) nonleaves realizes the value zero. This proves the exact bivariate maximum.

**5. Fixed total order and VC dimension.** Any tree shattering depth \(d\ge1\) has at least \(2^d+2^{d-1}=3\cdot2^{d-1}\) vertices by step 2, and step 3 attains equality. Adding new leaf children to an extremizer's root provides every larger order without destroying its shattered tree. This proves the fixed-order formula. Finally, for any two query vertices, if one is an ancestor of the other then a descendant-positive/ancestor-negative labeling is impossible; if incomparable, a both-positive labeling is impossible. Thus no pair is VC-shattered. If \(L\ge2\), a leaf-vertex query has both answers among the concepts, so VC dimension is exactly one.

## Verification

The standalone standard-library script `verify_leafpath_extremal.py` computes Littlestone dimension independently using the exact version-space recursion

\[
D(H)=\max_{q:\,\varnothing\neq H\cap S_q\neq H}
\left(1+\min\{D(H\cap S_q),D(H\setminus S_q)\}\right),
\]

with \(D(H)=0\) when no query splits \(H\). It exhaustively generates every unlabeled rooted tree of orders one through twelve, 7,813 shapes in total, and checks the sharp bivariate extremal dimension separately for every feasible \((I,L)\) at those orders. It also recursively constructs the explicit extremizers and verifies all paths of complete shattered query trees of depths one through five (respectively 2, 4, 8, 16, 32 paths), plus an independent exact recurrence on the first three constructed extremizers. The output `verify_leafpath_extremal.out` ends with `ALL_EXACT_CHECKS_PASS`. The infinite theorem relies on the foregoing proof, not on any finite enumeration.

To reproduce from the directory containing the two files: `python3 verify_leafpath_extremal.py`. No external package is required.

## Relationship to prior work

Walker, *Tree Dimension and the Sauer–Shelah Dichotomy* (2022), studies embeddings into binary-branch posets and extremal leaf sets, using tree dimension to deduce VC and Littlestone shatter-function bounds. Here the object is different: leaf-indexed **membership concepts on an arbitrary rooted tree**, and the measured resource is the number of vertices or nonleaf vertices required for a complete adaptive query tree. An embedded binary subtree is neither the same object as a Littlestone mistake tree nor an implication giving the sharp \(I\)-bound; a comb of many leaves already distinguishes the two notions.

Chase–Freitag–Reyzin (2023), Ghazi–Golowich–Kumar–Manurangsi (2020), and Malliaris–Moran (2021) treat general Littlestone learning, closure, query complexity or stability. Their results motivate the dimension, but the inspected material does not supply the exact leaf/nonleaf extremal law. General hypothesis counting supplies only \(L\ge2^d\); the additional sharp bound \(I\ge2^{d-1}\) arises here from non-reuse of laminar subtree-membership queries. Historical priority beyond the consulted sources is not certified.

## Limitations

This is an exact **extremal** theorem, not a formula for the dimension of each individual rooted tree. It assumes full root-to-leaf paths and vertex-membership queries, rather than arbitrary graph paths, edge queries, or general laminar classes with a different representation cost. Although the mathematical proof covers every positive integer depth, finite verification alone cannot establish that assertion. No independent scientific validation or exhaustive historical-priority search is claimed.

## References

1. Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted 2022-03-23. https://arxiv.org/abs/2203.12211
2. Hunter Chase, James Freitag and Lev Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812, first posted 2023-10-07. https://arxiv.org/abs/2310.04812
3. Badih Ghazi, Noah Golowich, Ravi Kumar and Pasin Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668, first posted 2020-07-07. https://arxiv.org/abs/2007.03668
4. Maryanthe Malliaris and Shay Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, first posted 2021-08-12. https://arxiv.org/abs/2108.05569
