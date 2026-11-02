# Power-domination spectra and sparse-sensor limits for categorical products of complete graphs

## Finding

Let \(m,n\ge3\) and let \(G_{m,n}=K_m\times K_n\) denote the **categorical (direct, tensor) product**, not the Cartesian product. Its vertices are \((i,j)\) for \(i\in[m]\), \(j\in[n]\), with two vertices adjacent precisely when both coordinates differ. A nonempty set \(S\) is **power dominating** if initially every vertex in its closed neighborhood is observed and, in each succeeding simultaneous round, every observed vertex with a unique unobserved neighbor forces that neighbor; every vertex must eventually become observed.

**Structure theorem.** A nonempty \(S\) is power dominating precisely when one of these conditions holds:

1. \(S\) contains two cells in different rows **and** different columns;
2. \(|S|\ge2\), all cells of \(S\) lie in one row, and \(|S|\ge n-2\);
3. \(|S|\ge2\), all cells of \(S\) lie in one column, and \(|S|\ge m-2\).

Every successful set finishes after no more than **one forcing round** following the initial domination step. Every failed set stalls after that initial step. In particular, the full power-domination polynomial, with a coefficient for every possible sensor count, is

\[
\mathcal P_{m,n}(z)
=(1+z)^{mn}-1-mnz
-m\sum_{k=2}^{n-3}\binom nk z^k
-n\sum_{k=2}^{m-3}\binom mk z^k.
\]

Sums with lower bound exceeding upper bound are zero. Thus the exact number of minimum (two-vertex) power-dominating sets is

\[
2\binom m2\binom n2+
\mathbf1_{\{n\le4\}}m\binom n2+
\mathbf1_{\{m\le4\}}n\binom m2.
\]

The maximum size of a failed nonempty placement and the minimum universal-success cardinality are, respectively,

\[
\overline\gamma_p(G_{m,n})=\max\{1,m-3,n-3\},
\qquad
\overline\gamma_p(G_{m,n})+1=\max\{2,m-2,n-2\}.
\]

If each sensor is chosen independently with probability \(p=\lambda/(mn)\), for fixed \(\lambda>0\), then the success probability has limits

\[
\lim_{n\to\infty}\Pr(\text{power domination})
=1-me^{-\lambda(1-1/m)}+(m-1)e^{-\lambda}
\quad\text{for fixed }m\ge3,
\]

whereas if both \(m,n\to\infty\), the limit is

\[
1-(1+\lambda)e^{-\lambda}.
\]

## Assumptions and scope

Graphs are simple and finite. Parameters are integers \(m,n\ge3\). A forcing round is simultaneous: every observed vertex with exactly one currently unobserved neighbor forces it, and all such forces are then applied together. The empty sensor set is not power dominating. The graph product is **categorical**, with adjacency requiring both coordinates to differ; it is the complement of the rook graph \(K_m\square K_n\), so results for the latter cannot be transferred without a separate argument. Every vertex and every sensor placement is distinguished by its row and column indices.

## Proof

**Lemma 1 (one sensor stalls).** Take \(S=\{(a,b)\}\). After the initial domination step, the unobserved vertices are the other cells of row \(a\) and column \(b\). The seed has no unobserved neighbors; every other observed vertex \((c,d)\), with \(c\ne a\) and \(d\ne b\), has exactly \((n-2)+(m-2)=m+n-4\ge2\) unobserved neighbors. Thus no force is possible and \(S\) fails.

**Lemma 2 (nonattacking pair succeeds in one round).** Take \(S=\{(a,b),(c,d)\}\), where \(a\ne c\) and \(b\ne d\). The only cells not in the closed neighborhood of \(S\) are \((a,d)\) and \((c,b)\): a cell failing adjacency to both seeds must share the first seed's row or column and the second seed's row or column. Choose any column \(e\notin\{b,d\}\), possible because \(n\ge3\). The observed vertex \((c,e)\) has exactly one unobserved neighbor, \((a,d)\), while \((a,e)\) has exactly one unobserved neighbor, \((c,b)\). Both cells are therefore observed after one forcing round. Power domination is monotone under adding seeds, and any superset of this pair also finishes in at most that round.

**Lemma 3 (sets lacking a nonattacking pair).** Let \(|S|\ge2\). If every pair of selected cells shares a row or a column, all selected cells lie in a single row or single column. To see this, two distinct cells sharing a row have different columns, so any third cell sharing a coordinate with both must lie in their common row; the column argument is symmetric.

Suppose \(S\) consists of \(t\ge2\) cells in one row \(a\). Since the selected columns are distinct, every cell outside that row is adjacent to at least one seed and is initially observed. Exactly \(u=n-t\) cells in row \(a\) remain unobserved. A vertex outside row \(a\) has either \(u\) or \(u-1\) unobserved neighbors, depending on whether its column is among the omitted columns; all vertices in row \(a\) have none. If \(u\ge3\), nobody can force, so the set fails. If \(u=0\), initial observation succeeds. If \(u=1\), any observed cell outside row \(a\) in a different column can force the missing cell. If \(u=2\), observed cells outside the row in the two missing columns force the opposite missing cells simultaneously. Hence success occurs exactly for \(u\le2\), equivalently \(t\ge n-2\). The column case is identical with \(m\) and \(n\) interchanged. Lemmas 1–3 prove the structure theorem, the one-step bound and the immediate-stalling assertion.

**Enumerating all placements.** All nonempty subsets except the singleton seeds and the failed one-row or one-column sets of sizes at least two succeed. A failed set of cardinality at least two cannot lie simultaneously in one row and one column; thus the two failure classes are disjoint. There are \(m\binom nk\) failed row placements of cardinality \(k\) for \(2\le k\le n-3\), and \(n\binom mk\) failed column placements for \(2\le k\le m-3\). Subtracting these and the empty set and \(mn\) singletons from \((1+z)^{mn}\) proves the complete polynomial. Its degree-two coefficient gives the minimum multiplicity: nonattacking pairs number \(2\binom m2\binom n2\), and attacking pairs succeed only for row length \(n\le4\) or column height \(m\le4\). The scalar minimum of two was previously known; here its multiplicity is explicit.

The largest failed placement has cardinality \(\max\{1,n-3,m-3\}\), attained by a singleton or by a row or column selection of that size whenever it is at least two. Therefore every set of at least one more vertex succeeds, with examples showing that this universal threshold is sharp.

**Sparse-sensor limits.** With \(p=\lambda/(mn)\), an empty or singleton seed contributes asymptotic failure probability \((1+\lambda)e^{-\lambda}\). For fixed \(m\), a failed row selection in a specified row with at least two sensors has probability tending to \(e^{-\lambda(1-1/m)}-e^{-\lambda}-(\lambda/m)e^{-\lambda}\); the excluded large selections have vanishing probability. There are \(m\) disjoint such row failure events, while the chance of a failed column selection of size at least two is \(O(1/n)\). Adding gives failure \(m e^{-\lambda(1-1/m)}-(m-1)e^{-\lambda}\), proving the first limit. If both dimensions diverge, the probability of any selected pair sharing a row is at most \(m\binom n2 p^2=O(1/m)\), and the analogous column probability is \(O(1/n)\); hence all failed sets of size at least two have vanishing probability, and the limiting success probability is the Poisson probability of selecting at least two vertices.

## Verification

The accompanying standalone Python program `verify_power_product.py` constructs the direct-product adjacency lists and independently simulates every legal simultaneous forcing round. It compares both success status and the exact coefficient formula, checks that failed configurations cannot make any forcing move, and verifies that successful configurations finish in at most one such round. It exhausts every nonempty vertex subset for parameter pairs \((3,3)\), \((3,4)\), \((3,5)\), \((4,4)\), \((4,5)\), and \((5,3)\), and independently examines all subsets of sizes up to four or three in \((5,5)\), \((5,6)\), and \((6,6)\). The verifier prints `VERIFY_OK`. These finite computations corroborate, but do not replace, the preceding all-orders proof.

## Relationship to prior work

The **power-domination polynomial** was introduced and studied by Brimkov, Patel, Suriyanarayana and Teich (2018). Their full preprint develops general algebraic results and explicit formulas for several graph families, but it does not state the above categorical-product formula, the complete failure classification or the sparse-sensor aspect-ratio limit. The **failed power-domination number** was introduced by Glasser, Jacob, Lederman and Radziszowski (2019); their full preprint treats several families including complete bipartite graphs, not this tensor product. Vemuri (2019) studies ordinary and total domination in direct products of complete graphs, a distinct, non-equivalent property. The scalar fact that the power-domination number of \(K_m\times K_n\) is two in this range was reported by Varghese and Vijayakumar (2011), and is **not** presented as new. The present result concerns the entire cardinality spectrum, the sharp universal threshold, forcing-time dichotomy and two asymptotic sensing limits.

## Limitations

The theorem applies only to two complete factors with both orders at least three; products involving \(K_2\), higher direct-product dimensions and sensor constraints beyond cardinality are not covered. Priority against unindexed or inaccessible historical literature has not been independently certified. The 2011 conference text was identifiable through indexed records but not available for full-text inspection. The computational tests are finite, whereas the infinite conclusion rests on the lemmas above. Independent mathematical review remains outstanding.

## References

- B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (2018-05-28). https://arxiv.org/abs/1805.10984
- A. Glasser, B. Jacob, E. Lederman, S. Radziszowski, *Failed power domination on graphs*, arXiv:1909.02057v1 (2019-09-04). https://arxiv.org/abs/1909.02057
- H. Vemuri, *Domination in direct products of complete graphs*, arXiv:1908.02445v1 (2019-08-07). https://arxiv.org/abs/1908.02445
- T. C. Varghese, A. Vijayakumar, *Power domination in some classes of graphs*, European Conference on Combinatorics, Graph Theory and Applications (2011), accessible indexed conference description, full text not independently inspected.
