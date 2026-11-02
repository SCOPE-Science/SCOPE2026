# Online entropy efficiency and first eight depth thresholds in prefix--sparse convex geometries

## Finding
For every pair of integers \(1\le k\le n-2\), let \(P(k,n)\) denote the family of subsets \(A\subseteq[n]\) satisfying the Knauer--Trotter rule: whenever \(|A|=k+i-1\), the initial segment \([i-1]\) is contained in \(A\). Equivalently, the indicator word avoids a (not necessarily adjacent) subsequence of one zero followed by \(k+1\) ones. With membership queries on coordinates, write \(L(k,n)=\operatorname{Ldim}(P(k,n))\). Then
\[
\left\lfloor\log_2(n+1)\right\rfloor\le L(k,n)\le U(k,n),\qquad
U(k,n)=\max\left\{d\in\mathbb Z_{\ge0}:2^d\le1+\sum_{j=0}^{k}(n-j)\binom dj\right\}.
\]
For each fixed \(k\ge1\),
\[
L(k,n)=\log_2 n+O_k(\log_2\log_2 n),\qquad
\lim_{n\to\infty}\frac{L(k,n)}{\log_2|P(k,n)|}=\frac1{k+1}.
\]
For \(k=1\), a complete exact finite online recurrence gives the first occurrence of depths \(3,4,5,6,7,8\) at respective ground-set sizes \(4,7,12,21,39,69\); depth two holds at \(n=3\), and depth nine does not occur through \(n=69\). Therefore these thresholds specify \(L(1,n)\) for every integer \(3\le n\le69\). The family is Sauer-maximum with \(|P(k,n)|=\sum_{j=0}^{k+1}\binom nj\) and VC dimension \(k+1\); this static fact is prior context, not a novelty claim.

## Assumptions and scope
The ground set is \([n]=\{1,\ldots,n\}\); \([0]\) is empty. The first-zero rule is: either all coordinates are one, or the first zero has position \(i\) and at most \(k\) later coordinates are one. A complete binary membership-query tree is shattered when every root-to-leaf binary sequence is realized by a concept; its maximum possible depth is the Littlestone dimension. The fixed-\(k\) asymptotics take \(n\to\infty\) while \(k\) is held constant. The exact finite table concerns \(k=1\) and no larger \(n\).

## Proof
**Equivalent descriptions.** If the indicator has first zero at \(i\) and exactly \(r\) later ones, its total size is \(i-1+r\). The rule for a nonempty initial segment forces \(r\le k\). Conversely, with \(r\le k\), any required initial segment has length at most \(i-1\). An alternative direct argument shows that a zero followed by \(k+1\) later ones violates the rule. Hence the family consists of the all-one word and the disjoint first-zero slices \(\mathscr F_i\) for \(1\le i\le n\), with the suffix after \(i\) containing at most \(k\) ones. Thus
\[
|P(k,n)|=1+\sum_{i=1}^{n}\sum_{j=0}^{\min(k,n-i)}\binom{n-i}{j}=\sum_{j=0}^{k+1}\binom nj.
\]
The equality follows from the hockey-stick identity. Every support of size at most \(k+1\) is shattered: for any target labeling, choose its first requested zero, put ones on all earlier coordinates, then exactly the requested later ones (at most \(k\)); if no zero is requested choose the all-one word. Any support of size \(k+2\) is not shattered, as the label with zero at its least coordinate and ones elsewhere would require \(k+1\) ones after the first zero. This recovers the established Sauer-maximum VC dimension.

**Lower online bound.** All initial segments \([0],[1],\ldots,[n]\) lie in \(P(k,n)\). Membership at coordinate \(j\) asks whether an unknown cutoff is at least \(j\). By recursively choosing a midpoint cutoff, these \(n+1\) ordered thresholds support a complete binary tree of depth \(\lfloor\log_2(n+1)\rfloor\).

**Upper online bound.** Fix any shattered complete binary query tree of depth \(d\). A concept generates a unique path. For a fixed first-zero slice \(\mathscr F_i\), encode each realized path by the set of depths at which its queried coordinate exceeds \(i\) and the response equals one. Each such depth uses a distinct later-one coordinate on the path (repeated queries cannot occur on any shattered path), so the code has at most \(k\) entries. Codes distinguish paths: replay the fixed tree from its root; a query below \(i\) is answered one, a query equal to \(i\) is answered zero, and a query above \(i\) is answered one exactly when the current depth belongs to the code. This uniquely reconstructs the entire response path. Hence at most \(\sum_{j=0}^{\min(k,n-i,d)}\binom dj\) leaves are realized by that slice; the all-one concept contributes at most one more. Every one of the \(2^d\) leaves has a realizing concept, and distinct slices are disjoint. Therefore
\[
2^d\le1+\sum_{i=1}^{n}\sum_{j=0}^{\min(k,n-i,d)}\binom dj
=1+\sum_{j=0}^{\min(k,d)}(n-j)\binom dj.
\]
This proves the stated upper fence. Since its right side is at most \(1+n(k+1)(d+1)^k\), elementary logarithms give \(d\le\log_2 n+O_k(\log_2\log_2 n)\). For fixed \(k\), the displayed cardinality is asymptotic to \(n^{k+1}/(k+1)!\), so division gives the entropy ratio \(1/(k+1)\).

**Finite depth thresholds.** For a nonempty version space \(H\), define \(F(H,0)=\mathrm{true}\) and \(F(H,d)=\bigvee_x[F(H\cap H_x^+,d-1)\land F(H\cap H_x^-,d-1)]\), where \(H_x^\pm\) are concepts with prescribed membership at coordinate \(x\). This is an exact induction on \(d\): the first query must work for both branches, and the recursion tests every possible coordinate. The attached standard-library verifier evaluates this recurrence on each of the twelve threshold-adjacent cases \((n,d)=(3,3),(4,3),(6,4),(7,4),(11,5),(12,5),(20,6),(21,6),(38,7),(39,7),(68,8),(69,8)\), obtains failure immediately before and success at each listed threshold, and separately proves \(F(P(1,69),9)=\mathrm{false}\). The concept classes are nested under coordinate restriction, so online depth is nondecreasing in \(n\); the six transitions and absence of depth nine determine the entire claimed initial spectrum. These are finite exhaustive conclusions only, not an all-order closed formula.

## Verification
Run `python3 verify_prefix_sparse.py` using Python 3.9 or newer, without third-party packages. The program independently reconstructs the family by its cardinality/prefix rule and by first-zero enumeration for small instances, exhaustively tests static traces, computes online feasibility by the exact memoized first-query recurrence at all stated threshold boundaries and the depth-nine exclusion, and checks the universal upper fence against its finite values. Successful output terminates in `ALL_PREFIX_SPARSE_ONLINE_CHECKS_PASS`. The infinite-family upper and lower bounds are mathematical arguments above, not consequences of finite testing.

## Relationship to prior work
Knauer and Trotter introduced and studied \(P(k,n)\) in *Concepts of Dimension for Convex Geometries* (arXiv:2303.08945, 2023), including its convex-geometric structure, cardinality, and static VC dimension. Their use of the abbreviation `ldim` denotes **poset local dimension**, not the online Littlestone dimension evaluated here. Walker's *Tree Dimension and the Sauer--Shelah Dichotomy* (arXiv:2203.12211) and Bhaskar's *Thicket Density* (arXiv:1702.03956) provide broader tree-shattering and online-dimension context but no identified value for this particular family. The new objects of assessment are the slice-encoding upper fence, the asymptotic entropy-efficiency ratio, and the exact initial depth thresholds; the established static facts are not claimed to be original.

## Limitations
The upper fence need not be exact for all parameters. An exact formula for arbitrary \(k,n\) is not claimed. The numerical thresholds are proved only through \(n=69\) for \(k=1\). Search and accessible-text comparisons cannot exclude unpublished or differently named equivalent results. Independent mathematical validation is not represented by the reproducible finite checker.

## References
Knauer, K., and Trotter, W. T., *Concepts of Dimension for Convex Geometries*, 2023, https://arxiv.org/abs/2303.08945 (original posting March 15, 2023).

Walker, R., *Tree Dimension and the Sauer--Shelah Dichotomy*, 2022, https://arxiv.org/abs/2203.12211.

Bhaskar, S., *Thicket Density*, 2017, https://arxiv.org/abs/1702.03956.
