# Cyclic-factor fidelity and the complete circular-palindrome language of dyadic Rudin–Shapiro words

## Finding

Let \(\rho\) be the four-letter substitution
\[
\rho(0)=01,\quad\rho(1)=02,\quad\rho(2)=31,\quad\rho(3)=32,
\]
and let the binary coding \(\tau\) send \(0,1\) to \(0\), and \(2,3\) to \(1\). Define the infinite Rudin–Shapiro word \(r=\tau(\rho^\omega(0))\) and its complete dyadic prefixes \(R_k=\tau(\rho^k(0))\), for integers \(k\ge0\). Then \(|R_k|=2^k\).

**Cyclic-factor fidelity.** For every integer \(k\ge0\) and every length \(1\le\ell\le2^k\), every length-\(\ell\) factor read on the cyclic word \(R_k\) occurs as an ordinary (contiguous) factor of \(r\). In particular, closing the finite prefix into a circle creates no factor absent from the infinite word, even for cyclic factors traversing almost an entire cycle.

**Complete circular-palindrome language.** Taking distinct factor *strings* rather than occurrences, the set of all nonempty circular palindromes of \(R_k\) equals the following fixed language \(\mathcal P\) for every \(k\ge8\). The first rank with this equality is \(k=8\). There are exactly \(36\) elements of \(\mathcal P\), with maximum length \(14\). For \(k=0,1,\ldots,8\), the total distinct circular-palindrome counts are respectively \(1,2,5,12,18,23,31,34,36\).

| Length | All palindromic words of that length in \(\mathcal P\) |
| --- | --- |
| 1 | `0`, `1` |
| 2 | `00`, `11` |
| 3 | `000`, `010`, `101`, `111` |
| 4 | `0000`, `0110`, `1001`, `1111` |
| 5 | `00100`, `01110`, `10001`, `11011` |
| 6 | `010010`, `011110`, `100001`, `101101` |
| 7 | `0001000`, `0100010`, `1011101`, `1110111` |
| 8 | `00100100`, `01000010`, `10111101`, `11011011` |
| 9 | none |
| 10 | `0001001000`, `0010000100`, `1101111011`, `1110110111` |
| 11 | none |
| 12 | `000010010000`, `111101101111` |
| 13 | none |
| 14 | `01111011011110`, `10000100100001` |
| \(\ge15\) | none |

For all \(k\ge8\), the circular palindrome count at lengths \(1,2,\ldots,14\) is therefore
\[
(2,2,4,4,4,4,4,4,0,4,0,2,0,2),
\]
with zero at every larger length.

## Assumptions and scope

For a finite word \(w\) of length \(n\), a circular factor of length \(\ell\), with \(1\le\ell\le n\), is the string beginning at one of the \(n\) positions of \(ww\) and reading exactly \(\ell\) symbols. Repeated occurrences of the same string count once. A palindrome equals its reversal. A linear factor is a contiguous substring without circular wraparound. All substitutions and codings above extend to words by concatenation, and all powers of \(\rho\) have nonnegative integral exponent. The coding convention is the usual binary Rudin–Shapiro sequence, equivalently the parity of the number of overlapping `11` occurrences in the binary expansion of an index.

## Proof

**1. Finite three-block embeddings.** Put \(q=\rho^\omega(0)\). Direct substitution to depth \(4\) gives occurrences of both distinct trigrams `010` and `101` in \(q\). For any \(k\ge1\), write \(H=2^{k-1}\), and let \(A=\rho^{k-1}(0)\), \(B=\rho^{k-1}(1)\), each of length \(H\). Because \(\rho(0)=01\), the four-letter preimage of the cyclic word \(\rho^k(0)\) is the two-block cycle \(AB\).

Any circular factor of \(AB\) of length at most \(2H\), at any start offset, is contained in either \(ABA=\rho^{k-1}(010)\) or \(BAB=\rho^{k-1}(101)\). Indeed, start within one of the two length-\(H\) blocks; traversing at most \(2H\) symbols enters at most the next two blocks. Both three-letter patterns occur in \(q\), so both three-block substitutions occur in \(\rho^{k-1}(q)=q\). Thus all circular factors of \(AB\), and after applying the letterwise coding all circular factors of \(R_k=\tau(AB)\), occur linearly in \(r\). At \(k=0\), \(R_0=0\), and its only circular factor `0` already occurs in \(r\). This proves cyclic-factor fidelity with the stated quantifiers.

**2. Exhaustive local determination of all infinite palindromes.** The exact two-letter factor set of \(q\) is
\[
\mathcal D=\{01,02,10,13,20,23,31,32\}.
\]
To verify completeness, direct inspection of \(\rho^4(0)\) exhibits all eight. The four internal image digrams are `01`, `02`, `31`, `32`, and all crossing image-boundary digrams from pairs in \(\mathcal D\) lie among `10`, `13`, `20`, `23`. Thus \(\mathcal D\) is closed under one substitution, and induction shows no further digrams occur in \(q\).

The four length-\(16\) coded supertiles \(W_a=\tau(\rho^4(a))\) are

```
W_0 = 0001001000011101
W_1 = 0001001011100010
W_2 = 1110110100011101
W_3 = 1110110111100010
```

Since \(q=\rho^4(q)\), every factor of \(r\) of length at most \(16\) begins at an offset \(i\in\{0,1,\ldots,15\}\) inside some \(W_aW_b\) with \(ab\in\mathcal D\). Conversely, every such candidate factor occurs in \(r\), because every digram in \(\mathcal D\) occurs in \(q\). Therefore the following finite set computation is a complete exact characterization at all lengths at most \(16\):
\[
\{(W_aW_b)[i:i+\ell]:ab\in\mathcal D,\ 0\le i<16,\ 1\le\ell\le16,\ (W_aW_b)[i:i+\ell]\text{ is a palindrome}\}.
\]
Here the slice notation is defined by the accompanying standalone Python checker; it extracts exactly \(\ell\) symbols. Exhausting the \(8\) choices of digram, \(16\) offsets and \(16\) lengths yields exactly the \(36\) words in the Finding table, and in particular no palindromes of length \(15\) or \(16\).

Every palindrome of odd length at least \(15\) has a centered palindromic substring of length \(15\); every even-length palindrome of length at least \(16\) has a centered palindromic substring of length \(16\). Hence absence at the two lengths implies absence at all lengths \(\ge15\). The table is therefore the **complete** palindrome language of \(r\), not an enumeration truncated at \(16\).

**3. Stabilization and sharp rank.** By step 1, the circular-palindrome language of each \(R_k\) is a subset of the table \(\mathcal P\). Direct complete enumeration of the circular factors of the nine finite words \(R_0,\ldots,R_8\) gives total counts \(1,2,5,12,18,23,31,34,36\); this finite assertion is checked by the standalone code. At \(k=8\), direct enumeration additionally shows that **every** member of \(\mathcal P\) is already a *linear* factor of \(R_8\). As \(\rho(0)=01\) begins in `0`, each \(\rho^{k+1}(0)\) begins with \(\rho^k(0)\), and the binary words \(R_k\) are nested prefixes of \(r\). Consequently every member of \(\mathcal P\) occurs linearly, hence circularly, in every \(R_k\) with \(k\ge8\). Combined with the upper inclusion, equality follows for all such \(k\). The rank-\(7\) count \(34<36\) establishes sharpness. The table gives the exact lengthwise counts and maximal length.

## Verification

Run the self-contained standard-library-only script `python checker.py` from a directory containing the embedded source. The checker (i) constructs \(\rho^4(0)\), proves the eight-digram closure and the occurrence of `010`, `101`, (ii) constructs and checks all four coded supertiles, (iii) exhaustively enumerates their candidate palindromes at every length through \(16\), (iv) independently constructs each \(R_k\) for \(0\le k\le8\) from the overlapping-`11` digit-parity definition, (v) enumerates every circular palindrome for those ranks, checks the exact counts and equality at rank \(8\), and (vi) directly checks circular factor containment by the two three-block embeddings through rank \(8\). It also samples palindrome stabilization at ranks \(9,10,11\). Its success output begins `CHECK_OK`.

Steps 1 and 2 are general proofs for all ranks and lengths; no inference from a bounded rank search is used to establish the infinite quantifiers. The only finite certificates are the explicitly bounded eight-digram/local-supertiles and ranks \(0\) through \(8\) needed for the exact onset.

## Relationship to prior work

Baake's 1999 *A note on palindromicity* discusses the ordinary Rudin–Shapiro palindrome-length restriction and cites the 1997 work of Allouche. Schaeffer and Shallit's 2015 *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences* studies palindromes and maximal palindromes of automatic sequences, including Rudin–Shapiro. Their inspected relevant material concerns factors of the **infinite** word, without proving that closing *each complete dyadic finite prefix* introduces no new factors. The present two-three-block argument supplies that general cyclic-to-linear implication and, with the finite supertile characterization, the exact rank of stabilization and all distinct circular palindrome strings. The finite-rank equality and all-factor fidelity do not follow simply from the known set of allowed palindrome *lengths*.

## Limitations

The cyclic-factor containment is proved only for complete dyadic prefixes \(R_k\) under the specified four-letter substitution and coding, with circular lengths not exceeding one traversal. It is not asserted for arbitrary prefixes or other Rudin–Shapiro normalizations. The palindrome language records distinct strings, not occurrence multiplicities. The elementary local certificate can be replayed independently, but independent mathematical assessment and exhaustive historical-priority verification have not been performed. In particular, the complete text of the 1997 Allouche paper was not available during this comparison; the directly inspected 1999 treatment quotes its main ordinary-palindrome result.

## References

1. M. Baake, *A note on palindromicity*, arXiv:math-ph/9907011, first submitted 14 July 1999. https://arxiv.org/abs/math-ph/9907011
2. L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074, first submitted 9 August 2015. https://arxiv.org/abs/1508.02074
3. J.-P. Allouche, *Schrödinger operators with Rudin–Shapiro potentials are not palindromic*, Journal of Mathematical Physics 38 (1997), DOI:10.1063/1.531916. Cited for context; full text not examined.
