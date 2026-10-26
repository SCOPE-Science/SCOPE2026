# Exact palindrome-pair length spectrum of the period-doubling word

## Finding
Let \(p=0100010101000100\cdots\) be the right-infinite binary fixed point of \(\sigma(0)=01\), \(\sigma(1)=00\). A *palindrome pair* is a concatenation of two palindromes; either palindrome may be empty. For every integer \(n\ge1\), **every** contiguous length-\(n\) factor of \(p\) is a palindrome pair if and only if the odd part of \(n\) is one of \(1,3,5\):
\[
\bigl(\forall i\ge0:\ p[i..i+n-1]=uv,\ u=u^{\mathrm{rev}},\ v=v^{\mathrm{rev}}\bigr)
\quad\Longleftrightarrow\quad
\frac{n}{2^{\nu_2(n)}}\in\{1,3,5\}.
\]
In particular, infinitely many lengths have the universal palindrome-pair property, whereas every odd part outside \(\{1,3,5\}\) forces at least one non-palindrome-pair factor.

## Assumptions and scope
All words are over \(\{0,1\}\); positions are zero-indexed. Factors are contiguous. Palindromes include the empty word. \(\nu_2(n)\) is the exponent of \(2\) in \(n\). The predicate concerns **all** factors of a fixed length in the specified infinite word; it does not concern arbitrary words or the number of distinct palindrome-pair factorizations. A *palindromic periodicity* in the cited work is a factor that is a sufficiently long prefix of a periodic repetition of two palindromes; any palindrome pair itself is a palindromic periodicity, but not conversely.

## Proof
**1. Reflection characterization.** A nonempty finite word \(w\) is a palindrome pair if and only if a cyclic rotation of \(w\) equals its reversal. Indeed, writing \(w=uv\) with \(u,v\) palindromes gives \(w^{\mathrm{rev}}=vu\), a rotation. Conversely, a reflection axis of the cyclic word partitions it into two (possibly empty) palindromic arcs; hence \(w=uv\) with each arc a palindrome. Therefore the predicate is invariant under cyclic rotation.

**2. Exact desubstitution.** For **every** finite binary word \(w=w_0\cdots w_{m-1}\), the word \(\sigma(w)\) of length \(2m\) has symbol \(0\) at each even position and symbol \(1-w_j\) at position \(2j+1\). A cyclic reflection has form \(t\mapsto c-t\pmod{2m}\). When \(c\) is even, it preserves parity; its action on odd positions corresponds to a cyclic reflection \(j\mapsto c/2-j-1\pmod m\), so \(\sigma(w)\) is reflection-invariant precisely if \(w\) is. If \(c\) is odd, it interchanges even and odd positions; invariance requires every odd-position symbol to be \(0\), so \(w=1^m\), already a palindrome. Conversely, any reflection of \(w\) lifts to an even-axis reflection of \(\sigma(w)\). Thus \(w\) is a palindrome pair if and only if \(\sigma(w)\) is.

**3. Length doubling.** Since \(p=\sigma(p)\), every length-\(2m\) factor of \(p\) beginning at an even position has form \(\sigma(w)\) for some length-\(m\) factor \(w\) of \(p\). Every such factor beginning at an odd position is a one-symbol cyclic rotation of \(\sigma(v)\) for a length-\(m\) factor \(v\) of \(p\). Each \(\sigma(w)\) occurs in the fixed point, and cyclic rotations do not affect the palindrome-pair property. Hence **all** length-\(2m\) factors are palindrome pairs exactly when **all** length-\(m\) factors are. Repeatedly removing powers of two reduces the theorem to odd lengths.

**4. Small odd lengths.** The complete occurring factor sets at lengths \(1\), \(3\), \(5\) are respectively

- `0`, `1`;
- `000`, `001`, `010`, `100`, `101`;
- `00010`, `00100`, `00101`, `01000`, `01010`, `10001`, `10100`, `10101`.

Every word in these three sets is a palindrome pair, checked directly by a palindromic split. Completeness follows by exhibiting the words in a finite substitution iterate and comparing their cardinalities with the established period-doubling factor-complexity formula quoted in Step 5 (its elementary small-length values agree). At length \(7\), the occurring words `1000101` and `1010001` fail the reflection criterion (neither reversal is any cyclic rotation), so the universal predicate is false. Doubling propagates this failure to odd part \(7\) at all larger corresponding lengths.

**5. Exclusion of every other odd part.** Let \(q(n)\) be the total number of distinct length-\(n\) factors of \(p\), and let \(f(n)\) count the distinct length-\(n\) factors that are palindromic periodicities. The established factor-complexity formula (see references) and Fici–Shallit–Simpson's exact period-doubling palindromic-periodicity count (Theorem 13 of the CPM 2025 paper) give, for \(n\ge8\), \(n=2^k+r\), \(k\ge3\), \(0\le r<2^k\):
\[
q(n)=\begin{cases}3\cdot2^{k-1}+2r,&0\le r\le2^{k-1},\\2^{k+1}+r,&2^{k-1}<r<2^k,\end{cases}
\]
\[
f(n)=\begin{cases}
3\cdot2^{k-1},&0\le r<2^{k-2},\\
2^{k+1},&2^{k-2}\le r<2^{k-1},\\
6\cdot2^{k-1}-r,&2^{k-1}\le r<3\cdot2^{k-2},\\
7\cdot2^{k-1}-r,&3\cdot2^{k-2}\le r<2^k.
\end{cases}
\]
Direct subtraction in the four ranges shows \(f(n)=q(n)\) precisely for \(r\in\{0,2^{k-2},2^{k-1},3\cdot2^{k-2}\}\), i.e. odd part \(\in\{1,5,3,7\}\). For all other \(n\ge8\), \(f(n)<q(n)\), so some factor is not even a palindromic periodicity and consequently is not a palindrome pair. When \(n\) is odd and \(n\ge9\), its odd part is \(n\) and is outside the four listed possibilities. Combining Steps 3–5 proves the characterization for every \(n\ge1\). \(\square\)

## Verification
The included standard-library-only script `verify.py` constructs the word independently from the morphism and the \(2\)-adic parity expression \(p_i=\nu_2(i+1)\bmod2\). It checks the complete factor languages at lengths \(1\)–\(160\) against the known complexity formula; computes the palindrome-pair property both by splitting into two palindromes and by cyclic reflection; confirms exact morphic preservation for all binary words of lengths \(1\)–\(12\); tests the published count-formula implication through \(32768\); and reproduces the length-\(7\) exceptional factors. These are independent finite checks, **not** an exhaustive proof for infinitely many lengths; the proof relies on the unrestricted morphism lemma and the explicitly cited exact literature formula.

## Relationship to prior work
Borchert and Rampersad introduced and investigated the natural question of infinitely many lengths for which every factor is a palindrome pair, establishing results for Sturmian and Thue–Morse words. The present theorem gives the complete length spectrum for the period-doubling word instead. The 2024 preprint and 2025 published theorem of Fici, Shallit, and Simpson determine a **larger** class, the palindromic periodicities, and give the exact counts used in Step 5. That result alone does **not** settle the palindrome-pair property at lengths with odd part \(7\): these length classes are entirely palindromic periodicities, but the exhibited factors are not palindrome pairs. The additional reflection/desubstitution argument and sharp exceptional family supply the missing classification. The known factor-complexity formula is used as a quoted input, not claimed as new.

## Limitations
The result is for this specific one-sided period-doubling fixed point and concerns a universal property of each factor length, not factorization multiplicities. It uses previously proved exact factor counts; re-proving those count theorems is outside its scope. Historic priority against inaccessible or unindexed literature has not been certified. Independent review has not been performed.

## References
1. A. Borchert and N. Rampersad, *Words with many palindrome pair factors* (2015), arXiv:1509.05396, https://arxiv.org/abs/1509.05396 .
2. G. Fici, J. Shallit, J. Simpson, *Some Remarks on Palindromic Periodicities* (2024), arXiv:2407.10564, https://arxiv.org/abs/2407.10564 .
3. G. Fici, J. Shallit, J. Simpson, *On Palindromic Periodicities*, CPM 2025, Theorem 13, DOI 10.4230/LIPIcs.CPM.2025.11, https://doi.org/10.4230/LIPIcs.CPM.2025.11 .
4. OEIS A275202, period-doubling subword complexity, https://oeis.org/A275202 .
