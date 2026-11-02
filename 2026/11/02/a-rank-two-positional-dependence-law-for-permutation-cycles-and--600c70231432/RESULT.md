# A rank-two positional dependence law for permutation cycles and consecutive triples

## Finding

Let \(\Pi_n\) be a uniformly sampled permutation of \(\{1,\ldots,n\}\), \(n\ge3\), and let \(K_n\) be its number of disjoint cycles (including fixed points). For \(1\le i\le n-2\), write \(A_{i,\sigma}\) for the event that the three entries at positions \(i,i+1,i+2\) have one-line rank pattern \(\sigma\in S_3\). For instance, \(132\) means the middle entry is largest and the first entry is smallest.

Put \(D_n=n(n-1)(n-2)\). The six exact conditional cycle-count deviations are

\[
\mathbb E[K_n\mid A_{i,\sigma}]-\mathbb E[K_n]
=\frac{b_\sigma(n,i)}{D_n},
\qquad \mathbb E[K_n]=H_n=\sum_{j=1}^n\frac1j,
\]

where the complete table is

| Pattern \(\sigma\) | Numerator \(b_\sigma(n,i)\) |
|:--|--:|
| \(123\) | \(3n-2\) |
| \(132\) | \(9n-14-12i\) |
| \(213\) | \(12i-3n-2\) |
| \(231\) | \(12i-9n+10\) |
| \(312\) | \(3n-2-12i\) |
| \(321\) | \(10-3n\) |

Equivalently, \(\operatorname{Cov}(K_n,\mathbf1_{A_{i,\sigma}})=b_\sigma(n,i)/(6D_n)\), since every triple pattern has probability \(1/6\). For \(n\ge4\), the matrix with these six pattern rows and \(n-2\) position columns has rank exactly two; for \(n=3\), it has rank one. No entry of any such covariance matrix is zero.

The position-resolved result distinguishes patterns invisible to descent-set statistics. In particular, although \(132\) and \(231\) both specify a peak, their covariance signs vary oppositely with position. For every \(n\ge5\), each of the four nonmonotone pattern profiles changes sign between the first and last window. Nevertheless, the *combined* peak event has the same strictly negative covariance at every position:

\[
\operatorname{Cov}\!\left(K_n,\mathbf1_{A_{i,132}\cup A_{i,231}}\right)
= -\frac{2}{3D_n}.
\]

The analogous valley covariance for \(213\cup312\) is identical. The aggregate peak-count covariance is \(-2/[3n(n-1)]\).

## Assumptions and scope

All probabilities refer to the uniform law on the full symmetric group \(S_n\); there is no conditioning on cycle type, parity, or the value of any entry. The one-line pattern at a *specified* consecutive triple is used, not a pattern in cycle notation, and not the total number of occurrences of an unrestricted pattern. Both the sample size \(n\) and the starting position \(i\) range over all integers in the stated domain.

## Proof

**1. Contracting three prescribed arrows.** Prescribe any three distinct image assignments \(\pi(p)=v_p\) at distinct positions \(p\), with distinct values \(v_p\). Regard each assignment as a directed arrow. The graph of the three forced arrows consists of disjoint directed paths, possibly together with closed directed cycles. Let \(F\) be the number of cycles already closed entirely by forced arrows. Contract each noncyclic directed path to a point and discard the closed cycles. There are exactly \(n-3\) remaining path components. Assigning all unforced images uniformly gives a uniformly random permutation of these components: each bijection of unassigned domain vertices to unused image vertices closes the component paths in precisely one way. Therefore

\[
\mathbb E[K_n\mid\text{the three prescribed arrows}]=F+H_{n-3},\qquad H_0=0.
\]

This includes the boundary case \(n=3\), when no unforced components remain.

**2. Count closed one-, two-, and three-cycles compatible with one triple pattern.** Let the positions be \(p_1=i\), \(p_2=i+1\), \(p_3=i+2\), and let \(r_t\in\{1,2,3\}\) be the rank of the image at \(p_t\) in pattern \(\sigma\). For a forced fixed point at \(p_t\), the number of compatible ordered assignments to the two other image positions is

\[
L_t=\binom{p_t-1}{r_t-1}\binom{n-p_t}{3-r_t}.
\]

Thus, summing the joint probabilities of the pattern and each possible one-cycle gives \(U_1/D_n\), where \(U_1=\sum_{t=1}^3L_t\).

For a forced transposition between two positions \(p_s<p_t\), one must have \(r_s>r_t\). If this order holds, write \(u\) for the remaining position. The number of allowable images at \(p_u\), according as \(r_u=1,2,3\), is respectively

\[
p_s-1,\qquad p_t-p_s-1,\qquad n-p_t.
\]

Let \(U_2\) be the sum of these counts over the three unordered position pairs satisfying the required rank order. Of the two directed three-cycles on the three positions, exactly one yields pattern \(231\) and one yields \(312\). Hence \(U_3=\mathbf1_{\{\sigma=231\text{ or }\sigma=312\}}\).

In each case, the prescribed arrows and the remaining assignments jointly have denominator \(D_n\). By linearity of expectation applied to the forced-cycle count, and since \(\Pr(A_{i,\sigma})=1/6\),

\[
\operatorname{Cov}(K_n,\mathbf1_{A_{i,\sigma}})
=\frac{U_1+U_2+U_3}{D_n}
-\frac16\left(\frac1n+\frac1{n-1}+\frac1{n-2}\right).
\]

The last term comes from \(H_n-H_{n-3}\). Directly expanding the three displayed finite sums gives exactly the six numerators in the table after multiplication by \(6D_n\). The standalone checker independently implements these finite counts and verifies their simplification, in addition to direct permutation enumeration.

**3. Rank, signs, and the peak cancellation.** Each numerator is affine in \(i\), so the six-by-\((n-2)\) matrix has rank at most two. For \(n\ge4\), row \(123\) is a nonzero constant while row \(132\) has nonzero slope, proving rank two; \(n=3\) has one column. Every numerator is congruent to \(1\) modulo \(3\), so none can vanish for integral \(n,i\). For \(n\ge5\), the numerator of each nonmonotone pattern has opposite signs at \(i=1\) and \(i=n-2\), as seen by substituting these endpoints in the table. Summing the \(132\) and \(231\) numerators gives \(-4\), and likewise for \(213\) and \(312\); this proves the position-independent peak and valley formulas. Summing over all \(n-2\) possible peak locations proves the aggregate expression.

## Verification

Run `python3 check.py` in the directory containing this file. Its independent all-permutation enumeration checks every one of the six pattern covariances at every valid position through \(n=8\), using exact rational arithmetic. Further exact integer checks cover the forced-cycle count identities, rank-profile relations, reversals, and symmetries through \(n=120\). The universal theorem follows from the symbolic argument above; finite tests do not substitute for that argument.

## Relationship to prior work

Gessel and Reutenauer (1993) enumerate permutations by cycle structure and descent set; the latter determines a peak but does not distinguish the one-line rank patterns \(132\) and \(231\) within that peak. Parviainen (2006, both cited works) develops cycles–pattern enumerators, primarily for vincular patterns or patterns read in standard cycle form. Gessel and Zhuang (2020, Section 7) give cycle-type-refined generating functions for *total* peak and descent counts. Those results provide significant broader context and cover weaker aggregated statistics, but none of the inspected portions supplies the full specified-position six-pattern covariance table or its orientation-sensitive affine profiles. The precise historical-priority comparison is limited by unavailable full text of the 1993 source; this work does not assert independently certified novelty.

## Limitations

The result is a first-moment dependence identity under uniform permutations, not a joint-law, conditional stochastic ordering, or independence theorem. For the four nonmonotone patterns, the exact sign transition is governed by the corresponding affine numerator; no claim is made for patterns of length four or more, arbitrary nonconsecutive positions, or nonuniform permutation laws. The source survey cannot establish exhaustive historical priority, and independent mathematical validation has not been performed.

## References

1. I. M. Gessel and C. Reutenauer, *Counting permutations with given cycle structure and descent set*, Journal of Combinatorial Theory, Series A 64 (1993), 189–215. DOI: https://doi.org/10.1016/0097-3165(93)90095-P.
2. R. Parviainen, *Permutations, cycles, and the pattern 2–13*, arXiv:math/0607793, first posted July 31, 2006; Electronic Journal of Combinatorics 13 (2006), R111. https://arxiv.org/abs/math/0607793.
3. R. Parviainen, *Cycles and patterns in permutations*, arXiv:math/0610616, first posted October 20, 2006. https://arxiv.org/abs/math/0610616.
4. I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, Advances in Mathematics 375 (2020), 107370; arXiv:2001.00654. https://arxiv.org/abs/2001.00654.
