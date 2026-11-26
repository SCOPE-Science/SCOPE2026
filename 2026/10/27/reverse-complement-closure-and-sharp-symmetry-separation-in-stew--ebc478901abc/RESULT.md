# Exact complement and reversal overlap spectra of Stewart words

## Finding

Let \(\mathbf s\) be any infinite binary Stewart word and let \(\mathcal L_n\) be its set of length-\(n\) contiguous factors. Let \(\overline u\) be bitwise complement and \(u^R\) reversal. The numbers of \(u\in\mathcal L_n\) with \(\overline u\in\mathcal L_n\), and of \(u\in\mathcal L_n\) with \(u^R\in\mathcal L_n\), are equal. Their common spectrum at lengths \(1,\ldots,8\) is
\[
2,4,6,6,6,6,2,0.
\]
The counts remain zero for all \(n>8\). At length seven the only factors counted are `0110110` and `1001001`; these two universal palindromes were already listed by Fici and Shallit. All comparisons are within the language of one fixed infinite word. Reverse-complement closure is used as an auxiliary fact; it follows from prior common-factor results, as explained below.

## Assumptions and scope

The directive \((p_j)_{j\ge0}\) is arbitrary, and each \(p_j\) is a permutation of `01?`. Positions are numbered from zero. If \(i=\sum_j d_j3^j\) and \(h_j\) is the index of `?` in \(p_j\), then \(\mathbf s_i=p_j[d_j]\) at the first digit \(d_j\ne h_j\). If no such digit exists at a position, that single exceptional symbol may be either bit. Factors are noncircular and are counted as distinct words, without quotienting by any symmetry.

## Proof

### The short languages

The first pattern is repeated with period three and its holes are filled by the Stewart word of the tail directive. Each window of three positions in the first pattern contains both fixed bits and one hole. For any of the three starting residues, either value occurs at the hole because the tail itself contains both bits infinitely often. Thus every length-three nonconstant binary word occurs, and there are no constant length-three words. Its length-two prefixes give all four binary pairs. These facts hold for every tail directive.

For first pattern `01?`, the three starting residues give the templates `01a01b01`, `1a01b01c` and `a01b01c0` for length eight. The letters in the holes range respectively over all pairs and all nonconstant triples from the tail. This yields the exact set \(E\):

`00100110`, `00110100`, `00110110`, `01001001`, `01001101`, `01101001`, `01101101`, `10010011`, `10011010`, `10011011`, `10100100`, `10100110`, `10110100`, `11010010`, `11010011`, `11011010`.

Cyclic shifts of the first pattern give the same set because all starting residues and the same tail languages are used. The other orientation (a cyclic shift of `10?`) gives \(\overline E\). As the word is infinite to the right, its language at length \(n\le 8\) is the set of length-\(n\) prefixes of its length-eight language. The complement comparison for prefixes of \(E\) is as follows; complementing the language leaves the counts unchanged.

| \(n\) | Prefixes whose complements also occur |
|---:|:---|
| 1 | `0`, `1` |
| 2 | `00`, `01`, `10`, `11` |
| 3 | `001`, `010`, `011`, `100`, `101`, `110` |
| 4 | `0010`, `0100`, `0110`, `1001`, `1011`, `1101` |
| 5 | `00100`, `01001`, `01101`, `10010`, `10110`, `11011` |
| 6 | `001001`, `010010`, `011011`, `100100`, `101101`, `110110` |
| 7 | `0110110`, `1001001` |
| 8 | none |

A longer complement pair would have complementary length-eight prefixes, so none occurs.

### Auxiliary symmetry (direct proof)

In the depth-\(r\) periodic skeleton, of period \(Q=3^r\), the sole hole residue is \(H=\sum_{j<r}h_j3^j\). Reflection \(i\mapsto2H-i\pmod Q\) interchanges the assigned bits and preserves the hole: at the first digit where \(i\) differs from \(H\), the map sends the digit \(d_j\) to \(2h_j-d_j\pmod 3\), interchanging the two non-hole digits. Every finite factor has a fully assigned occurrence in some finite skeleton. Indeed, take \(Q\) larger than the window; it contains at most one hole. If there is a hole, shift the window by a multiple of \(Q\) to match the bit there with one of the two filled residues at the next level. All other bits are unchanged, and a nonnegative shift can always be chosen. Reflect this resolved occurrence in its skeleton and choose a sufficiently large nonnegative representative to realize \(\overline{u^R}\) in the same infinite word.

Consequently, for each \(u\in\mathcal L_n\), \(u^R\in\mathcal L_n\) if and only if \(\overline u\in\mathcal L_n\), which transfers the entire comparison above to reversal.

## Relationship to prior work

Fici and Shallit [1, Theorems 5 and 9] already gave the two universal length-seven palindromes and the total factor complexity \(2n\). Their Theorem 10 yields reverse-complement closure as follows. For any directive, replacing each \(p_j\) by \(\overline{p_j^R}\) gives a word whose language is the reverse-complement of the original one: on each resolved window in a depth-\(r\) skeleton this transformation is reflection \(i\mapsto3^r-1-i\) combined with complement, and the resolved-occurrence argument above applies in both directions. Corresponding patterns of the two directives have Hamming distance zero or three, so Theorem 10 gives arbitrarily long common factors. Each word is uniformly recurrent, since a fully assigned occurrence repeats with its skeleton period. Arbitrarily long common factors therefore imply equal languages. For ordinary complement, corresponding patterns have Hamming distance two from the first position, and Theorem 10 gives a nonsharp upper bound of nine on common-factor length. The exact spectrum and sharp cutoff here come from the length-eight grammar, not from the total complexity or the palindrome list.

Currie et al. [2] study existence and repetition thresholds for binary words with complementary-factor avoidance, not the exact Stewart-word overlap spectrum. The older choral-sequence literature includes Noche [3]; the full text of that paper was not inspected. The exact result is specific to binary Stewart directives and does not classify all long factor sets or reverse-complement fixed points.

## Verification

`verify_stewart_symmetry.py` (Python 3, standard library only) supports the finite comparisons and illustrates the skeleton property. The exhaustive template comparison and the uniform skeleton argument above, rather than the finite-prefix tests, prove the arbitrary-directive result.

## References

1. G. Fici and J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125; *Theoretical Computer Science* 922 (2022), 1–12, doi:10.1016/j.tcs.2022.04.006.
2. J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598, doi:10.37236/11555.
3. J. R. Noche, *On Stewart’s Choral Sequence*, *Gibón* 8 (2008), 1–5.
