# Sharp source-order thresholds for tree-homomorphism fingerprints through thirteen vertices

## Finding

For each positive integer \(k\), let \(\mathcal T_{\le k}\) be one representative of every isomorphism class of nonempty **unlabelled, finite, simple, connected trees** on at most \(k\) vertices. For a finite tree target \(G\) write
\[
\Phi_k(G)=\bigl(\operatorname{hom}(F,G):F\in\mathcal T_{\le k}\bigr),
\]
where \(\operatorname{hom}(F,G)\) counts all adjacency-preserving vertex maps, without requiring injectivity. For each \(n\), let \(\lambda(n)\) be the least \(k\) such that \(\Phi_k\) distinguishes every pair of nonisomorphic \(n\)-vertex trees. For every \(4\le n\le13\), the exact \(\lambda(n)\) and number of classes just below that threshold are:

| Target order \(n\) | All trees | \(\lambda(n)\) | Profiles at \(k=\lambda(n)-1\) |
| ---: | ---: | ---: | ---: |
| 4 | 2 | 3 | 1 |
| 5 | 3 | 3 | 1 |
| 6 | 6 | 4 | 5 |
| 7 | 11 | 4 | 7 |
| 8 | 23 | 5 | 21 |
| 9 | 47 | 5 | 38 |
| 10 | 106 | 6 | 103 |
| 11 | 235 | 6 | 218 |
| 12 | 551 | 7 | 547 |
| **13** | **1301** | **8** | **1300** |

Equivalently, the first collision orders for source budgets \(k=3,4,5,6,7\) are respectively \(6,8,10,12,13\). The last case breaks the preceding doubled-order pattern: among 1301 trees of order thirteen, there is exactly **one** nonisomorphic pair with equal counts from all **25** source-tree types of order at most seven. Exactly **five** of the 23 eight-vertex tree-source types distinguish the pair. Hence \(\Phi_8\) is injective on thirteen-vertex trees, but \(\Phi_7\) is not.

## Assumptions and scope

Graphs are finite, undirected, loopless, and simple. Only **unlabelled tree isomorphism types** serve as sources and targets. Targets are compared at equal order; the one-vertex source also explicitly records target order, so differently ordered targets cannot share the full profile. The table covers exactly orders \(4\) through \(13\); it makes no assertion about \(\lambda(n)\) for \(n>13\). Counts are of all graph homomorphisms, not embeddings. An isolated one-vertex tree is permitted.

## Proof

**Exhaustive class generation.** Begin with the unique one-vertex tree. From each representative of every \((n-1)\)-vertex tree, attach a new leaf at every vertex. Any \(n\)-vertex tree has at least one leaf, so deleting that leaf gives a smaller tree: the procedure covers every isomorphism type by induction. To remove duplicates, repeatedly strip leaves to find one or two centers, recursively encode each center-rooted tree by sorted multisets of child codes, and take the lexicographically smaller center code. The recursive strings classify rooted trees by induction, while the center set is isomorphism invariant; hence the resulting free-tree code is a complete, collision-free canonical form. This construction yields the classical counts \(1,1,1,2,3,6,11,23,47,106,235,551,1301\) for orders one to thirteen.

**Exact count recurrence.** Root a source tree \(F\) at any vertex. For every source vertex \(u\) and target vertex \(x\), let \(D_u(x)\) be the number of homomorphisms from the descendant subtree of \(u\) to \(G\) sending \(u\) to \(x\). Then
\[
D_u(x)=\prod_{v\text{ child of }u}\biggl(\sum_{y\sim_G x}D_v(y)\biggr),\qquad
\operatorname{hom}(F,G)=\sum_{x\in V(G)}D_r(x).
\]
This is an exact integer identity by independent choices of the descendant-branch maps. Empty products equal one. Therefore every profile entry is computed exactly, with no sampling and no floating-point comparison.

**Finite classification.** The included standard-library verifier generates every tree target through order thirteen and each source tree through order eight; it forms exact tuples by the recurrence, groups them by equality, and checks the displayed class counts and minimum source orders. All lower bounds arise from non-singleton equal-profile classes at one smaller source budget; all upper bounds arise from complete injectivity at the stated budget. In particular the counts at order thirteen are \(34,370,1052,1285,1300,1301\) profiles for budgets \(k=3,4,5,6,7,8\) respectively.

**Explicit sharp obstruction.** Two nonisomorphic trees \(A,B\) on vertices \(0,\ldots,12\) that have the same \(\Phi_7\) profile have these unambiguous edge lists:

- \(A\): `[[0,1],[0,2],[1,3],[1,11],[2,4],[2,9],[3,5],[4,6],[4,8],[5,7],[6,12],[9,10]]`.
- \(B\): `[[0,1],[0,2],[0,9],[1,3],[1,10],[2,4],[3,5],[4,6],[4,8],[5,7],[6,12],[10,11]]`.

The verifier confirms that their canonical codes differ, all 25 source counts through order seven agree, and precisely five of the 23 order-eight tree sources separate them. For example, the eight-vertex source with edges `[[0,1],[0,5],[1,2],[1,4],[2,3],[5,6],[6,7]]` has homomorphism counts \(2722\) and \(2723\) for \(A\) and \(B\), respectively.

## Verification

Run `python verify_tree_profiles.py` in Python 3. It needs only the standard library and checks the exhaustive classification, explicit collision, source-size boundary, recurrence against direct enumeration for small examples, and number of separating order-eight probes. Its final line is `ALL_BOUNDED_TREE_SOURCE_PROFILE_CHECKS_PASS`. Separately, `python verify_tree_profiles_alt.py` independently generates tree isomorphism classes via NetworkX and applies a differently written rooted-tree dynamic program; it requires NetworkX and reports `INDEPENDENT_BOUNDED_PROFILE_CROSSCHECK_PASS`. The `verification_output.txt` record contains the actual outputs. The finite result is fully decidable by these enumerations; no extrapolation to larger orders is made.

## Relationship to prior work

Dell, Grohe, and Rattan (2018) characterize all-tree homomorphism equivalence by color refinement and also characterize path-profile equivalence. Grohe (2020) relates source graphs of bounded treedepth to counting quantifier rank. Fluck, Seppelt, and Spitzer (2023) analyze joint treewidth/treedepth restrictions. None of those characterizations provides the exact **number-of-vertices** source-budget thresholds for unlabelled tree targets in the table. Bounded source cardinality is a distinct filtration from tree depth or the all-tree and all-path filtrations. Existing path-profile results about small trees neither imply the 25-query-profile collision at order thirteen nor rule out the five size-eight separating trees. The ordinary unlabelled-tree counts agree with OEIS A000055, but that sequence is not a table of the finer homomorphism-fingerprint classes.

## Limitations

This is a finite complete classification through target order thirteen, not a general asymptotic formula. The distinction among fingerprints depends on counting all homomorphisms (allowing collapsed vertices) from each source type. The alternative verifier uses a separate NetworkX dependency. No comprehensive proof of historical priority or independent external scientific audit is claimed.

## References

1. H. Dell, M. Grohe, G. Rattan, *Lovász Meets Weisfeiler and Leman*, arXiv:1802.08876v1, first public 2018-02-24. https://arxiv.org/abs/1802.08876
2. M. Grohe, *Counting Bounded Tree Depth Homomorphisms*, arXiv:2003.08164v1, first public 2020-03-18. https://arxiv.org/html/2003.08164v1
3. E. Fluck, T. Seppelt, G. L. Spitzer, *Going Deep and Going Wide*, arXiv:2308.06044v1, first public 2023-08-11. https://arxiv.org/html/2308.06044v1
4. OEIS A000055, numbers of unlabelled trees. https://oeis.org/A000055
