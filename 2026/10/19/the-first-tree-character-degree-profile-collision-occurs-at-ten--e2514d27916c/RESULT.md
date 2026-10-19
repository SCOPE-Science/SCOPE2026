# The first tree character-degree profile collision occurs at ten vertices

## Finding
Let \(T\) be a finite tree on \(n\) vertices. Let \(G_T(q)\) be its graphical group over an odd prime-power field, in the sense of Rossmann. Define the complete ordinary irreducible-character degree profile as the functions \(q\mapsto \#\{\chi\in\operatorname{Irr}(G_T(q)): \chi(1)=q^r\}\), for every nonnegative integer \(r\) and odd prime power \(q\).

**Theorem.** Among trees with at most nine vertices, equal complete character-degree profiles imply isomorphic trees. At ten vertices, there are exactly 106 isomorphism classes of trees but only 105 distinct complete character-degree profiles; exactly one pair collides. The two trees in that pair are given explicitly below. Thus the smallest tree order at which these profiles cease to reconstruct the defining tree is ten.

Use vertex set \(\{0,1,\ldots,9\}\), with the two edge sets, respectively, coded as

```text
A: [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(3,7),(6,8),(8,9)]
B: [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(4,7),(6,8),(7,9)]
```

The trees are nonisomorphic: their diameters are six and seven, respectively. Their common support-matching polynomial is
\[
M_T(s,z)=\sum_{S\subseteq E(T)}s^{|S|}z^{\nu(V(T),S)},
\]
where \(\nu\) is maximum matching cardinality. The entire list of nonzero coefficients \([s^kz^r]M_T(s,z)\) is:

| Edge count \(k\) | Matching number \(r\) | Coefficient |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 1 | 9 |
| 2 | 1 | 10 |
| 2 | 2 | 26 |
| 3 | 1 | 2 |
| 3 | 2 | 54 |
| 3 | 3 | 28 |
| 4 | 2 | 35 |
| 4 | 3 | 82 |
| 4 | 4 | 9 |
| 5 | 2 | 7 |
| 5 | 3 | 86 |
| 5 | 4 | 33 |
| 6 | 3 | 38 |
| 6 | 4 | 46 |
| 7 | 3 | 6 |
| 7 | 4 | 30 |
| 8 | 4 | 9 |
| 9 | 4 | 1 |

Consequently for each odd prime power \(q\) and every \(r\), both groups have exactly
\[
q^{10-2r}[z^r]M_T(q-1,z)
\]
ordinary irreducible characters of degree \(q^r\). (The coefficient is zero for \(r>4\).) This does not assert that the two groups are nonisomorphic, or that they have equal character tables.

## Assumptions and scope
Trees are finite, simple, undirected, and unlabelled up to graph isomorphism. The graph-to-group construction is that of Rossmann (2021); character degrees are ordinary complex character degrees. Finite fields have odd cardinality \(q\). Polynomial coefficients are exact nonnegative integers and the equality is symbolic in \(q-1\), not merely a few numerical specialisations.

## Proof
**1. Reduction to the matching-support polynomial.** For any weighting of a tree's edges by \(\mathbb F_q\), let \(S\) be the support of its nonzero weights. The associated skew-symmetric adjacency matrix has rank exactly \(2\nu(V(T),S)\). Indeed every induced subforest has at most one perfect matching; choosing vertices of a maximum matching gives a nonzero principal Pfaffian, while the Pfaffian expansion of any larger even principal minor vanishes because its graph has no perfect matching. Every support \(S\) has exactly \((q-1)^{|S|}\) weightings. The standard class-two graphical-group character parametrisation therefore gives \(q^{n-2r}\) characters of degree \(q^r\) for each rank-\(2r\) weight assignment. This reduction and its general tree enumerator are **prior results** (Rossmann's character-rank relation; the pre-existing tree graphical-group support-matching formula). No novelty is claimed for this step.

**2. Exact exhaustive construction of unlabelled trees.** Beginning with the single-vertex tree, form the next collection by appending one leaf at every vertex of every representative. Remove isomorphic duplicates using the canonical unrooted tree code: recursively encode rooted branch codes, center the tree by successive leaf stripping, and lexicographically sort the one or two center branch encodings. The code is a complete isomorphism invariant because two trees are isomorphic exactly when these recursively sorted central rooted trees agree. Every \(n\)-vertex tree has a leaf, so deleting it proves induction that no isomorphism class can be omitted. A single code is retained per class. Counts at orders \(2,\ldots,10\) were exactly \(1,1,2,3,6,11,23,47,106\).

**3. Exact profiles.** For each tree on up to ten vertices, loop through all \(2^{n-1}\) edge subsets. For every subset compute the matching number by the exhaustive recurrence \(\nu(E)=\max\{\nu(E\setminus\{e\}),1+\nu(E\setminus\operatorname{Inc}(e))\}\), where \(\operatorname{Inc}(e)\) consists of all edges incident to either endpoint of \(e\), implemented in `checker.py` as a vertex-occupation dynamic program. Tabulate the integer coefficients by edge-subset size and maximum matching size. The 106 trees at order ten yield exactly 105 distinct coefficient arrays, with exactly one duplicated array, printed above. Every tree with at most nine vertices has a distinct array. The pair's diameters differ, confirming nonisomorphism. The coefficient arrays are identical symbolically, proving character profiles equal over all odd prime-power fields by Step 1. A separate two-state rooted matching-polynomial recursion independently recomputes both witness arrays.

## Verification
Run `python3 checker.py` (Python standard library only). The program independently generates all unlabelled trees of orders \(1\) to \(10\), checks their expected class counts, compares exact integer support-matching polynomials, identifies the unique order-ten pair and rechecks both witnesses with a separate rooted recurrence. The expected terminal line is `ALL_EXACT_CHECKS_PASSED`. The program is included in full, and no stored table or external database is required for the result. The known unlabelled tree counts are asserted as cross-checks; completeness instead follows from leaf extension and canonical coding as proved in Step 2.

## Relationship to prior work
Rossmann (arXiv:2107.05564; first posted 2021-07-12), Section 1.6, explicitly relates graphical-group character degrees to skew-adjacency rank specialisations and asks about their distributions. The pre-existing tree graphical-group finding at published-finding corpus identifier `2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65` establishes the general support-matching polynomial and rooted recurrence. The present result **only** claims the new, sharp isomorphism-reconstruction cutoff and the unique explicit collision at size ten, not the earlier general formula. The prior generalized-cospectral tree census at published-finding corpus `2026/9/8/SCOPE045` addresses ordinary adjacency/complement spectra and reports a different cutoff of twelve, which neither proves nor contradicts the present character-degree collision. Searches for character-degree twins, matching-support polynomial twins, and first tree collisions did not locate the asserted order-ten result.

## Limitations
The enumeration establishes minimality **within trees**. It does not establish that the graphical groups themselves are nonisomorphic, that other representation-theoretic invariants coincide, or that all trees of orders greater than ten have twins. Originality beyond the inspected literature has not been independently established. Mathematical testing is exact and exhaustive only through order ten, and the inference for every odd prime power uses the proved rank-to-character formula, not finite experiments.

## References
1. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, first public version 2021-07-12, Section 1.6, Question 1.10; DOI 10.1112/blms.12665.
2. *Tree graphical groups have matching-support character polynomials*, published-finding corpus, identifier `2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65` (pre-existing theorem, used here).
3. *First generalized-cospectral pair of trees at n=12 with closure through n<=11*, published-finding corpus, identifier `2026/9/8/SCOPE045` (different invariant).
