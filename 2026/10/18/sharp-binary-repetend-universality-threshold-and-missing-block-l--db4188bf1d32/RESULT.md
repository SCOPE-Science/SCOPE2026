# Sharp binary-repetend universality threshold and missing-block law for reciprocal powers of three

## Finding

For an integer \(k\ge1\), let \(W_k\) be the cyclic binary repetend of \(1/3^k\), of length \(N_k=2\cdot3^{k-1}\). Let \(P_k(j)\) denote the number of distinct length-\(j\) binary words occurring in its infinite periodic continuation; occurrences may cross the repetend boundary. Put
\[
Q_k=3^k,\qquad m_k=\lfloor\log_2 N_k\rfloor,\qquad M_k=2^{m_k}.
\]
The number of absent words at the **critical** length \(m_k\) is exactly
\[
\boxed{2^{m_k}-P_k(m_k)
=\max\left\{0,\left\lfloor\frac{M_k-1}{3}\right\rfloor
-\left\lfloor\frac{Q_k-M_k}{3}\right\rfloor\right\}.}
\]
Every word of every length \(1\le j<m_k\) occurs. No length \(j>m_k\) contains all \(2^j\) binary words. Therefore the maximal universal word length
\[
J_k=\max\{j\ge1:P_k(j)=2^j\}
\]
satisfies \(J_1=1\), and for every \(k\ge2\),
\[
\boxed{J_k=\begin{cases}
m_k,&3^k\ge2^{m_k+1},\\
m_k-1,&3^k<2^{m_k+1}.
\end{cases}}
\]
The two possibilities both occur infinitely often. More precisely, the natural density, among positive indices \(k\), of the indices with \(J_k=m_k\) exists and is \(\log_2(3/2)\); the complementary density is \(\log_2(4/3)\).

## Assumptions and scope

The radix is two, the numerator is one, the denominator is an integer power \(3^k\) with \(k\ge1\), and binary words are counted cyclically across the endpoint of a period. A word is considered present if it occurs at least once, not with a specified frequency. The number \(m_k\) is the integer logarithm of the minimal period length, not the logarithm of the denominator. All floor functions act on ordinary real quotients and all index densities are ordinary natural densities in the parameter \(k\).

## Proof

**1. The remainders exhaust the units.** The integer \(2\) has order \(2\) modulo \(3\), and
\[
\nu_3\bigl(2^{2\cdot3^t}-1\bigr)=t+1\qquad(t\ge0)
\]
by the standard lifting-the-exponent identity applied to \(4^{3^t}-1\). Thus \(\operatorname{ord}_{3^k}(2)=2\cdot3^{k-1}=\varphi(3^k)\). Starting the binary long division of \(1/Q_k\) with remainder one, its successive nonzero remainders therefore run exactly once through all \(1\le r<Q_k\) with \(3\nmid r\).

**2. Words are bins of unit remainders.** The next \(j\) bits after a remainder \(r\) have the numerical value \(\lfloor 2^j r/Q_k\rfloor\). Consequently,
\[
P_k(j)=\#\left\{\left\lfloor\frac{2^j r}{Q_k}\right\rfloor:
1\le r<Q_k,\ 3\nmid r\right\}.
\]
This equality also counts boundary-crossing words because the remainder cycle is periodic.

**3. Only one critical length can fail.** Since \(2^{m_k}\le N_k<2^{m_k+1}\), multiplication by \(3/2\) gives
\[
\frac32\le\frac{Q_k}{M_k}<3.
\]
For \(j\le m_k-1\), every interval
\[
\left[\frac{sQ_k}{2^j},\frac{(s+1)Q_k}{2^j}\right),
\qquad0\le s<2^j,
\]
has length at least three. It contains an integer not divisible by three, hence every word is present. Conversely, for \(j\ge m_k+1\), the number \(2^j\) of possible words exceeds the \(N_k\) cyclic starting positions, so complete occurrence is impossible.

**4. Exact critical deficit.** Write \(Q=Q_k\), \(M=M_k\). Each of the \(M\) bins at length \(m_k\) has width \(Q/M\in[3/2,3)\). If \(Q\ge2M\), every bin has at least two consecutive integers, at least one of which is not divisible by three. Thus none is missing.

Suppose \(Q<2M\). The bin width is in \([3/2,2)\), and every bin contains one or two integers. A bin is missing precisely if its unique integer is an interior multiple \(r=3t\) of three. Let \(u\) be the remainder of \(Mr\) modulo \(Q\), chosen with \(0<u<Q\). The adjacent integers \(r-1\) and \(r+1\) are in other bins exactly when
\[
Q-M<u<M.
\]
Indeed, the position of \(r\) within its bin is \(u/Q\), while the positions of its neighbors differ by \(M/Q\). The endpoints cannot equal either boundary: \(u=M\) would require \(r\equiv1\pmod Q\), while \(u=Q-M\) would require \(r\equiv-1\pmod Q\), neither possible for \(3\mid r\). The map \(r\mapsto Mr\pmod Q\) permutes the nonzero multiples of three modulo \(Q\), because \(\gcd(M,Q)=1\). Therefore the number of missing bins is
\[
\#\{u:3\mid u,\ Q-M<u<M\}
=\left\lfloor\frac{M-1}{3}\right\rfloor
-\left\lfloor\frac{Q-M}{3}\right\rfloor.
\]
Combining both width regimes proves the asserted nonnegative-part formula, including \(k=1\).

**5. Exact phase and its density.** The case \(k=1\) gives \(Q=3\), \(M=2\), and zero missing bins. For \(k\ge2\), one has \(m_k\ge2\), so \(2M\) is divisible by eight. Since \(Q=3^k\equiv1\) or \(3\pmod8\), the positive integer \(2M-Q\), whenever positive, is at least five. The open interval \((Q-M,M)\) then contains a multiple of three, and its critical deficit is strictly positive. Thus \(J_k=m_k\) if and only if \(Q\ge2M\), proving the phase formula.

Finally, set \(\theta_k=\{\log_2 N_k\}\). The condition \(Q_k\ge2M_k\) is exactly \(\theta_k\ge\log_2(4/3)\). Since
\[
\theta_k=\{(k-1)\log_2 3\},
\]
and \(\log_2 3\) is irrational, elementary equidistribution of an irrational rotation shows that the index sets in the two intervals have densities \(1-\log_2(4/3)=\log_2(3/2)\) and \(\log_2(4/3)\). This establishes both infinite occurrence and the claimed proportions.

## Verification

The companion `verify.py` performs exact integer arithmetic. It independently generates the binary repetend by long division, checks every cyclic word set against the unit-remainder bin construction for each \(1\le j\le m_k+1\) and \(1\le k\le9\), and checks the missing-word counts and full-complexity thresholds. It also checks the exact phase-condition algebra for \(2\le k\le100\). The executed checks examined 45,390 distinct-word memberships and 99 phase comparisons without mismatch. The infinite statements are proved above; finite calculations are consistency checks, not substitutes for the proof.

The first critical deficits at indices \(k=1,2,3,4,5,6,7,8,9\) are respectively \(0,0,2,0,4,0,0,544,0\).

## Relationship to prior work

López and Stoll studied binary repetends of \(1/3^k\) in their 2012 article and proved eventual full complexity at every fixed word length. Their later article, publicly available as arXiv:2105.06513 in 2021, gives general remainder/frequency methods for repetends with prime-power denominators. In particular, its Lemma 11 gives a bin-occupancy equivalence and Theorem 1 expressly leaves an intermediate gap regime undecided by the coarse gap bound. The present result concerns the moving, period-scale length \(m_k\): it resolves that critical regime explicitly for powers of three, counts every absent critical word, and determines the asymptotic frequency of the two sharp length phases. The basic remainder correspondence and the fixed-length convergence are prior work, not new claims.

## Limitations

The result is specific to radix two and denominators \(3^k\); it does not give a full frequency vector for all words at all lengths or classify other prime-power denominators. The 2012 paper on exactly this repetend family was identifiable, but its complete text could not be retrieved from the accessible mirrors for a page-by-page comparison. Its published abstract describes a sufficient fixed-word-length condition, not the exact critical deficit; an uninspected stronger statement in that paper remains a concrete publication-priority risk. A general floor-distribution theorem might also subsume the deficit formula. No independent mathematical audit is asserted.

## References

1. Josefina López and Peter Stoll, *The repetends of reduced fractions \(a/b^k\) approach full complexity with an increasing \(k\)*, arXiv:2105.06513, first public version May 13, 2021; *Integers* 22 (2022), article A75. https://arxiv.org/abs/2105.06513 .
2. Josefina López and Peter Stoll, *The 2-adic, binary and decimal periods of \(1/3^k\) approach full complexity for increasing \(k\)*, *Integers* 12 (2012), article A28, April 18, 2012. https://www.kurims.kyoto-u.ac.jp/EMIS/journals/INTEGERS/papers/m28/m28.pdf .
