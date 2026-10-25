# Complete sharp length-eight unclustered Burrows–Wheeler images

## Finding
Fix an ordered alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\) with \(q\ge3\). A primitive necklace is a cyclic-rotation class of a word of length eight having no shorter period. Its Burrows–Wheeler transform \(L\) is the final column of the lexicographically sorted matrix of its eight rotations. A word \(L\) is *completely unclustered* when its seven neighboring pairs contain distinct symbols. A necklace has \(r\) cyclic runs when exactly \(r\) of its eight cyclicly neighboring pairs have distinct symbols.

**Theorem.** A primitive length-eight necklace with completely unclustered Burrows–Wheeler transform has the sharp minimum of **four cyclic runs** if and only if its transform is obtained by selecting strictly increasing alphabet symbols and substituting them for the digits in one of precisely six order-reduced patterns:

```
10120121   10201020   20212021
10130232   20312130   30212031
```

The first three patterns use exactly three symbols; the last three use exactly four. Among the first three, each of the three ordered Parikh profiles \((4,2,2)\), \((2,4,2)\), and \((2,2,4)\) occurs exactly once. The four-symbol patterns all have profile \((2,2,2,2)\). In particular, the **fixed-content sharpness problem** in length eight is completely solved: a positive-multiplicity profile admits a sharp completely unclustered primitive BWT if and only if, after removing zero components and retaining alphabet order, it is one of these four profiles.

Consequently, the number \(E_q\) of such necklaces over \(\Sigma_q\), with no requirement that every alphabet symbol occur, is exactly
\[
 E_q=3\binom q3+3\binom q4\qquad(q\ge3).
\]
Different BWT images correspond to different necklaces, so this counts necklaces, not representatives or rotations.

## Assumptions and scope
All finite words have length eight. Alphabet labels are ordered, and only *order-preserving* relabeling is allowed in the six-pattern classification. The lower bound of four runs and the complete list are valid for every integer \(q\ge3\); there is no assertion about longer words, other order types, or cyclic output-run counts. An image is unclustered in the **linear BWT output** sense, while the input-run statistic is cyclic.

## Proof
**1. The standard-permutation criterion.** Given a word \(L=L_0\cdots L_7\), write \(F\) for its letters sorted nondecreasingly. Define \(\pi_L(i)\) to be the index in \(F\) of the occurrence \(L_i\), counting repeated equal symbols from left to right. Thus if \(L_i=a\), \(r\) occurrences of \(a\) precede index \(i\) in \(L\), and \(C_a\) symbols of \(F\) are smaller than \(a\), then \(\pi_L(i)=C_a+r\). A standard inverse-BWT criterion says that \(L\) is the transform of a primitive necklace precisely when \(\pi_L\) is one eight-cycle. For such a word the cyclic input-run number equals
\[
 \#\{i:F_i\ne L_i\}=d_H(L,F).
\]
The same identities can be verified directly by sorting rotations, as the second standalone checker does.

**2. Every sharp image has even multiplicities.** Let \(m_a\) be the multiplicity of each occurring letter \(a\), and let \(I_a\) be its interval of \(m_a\) consecutive positions in \(F\). Write \(s_a=\#\{i\in I_a:L_i=a\}\). Since adjacent positions of \(L\) differ, the matching positions in \(I_a\) form an independent set in a path of \(m_a\) vertices. If \(m_a=2u+1\) is odd and \(s_a=u+1\), the matching positions must be precisely \(C_a,C_a+2,\ldots,C_a+2u\). Let \(\ell\) be the number of occurrences of \(a\) before \(C_a\); then \(0\le\ell\le u\). By stable sorting,
\[
 \pi_L(C_a+2j)=C_a+\ell+j\quad(0\le j\le u).
\]
Choosing \(j=\ell\) makes \(C_a+2\ell\) a fixed point of \(\pi_L\), impossible for an eight-cycle. Therefore for **every** letter, even or odd multiplicity,
\[
 s_a\le\lfloor m_a/2\rfloor.
\]
Because \(\sum_a m_a=8\), it follows that \(d_H(L,F)=8-\sum_a s_a\ge4\). In the sharp case equality forces \(\sum_a\lfloor m_a/2\rfloor=4\). Hence no positive \(m_a\) is odd. Also, a linear unclustered word of length eight cannot use any letter more than four times. Every positive multiplicity is therefore \(2\) or \(4\), giving precisely the ordered profiles \((4,4)\), \((4,2,2)\), \((2,4,2)\), \((2,2,4)\), and \((2,2,2,2)\).

**3. Exhaustive finite reduction.** For each of these five profiles, enumerate all distinct permutations of the associated sorted multiset, retain only words with no equal adjacent letters, calculate \(\pi_L\) from the explicit formula in step 1, check it is one cycle, and finally require \(d_H(L,F)=4\). The exact census is:

| Ordered multiplicities | Distinct candidate words | Accepted words |
| --- | ---: | --- |
| \((4,4)\) | 70 | none |
| \((4,2,2)\) | 420 | `10201020` |
| \((2,4,2)\) | 420 | `10120121` |
| \((2,2,4)\) | 420 | `20212021` |
| \((2,2,2,2)\) | 2520 | `10130232`, `20312130`, `30212031` |

This is a *complete finite proof* because the preceding parity argument reduces **every possible alphabet size** to these 3,850 words. The attached `verify_bwt_n8.py` is a standalone executable implementation of the exact predicate and enumeration, with assertions for each cell of the table. No sampling, numerical tolerance, or search timeout is used. The one-cycle criterion gives the exact six patterns, and the preceding inequality proves that four runs is minimal.

**4. Recovering every ordered alphabet.** An order-preserving choice of \(t\) distinct letters in \(\Sigma_q\) has \(\binom qt\) possibilities. It preserves equality, lexicographic order, \(\pi_L\), and the Hamming distance to \(F\). Conversely, each sharp image reduces uniquely to one listed order type. There are three types with \(t=3\) and three with \(t=4\), yielding the stated exact binomial count and fixed-content classification. \(\square\)

## Verification
Run `python3 verify_bwt_n8.py` using Python 3 and the standard library only. It independently verifies the five profile rows and their 3,850 candidates, then directly constructs the lexicographic BWT of all 65,280 primitive words of length eight on four letters. The second route computes cyclic runs on source words, without using the standard-permutation formula, and recovers exactly the same six reduced output patterns. Separate direct BWT counts for three- and four-letter alphabets confirm the binomial formula at those alphabet sizes. The expected final line is `VALIDATION_OK`.

For independent manual spot checks, the canonical transforms `10120121`, `10201020`, `20212021`, `10130232`, `20312130`, and `30212031` arise respectively from the primitive input representatives `00112211`, `00022011`, `00211222`, `00223311`, `00331122`, and `00221133`, each with exactly four cyclic runs. These witnesses alone establish existence, not uniqueness; uniqueness comes from the exhaustive profile enumeration.

## Relationship to prior work
Kumallagov (arXiv:2606.01267v1, Sections 3, 4, 6, 9, and Appendix A) introduced the extremal cyclic-run problem, proved \(U_q(8)=4\), and displayed `10120121` as one length-eight example. Its Parikh obstruction is compatible with step 2, and its appendix exhaustively enumerates *length six* for a different, exceptional case. The inspected text does not classify all length-eight optimizers, their fixed-content profiles, or their dependence on alphabet size. Fici–Gabory–Romana–Sciortino (arXiv:2508.20879v1, Sections 1–3) proved the existence of completely unclustered BWT images at every length on nonbinary alphabets, but not the length-eight four-input-run equality census. Thus the present result refines the explicit fixed-Parikh question posed in Kumallagov's Problem 10.1; it does not claim a new general run inequality or a construction for arbitrary lengths.

## Limitations
The calculation is finite in the word length, albeit uniform in all finite ordered alphabet sizes. It does not establish the sharpness conjecture for longer lengths. The complete list uses the standard primitive-necklace BWT criterion; the independent direct enumeration serves as an additional cross-check. Exhaustively inspecting 3,850 length-eight candidates is feasible, but does not establish historical priority against all unpublished or unindexed work. No external audit has been performed.

## References
1. D. Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267v1 (first public 2026-05-31), https://arxiv.org/pdf/2606.01267v1.
2. G. Fici, E. Gabory, G. Romana, M. Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879v1 (first public 2025-08-28), https://arxiv.org/abs/2508.20879.
