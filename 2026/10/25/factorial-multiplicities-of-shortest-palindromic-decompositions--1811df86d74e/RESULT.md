# Factorial multiplicities of shortest palindromic decompositions of Zimin prefixes

## Finding
Let \(Z=z_1z_2\cdots\) be the infinite word over positive integers defined by \(z_j=1+\nu_2(j)\) for \(j\ge1\), where \(\nu_2(j)\) is the exponent of two dividing \(j\). This is the limit of the Zimin words \(Z_0=\varepsilon\) and \(Z_{k+1}=Z_k(k+1)Z_k\). Write \(G(n)=n\mathbin{\mathrm{xor}}\lfloor n/2\rfloor\), where `xor` denotes bitwise exclusive-or; put \(r(n)=\operatorname{popcount}(G(n))\).

**Theorem.** For every \(n\ge0\), the minimum number of nonempty palindromes in a concatenation equal to \(Z[1..n]\) is \(r(n)\). Moreover the number \(T(n)\) of *ordered* optimal palindrome factorizations (different cut-position lists counted separately) is
\[
T(n)=\left\lceil\frac{r(n)}2\right\rceil!\left\lfloor\frac{r(n)}2\right\rfloor!.
\]
For \(n=0\), the empty word has one empty factorization. Since \(r(n)\) is the number of binary digit runs of \(n>0\), the new point is the exact count of optimal decompositions, not the previously known minimum length.

## Assumptions and scope
All words are contiguous, with positions numbered from one. A palindrome is unchanged by reversal. Only nonempty factors are permitted for \(n>0\); factorizations are ordered partitions of the fixed prefix, not factorizations modulo permutations or word equality. The alphabet symbols in \(Z\) are distinct positive integers. The Gray map \(G\) acts on arbitrary nonnegative integers with leading zero bits and has an inverse on nonnegative integers. No length restriction on \(n\) is imposed.

## Proof
**1. Exact palindrome intervals.** A nonempty factor \(Z[a+1..b]\), with integers \(0\le a<b\), is palindromic if and only if its length is odd and there are unique integers \(m\ge1\), \(k=\nu_2(m)\), and \(0\le s<2^k\) with \(a+1=m-s\) and \(b=m+s\). Indeed adjacent letters have different valuations, eliminating even palindromes. For a center \(m\), the equality \(\nu_2(m-t)=\nu_2(m+t)=\nu_2(t)\) holds for every \(0<t<2^k\), proving all indicated intervals palindromic. If \(s\ge2^k\), either the proposed factor extends beyond the left end of the word (when \(m=2^k\)), or comparison of the letters at distance \(2^k\) from \(m\) fails: \(m-2^k=2^{k+1}q\) and \(m+2^k=2^{k+1}(q+1)\) for \(q\ge1\), which have different valuations.

**2. Palindromes are precisely forward Gray-hypercube edges.** For an interval from step 1, \(m=2^{k+1}q+2^k\), hence
\[
a=2^{k+1}q+(2^k-1-s),\qquad b=2^{k+1}q+(2^k+s).
\]
The lower \(k+1\) bits of \(a\) and \(b\) are complementary, with all higher bits equal. Thus \(a\mathbin{\mathrm{xor}}b=2^{k+1}-1\), and linearity of the Gray map over bitwise exclusive-or gives
\[
G(a)\mathbin{\mathrm{xor}}G(b)
=(2^{k+1}-1)\mathbin{\mathrm{xor}}(2^k-1)=2^k.
\]
Conversely, if \(a<b\) and \(G(a)\mathbin{\mathrm{xor}}G(b)=2^k\), the inverse Gray map shows \(a\mathbin{\mathrm{xor}}b=2^{k+1}-1\). Their common high-bit block and complementary low bits force the displayed representation, so \(Z[a+1..b]\) is palindromic. Therefore palindrome partitions of \(Z[1..n]\) correspond *bijectively* to strictly increasing integer paths \(0=a_0<a_1<\cdots<a_t=n\) for which consecutive Gray labels differ in exactly one bit.

**3. Minimum length and optimal paths.** Such a path is a walk in the Boolean hypercube from \(G(0)=0\) to \(G(n)\). At least \(r(n)\) bit flips are necessary. Conversely, let \(k\) be the highest set bit of \(n>0\), and let \(m=2^{k+1}-1-n<n\). The Gray labels \(G(m)\) and \(G(n)\) differ only in bit \(k\); \(G(n)\) has this bit set whereas \(G(m)\) does not, so \(r(m)=r(n)-1\). Their indices satisfy \(0\le m<n\), hence the connecting factor is palindromic by step 2. Iterating produces a partition with exactly \(r(n)\) pieces. Every optimal path must flip each set bit of \(G(n)\) once and no other bit.

**4. Counting the optimal paths.** Write the set bits of \(G(n)\) as \(k_1<\cdots<k_r\). Each ordering of these \(r\) bit positions determines a unique candidate sequence of intermediate Gray labels and, by Gray inversion, a unique candidate cut list. It is valid precisely when the associated integer indices increase at each flip. Flipping Gray bit \(k\) complements exactly the binary index bits \(0,\ldots,k\) and leaves higher bits fixed. Thus that flip increases the index if and only if index bit \(k\) was zero before the flip. That bit equals the parity of the number of already flipped Gray positions strictly greater than \(k\). Hence an ordering is admissible if and only if, immediately before choosing each position, an **even** number of larger positions have already been chosen.

Let \(f(r)\) count admissible permutations of \(r\) totally ordered positions, with \(f(0)=1\). The final selected position must have an even number of greater positions in the full set; there are exactly \(\lceil r/2\rceil\) choices. Deleting that final selection leaves any admissible permutation of the remaining \(r-1\) positions (the restriction for earlier selections is unaffected), so
\[
f(r)=\lceil r/2\rceil f(r-1).
\]
Iterating yields \(f(r)=\lceil r/2\rceil!\lfloor r/2\rfloor!\). Since each valid permutation determines exactly one optimal partition, \(T(n)=f(r(n))\), as claimed. \(\square\)

## Verification
The included `verify.py` checks the formula against a separate exact palindromic-partition dynamic program on the literal word \(Z[1..500]\). That algorithm compares each candidate factor against its own reversal and computes both the minimum and its multiplicity. It does not use Gray labels to recognize palindromes. The all-length proof is the four-step argument above, not the finite test.

## Relationship to prior work
Fici, Gagie, Kärkkäinen, and Kempa (2014) prove that a length-\(n\) Zimin prefix has exactly \(\operatorname{popcount}(n)\) *palindromic suffixes* (Lemma 12), a different invariant from the number of minimum factorizations. Li (2020), Theorem 1, establishes that the minimum number of palindromes in a ruler-word prefix is the number of binary runs (equivalently \(r(n)\)); the first clause of the present theorem is therefore background, not claimed as original. The new claim is the factorial count of *all distinct optimal factorizations*, supplied by the Gray-cube path argument. The 2020 mask-based characterization of minimum lengths is compatible but does not state an optimal-factorization multiplicity formula in the inspected full article.

## Limitations
The theorem is for the infinite-alphabet Zimin/ruler word, not the binary period-doubling image obtained by taking symbols modulo two. The count concerns exact minimum-length factorizations, not all palindromic factorizations. Historical-priority search cannot exclude unpublished enumerations or every unindexed related result; no independent scientific audit has been carried out.

## References
1. G. Fici, T. Gagie, J. Kärkkäinen, D. Kempa, “A Subquadratic Algorithm for Minimum Palindromic Factorization,” arXiv:1403.2431 (first posted 2014-03-10), Lemma 12 and Theorem 13. https://arxiv.org/abs/1403.2431
2. S. Li, “Palindromic length sequence of the ruler sequence and of the period-doubling sequence,” arXiv:2007.08317 (first posted 2020-07-16), Theorem 1, Proposition 1. https://arxiv.org/abs/2007.08317
3. N. J. A. Sloane et al., OEIS A005811, number of runs of digits in binary expansion (cited in Li 2020). https://oeis.org/A005811
