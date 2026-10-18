# Exact palindrome complexity of every generalized Cantor word

## Finding
For an integer \(q\ge3\), let \(C_q\) be the infinite fixed point, starting with \(1\), of the uniform morphism
\[\mu_q(1)=10^{q-2}1,\qquad\mu_q(0)=0^q.\]
Let \(P_q(n)\) be the number of **distinct palindromic contiguous factors** of length \(n\) in \(C_q\); put \(P_q(0)=1\). For \(j\ge0\), write
\[g_j=(q-2)q^j,\qquad M_j=(2q-3)q^{j+1}.\]
For every \(n\ge1\), the exact all-length, all-base formula is
\[
\boxed{P_q(n)=1+\mathbf 1_{\{n\text{ odd},\ n\le2q-3\}}+\sum_{j\ge0}\mathbf1_{\{n\equiv g_j\pmod2,\ g_j+2\le n\le M_j\}}.}
\]
The sum is finite. It follows that \(1\le P_q(n)\le3\) for all \(n\ge1\) and every \(q\ge3\). The formula classifies the palindrome factors by their centers, not merely their counts.

## Assumptions and scope
All words use the alphabet \(\{0,1\}\). A factor is a contiguous subword, not a scattered subsequence; palindromes are unchanged by reversal. All quantifiers range over integers \(q\ge3\), \(n\ge0\), and \(j\ge0\). The empty word is the unique factor of length zero. The fixed point is well-defined because \(\mu_q(1)\) begins in \(1\); no uniform-recurrence assumption is used. This result addresses palindromic **factor complexity**, not minimal palindrome concatenations of prefixes.

## Proof
**1. Separation of successive ones.** Put \(W_0=1\) and \(W_{t+1}=W_t0^{(q-2)q^t}W_t\). Induction gives \(W_t=\mu_q^t(1)\), \(|W_t|=q^t\), and \(W_t\) palindromic. Every factor of \(C_q\) occurs in some \(W_t\). Number the occurrences of \(1\) from the beginning. The gap after occurrence \(m\ge1\) has exactly \(g_{\nu_2(m)}\) zeros, where \(\nu_2(m)\) is the exponent of two dividing \(m\). This follows by induction from the gap list for \(W_{t+1}\): the old list, a central gap \(g_t\), and the old list again, indexed by \(1\le m<2^{t+1}\).

**2. Centers at a one.** Between any three consecutive ones, the two gaps have different lengths: of consecutive positive integers, one is odd and therefore has valuation zero, while the other has positive valuation. A palindrome centered at a one cannot include another one on both sides; its maximal zero radius is \(g_0=q-2\). Every radius \(0\le r\le g_0\) does occur, for instance at an interior one bordered by gaps \(g_0\) and \(g_1\). Consequently the palindromes centered at a one are exactly \(0^r10^r\) for these radii. They contribute precisely one factor at each odd length \(1\le n\le2q-3\).

**3. Centers at zero gaps.** A palindrome containing ones but not centered at one has an even number of ones and is centered between two consecutive ones. Suppose that the central zero gap has size \(g_j\), i.e. index \(m\) has \(\nu_2(m)=j\). For every integer \(1\le h<2^j\),
\[\nu_2(m-h)=\nu_2(m+h)=\nu_2(h),\]
so the gaps on either side of the central gap agree through the nearest \(2^j\) ones on each side. The symmetric core is exactly \(W_{j+1}\), of length \(q^{j+1}\) and with \(2^{j+1}\) ones. At the next gap pair, the indices are \(m\pm2^j\). Their valuations are \(j+1\) and at least \(j+2\), in some order. Hence the shorter bordering zero run has length exactly \(g_{j+1}\). It is impossible to extend a palindrome past the end of that run, since one side next meets a one while the other still sees zero. The longest possible palindrome with center type \(j\) therefore has length
\[q^{j+1}+2g_{j+1}=(2q-3)q^{j+1}=M_j.\]
For existence at the maximal length, take the central gap of index \(m=3\cdot2^j\), where both neighboring outer gaps exist; its symmetric extension realizes the bound. All shorter centered substrings have the same content for a fixed \(j\), independent of \(m\). A palindrome with ones has both of its two central ones included exactly when \(n\ge g_j+2\); its parity agrees with \(g_j\). Therefore for each \(j\) precisely one such distinct palindromic factor occurs at every \(n\) satisfying \(g_j+2\le n\le M_j\) and \(n\equiv g_j\pmod2\).

**4. Disjointness and completeness.** For a fixed length, palindromes with different central gap types \(j\) are distinct: their innermost pair of ones bounds zero runs of different lengths \(g_j\). A one-centered palindrome and an all-zero palindrome are distinct from these and from each other. All-zero factors \(0^n\) occur for each \(n\ge1\) because \(g_j\to\infty\). Every nonzero palindrome has a center of exactly one of the two preceding kinds. Adding the disjoint contributions gives the claimed formula. Finally, three different gap levels cannot qualify at the same length: the interval for level \(j-1\) ends at \((2q-3)q^j\), which is strictly smaller than the next-but-one level's start \((q-2)q^{j+1}+2\) for \(q\ge3\). Thus at most two gap types qualify; if two qualify then \(n\) already exceeds \(2q-3\), so the single-one contribution vanishes. This proves \(P_q(n)\le3\).

## Verification
The accompanying standalone `verify_pal.py` independently generates finite prefixes both by substitution and by base-\(q\) digit testing (one exactly when all digits are \(0\) or \(q-1\)). It exhaustively enumerates palindromic factors and checks the formula for \(3\le q\le9\) and \(1\le n\le80\), 560 parameter pairs. It also tests the empty-factor convention. A finite check is not the infinite proof, which is the preceding gap-center classification. Run with `python verify_pal.py` (Python 3, standard library only).

## Relationship to prior work
Glen–Justin–Widmer–Zamboni (2008/2009) **already record richness of the classical Cantor word**; richness of that particular word is not new here. Lü–Chen–Guo–Wen (2016), Section 3, give factor complexity for the full Cantor-like family, including the classical identity \(p(n)=2n-1\) for \(n\ge2\). Bucci–De Luca–Glen–Zamboni (2008/2009) relate richness to factor and palindrome complexity. These together imply the classical \(q=3\) palindrome counts, so that specialization is **not asserted as original**. Bulgakova–Frid–Scanvic (2022) determine **prefix palindromic length**, a different invariant, and discuss the wider family. Morfonios–Schmelcher–Kalozoumis–Diakonos (2014) investigate symmetry axes numerically in the classical Cantor lattice, without the stated all-base factor-count formula. The contribution here is the **uniform all-base, all-length** exact formula and its center-level classification, especially the alternating and scale-dependent profiles at \(q\ge4\).

## Limitations
This is a mathematical statement about one explicit uniform-morphism family, not arbitrary automatic words. The result does not determine palindrome occurrence frequencies, return-word distributions, prefix-palindromic factorization lengths, or all maximal palindromes in an arbitrary finite prefix. Although the accessible literature does not supply the all-base formula, an equivalent result in unindexed or inaccessible work remains a possible originality risk. No independent scientific audit has been performed.

## References
- A. Glen, J. Justin, S. Widmer, L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656 (first posted January 10, 2008), Proposition 2.10. https://arxiv.org/abs/0801.1656
- M. Bucci, A. De Luca, A. Glen, L. Q. Zamboni, *A connection between palindromic and factor complexity using return words*, arXiv:0802.1332 (2008), Theorem 1.1. https://arxiv.org/abs/0802.1332
- X.-T. Lü, J. Chen, Y.-J. Guo, Z. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, §3 and Remark 5. https://doi.org/10.1016/j.tcs.2015.12.022
- D. Bulgakova, A. E. Frid, J. Scanvic, *Prefix palindromic length of the Sierpinski word*, arXiv:2201.09556 (2022). https://arxiv.org/abs/2201.09556
- C. Morfonios et al., *Local symmetry dynamics in one-dimensional aperiodic lattices: a numerical study*, Nonlinear Dynamics (2014), §3.5. https://doi.org/10.1007/s11071-014-1422-1
