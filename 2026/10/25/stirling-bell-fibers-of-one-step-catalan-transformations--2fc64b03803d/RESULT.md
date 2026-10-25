# Stirling–Bell fibers of one-step Catalan transformations

## Finding
Let \(n\geq1\), let \(\Phi:\mathrm{Styl}_n\twoheadrightarrow\mathrm{Cat}_n\) be the standard homomorphism sending the stylic generator \(i\) to the order-preserving, order-decreasing map \(\varepsilon_i\) that sends \(i\) to \(i-1\) and fixes all other points of \(\{0,\ldots,n\}\). For every subset \(S\subseteq\{1,\ldots,n\}\), define the *one-step transformation*
\[
 x\alpha_S=\begin{cases}x-1,&x\in S,\\x,&x\notin S.\end{cases}
\]
Let \(b(S)\) be the number of maximal nonempty intervals of consecutive integers constituting \(S\); set \(b(\varnothing)=0\). Write \(\left\{\begin{smallmatrix}b\\h\end{smallmatrix}\right\}\) for a Stirling number of the second kind and \(B_b\) for the corresponding Bell number, with \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=B_0=1\).

**Theorem (fiber stratification).** For every \(S\) and every integer \(h\geq0\), exactly
\[
 \left\{\begin{matrix}b(S)\\h\end{matrix}\right\}
\]
elements of \(\Phi^{-1}(\alpha_S)\) have an \(N\)-tableau with exactly \(h\) rows. In particular,
\[
 \left|\Phi^{-1}(\alpha_S)\right|=B_{b(S)}.
\]
The bijection is explicit: choose a set partition of the ordered set of starts of the maximal consecutive runs of \(S\), label its blocks in order of first appearance, and use those block labels as the tableau heights of the run starts (all other letters of \(S\) have tableau height one).

For \(0\leq b\leq\lceil n/2\rceil\), exactly \(\binom{n+1}{2b}\) one-step transformations have **exactly \(b\) support runs**, and each of those has fiber size \(B_b\) with the displayed Stirling row profile. Consequently the total number of stylic elements above all one-step transformations is
\[
 \sum_{b=0}^{\lceil n/2\rceil}\binom{n+1}{2b}B_b.
\]
(The run-number counts are disjoint; fiber sizes alone do not distinguish the empty-support case from the one-run case, since \(B_0=B_1=1\).)

**Idempotent subfamily.** \(\alpha_S\) is idempotent precisely when \(S\) has no adjacent integers. In this case \(b(S)=|S|\), so its fiber is canonically counted by partitions of \(S\), stratified by Stirling numbers. There are exactly \(\binom{n-k+1}{k}\) such idempotent one-step maps moving exactly \(k\) points.

## Assumptions and scope
Throughout, \(\mathrm{Styl}_n\) denotes the stylic monoid on the totally ordered alphabet \(\{1,\ldots,n\}\). The standard \(N\)-tableau normal form consists of a possibly empty sequence of nonempty rows \(R_1,\ldots,R_m\), indexed bottom-to-top, in which each row is a strictly increasing subset, \(R_{i+1}\subseteq R_i\), and \(\min R_1<\cdots<\min R_m\). Different \(N\)-tableaux represent different stylic elements. The row word is read from top row to bottom row, with each row in increasing order. Applying \(\varepsilon_i\) in that order computes \(\Phi\). The empty tableau represents the identity.

Every \(\alpha_S\) lies in \(\mathrm{Cat}_n\): its values are weakly increasing since \(x\alpha_S\leq x\leq(x+1)\alpha_S\), and it is order-decreasing. The theorem concerns exactly this \(2^n\)-element family, not arbitrary Catalan transformations.

## Proof
**1. Identify the bottom row.** Each generator \(\varepsilon_i\) decreases only a point currently equal to \(i\), and no composition of these maps increases any point. For a product word, a point \(i\in\{1,\ldots,n\}\) is fixed if and only if the letter \(i\) never occurs: before the first \(\varepsilon_i\), the point \(i\) is unchanged, and at the first occurrence it decreases permanently; generators \(\varepsilon_j\) with \(j\ne i\) cannot change it before then. Every letter in an \(N\)-tableau appears in its bottom row \(R_1\), by nesting. Hence, if \(\Phi(T)=\alpha_S\), necessarily \(R_1=S\). When \(S=\varnothing\) the only possible tableau is empty, giving the claimed \(h=0\) case.

**2. Characterize the allowable upper entries.** Suppose \(S\ne\varnothing\), and write \(D=\{s\in S:s-1\notin S\}\) for its set of run starts, in increasing order \(d_1<\cdots<d_b\). If an entry \(y\in R_2\) has \(y-1\in S\), then \(y\) occurs in an upper row before the bottom row in the row word. Its first upper occurrence decreases the original point \(y\) at least to \(y-1\); the bottom-row occurrence of \(y-1\) thereafter decreases it further if it has not already fallen below \(y-1\). Thus \(y\alpha_S\leq y-2\), contradicting the prescribed one-step value. Therefore \(R_2\subseteq D\). The strict row-minimum inequality excludes \(d_1\) from \(R_2\).

Conversely, suppose \(R_1=S\) and \(R_2\subseteq D\) (with any further nested rows satisfying the tableau axioms). Every upper-row letter is then a run start. If \(y\notin S\), no \(\varepsilon_y\) occurs, so \(y\) remains fixed. If \(y\in D\), at its first occurrence the point \(y\) drops to \(y-1\notin S\), and cannot fall further. If \(y\in S\setminus D\), it never occurs in an upper row; in the increasing bottom row, \(\varepsilon_{y-1}\), if present, precedes \(\varepsilon_y\), so the original \(y\) drops exactly once, at \(\varepsilon_y\). Hence every such tableau maps to \(\alpha_S\). The fiber is exactly the set of \(N\)-tableaux with bottom row \(S\) and all upper-row entries drawn from \(D\setminus\{d_1\}\).

**3. A canonical partition bijection.** For such a tableau let \(h_j\) be the number of rows containing run start \(d_j\). Nesting implies that \(d_j\) lies in precisely rows \(1,\ldots,h_j\). Every other letter of \(S\) lies only in row one. Consequently the tableau is completely reconstructed from \((h_1,\ldots,h_b)\), with \(h_1=1\). The strict row-minima condition is equivalent to the restricted-growth rule
\[
 1\leq h_j\leq 1+\max_{i<j}h_i\quad(2\leq j\leq b).
\]
Indeed, a violation skips a new row level at the first occurrence of \(d_j\), making the minima of two consecutive nonempty upper rows equal to \(d_j\). Conversely, under the rule, the first index with height at least \(r+1\) is strictly later than the first index with height at least \(r\); hence row minima strictly increase. Such restricted-growth strings are canonically equivalent to set partitions of \(\{d_1,\ldots,d_b\}\), with each number \(h_j\) naming the block of \(d_j\) in order of first appearance. The maximum height is exactly the number \(h\) of blocks. There are \(\left\{\begin{smallmatrix}b\\h\end{smallmatrix}\right\}\) such strings with maximum \(h\), and \(B_b\) in total.

**4. Count the supports and idempotents.** A subset with exactly \(b\) maximal consecutive runs is uniquely determined by the \(2b\) distinct endpoints of its runs chosen from the \(n+1\) gaps around the \(n\) positions. Thus their number is \(\binom{n+1}{2b}\), including the empty set for \(b=0\). Summing the fiber cardinalities yields the displayed aggregate formula. Finally, for \(y\in S\), applying \(\alpha_S\) twice sends \(y\) to \(y-2\) precisely when \(y-1\in S\); hence idempotence is equivalent to absence of consecutive members of \(S\). Choosing \(k\) nonadjacent positions on an \(n\)-chain gives \(\binom{n-k+1}{k}\) choices. This completes the proof.

## Verification
A standalone checker, `verification/check_fibers.py`, exhaustively enumerates all \(N\)-tableaux for \(1\leq n\leq8\) using nested subset rows with increasing minima, evaluates the quotient map by direct composition of the elementary \(\varepsilon_i\), and checks every one-step image's full row-count profile against independently generated Stirling numbers. At \(n=8\), it enumerates \(21{,}147\) distinct tableaux and checks all \(256\) one-step images. It separately checks the known total \(B_{n+1}\) and the binomial count of supports by run number. Run from the package root:

`python3 verification/check_fibers.py`

The checker prints `VERIFY_OK` on success. The proof above, not this finite check, establishes the theorem for every \(n\).

## Relationship to prior work
Abram and Reutenauer introduced \(\mathrm{Styl}_n\), proved the \(N\)-tableau normal form and its total cardinality \(B_{n+1}\) (arXiv:2106.06556). Volkov established the quotient to \(\mathrm{Cat}_n\) (arXiv:2206.09129). Stein's October 6, 2026 paper *From stylic monoid to Catalan monoid* (arXiv:2610.07983v1) proves that a unique full core determines each image; its Theorem 7.11 and Corollary 8.9 describe all fiber membership via that core. The present result **does not claim a new quotient or core classification**. It adds the exact Stirling row profile, Bell fiber size and run-count multiplicity on the intrinsic one-step subfamily. These numbers require identifying allowable upper letters and establishing a partition bijection; they are not stated in the inspected primary text.

## Limitations
The formulas apply only to transformations decreasing each moved point by exactly one. No claim is made about the complete distribution of fibers over all \(\mathrm{Cat}_n\), their global maximum, or general efficient counting of arbitrary fibers. The existing full-core theorem gives a stronger membership classification, and the present enumerative theorem depends on established tableau normal forms. An unindexed prior enumerative interpretation remains possible. Computational verification covers only \(n\leq8\); independent mathematical audit has not been performed.

## References
1. A. Abram and C. Reutenauer, *The Stylic Monoid*, arXiv:2106.06556 (2021), https://arxiv.org/abs/2106.06556 .
2. M. V. Volkov, *Identities of the stylic monoid*, arXiv:2206.09129 (2022), https://arxiv.org/abs/2206.09129 .
3. I. Stein, *From stylic monoid to Catalan monoid*, arXiv:2610.07983v1, first public October 6, 2026, https://arxiv.org/html/2610.07983v1 .
