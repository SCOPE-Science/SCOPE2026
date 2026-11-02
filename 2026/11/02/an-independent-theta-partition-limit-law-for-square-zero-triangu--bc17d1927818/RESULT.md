# An independent theta–partition limit law for square-zero triangular Boolean matrices

## Finding
Let \(B_n\) be selected uniformly from all strictly upper-triangular \(n\times n\) matrices with entries in \(\{0,1\}\) whose square is zero over the Boolean semiring (equivalently, whose ordinary integer matrix square vanishes). Define \(S(B)=\{i:\text{row }i\text{ is nonzero}\}\), \(T(B)=\{j:\text{column }j\text{ is nonzero}\}\), and let \(I(B)=[n]\setminus(S(B)\cup T(B))\). Then \(S(B)\cap T(B)=\varnothing\), and \(\Pr(I(B_n)=\varnothing)\to1\).

On the event \(I(B_n)=\varnothing\), write the ordered binary word on \([n]\) using \(S\) for row-active and \(T\) for column-active indices. If its \(S\)-indices in increasing order are \(s_1<\cdots<s_a\), the reversed list of integers \(\#\{t\in T:t<s_i\}\), \(1\le i\le a\), is a partition \(\Lambda_n\) (trailing zeros allowed). Put \(J_n=|S(B_n)|-\lfloor n/2\rfloor\). Let \(\mathcal P\) be the set of all integer partitions, including the empty partition, and define
\[
Q=\prod_{r\ge1}(1-2^{-r}),\quad Z_0=\sum_{j\in\mathbb Z}2^{-j^2},\quad Z_1=\sum_{j\in\mathbb Z}2^{j-j^2}.
\]
For every fixed integer \(j\) and partition \(\lambda\in\mathcal P\), the parity-dependent joint limits are
\[
\lim_{m\to\infty}\Pr\bigl(I(B_{2m})=\varnothing,J_{2m}=j,\Lambda_{2m}=\lambda\bigr)
=\frac{2^{-j^2}}{Z_0}\,Q2^{-|\lambda|},
\]
\[
\lim_{m\to\infty}\Pr\bigl(I(B_{2m+1})=\varnothing,J_{2m+1}=j,\Lambda_{2m+1}=\lambda\bigr)
=\frac{2^{j-j^2}}{Z_1}\,Q2^{-|\lambda|}.
\]
In both parity classes the full pair converges in total variation on \(\mathbb Z\times\mathcal P\) to a product measure. In particular, the source-side imbalance is independent in the limit of the entire Ferrers-diagram shape of backward cross pairs. The partition-size statistic \(K_n=|\Lambda_n|\) has limiting law \(\Pr(K_n=k)=Qp(k)2^{-k}\), where \(p(k)\) is the ordinary partition number. No total-variation statement is made without specifying the canonical zero-isolate event; it has probability tending to one.

## Assumptions and scope
The product in the Boolean semiring uses \(1+1=1\); for nonnegative binary matrices, zero Boolean square is equivalent to zero ordinary integer square. The matrices are **strictly** upper triangular, not the reflexive upper-triangular semiring (which has diagonal ones). Row and column activity is measured in the fixed increasing coordinate order, not up to conjugacy. The comparison with naturally labelled height-at-most-two posets uses the transitive-closure convention, which equals the adjacency relation because length-two paths are absent. No assumption on prime fields or ordinary linear-algebra rank is used.

A partition is a weakly decreasing finite sequence of positive integers. The empty partition has size zero. The zero rows and columns of an isolated index are both zero, so each non-isolated index belongs to exactly one of \(S\) and \(T\). The stated random partition is defined on the zero-isolate event; extending it arbitrarily off that event does not change the limit.

## Proof
**1. Canonical support bipartition.** For binary \(B\), \((B^2)_{ik}=0\) over the Boolean semiring if and only if there is no length-two directed path \(i\to j\to k\) through a positive entry. Thus no index can have simultaneously a positive incoming and outgoing entry. Every positive entry runs from \(S(B)\) to \(T(B)\), and no edge runs within either set. The isolated set is its complement. As \(B\) is strictly upper triangular, an edge \(s\to t\) is permitted precisely when \(s<t\). Conversely any choice of such edges with all active rows and columns nonzero yields a unique matrix with the indicated support bipartition.

**2. Binary words and Ferrers diagrams.** For a fixed ordered bipartition \([n]=S\sqcup T\), write \(a=|S|\), \(b=|T|\), and \(k=\#\{(s,t)\in S\times T:t<s\}\). Precisely \(ab-k\) forward pairs are available. The number of binary words with sizes \(a,b\) and inversion diagram \(\lambda\) is one, provided that \(\lambda\) fits into the \(a\times b\) rectangle: reading the \(S\)-positions in increasing order gives a nondecreasing sequence of counts of earlier \(T\)-positions, whose reverse is \(\lambda\). Any assignment of entries to the \(ab-k\) forward positions gives a candidate with no length-two paths; the requirement that active rows and columns really be nonzero only removes assignments.

For any *fixed* \(\lambda\) and \(j\), along even dimensions set \(a=m+j\), \(b=m-j\); along odd dimensions set \(a=m+j\), \(b=m+1-j\). As \(m\to\infty\), the diagram fits the rectangle and \(k=|\lambda|\) remains fixed. Every row-active index has at least \(b-k\) allowable outgoing positions and every column-active index has at least \(a-k\) allowable incoming positions. Therefore a union bound shows that the fraction of \(2^{ab-k}\) unrestricted assignments with any forbidden empty row or column is at most
\[
a2^{-(b-k)}+b2^{-(a-k)}=o(1).
\]
The exact support-shape stratum therefore has cardinality \(2^{ab-|\lambda|}(1+o(1))\). The powers are \(ab=m^2-j^2\) for even dimensions and \(ab=m(m+1)+j-j^2\) for odd dimensions.

**3. Tightness and isolates.** Let \(H_n\) count all such matrices and \(H_n^{(0)}\) those without isolates, including the empty matrix in dimension zero. Choosing the isolated indices and deleting their rows and columns gives the **exact** convolution
\[
H_n=\sum_{u=0}^n\binom nu H_{n-u}^{(0)}.
\]
For a zero-isolate word with source size \(a\) and target size \(b\), the number of matrices is bounded by \(2^{ab}\sum_{\lambda\subseteq b^a}2^{-|\lambda|}\). The sum is a Gaussian binomial coefficient at \(1/2\), bounded above by \(Q^{-2}\) using its finite product expression. Consequently
\[
H_r^{(0)}\le (r+1)Q^{-2}2^{\lfloor r^2/4\rfloor}
\]
for every nonnegative integer \(r\). The convolution therefore gives
\[
\#\{B:I(B)\ne\varnothing\}\le Q^{-2}\sum_{u=1}^n\binom nu(n-u+1)2^{\lfloor(n-u)^2/4\rfloor}=o(2^{\lfloor n^2/4\rfloor}).
\]
For \(u\le n/2\), the ratio of the exponentials to \(2^{\lfloor n^2/4\rfloor}\) is at most \(2^{-un/4+O(1)}\), so the sum is bounded by a geometric series of scale \(O(n^2 2^{-n/4})\). For \(u>n/2\), the entire sum is bounded by \(2^n(n+1)2^{-3n^2/16+O(1)}\). Taking the canonical ordered split of early sources and late sinks produces at least \(2^{\lfloor n^2/4\rfloor}\) admissible matrices (some may have isolates), so the isolate probability tends to zero.

**4. Dominated convergence and independence.** Let \(H_n^{(0)}(j,\lambda)\) be the count with no isolates, given imbalance and diagram. The preceding exact support description gives
\[
0\le H_{2m}^{(0)}(j,\lambda)/2^{m^2}\le2^{-j^2-|\lambda|},
\quad 0\le H_{2m+1}^{(0)}(j,\lambda)/2^{m(m+1)}\le2^{j-j^2-|\lambda|}.
\]
Both bounding sums converge because \(\sum_{\lambda\in\mathcal P}2^{-|\lambda|}=Q^{-1}\), Euler's partition product. Pointwise convergence follows from Step 2. Dominated convergence on the countable set \(\mathbb Z\times\mathcal P\) gives
\[
H_{2m}^{(0)}/2^{m^2}\to Z_0/Q,\qquad H_{2m+1}^{(0)}/2^{m(m+1)}\to Z_1/Q.
\]
Step 3 makes isolates negligible, so these are also the total normalizers. Dividing the stratum limits by the normalizers yields the two stated product laws. Dominated convergence applied to normalized probability masses (or Scheffé's lemma on a countable space) gives total-variation convergence. Summing over diagrams of size \(k\) yields the partition-number marginal.

## Verification
Run \(`python3 verify.py`\) from this package to check the Boolean square-zero condition by direct edge enumeration for dimensions \(1\) through \(6\), compare every total against the independent \(q=2\) Stirling recurrence, and cross-check the canonical Ferrers-diagram encoding. This finite computation is independent evidence for the combinatorial setup, not proof of the infinite limit. The proof of the infinite limit is Steps 1–4 above. Known finite totals for dimensions \(1\) to \(6\) are \(1,2,6,26,158,1330\).

## Relationship to prior work
Huang and Lyu (2018, primary MSC 15A36) study the extremal number of nonzero entries in binary matrices with zero trace whose squares are binary. Their main theorems classify extremizers in that larger class; the present statement instead concerns the full random law of the strict-upper-triangular square-zero subfamily. Gusev (2023) treats semiring identities of reflexive upper-triangular Boolean matrices, not the nilpotent-radical support-shape law. Bevan, Cheon and Kitaev (2023 preprint; 2024 revised text, Section 2, Propositions 4–5) derive the exact count and generating functions for naturally labelled height-at-most-two posets, including enumeration by the number of minimal elements, but do not state the asymptotic *joint Ferrers-shape and imbalance law*. OEIS A135922 already records the total counts and theta-function asymptotic constants, credited here; those totals alone do not determine the conditional limit shape. The claim is specifically the new full partition-valued law and its asymptotic independence from the source-size defect, not a new enumeration of the total.

## Limitations
No assertion about unrestricted (nontriangular) square-zero Boolean matrices or nonzero square of ordinary binary matrices. Exact normalizers are known from previous work; no novelty is claimed for their limits. The result concerns the fixed coordinate order and two separate parity subsequences. Whether an equivalent distribution is implicit in older work on random naturally labelled posets or Gaussian-binomial Boltzmann measures remains a publication-priority risk.

## References
1. Z. Huang and Z. Lyu, *0-1 matrices with zero trace whose squares are 0-1 matrices*, arXiv:1803.01293 (first public 2018-03-04), primary MSC 15A36, https://arxiv.org/abs/1803.01293.
2. S. V. Gusev, *Semiring identities of semigroups of reflexive relations and upper triangular boolean matrices*, arXiv:2301.11863 (first public 2023-01-27), https://arxiv.org/abs/2301.11863.
3. D. Bevan, G.-S. Cheon and S. Kitaev, *On naturally labelled posets and permutations avoiding 12-34*, arXiv:2311.08023 (first public 2023-11-14), Section 2, https://arxiv.org/html/2311.08023v2.
4. OEIS A135922, *Inverse binomial transform of A006116*, including pre-existing exact counts and Kotesovec's 2013 theta asymptotics, https://oeis.org/A135922.
