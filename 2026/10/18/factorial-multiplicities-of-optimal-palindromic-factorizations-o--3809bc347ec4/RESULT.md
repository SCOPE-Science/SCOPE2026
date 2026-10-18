# Factorial multiplicities of optimal palindromic factorizations of Zimin prefixes

## Finding
Let \(Z=z_1z_2\cdots\) be the infinite Zimin (ruler) word with \(z_j=1+\nu_2(j)\) for every integer \(j\ge1\), where \(\nu_2(j)\) is the exponent of two dividing \(j\). A *palindromic factorization* of its length-\(n\) prefix means a partition into consecutive nonempty palindromic substrings, and two such factorizations are distinct when their cut positions differ. Let \(R(n)\) be the number of maximal constant-bit runs in the ordinary binary representation of \(n\), with \(R(0)=0\). Write \(M(n)\) for the number of palindromic factorizations of \(z_1\cdots z_n\) having the **minimum possible number of parts**, and put \(M(0)=1\).

For every integer \(n\ge1\), the exact multiplicity is
\[
\boxed{M(n)=\left\lceil \frac{R(n)}2\right\rceil!\,\left\lfloor\frac{R(n)}2\right\rfloor!}. 
\]
In particular, this multiplicity is independent of the individual binary run lengths and depends only on the number of runs. More explicitly, the optimal last factors correspond bijectively to the starts of the maximal runs of ones in the binary expansion, and their number is \(\lceil R(n)/2\rceil\).

For every integer \(m\ge1\) and every \(1\le r\le m\), **exactly** \(\binom mr\) integers \(n\) with \(1\le n<2^m\) have minimum palindromic length \(r\) and exactly \(\lceil r/2\rceil!\lfloor r/2\rfloor!\) optimal factorizations. For \(m\ge3\), the unique prefix maximizing the number of optimal factorizations among these \(2^m-1\) prefixes is the one indexed by the alternating \(m\)-bit integer starting with one.

The identity between minimum palindromic length and \(R(n)\) is an earlier result of Shuo Li (2020); **it is not part of the claimed new contribution**. The contribution claimed here is the exact multiplicity and its all-prefix distribution, together with the characterization of permissible optimal final cuts.

## Assumptions and scope
Positions in \(Z\) are indexed from one. A factorization consists of a strictly increasing chain \(0=n_0<n_1<\cdots<n_\ell=n\), with each \(z_{n_{j-1}+1}\cdots z_{n_j}\) a palindrome; repetitions of the same substring at different positions are counted separately if the chains differ. The alphabet is the infinite ordered family of distinct integer labels, but palindrome testing uses only equality of labels, so the additive one in \(z_j\) is immaterial. The binary expansion of \(n\) has no leading zeros. The stated histogram ranges over all nonzero integers below \(2^m\), including shorter binary expansions. No randomness or limiting assumption is used.

## Proof
**1. Exact suffix-palindrome correspondence.** Adjacent letters in \(Z\) differ because precisely one of two adjacent positive integers is even; hence every palindrome has odd length and an integral center \(c\ge1\). Put \(s=\nu_2(c)\). For every integer \(d\) with \(0<d<2^s\), provided both positions are positive, the valuation identity
\[
\nu_2(c-d)=\nu_2(d)=\nu_2(c+d)
\]
shows that the substring centered at \(c\) is palindromic through radius \(2^s-1\). At \(d=2^s\), if the left position is positive, the two valuations differ: writing \(c=2^s u\) with \(u\) odd, the adjacent even integers \(u-1\) and \(u+1\) have unequal two-adic valuations. Thus no palindrome centered at \(c\) can extend to radius \(2^s\).

Fix \(n\ge1\). A palindromic suffix ending at \(n\) and centered at \(c\) exists exactly when \(n-c<2^{\nu_2(c)}\). It follows that \(c\) is the positive integer obtained from \(n\) by zeroing its bottom \(i\) binary bits for an index \(i\) at which the bit \(a_i(n)\) equals one. Conversely every such set-bit index yields one suffix: its center is \(c=2^i\lfloor n/2^i\rfloor\), its radius is \(n\bmod 2^i\), and its preceding prefix length is
\[
 m_i=n-2(n\bmod 2^i)-1.
\]
In ordinary binary, \(m_i\) is obtained from \(n\) by complementing precisely the bits in positions \(0,1,\ldots,i\), leaving all more significant bits fixed. These suffixes have distinct preceding prefix lengths, so they are distinct final factors.

**2. Run change at a suffix step.** Let the bits of \(n\) be \(a_0,a_1,\ldots\), least-significant first, with zeros above the top bit. Then
\[
R(n)=\sum_{j\ge0}\bigl(a_j(n)\mathbin{\mathrm{xor}}a_{j+1}(n)\bigr).
\]
Every adjacent-bit comparison strictly below index \(i\) is unaffected when both bits flip, and comparisons strictly above \(i\) are also unaffected. The sole altered term compares bits \(i\) and \(i+1\). Since \(a_i(n)=1\), this proves
\[
R(m_i)=\begin{cases}R(n)-1,&a_{i+1}(n)=0,\\R(n)+1,&a_{i+1}(n)=1.\end{cases}
\]
In particular, \(R(m_i)\ge R(n)-1\) for every suffix, and the highest set-bit position of \(n\) always offers a suffix with \(R(m_i)=R(n)-1\).

**3. Minimum length and counting optimal factorizations.** Let \(L(n)\) be the minimum number of palindrome parts. Every factorization has exactly one final palindrome, hence
\[
L(n)=1+\min_{i:\,a_i(n)=1}L(m_i),\qquad L(0)=0.
\]
All \(m_i<n\); strong induction using step 2 yields \(L(n)=R(n)\). This rederives the previously known length formula only to support the multiplicity theorem. A suffix can finish an optimal factorization if and only if \(R(m_i)=R(n)-1\), equivalently \(a_i(n)=1\) and \(a_{i+1}(n)=0\). Such indices are exactly the most significant positions of the maximal one-runs of the binary representation. Because binary runs alternate, starting with a one-run, their number is \(\lceil R(n)/2\rceil\).

By induction the number \(M(m_i)\) of optimal factorizations of any such predecessor depends only on its run count \(R(n)-1\). Different final palindromes yield disjoint classes of cut chains. Consequently
\[
M(n)=\left\lceil\frac{R(n)}2\right\rceil M_{R(n)-1},
\qquad M_0=1,
\]
where \(M_r\) denotes the common value for all \(n\) with \(R(n)=r\). Multiplying the factors \(\lceil j/2\rceil\) for \(1\le j\le r\) separates the odd and even indices and gives
\[
M_r=\left\lceil\frac r2\right\rceil!\left\lfloor\frac r2\right\rfloor!,
\]
proving the main identity. The successive choices also provide a bijection between optimal factorizations and two permutations of lengths \(\lceil r/2\rceil\) and \(\lfloor r/2\rfloor\): at stages with the same parity of the remaining run count, record the rank of the selected one-run among remaining choices, obtaining two independent factorial number-system codes.

**4. Complete finite-level distribution.** Among positive integers with exactly \(\ell\) binary digits, the leading bit is one. Exactly \(r\) maximal bit runs occur iff precisely \(r-1\) of the \(\ell-1\) adjacent-bit boundaries are transitions, giving \(\binom{\ell-1}{r-1}\) choices. Summing over \(\ell=r,\ldots,m\) and using the hockey-stick identity gives \(\binom mr\). Since \(M_{r+1}/M_r=\lceil(r+1)/2\rceil\), these multiplicities are nondecreasing and become strictly increasing after \(r=2\). For \(m\ge3\), the only length-at-most-\(m\) binary expansion with \(m\) runs is the unique alternating word of length \(m\) beginning with one, so its factorization multiplicity is the unique maximum. This finishes the proof.

## Verification
The accompanying `verify.py` requires only Python 3's standard library and can be run as `python3 verify.py`. Rather than using the bit-based suffix characterization, it independently enumerates every palindromic occurrence by center expansion, then computes palindromic lengths and optimal-factorization counts by exact dynamic programming for each of the first \(65{,}535\) nonempty prefixes. It checks the exact multiplicity and all \(16\) histogram levels, examines \(524{,}288\) palindrome occurrences, and separately probes \(254{,}553\) suffix-step bit identities on much larger integers. A passing run prints the `VERIFY_OK` summary. The computation tests examples and is not the proof of the unbounded assertion.

## Relationship to prior work
Fici, Gagie, Kärkkäinen and Kempa (2014) characterize all palindromic suffixes of Zimin prefixes (Lemma 12) for worst-case analysis of palindromic-factorization algorithms. Li (2020), especially Proposition 2 and Theorem 1, identifies the minimal palindromic length of ruler-sequence prefixes with the number of binary runs. These results supply essential ingredients and are explicitly credited. Neither inspected treatment states the present exact number of optimal cut chains, the characterization of all optimal final cuts, or their complete binomial-by-factorial distribution. The resulting factorial numerical sequence is already known in other contexts (OEIS A010551), so its numerical values are not claimed to be a newly discovered integer sequence.

## Limitations
This theorem is specific to Zimin/ruler prefixes, positional palindromic factorizations, and the usual binary expansion of the prefix length. It does not classify factorizations of arbitrary factors, general alphabets, or minimum factorizations under other costs. Its proposed originality is relative to the inspected literature and database evidence; an equivalent earlier presentation may exist. Computational checks cover finite prefixes only; the all-length assertion follows from the explicit inductive proof above. No independent audit has been performed.

## References
- G. Fici, T. Gagie, J. Kärkkäinen, D. Kempa, *A Subquadratic Algorithm for Minimum Palindromic Factorization*, arXiv:1403.2431 (first public posting 2014-03-10), Lemma 12, https://arxiv.org/abs/1403.2431.
- S. Li, *Palindromic length sequence of the ruler sequence and of the period-doubling sequence*, arXiv:2007.08317 (first public posting 2020-07-16), Proposition 2 and Theorem 1, https://arxiv.org/abs/2007.08317.
- OEIS A005811, number of runs in the binary expansion, https://oeis.org/A005811.
- OEIS A010551, parity-preserving permutations and corresponding factorial values, https://oeis.org/A010551.
