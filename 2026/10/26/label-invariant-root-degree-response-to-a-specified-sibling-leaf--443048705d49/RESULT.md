# Label-invariant root-degree response to a specified sibling-leaf pair in uniform recursive trees

## Finding
In a uniformly random recursive tree on labels \(1,\ldots,n\), \(n\ge3\), let \(R\) be the number of children of vertex \(1\). Let \(Z\) count **unordered pairs** of distinct leaves having the same parent, with each pair counted once even if its parent has three or more leaf children. For each \(1\le v<a<b\le n\), denote by \(E_{vab}\) the event that both \(a\) and \(b\) are leaf children of \(v\). Then
\[
\Pr(E_{vab})=\frac1{(n-1)(n-2)},\qquad
\mathbb E[R\mid E_{vab}]-\mathbb E[R]
=2\mathbf1_{\{v=1\}}-\frac1{n-2}-\frac1{n-1}.
\]
Thus the **entire conditional mean response** depends only on whether the shared parent is the root: the birth labels of the parent and leaf pair do not affect the shift. In particular,
\[
\mathbb E[Z]=\frac n6,\quad
\operatorname{Cov}(R,Z)
=\frac{4n^2-15n+12}{6(n-1)(n-2)}>0,
\quad\lim_{n\to\infty}\operatorname{Cov}(R,Z)=\frac23.
\]

## Assumptions and scope
The vertex set is \([n]\). For every \(j\in\{2,\ldots,n\}\), vertex \(j\) independently picks a parent \(P_j\) uniformly from \([j-1]\). A leaf has zero children. The random variable \(Z\) counts all sibling-leaf **pairs**, not merely those whose parent has exactly two children; hence a parent with \(s\) leaf children contributes \(\binom{s}{2}\). The statement covers every integer \(n\ge3\) and every admissible triple \(v<a<b\), with no limit-order or asymptotic hypothesis. The quantity \(R=\sum_{j=2}^n\mathbf1_{\{P_j=1\}}\) has mean \(H_{n-1}\).

## Proof
**1. Local motif probability.** Event \(E_{vab}\) requires \(P_a=P_b=v\), no \(j\in(a,b)\) to choose \(a\), and no \(j>b\) to choose either \(a\) or \(b\). Independence of the parent variables gives
\[
\Pr(E_{vab})=\frac1{(a-1)(b-1)}
\prod_{j=a+1}^{b-1}\frac{j-2}{j-1}
\prod_{j=b+1}^{n}\frac{j-3}{j-1}
=\frac1{(n-1)(n-2)}.
\]
Empty products are \(1\); the cancellation remains valid when \(b=a+1\) or \(b=n\).

**2. Conditional root degree.** Given \(E_{vab}\), all non-forced parent variables remain independent and uniform over their individually allowed parents. At positions \(a,b\) the root-attachment indicators are both the constant \(\mathbf1_{\{v=1\}}\). Positions strictly between \(a,b\) exclude parent \(a\), giving conditional root-attachment probability \(1/(j-2)\), and positions after \(b\) exclude both \(a,b\), giving \(1/(j-3)\). The other indicators retain probability \(1/(j-1)\). Thus the conditional-minus-unconditional difference is
\[
\begin{aligned}
&2\mathbf1_{\{v=1\}}-\frac1{a-1}-\frac1{b-1}\\
&\quad+\sum_{j=a+1}^{b-1}\left(\frac1{j-2}-\frac1{j-1}\right)
+\sum_{j=b+1}^{n}\left(\frac1{j-3}-\frac1{j-1}\right).
\end{aligned}
\]
The first sum equals \(1/(a-1)-1/(b-2)\), the second equals \(1/(b-2)+1/(b-1)-1/(n-2)-1/(n-1)\), and all dependence on \(a,b\) cancels. This proves the conditional-response formula for every valid triple.

**3. Global covariance.** Write \(I_{vab}=\mathbf1_{E_{vab}}\). Every unordered sibling-leaf pair has exactly one shared parent and hence \(Z=\sum_{v<a<b}I_{vab}\), where the sum ranges over all \(\binom n3\) admissible triples. Consequently
\[
\mathbb E[Z]=\binom n3\frac1{(n-1)(n-2)}=\frac n6.
\]
For any event \(E\) of positive probability, \(\operatorname{Cov}(R,\mathbf1_E)=\Pr(E)(\mathbb E[R\mid E]-\mathbb E[R])\). There are \(\binom{n-1}{2}\) admissible triples with \(v=1\). Summing the local response therefore gives
\[
\begin{aligned}
\operatorname{Cov}(R,Z)
&=\frac{2\binom{n-1}{2}-\binom n3\left(\frac1{n-2}+\frac1{n-1}\right)}{(n-1)(n-2)}\\
&=\frac{4n^2-15n+12}{6(n-1)(n-2)}.
\end{aligned}
\]
The numerator is \(3\) at \(n=3\) and is strictly increasing for integers \(n\ge3\); the ratio tends to \(2/3\). All claims follow.

## Verification
Run \(`python3 verify_cherries.py`\) using only the Python standard library. It exhaustively lists all \((n-1)!\) parent vectors for every \(3\le n\le9\), independently calculates \(R,Z\), and checks the exact mean, covariance, event probabilities and conditional root-degree responses as rational numbers. The tested range includes every admissible triple for each size. All 434 exact assertions passed. These finite checks are sanity tests, not a substitute for the proof above.

## Relationship to prior work
The uniform increasing-parent construction and degree statistics are classical (Janson, 2004/2005). Feng and Mahmoud (2010) treat **fringe** occurrences of specified complete rooted shapes. The present statistic counts a pair of leaf siblings even when their parent has additional children, and the exact conditional root-degree response refers to a specified labeled pair, not to an unconditioned fringe-shape count. Gopaladesikan (2014) develops multivariate fringe-motif methods, a related but not automatically dominating scope. Previously reported root-degree/total-leaf covariance and root-degree/path-length covariance concern different statistics and do not yield the sibling-leaf-pair identity without an additional argument. The core novelty claimed here is the all-label cancellation and resulting closed covariance law, not the independent-parent model or elementary telescoping itself.

## Limitations
These formulas pertain to uniform random recursive trees and **pairs** of terminal siblings, not all terminal pairs or a fixed finite fringe subtree. No statement is made about conditional distributions, concentration, joint central limit theorems, or other tree-growth rules. The historical novelty assessment is provisional because an older general motif treatment might contain an equivalent unlocated identity; the accessible full text and published result summaries consulted did not establish this exact labeled conditional regression. Independent external validation has not been performed.

## References
1. Svante Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* 26 (2005), 69–83; first online November 16, 2004. DOI: 10.1002/rsa.20046.
2. Qunqiang Feng and Hosam M. Mahmoud, “On the variety of shapes on the fringe of a random recursive tree,” *Journal of Applied Probability* 47 (2010), 191–200. DOI: 10.1239/jap/1269610825.
3. Mohan Gopaladesikan, *On the occurrences of motifs in recursive trees, with applications to random structures*, Purdue dissertation (2014), Open Access Dissertations 274; consulted abstract and available presentation, with inaccessible full dissertation noted as a priority risk.
