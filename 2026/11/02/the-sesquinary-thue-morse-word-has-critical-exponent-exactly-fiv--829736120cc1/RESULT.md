# The sesquinary Thue–Morse word has critical exponent exactly five

## Finding

Let \(x=(x_n)_{n\ge0}\) be the parity of the digit sum of the unscaled base-\(3/2\) expansion of the nonnegative integers. It is uniquely defined by \(x_0=0\) and
\[
x_{3m}=x_{2m},\qquad x_{3m+1}=1-x_{2m},\qquad x_{3m+2}=x_{2m}\quad(m\ge0).
\]
A length-\(L\) factor has period \(p\) if its entries at positions \(i\) and \(i+p\) agree whenever both are in the factor. Its exponent at that period is \(L/p\). The critical exponent is the supremum of such exponents over all factors and periods.

**Theorem.** For every integer \(p\ge1\), no factor of \(x\) of length \(5p+1\) has period \(p\). Moreover
\[
x_{18}x_{19}\cdots x_{32}=101101101101101=(101)^5.
\]
Consequently the critical exponent of \(x\) is exactly \(5\), including the usual fractional-exponent convention. This proves Conjecture 9 of Dekking [1], attributed there to J. Shallit.

## Assumptions and scope

All words and periods are finite, while \(x\) is an infinite one-sided binary word. The definition uses the **unscaled** base-\(3/2\) representation (OEIS A357448), not the distinct normalised \(\frac12\cdot\frac32\) numeration system. The binary complement of a symbol \(b\in\{0,1\}\) is denoted by \(\bar b=1-b\). Define the even-index word \(u_m=x_{2m}\). The displayed recursion for \(x\) is a previously known identity [1]; the statements and proof below concern the repetition threshold.

## Proof

**1. Macroblock identities and local obstructions.** From the defining recursion, the three entries of the \(m\)-th aligned block of \(x\) are
\[
(x_{3m},x_{3m+1},x_{3m+2})=(u_m,\bar u_m,u_m).
\tag{1}
\]
Applying this at even arguments gives the second macroblock identity
\[
(u_{3m},u_{3m+1},u_{3m+2})=(u_{2m},u_{2m},\bar u_{2m+1}).
\tag{2}
\]
In particular, \(u_{3m}=u_{3m+1}\). Every four consecutive positions contain such a pair, so there are **no four consecutive alternating symbols in \(u\)**.

There are also **no six consecutive equal symbols in \(u\)**. Indeed, suppose a six-letter constant factor begins at one of \(3m\), \(3m+1\), or \(3m+2\). Substituting (2) for the relevant blocks forces, respectively, the source entries indexed from \(2m\) to \(2m+3\), from \(2m\) to \(2m+4\), or from \(2m+1\) to \(2m+4\) to alternate. Each possibility includes four alternating source symbols, a contradiction.

By (1), every three successive entries of \(x\) include a flip, so there are **no three consecutive equal symbols in \(x\)**. Moreover **no ten consecutive entries of \(x\) alternate**: the nine edges of such a factor include three consecutive block-boundary edges of the form \((x_{3m+2},x_{3m+3})=(u_m,u_{m+1})\). Alternation across those three edges forces four consecutive \(u\)-symbols to alternate, already excluded.

**2. Rigidity at periods not divisible by three.** Suppose a word factor \(w\) of length \(L\ge3p+1\) has period \(p\) with \(3\nmid p\). For any fixed cyclic adjacent pair of the period word (including the pair crossing the period boundary), the three copies of this pair beginning \(p\) positions apart all occur within \(w\); their starting indices run through all residues modulo three.

For \(w\subset u\), one of those edges begins at a multiple of three, where (2) makes the two symbols equal. Therefore *every* cyclic adjacent pair in the period word is equal, and \(w\) is constant. In particular, if \(L\ge6\) this contradicts step 1.

For \(w\subset x\), one of those edges begins at residue zero or one modulo three, where (1) makes the two symbols distinct. Therefore *every* cyclic adjacent pair in the period word differs, and \(w\) is alternating. In particular, if \(L\ge10\) this contradicts step 1.

**3. Desubstituting a divisible period in the even-index word.** Let a factor of \(u\) start at \(s\), have length \(L\), and have period \(q=3r\). Retain only its complete aligned three-letter blocks in (2). The number of these blocks is
\[
K=\left\lfloor\frac{s+L}{3}\right\rfloor-\left\lceil\frac{s}{3}\right\rceil,
\]
and the first and third entries of each retained block recover the two consecutive input symbols \(u_{2m}\) and \(u_{2m+1}\). Thus the recovered contiguous factor of \(u\) has length \(L'=2K\), period \(q'=2r\), and
\[
L'\ge\frac{2L}{3}-\frac83.
\tag{3}
\]
The periodicity holds because an aligned output shift by \(3r\) is an input shift by \(2r\), and both decoded input symbols agree whenever both output blocks lie in the original factor.

**4. A uniform repetition cutoff for \(u\).** We claim that **no factor of \(u\) with period \(q\ge2\) has length at least \(5q-1\)**. Suppose one does. Write \(q=3^h q_0\) with \(3\nmid q_0\), and apply step 3 exactly \(h\) times. The resulting factor has period \(q_h=2^h q_0\), not divisible by three. Iterating (3) from \(L_0\ge5q-1\) gives
\[
L_h\ge 5q_h-8+7(2/3)^h.
\tag{4}
\]
If \(h=0\), then \(q_h\ge2\), so \(L_h\ge5q_h-1\ge3q_h+1\) and \(L_h\ge6\). If \(h=1\), then \(q_h\ge2\), and (4) gives \(L_h\ge5q_h-10/3\); for the smallest case \(q_h=2\) the integer length is at least seven, and for greater \(q_h\) it is at least \(3q_h+1\). If \(h=2\), then \(q_h\ge4\), and (4) gives \(L_h\ge5q_h-44/9\ge3q_h+1\). If \(h\ge3\), then \(q_h\ge8\) and (4) gives \(L_h>5q_h-8\ge3q_h+1\). In every case \(L_h\ge6\), contradicting the rigidity of step 2 for the period \(q_h\). The claim follows.

**5. Excluding all exponents strictly greater than five.** Suppose \(x\) has a factor of period \(p\) and length \(5p+1\). If \(3\nmid p\) and \(p\ge2\), step 2 makes the factor alternating because \(5p+1\ge3p+1\), whereas \(5p+1\ge11\); this contradicts step 1. If \(p=1\), six equal symbols contradict the absence of three equal symbols in \(x\).

Now let \(p=3q\). The factor length is \(15q+1\), hence it contains at least \(5q-1\) **complete** aligned blocks of (1). Their first letters form a factor of \(u\) having period \(q\). For \(q\ge2\), this contradicts step 4. For \(q=1\), a length-sixteen period-three factor intersects at least six consecutive aligned blocks of (1). Since at least one of these is complete, period three determines the entire three-phase pattern as \((b,\bar b,b)\); every intersected block must then have value \(u_m=b\). This yields six consecutive equal symbols of \(u\), contradicting step 1. All periods have been excluded.

Finally the defining recursion gives the explicit fifteen-letter factor in the theorem (also checked by the supplied independent digit algorithm). Its period is three, so exponent five is attained. Since any factor of exponent strictly greater than five has an initial subfactor of length \(5p+1\), the critical exponent is exactly five. \(\square\)

## Verification

Run `python3 VERIFY.py` using ordinary Python 3. It independently computes \(x_n\) both recursively and by repeatedly taking base-\(3/2\) least significant digits \(n\bmod3\) while replacing \(n\) by \(2\lfloor n/3\rfloor\). It checks the identities (1)–(2), the fifteen-letter witness, local obstructions, and finite-range exclusions of periods. These checks guard against transcription and boundary mistakes but do not establish the infinite claim: steps 1–5 supply its proof.

## Relationship to prior work

Dekking [1] supplies the digit recursion and explicitly states the critical-exponent-five assertion as Conjecture 9 (attributed to Shallit), without a proof. Cassaigne–Espinoza–Rigo–Stipulanti [2] study the same unscaled word as a sibling of their normalised-base word, and prove uniform recurrence and complement/reversal stability, but do not state a critical-exponent or \(5p+1\)-period theorem. The separate 2025 work of Dvořáková–Kreczman–Pelantová [3] concerns a different indexed family of Thue–Morse-like words; it is not a proof of the rational-base conjecture. No more general theorem subsuming the present cutoff was located in the checked materials. This last statement is an evidence-limited comparison, not a claim to complete priority certification.

## Limitations

The theorem concerns precisely the parity word from the unscaled rational-base \(3/2\) representation, not arbitrary rational-base expansions, general block substitutions, or the distinct normalised-base word. No assertions about exponent frequencies or multiplicities are made. The scientific review is not independent; undiscovered earlier equivalent arguments remain possible.

## References

[1] F. M. Dekking, *The Thue–Morse sequence in base 3/2*, arXiv:2301.13563v1 (31 January 2023), especially Theorem 1, Theorem 2 and Conjecture 9; Journal of Integer Sequences 26 (2023), Article 23.2.3. https://arxiv.org/html/2301.13563v1

[2] J. Cassaigne, B. Espinoza, M. Rigo and M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base 3/2 and related conjectures*, arXiv:2602.21895v1 (25 February 2026), especially Section 1.4 and the contributions summary. https://arxiv.org/pdf/2602.21895

[3] L. Dvořáková, S. Kreczman and E. Pelantová, *On two conjectures of Shallit about Thue-Morse-like sequences*, arXiv:2506.04407 (4 June 2025). https://arxiv.org/abs/2506.04407
