# Diagonal forward–inverse record covariance for uniform permutations

## Finding
Let \(\pi\) be a uniform permutation of \(\{1,\ldots,n\}\), where \(n\ge1\). Let \(A_i\) mark an upper left-to-right record at position \(i\) in \(\pi\), and let \(B_j\) mark an upper left-to-right record at position \(j\) in the inverse word \(\pi^{-1}\). For every \(1\le i,j\le n\),
\[
\operatorname{Cov}(A_i,B_j)=\mathbf1_{\{i=j\}}\frac{i-1}{i^2\binom ni}.
\]
In particular the two Bernoulli events are independent whenever \(i\ne j\); matched indices \(i=j\ge2\) have strictly positive covariance. The entire cross-covariance matrix is diagonal of rank \(n-1\), including the deterministic first record.

For the total upper-record counts \(R=\sum_{i=1}^n A_i\) and \(R'=\sum_{j=1}^n B_j\),
\[
\operatorname{Cov}(R,R')=\sum_{i=2}^n\frac{i-1}{i^2\binom ni}
=\frac1n+\frac1{2n^2}+O(n^{-3})\quad(n\to\infty).
\]
Since each marginal record-count variance is \(H_n-H_n^{(2)}\),
\[
\operatorname{Corr}(R,R')\sim\frac1{n\log n}.
\]
For arbitrary deterministic real weights \(a_i,b_j\), the weighted cross-covariance is exactly \(\sum_{i=2}^n a_i b_i(i-1)/(i^2\binom ni)\).

## Assumptions and scope
All permutations have probability \(1/n!\); record comparisons are strict (there are no ties). Here
\[
 A_i=\mathbf1\{\pi(i)=\max_{1\le k\le i}\pi(k)\},\qquad
 B_j=\mathbf1\{\pi^{-1}(j)=\max_{1\le k\le j}\pi^{-1}(k)\}.
\]
Thus \(B_j\) equivalently indicates that value \(j\) occurs in a right-to-left minimum position of \(\pi\). The indices \(i,j\) respectively refer to a position of the original word and a value of the original word; they must not be conflated with two original-word position indices. \(H_n=\sum_{k=1}^n 1/k\) and \(H_n^{(2)}=\sum_{k=1}^n 1/k^2\).

## Proof
The initial relative ranks in a uniformly random permutation are independent, each uniform on its range. Applying this to the permutation and its inverse gives \(\mathbb E A_i=1/i\), \(\mathbb E B_j=1/j\), and \(\operatorname{Var}(R)=\operatorname{Var}(R')=H_n-H_n^{(2)}\).

**Case \(i<j\).** Condition on the unordered set \(S\) of values occurring in the first \(i\) positions. Conditional on \(S\), their order is uniform and independent of the order on the complementary suffix. Thus \(\Pr(A_i=1\mid S)=1/i\). The event \(B_j=1\) implies value \(j\) is in the suffix: if value \(j\) were in the first \(i<j\) positions, at least one smaller value would lie outside that prefix and hence to its right. Therefore \(B_j\), given \(S\), is a function of the suffix order (or identically false), independent of \(A_i\). Taking expectations yields \(\mathbb E[A_iB_j]=\mathbb E[B_j]/i=1/(ij)\).

**Case \(i>j\).** Condition instead on the unordered set \(P\) of positions occupied by values \(1,\ldots,j\). Independently assign the small values to \(P\) and the larger values to its complement, in uniformly random orders. The event \(B_j=1\) depends solely on the former assignment. Because \(i>j\), at least one value larger than \(j\) must appear among the first \(i\) positions, so \(A_i=1\) depends solely on the latter assignment (and on the fixed position set \(P\)). Conditional independence follows. As \(\Pr(B_j=1\mid P)=1/j\), taking expectations yields \(\mathbb E[A_iB_j]=1/(ij)\).

**Case \(i=j\).** Again condition on the unordered prefix-value set \(S\) of cardinality \(i\). The conditional chance of \(A_i\) is always \(1/i\). If \(S\ne\{1,\ldots,i\}\), then either \(i\in S\), in which case \(B_i\) is impossible because some smaller value occurs to its right, or \(i\notin S\), in which case \(B_i\) depends solely on the independently ordered suffix. Hence conditional covariance is zero in both cases. On the exceptional event \(S=\{1,\ldots,i\}\), the indicators coincide: both are one exactly when \(\pi(i)=i\). Their conditional covariance is \(1/i-1/i^2=(i-1)/i^2\). A uniformly random prefix-value set is \(\{1,\ldots,i\}\) with probability \(1/\binom ni\). The conditional expectation of \(A_i\) is the constant \(1/i\), so the law of total covariance gives precisely \((i-1)/(i^2\binom ni)\).

**Totals and asymptotics.** Summing diagonal entries gives the exact formula. For \(n\to\infty\), the \(i=n\) summand equals \(1/n-1/n^2\), the \(i=n-1\) summand equals \(1/n^2+O(n^{-4})\), and the \(i=2\) summand equals \(1/(2n^2)+O(n^{-3})\). The other summands sum to \(O(n^{-3})\): the \(i=3,n-3,n-2\) terms are individually \(O(n^{-3})\); for \(4\le i\le n-4\) the lower bound \(\binom ni\ge\binom n4\) holds for all sufficiently large \(n\), yielding a bound \(O((\log n)/n^4)\). Thus the displayed two-term asymptotic holds. Independent record indicators yield the marginal variance stated above; since \(H_n-H_n^{(2)}\sim\log n\), the correlation follows. Linearity proves the weighted identity.

## Verification
The standalone standard-library program `verify.py` enumerates all permutations for \(1\le n\le8\), computes both indicator vectors independently, and checks all \(204\) exact cross-covariance entries against the stated formula using rational arithmetic. It also checks total covariances and positivity in a separate exact binomial expression for \(2\le n\le100\). The enumeration checks a finite range; it is not used as a proof of the all-\(n\) statement. Reproduce with `python verify.py`.

## Relationship to prior work
Gnedin (2006) treats coherent random permutations with upper/lower record values and supplies a probabilistic framework for record statistics; Gnedin and Gorin (2012) examine record-dependent coherent measures. Neither of the inspected statements gives the position-by-inverse-position cross-covariance matrix above. Jin (2022) gives bivariate and multivariate generating functions for Euler–Stirling statistics, including left-to-right maxima and **inverse descents**, but the inspected main theorems do not feature the full positional upper-record vector of both a permutation and its inverse. Importantly, the total number of inverse upper records also equals the number of original-word right-to-left minima. Counting distributions for that pair, if known, do not by themselves determine the full position-versus-value covariance matrix; the theorem resolves that finer question. Prior record-indicator marginal independence is classical and not claimed as new.

## Limitations
The theorem is restricted to uniform permutations, strict records, and pairwise covariance/independence; it does not assert independence of the two full record-indicator vectors or their joint generating function. The asymptotic applies to unweighted total counts. Equivalent older descriptions of two-directional record indicator coupling might exist; exact historical priority requires an independent literature audit.

## References
- A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first posted 2006-11-17. https://arxiv.org/abs/math/0611538
- A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680, first posted 2012-02-16. https://arxiv.org/abs/1202.3680
- E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789, first posted 2022-10-17. https://arxiv.org/abs/2210.08789

