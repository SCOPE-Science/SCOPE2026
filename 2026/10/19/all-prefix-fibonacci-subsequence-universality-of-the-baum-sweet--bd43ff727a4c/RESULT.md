# All-prefix Fibonacci subsequence universality of the Baum–Sweet word

## Finding
Let \(b(0)=1\) and, for \(n>0\), set \(b(n)=1\) if and only if every maximal run of zero digits in the usual binary expansion of \(n\) has even length. Define the finite prefix \(W_N=b(0)\cdots b(N-1)\), its one-count \(S(N)\), and its **subsequence universality index** \(U(N)\): the largest \(k\ge0\) for which each of the \(2^k\) binary words of length \(k\) can be obtained by retaining increasing-index letters of \(W_N\).

**Theorem.** For every integer \(N\ge8\),
\[
U(N)=S(N)-2-\begin{cases}1,&N=4^j+1\text{ for some integer }j\ge2,\\0,&\text{otherwise}.\end{cases}
\]
For \(N=1,\dots,7\), the values are respectively \(0,0,1,1,1,2,2\). If \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\), then for every \(m\ge3\),
\[
S(2^m)=F_{m+2},\qquad U(2^m)=F_{m+2}-2.
\]
Hence the shortest length of a binary word missing as a scattered subsequence from \(W_N\) is exactly \(U(N)+1\), and in particular is \(F_{m+2}-1\) at dyadic cutoffs \(N=2^m\), \(m\ge3\).

## Assumptions and scope
These statements concern the standard zero-indexed Baum–Sweet word with \(b(0)=1\), the ordered binary alphabet \(\{0,1\}\), noncontiguous (scattered) subsequences, and prefixes starting at zero. No claim is made about contiguous-factor universality, arbitrary shifted windows, or the number of shortest absent subsequences. The indicator above applies exactly at \(N=17,65,257,\ldots\) and **not** at \(N=5\).

## Proof
**Lemma 1 (consecutive ones).** For integers \(n\ge0\), the pair \(b(n)b(n+1)\) equals `11` precisely when \(n=4^j-1\) for some integer \(j\ge0\).

For \(n=0\), both bits are one. Suppose \(n>0\) and \(b(n)=b(n+1)=1\). If the binary expansion of \(n\) ends in a maximal positive run of zeros of length \(2r\), incrementing it gives a final zero run of length \(2r-1\) followed by `1`, so \(b(n+1)=0\), contradiction. Therefore \(n\) ends in ones. If this trailing run is preceded by a maximal run of zeros of even length \(2r\), incrementing changes that zero run into a length-\((2r-1)\) zero run, again impossible. Thus \(n\) is an all-ones binary integer, \(n=2^t-1\), and \(n+1=2^t\) is admissible precisely when \(t\) is even. This gives \(n=4^j-1\). Conversely all such pairs are admissible, including \(j=0\). \(\square\)

**Lemma 2 (arch characterization).** For any binary finite word \(w\), scan from left to right, cutting an *arch* as soon as both letters have occurred since the previous cut. If \(a(w)\) arches are completed, then \(w\) is subsequence-universal through length \(a(w)\), and not through length \(a(w)+1\).

Any word of length \(a(w)\) embeds by selecting its \(i\)-th symbol from the \(i\)-th arch. Conversely, the last letter of each arch is the first occurrence of that symbol within that arch. Greedy matching of the sequence of these last letters therefore consumes exactly the entire arches. Append a letter absent from the unfinished final suffix (which contains at most one distinct symbol); greedy matching then fails. The greedy embedding uses the earliest possible position for each letter, so no embedding exists. Therefore \(U(w)=a(w)\). \(\square\)

**Lemma 3 (exact arch count).** For every \(N\ge8\),
\[
a(W_N)=S(N)-2-\mathbf1_{\{N=4^j+1,\ j\ge2\}}.\]

The first eight symbols are `11011001`. Their greedy arches are `110`, `110`, `01`, consuming five ones but completing three arches, with the next arch starting immediately after position seven. All later consecutive-one pairs have first positions \(4^j-1\), \(j\ge2\), by Lemma 1; these pairs are isolated from one another and followed by zero. Until such a pair, a fresh one always follows at least one zero since the previous completed arch; it therefore completes exactly one new arch. At an adjacent pair, the **first** one completes an arch that ends in one; the **second** one starts an arch that ends upon the next zero. Consequently every one beyond the first eight symbols eventually contributes exactly one additional arch, with exactly one possible unfinished contribution when the prefix ends immediately after the second one of a pair. This happens only at \(N=4^j+1\), \(j\ge2\). Counting the initial three arches against five initial ones proves the identity. \(\square\)

The main formula follows from Lemmas 2 and 3. The seven initial indices are obtained directly from the stated beginning of the word.

**Lemma 4 (Fibonacci one-count).** A positive binary integer is admissible if and only if its expansion belongs to the regular language \(1(1\mid00)^*\). A suffix of length \(r\) in \((1\mid00)^*\) can begin with `1` or `00`, so its number \(c_r\) satisfies \(c_0=c_1=1\) and \(c_r=c_{r-1}+c_{r-2}\) for \(r\ge2\). Hence \(c_r=F_{r+1}\). There are \(F_\ell\) admissible positive integers of binary length \(\ell\). Including zero, the number below \(2^m\) is \(1+\sum_{\ell=1}^m F_\ell=F_{m+2}\). \(\square\)

For \(m\ge3\), the dyadic \(N=2^m\) is never of the exceptional form \(4^j+1\). Lemma 4 and the main formula give \(U(2^m)=F_{m+2}-2\). \(\square\)

## Verification
The standalone program `bs_universality_verify.py` independently generates \(b(n)\) in two ways: literal zero-run inspection and a digit-by-digit finite automaton. It computes the universality index via greedy arches and, separately, the shortest absent subsequence length by a backwards dynamic program using next occurrences of each letter. It verifies every prefix length from one through \(2048\), selected dyadic and exceptional boundaries through \(65536\), all adjacent-one positions below \(65536\), and the Fibonacci counts at powers of two through \(2^{16}\). Run `python3 bs_universality_verify.py`; expected terminal line begins `VERIFY_OK`. These checks are finite corroboration; the theorem for arbitrary \(N\) follows from the preceding lemmas.

## Relationship to prior work
Hofman and Martens (2015) consider regular languages distinguished by short subsequences and subwords; their separability theorems concern language-theoretic decision problems, not the exact universality index of Baum–Sweet prefixes. Hébrard's arch factorization and its general connection to subsequence universality are established tools, surveyed and developed by Schnoebelen and Veron (2023, Section 2). The arch characterization is expressly used here as a known general principle. The contribution is the Baum–Sweet-specific exhaustive all-prefix formula and its rare \(4^j+1\) correction, together with the exact Fibonacci dyadic scale; a generic algorithm for computing universality on a given word does not imply those closed forms without analyzing the automatic word.

## Limitations
The exact shortest absent *length* is determined, not the number or language of missing subsequences. No new general theory of arch factorizations or regular-language separation is claimed. Unindexed equivalent work about the Baum–Sweet word remains a literature risk. Independent audit has not been performed.

## References
1. P. Hofman and W. Martens, *Separability by Short Subsequences and Subwords*, ICDT 2015, LIPIcs 31 (2015), 230–246; DOI: `10.4230/LIPIcs.ICDT.2015.230`.
2. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:`2304.11932` (first submitted 2023-04-24), especially Section 2 and its references to Hébrard's arch factorization.
3. Sage/PassageMath combinatorics reference, entry `BaumSweetWord()`, documented binary-run definition and automatic representation: `https://passagemath.org/docs/10.6/html/en/reference/combinat/sage/combinat/words/word_generators.html`.
