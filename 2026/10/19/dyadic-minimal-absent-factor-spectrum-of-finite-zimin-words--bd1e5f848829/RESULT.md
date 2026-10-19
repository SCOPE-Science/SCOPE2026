# Dyadic minimal-absent-factor spectrum of finite Zimin words

## Finding

For each integer \(k\ge 1\), form the finite Zimin word \(Z_0=\varepsilon\), \(Z_k=Z_{k-1}x_kZ_{k-1}\), over its **exact** alphabet \(\Sigma_k=\{x_1,\ldots,x_k\}\). Write \(\mathcal M(Z_k)\) for its set of minimal absent **contiguous factors** relative to this alphabet. Then

\[
\boxed{\mathcal M(Z_k)=\bigsqcup_{j=0}^{k-1}\left(\{x_iZ_jx_i:j+1\le i\le k\}\ \sqcup\ \{x_iZ_jx_h:j+2\le i,h\le k,\ i\ne h\}\right).}
\]

All these families are disjoint. Consequently, the only occurring minimal-absence lengths are \(2^j+1\) for \(0\le j<k\), and their exact multiplicities are

\[
\boxed{\#\{u\in\mathcal M(Z_k):|u|=2^j+1\}=(k-j-1)^2+1.}
\]

The entire antidictionary has cardinality

\[
\boxed{|\mathcal M(Z_k)|=k+\frac{k(k-1)(2k-1)}6.}
\]

## Assumptions and scope

Words are linear, not circular. A factor is a **contiguous** substring, not a scattered subsequence and not an instance of a pattern under variable substitution. The alphabet is exactly \(\Sigma_k\), and every one-letter word in that alphabet occurs in \(Z_k\); in particular no length-one minimal absent words occur. A nonempty absent word is *minimal absent* if every proper contiguous factor occurs. It suffices to check its length-one-shorter prefix and suffix whenever its length is at least two. The empty word \(Z_0\) is included as a valid middle block in the displayed classification; \(|Z_j|=2^j-1\).

## Proof

**Lemma 1 (all borders).** For every \(m\ge1\), the proper nonempty borders (simultaneously prefixes and suffixes) of \(Z_m\) are exactly \(Z_1,\ldots,Z_{m-1}\). The empty word is also a border.

*Proof.* The claim holds for \(m=1\). Suppose it holds for \(m-1\), and put \(L=|Z_{m-1}|\). For a border of length at most \(L\), equality of the prefix and suffix of \(Z_m=Z_{m-1}x_mZ_{m-1}\) is equivalent to equality of the corresponding prefix and suffix of \(Z_{m-1}\), and the whole \(Z_{m-1}\) is allowed. A longer proper prefix and an equally long suffix both contain the unique letter \(x_m\), but at distinct relative positions: for border length \(t\) those positions are \(L+1\) and \(t-L\), equal only when \(t=2L+1=|Z_m|\), contrary to propriety. Induction completes the proof. \(\square\)

**Lemma 2 (right extensions of prefixes).** For a prefix \(P\) of \(Z_m\), let \(E_m(P)\subseteq\Sigma_m\) consist of the letters immediately following some occurrence of \(P\) in \(Z_m\) (the empty prefix is allowed). Then for \(0\le j<m\),
\[
E_m(Z_j)=\{x_{j+1},\ldots,x_m\}.
\]
Every other proper prefix has at most one right extension. The full prefix has no right extensions.

*Proof.* For any proper prefix containing \(x_m\), uniqueness of \(x_m\) in \(Z_m\) forces at most one occurrence, hence at most one right extension. Every prefix avoiding \(x_m\) is a prefix of \(Z_{m-1}\). Such a prefix \(P\) acquires exactly the old extension set \(E_{m-1}(P)\), together with the new letter \(x_m\) precisely when \(P\) is a suffix of \(Z_{m-1}\) (at the boundary before the unique central letter). By Lemma 1, among prefixes these are exactly \(Z_0,\ldots,Z_{m-1}\). Starting with \(E_0(Z_0)=\varnothing\), induction gives the stated sets and the at-most-one assertion for all other prefixes. \(\square\)

**Induction to classify the missing factors.** Assume the formula known for \(Z_{k-1}\), with the trivial empty-word base when \(k=1\). Any factor of \(Z_k\) avoiding \(x_k\) is a factor of \(Z_{k-1}\), because the two copies of \(Z_{k-1}\) are separated by the unique \(x_k\). Thus minimal absent words not involving \(x_k\) are exactly the inherited ones.

Consider a new minimal absent word \(u\) containing \(x_k\). There cannot be three occurrences of \(x_k\), nor two occurrences unless they are the first and last letters of \(u\): otherwise one length-one-shorter prefix or suffix would have at least two occurrences of \(x_k\) and could not occur in \(Z_k\). If the sole occurrence of \(x_k\) lies strictly inside \(u\), the existing length-one-shorter prefix and suffix force all letters on both sides of that unique central occurrence in \(Z_k\); hence \(u\) itself occurs, contradiction. Therefore the only cases are a single \(x_k\) at one end and an \(x_k\) at both ends.

For a word with one \(x_k\) at its left end, write \(u=x_kPc\) with \(c\in\Sigma_{k-1}\) and \(P\) an \(x_k\)-free word. The proper prefix \(x_kP\) occurs exactly when \(P\) is a prefix of \(Z_{k-1}\), and the proper suffix \(Pc\) occurs exactly when \(c\in E_{k-1}(P)\). Moreover \(u\) occurs precisely when \(c\) is the letter immediately following the initial copy of \(P\) in \(Z_{k-1}\). Therefore a new minimal absent word of this kind requires a prefix with at least two right extensions. Lemma 2 forces \(P=Z_j\) with \(0\le j\le k-2\); the right-extension set is \(\{x_{j+1},\ldots,x_{k-1}\}\), and the initial successor is \(x_{j+1}\). Thus the *exact* new words with one left-end \(x_k\) are
\[
x_kZ_jx_i\quad(0\le j\le k-2,\ j+2\le i\le k-1).
\]
All these are absent and have both length-one-shorter factors present. Every \(Z_m\) is a palindrome by recursion, so reversal gives the same classification with \(x_k\) at the right end:
\[
x_iZ_jx_k\quad(0\le j\le k-2,\ j+2\le i\le k-1).
\]

If \(u\) starts and ends with \(x_k\), write \(u=x_kPx_k\). The shorter prefix and suffix occur precisely when \(P\) is respectively a prefix and a suffix of \(Z_{k-1}\). Lemma 1 shows that \(P=Z_j\) for some \(0\le j\le k-1\). All the words \(x_kZ_jx_k\) are absent because \(Z_k\) has only one \(x_k\), and their shorter prefix and suffix occur, so these are *exactly* the two-end new words.

Adding the inherited words gives the displayed disjoint decomposition by induction. No two listed words with distinct \(j\) share a length because \(|Z_j|+2=2^j+1\), and different ordered endpoint pairs give different words at a fixed \(j\). For a fixed \(j\), the diagonal contributes \(k-j\) words and the distinct off-diagonal ordered pairs contribute \((k-j-1)(k-j-2)\), whose sum is \((k-j-1)^2+1\). Summation over \(j=0,\ldots,k-1\), with \(r=k-j-1\), gives \(\sum_{r=0}^{k-1}(r^2+1)=k+k(k-1)(2k-1)/6\). \(\square\)

## Verification

The accompanying standalone Python 3 script `check_zimin.py` reconstructs all factors directly, independently enumerates minimal absent words from factor-extension pairs, and compares the full sets with the theorem for every \(k=1,\ldots,8\). It also checks the exact per-length distributions and cubic cardinality. Its successful completion prints `ZIMIN_ANTIDICTIONARY_PASS k=1..8`. These checks are finite corroboration, not an infinite proof; the proof above supplies the unrestricted conclusion.

For illustration, \(Z_4=x_1x_2x_1x_3x_1x_2x_1x_4x_1x_2x_1x_3x_1x_2x_1\) has exactly \(18\) minimal absent words, with length multiplicities \(10,5,2,1\) at lengths \(2,3,5,9\), respectively.

## Relationship to prior work

Zimin words are classical recursively nested patterns studied, for example, by Conlon, Fox and Sudakov (2017) in their work on unavoidable patterns. Charalampopoulos and collaborators (2018) treat general minimal absent words and sequence comparison; Ayad and collaborators (2019) develop output-sensitive antidictionary construction; Akagi and collaborators (2022) classify MAW types with respect to run-length compression and report general enumeration structures. Their inspected statements and proofs supply general tools and different structural results, but do not explicitly characterize the finite Zimin antidictionary or its dyadic multiplicity distribution. No implication from their stated general bounds or algorithms to the displayed identity follows without the Zimin-specific border/right-extension analysis above. This is a best-knowledge literature comparison, not a claim of exhaustive historical novelty.

## Limitations

The result concerns only the **finite canonical** Zimin word, over the alphabet of its actual \(k\) symbols. If a larger ambient alphabet is used, each extra symbol is a length-one minimal absent word and the stated list must be enlarged. The theorem does not count forbidden *pattern substitutions* or scattered subsequences, nor does it establish improved general-purpose complexity bounds for arbitrary compressed texts. An equivalent result in unindexed literature remains possible.

## References

1. D. Conlon, J. Fox, B. Sudakov, “Tower-type bounds for unavoidable patterns in words,” arXiv:1704.03479 (initially public 2017-04-11). https://arxiv.org/abs/1704.03479
2. P. Charalampopoulos, M. Crochemore, G. Fici, R. Mercaş, S. P. Pissis, “Alignment-free sequence comparison using absent words,” arXiv:1806.02718 (initially public 2018-06-07). https://arxiv.org/abs/1806.02718
3. L. A. K. Ayad, G. Badkobeh, G. Fici, A. Héliou, S. P. Pissis, “Constructing Antidictionaries in Output-Sensitive Space,” arXiv:1902.04785 (initially public 2019-02-13). https://arxiv.org/abs/1902.04785
4. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, “Minimal Absent Words on Run-Length Encoded Strings,” arXiv:2202.13591 (initially public 2022-02-28). https://arxiv.org/abs/2202.13591

