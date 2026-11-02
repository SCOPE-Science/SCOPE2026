# Exact initial online-shattering thresholds for finite-chain intervals

## Finding
Let \(X_n=\{1,\ldots,n\}\) with its usual order, and let \(\mathcal I_n=\{[a,b]\cap X_n:1\le a\le b\le n\}\), viewed as Boolean point-membership concepts. For every \(1\le n\le55\), the exact Littlestone dimension is given by the following sharp attainment thresholds: the smallest \(n\) permitting depth \(d\), for \(d=1,\ldots,10\), is respectively
\[
(2,3,4,6,9,13,19,27,39,55).
\]
Equivalently, \(\operatorname{Ldim}(\mathcal I_1)=0\), and for \(2\le n\le55\) the value is the number of entries in this ordered threshold list that are at most \(n\). This is a finite exact statement, **not** an extrapolated formula for all \(n\). The VC dimension is \(2\) for all \(n\ge3\), so the online/static difference reaches \(8\) at \(n=55\). The first failure of the naive cardinality upper bound \(\lfloor\log_2|\mathcal I_n|\rfloor\) occurs already at \(n=8\): there are \(36\) concepts, yet the Littlestone dimension is \(4\), not \(5\).

More generally, the following **exact structural recurrence** applies to any union of interval classes supported on finitely many pairwise disjoint finite integer blocks; it reduces adaptive shattering to the unordered multiset of block lengths, rather than a subset of the full concept set. For a nonempty multiset \(S\) of positive block lengths, define \(D(S)\) recursively by
\[
D(S)=\max\Bigl(\{0\}\cup\bigl\{1+\min\bigl(\lfloor\log_2 j\rfloor+\lfloor\log_2(s-j+1)\rfloor,D((S\setminus\{s\})\uplus\{j-1,s-j\}_{>0})\bigr):\ s\in S,\ 1\le j\le s,\ (S\setminus\{s\})\uplus\{j-1,s-j\}_{>0}\ne\varnothing\bigr\}\Bigr).
\]
Here \(\uplus\) denotes multiset union, and \(\{u,v\}_{>0}\) means retaining the strictly positive entries. The recursion is well founded because every recursive argument has total block length exactly one less. The claimed values are \(D(\{n\})\) for \(n\le55\).

## Assumptions and scope
All intervals are **nonempty**, the ambient point set is finite and ordered, and an adaptive query asks the membership of one point. Empty intervals are excluded; adding one changes some small cases. The theorem concerns the standard deterministic complete-binary-tree notion of Littlestone dimension (also called thicket dimension or Shelah \(2\)-rank in closely related settings), not randomized mistake complexity, transductive learning, or an arbitrary unrestricted subset family. There is no assertion that the observed pattern of thresholds continues after depth \(10\).

## Proof
**Positive-state lemma.** Suppose the labels observed so far contain at least one positive answer, and the remaining intervals all range over a single original block. Let \(L\) be the set of eligible left endpoints and \(R\) the set of eligible right endpoints. The positive answers force every left endpoint to precede every right endpoint; the negative answers impose independent half-line exclusions on one endpoint or the other. Thus \(L\) and \(R\) are consecutive nonempty integer ranges and every pair \((\ell,r)\in L\times R\) determines exactly one viable interval. Point queries to the left of the forced positive core induce threshold queries on \(L\), and point queries to the right induce threshold queries on \(R\); queries inside the core are constant. Consequently the viable-class dimension is
\[
\lfloor\log_2|L|\rfloor+\lfloor\log_2|R|\rfloor.
\]
Indeed a threshold family on \(m\) possible cut positions has dimension \(\lfloor\log_2m\rfloor\) by balanced bisection and cardinality. For concept-class products on disjoint query domains, Littlestone dimension is additive: the lower bound concatenates optimal trees, while the upper bound follows by induction from the fact that a query acts on only one factor and the ordinary two-branch rank recurrence.

**Zero-state lemma.** Before any positive answer, every surviving interval lies entirely inside one of the maximal contiguous blocks of points not yet queried negatively. If the lengths of these blocks form \(S\), a query at the \(j\)-th position of a block of length \(s\) produces: (i) a positive branch with independently selectable left and right endpoints of cardinalities \(j\) and \(s-j+1\), respectively; and (ii) a negative branch where that block is replaced by the two surviving lengths \(j-1\) and \(s-j\), with zero lengths omitted. These are **all** possible nonconstant queries. The positive-state lemma gives the first branch rank exactly; induction on total unqueried length gives the second. The standard complete-tree rank identity \(\operatorname{Ldim}(F)=\max_q(1+\min\{\operatorname{Ldim}(F_{q=0}),\operatorname{Ldim}(F_{q=1})\})\), with constant queries excluded and singleton rank zero, proves the displayed recurrence, including the empty-negative-branch exception.

**Finite cutoff calculation.** The standalone `verify.py` evaluates this proved recurrence by exact integer operations, caching each sorted multiset of block lengths. It obtains the full 55-entry dimension vector in `dimensions.json`; its changes of value occur exactly at the ten claimed points. The script independently computes the ordinary hypothesis-bitmask tree recurrence for every \(n\le12\), giving agreement in all 12 cases. A complete depth-10 adaptive tree on \(55\) points is embedded as `tree_n55_d10.json`: it has \(1,023\) internal queries and \(1,024\) different terminal interval witnesses, each independently checked against all ten responses on its path. The recurrence establishes all finite upper bounds and all intermediate lower bounds; the explicit tree is an additional check at the largest threshold.

**VC calculation.** Every three fixed points cannot be shattered because the label pattern positive-negative-positive is not an interval trace. For \(n\ge3\), the two endpoints \(1,3\) are shattered: the four traces are realized by \([2,2]\), \([1,1]\), \([3,3]\), and \([1,3]\). Hence the VC dimension is \(2\). Finally \(|\mathcal I_8|=8\cdot9/2=36\), so the cardinality bound permits depth five, whereas the exact recurrence gives only four.

## Verification
From a directory containing `verify.py`, `dimensions.json`, and `tree_n55_d10.json`, execute `python verify.py` (Python 3, standard library only). The expected final line is `FINAL_ORDERED_INTERVAL_CHECKS_PASS`. This recreates the 55 values, independently verifies the first 12 against direct set-system recursion, verifies the first cardinality gap, and checks all \(2^{10}\) root-to-leaf assignments of the depth-ten witness tree. Integer arithmetic is exact. The computed table is a finite result; no finite experiment is used as a proof of an unbounded threshold pattern.

## Relationship to prior work
Bhaskar's *Thicket Density* (2017) supplies the general adaptive-tree/thicket framework, including the general rank recursion and the Sauer–Shelah-type context, but does not present these ordered-interval cutoffs in the inspected main text. Walker's 2022 tree-dimension paper considers general growth and extremal-tree structure; the accessible abstract does not itself imply the interval-specific finite threshold values. Chase, Freitag and Reyzin's 2023/2026 work develops query-learning applications and discusses a **disjoint infinite collection** of intervals of Littlestone dimension one, a different concept class from **all intersecting and nested nonempty intervals in one finite chain**. The present contribution is the special-purpose state compression and its exact cutoff census, not the generic Littlestone recurrence itself.

## Limitations
The table is certified only for \(n\le55\), and the apparent arithmetic regularity of its thresholds is not claimed beyond depth ten. The empty-concept convention differs from the common rank \(-1\) convention for empty families; the recurrence simply excludes constant queries to avoid ambiguity. This is a self-review and finite computational verification, **not independent scientific audit or an exhaustive historical-priority determination**. Broader or differently named previously published interval-learning results may contain equivalent formulas; that residual risk remains.

## References
- S. Bhaskar, *Thicket Density*, arXiv:1702.03956v1, first posted 2017-02-13, https://arxiv.org/abs/1702.03956.
- R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211v1, first posted 2022-03-23, https://arxiv.org/abs/2203.12211.
- H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812v1, first posted 2023-10-07, https://arxiv.org/abs/2310.04812; *Information and Computation* 309 (2026), article 105424.
