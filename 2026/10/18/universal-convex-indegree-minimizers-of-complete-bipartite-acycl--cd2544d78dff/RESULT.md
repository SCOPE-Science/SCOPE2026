# Universal convex-indegree minimizers of complete bipartite acyclic orientations

## Finding
Let \(G=K_{a,b}\) be a simple complete bipartite graph with two **labelled**, nonempty parts, and put \(m=\min\{a,b\}\) and \(t=|a-b|\). For any real-valued discrete strictly convex function \(\varphi\) on the integers from zero to \(\max\{a,b\}\), define
\[
F_\varphi(D)=\sum_{v\in V(G)}\varphi(\operatorname{indeg}_{D}(v)),
\]
where \(D\) ranges over acyclic orientations of \(G\).

**Theorem.** The orientations minimizing \(F_\varphi\) are independent of the choice of strictly convex \(\varphi\). If the smaller part is denoted \(A\) and the larger \(B\), their canonical part-words are exactly the \(2^m\) words obtained by concatenating \(m\) tiles, each independently either `AB` or `BA`, and then appending \(t\) copies of `B`. The optimal indegree multiset is
\[
\{0\}\ \uplus\ \biguplus_{j=1}^{m-1}\{j,j\}\ \uplus\ \{\underbrace{m,\ldots,m}_{t+1}\}.
\]
In particular,
\[
\min_D F_\varphi(D)=\varphi(0)+2\sum_{j=1}^{m-1}\varphi(j)+(t+1)\varphi(m).
\]
The **number of distinct labelled acyclic orientations**, as opposed to part-words, attaining this value is exactly
\[
\boxed{N(a,b)=m!(m+t)!\left(\frac32\right)^{m-1}\left(\frac1{t!}+\frac1{(t+1)!}\right).}
\]
Furthermore, the displayed multiset is majorized by the indegree multiset of every other acyclic orientation. Thus these same orientations minimize every convex separable indegree sum, with uniqueness of the class of minimizers for strictly convex functions.

For the quadratic objective, the optimal value simplifies to
\[
\frac{m(m-1)(2m-1)}3+(t+1)m^2.
\]
For example, \(K_{2,3}\) has exactly \(27\) optimal orientations, and \(K_{3,3}\) has exactly \(162\), compared with \(46\) and \(230\) acyclic orientations in total, respectively.

## Assumptions and scope
Both parts are nonempty and their vertices are distinguished. The graph is simple. An orientation is acyclic if it contains no directed cycle. A discrete strictly convex function satisfies
\[
\Delta\varphi(j+1)>\Delta\varphi(j),\qquad\Delta\varphi(j)=\varphi(j+1)-\varphi(j)
\]
whenever these expressions are defined; the function need not be nonnegative or nondecreasing. The theorem counts orientations, not topological orderings. Swapping two consecutive vertices within the same bipartition part cannot change an orientation.

Every acyclic orientation of a complete bipartite graph admits a topological ordering. Reading only which part supplies each successive vertex gives a **canonical part-word**, independent of which topological ordering is selected: each vertex of one part is adjacent to each vertex of the other, so their relative order is forced by that edge's direction. Conversely, any such part-word, with an assignment of labelled vertices to its slots, induces an acyclic orientation. Permutations within a maximal run of identical letters induce the same orientation, and these are the only duplications.

## Proof
**1. Exchange identity.** Suppose a part-word has a consecutive `AB` at a point where \(i\) vertices of \(A\) and \(j\) of \(B\) have already appeared. The contribution of these two positions to the indegree sum is \(\varphi(j)+\varphi(i+1)\). Switching to `BA` changes it to \(\varphi(i)+\varphi(j+1)\); all later vertices see the same prefix counts, so their contributions are unchanged. Thus
\[
F_\varphi(AB)-F_\varphi(BA)=\Delta\varphi(i)-\Delta\varphi(j).
\]
When \(i>j\), `BA` is strictly better; when \(i<j\), `AB` is strictly better. The switch replaces an indegree pair \((j,i+1)\) by \((j+1,i)\) when \(i>j\), which is a strict balancing transfer, and similarly in the opposite case.

**2. Exhaustive classification of minimizers.** Assume \(|A|=m\le |B|=m+t\). An optimal word can never have an initial segment with two more `A` letters than `B` letters: the next `B` exists, and its immediately preceding `A` forms an improving `AB` switch. Likewise, while any `A` remains, the word cannot have two more `B` letters than `A` letters: the first subsequent `A` is immediately preceded by `B`, forming an improving `BA` switch. A sharper formulation avoids a boundary ambiguity: if an `A` surplus of two first occurs at the last `A`, the first following `B` still yields the improving switch. Therefore, until all \(m\) letters `A` have appeared, each successive pair must contain exactly one `A` and one `B`. These are the \(m\) freely chosen tiles `AB` or `BA`; the remaining \(t\) letters are `B`. Conversely, every such word is feasible and has the same objective: tile number \(j+1\), starting at counts \((j,j)\), contributes exactly \(\varphi(j)+\varphi(j+1)\) in either order. The trailing letters each contribute \(\varphi(m)\). Any nontiled word admits a strict improving exchange, hence no other optimal word exists.

**3. Universal majorization and value.** Every improving exchange described above transfers one indegree unit from a larger indegree to a smaller one without changing any other indegree. Repeating exchanges terminates, since the sum of squared indegrees strictly decreases and there are finitely many part-words. The terminal word must be tiled. Consequently its indegree multiset is majorized by that of the starting word. Every tile contributes the pair \((j,j+1)\), for \(0\le j<m\), regardless of its order, and each trailing `B` contributes \(m\). This gives the displayed multiset, the universal objective value, and the quadratic specialization.

**4. Distinct labelled orientation count.** For a fixed part-word, place the \(m\) labelled `A` vertices and \(m+t\) labelled `B` vertices in their slots. Two resulting orders yield the same orientation exactly when they differ only by a permutation within a maximal same-letter run. Thus the number of orientations for that word is \(m!(m+t)!\) divided by the factorials of its run lengths. In a tiled word, each change between consecutive tile choices creates exactly one same-letter run of length two; other interior runs have length one. If there are \(c\) tile changes, the interior multiplicity divisor is \(2^c\). If the final tile ends in `B`, the trailing \(t\) letters extend its last `B` run to length \(t+1\), contributing \((t+1)!\); otherwise the final `B` run has length \(t\), contributing \(t!\). For either prescribed final tile, the sum of weights \(2^{-c}\) over the preceding \(m-1\) choices is
\[
\sum_{c=0}^{m-1}\binom{m-1}{c}2^{-c}=\left(\frac32\right)^{m-1}.
\]
Multiplying by the label permutations and adding the two final-tile cases proves the exact expression for \(N(a,b)\). This holds when \(t=0\) by the convention \(0!=1\), and when \(m=1\) because the change sum is empty. All boundary cases are included.

## Verification
The accompanying `check_minimizers.py` independently enumerates **literal orientations of the graph's labelled edges**, checks acyclicity by topological elimination, computes their indegrees, and compares both exact optimum and number of optimizers against the theorem. It does not use part-words to generate cases. Four strictly convex test functions include quadratic, cubic, exponential, and a quadratic with a negative linear term. In all, it checks \(52\) graph/function combinations, encompassing \(104334\) raw edge orientations and \(13638\) acyclic orientations. All passed in the supplied run. The finite checks supplement, but cannot replace, the unrestricted exchange proof.

Run from the package directory with `python check_minimizers.py` (standard-library Python 3 only). The program exits nonzero on any discrepancy.

## Relationship to prior work
Borsik and Madarasi studied exactly the general acyclic indegree-convex optimization problem and established complexity and approximation results for arbitrary graphs, including hardness even for strictly convex cost functions. Their inspected manuscript does not state the present universal closed-form biclique minimizer classification or multiplicity formula. This finding supplies an explicit infinite tractable family for that problem, not a competing general algorithm.

West characterized complete-bipartite acyclic orientations using alternating vertex blocks while studying the number of independently reversible edges. The present construction uses this underlying canonical-order idea but optimizes a different statistic and counts the minimizers rather than reversible edges. Cameron, Glass, Rekvényi and Schumacher identified the total count of acyclic orientations of \(K_{a,b}\) with poly-Bernoulli numbers; the total count is not the minimum-cost subfamily count. Borradaile, Iglesias, Migler, Ochoa, Wilfong and Zhang established general indegree-fairness results for unconstrained orientations and an acyclic maximum-indegree algorithm and hardness results, but no biclique-specific universal strictly convex minimizer enumeration.

## Limitations
The theorem assumes a common strictly convex function across **all vertices** and exact complete-bipartite adjacency. It makes no claim of universality for vertex-specific objectives, arbitrary bipartite graphs, or convex functions with flat increments (which can have extra optimal orientations). The literature comparison does not establish absolute bibliographic priority, and no independent mathematical audit has been performed.

## References
1. Nóra A. Borsik and Péter Madarasi, *Separable convex optimization over indegree polytopes*, arXiv:2509.06182, initial public preprint 2025-09-07, https://arxiv.org/abs/2509.06182.
2. Douglas B. West, *Acyclic orientations of complete bipartite graphs*, Discrete Mathematics **138** (1995), 393–396, https://dwest.web.illinois.edu/pubs/aobip.pdf.
3. Peter J. Cameron, C. A. Glass, Kamilla Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685, https://arxiv.org/abs/1412.3685.
4. Glencora Borradaile, Jennifer Iglesias, Theresa Migler, Antonio Ochoa, Gordon Wilfong and Lisa Zhang, *Egalitarian Graph Orientations*, Journal of Graph Algorithms and Applications **21** (2017), 687–708, arXiv:1212.2178, https://arxiv.org/abs/1212.2178.
