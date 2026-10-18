# Shortest unique factors of finite Rudin–Shapiro words

## Finding

Let \(r(i)\in\{0,1\}\) be the parity of the number of (overlapping) occurrences of `11` in the ordinary binary representation of \(i\), with \(r(0)=0\). Write \(R_n=r(0)\cdots r(2^n-1)\). For every integer \(n\ge9\), the shortest length of a contiguous word occurring exactly once in \(R_n\) is
\[
\ell_n=2^{n-5}+2.
\]
Exactly eight distinct factors have this length and multiplicity one. With zero-based indexing, their occurrence starts are precisely
\[
P_n=\{a2^{n-5}-1:a\in\{11,12,13,14,23,24,25,26\}\}.
\]
No shorter factor occurs exactly once. The theorem does not assert the classification for orders below nine, although the checker explores some larger orders.

## Assumptions and scope

A factor is a *contiguous* substring; occurrences are counted by starting positions, including overlapping occurrences. A factor is *unique* if the number of its occurrences in the specified finite word is exactly one. The word \(R_n\) is the prefix of length \(2^n\) of the binary Rudin–Shapiro sequence specified above. All positions are zero-based. Every statement here concerns integer \(n\ge9\). No stochastic or asymptotic assumption is used.

## Proof

**1. Binary decimation and four aligned blocks.** The defining adjacent-`11` parity gives, for every nonnegative integer \(j\),
\[
r(2j)=r(j),\qquad r(2j+1)=r(j)\mathbin{\oplus}(j\bmod2),
\]
where \(\oplus\) is XOR. Thus \(R_{n+1}\) is obtained from \(R_n\) by replacing the letter \(r(j)\) at parent index \(j\) by the pair \((r(j),r(j)\oplus(j\bmod2))\). Repeating the identities three times shows that the eight consecutive output letters beginning at \(8j\) depend only on \((r(j),j\bmod2)\):

| \((r(j),j\bmod2)\) | Eight-letter block |
|---|---|
| \((0,0)\) | `00010010` |
| \((0,1)\) | `00011101` |
| \((1,0)\) | `11101101` |
| \((1,1)\) | `11100010` |

Call these four words the *aligned blocks*. Exhaustively inspecting the \(4\cdot4\cdot8=128\) eight-letter windows at offsets \(0,\ldots,7\) in concatenations of two arbitrary aligned blocks produces 56 distinct windows, and no window is seen at two different offsets. This is a finite lemma certified directly by `rs_unique_check.py` (the loops over the four blocks and eight offsets require no assumptions about which concatenations actually occur). Consequently, **any two equal factors of the infinite Rudin–Shapiro word of length at least eight start at indices congruent modulo eight**. The same is true inside any \(R_n\).

**2. Repetition of all very short factors.** The state of an aligned block records the parity of the block index, so any three successive aligned blocks come from one of the 16 parity-alternating state triples. Every factor of length 14 in the infinite sequence is a substring of one such 24-letter triple: its start offset is between zero and seven. The 16 triples yield precisely 104 distinct length-14 factors. The independent finite scan in `rs_unique_check.py` verifies that *all* 104 factors have at least six occurrences already in \(R_{10}\). Hence every factor of length at most 14 of any \(R_n\), \(n\ge10\), occurs at least twice in \(R_{10}\). Indeed, extend any such short factor to a length-14 factor of the infinite word and select its at least six occurrences in the prefix. The claim applies even to a factor initially encountered at the right endpoint of a finite prefix.

**3. Exact occurrence correspondence under one decimation.** Fix \(n\ge9\), and consider a factor \(X\) of \(R_{n+1}\) of length \(k\ge15\), starting at \(2p\) or \(2p+1\). In the even-start case it is determined by the contiguous parent factor of \(R_n\) beginning at \(p\) and having length \(\lceil k/2\rceil\). In the odd-start case the corresponding parent factor has length \(\lfloor k/2\rfloor+1\). Both parent lengths are at least eight. For an even start, the first bit of each complete output pair is the parent bit; for an odd start, its initial bit is the second bit of the first output pair and the final bit (when present) is the first bit of the last pair. By Step 1, the observed length-eight prefix of \(X\) fixes the start residue modulo eight, so it fixes the parity of \(p\). This makes even the partial endpoint pairs uniquely decodable using the XOR identity of Step 1. Thus equal child factors necessarily decode to equal parent factors.

Conversely, any two occurrences of the same decoded parent factor start at parent indices congruent modulo eight, by Step 1 and the fact that its length is at least eight. The pair rule above then gives identical child factors in the prescribed start parity at both occurrences, with no boundary truncation because the entire decoded parent factor fits in \(R_n\). It follows that **the occurrence count of \(X\) in \(R_{n+1}\) equals the occurrence count of its decoded parent factor in \(R_n\)**. All occurrences of \(X\) have the same starting parity by eight-offset recognition, so no extra child occurrences have been omitted.

**4. Finite base.** The exact scan of all contiguous factors of \(R_9\), which has 512 letters, gives no singleton factor of length below 18. At length 18 there are exactly eight singleton factors, at the starting indices
\[
P_9=\{175,191,207,223,367,383,399,415\}.
\]
The supplied self-contained checker enumerates every factor at all smaller lengths, counts occurrences by equality of the factor text, and lists the singleton starts; it is an exhaustive finite proof for this fixed word. The same checker separately verifies the block-offset certificate and short-factor saturation stated above. Its successful output is included as `rs_unique_output.txt`.

**5. Induction.** Suppose the least singleton length of \(R_n\) is \(\ell_n\ge18\), with singleton starts \(P_n\). Consider \(R_{n+1}\). No factor of length at most 14 is a singleton by Step 2. For a factor of length \(15\le k<2\ell_n-2\), both possible decoded parent lengths from Step 3 are strictly less than \(\ell_n\). Its parent factor therefore occurs at least twice in \(R_n\), and Step 3 gives at least two child occurrences. At length \(2\ell_n-2\), every even-start child factor decodes to \(\ell_n-1\) parent symbols and is repeated. Every odd-start child factor decodes to exactly \(\ell_n\) parent symbols and is unique if and only if that parent factor is unique. Therefore the minimum singleton length in \(R_{n+1}\) is exactly \(2\ell_n-2\), and the complete set of singleton starts is
\[
P_{n+1}=\{2p+1:p\in P_n\}.
\]
Solving the length recurrence with \(\ell_9=18\) yields \(\ell_n=2^{n-5}+2\). Since \(P_9=\{16a-1:a\in\{11,12,13,14,23,24,25,26\}\}\), the position recurrence yields the stated formula and exactly eight singletons for every \(n\ge9\).

## Verification

Run `python3 rs_unique_check.py` from the directory containing the supplied verification file, using a standard Python 3 installation. The checker calculates \(r(i)\) directly as the parity of the bits in \(i\mathbin{\&}(i\gg1)\) and independently performs the finite frequency scans at orders nine through twelve. It checks the eight-block table, every offset of every two-block concatenation, all sixteen parity-alternating block triples, the 104 fourteen-letter factors, and their multiplicities inside the first 1024 letters. It prints `ALL CHECKS PASS` upon success. The finite scan certifies the base and the finite lemmas only; the induction in Step 5 supplies the proof for unbounded orders.

## Relationship to prior work

The 2026 work *Faster Algorithms for Shortest Unique or Absent Substrings* establishes general algorithms to find shortest unique factors of arbitrary strings, but does not classify the Rudin–Shapiro family or imply the eight exact positions without a family-specific analysis. The 2026 work *On Occurrence-Preserving Morphisms* studies occurrence-preserving substitutions and applies them to Fibonacci and Thue–Morse words, rather than the parity-indexed binary Rudin–Shapiro decoding here. The 2026 work on Thue–Morse attractors also examines unique factors but has a different sequence, morphism, and parameter. Available earlier Rudin–Shapiro attractor calculations address minimum sets of factor-hitting positions, which do not determine singleton-factor multiplicities. The new result is the exact all-order shortest-unique-factor length and position classification for the stated Rudin–Shapiro prefixes.

## Limitations

No claim of independent audit or machine proof is made. Exhaustive computational checks cover finitely many orders and bounded finite lemmas; the general assertion relies on the displayed mathematical induction. The examination of publicly discoverable literature and related mathematical records does not exclude all unindexed or differently phrased equivalent results. No conclusion is drawn about other definitions of the Rudin–Shapiro sequence, alternate prefix lengths, or all longer minimal unique substrings.

## References

1. P. Charalampopoulos, M. Mohamed, S. P. Pissis, H. Verbeek and W. Zuba, *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826, first posted 2026-05-06, https://arxiv.org/abs/2605.04826.
2. K. Kishi, P. Guo, C. Urbina and H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034, first posted 2026-05-18, https://arxiv.org/abs/2605.18034.
3. S. Faro, F. P. Marino and A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950, first posted 2026-10-07, https://arxiv.org/abs/2610.10950.
