# Two palindromic extremizers for pseudoperiod \((9,12)\) at the \(\frac{55}{21}\)-free boundary
## Finding
A finite binary word \(w=w_0w_1\cdots w_{n-1}\) has pseudoperiod \((9,12)\) when
\[
w_i\in\{w_{i+9},w_{i+12}\}\qquad(0\le i<n-12).
\]
Say that \(w\) is \(\frac{55}{21}\)-free when every nonempty factor has exponent strictly below \(\frac{55}{21}\).

The published sharp maximum length for a binary \((9,12)\)-pseudoperiodic \(\frac{55}{21}\)-free word is \(200\). Exactly two words attain that maximum:
\[
\mathtt{00110100101100110100101100110101100110100101100110101100100110101100110100101100110101100100110101100110101100100110101100110100101100110101100100110101100110100101100110101100110100101100110100101100}
\]
and
\[
\mathtt{11001011010011001011010011001010011001011010011001010011011001010011001011010011001010011011001010011001010011011001010011001011010011001010011011001010011001011010011001010011001011010011001011010011}.
\]
They are bitwise complements of one another, and each is a palindrome. No valid word of length \(201\) exists.

## Assumptions and scope
The pseudoperiod condition is the finite-word definition used by Meleshko, Ochem, Shallit, and Shan: it is imposed only at indices \(i<n-12\). The repetition exponent of a factor is its length divided by its least period. Thus \(\frac{55}{21}\)-free means that factors of exponent exactly \(\frac{55}{21}\) are forbidden as well as factors of larger exponent.

The source already gives the scalar maximum \(200\) in its table of optimal critical exponents and its companion data file gives one length-\(200\) witness. The new statement is the complete equality classification: there are no further maximizers.

## Proof
Both constraints are prefix-closed, so exhaustive extension from the empty word is complete.

Suppose a valid prefix is extended by one bit. The only newly imposed pseudoperiod equation is the one with index \(i=n-1-12\); it is checked directly as
\[
w_i=w_{i+9}\quad\text{or}\quad w_i=w_{i+12}.
\]
Any newly created forbidden power must be a suffix. Fix a candidate period \(p\), and put
\[
L_p=\left\lceil\frac{55p}{21}\right\rceil.
\]
A suffix has exponent at least \(\frac{55}{21}\) with period \(p\) exactly when its last \(L_p\) letters have period \(p\). Therefore it is enough, and necessary, to reject an extension whenever the suffix of length \(L_p\) satisfies
\[
w_j=w_{j+p}
\]
throughout that suffix.

Exhaustive generation with these exact tests leaves \(2\) words at length \(200\) and \(0\) at length \(201\). Reading the two length-\(200\) survivors gives the displayed pair. Direct comparison shows that one is the bitwise complement of the other and that each equals its reversal.

For a second implementation, the verifier recomputes each suffix-period test by an explicit index loop rather than string-slice equality. The complete level sets of the two engines agree through length \(201\). The two boundary words are then rescanned globally: every pseudoperiod equation is checked, and every possible repeated-distance run is tested for a factor of exponent at least \(\frac{55}{21}\).

## Verification
Run `python3 verify.py` beside `certificate.json`.

The certificate stores the full survivor-count vector through length \(201\), the two length-\(200\) extremizers, and the published companion witness. The verifier reconstructs the entire prefix tree twice using independently coded suffix-period tests and requires exact equality of all levels. It then performs whole-word pseudoperiod and power scans on both extremizers, checks their two one-bit right extensions, and verifies the complement and palindrome statements.

## Relationship to prior work
Meleshko, Ochem, Shallit, and Shan study binary words with specified pseudoperiods and determine optimal critical exponents for all pairs \((a,b)\) with \(1\le a<b\le12\), \(b
e2a\), in their Table 1. For \((9,12)\), the table gives exponent \(\frac{55}{21}\) and longest finite length \(200\). This is the largest finite cutoff appearing in that table.

The public companion file `critical_exp_tables/longest_finite_seqs.txt` records one length-\(200\) witness, namely the second word displayed above. Bitwise complementation immediately supplies another witness, but neither the article nor the inspected companion table states that these two exhaust the equality layer. The exact census therefore sharpens the scalar obstruction without changing the published repetition threshold.

Targeted searches under “pseudoperiod \((9,12)\)”, “\(\frac{55}{21}\)-free”, “length \(200\)”, uniqueness/equality-case terminology, and the exact witness string did not locate a published complete extremizer classification.

## Limitations
The result classifies only the equality layer for the \((9,12)\) entry. It does not alter the published optimal critical exponent, classify near-extremal words, or address pseudoperiod pairs outside this parameter choice.

The original computation necessarily explored a finite search tree, so unpublished search logs could contain the same two-word top layer. The public article and inspected companion files do not state that uniqueness result.

## References
1. J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, “Pseudoperiodic Words and a Question of Shevelev,” arXiv:2207.10171v1, first public version 2022-07-20; Discrete Mathematics & Theoretical Computer Science 25(2), #6, 2023, DOI 10.46298/dmtcs.9919.
2. Public companion repository for the preceding article, `sonjashan/sha_gen`, file `critical_exp_tables/longest_finite_seqs.txt`.
