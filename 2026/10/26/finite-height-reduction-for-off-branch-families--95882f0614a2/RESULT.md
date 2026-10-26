# Finite-height reduction for off-branch families

## Finding

Let \(T=\omega^{<\omega}\) be ordered by extension, and let \(\mathfrak{o}\) and \(\bar{\mathfrak{o}}\) be the least sizes of maximal almost-disjoint families of infinite off-branch sets and infinite antichains, respectively. If \(\mathcal O\) is a maximal off-branch family in which every member has finite chain height (with no uniform height bound required), then there is a maximal almost-disjoint family \(\mathcal B\) of infinite antichains with \(|\mathcal B|\le|\mathcal O|\). Consequently, if \(\mathfrak{o}<\bar{\mathfrak{o}}\), every \(\mathfrak{o}\)-sized maximal off-branch family contains a member of unbounded finite chain height.

## Assumptions and scope

Let \(T=\omega^{<\omega}\) be the tree of finite sequences of natural numbers, ordered by the prefix relation. A branch is a maximal chain. An infinite set \(A\subseteq T\) is off-branch when it has finite intersection with every branch. An antichain is a set of pairwise incomparable nodes. The chain height of \(A\) is finite if some natural number \(h(A)\) bounds the size of every chain contained in \(A\). The bound \(h(A)\) may depend on \(A\); no uniform bound over the family is assumed. The invariants \(\mathfrak{o}\) and \(\bar{\mathfrak{o}}\) are the least sizes of maximal almost-disjoint families of infinite off-branch sets and infinite antichains, respectively.

## Proof

Let \(\mathcal O\) be a maximal off-branch family whose members all have finite chain height. For each \(A\in\mathcal O\) and each \(x\in A\), define \(r_A(x)\) to be the maximum length of a chain in \(A\) ending at \(x\). This maximum exists and is finite because \(A\) has finite chain height. If \(x\) is a proper prefix of \(y\), then \(r_A(x)<r_A(y)\). Therefore each rank level \(L_{A,j}=\{x\in A:r_A(x)=j\}\) is an antichain, and the finitely many levels \(L_{A,1},\ldots,L_{A,h(A)}\) partition \(A\).

Let \(\mathcal B\) consist of all infinite levels \(L_{A,j}\) as \(A\) ranges over \(\mathcal O\). Two levels from the same \(A\) are disjoint. Levels coming from distinct \(A,A'\in\mathcal O\) have finite intersection because they are subsets of \(A\cap A'\). Thus \(\mathcal B\) is an almost-disjoint family of infinite antichains.

To prove maximality, let \(C\) be any infinite antichain. Every branch meets \(C\) in at most one node, so \(C\) is off-branch. Maximality of \(\mathcal O\) gives some \(A\in\mathcal O\) with \(|C\cap A|=\infty\). Since \(A\) is the union of finitely many rank levels, at least one level has infinite intersection with \(C\); that level belongs to \(\mathcal B\). Hence no infinite antichain can be added to \(\mathcal B\) while preserving almost-disjointness, so \(\mathcal B\) is maximal among antichain families.

Each member of \(\mathcal O\) contributes only finitely many levels. Maximal off-branch families in this setting are infinite; Leathrum proves \(\mathfrak a\le\mathfrak o\), and the usual almost-disjointness number is uncountable. Therefore \(|\mathcal B|\le|\mathcal O|\cdot\aleph_0=|\mathcal O|\). It follows that \(\bar{\mathfrak{o}}\le|\mathcal O|\) for every maximal off-branch family all of whose members have finite chain height.

Now suppose \(\mathfrak{o}<\bar{\mathfrak{o}}\), and let \(\mathcal O\) be any maximal off-branch family of size \(\mathfrak{o}\). If every member had finite chain height, the preceding argument would give \(\bar{\mathfrak{o}}\le|\mathcal O|=\mathfrak{o}\), a contradiction. Thus at least one member of every such family has unbounded finite chain height: it contains chains of arbitrarily large finite length, while still meeting every branch only finitely.

## Verification

The proof uses only the finite-height rank partition, almost-disjointness inherited by subsets, maximality of the original family, and cardinal arithmetic for infinite families. The rank maximum is well-defined because each member has a finite height bound. The finite partition is essential: it ensures that an infinite intersection with a member of the original family persists in at least one antichain level. No computational enumeration or finite experiment is used as a proof.

## Relationship to prior work

Leathrum defines the invariants \(\mathfrak{o}\) and \(\bar{\mathfrak{o}}\), observes that every infinite off-branch set contains an infinite antichain, and records \(\mathfrak{o}\le\bar{\mathfrak{o}}\). The inspected preprint also poses the consistency question \(\operatorname{Con}(\mathfrak{o}<\bar{\mathfrak{o}})\). The finite-height reduction above is not stated in the inspected sections. It is a conditional structural restriction, not a solution of that consistency question: any strict separation must use a minimal maximal family with at least one member of unbounded finite chain height.

## Limitations

The result neither proves nor refutes \(\operatorname{Con}(\mathfrak{o}<\bar{\mathfrak{o}})\), constructs a forcing model, nor determines either invariant. The literature search was scoped rather than exhaustive; an unindexed source may contain the reduction as folklore.

## References

Thomas E. Leathrum, “A Special Class of Almost Disjoint Families,” arXiv:math/9403201v1, first posted 10 March 1994, especially Sections 3–4 and 8.
