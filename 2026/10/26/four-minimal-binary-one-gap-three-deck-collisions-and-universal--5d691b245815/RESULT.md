# Four minimal binary one-gap three-deck collisions and universal local substitutions

## Finding
Fix the alphabet \(\{0,1\}\). For a binary word \(w\), its **one-gap \(j\)-deck** \(B_j(w)\) records, with multiplicity, all length-\(j\) subsequences selected at indices \(i_1<\cdots<i_j\) with \(i_{h+1}-i_h\ge2\). Write \(B_{\le k}(w)=(B_1(w),\ldots,B_k(w))\). The full observation in this theorem is \(B_{\le3}\), not the ungapped deck.

**Exact length-thirteen census.** The \(8192\) binary words of length \(13\) have exactly \(8188\) distinct \(B_{\le3}\) observations: \(8184\) observations have one word and exactly four have two. The complete list of the doubleton classes, with word strings shown left to right, is:

| First member | Second member |
|---|---|
| `0010000101000` | `0001010000100` |
| `0110101111010` | `0101111010110` |
| `1010000101001` | `1001010000101` |
| `1110101111011` | `1101111010111` |

Every listed pair consists of reverse words. For lengths \(3\le n\le12\), the same full observation is injective. (There is a degenerate shorter exception: the length-two words `01` and `10` have the same single-letter observations.)

**Universal context substitution.** Each of these four pairs \((x,y)\) satisfies
\[
 B_{\le3}(pxq)=B_{\le3}(pyq)\qquad\text{for every }p,q\in\{0,1\}^{*}.
\]
More generally, the same conclusion holds for **any** equal-length words \(x,y\) with equal full one-gap decks through length three and equal one-gap decks through length two after deletion of the first letter, the last letter, and both endpoint letters separately. No padding or boundary restrictions on the contexts are needed.

Consequently, the single pair `1110101111011` and `1101111010111` supplies \(2^m\) distinct words of length \(13m\), all with the same complete one-gap three-deck, for every integer \(m\ge1\).

**Optimal reconstruction codebooks.** A length-thirteen code whose distinct words have distinct full observations has at most \(8188\) words. Exactly \(16\) distinct maximum codebooks attain this size. Under reversal and the global exchange of zero and one these maxima form exactly \(6\) orbits.

## Assumptions and scope
Words are finite, ordered strings with labeled positions; subsequences retain order but skip at least one index between each successive selected symbol. A deck is a **multiset** of observed subsequence strings, equivalently its complete vector of integer multiplicities. The result does not equate decks with sets, and does not use circular wraparound. The length-thirteen census is exhaustive for all \(2^{13}\) binary words, not a sample. Universal substitution allows any finite binary contexts, including empty contexts. The codebook optimum concerns noiseless observation of the entire one-gap three-deck of a single fixed-length word, with no other channel outputs assumed.

## Proof
**1. Exact integer census.** For each candidate word and each \(j\in\{1,2,3\}\), count the distinct ordered index selections of length \(j\) with consecutive selected indices differing by at least two. Collect the counts of the \(2+4+8=14\) possible nonempty observation strings into a tuple. Group all words by tuple, using exact integers. The reproducible `CHECK.py` performs the grouping for every length through thirteen and finds the four doubletons written above, with \(8184\) singleton groups and no group of size greater than two.

The same counts are independently reconstructed by a recurrence. Let \(F_i^{(j)}(v)\) be the number of valid selections spelling \(v\) and ending at index \(i\) (zero-based). For a one-symbol string \(b\), \(F_i^{(1)}(b)=\mathbf1_{w_i=b}\). For \(j\ge2\), when \(v=ub\),
\[
 F_i^{(j)}(ub)=\mathbf1_{w_i=b}\sum_{h=0}^{i-2}F_h^{(j-1)}(u).
\]
The deck count of \(v\) is \(\sum_iF_i^{(j)}(v)\). This recurrence is an exact partition by final selected index; it omits exactly the disallowed adjacency cases. The checker compares direct index enumeration and this recurrence on every length-thirteen binary word (as well as selected shorter lengths). Exhaustive grouping then proves the claimed entire census and the shorter injectivity statements, subject only to reproducible finite computation.

**2. Boundary-puncture identity.** For each displayed pair, direct exact deck computation establishes equality of the one-gap decks through length three on the intact words. It also establishes equality of one-gap decks through length two for the words obtained by removing only the first symbol, only the last, and both. The reproducible test checks these three operations separately for every pair. Importantly, the corresponding length-three punctured decks are *not* equal, so the weaker, two-letter puncture condition matters.

**3. Arbitrary-context lemma.** Suppose equal-length \(x,y\) satisfy the four deck equalities from step 2. Fix arbitrary contexts \(p,q\) and an observed output of length \(j\le3\). Partition its realizing index sets by the exact indices selected in the exterior contexts \(p,q\), including their prescribed bit values. These exterior choices are identical in \(pxq\) and \(pyq\). Inside the replaced block, allowable internal index selections obey the usual nonadjacency rule. If the last index of \(p\) was selected, the first index inside the block is forbidden; if the first index of \(q\) was selected, the last index inside the block is forbidden. No other exterior-selected index can forbid an interior position. Thus the internal contributions are counted by the intact deck or one of the three endpoint-punctured decks. If no exterior index was selected, at most three internal indices are needed and the intact \(B_{\le3}\) equality applies. If at least one exterior index was selected, at most two interior indices are needed and the appropriate \(B_{\le2}\) equality applies. Contributions using no interior positions depend only on the common block length. Every partition summand is therefore equal for \(pxq\) and \(pyq\), proving the lemma and its application to all four doubletons.

**4. Unbounded collision multiplicity.** Start with \(m\) consecutive length-thirteen copies of one member of any one doubleton pair. Replace any chosen copies with its partner. The context lemma preserves the complete deck after each independent replacement. There are \(2^m\) distinct resulting words because their length-thirteen blocks differ at every switched site. This proves the assertion for every \(m\ge1\), not just the finite test range.

**5. Exact codebook census and symmetry.** Any uniquely decodable set contains at most one word from each of the \(8188\) classes, and every maximal-size set contains all \(8184\) singleton words and exactly one representative from each doubleton. Hence the maximum size is \(8188\) and there are \(2^4=16\) maximum codebooks. Reversal and complementation each permute the observation classes because they relabel observation strings; their induced Klein-four action on the \(16\) choices has fixed-codebook counts \(16,0,4,4\), respectively, for identity, reversal, complement and reverse-complement. These four counts follow by explicit permutation of the eight listed doubleton words (also checked in `CHECK.py`). Burnside's lemma gives \((16+0+4+4)/4=6\) orbits.

## Verification
Run `python3 CHECK.py` with any standard Python 3 interpreter. The program enumerates every binary word of lengths one through thirteen, checks all thirteen-letter signatures by a separately implemented index-subset method, verifies the four listed pairs and their three boundary-puncture relations, tests a finite cross-section of two-sided contexts, independently checks collision multiplicity for two and three concatenated blocks, and evaluates all sixteen maximum codebooks under the reversal/complement group. Successful execution prints `GAPPED_THREE_DECK_PASS words=8192 classes=8188 doubletons=4 codebooks=16 orbits=6`. The universal-context statement and arbitrary-\(m\) corollary rely on the proved partition argument, not the finite context tests.

## Relationship to prior work
Golm, Nahvi, Gabrys and Milenkovic established the first nontrivial one-gap three-deck ambiguity at length thirteen; their Section III lists one example which coincides with the final doubleton above. That **threshold and example are prior work, not novel claims here**. Their later padded construction, Lemma 4, requires full length-three deck agreement also on three boundary punctures; the four pairs here fail those stronger punctured conditions, while the present lemma proves arbitrary unpadded context replacement from just length-two puncture agreement. Rigo, Stipulanti and Whiteland explicitly note that general positive-gap deck equivalence is not a concatenation congruence, and their displayed context-preserving local rules concern the two-deck relation; the present result identifies four particular three-deck equivalences for which arbitrary-context substitution *does* hold. Chrisnata and collaborators count **ungapped** subsequence decks; their tables concern a different observation channel. The present contribution is the complete first nontrivial collision-class census, the weaker-condition local replacement lemma, its exponential collision-family corollary and the associated optimal reconstruction-codebook census.

## Limitations
The complete finite classification is restricted to binary length thirteen and full decks through length three with a one-index gap. The context lemma has its stated sufficient hypotheses but is not asserted to characterize every context-stable equality. The lower bound \(2^m\) is for collision-class sizes at lengths \(13m\), not an asymptotic equality or maximum over all lengths. Published literature may contain an independently derived or differently formulated equivalent of some census entries; independently conducted review remains absent. The program is a transparent exhaustive finite certificate, not formal proof-assistant verification.

## References
1. J. Golm, M. Nahvi, R. Gabrys, O. Milenkovic, *The Gapped k-Deck Problem*, arXiv:2201.12671 (first public 2022-01-29), Sections III–IV and Lemma 4. https://arxiv.org/html/2201.12671v2
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, ISIT 2023, pp. 1294–1299, DOI:10.1109/ISIT54713.2023.10206676; Sections II, VI. https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf
3. J. Chrisnata et al., *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications 17 (2023), 960–978, DOI:10.3934/amc.2021032. https://www.aimsciences.org/article/doi/10.3934/amc.2021032
