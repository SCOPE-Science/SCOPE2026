# Exact positional covariance of permutation cycles and records

## Finding

Let \(\pi\) be a uniformly distributed permutation of \(\{1,\ldots,n\}\), with \(n\ge2\). Let \(C_n\) denote the number of disjoint cycles in the usual functional cycle decomposition of \(\pi\), and let \(I_k=\mathbf1\{\pi(k)>\max_{i<k}\pi(i)\}\) indicate a strict left-to-right upper record at position \(k\), with \(I_1=1\). Write \(R_n=\sum_{k=1}^n I_k\). Then, for each integer \(1\le k\le n\),

\[
\operatorname{Cov}(C_n,I_k)=\frac{k-1}{k^2\binom nk}.
\]

In particular, every record indicator after the first is **strictly positively correlated** with the cycle count, although the latter and the record count have only the same *marginal distribution*, not the same value on a common permutation. Their exact covariance is

\[
\operatorname{Cov}(C_n,R_n)=\sum_{k=2}^n\frac{k-1}{k^2\binom nk}>0.
\]

As \(n\to\infty\),

\[
\operatorname{Cov}(C_n,R_n)=\frac1n+\frac1{2n^2}+O(n^{-3}),\qquad
\operatorname{Corr}(C_n,R_n)\sim\frac1{n\log n}.
\]

The last-position contribution alone is \((n-1)/n^2\); its ratio to the entire covariance tends to one.

## Assumptions and scope

A permutation is viewed simultaneously as a bijection \(i\mapsto\pi(i)\) (to count functional cycles) and as its one-line word \((\pi(1),\ldots,\pi(n))\) (to count records). These statistics are evaluated on the **same** uniformly sampled permutation. All probabilities and covariances refer to the uniform law on \(S_n\). The exact kernel holds for every finite integer \(n\ge2\) and \(1\le k\le n\). The asymptotic statements concern \(n\to\infty\) under that same law. The first record is deterministic and has zero covariance.

Set \(H_s=\sum_{j=1}^s j^{-1}\) for integers \(s\ge1\), and \(H_0=0\); use \((n)_r=n(n-1)\cdots(n-r+1)\) for \(1\le r\le n\).

## Proof

**1. Partial permutation decomposition.** Reveal the values \(\pi(1),\ldots,\pi(k)\). As a directed partial permutation graph, the \(k\) known arrows form a disjoint union of closed cycles and directed open paths, including isolated vertices. Write \(Z_k\) for the number of its closed cycles, each supported wholly in \(\{1,\ldots,k\}\). There are exactly \(n-k\) open path components: each of the \(k\) arrows either closes one cycle or merges open path components, and a direct in-/out-degree count gives the number of free tails and free heads. Each of the \((n-k)!\) uniform completions connects these components through a bijection between their free ends. After contracting each open path, these completions are the uniform permutations of \(n-k\) components. Hence

\[
\mathbb E[C_n\mid\pi(1),\ldots,\pi(k)]=Z_k+H_{n-k}.
\]

In particular \(\operatorname{Cov}(C_n,I_k)=\operatorname{Cov}(Z_k,I_k)\), since \(I_k\) is determined by the revealed values. It also follows that \(\mathbb E[Z_k]=H_n-H_{n-k}\). Independently, linearity over specified cycles provides a combinatorial identity:

\[
\mathbb E[Z_k]=\sum_{r=1}^k\frac{\binom kr(r-1)!}{(n)_r}
=\sum_{r=1}^k\frac{\binom kr}{r\binom nr}.
\]

Here a specified directed cycle of length \(r\) occurs with probability \(1/(n)_r\), because fixing \(r\) arrows leaves \((n-r)!\) equally likely completions.

**2. Mixed cycle-record moment.** As is standard for records in a uniform permutation, \(\Pr(I_k=1)=1/k\). Consider a specified closed cycle of length \(r\) whose vertices lie in \(\{1,\ldots,k\}\). If its vertices lie wholly in \(\{1,\ldots,k-1\}\), its \(r\) predetermined images are also smaller than \(k\). Among the other \(k-r\) first-\(k\) image values, the largest image of all the first \(k\) positions necessarily occurs: only \(k-r-1\) unused values smaller than \(k\) remain. These \(k-r\) unforced positions are exchangeable, so the probability of a record at \(k\), conditional on that specified cycle, is \(1/(k-r)\).

If the specified cycle contains \(k\) and has length \(r\ge2\), it forces a prior position to map to \(k\), while \(\pi(k)\le k\); a strict record at \(k\) is impossible. If the specified cycle is the fixed point \((k)\), a record at \(k\) occurs exactly when every other first-\(k\) image lies in \(\{1,\ldots,k-1\}\). The joint probability of this event and \(\pi(k)=k\) equals \(1/(k\binom nk)\). Combining these cases,

\[
\begin{aligned}
\mathbb E[Z_k I_k]
&=\sum_{r=1}^{k-1}\frac{\binom{k-1}r(r-1)!}{(n)_r(k-r)}
 +\frac1{k\binom nk}\\
&=\frac1k\sum_{r=1}^{k-1}\frac{\binom kr}{r\binom nr}
 +\frac1{k\binom nk},
\end{aligned}
\]

using \(\binom{k-1}r/(k-r)=\binom kr/k\). Subtract \(\mathbb E[Z_k]\mathbb E[I_k]\), including the omitted \(r=k\) term of the preceding cycle sum. This gives

\[
\operatorname{Cov}(C_n,I_k)
=\frac1{k\binom nk}-\frac1{k^2\binom nk}
=\frac{k-1}{k^2\binom nk}.
\]

For \(k=1\), both sides vanish. For \(k=n\), the formula gives \((n-1)/n^2\), consistent with the event that the terminal entry is \(n\).

**3. Summation and asymptotics.** Sum the covariance over all \(k\). Its terms are positive for \(k\ge2\). The summands at \(k=n\), \(k=n-1\), and \(k=2\) are respectively

\[
\frac{n-1}{n^2}=\frac1n-\frac1{n^2},\quad
\frac{n-2}{n(n-1)^2}=\frac1{n^2}+O(n^{-4}),\quad
\frac1{2n(n-1)}=\frac1{2n^2}+O(n^{-3}).
\]

The terms at \(k=3\) and \(k=n-2\) are \(O(n^{-3})\); the term at \(k=n-3\) is \(O(n^{-4})\). For \(4\le k\le n-4\), binomial unimodality gives \(\binom nk\ge\binom n4\), so these remaining terms are at most \(H_n/\binom n4=O((\log n)/n^4)=O(n^{-3})\). For small \(n\) with an empty index range the assertion is vacuous. Therefore the covariance has the claimed two-term expansion, and the final-position contribution asymptotically accounts for all of it.

The classical cycle/record equidistribution and record-indicator independence give

\[
\operatorname{Var}(C_n)=\operatorname{Var}(R_n)
=\sum_{k=1}^n\left(\frac1k-\frac1{k^2}\right)
=H_n-H_n^{(2)},\quad H_n^{(2)}=\sum_{k=1}^n k^{-2}.
\]

Since this variance is \(\log n+O(1)\), dividing the covariance by the common variance proves the correlation asymptotic.

## Verification

The accompanying standalone `verify.py` exhaustively enumerates all \(n!\) permutations for each \(1\le n\le9\), counts functional cycles and one-line strict upper records on the *same* permutation, and evaluates all covariances with exact rational arithmetic. The observed values match the theorem, including the total mixed covariance. It independently checks the harmonic/binomial identity used in the proof for every \(1\le k\le n\le200\). Run `python3 verify.py` in a directory containing that file. Successful execution prints `PASS exact enumeration n<=9, all n<=200 binomial-harmonic identities`. These are finite checks; they do not establish the infinite all-\(n\) statements, which follow from the proof above.

## Relationship to prior work

Cycles and upper records are classical equidistributed Stirling statistics, and Foata's transformation provides a bijective explanation. Equidistribution is not joint independence, nor does it identify their covariance **on one fixed permutation**. Mahmoud's *Sorting: A Distribution Theory* explicitly distinguishes the two values on the same permutation, establishing marginal equality rather than the present positional joint formula. Maples, Nikeghbali and Zeindler study cycle counts under generalized Ewens weights, without a simultaneous one-line record kernel. Jin's Euler–Stirling work addresses generating functions for other joint permutation statistics and cycle/record equidistribution, not the original map's mixed indicator covariance. Baril and Petrossian study descents and record-maxima equivalence classes, not the present cycle covariance. Dubach studies record structure of conjugation-invariant permutations and conditioning on cycle type, a related but different level of description. Hamaker and Rhoades develop a broad conditional moment framework for **partial permutation** indicators grouped by cycle-path type, including the same partial-map objects used here. Their general moment theorem gives structural polynomiality under conditioning on cycle type but does not evaluate this all-position original-cycle/strict-prefix-record covariance or its asymptotic final-position localization. Their Section 6.2 explicitly frames joint-distribution analysis of regular permutation statistics as a further problem. The exact positional formula and terminal localization are the statements evaluated here, not the known marginal distributions.

## Limitations

This is an exact result only for uniform permutations, not Ewens-weighted, Mallows-weighted, or nonuniform laws. It concerns disjoint cycles of the **original** bijection and records in that same permutation's one-line notation; applying a Foata bijection first changes the joint distribution. The nonzero finite covariance tends to zero even as both marginal variances grow logarithmically. The analytic proof is self-contained; independent scientific audit and exhaustive historical-priority verification have not been performed. Earlier general bivariate generating functions might implicitly imply parts of the statement.

## References

1. Maples, K., Nikeghbali, A., and Zeindler, D., *On the number of cycles in a random permutation*, arXiv:1203.4132, first posted 2012-03-19, https://arxiv.org/abs/1203.4132.
2. Mahmoud, H. M., *Sorting: A Distribution Theory*, Wiley, 2000, §1.10, on the distinction between cycles and records in the same permutation.
3. Jin, E. Y., *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789, https://arxiv.org/abs/2210.08789.
4. Baril, J.-L. and Petrossian, S., *Equivalence classes of permutations modulo descents and left-to-right maxima*, https://jl.baril.u-bourgogne.fr/equivaldescentrevue.pdf.
5. Dubach, V., *A geometric approach to conjugation-invariant random permutations*, arXiv:2402.10116, for related conditioned-cycle record processes.
6. Hamaker, Z. and Rhoades, B., *Moments of permutation statistics by cycle type*, arXiv:2503.17556, particularly Theorem 1.1 and §6.2, https://arxiv.org/abs/2503.17556.
