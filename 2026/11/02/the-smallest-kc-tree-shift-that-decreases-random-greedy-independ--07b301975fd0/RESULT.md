# The smallest KC-tree shift that decreases random-greedy independence

## Finding

**Theorem (a minimum-order obstruction).** Let \(X(G)\) denote the cardinality of the maximal independent set produced by inspecting the vertices of a finite simple graph \(G\) in a uniformly random order and retaining each vertex if none of its already-retained neighbors is present. There are two trees \(T,T'\) on nine vertices such that \(T'\) is obtained from \(T\) by a **proper** Kelmans–Csikvári (KC) transformation, yet

\[
\mathbb E X(T)=\frac{73}{15},\qquad
\mathbb E X(T')=\frac{34}{7},\qquad
\mathbb E X(T')-\mathbb E X(T)=-\frac1{105}<0.
\]

No tree of order at most eight admits a proper KC transformation with a strictly negative change in this expected cardinality. Thus nine vertices is the minimum possible order of a failure of monotonicity. For the greedy independence **ratio**, the corresponding difference is \(-1/945\).

This refutes the suggested monotonicity of the expected random-greedy independence ratio along proper KC transformations, while not contradicting the established minimum-on-path theorem.

## Assumptions and scope

The model uses one **uniform random permutation** of all vertices, not an adaptive random choice, uniform sampling of surviving vertices, or a maximum-independent-set algorithm. A KC transformation is defined for distinct vertices \(x,y\) whose connecting path has only degree-two internal vertices. If \(z\) is the neighbor of \(y\) on that path, every edge \(yw\) with \(w\in N(y)\setminus\{z\}\) is replaced by \(xw\). A transformation is *proper* when it increases the number of leaves by one.

Take vertex set \(\{1,2,\ldots,9\}\), and let

\[
\begin{aligned}
E(T)={}&\{(1,2),(2,3),(2,4),(4,5),(5,6),(6,7),(7,8),(7,9)\},\\
E(T')={}&\{(1,2),(2,3),(2,4),(4,5),(4,7),(5,6),(7,8),(7,9)\}.
\end{aligned}
\]

The path \(4-5-6\) in \(T\) is bare, and \(T'\) results from its KC transformation with \(x=4\), \(y=6\), which replaces edge \((6,7)\) by \((4,7)\). In \(T\) there are four leaves; in \(T'\) there are five. Both are trees.

## Proof

**Exact random-greedy law.** For an induced subgraph on the remaining vertex set \(S\), let \(F_G(S;z)\) be the probability-generating polynomial for the eventual accepted count, with \(F_G(\varnothing;z)=1\). If \(N_G[v]\) denotes the closed neighborhood of \(v\) in the original graph, conditioning on the first vertex of a uniform ordering gives the exact finite recurrence

\[
F_G(S;z)=\frac{z}{|S|}\sum_{v\in S}
 F_G(S\setminus N_G[v];z),\qquad S\ne\varnothing.
\]

This holds because the first vertex is retained, its neighbors can never be retained, and the relative order on the surviving induced subgraph remains uniform. Every recursive call has a smaller vertex set, so the identity determines the polynomial uniquely, using rational arithmetic only.

Applying it to the displayed edge lists gives

\[
\begin{aligned}
F_T(V;z)&=\frac{29z^3+156z^4+60z^5+160z^6}{405},\\
F_{T'}(V;z)&=\frac{110z^3+399z^4+168z^5+457z^6}{1134}.
\end{aligned}
\]

For a second, directly checkable finite certificate, exhaustive enumeration of all \(9!=362880\) possible vertex orders yields:

| Accepted count | Orders for \(T\) | Orders for \(T'\) |
|---:|---:|---:|
| \(3\) | 25,984 | 35,200 |
| \(4\) | 139,776 | 127,680 |
| \(5\) | 53,760 | 53,760 |
| \(6\) | 143,360 | 146,240 |

Each column totals \(362880\), and division by this total reproduces the generating polynomials. Differentiating at \(z=1\), or summing accepted counts over the table, gives \(73/15\) and \(34/7\), hence the strict negative difference \(-1/105\). The two counting methods are implemented independently in the attached verifier.

**Minimum order.** Every tree of order \(n+1\) can be obtained by adjoining a pendant vertex to a tree of order \(n\), since every nontrivial tree has a leaf. Starting at the one-vertex tree, the attached verifier generates all such extensions and identifies isomorphic trees by a canonical tree-center parenthesis code (the unordered rooted-tree code at either center). For each resulting unlabelled tree it checks every ordered pair \((x,y)\), tests the bare-path and properness conditions, and evaluates the same exact recurrence before and after the move. Consequently the enumeration covers **all** proper KC transformations through nine vertices, not a sampled subset. The finite census is:

| Order | Unlabelled trees | Oriented proper KC moves | Strict decreases |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 3 | 1 | 0 | 0 |
| 4 | 2 | 2 | 0 |
| 5 | 3 | 8 | 0 |
| 6 | 6 | 26 | 0 |
| 7 | 11 | 70 | 0 |
| 8 | 23 | 186 | 0 |
| 9 | 47 | 470 | 4 |

The move count includes orientations of endpoint pairs and does not purport to count distinct isomorphism classes of moves. Rational comparisons give no negative difference before order nine and at least one at order nine. Together with the explicit witness, this proves the minimum-order assertion.

## Verification

Run \(\texttt{python3 verify.py}\) in the directory containing the standalone Python 3 file, using only the standard library. It performs three checks: a direct \(9!\)-permutation census, an independent exact rational first-vertex recursion, and the exhaustive leaf-extension/isomorphism-reduced minimality census. The three checks passed, with the exact fractions and counts displayed above. No asymptotic extrapolation, simulation, numerical tolerance, or unexamined solver certificate is used.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli and Shikhelman established the expected path-minimization theorem and proved monotonicity of an auxiliary functional \(\nu\) under KC transformations. In their 2019 preprint, later 2020 conference version and 2023 revised full text, they separately suggest that the **actual expected greedy independence ratio** should be nondecreasing under KC transformations (strictly increasing under proper ones). The present explicit proper KC move falsifies that suggested strengthening. It does **not** falsify their proved auxiliary-functional inequality or their path-minimization theorem. The paper's general first-vertex approach permits evaluating individual trees, but does not state or imply this counterexample without the finite comparison.

The source was first publicly posted on 2019-07-16 as arXiv:1907.07216. The 2023 full text was checked in Sections 8.1 and 9, and the arXiv full text was checked in Sections 6.1 and 7. A targeted literature and database comparison found no previous statement of this nine-vertex obstruction; that search result is not a proof of priority.

## Limitations

The result refutes **KC monotonicity**, not the theorem that paths minimize expected greedy independent-set size among trees. It makes no claim about monotonicity for restricted tree subclasses, other greedy algorithms, or the size of larger counterexamples. The minimum-order statement is a finite, fully specified exhaustive computation; its independent replication would strengthen confidence. Historical priority, outside the inspected material and searchable records, remains unverified, and no independent mathematical audit is claimed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216, first posted 2019-07-16. https://arxiv.org/abs/1907.07216
2. The same authors, *Greedy maximal independent sets via local limits*, *Random Structures & Algorithms* 64 (2024), 986–1015, online 2023-12-18, Sections 8.1 and 9. https://doi.org/10.1002/rsa.21200
3. The same authors, *Greedy Maximal Independent Sets via Local Limits*, *AofA 2020*, LIPIcs 159 (2020), article 20. https://doi.org/10.4230/LIPIcs.AofA.2020.20
