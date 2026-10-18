# The complete antidictionary and cubic spectrum of Zimin words

## Finding
For every integer \(n\ge1\), set \(Z_0=\varepsilon\) and recursively define the finite Zimin words over the integer alphabet \(\{1,\ldots,n\}\) by \(Z_j=Z_{j-1}\,j\,Z_{j-1}\). Let \(\mathcal M(Z_n)\) be the set of *minimal absent contiguous factors*: absent words whose every proper contiguous factor occurs in \(Z_n\). Then, with \(a,b\) denoting single alphabet symbols,

\[
\boxed{\mathcal M(Z_n)=\bigcup_{j=0}^{n-1}\left(\{(j+1)Z_j(j+1)\}\cup\{aZ_jb:j+2\le a,b\le n\}\right).}
\]

The union is disjoint. In particular, all minimal absent word lengths are exactly \(2^j+1\), for \(0\le j<n\), and the number at each such length is
\[
\boxed{\left|\{u\in\mathcal M(Z_n):|u|=2^j+1\}\right|=1+(n-j-1)^2.}
\]
Consequently,
\[
\boxed{|\mathcal M(Z_n)|=n+\frac{n(n-1)(2n-1)}6.}
\]
As the source word length is \(2^n-1\), its complete antidictionary has cubic growth in the alphabet rank, equivalently cubic logarithmic growth in source length.

## Assumptions and scope
A contiguous factor is a consecutive substring. Empty word \(\varepsilon\) is a factor. A minimal absent word has length at least two, and its length-one-deleted prefix and suffix must both be factors; this is equivalent to occurrence of every proper factor. The alphabet is exactly \(\{1,\ldots,n\}\), not an ambient alphabet with unused symbols. The finite word is linear, not circular or infinite. The displayed concatenation notation \((j+1)Z_j(j+1)\) uses letters \(j+1\), not integer multiplication.

## Proof
**1. Valuation geometry.** Number the letters of \(Z_n\) by \(i=1,\ldots,2^n-1\). The letter at \(i\) is \(1+v_2(i)\), where \(v_2(i)\) is the exponent of two dividing \(i\). This follows by induction from the recursive definition. For each \(h\ge1\), the open interval of indices between consecutive multiples of \(2^h\) spells \(Z_h\), provided it lies inside \(Z_n\). Every factor with greatest letter \(h\) contains no multiple of \(2^h\), so it is contained within such a copy of \(Z_h\). There is exactly one letter \(h\) in \(Z_h\), at the center. Therefore every occurrence of a fixed factor \(u\) whose maximum is \(h\) starts at the *same offset* within its copy of \(Z_h\). These are all copies at that offset, since the intervening blocks are identical.

**2. Only complete lower-level words can be middles of minimal absences.** Take a minimal absent word \(aub\), where \(a,b\) are single letters and \(u\) is its possibly empty middle. The factors \(au\) and \(ub\) occur, while \(aub\) does not. If \(u\ne\varepsilon\), put \(h=\max(u)\). If \(h=n\), the letter \(n\) occurs just once in \(Z_n\); hence \(u\) occurs once and the two available extensions would occur together, contradiction. Suppose \(h<n\). All occurrences of \(u\) occupy the identical offset inside distinct copies of \(Z_h\). If \(u\ne Z_h\), at least one end of \(u\) lies strictly inside its containing \(Z_h\) block. At such an end, its neighboring letter is fixed across *every* occurrence of \(u\), and exists even when the block is the initial or final copy. If the left neighbor is fixed, every occurrence of \(ub\) therefore extends to \(aub\), with \(a\) necessarily that fixed left letter (because \(au\) occurs); a contradiction. The symmetric argument holds if the right neighbor is fixed. It follows that \(u=Z_h\). The empty middle case is \(u=Z_0\). Thus only middles \(Z_j\), \(0\le j<n\), need examination.

**3. The complete extension graphs.** Fix \(1\le j<n\) and put \(T=2^{n-j}\). Every occurrence of \(Z_j\) occupies precisely the index interval
\[
 t2^j+1,\ldots,(t+1)2^j-1,\qquad 0\le t<T.
\]
For \(1\le t\le T-2\), both neighboring symbols exist; by the valuation formula their ordered pair is
\[
\bigl(j+1+v_2(t),\ j+1+v_2(t+1)\bigr).
\]
Since consecutive positive integers have opposite parity, such a pair contains exactly one instance of the smallest possible boundary letter \(j+1\), and its other letter belongs to \(\{j+2,\ldots,n\}\). Conversely *every* ordered pair \((j+1,b)\) and \((a,j+1)\) with \(j+2\le a,b\le n\) occurs: take \(t=2^{b-j-1}-1\) and \(t=2^{a-j-1}\), respectively. These choices lie in \(1\le t\le T-2\). The left and right one-sided extension sets of \(Z_j\) are each the complete set \(\{j+1,\ldots,n\}\): the occurrences with \(t=0\) and \(t=T-1\) supply the missing one-sided boundary cases, including \(T=2\). Thus the absent two-sided extension pairs are *precisely* \((j+1,j+1)\) and all \((a,b)\) with \(a,b\ge j+2\). When \(j=n-1\), there are no internal two-sided occurrences, and the only one-sided extension letter is \(n\); the same description gives just \(nZ_{n-1}n\).

For \(j=0\), the middle is empty, the one-sided extension sets contain all letters \(1,\ldots,n\), and an adjacent pair in \(Z_n\) always consists of \(1\) and a letter greater than \(1\). Every such ordered pair occurs when \(n\ge2\); for \(n=1\) there are no adjacent pairs. Consequently the absent minimal length-two words are exactly \(11\) and the pairs \(ab\) with \(2\le a,b\le n\), as asserted.

**4. Enumeration.** Every listed word is absent by the extension-graph classification, while both of its length-one-deleted factors occur, making it minimal absent. Conversely Step 2 excludes every other middle. Each \(Z_j\) has length \(2^j-1\); therefore each minimal absent word from its family has length \(2^j+1\), and different families cannot overlap. The family contains \(1+(n-j-1)^2\) words. Summing over \(0\le j<n\) yields \(n+\sum_{r=0}^{n-1}r^2=n+n(n-1)(2n-1)/6\).

## Verification
The standalone Python file `maw_verify.py` independently constructs the words by both recursion and binary valuations; reconstructs all minimal absent words from observed factor extension contexts, rather than from the claimed classification; and compares the sets and length spectra for \(1\le n\le9\). It also tests every predicted minimal absent word directly for \(n=10,11\). Run with `python3 maw_verify.py`. Recorded output terminates with `VERIFY_OK exhaustive_all_MAWs_levels=1..9 explicit_candidates_levels=1..11`. These finite tests check the implementation and small boundaries; the preceding argument proves the universal claim.

## Relationship to prior work
The Zimin recursion and valuation representation are classical, and appear explicitly in Cooper and Rorabaugh, *Bounds on Zimin Word Avoidance* (2014), arXiv:1409.3080. That work investigates pattern encounters and avoidance thresholds, not the minimal absent contiguous factors of the fixed Zimin word. Barton, Heliou, Mouchard, and Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array* (2014), arXiv:1406.6341, supplies the established generic minimal-absent-factor definition and an algorithm for arbitrary input words. Crochemore, Fici, Mercaş, and Pissis, *Linear-Time Sequence Comparison Using Minimal Absent Words & Applications* (2015), arXiv:1506.04917, studies comparison algorithms and circular extensions. These algorithms permit computation for any fixed input but do not state or imply the present closed description or cubic spectrum without the additional valuation-extension argument.

## Limitations
The classification is for exact finite Zimin words over their full used alphabet; changing the ambient alphabet, allowing scattered subsequences, changing to a circular word, or passing to the infinite ruler word changes the notion of minimal absence. Unindexed Zimin-specific literature could contain a restatement; the claim has not received independent scientific review. General algorithms for minimal absent factors are not claimed as new.

## References
[1] J. Cooper and D. Rorabaugh, *Bounds on Zimin Word Avoidance*, arXiv:1409.3080 (first public version 2014-09-10), https://arxiv.org/abs/1409.3080.

[2] C. Barton, A. Heliou, L. Mouchard and S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341 (first public version 2014-06-24), https://arxiv.org/abs/1406.6341.

[3] M. Crochemore, G. Fici, R. Mercaş and S. P. Pissis, *Linear-Time Sequence Comparison Using Minimal Absent Words & Applications*, arXiv:1506.04917 (first public version 2015-06-16), https://arxiv.org/abs/1506.04917.
