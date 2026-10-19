# Sharp initial total-bondage thresholds in four-column grid graphs

## Finding
Let \(G_n=P_n\square P_4\), with the usual Cartesian-product adjacency. For a graph \(H\) without isolated vertices, write \(\gamma_t(H)\) for the minimum cardinality of a set \(D\subseteq V(H)\) satisfying \(N_H(v)\cap D\neq\varnothing\) for **every** vertex \(v\), including those belonging to \(D\). Define the *total-bondage number*
\[
 b_t(H)=\min\bigl\{|F|:F\subseteq E(H),\;\delta(H-F)\geq1,\;\gamma_t(H-F)>\gamma_t(H)\bigr\}.
\]
Then the three smallest cases left without an exact value by the four-column bounds of Hu, Lu and Xu [1] satisfy
\[
 \boxed{b_t(G_5)=3,\qquad b_t(G_7)=3,\qquad b_t(G_8)=4.}
\]
In particular, the established four-edge upper bound is sharp for \(G_8\), while \(G_5\) improves that bound from four to three. The exact numbers of admissible damaging three-edge sets are respectively \(40\), \(727\) and \(0\). Here a damaging set is one satisfying both conditions inside the definition of \(b_t\).

The full exhaustive small-cut census is:

| \(n\) | \(|E(G_n)|\) | \(\gamma_t(G_n)\) | minimum total dominating sets | \(k\) | admissible \(k\)-edge sets | damaging \(k\)-edge sets |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 31 | 8 | 256 | 1 | 31 | 0 |
| 5 | 31 | 8 | 256 | 2 | 461 | 0 |
| 5 | 31 | 8 | 256 | 3 | 4,369 | 40 |
| 7 | 45 | 10 | 121 | 1 | 45 | 0 |
| 7 | 45 | 10 | 121 | 2 | 986 | 0 |
| 7 | 45 | 10 | 121 | 3 | 14,004 | 727 |
| 8 | 52 | 12 | 2,916 | 1 | 52 | 0 |
| 8 | 52 | 12 | 2,916 | 2 | 1,322 | 0 |
| 8 | 52 | 12 | 2,916 | 3 | 21,884 | 0 |

## Assumptions and scope
The graphs are finite simple **nonperiodic** rectangular grid graphs, with row coordinates \(1\leq i\leq n\) and column coordinates \(1\leq j\leq4\). Distinct vertices \((i,j)\) and \((i',j')\) are adjacent exactly when \(|i-i'|+|j-j'|=1\). The result applies only to \(n\in\{5,7,8\}\). Edge removals creating any isolated vertex are excluded from the total-bondage minimization; counting those as successful failures would yield different, incorrect numbers. Vertex membership in a total dominating set does **not** allow self-domination.

The values \(\gamma_t(G_5)=8\), \(\gamma_t(G_7)=10\), and \(\gamma_t(G_8)=12\) follow from the known four-column formula in [1]. They are also computed independently in both included checkers and are not claimed as new. The newly determined objects are the exact total-bondage values and the indicated small-edge-cut counts.

## Proof
For the upper bounds, write \((i,j)(i',j')\) for the edge between those grid vertices. Take
\[
\begin{aligned}
F_5={}&\{(1,1)(2,1),\ (1,2)(1,3),\ (3,1)(4,1)\},\\
F_7={}&\{(6,1)(7,1),\ (6,2)(7,2),\ (7,2)(7,3)\},\\
F_8={}&\{(5,1)(6,1),\ (7,1)(8,1),\ (7,2)(8,2),\ (8,2)(8,3)\}.
\end{aligned}
\]
Every resulting graph has minimum degree at least one. An exact finite calculation gives
\[
\gamma_t(G_5-F_5)=9,\qquad
\gamma_t(G_7-F_7)=11,\qquad
\gamma_t(G_8-F_8)=13.
\]
This yields the proposed upper bounds. The three-edge construction for \(G_7\) and the four-edge construction for \(G_8\) are instances of the earlier published upper-bound constructions [1], not asserted as new; the three-edge construction for \(G_5\) improves the published upper bound.

For completeness, the following finite recurrence establishes all needed lower bounds without appealing to numerical heuristics. Fix an edge set \(F\). For each row \(i\), let \(A_i\subseteq\{1,2,3,4\}\) be the columns whose vertices are selected for a candidate total dominating set. Set \(A_0=A_{n+1}=\varnothing\). A vertex in row \(i\) can have a selected neighbor only in rows \(i-1\), \(i\), or \(i+1\). Let \(C_i^F(A_i)\) be the columns in row \(i\) covered from selected vertices in that row by surviving horizontal edges, and let \(U_{j\to i}^F(A_j)\) be the columns in row \(i\) covered from selected vertices of adjacent row \(j\) via surviving vertical edges. Thus **all** vertices in row \(i\) are totally dominated precisely when
\[
 C_i^F(A_i)\cup U_{i-1\to i}^F(A_{i-1})
 \cup U_{i+1\to i}^F(A_{i+1})=\{1,2,3,4\}.
\]
Minimize \(\sum_{i=1}^n|A_i|\) over all row-mask sequences satisfying these local equalities. A dynamic program keeps the two latest row masks, tries all sixteen possibilities for the next mask, verifies the now-complete middle-row equality, and adds the number of vertices in the new mask. Its initial previous mask and final following mask are empty. The recurrence is exact: every total dominating set determines one sequence accepted by the recurrence, and every accepted sequence determines a total dominating set. Consequently its terminal optimum is exactly \(\gamma_t(G_n-F)\).

The standalone C++ checker constructs each grid edge, exhausts every edge subset of sizes one, two and three, rejects subsets that isolate any vertex, and applies this recurrence to each remaining deletion. Its output gives the table above. Hence no admissible cut of at most two edges is damaging in \(G_5\) or \(G_7\), and none of at most three edges is damaging in \(G_8\). Together with the explicit witnesses, this proves the three exact values.

There is a separate finite check of the entire lower-bound computation. The included Python program generates all minimum total dominating sets of each **original** grid using a backward optimality recurrence (numbers \(256,121,2916\)). For every admissible set \(F\) of at most three edges, it checks whether some such original optimum remains a total dominating set of \(G_n-F\). Since deleting edges never reduces \(\gamma_t\), equality \(\gamma_t(G_n-F)=\gamma_t(G_n)\) holds **if and only if** one original minimum set survives. This alternative test reproduces every admissible and damaging count shown in the table. It does not depend on the edge-deleted-graph minimization used by the C++ checker.

## Verification
The files `check_total_bondage.cpp` and `check_optimal_sets.py` contain executable, standard-library-only enumerators with explicit assertions. Compile the former with `g++ -std=c++17 -O3 check_total_bondage.cpp -o check_total_bondage` and run `./check_total_bondage`; run the latter with `python3 check_optimal_sets.py`. Their observed outputs are included as `check_output.txt` and `check_optimal_sets_output.txt`. Both were executed from the indicated source files and agree on every small-cut count. The upper-bound witnesses are also checked directly for admissibility and the exact increase in \(\gamma_t\).

## Relationship to prior work
Hu, Lu and Xu [1, Section 5, particularly Lemmas 5.3–5.4 and Theorem 5.1] prove \(b_t(G_7)\leq3\), \(b_t(G_5)\leq4\), and \(b_t(G_8)\leq4\), but do not give lower bounds completing these three cases. Their general results for lengths congruent to one or four modulo five do not imply these exact values. The new lower bounds show sharpness at the first length of two unresolved residue classes and improve the bound at the first length of the third. Gamlath and Wei [2] provide general bounds for broader graph families, not exact evaluations for these three grids. The survey [3] fixes the crucial convention excluding isolate-producing deletions. Neither the known four-column total-domination formula nor the older upper-bound witnesses alone imply the present lower bounds or the three-edge-cut counts.

## Limitations
No formula for arbitrary \(n\) is proved, and no prediction is made about the first larger representative in any residue class. The damaging-cut counts are exact **only** for cuts of size three; the claim does not classify all damaging four-edge sets of \(G_8\). Computation is exhaustive over explicitly finite input ranges and supported by two differently organized checkers; it is not a formally verified proof-assistant development or an independent external audit. An unindexed prior exact computation of the same cases remains a novelty risk.

## References
[1] F.-T. Hu, Y. Lu and J.-M. Xu, *The total bondage number of grid graphs*, arXiv:1109.3929v1, first publicly submitted 2011-09-19; Discrete Applied Mathematics 160 (2012), 2408–2418. https://arxiv.org/abs/1109.3929 ; https://doi.org/10.1016/j.dam.2012.06.012

[2] E. G. K. M. Gamlath and B. Wei, *On total bondage number of graphs*, arXiv:2401.16615v1 (2024). https://arxiv.org/abs/2401.16615

[3] J.-M. Xu, *On bondage numbers of graphs: A survey with some comments*, International Journal of Combinatorics (2013), article 595210. https://doi.org/10.1155/2013/595210
