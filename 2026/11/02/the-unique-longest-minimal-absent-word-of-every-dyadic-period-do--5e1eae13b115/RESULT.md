# The unique longest minimal absent word of every dyadic period-doubling prefix

## Finding

For every integer \(k\ge3\), define the binary word \(P_0=0\) and \(P_{k+1}=\mu(P_k)\), where \(\mu(0)=01\) and \(\mu(1)=00\). Put \(h=2^{k-1}\), let \(Q_k\) be the prefix of \(P_{k-1}\) obtained by deleting its final letter, and write \(c_k\) for that final letter. Then the largest length of a minimal absent contiguous word of \(P_k\) is \(h+1\), and the complete set of words attaining the maximum is

\[\boxed{\{c_kQ_kc_k\}},\qquad c_k=(k-1)\bmod 2.\]

For example, \(P_3=01000101\); the unique longest minimal absent word is `00100`, of length \(5\). For \(P_4\), it is `101000101`, of length \(9\). These are statements about finite linear words, without wrapping around their endpoints.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); factors are contiguous strings, with zero-based starting indices. A word \(v\) is *absent* from \(P_k\) if it does not occur as a contiguous factor. It is *minimal absent* if every proper contiguous factor occurs. For length at least two, checking the proper prefix and proper suffix of length one less suffices, because every other proper factor is contained in one of them. The result holds for all integers \(k\ge3\), and no statement about other substitutions or the infinite limit is needed.

## Proof

**1. Half-block identity and parity.** Set \(n=2^j\). For every \(j\ge1\), \(P_j\) consists of two length-\(2^{j-1}\) blocks agreeing at all but the final position: the first is \(P_{j-1}\), and the second is \(P_{j-1}\) with its last letter toggled. For \(j=1\) this is `01`. Inductively, the morphic images of two equal-length strings differing only in the final letter agree except at their final symbol, because \(\mu(0)\) and \(\mu(1)\) agree in their first symbols and disagree in their second symbols. Thus the half-block identity persists.

Every symbol at an even zero-based position of \(P_j\) is zero, and its symbol at odd position \(2i+1\) equals \(1-P_{j-1}[i]\). Consequently \(P_j\) contains no `11`. It also contains no `0000`: two successive odd positions in any run of four zeros would imply `11` at successive positions of \(P_{j-1}\). Hence every factor of length at least four contains a one. Since all ones occupy odd global positions, two equal factors of length at least four must start at positions of the same parity.

**2. Exact longest repeated-factor structure.** We prove by induction that for every \(j\ge3\), writing \(H=2^{j-1}\), all length-\(H\) factors of \(P_j\) occur once, and the only repeated factor of length \(H-1\) is its first \(H-1\) letters, occurring exactly at starts \(0\) and \(H\).

For \(j=3\), \(P_3=01000101\). Its length-three factors, in starting-position order, are `010`, `100`, `000`, `001`, `010`, `101`; only `010` repeats, at \(0\) and \(4\). Its five length-four factors are `0100`, `1000`, `0001`, `0010`, `0101`, all different.

Assume the claim for \(P_j\) of length \(2H\), and consider \(P_{j+1}\), of length \(4H\). Let \(L=2H-1\). Any two equal length-\(L\) factors begin at the same parity, by step 1. For odd starts \(2i+1\), restricting the factor to its \(H\) odd global positions and complementing those letters recovers exactly the length-\(H\) factor of \(P_j\) beginning at \(i\). These are pairwise distinct by induction. For even starts \(2i\), restricting to the \(H-1\) odd global positions and complementing recovers the length-\(H-1\) factor of \(P_j\) beginning at \(i\). By induction, the only possibly equal pair comes from \(i=0\) and \(i=H\). The half-block identity from step 1 ensures the corresponding length-\(L\) factors of \(P_{j+1}\) really agree, at starts \(0\) and \(2H\). There are no others.

A repeated length-\(2H\) factor of \(P_{j+1}\) would have repeated length-\((2H-1)\) prefixes and hence would have to occur at starts \(0,2H\). But the two length-\(2H\) halves have distinct last letters. This proves both induction claims.

**3. Relating absent words to repeated interiors.** Let \(v=aub\) be an absent word of length \(\ell\ge3\) with its length-\((\ell-1)\) prefix \(au\) and suffix \(ub\) occurring in \(P_k\). The interior \(u\), of length \(\ell-2\), must then occur at two *different* positions: if an occurrence of \(au\) ending at a given occurrence of \(u\) and an occurrence of \(ub\) beginning at that same occurrence of \(u\) coincided, they would form an occurrence of \(aub\), contrary to absence. If \(\ell\ge h+2\), then \(\lvert u\rvert\ge h\), impossible because all length-\(h\) factors of \(P_k\) are unique. Hence no minimal absent word is longer than \(h+1\).

At length \(h+1\), the interior must be the *unique* repeated length-\((h-1)\) factor \(Q_k\), which occurs only at \(0\) and \(h\). Its occurrence at \(0\) has right context \(c_k\) and no left context. The one at \(h\) has left context \(c_k\) and right context \(1-c_k\). Thus the only available nonempty left context of \(Q_k\) is \(c_k\), and the only absent two-sided combination whose left and right one-sided factors both occur is \(c_kQ_kc_k\). The prefix \(c_kQ_k\) occurs starting at \(h-1\); the suffix \(Q_kc_k\) occurs starting at \(0\); and \(c_kQ_kc_k\) never occurs, because the only right continuation after a left \(c_k\) is \(1-c_k\). Therefore this word is minimal absent and is unique at the maximum length.

Finally, the last symbol toggles under each substitution step, starting with the zero in \(P_0\), giving \(c_k=(k-1)\bmod2\). This proves the theorem. \(\square\)

## Verification

The supplied standalone `checker.py` directly builds \(P_k\) and all distinct contiguous factors. For each \(k=3,\ldots,9\), it enumerates all minimal absent words via occurring length-one-shorter prefixes and suffixes, independently checks the uniqueness of the length-\((h-1)\) repeated factor and the uniqueness of length-\(h\) factors, and tests the stated extremal set and length. All seven substitution levels passed. This finite computation confirms boundary cases but does not prove the all-level induction.

To reproduce, run `python checker.py` using Python 3 and no third-party packages.

## Relationship to prior work

Barton, Heliou, Mouchard, and Pissis (2014) study computation of minimal absent words via suffix arrays; Crochemore, Fici, Mercaş, and Pissis (2015) study their use in sequence comparison. Neither inspected treatment classifies the longest minimal absent factors of these period-doubling prefixes. Schaeffer and Shallit (2015) study other automatic-sequence factor properties. Banbara and collaborators (2026) establish period-doubling parity and half-block properties in their study of string attractors; those structural observations are consistent with steps 1–2 but do not state or establish this extremal minimal-absent-word classification. A previous lower-bound construction had already exhibited this *particular absent word* among several explicit witnesses, but did not establish that it was uniquely longest. Accordingly, only the sharp upper bound and completeness/uniqueness of the extremal class are asserted as the distinguishing contribution, not the existence of the witness alone.

## Limitations

The theorem applies to the finite prefixes \(P_k\) for \(k\ge3\), not circular words or arbitrary prefix lengths. It does not enumerate all shorter minimal absent words; counts printed by the finite checker are observations, not an asserted all-level counting formula. The earlier boundary witness is acknowledged, and historical priority for the additional extremality and uniqueness conclusion remains subject to further literature review. Independent review has not been performed.

## References

1. C. Barton, A. Heliou, L. Mouchard, S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341, first posted 2014-06-24, https://arxiv.org/abs/1406.6341 .
2. M. Crochemore, G. Fici, R. Mercaş, S. P. Pissis, *Linear-Time Sequence Comparison Using Minimal Absent Words & Applications*, arXiv:1506.04917, 2015, https://arxiv.org/abs/1506.04917 .
3. L. Schaeffer, J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074, 2015, https://arxiv.org/abs/1508.02074 .
4. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152 (initial version, 2026-02-18; later updated), https://arxiv.org/abs/2602.16152 .
