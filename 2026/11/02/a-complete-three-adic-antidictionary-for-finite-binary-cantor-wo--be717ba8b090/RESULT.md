# A complete three-adic antidictionary for finite binary Cantor words

## Finding

Let \(C_0=1\) and, for \(k\geq 0\), let \(C_{k+1}=\mu(C_k)\), where \(\mu(1)=101\) and \(\mu(0)=000\). For every integer \(k\geq1\), put \(G=3^{k-1}\). The *minimal absent factors* are exactly the following **disjoint** families:

1. \(11\), \(0^{G+1}\), and \(0C_{k-1}0\);
2. \(10^t1\) for \(1\leq t<G\) with \(t\) not a power of \(3\);
3. \(0^{3^r+1}C_r0^{3^r+1}\) and \(10^{3^r}C_r0^{3^r}1\) for each \(0\leq r\leq k-2\).

Consequently, their number is exactly
\[
3+(G-k)+2(k-1)=G+k+1=3^{k-1}+k+1.
\]
The set in item 2 is empty when \(k=1\). The empty-index family in item 3 is also empty when \(k=1\).

## Assumptions and scope

All factors are contiguous, all words are linear (not circular), and absence and minimality are relative to the alphabet \(\{0,1\}\). An absent word is *minimal* when its nonempty proper contiguous factors all occur. Equivalently, for a word \(aub\) of length at least two, with \(a,b\in\{0,1\}\), it is minimal absent exactly when \(au\) and \(ub\) occur but \(aub\) does not. This formulation also covers an empty interior \(u\). The substitution iterates have length \(3^k\), begin and end in \(1\), and are palindromes.

## Proof

**Gap-ruler law.** Number the ones from left to right, starting at one. There are \(2^k\) ones. For \(1\leq t<2^k\), the number of zeros separating the \(t\)-th and \((t+1)\)-st ones is
\[
g_t=3^{\nu_2(t)}.
\]
This follows inductively from \(C_{k+1}=C_k0^{3^k}C_k\): the gaps in both copies are the previous gaps; the new separating gap is \(3^k\). Thus the sequence of gap *ranks* \(1+\nu_2(t)\) is the finite ruler/Zimin sequence \(Z_{k-1}\), defined by \(Z_0=\varepsilon\), \(Z_{r+1}=Z_ra_{r+1}Z_r\).

**Boundary-context classification.** Write \(F_k\) for the set of factors of \(C_k\). The following classification results directly from the ruler law and determines *all* pairs \((a,b)\) for which \(au\) and \(ub\) occur but \(aub\) does not:

- For an all-zero interior \(u=0^t\), such pairs give \(11\) when \(t=0\), \(10^t1\) when \(1\le t<G\) is not a power of three, and \(0^{G+1}\) when \(t=G-1\). No other pair is missing.
- For an interior containing \(1\) and having two distinct left and two distinct right extension letters, necessarily
\[
u=0^{3^r}C_r0^{3^r},\qquad 0\le r\le k-2.\]
For each such \(u\), the present two-sided extensions are \(0u1\) and \(1u0\), whereas \(0u0\) and \(1u1\) are absent.
- If an interior containing \(1\) has fewer than two left or fewer than two right extension letters, the *only* failure to combine two individually present one-sided extensions occurs at \(u=C_{k-1}\): both \(0u\) and \(u0\) occur, but \(0u0\) does not.

For completeness, here is the ruler argument underlying the two nonzero assertions. Express an interior containing ones by its leading/trailing partial zero gaps and its intervening **complete** gaps. If the intervening gap-rank word is nonempty and has highest rank \(r\), its highest letter is unique. Its occurrences are centered at rank-\(r\) gaps, with a fixed lower-rank ruler block of length \(2^{r-1}-1\) on each side. Unless the interior consumes *both entire* fixed flanks, one exterior gap rank, and hence the corresponding one-bit extension condition, is constant across all occurrences. Simultaneous left and right variability therefore forces the complete rank block \(Z_r\) (where the single-one case is \(r=0\)). Its immediately exterior gap ranks alternate between \(r+1\) and ranks greater than \(r+1\); at least one of the two exterior ranks is always \(r+1\). To obtain both kinds of extension on *both* sides, each partial zero gap must consequently have length exactly \(3^r\). This gives precisely \(0^{3^r}C_r0^{3^r}\), and the alternating exterior ranks give the two cross extensions and forbid the two same-letter extensions. Thresholds smaller than \(3^r\) give only zero extensions; larger thresholds leave at most one side viable, so no further bispecial interior arises. At the endpoints of the finite gap-rank word the only missing combination caused purely by an omitted outside context is the longest repeated prefix/suffix \(C_{k-1}\), whose two occurrences lie at the two ends. Every shorter proper ruler-aligned block also has an internal occurrence, so its individually available unique extensions combine. This includes the one-one case: an interior with exactly one \(1\) has neighboring gap ranks alternating between rank one and a larger rank, yielding only \(u=010\) as the bispecial case. These statements are a direct case split on the unique maximum rank, with the two end occurrences treated separately.

**Enumerating the missing pairs.** For \(u=0^t\), the longest zero run has length \(G\); a run of exactly \(t\) zeros between two ones exists if and only if \(t\) is one of \(1,3,\ldots,G\). This accounts for item 2 and the unary obstruction. There are no adjacent ones, so \(11\) is absent. For each nonzero bispecial interior \(u=0^{3^r}C_r0^{3^r}\), its two absent two-sided extensions are exactly the two words in item 3. Finally \(C_{k-1}\) occurs as the two external copies in \(C_k=C_{k-1}0^GC_{k-1}\); the central gap supplies \(0C_{k-1}\) and \(C_{k-1}0\), while their simultaneous two-sided extension is absent, giving \(0C_{k-1}0\). The classification above rules out every other minimal absent word.

The families cannot overlap: item 2 has exactly two ones separated by a non-power-of-three gap; item 3 has allowed internal gaps but a missing exterior context; the longest case has unique length \(G+2\), while the level-\(r\) exceptional pair has length \(3^{r+1}+2\). Since there are exactly \(k-1\) allowed gap lengths strictly below \(G\), item 2 contributes \(G-k\). Adding the three elementary/top words and two words for each of \(k-1\) levels gives the displayed count.

## Verification

The accompanying standalone `checker.py` constructs each finite word independently, enumerates all distinct factors, generates minimal absent words from independently observed present prefix/suffix combinations, and compares the result with the explicit formula for ranks \(1\) through \(6\). The computed cardinalities are \(3,6,13,32,87,250\). The checker also rechecks the exact equation \(3^{k-1}+k+1\). The tests are finite; the unrestricted proof uses the gap-ruler and boundary-context classification above.

## Relationship to prior work

Barton–Heliou–Mouchard–Pissis (2014) give general algorithms for extracting minimal absent words via suffix arrays and extension contexts, but do not state this recursive-family classification. Głowinski–Rytter (2013) and Rytter–Shur (2014) study Zimin-pattern matching, rather than minimal absent factors of binary Cantor iterates. A prior accessible claim identified only the three minimal absent words of maximal length \(G+2\); this finding includes those as previously obtained special cases and extends them to the **complete** antidictionary at all lengths, including the gap-exclusion family and every persistent lower-level pair. It does not claim novelty for those earlier three maximal-length words. Priority outside the inspected sources remains uncertain.

## Limitations

The statement is restricted to literal complete binary substitution iterates, not arbitrary prefixes, circular factors, other alphabets, or minimal absent **subsequences**. The mathematical proof relies on the exact gap-boundary classification, while the finite checker provides an independent small-rank falsification test only. Historical novelty has not been independently certified.

## References

1. R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, arXiv:1307.1560 (first posted 2013-07-05).
2. C. Barton, A. Heliou, L. Mouchard, S. P. Pissis, *Linear-Time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341 (2014-06-24); BMC Bioinformatics **15**, 388 (2014), doi:10.1186/s12859-014-0388-9.
3. W. Rytter and A. M. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235 (2014-09-29).
