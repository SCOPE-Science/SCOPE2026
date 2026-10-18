# Exact minimum string attractors for dyadic prefixes of the powers-of-two word

## Finding
Let \(p_1p_2\cdots\) be the binary word with \(p_i=1\) exactly when \(i\) is an integral power of \(2\), and let \(P_m=p_1\cdots p_{2^m}\). For every integer \(m\ge2\), the minimum size of a (non-circular) string attractor of \(P_m\) is
\[
\gamma(P_m)=\left\lceil\frac{m}{2}\right\rceil+1.
\]
The exceptional length-two prefix \(P_1=11\) has minimum attractor size \(1\). The result holds for all dyadic lengths, not merely the finite lengths checked computationally.

## Assumptions and scope
For a finite word \(w=w_1\cdots w_n\), a string attractor is a set \(S\subseteq\{1,\ldots,n\}\) such that every nonempty factor of \(w\) has at least one occurrence whose position interval intersects \(S\). The minimum cardinality is denoted \(\gamma(w)\). Occurrences cannot wrap around the ends; indices are one-based. We work with the fixed, explicitly defined powers-of-two characteristic word and with integers \(m\ge2\).

## Proof
**Upper bound.** Schaeffer and Shallit, *String Attractors for Automatic Sequences*, Theorem 8, prove two attractor constructions for every sufficiently long prefix of this characteristic word. Specializing their one-based versions to length \(2^m\) gives the following explicit sets.

For even \(m=2k\), where \(k\ge1\), take
\[
S_m=\{2\cdot4^j:0\le j<k\}\cup\{3\cdot4^{k-1}\},
\]
which has \(k+1\) elements. Indeed \(2^m=4\cdot4^{k-1}\) lies between \(3\cdot4^{k-1}\) and \(6\cdot4^{k-1}\), so Theorem 8(a) applies (after shifting its zero-based positions by one).

For odd \(m=2k+1\), where \(k\ge1\), take
\[
S_m=\{4^j:0\le j\le k\}\cup\{6\cdot4^{k-1}\},
\]
which has \(k+2\) elements. Here \(2^m=8\cdot4^{k-1}\) lies in the interval required by Theorem 8(b). These published sets provide the asserted upper bounds.

**Matching lower bound.** We exhibit \(\lceil m/2\rceil+1\) pairwise disjoint intervals, each the only occurrence of a particular nonempty factor. An attractor must include at least one position in each interval.

For every \(m\ge2\), the factor \(11\) occurs exactly once, on \([1,2]\). For every even integer \(j\) with \(2\le j\le m-2\), the factor \(1\,0^{2^j-1}1\) occurs exactly once, on \([2^j,2^{j+1}]\): all the \(1\)'s lie at powers of two, and only the consecutive pair \(2^j,2^{j+1}\) has a gap containing exactly \(2^j-1\) zeros. The chosen intervals for different even \(j\) are disjoint.

The factor \(0^{2^{m-2}}1\) occurs exactly once, on \([2^m-2^{m-2},2^m]\). The preceding zero run of the final \(1\) has length \(2^{m-1}-1\); every earlier \(1\) has at most \(2^{m-2}-1\) preceding zeros. This last interval is strictly to the right of the preceding chosen ones.

If \(m=2k\) is even, the first interval, the \(k-1\) two-one intervals (even \(j=2,4,\ldots,m-2\)), and the last interval form \(k+1\) disjoint, uniquely occurring factors. Hence \(\gamma(P_m)\ge k+1\).

If \(m=2k+1\) is odd, add one further uniquely occurring factor
\[
0^{2^{m-3}}10
\]
on interval \([2^{m-1}-2^{m-3},2^{m-1}+1]\). Its middle \(1\) must be at \(2^{m-1}\): all earlier \(1\)'s have shorter preceding zero runs, while the final \(1\) at \(2^m\) is not followed by \(0\) within the prefix. The added interval lies strictly between the last selected two-one interval (if present) and the final interval; for \(m=3\) the selected intervals are exactly \([1,2]\), \([3,5]\), and \([6,8]\). Thus there are \(1+(k-1)+1+1=k+2\) disjoint forced intervals, yielding \(\gamma(P_m)\ge k+2\).

In both parity cases the lower bound matches the published explicit attractor, proving the formula. Finally \(P_1=11\), so \(\gamma(P_1)=1\). \(\square\)

## Verification
The accompanying `verify.py` reconstructs the claimed forced intervals for \(2\le m\le14\), independently checks that their factor spellings are correct, are unique, and occupy pairwise disjoint intervals, and checks the witness cardinalities. For \(2\le m\le9\), it additionally enumerates every nonempty factor occurrence and independently verifies that the explicit upper-bound set intersects some occurrence of each distinct factor. The exact finite computation checks the definitions; the all-order proof does not extrapolate from the finite results. Run `python verify.py` using the Python standard library.

## Relationship to prior work
Schaeffer and Shallit, Theorem 8 of arXiv:2012.06840, supply exactly the upper-bound attractors used here and expressly note that a matching lower bound requires other techniques. The additional contribution here is the explicit parity-sensitive disjoint packing of uniquely occurring factors, closing the resulting dyadic-prefix optimality gap. Béal, Crochemore, and Romana (arXiv:2509.08503v2, Section 5, Table 2) report greedy-attractor sizes for dyadic prefixes of the same sequence, not their minimum sizes. The 2024 analysis of string-attractor complexity by Cassaigne and coauthors addresses asymptotic complexity and related invariants rather than this exact dyadic profile.

## Limitations
The theorem concerns only prefix lengths that are powers of two; it does not determine minimum attractor sizes for every arbitrary prefix length, count all optimal attractors, or determine the behavior of any greedy algorithm beyond the cited finite experiments. The upper bound invokes an existing published theorem whose proof uses automated first-order verification; the new lower bound is elementary. The finite checker is supporting evidence, not an infinite proof. The possibility of an equivalent earlier characterization not found in the checked literature remains a priority risk. No independent scientific audit has been performed.

## References
1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, Theorem 8 and Section 6, https://arxiv.org/abs/2012.06840.
2. M.-P. Béal, M. Crochemore, and G. Romana, *Checking and producing word attractors*, arXiv:2509.08503, originally publicly posted 10 September 2025, revised 9 October 2026; Section 5, Table 2, https://arxiv.org/abs/2509.08503.
3. J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino, and M. Stipulanti, *New string attractor-based complexities for infinite words*, J. Combin. Theory Ser. A 208 (2024), 105936, https://doi.org/10.1016/j.jcta.2024.105936.
