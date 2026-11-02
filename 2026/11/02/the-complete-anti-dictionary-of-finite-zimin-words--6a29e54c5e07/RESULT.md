# The Complete Anti-Dictionary of Finite Zimin Words

## Finding

Let \(a_1,a_2,\ldots\) be pairwise distinct letters. Define \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\) for every integer \(n\ge1\). The alphabet for a fixed \(Z_n\) is exactly \(\Sigma_n=\{a_1,\ldots,a_n\}\). A *minimal absent factor* of \(Z_n\) is a word over \(\Sigma_n\) which does not occur contiguously in \(Z_n\), but every proper contiguous factor does.

**Theorem.** For every \(n\ge1\), the complete set of minimal absent factors is the following disjoint union:

\[
\operatorname{MAW}(Z_n)=
\bigcup_{m=0}^{n-1}
\left(
 \{a_{m+1}Z_ma_{m+1}\}
 \;\cup\;
 \{a_iZ_ma_j:m+2\le i,j\le n\}
\right).
\]

Empty index ranges contribute no words. In particular, minimal absent factors have **only** lengths \(2^m+1\) for \(0\le m<n\), with the exact multiplicity

\[
\#\{w\in\operatorname{MAW}(Z_n):|w|=2^m+1\}
 =1+(n-m-1)^2.
\]

Their total number is

\[
|\operatorname{MAW}(Z_n)|=n+\frac{n(n-1)(2n-1)}6.
\]

The unique longest minimal absent factor is \(a_nZ_{n-1}a_n\), of length \(2^{n-1}+1\). Since \(|Z_n|=2^n-1\), the total number of minimal absent factors grows cubically in \(\log_2(|Z_n|+1)\), while the host length grows exponentially in \(n\).

## Assumptions and scope

All factors are **contiguous**, the words are **finite and linear**, and distinct letters \(a_i\) are literal alphabet symbols rather than variables to be substituted by arbitrary nonempty words. The empty word \(Z_0\) occurs only as an interior expression. Missing single letters outside \(\Sigma_n\) are not counted because the ambient alphabet is fixed to \(\Sigma_n\). A minimal absent word of length at least two is equivalently an absent word whose length-one-shorter prefix and suffix both occur.

## Proof

**1. Ruler positions and aligned copies.** Number the positions of \(Z_n\) from one. Its letter at position \(p\) is \(a_{1+\nu_2(p)}\), for \(1\le p<2^n\); this follows by induction from the central new letter and two equal halves. If \(m\ge1\), an occurrence of \(Z_m\) must begin at a position congruent to \(1\pmod{2^m}\). Indeed its unique central \(a_m\) must lie at an integer congruent to \(2^{m-1}\pmod{2^m}\), so the start has this residue. Conversely every fitting start congruent to \(1\pmod{2^m}\) spells \(Z_m\), since \(\nu_2(q2^m+t)=\nu_2(t)\) for \(1\le t<2^m\). For \(m=0\) alignment is vacuous.

**2. Prefix-continuation lemma.** Fix \(s\ge1\). For every prefix \(U\) of \(Z_s\) with \(|U|<|Z_s|\), the set of letters that can immediately follow some occurrence of \(U\) in \(Z_s\) is a singleton except when \(U=Z_m\) for some \(0\le m<s\). In that exceptional case it is exactly \(\{a_{m+1},a_{m+2},\ldots,a_s\}\).

For the empty prefix \(Z_0\), this is immediate. For a nonempty prefix length \(t\), put \(m=\lfloor\log_2(t+1)\rfloor\), so \(2^m-1\le t<2^{m+1}-1\). Every occurrence of that prefix begins with a copy of \(Z_m\) and is therefore aligned modulo \(2^m\). If \(t\ne2^m-1\), then \(2^m<t+1<2^{m+1}\), so the valuation of the next position is always \(\nu_2(t+1)<m\), independent of the occurrence. If \(t=2^m-1\), the next position is divisible by \(2^m\). All levels \(m,m+1,\ldots,s-1\) actually occur, by placing this next position at \(2^{j-1}\) for each \(m+1\le j\le s\). This proves the lemma.

**3. Border lemma.** Every border of \(Z_s\), including the empty word and the full word, is exactly one of \(Z_0,Z_1,\ldots,Z_s\). The stated words are borders by recursion. Conversely, let a nonempty prefix of length \(t\) also be a suffix, and take \(m=\lfloor\log_2(t+1)\rfloor\). The occurrence of its initial \(Z_m\) at the suffix start \(2^s-t\) must begin at residue \(1\pmod{2^m}\). Consequently \(t\equiv -1\pmod{2^m}\). Within \(2^m-1\le t<2^{m+1}-1\), the only possibility is \(t=2^m-1\), i.e. the prefix is \(Z_m\).

**4. Induction on the alphabet.** For \(n=1\), \(Z_1=a_1\) and its only minimal absent word over \(\Sigma_1\) is \(a_1a_1\). Assume the theorem for \(Z_{n-1}\). Because \(a_n\) occurs exactly once in \(Z_n=Z_{n-1}a_nZ_{n-1}\), a word without \(a_n\) occurs in \(Z_n\) exactly when it occurs in \(Z_{n-1}\). Hence all old minimal absent factors survive unchanged, and no new minimal absent factor avoiding \(a_n\) appears.

Consider a new minimal absent word \(w\) containing \(a_n\). Its prefix and suffix obtained by deleting one letter must occur. If \(a_n\) appears at least twice, those two copies must be precisely the first and last letters: otherwise a proper prefix or suffix would already contain two copies, impossible in \(Z_n\). Thus \(w=a_nUa_n\). The factors \(a_nU\) and \(Ua_n\) occur precisely when \(U\) is, respectively, a prefix and a suffix of \(Z_{n-1}\). The border lemma gives \(U=Z_m\) with \(0\le m\le n-1\). Every resulting \(a_nZ_ma_n\) is absent and minimal.

If \(a_n\) appears exactly once in the interior of \(w\), occurrence of the proper prefix fixes the left context and all but the final right-context letter around the unique \(a_n\). Occurrence of the proper suffix fixes the full right context and all but the initial left-context letter. These contexts necessarily fit together around the same unique position, forcing \(w\) itself to occur, a contradiction. Therefore \(a_n\) occurs at an endpoint. Reversal symmetry lets us take \(w=a_nV\), where \(V\) has no \(a_n\). The proper prefix occurs if and only if \(V\) without its final letter is a prefix of \(Z_{n-1}\); the proper suffix occurs if and only if \(V\) is a factor of \(Z_{n-1}\). For \(w\) to be absent, \(V\) must give an alternative next letter to a prefix. By the prefix-continuation lemma, \(V=Z_ma_j\), with \(0\le m\le n-3\) and \(m+2\le j\le n-1\). Every such \(a_nZ_ma_j\) is minimal absent. Reversal yields exactly the counterparts \(a_jZ_ma_n\). There are no others.

The new words just identified, together with the induction hypothesis, give exactly the theorem's disjoint union: at each middle rank \(m\), the unavailable endpoint pairs are the diagonal pair \((m+1,m+1)\) and all ordered pairs in \(\{m+2,\ldots,n\}^2\). There are \(1+(n-m-1)^2\) such pairs. Different middle ranks yield different lengths, and distinct endpoint pairs yield different words, proving the spectrum and its total. The largest length corresponds to \(m=n-1\), where only one endpoint pair is allowed. \(\square\)

## Verification

The supplied standalone Python checker constructs the Zimin words independently from their recursion, obtains minimal absent words by comparing left and right extensions of each *actual* factor, and compares the resulting sets (not only counts) with the proposed formula. It also verifies every proper-prefix continuation set by scanning all occurrences. Tests for \(1\le n\le9\) passed. For example, the total counts at ranks \(1,2,\ldots,9\) are \(1,3,8,18,35,61,98,148,213\). These finite tests are not used as a proof of the all-rank claim.

Run `python3 checker.py` in a directory containing the supplied checker. It has no third-party dependencies.

## Relationship to prior work

Głowinski and Rytter (2013, arXiv:1307.1560) study factors and compressed pattern matching in Zimin words; their Section 2 gives a general interleaving criterion for whether an explicitly given word is a factor. Rytter and Shur (2014, arXiv:1409.8235) investigate searching for Zimin patterns, Zimin type, and bounds on unavoidability. Barton et al. (2014) present general algorithms for generating the minimal absent factors of a supplied string. Those general membership and generation tools are distinct from the explicit all-rank *classification and multiplicity-by-length law* proved here. The fact that one could algorithmically enumerate absent factors using a general method does not by itself provide the compact index-pair formula or cubic count. No claim of priority beyond the investigated literature is made.

## Limitations

The result treats literal contiguous factors over the growing rank-dependent alphabet; it does not classify homomorphic occurrences of Zimin *patterns*, other Zimin encodings, or subsequence-absence. No theorem is asserted for factors over a larger alphabet including absent letters. The theorem's all-rank proof is mathematical; its finite checker covers ranks only through nine. The historical comparison is non-exhaustive and cannot rule out an equivalent classification under different terminology.

## References

1. R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, arXiv:1307.1560, first posted 2013-07-05, https://arxiv.org/abs/1307.1560.
2. W. Rytter and A. M. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235, first posted 2014-09-29, https://arxiv.org/abs/1409.8235.
3. C. Barton, A. Heliou, L. Mouchard, and S. P. Pissis, *Linear-time computation of minimal absent words using suffix array*, BMC Bioinformatics 15, 388 (2014), https://doi.org/10.1186/s12859-014-0388-9.
