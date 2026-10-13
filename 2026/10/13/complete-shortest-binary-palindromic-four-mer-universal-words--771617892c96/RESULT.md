# Complete shortest binary palindromic four-mer universal words

## Finding

There are precisely **six** shortest binary palindromes that contain every one of the sixteen length-four binary words as a consecutive substring. Their common minimum length is **24**. With positions distinguished and symbols fixed, the full list in lexicographic order is:

```
000010110011110011010000
000011001011110100110000
000011010011110010110000
111100101100001101001111
111100110100001011001111
111101001100001100101111
```

The six solutions form three classes under simultaneous interchange of 0 and 1. **The minimum length itself is not asserted to be new**: it is already implied by the unoriented de Bruijn graph parity argument and the explicit order-four construction in Burris--Motta--Shipman (2016). The equality-case classification, i.e. exactly six words and their explicit complete list, is the asserted contribution.

## Assumptions and scope

Let \(\Sigma=\{0,1\}\). A word \(W=w_1\cdots w_L\in\Sigma^L\) is a *palindrome* when \(w_i=w_{L+1-i}\) for all \(1\le i\le L\). It is a *four-mer cover* when each of the sixteen words in \(\Sigma^4\) occurs as a contiguous, non-wrapping length-four factor of \(W\). Positions are indexed and the two symbols are fixed; rotation, complementation and reversal are not quotient identifications in the count. A repeated factor is allowed, and no cyclic wraparound is used.

## Proof

**Lower bound.** Reversal partitions the sixteen four-mers into ten orbits: four fixed (palindromic) words and six pairs. The corresponding undirected reflected de Bruijn multigraph has vertices the six reversal classes of three-mers, labeled \(000,001,010,011,101,111\), and one edge for each four-mer orbit, joining the classes of its three-letter prefix and suffix. Loops contribute two to degree. Directly from the ten edge labels \(0000,0001,0010,0011,0101,0110,0111,1001,1011,1111\), its respective degrees are \(3,5,2,5,2,3\). Thus it has four odd-degree vertices and no Euler trail through each edge exactly once.

A length-\(L\) palindrome has \(L-3\) four-mer occurrences in mirror-related positions. Hence it cannot realize all ten reversal orbits with \(L\le21\). For \(L=22\), the first ten of its nineteen factor positions contain one representative of every required orbit, with no repetition. For \(L=23\), the first ten of twenty factor positions do likewise. (Mirroring maps the other factor positions to these ten.) Either case would yield an Euler trail of the ten distinct edges in the reflected de Bruijn multigraph, contradicting the four odd vertices. Therefore \(L\ge24\).

**Complete equality cases.** Every palindrome of length 24 has the form \(W=U\operatorname{rev}(U)\) for a unique twelve-bit word \(U\). Let \(P\) be the length-fourteen prefix of \(W\). Its last four bits form a palindrome, and the eleven consecutive four-mer factors of \(P\) represent every reversal orbit if and only if \(W\) contains all sixteen four-mers: each factor in the prefix has its reversal in the reflected suffix. Conversely, any length-fourteen word \(P\) with a palindromic final four-mer arises from the unique \(U=P_1\cdots P_{12}\), and the same orbit-covering condition is sufficient.

This converts equality-case classification to a complete, finite state enumeration of \(2^{14}=16384\) possible prefixes. The accompanying `verify_orbit_dp.py` starts at the eight length-three prefixes and appends eleven bits. Each state records the last three bits and a ten-bit mask of reversal-orbit coverage, retaining exact representatives. Transitions append a bit and mark the newly formed four-mer's orbit. After length fourteen, retain only states with all ten orbit bits set and a palindromic final four-mer. Exactly six distinct prefixes survive and yield the six displayed words. Since every prefix is generated once and every palindrome corresponds to exactly one such prefix, this proves that the list is complete. The first displayed word gives existence at the lower bound. \(\square\)

## Verification

Run `python3 verify_orbit_dp.py` to reproduce the ten-orbit prefix enumeration. It reports `ORBIT_DP_OK`, 1,382 final dynamic-programming states, 16,384 length-fourteen prefixes, and six solutions. Independently run `python3 verify_direct.py`; it generates every palindrome of each length from 4 through 24 using its first half and tests its full factor set directly against all sixteen four-mers. It reports `DIRECT_OK`, no shorter covering palindrome, and exactly the six displayed words at length 24. Both programs use only the Python standard library. The graph-degree obstruction provides a noncomputational minimum-length proof; finite enumeration supplies the exhaustive equality-case count.

## Relationship to prior work

Burris, Motta and Shipman (2016), *An Unoriented Variation on de Bruijn Sequences*, establish the unoriented de Bruijn multigraph framework, the four-odd-vertex obstruction at binary order four, and a length-fourteen example `00001100101111` with one repeated reversal orbit. Reflecting such a length-fourteen covering prefix gives a length-twenty-four palindrome, so the **length 24 bound and existence are already derivable from their results**. Their article does not state or classify all six optimal *palindromic* completion words.

Anisiu, Anisiu and Kása study which palindromic factors occur in finite words; this differs from requiring a globally palindromic word to contain **all**, including nonpalindromic, factors. Orenstein and Shamir study shortest reverse-complement k-mer covers motivated by double-stranded DNA, not the stated ordinary-reversal palindrome requirement. Orenstein's reverse de Bruijn paper concerns coverage using a sequence read in both directions; the accessible abstract does not establish the complete palindrome equality cases, but its complete text could not be assessed, leaving bibliographic uncertainty.

## Limitations

This is an exact finite four-mer classification, not a formula for all factor lengths or alphabets. The six sequences are indexed linear words, not cyclic equivalence classes. The finite-count certificate is independently checkable by running either supplied program, but no independent external scientific audit is claimed. An earlier unindexed enumeration, or a table in an inaccessible related full text, remains possible.

## References

1. M.-C. Anisiu, V. Anisiu and Z. Kása, *Properties of palindromes in finite words*, Pure Math. Appl. 17 (2006), 183--195; public arXiv submission 2010-02-13, arXiv:1002.2723.
2. H. Orenstein and R. Shamir, *Design of shortest double-stranded DNA sequences covering all k-mers*, Bioinformatics (2013), DOI:10.1093/bioinformatics/btt230.
3. C. S. Burris, F. C. Motta and P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480 (public 2016-08-30), especially Theorem 4.3 and Section 5.
4. Y. Orenstein, *Reverse de Bruijn: Utilizing Reverse Peptide Synthesis to Cover All Amino Acid k-mers*, J. Comput. Biol. (2020), DOI:10.1089/cmb.2019.0448; abstract inspected, full text not assessed.
