# Exact non-overlapping greedy LZ parsing of finite ternary Cantor words

## Finding
Let \(C_0=1\) and \(C_{k+1}=C_k0^{3^k}C_k\), equivalently iterate the uniform substitution \(1\mapsto101\), \(0\mapsto000\). Use the *non-self-referential greedy longest-previous-factor parsing*: at offset \(i\), consume the longest nonempty prefix of the unparsed suffix occurring wholly within the preceding prefix of length \(i\); consume one literal symbol if no such occurrence exists. A source starting at \(s\) is admissible for a phrase of length \(\ell\) only if \(s+\ell\le i\). Sources need not be unique.

For every integer \(k\ge1\), the number of phrases in this parsing of \(C_k\) is exactly \(3k\); \(C_0\) has one phrase. In addition, *every phrase head and phrase length* is given explicitly below. The first five phrases of the infinite fixed point have zero-based \((\mathrm{start},\mathrm{length})\) pairs
\[
(0,1),(1,1),(2,2),(4,1),(5,3).
\]
For each integer \(j\ge1\) with \(q=3^{j-1}\), three subsequent phrases have pairs
\[
(8q,4q),\qquad(12q,3q),\qquad(15q,9q).
\]
For \(k\ge2\), the parsing of \(C_k\) comprises the five initial phrases, these full triples for \(1\le j\le k-2\), and one final truncated phrase with pair \((8\cdot3^{k-2},3^{k-2})\). For \(k=1\) the length-three word is parsed as three single characters.

## Assumptions and scope
The alphabet is \(\{0,1\}\); indices start at zero and all powers have integral nonnegative exponents. The specified longest-previous-factor *reproductive* convention permits only nonoverlapping references entirely preceding the phrase. This is not the shortest-new-phrase/exhaustive Lempel–Ziv history, and is not the LZ77 variant that permits self-references to overlap the phrase being decoded. An exact phrase count is asserted only for the finite substitution iterates \(C_k\), not every prefix length or every compression convention. \(C_k\) is the length-\(3^k\) prefix of the one-sided infinite fixed point \(c\).

## Proof
**1. Digit model and aligned blocks.** The fixed point satisfies \(c(n)=1\) if and only if every base-three digit of the nonnegative integer \(n\) is either \(0\) or \(2\). Indeed, \(c(3m)=c(m)\), \(c(3m+1)=0\), \(c(3m+2)=c(m)\), with \(c(0)=1\). For every \(q=3^{j-1}\) and integer \(m\ge0\), the aligned length-\(q\) block beginning at \(mq\) is either \(C_{j-1}\) or \(0^q\), according as \(c(m)=1\) or \(c(m)=0\). The first twenty-five coarse symbols are
```
1010001010000000001010001
```
In particular, the blocks at coarse indices \(0,2,6,8,18,20,24\) are copies of \(C_{j-1}\), and those at indices \(3,4,5,9,10,11,12,13,14,15,16,17,19,21,22,23\) are zero blocks. The initial three-letter coarse prefix in blocks \(0,1,2\), and similarly in blocks \(6,7,8\), is exactly \(C_j\).

**2. Direct initialization.** At the first eight positions of the fixed point \(10100010\ldots\), exhaustive comparison with the strictly earlier substring gives successive phrase pairs \((0,1),(1,1),(2,2),(4,1),(5,3)\). At start two, \(10\) occurs at start zero but the following characters disagree; at start four, \(0\) occurs before but the prefix contains no earlier \(00\); at start five, \(010\) occurs at start one but \(0101\) does not occur wholly before start five. Thus the next unparsed offset is eight.

**3. The first phrase of a scale.** Fix \(q=3^{j-1}\). At head \(8q\), the length-\(4q\) target is \(C_{j-1}0^{3q}\), the same as the source at \(2q\) (coarse blocks \(2,3,4,5\)); its source ends at \(6q<8q\). Immediately after these \(4q\) symbols the target is still zero, so an extension by one would include a consecutive run of at least \(3q+1\) zeros. In the whole prefix preceding \(8q\), no run of more than \(3q\) zeros exists: its zero blocks occupy coarse indices \(1\), \(3,4,5\), and \(7\), with blocks of \(C_{j-1}\) beginning and ending in one. Thus no earlier source can provide the extra symbol, establishing exact phrase length \(4q\).

**4. The second phrase of a scale.** At head \(12q\) the next \(3q\) symbols are all zero, previously occurring at \(9q\), whose source ends at the phrase head. The preceding prefix \([0,12q)\) has no run of \(3q+1\) zeros: its maximal run is \(3q\) (coarse indices \(3,4,5\) or \(9,10,11\)). Hence this phrase has exact length \(3q\).

**5. The third phrase of a scale.** At head \(15q\), the next \(9q\) symbols have coarse pattern \(000101000\), identical to the blocks at \(3q\) through \(12q\), so the source at \(3q\) supplies a length-\(9q\) admissible match. Suppose a match of length \(9q+1\) existed wholly before head \(15q\), from source \(s\le6q-1\). The target includes \(C_j\) in its offset-\(3q\) segment \([18q,21q)\), so the source would contain \(C_j\) at \(s+3q\). But the only occurrences of \(C_j\) beginning before \(15q\) are at zero and \(6q\): since \(C_j\) begins and ends in one, both endpoint positions of such a length-\(3q\) occurrence must lie in the only available one-bearing coarse triples \([0,3q)\) or \([6q,9q)\). These endpoint constraints force the beginning to be zero or \(6q\), where \(C_j\) indeed occurs. Because \(s\ge0\), the equation \(s+3q\in\{0,6q\}\) forces \(s=3q\). Yet the next symbol at source offset \(12q\) is zero whereas the next target symbol at \(24q\) is one, contradicting the extended match. Hence the third phrase has exact length \(9q\).

**6. Scale induction and finite truncation.** The three proven phrases partition \([8q,24q)\) and end exactly where the first phrase at the next scale \(3q\) begins, because \(24q=8(3q)\). Thus the initialization and repeating triples constitute the entire infinite greedy parse. For each \(k\ge2\), the prefix \(C_k\) ends at \(9\cdot3^{k-2}\). All triples through \(j=k-2\) lie entirely before the final head \(8\cdot3^{k-2}\); that last head has exactly \(3^{k-2}\) symbols remaining and its longer infinite phrase is therefore truncated to that length. Consequently the number of phrases is \(5+3(k-2)+1=3k\). The cases \(k=0,1\) were noted directly. This proves the exact count and all asserted phrase boundaries.

## Verification
A standalone `checker.py` constructs each \(C_k\) directly from its defining recurrence, then independently determines the next phrase by testing all strictly previous source positions and nonoverlap constraints. It checks complete phrase lists and counts for \(0\le k\le7\). It additionally checks the claimed aligned source witnesses for every full scale occurring at the inspected lengths. It is a finite regression test; the unrestricted claim rests on the preceding digit/zero-run arguments and not on extrapolation.

## Relationship to prior work
Constantinescu and Ilie (2007) classified asymptotic growth of Lempel–Ziv complexity for fixed points of morphisms, including logarithmic behavior for nonperiodic fixed points of uniform morphisms, and distinguished exhaustive from maximally reproductive histories. Their analyzed examples include an exact Fibonacci formula, but the inspected article does not state an exact nonoverlapping greedy factorization of these Cantor iterates. Kärkkäinen, Kempa and Puglisi (2013) describe LZ parsing and longest previous factors algorithmically rather than proving an exact Cantor-word parse. Cassaigne et al. (2024) discuss LZ-based and attractor-based complexity for morphic words, cite the asymptotic morphic theorem, and study different invariants, without listing this exact parse. The exact coefficient and complete scale-by-scale phrase decomposition are the contributions assessed here. No claim of novelty for logarithmic growth itself or the general LZ machinery is made.

## Limitations
The statement depends on the nonoverlapping greedy parsing definition. It does not establish the exact counts for the original exhaustive Lempel–Ziv history, for an overlapping-reference compressor, or for prefixes at arbitrary lengths. Earlier literature under another terminology remains a possible historical-priority risk; no independent audit was performed.

## References
1. S. Constantinescu and L. Ilie, *The Lempel–Ziv Complexity of Fixed Points of Morphisms*, SIAM Journal on Discrete Mathematics **21** (2007), 466–481, doi:10.1137/050646846. Author's full text: https://www.csd.uwo.ca/~ilie/SIDMA07.pdf
2. J. Kärkkäinen, D. Kempa and S. J. Puglisi, *Lempel-Ziv Parsing in External Memory*, arXiv:1307.1428v1, first public 2013-07-04, https://arxiv.org/html/1307.1428v1
3. J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino and M. Stipulanti, *New string attractor-based complexities for infinite words*, Journal of Combinatorial Theory A **208** (2024), 105936, doi:10.1016/j.jcta.2024.105936. Author manuscript: https://orbi.uliege.be/handle/2268/309672
