# Exactly two shortest-slack Lyndon words with full binary subsequence spectra

## Finding
Fix the ordered binary alphabet \(0<1\). A finite word is *\(k\)-subsequence-universal* if every length-\(k\) binary word occurs as a (not necessarily contiguous) order-preserving subsequence. A nonempty word is *Lyndon* if it is strictly lexicographically smaller than every nontrivial cyclic rotation.

**Theorem (first-slack Lyndon rigidity).** For every integer \(k\geq1\), the complete set of Lyndon, \(k\)-subsequence-universal binary words of length \(2k+1\) is
\[
\boxed{\big\{\,001(01)^{k-1},\ (01)^k1\,\big\}.}
\]
The two words are distinct and are related by reversing their order and complementing each bit. For every \(k\geq2\), no Lyndon word of length \(2k\) is \(k\)-subsequence-universal. Since no binary \(k\)-subsequence-universal word has length smaller than \(2k\), the **shortest length of a Lyndon \(k\)-subsequence-universal word** is \(2k+1\) for \(k\geq2\), and precisely the two displayed words attain it. When \(k=1\), the shortest such word is \(01\) of length two; the length-three classification remains valid.

For comparison, the full (unrestricted) family of \(k\)-subsequence-universal binary words of length \(2k+1\) has exactly
\[
(k+2)2^k
\]
members. Thus the exact proportion that are Lyndon is
\[
\boxed{\frac{2}{(k+2)2^k}.}
\]
This proportion tends exponentially to zero. The unrestricted count is an elementary consequence of the established binary arch factorization, and is supplied here only as context, not as a separate novelty claim.

## Assumptions and scope
Every word is a finite sequence of symbols from the **fixed** alphabet \(\{0,1\}\). The order is \(0<1\); complementing letters alone does not preserve the Lyndon property. The notion of \(k\)-subsequence-universality requires *all* \(2^k\) binary patterns of length \(k\), including the constant patterns. The intended quantifier is **every** integer \(k\geq1\), without an asymptotic qualification. A cyclic rotation moves an initial segment to the end without changing the order of either segment. Lyndon words here must be strictly less than all nonidentity rotations and therefore are primitive.

An *arch* is a shortest prefix of the remaining word containing both letters. For a binary alphabet it is a word of the form \(0^r1\) or \(1^r0\), with \(r\geq1\). Greedy removal of arches stops when the remainder contains at most one distinct letter. The number of extracted arches is exactly the subsequence-universality index: this is the classical arch criterion recalled by Barker et al. and Adamson. For clarity, it can also be proved directly by induction: one occurrence of each letter can be selected from the first arch, followed by an arbitrary pattern from subsequent arches; conversely, if the greedy decomposition has \(h\) arches, appending the missing letter of the terminal remainder to the last letters of the preceding arches gives an absent length-\(h+1\) subsequence.

## Proof
**1. Short length and basic Lyndon constraints.** Any \(k\)-universal binary word has at least \(k\) copies of each letter (because the patterns \(0^k\) and \(1^k\) must occur), so its length is at least \(2k\). Equivalently, every greedy arch has length at least two. A binary Lyndon word containing both letters starts with \(0\) and ends with \(1\). It cannot start with the larger letter. If it ended in a nonempty run of zeros, cyclically moving that trailing run in front of the initial zero run would create a rotation with more leading zeros than the original, contradicting Lyndon minimality. In particular, an internal occurrence of \(00\) rules out Lyndon status for a word beginning \(01\), because the corresponding cyclic rotation starts \(00\) and is smaller.

**2. At the absolute minimum length.** A \(k\)-universal word of length \(2k\) consists of exactly \(k\) greedy arches of length two and has no remainder. Every arch is \(01\) or \(10\). If the word were Lyndon, its first arch would be \(01\), and the entire word would have no \(00\) (otherwise rotation at \(00\) is smaller). Because the word has exactly \(k\) zeros, begins with \(0\), ends with \(1\), and has no adjacent zeros, all its zeros must occupy positions \(1,3,\ldots,2k-1\). Hence the only possibility is \((01)^k\), which is periodic and not Lyndon when \(k\geq2\). For \(k=1\) it is the Lyndon word \(01\).

**3. Length \(2k+1\), beginning \(01\).** Let \(w\) be a Lyndon \(k\)-universal word of length \(2k+1\) beginning with \(01\). It must avoid \(00\), or a cyclic rotation would be smaller. As \(w\) starts with \(0\), ends with \(1\), and has no \(00\), it can contain at most \(k\) zeros. Since \(0^k\) occurs as a subsequence, it contains exactly \(k\) zeros and \(k+1\) ones. Its \(k\) nonempty runs of ones after successive zeros therefore have lengths \(1,\ldots,1\), except for one run of length two. Thus for a unique \(j\in\{1,\ldots,k\}\),
\[
w=(01)^{j-1}011(01)^{k-j}.
\]
If \(j<k\), rotate \(w\) to start at the first zero after the unique \(11\). The resulting word is \((01)^k1\) and, having its unique doubled-one run later in the lexicographic comparison, is strictly smaller than \(w\). This contradicts the Lyndon property. Therefore \(j=k\) and \(w=(01)^k1\). Conversely, every rotation of this word beginning at a later zero encounters \(11\) before the original word does, and hence is lexicographically larger; every rotation beginning at a one is larger immediately. Therefore \((01)^k1\) is Lyndon. Its first \(2k\) positions are \(k\) successive arches \(01\), so it is \(k\)-universal.

**4. Length \(2k+1\), beginning \(00\).** The greedy first arch must be \(001\). Indeed, an arch starting \(00\) has length at least three, and length four would leave insufficient room for the other \(k-1\) arches. After \(001\), exactly \(2(k-1)\) letters remain, so they are precisely \(k-1\) arches, each one of \(01\) or \(10\), with no remainder. For \(k=1\) this already forces \(w=001\).

Suppose \(k\geq2\). The final arch must be \(01\), because a Lyndon word ends in \(1\). If any arch \(10\) occurs, take the *last* such arch. It is followed by \(b\geq1\) copies of \(01\). Rotate at the last zero of that \(10\); because the final suffix consists of \(b\) copies of \(01\) followed cyclically by the initial \(00\), the rotated word begins
\[
001(01)^{b-1}00.
\]
Let \(a\geq0\) be the number of initial \(01\) arches before the first \(10\). The original word begins
\[
001(01)^a10.
\]
If \(b-1<a\), then at the first divergence the rotation continues with \(00\) while the original continues with \(01\), so the rotation is smaller. If \(b-1\geq a\), then the original continues with the \(10\) arch while the rotation continues with \(01\) or \(00\), so again the rotation is smaller. The comparison is valid also when \(a=0\), and all displayed prefixes exist within the length-\(2k+1\) cyclic words. This contradicts Lyndon status. Therefore every remaining arch is \(01\) and
\[
w=001(01)^{k-1}.
\]
Conversely, this word has exactly one cyclic occurrence of \(00\), namely its first two letters. Every nontrivial rotation starting with \(0\) begins \(01\), and every rotation starting with \(1\) is larger, proving that it is Lyndon. Its initial \(001\) and its \(k-1\) subsequent \(01\) arches prove \(k\)-universality.

The two cases exhaust all binary Lyndon words: they must start \(0\), and the second symbol is either \(0\) or \(1\). This proves the classification for every \(k\geq1\) and the sharp minimum-length statement for \(k\geq2\).

**5. Comparison with unrestricted words.** With \(2k+1\) letters and at least \(k\) arches of length two, exactly one of two mutually exclusive possibilities occurs. Either there are \(k\) length-two arches \(01\) or \(10\), followed by one arbitrary bit, yielding \(2^k\cdot2=2^{k+1}\) words; or there is exactly one length-three arch, which must be \(001\) or \(110\), while the remaining \(k-1\) arches have length two, yielding \(k\cdot2\cdot2^{k-1}=k2^k\) words. The greedy factorization is unique, so these families are disjoint and exhaust all possibilities. Their sum is \((k+2)2^k\). As only the two classified words are Lyndon, the stated exact proportion follows.

## Verification
The standalone checker `CHECK.py` reconstructs the binary arch index and checks it against a logically independent direct greedy subsequence search over all \(2^k\) patterns for every binary host at lengths \(2k\) and \(2k+1\) with \(1\leq k\leq6\). It exhaustively enumerates all binary words at the first-slack length for \(1\leq k\leq9\), tests strict minimality against every nontrivial cyclic rotation, compares the complete Lyndon set with both displayed formulas, and checks the unrestricted count. It also proves computationally that no length-\(2k\) Lyndon \(k\)-universal word exists for \(2\leq k\leq9\), and tests the explicit witnesses at seven larger values through \(k=200\). All checks succeeded. These finite checks are a diagnostic confirmation, not a substitute for Steps 1–5, which establish the infinite theorem.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea, and Nowotka introduced systematic arch-based scattered-factor universality, including its circular version; their arXiv preprint dates to 10 March 2020. Their analysis gives the complete length-\(2k\) binary universal family but does not, in the inspected material, classify those with the additional Lyndon constraint at length \(2k+1\). Adamson's April 2023 paper gives algorithms counting and ranking all \(k\)-subsequence-universal words; the unrestricted count in the present theorem is consistent with that general machinery and is not independently claimed. Bannai, I, Kociumaka, Köppl, and Puglisi (January 2022) develop algorithms for longest Lyndon subsequences of a *given* host, not for Lyndon hosts carrying a full binary subsequence spectrum. Adamson et al. (November 2023) study intersections with regular languages; the full Lyndon language is not regular, and no uniform two-witness first-slack classification appears in its inspected text.

Related results on **circular** binary universality count necklace orbits at odd lengths and show that their maximizers are primitive. Their counts do not specify which lexicographically minimal rotations are **linearly** \(k\)-subsequence-universal. The present theorem determines this intersection, rather than inferring it from necklace counts or claiming novelty for arch factorization, unrestricted enumeration, or primitivity.

## Limitations
The theorem concerns exactly the ordered binary alphabet, the complete subsequence spectrum of a *fixed* order, and the two lengths \(2k\) and \(2k+1\). It does **not** enumerate Lyndon universal words at larger lengths, give a formula for other alphabet sizes, or claim novelty for the unrestricted arch count. Prior equivalence in unindexed or independently inaccessible literature remains a possible originality risk. The verification code checks only finite instances; the all-\(k\) conclusion follows from the written proof.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words* (first preprint 10 March 2020), arXiv:2003.04629v1, https://arxiv.org/html/2003.04629v1.
2. D. Adamson, *Ranking and Unranking k-subsequence universal words* (first preprint 10 April 2023), arXiv:2304.04583v1, https://arxiv.org/html/2304.04583v1.
3. H. Bannai, T. I, T. Kociumaka, D. Köppl, and S. J. Puglisi, *Computing Longest (Common) Lyndon Subsequences* (first preprint 18 January 2022), arXiv:2201.06773v1, https://arxiv.org/html/2201.06773v1.
4. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages* (2023), doi:10.4230/LIPIcs.ISAAC.2023.4, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2023.4.
