# Sharp three-antipower radius and dyadic exclusions in the period-doubling word

## Finding
Let \(p=p_0p_1p_2\cdots\) be the binary fixed point of \(\mu(0)=01\) and \(\mu(1)=00\), starting with \(p_0=0\). A three-antipower with block length \(m\) at position \(i\) means that the three consecutive length-\(m\) factors beginning at \(i\), \(i+m\), and \(i+2m\) are pairwise distinct. Define the least such length \(a(i)\).

**Theorem.** For every integer \(i\ge0\), one has \(a(i)\in\{3,5\}\). More precisely, \(a(i)=5\) if and only if one of the following mutually exclusive conditions holds:

- \(i=2j\) and \(p_jp_{j+1}p_{j+2}p_{j+3}\) is `0100` or `0010`;
- \(i=2j+1\) and \(p_jp_{j+1}p_{j+2}p_{j+3}p_{j+4}\) is `00100`.

The natural density of positions with \(a(i)=5\) is exactly \(5/24\), while the density with \(a(i)=3\) is \(19/24\). In addition, for every integer \(r\ge0\), **no** three-antipower in \(p\) has block length \(2^r\), regardless of its starting position. In particular, the uniform bound \(a(i)\le5\) is sharp; it cannot be replaced by four.

## Assumptions and scope
All words are one-sided, binary, and indexed from zero. Distinctness is literal equality of complete length-\(m\) blocks, not equality of their Parikh vectors or a cyclic-rotation equivalence. A fixed starting position is chosen before the block length. Densities refer to the ordinary natural density of nonnegative starting indices. The theorem applies to the specified fixed point, not to arbitrary binary morphic words.

## Proof
The substitution satisfies \(p_{2j}=0\) and \(p_{2j+1}=1-p_j\). Inductively, \(\mu^r(0)\) and \(\mu^r(1)\) have a common prefix of length \(2^r-1\), and their final letters differ. Fix \(m=2^r\) and write a starting position as \(i=qm+t\) with \(0\le t<m\). For \(t=0\), every successive length-\(m\) block is one of the two words \(\mu^r(0),\mu^r(1)\). For \(t>0\), the block beginning at \(i+hm\) is the suffix of length \(m-t\) of \(\mu^r(p_{q+h})\), followed by the prefix of length \(t\) of \(\mu^r(p_{q+h+1})\). The latter prefix is independent of its source letter. Hence every such block is a function of the single binary symbol \(p_{q+h}\). Three consecutive blocks have at most two distinct values. Thus no dyadic block length is admissible.

It remains to test block lengths three and five. We give a *finite exhaustive language argument*, rather than assuming that a long prefix empirically represents the infinite word. The adjacent two-letter factors of \(p\) are exactly `00`, `01`, and `10`: all occur in \(\mu^2(0)=\texttt{0100}\), and `11` cannot occur because every odd position is followed by an even position containing zero. The infinite word is tiled into successive aligned blocks \(\mu^4(p_j)\), each of length sixteen. Every length-fifteen factor intersects at most two neighboring blocks. Conversely every factor of \(\mu^4(ab)\), for \(ab\in\{\texttt{00},\texttt{01},\texttt{10}\}\), occurs in \(p\). Therefore the complete length-fifteen language is precisely the set of length-fifteen subwords of those three explicit 32-letter strings.

Enumerating those three strings gives exactly 23 distinct length-fifteen factors, as listed with each block test in `factors.csv`. Their length-nine prefixes are exactly fourteen words. Splitting each nine-letter prefix into three consecutive triples gives pairwise distinct triples for eleven of these fourteen words. The three exceptions are precisely `010001010`, `010100010`, and `101000101`. There are exactly four length-fifteen factors extending one of those three bad nine-letter prefixes; in each such length-fifteen factor, the three consecutive blocks of length five are pairwise distinct. Thus every starting index admits block length three or five. Since lengths one, two, and four are excluded by the dyadic argument, these are precisely the least possible lengths. At the starting position zero, the first nine letters are `010001010`, so five is needed, establishing sharpness.

The parity recurrence rewrites the three bad length-nine patterns without ambiguity. At an even start \(i=2j\), a length-nine factor has the form \(0\,(1-p_j)\,0\,(1-p_{j+1})\,0\,(1-p_{j+2})\,0\,(1-p_{j+3})\,0\). Consequently its two possible bad patterns correspond exactly to the source length-four factors `0100` and `0010`. At an odd start \(i=2j+1\), the five odd-position source-derived entries are \(1-p_j,\ldots,1-p_{j+4}\). The remaining bad pattern corresponds exactly to the source length-five factor `00100`. This proves the characterization.

For the density, the explicit formula \(p_j=\nu_2(j+1)\pmod2\), with \(\nu_2\) the exponent of two, implies that the density of ones is \(\sum_{h\ge0}2^{-2h-2}=1/3\). There are no adjacent ones; hence each of the two-letter factors `00`, `01`, and `10` has density \(1/3\). Applying the parity recurrence to source factors gives
\[
 f(\texttt{0100})=\tfrac12 f(\texttt{01})=\tfrac16,\qquad
 f(\texttt{0010})=\tfrac12 f(\texttt{10})=\tfrac16,
\]
\[
 f(\texttt{101})=\tfrac12 f(\texttt{00})=\tfrac16,\qquad
 f(\texttt{00100})=\tfrac12 f(\texttt{101})=\tfrac1{12}.
\]
These identities also prove existence of the factor frequencies used here. Exactly half of starting indices are even and half odd. Applying the already-proved exceptional-position characterization gives
\[
 \lim_{N\to\infty}\frac{\#\{0\le i<N:a(i)=5\}}{N}
 =\tfrac12\left(\tfrac16+\tfrac16\right)+\tfrac12\cdot\tfrac1{12}=\boxed{\tfrac5{24}}.
\]

## Verification
`verify.py` (Python standard library only) reconstructs the full length-fifteen factor set from the three adjacent source pairs; compares all 23 records in `factors.csv`; checks the three exceptional nine-letter prefixes and the four length-fifteen extensions; and independently reconstructs the first 65,536 symbols by the valuation-parity formula, then by the morphism. It also checks the dyadic common-prefix lemma and finite sample blocks through length \(2^{12}\). The proof above, not those finite samples, establishes both unrestricted statements.

Run `python3 verify.py` in a directory containing both `verify.py` and `factors.csv`. A successful run prints `VERIFY_OK` lines with the exhaustive sizes and identities.

## Relationship to prior work
Fici, Restivo, Silva, and Zamboni introduced antipowers and proved general existence results for nonperiodic uniformly recurrent infinite words. Berger and Defant subsequently proved a uniform linear block-length bound for antipowers starting at arbitrary positions of suitable binary uniform morphic words. Their general conclusions ensure eventual existence but do not supply the present exact minimum for three blocks, the forbidden infinite dyadic length spectrum, the characterization of all exceptional positions, or their density.

## Limitations
The theorem concerns three blocks, not arbitrary antipower order. It does not assert that all nondyadic block lengths work. Only the *least* three-antipower block length and the dyadic exclusion are classified; block-length availability beyond five is not enumerated. Historical-priority risk remains for potentially unindexed period-doubling examples and computations. The exhaustive argument relies on the displayed morphism and must not be generalized to arbitrary morphisms by analogy.

## References
1. G. Fici, A. Restivo, M. Silva, L. Q. Zamboni, *Anti-Powers in Infinite Words*, arXiv:1606.02868 (first public version 2016-06-09), https://arxiv.org/abs/1606.02868.
2. A. Berger, C. Defant, *On Anti-Powers in Aperiodic Recurrent Words*, arXiv:1902.01291 (first public version 2019-02-04), https://arxiv.org/abs/1902.01291.
