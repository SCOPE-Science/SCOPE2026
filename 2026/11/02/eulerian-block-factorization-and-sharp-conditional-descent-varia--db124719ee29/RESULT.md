# Eulerian block factorization and sharp conditional-descent variance bounds for permutation records

## Finding

Let \(\pi\) be a uniformly random permutation of \([n]\). The exact law of its descent count, conditional on **all** left-to-right upper-record positions, is a convolution of independent Eulerian descent laws, plus a deterministic boundary contribution. The resulting family admits sharp, attained, finite-sample bounds on conditional variance when only the number of record positions is fixed.

Write \(\mathcal R=\{i\in[n]:\pi(i)>\max_{j<i}\pi(j)\}\), with the maximum over the empty set understood as smaller than every label, and \(D=\sum_{i=1}^{n-1}\mathbf1\{\pi(i)>\pi(i+1)\}\). Fix any \(S\subseteq[n]\) containing \(1\), and condition on \(\mathcal R=S\). Define \(\ell_1,\ldots,\ell_m\) as the lengths of the maximal nonempty intervals of consecutive positions in \([n]\setminus S\). Let \(Z=n-|S|\), so \(\sum_{j=1}^m\ell_j=Z\); when \(Z=0\), take \(m=0\). Define the ordinary Eulerian polynomial by
\[
 A_\ell(t)=\sum_{\sigma\in\mathfrak S_\ell}t^{\operatorname{des}(\sigma)}\qquad(\ell\ge1).
\]
Then
\[
 \boxed{\mathbb E[t^D\mid\mathcal R=S]=t^m\prod_{j=1}^{m}\frac{A_{\ell_j}(t)}{\ell_j!}.}
\]
Consequently,
\[
 \boxed{\mathbb E[D\mid\mathcal R=S]=\frac{Z+m}{2},\qquad
 \operatorname{Var}(D\mid\mathcal R=S)=\frac1{12}\sum_{j:\ell_j\ge2}(\ell_j+1).}
\]

For fixed \(n\ge1\) and \(1\le K\le n\), consider all record-position patterns with exactly \(K\) records, and write \(Z=n-K\). The **attainable sharp lower and upper variance bounds** are
\[
 \boxed{V_{\min}(n,K)=
 \begin{cases}0,&Z\le K,\\(Z-K+2)/12,&Z>K,\end{cases}}
\]
\[
 \boxed{V_{\max}(n,K)=
 \begin{cases}0,&Z\le1,\\(Z+\min\{K,\lfloor Z/2\rfloor\})/12,&Z\ge2.
 \end{cases}}
\]
They concern conditioning on a **full record-position pattern**, then optimizing across patterns of fixed record count; they are not claims about conditioning only on \(|\mathcal R|=K\).

For instance, when \(n=9\) and \(K=3\), the nonrecord block lengths \((4,1,1)\) give the minimum variance \(5/12\); lengths \((2,2,2)\) give the maximum variance \(3/4\).

## Assumptions and scope

The sampling law is uniform on the \(n!\) permutations of distinct labels. The only record notion here is a strict **left-to-right upper record at a position**, not a record value, a right-to-left record, a fixed point, or an excedance. All \(2^{n-1}\) subsets \(S\subseteq[n]\) containing \(1\) are feasible. The Eulerian normalization is \(A_\ell(1)=\ell!\), so the displayed product is a probability generating function. The case of no nonrecord blocks uses an empty product of one. All inequalities and formulas hold at the endpoints \(n=1\), \(Z=0\), and \(Z=1\).

## Proof

**Step 1 — positive-probability fibers and independent block orders.** Uniform random permutations can be represented by the relative ranks of independent continuous identically distributed observations \(X_1,\ldots,X_n\). Their successive insertion ranks are independent, uniform on \([i]\), hence \(\mathbb P(\mathcal R=S)=\prod_{i\in S}(1/i)\prod_{i\notin S}(1-1/i)>0\). Fix such a fiber \(\{\mathcal R=S\}\). In every maximal nonrecord interval, rearranging its entries among those positions cannot change any record indicator: every such entry is smaller than the immediately preceding record value; every later record value already exceeds all preceding entries. The fiber is therefore invariant under the Cartesian product of full symmetric groups acting on the positions within each nonrecord interval. This action is transitive on all relative orderings within each interval, so the product vector of interval-relative permutations is uniform, and its coordinates are mutually independent. This argument is conditional on the entire fiber, not merely an unconditional independence assertion.

**Step 2 — boundary descents and Eulerian convolution.** For each nonrecord interval there is exactly one descent across its left boundary: the preceding record value is larger than the interval's first entry. At every left boundary of a record position after the first, the comparison is an ascent because the record exceeds every earlier entry. All remaining adjacent comparisons are the internal comparisons of the nonrecord intervals. Thus \(D=m+\sum_j D_j\), where the \(D_j\) are independent and each follows the descent-number distribution of a uniform permutation of length \(\ell_j\). Their probability generating functions are \(A_{\ell_j}(t)/\ell_j!\), proving the factorization.

**Step 3 — moments.** For \(\ell\ge2\), the \(\ell-1\) consecutive descent indicators have mean \(1/2\), variance \(1/4\), adjacent covariance \(-1/12\), and all nonadjacent covariances zero; the last two assertions follow from uniform orders of three observations and disjoint underlying observation sets. Therefore a length-\(\ell\) Eulerian descent number has mean \((\ell-1)/2\) and variance \((\ell+1)/12\). At \(\ell=1\), both are zero. Summing over independent intervals and adding their \(m\) obligatory descents gives the moment identities.

**Step 4 — sharp extrema.** A record-position pattern with exactly \(K\) records supports precisely those ordered positive nonrecord-block lengths that form a composition of \(Z\) into \(m\le K\) parts: place each of these \(m\) blocks after a distinct record and place any other records consecutively. Conversely, any pattern induces such a composition. For \(Z>0\), let \(s\) denote the number of singleton blocks; then
\[
 12\,\operatorname{Var}(D\mid\mathcal R=S)=Z+m-2s.
\]
If \(Z\le K\), all \(Z\) nonrecords can be isolated into singleton blocks and the minimum is zero. If \(Z>K\), then \(m\le K<Z\) and at most \(m-1\) blocks can be singletons, so
\[
 Z+m-2s\ge Z-m+2\ge Z-K+2.
\]
Take \(m=K\), with \(K-1\) singleton blocks and one block of length \(Z-K+1\), to attain equality.

For the maximum, every non-singleton block has length at least two, so \(s\ge\max\{0,2m-Z\}\). Consequently the variance numerator is at most \(Z+m\) when \(m\le\lfloor Z/2\rfloor\), and at most \(3Z-3m\) when \(m>\lfloor Z/2\rfloor\). The first upper bound increases in \(m\); the second strictly decreases. Hence the maximum occurs at \(m=\min\{K,\lfloor Z/2\rfloor\}\), with no singleton blocks. A composition of \(Z\) into this many parts of size at least two always exists for \(Z\ge2\), proving the bound and its attainment. For \(Z\le1\) the variance is identically zero. This completes the all-size proof.

## Verification

Run `python3 verify.py` using Python's standard library only. The verifier independently enumerates all permutations through \(n=9\), checks the conditional probability-generating function coefficient by coefficient for every feasible record-position set, and checks its first two moments as exact rational numbers. It also checks the claimed sharp minimum and maximum for every \(n\le15\) and every possible record count by enumerating all record-position patterns without enumerating all permutations at those larger sizes. The recorded execution passed **1,151 exact assertions**. These finite checks corroborate; the preceding combinatorial proof, not the enumeration, establishes the infinite-size assertion.

## Relationship to prior work

Gnedin's work on coherent random permutations with record statistics establishes the classical initial-rank representation and record-position foundations. Dzhumadil'daev studies joint descent-position and right-maximal-record statistics and noncommutative code equidistribution; this is a serious related comparison, but its stated equidistribution identities do not give the left-to-right full-record-fiber Eulerian product or the fixed-record-count sharp variance bounds. Jin's Euler–Stirling generating functions aggregate descent and record **counts**, not a full record-position pattern; aggregate enumerators do not recover the entire collection of conditional fiber laws. The present statement is about conditional distributions and the sharp patternwise variance envelope, not a claim to first discover Eulerian numbers or independent insertion ranks.

## Limitations

The product formula is specific to a uniformly random permutation. It does not assert the same conditional law for arbitrary nonidentically distributed observations, nonuniform permutation measures, or other notions of records. The variance bounds are over the possible patterns with a fixed record count and are not the conditional variance given only that count. Exhaustive computational checks end at the stated finite limits. The cited sources do not eliminate all historical priority risks, and no independent audit has been performed.

## References

- A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first submitted 17 November 2006. https://arxiv.org/abs/math/0611538
- A. Dzhumadil'daev, *MacMahon's theorem for a set of permutations with given descent indices and right-maximal records*, Electronic Journal of Combinatorics 17 (2010), R34. https://doi.org/10.37236/306
- E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789, first submitted 17 October 2022. https://arxiv.org/abs/2210.08789
