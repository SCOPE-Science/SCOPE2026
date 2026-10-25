# Sharp online and static shattering laws for bounded-component partial orders

## Finding

For integers \(n,b\ge1\), let \(\mathcal P_{n,b}\) be the Boolean concept class on ordered pairs \(X_n=\{(i,j):i,j\in[n],\ i\ne j\}\). A concept is the indicator of the strict relation \(i<_{P}j\) of a labeled partial order \(P\) whose *comparability graph* (join distinct vertices if either is below the other) has connected components of size at most \(b\). No comparabilities occur between different components.

**Structural shattering criterion.** A query set \(Q\subseteq X_n\) is VC-shattered by \(\mathcal P_{n,b}\) if and only if its directed graph is acyclic, has no edge supported by a different directed path with the same endpoints, and has weakly connected components of size at most \(b\). Equivalently, \(Q\) is the arc set of a transitively reduced directed acyclic graph with component order at most \(b\).

Write \(n=qb+r\) with \(0\le r<b\), and put \(f(t)=\lfloor t^2/4\rfloor\). **For every** \(n,b\ge1\),
\[
\operatorname{VCdim}(\mathcal P_{n,b})=q f(b)+f(r).
\]
**For every** \(n\ge1\) and \(1\le b\le4\),
\[
\operatorname{Ldim}(\mathcal P_{n,b})=q\binom b2+\binom r2.
\]
In particular, the dimensions agree for \(b\le2\). For \(b=3\) their difference is exactly \(\lfloor n/3\rfloor\), and for \(b=4\) their difference is \(2\lfloor n/4\rfloor+\mathbf1_{n\bmod4=3}\). Thus component size three is the smallest allowed comparability-component bound giving any adaptive advantage; that advantage grows without bound although **every possible target component has at most three vertices**.

The smallest cases have \((\operatorname{VCdim},\operatorname{Ldim})=(2,3)\) for unrestricted strict orders on three labeled vertices, and \((4,6)\) on four labeled vertices. There are respectively \(19\) and \(219\) such partial orders.

## Assumptions and scope

All ground sets are finite, and partial orders are strict (irreflexive and transitive). Queries are *ordered* distinct pairs, evaluated as true only for strict comparability in that direction; incomparability and reverse comparability both produce false. The family contains the empty relation. Component size is measured in the undirected comparability graph, not in the Hasse diagram of a fixed reference order. The formula for the Littlestone dimension is asserted only for \(b\le4\); no exact formula for larger component bounds is claimed.

## Proof

**Lemma 1 (exact shattered query sets).** Write \(D=(V,Q)\) for the query digraph. If \(Q\) is shattered, the all-true labeling is realized by some strict order. Therefore \(D\) is acyclic and all weak components of \(D\) have order at most \(b\). If an arc \(u\to v\) has an alternative directed \(u\)-to-\(v\) path in \(D\), label the path arcs true and that arc false: transitivity makes this impossible. Conversely, if these three conditions hold, take any labeling and form the transitive closure of its true arcs. This is an irreflexive transitive relation, remains within the weak components of \(D\), and cannot make a false query arc true (that would give an alternative directed path in \(D\)). It realizes the labeling in \(\mathcal P_{n,b}\). This proves the criterion with both directions and all quantifiers.

**Lemma 2 (VC extremality).** A transitively reduced acyclic digraph contains no undirected triangle: every acyclic orientation of a triangle includes a redundant transitive arc. Thus the underlying undirected graph of each weak query component of size \(t\) is triangle-free, with at most \(f(t)\) edges by Mantel's bound. If the component sizes are \(t_1,\ldots,t_k\le b\), with sum \(n\), then \(|Q|\le\sum_i f(t_i)\le qf(b)+f(r)\). The latter extremum follows because the increments \(f(t+1)-f(t)\) are nondecreasing: transferring a vertex from a smaller nonempty block to a larger block not yet at size \(b\) cannot decrease the sum, eventually leaving \(q\) full blocks and a remainder block. For the reverse inequality, partition \([n]\) into such blocks. Within each block orient the balanced complete bipartite graph wholly from its left side to its right side. Every subset of these arcs is itself transitively closed, with no arcs between blocks, hence is a legal strict order. The entire query set is shattered. Therefore the VC formula is exact.

**Lemma 3 (online upper bound).** Against any target, predict false on each previously unseen ordered pair and remember all affirmative observations. Predict true only on a previously observed affirmative pair. This deterministic realizable online learner makes at most the number of true ordered pairs of the target as mistakes. A partial-order component of order \(t\) has at most \(\binom t2\) true ordered pairs, attained by a chain. Convexity of \(\binom t2\) and the component bound give at most \(q\binom b2+\binom r2\). The online mistake characterization of Littlestone dimension gives the same upper bound for \(\operatorname{Ldim}(\mathcal P_{n,b})\), for every \(b\).

**Lemma 4 (sharpness through four).** On one, two, three, and four labeled vertices the full strict-order classes admit complete online-shattered binary trees of respective depths \(0,1,3,6\). The nontrivial depth-three and depth-six trees are given by `poset_depth3_certificate.json` and `poset_depth6_certificate.json`; their respective \(8\) and \(64\) leaves are distinct explicit posets and all \(7\) and \(63\) internal questions have both correctly realized branches. `verify.py` checks every certificate path using an independently enumerated list of all valid strict partial orders. In both cases the trivial number-of-true-relations upper bound from Lemma 3 matches these depths, so these are *exact* dimensions, not partial numerical evidence. The two-point case is one nonconstant ordered-pair query, and the one-point case has no query.

Now let \(b\le4\) and partition the ground set into \(q\) fixed blocks of size \(b\) and one block of size \(r\). Restrict to orders with no interblock comparabilities and arbitrary strict partial orders on individual blocks. Their concept class is a Cartesian product on disjoint query domains. Concatenating the independently shattered trees from Lemma 4 gives depth \(q\binom b2+\binom r2\) in the full bounded-component class. Lemma 3 gives the reverse inequality. Subtracting the VC formula yields the stated sharp threshold and gaps.

## Verification

Run `python3 verify.py` from the directory containing the certificates. It exhausts all irreflexive directed relations on up to four labeled vertices (at four points, \(2^{12}=4096\) possibilities), independently filters antisymmetry and transitivity, computes exact VC and Littlestone dimensions by the standard finite subset recurrences, checks every question and leaf of the two explicit shattered trees, and checks the four-point bounded-component VC values. The expected exact full-poset profile for orders \(1,2,3,4\) is \((\text{number of orders},\operatorname{VCdim},\operatorname{Ldim})=(1,0,0),(3,1,1),(19,2,3),(219,4,6)\). The extracted checker reports `ALL_POSET_CHECKS_PASS`.

The infinite assertions are proved by Lemmas 1–4; finite enumeration alone is not used to extrapolate to larger \(n\). The optional `build_certificate.py` regenerates the two trees from a different, ternary per-unordered-pair order enumeration and the exact Littlestone recurrence.

## Relationship to prior work

The August 12, 2021 first version of Malliaris and Moran's *Agnostic Online Learning and Excellent Sets* develops general links between Littlestone rank, stability, and online learning, rather than the bounded-comparability-component relation classes or these exact formulas. Chase, Freitag, and Reyzin's October 7, 2023 *Applications of Littlestone dimension to query learning and to compression* establishes general learning/compression bounds, not these poset-specific dimensions. Duan, Ouyang, and Wang's December 9, 2024 preprint *VC-dimensions between partially ordered sets and totally ordered sets* concerns **compatibility between entire orders**, with concepts and query objects distinct from the present ordered-pair relation-membership class. Its equal-looking \(\lfloor n^2/4\rfloor\) expression is therefore not the same theorem. The present result derives a transitively reduced digraph criterion and pairs exact static dimensions with sharp online dimensions for small component bounds.

## Limitations

The formula for \(\operatorname{Ldim}\) is not extended beyond \(b=4\); the general counting upper bound may cease to be attainable for large components. The first-version source dates refer to background literature, not a historical novelty certification. A priority check over accessible publications and research records found no statement implying the full joint result, but unindexed or inaccessible results may exist. Only self-review is reported; no independent audit has been carried out.

## References

- M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, first posted 2021-08-12, https://arxiv.org/abs/2108.05569 .
- H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812, first posted 2023-10-07, https://arxiv.org/abs/2310.04812 .
- B. Duan, M. Ouyang and Z. Wang, *VC-dimensions between partially ordered sets and totally ordered sets*, arXiv:2412.06402, first posted 2024-12-09, https://arxiv.org/abs/2412.06402 . Its ground set and concept objects are different.
- Mantel's triangle-free graph theorem (1907), used in Lemma 2.
