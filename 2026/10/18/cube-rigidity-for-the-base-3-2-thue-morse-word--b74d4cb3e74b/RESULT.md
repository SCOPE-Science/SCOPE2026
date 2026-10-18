# Cube rigidity for the base-\(3/2\) Thue–Morse word

## Finding
Let \(x=x_0x_1\cdots\) be the binary word defined by \(x_0=0\) and, for all integers \(m\geq0\),
\[
x_{3m}=x_{2m},\qquad x_{3m+1}=1-x_{2m},\qquad x_{3m+2}=x_{2m}.
\]
A period \(p\geq1\) of a factor \(x_s\cdots x_{s+L-1}\), where \(s\geq0\) and \(L>p\), means \(x_{s+i}=x_{s+i+p}\) for every \(0\leq i<L-p\). The period need not be the least period.

**Theorem.** If \(3\nmid p\) and a factor of \(x\) of length \(3p\) has period \(p\), then \(p=2\) and the factor is \(010101\) or \(101010\). Both factors occur. Moreover,
\[
\max_{\substack{s\geq0,\;p\geq1,\;L>p\\3\nmid p,\; p\text{ a period of }x_s\cdots x_{s+L-1}}}\frac Lp=\frac92.
\]
The maximum is attained by \(x_{12}\cdots x_{20}=101010101\), with period \(p=2\). In particular every factor that is a fifth power has all of its exhibited fifth-power periods divisible by \(3\); the conclusion also excludes every cube with a period coprime to \(3\), except the two alternating period-\(2\) cubes.

## Assumptions and scope
All indices and periods are integers. For \(m=0\), the displayed recurrence at index zero is read together with the given initial condition \(x_0=0\). The word is the parity of the sum of digits of nonnegative integers in the base-\(3/2\) representation, listed as OEIS A357448. The maximum is a restricted critical exponent: only periods not divisible by \(3\) are admitted. No claim about periods divisible by \(3\), or the unrestricted critical exponent, is asserted.

## Proof
**1. Aligned blocks and equalities.** Put \(a_m=x_{2m}\). The recurrence gives the exact aligned blocks
\[
(x_{3m},x_{3m+1},x_{3m+2})=(a_m,1-a_m,a_m).
\]
Consequently an equal adjacent pair \(x_j=x_{j+1}\) can start only when \(j\equiv2\pmod3\). In particular every three consecutive letters contain adjacent unequal letters, and no factor \(000\) or \(111\) occurs.

**2. No alternating factor of length ten.** Among each four consecutive letters \(a_m,a_{m+1},a_{m+2},a_{m+3}\), some two adjacent letters coincide. Indeed the corresponding indices \(2m,2m+2,2m+4,2m+6\) contain a consecutive pair \((3j,3j+2)\): it is pair \((0,1)\), \((2,3)\), or \((1,2)\) as \(m\equiv0,1,2\pmod3\), respectively. By the recurrence, \(x_{3j}=x_{3j+2}\). On the other hand, any alternating factor of length ten spans three successive boundaries between aligned length-three blocks, regardless of its starting residue modulo three. Alternation across these boundaries would force four consecutive \(a\)-letters to alternate. This contradicts their mandatory adjacent equality. Thus every alternating factor has length at most nine.

**3. Rigidity of cubes.** Let \(w=x_s\cdots x_{s+3p-1}\) have period \(p\) with \(3\nmid p\). Suppose an equal adjacent pair exists within \(w\). By period-\(p\) repetition, some such pair starts at relative offset \(r\), with \(0\leq r<p\). If \(r\leq p-2\), the same pair starts at offsets \(r\), \(r+p\), and \(r+2p\), all within the factor. Their starting indices occupy three distinct residues modulo three, contradicting Step 1. If \(r=p-1\), the same pair starts at relative offsets \(p-1\) and \(2p-1\); these start in different residue classes modulo three and again contradict Step 1. (All these pairs lie inside the length-\(3p\) factor.) Therefore every adjacent pair in \(w\) is unequal: \(w\) is alternating. A nonconstant alternating word can have period \(p\) only when \(p\) is even. By Step 2, \(3p\leq9\). Hence \(p\) is a positive even integer at most three, so \(p=2\). The only two binary alternating words of length six are \(010101\) and \(101010\).

**4. Sharp exponent.** Suppose \(x_s\cdots x_{s+L-1}\) has period \(p\) with \(3\nmid p\). If \(L<3p\), then \(L/p<3\). Otherwise its prefix of length \(3p\) is a cube with the same period; Step 3 forces \(p=2\). In this case the entire factor is alternating (its first six letters alternate, and period two propagates this through the entire factor), so Step 2 implies \(L\leq9\), whence \(L/p\leq9/2\). Direct application of the recurrence gives \(x_{12}\cdots x_{20}=101010101\). This period-two factor realizes \(9/2\), and its length-six subfactors realize both cubic words. The theorem follows. \(\square\)

## Verification
The standalone standard-library program `CHECK.py` reconstructs the recurrence, independently agrees with direct base-\(3/2\) digit-parity computation at the first 5,000 indices, locates the length-nine alternating factor at indices \(12\) through \(20\), and confirms that all cubic occurrences with \(1\leq p\leq120\), \(3\nmid p\), in its finite 50,000-letter prefix have \(p=2\) and one of the two asserted words. It also checks the prefix's longest alternating run is nine. These finite checks are cross-checks; the infinite assertions are established by the four-step proof.

Reproduce with `python3 CHECK.py` (Python standard library only).

## Relationship to prior work
Dekking identified this binary word as the parity sequence for base-\(3/2\) digits, proved its length-two-to-length-three block recurrence, and recorded Shallit's conjecture that its unrestricted critical exponent is five (arXiv:2301.13563, Journal of Integer Sequences 26, 2023). Dekking and Keane studied the related two-block substitution and exhibited a fourth power; neither inspected article determines which coprime-to-three cube periods occur or the exact restricted exponent. A later paper of Cassaigne, Espinoza, Rigo, and Stipulanti (arXiv:2602.21895, 2026) resolves recurrence and frequency questions but does not state this restricted repetition theorem. OEIS A357448 records the sequence and recurrence, not a cube-period classification. The present result uses the known recurrence but introduces the aligned-boundary obstruction needed for sharp repetition rigidity.

## Limitations
The theorem gives no bound for periods divisible by three and does not prove or disprove the conjectural unrestricted critical exponent five. A semantically equivalent result outside the examined literature or not indexed by the consulted resources is a remaining originality risk. The result has received the self-review only; no independent mathematical audit has been performed.

## References
1. F. M. Dekking, *The Thue–Morse sequence in base 3/2*, arXiv:2301.13563 (first public preprint January 31, 2023); *Journal of Integer Sequences* **26** (2023), Article 23.2.3. https://arxiv.org/abs/2301.13563 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Dekking/dek25.pdf
2. F. M. Dekking and M. Keane, *Two-block substitutions and morphic words*, *Advances in Applied Mathematics* **148** (2023), 102536. https://ir.cwi.nl/pub/33010/33010.pdf
3. J. Cassaigne, B. Espinoza, M. Rigo, and M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base 3/2 and related conjectures*, arXiv:2602.21895 (2026). https://arxiv.org/abs/2602.21895
4. *On-Line Encyclopedia of Integer Sequences*, A357448, approved September 30, 2022. https://oeis.org/A357448 ; https://oeis.org/history?seq=A357448
