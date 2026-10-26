# Conditional reversal of singleton–tagged-block covariance in uniform set partitions

## Finding
Let \(\Pi_n\) be uniform among all set partitions of \([n]\), \(n\ge4\). Let \(L\) be the cardinality of the block containing the tagged element \(1\), and \(T\) the total number of singleton blocks. Let \(K\) be the number of blocks. The unconditional covariance is **strictly negative**, while both conditional covariances at the two natural nondegenerate block-count extremes are **strictly positive**:
\[
\operatorname{Cov}(L,T)<0,\qquad
\operatorname{Cov}(L,T\mid K=2)>0,\qquad
\operatorname{Cov}(L,T\mid K=n-2)>0.
\]
More precisely, if \(B_n\) denotes the Bell number and \(S(n,k)\) the Stirling number of the second kind, the three covariances equal
\[
\frac{n-1}{B_n^2}\big((n-2)B_{n-2}B_n-nB_{n-1}^2\big),
\]
\[
\frac{(n-1)\big((n-4)2^{n-2}+2\big)}{(2^{n-1}-1)^2},
\]
and
\[
\frac{2\binom n3\,3\binom n4}{n\big(\binom n3+3\binom n4\big)^2},
\]
respectively. For all admissible \(1\le k\le n\), the exact conditional covariance is
\[
\operatorname{Cov}(L,T\mid K=k)=\frac{n-1}{S(n,k)^2}\Big[(n-2)S(n-2,k-1)S(n,k)-nS(n-1,k-1)S(n-1,k)\Big].
\]
The displayed global formula is not claimed to have a particular sign at every intermediate \(k\).

## Assumptions and scope
Set partitions are unlabeled collections of nonempty blocks of labeled elements. All \(B_n\) possibilities have equal probabilities, and conditioning on \(K=k\) yields the uniform law over the \(S(n,k)\) possibilities. Empty-set conventions are \(B_0=S(0,0)=1\); \(S(a,b)=0\) outside \(0\le b\le a\). The assertion about strictly positive conditional covariance holds for all integers \(n\ge4\). The unconditional formula/negative sign applies for \(n\ge2\). No universal positive-sign assertion for every fixed \(k\) is made.

## Proof
First fix \(k\). By symmetry and removal of an isolated singleton, \(\mathbb E[T\mid K=k]=n S(n-1,k-1)/S(n,k)\). A given distinct label shares the tagged block with element 1 in \(S(n-1,k)\) out of \(S(n,k)\) partitions, so
\[
\mathbb E[L\mid K=k]=1+(n-1)S(n-1,k)/S(n,k).
\]
Writing \(L=1+\sum_{i=2}^n\mathbf 1_{\{i\sim 1\}}\) and \(T=\sum_{j=1}^n\mathbf 1_{\{j\text{ singleton}\}}\), the diagonal terms and terms with \(j=1\) vanish in the product \((L-1)T\). For distinct \(1,i,j\), the event that \(j\) is singleton and \(i\) belongs to the tagged block is counted by merging \(i\) with 1 and removing \(j\), leaving \(S(n-2,k-1)\) partitions. Hence
\[
\mathbb E[LT\mid K=k]=\frac{n S(n-1,k-1)+(n-1)(n-2)S(n-2,k-1)}{S(n,k)}.
\]
Subtracting the product of the first two expectations gives the stated universal conditional formula.

For \(k=2\), use \(S(n,2)=2^{n-1}-1\), \(S(n-1,1)=1\), \(S(n-2,1)=1\), and \(S(n-1,2)=2^{n-2}-1\). Direct substitution yields the displayed two-block formula, strictly positive when \(n\ge4\).

For \(k=n-2\), every partition comprises either one triple and \(n-3\) singleton blocks (\(A=\binom n3\) possibilities), or two disjoint pairs and \(n-4\) singleton blocks (\(D=3\binom n4\) possibilities). In the first class \(T=n-3\) and the conditional mean tagged-block size is \(1+6/n\); in the second \(T=n-4\) and the mean tagged-block size is \(1+4/n\). The law of total covariance for this binary shape indicator gives
\[
\operatorname{Cov}(L,T\mid K=n-2)=\frac{AD}{(A+D)^2}\cdot\frac2n>0.
\]
The two classes have positive counts for every \(n\ge4\).

Without conditioning on \(K\), the same event counts use Bell numbers rather than Stirling numbers. Therefore
\[
\mathbb E[T]=nB_{n-1}/B_n,\qquad
\mathbb E[L]=1+(n-1)B_{n-1}/B_n,
\]
\[
\mathbb E[LT]=nB_{n-1}/B_n+(n-1)(n-2)B_{n-2}/B_n.
\]
These yield the stated unconditional formula. The known log-concavity theorem for normalized Bell numbers \(B_j/j!\) (Asai–Kubo–Kuo, cited below) gives
\[
B_nB_{n-2}\le\frac{n}{n-1}B_{n-1}^2 \quad(n\ge2).
\]
Consequently
\[
(n-2)B_{n-2}B_n-nB_{n-1}^2
\le-\frac{n}{n-1}B_{n-1}^2<0.
\]
This proves the unconditional sign strictly. The sign reversal follows.

## Verification
The accompanying dependency-free `verify.py` enumerates all set partitions of \([n]\), for \(2\le n\le8\), and compares their exact rational covariances with both analytic formulas. It also checks the two extreme-stratum expressions and the Bell inequality through \(n=99\). A successful run prints `PASS 621 exact assertions; exhaustive set partitions n=2..8; formulas/signs to n=99`. These finite checks supplement, but do not replace, the proof for all \(n\).

## Relationship to prior work
Asai, Kubo, and Kuo proved log-concavity of normalized Bell numbers, supplying the inequality used in the negative unconditional sign; this inequality is not new. Gnedin and Pitman set out the more general exchangeable random-partition and Stirling-triangle framework, including fixed-block uniform partitions. Neither inspected source states the paired strict sign reversal for a tagged block's size and the total singleton count. The contribution claimed here is specifically the simultaneous sign-reversal classification at the two natural nondegenerate fixed-block extremes together with its exact joint moment identity; no priority claim is made for the established Bell-number or Stirling-number identities.

## Limitations
No sign classification is proved for intermediate conditioned block counts \(3\le k\le n-3\). The general identity alone is not a proof of such a sign. The proof relies on a published normalized Bell-number log-concavity theorem. Earlier broad formulas for random partitions might implicitly cover these conditional covariance statements; historical priority has not been independently confirmed. No distribution-free or nonuniform-partition assertion is made.

## References
- N. Asai, I. Kubo, and H.-H. Kuo, *Bell numbers, log-concavity, and log-convexity*, arXiv:math/0104137 (first posted 2001-04-12), Theorem 1.
- A. Gnedin and J. Pitman, *Exchangeable Gibbs partitions and Stirling triangles*, arXiv:math/0412494 (first posted 2004-12-25), Sections 1–4.
