# Exact enumeration and positive-entropy threshold for complement-avoiding binary triples

## Finding

Write \(\overline{x}\) for the bitwise complement of a binary word \(x\). For an integer \(\ell\ge1\), call a finite binary word **\(\ell\)-complement-avoiding** when there is no binary factor \(x\) of length \(\ell\) for which both \(x\) and \(\overline{x}\) occur (possibly overlapping) as contiguous factors of the word. Let \(a_\ell(n)\) count such words of length \(n\), including the empty word at \(n=0\).

For the first exponentially growing case \(\ell=3\), the complete ordinary generating function is
\[
\boxed{\sum_{n\ge0}a_3(n)z^n=\frac{1+z^2+z^3+z^4-4z^6-2z^7-2z^8}{(1-z)(1-z-z^3)}.}
\]
The first values, beginning at \(n=0\), are \(1,2,4,8,14,22,30,42,60,86,124,180,262,382,558,816\).

Equivalently, if \(b_0=1,b_1=2,b_2=3\) and \(b_n=b_{n-1}+b_{n-3}\) for every \(n\ge3\), then
\[
\boxed{a_3(n)=4+2b_n\quad(n\ge5).}
\]
Moreover, write \(\lambda>1\) for the unique real root of \(\lambda^3-\lambda^2-1=0\), and \(r=1/\lambda\). Then, with \(C=2(1+r+r^2)/(r(1+3r^2))\),
\[
\boxed{a_3(n)=C\lambda^n+4+O(\lambda^{-n/2})},\qquad
\lambda=1.465571231876\ldots,\quad C=2.626846119704\ldots.
\]
For \(\ell=1\), there are exactly two valid nonempty words at each length; for \(\ell=2\), \(a_2(1)=2\), \(a_2(2)=4\), and \(a_2(n)=6\) for every \(n\ge3\). Thus \(\ell=3\) is the sharp threshold for positive exponential growth: the number of admissible words has exponential growth rate one at \(\ell\le2\), and at least \(\lambda>1\) at every \(\ell\ge3\).

## Assumptions and scope

All words are linear, finite, labeled binary strings over \(\{0,1\}\); they are not identified under complementation, reversal, or rotation. Factors are contiguous and may overlap. Only the simultaneous presence of a factor and its bitwise complement is forbidden. In particular, having one member of a complementary pair is allowed. Counts include the empty word. The exact enumerator and asymptotic constant concern \(\ell=3\); for \(\ell>3\), only positivity of exponential growth is asserted, not its exact rate.

## Proof

**Step 1: an exact factorwise inclusion-exclusion.** Identify each triple with its binary integer \(0,\ldots,7\), so complementation is \(i\mapsto7-i\). The four complementary pairs are \(\{i,7-i\}\) for \(i\in\{0,1,2,3\}\). For any word let \(X_i\) be the indicator that triple \(i\) is absent, and let \(Y_i\) be the indicator that triple \(7-i\) is absent. Its admissibility indicator is exactly
\[
\prod_{i=0}^3(X_i+Y_i-X_iY_i).
\]
Expanding gives \(3^4=81\) signed forbidden-factor languages. Specifically, for \(\alpha\in\{0,1,2\}^4\), forbid triple \(i\) when \(\alpha_i=0\), forbid \(7-i\) when \(\alpha_i=1\), and forbid both when \(\alpha_i=2\). Denote this forbidden set by \(S_\alpha\) and assign weight \(\epsilon_\alpha=(-1)^{|\{i:\alpha_i=2\}|}\). This is an exact identity for each individual word, not a disjointness approximation.

**Step 2: four-state transfer matrices.** Index states by length-two binary suffixes \(00,01,10,11\), encoded as integers \(0,1,2,3\). For every \(S\subseteq\{0,\ldots,7\}\), define a \(4\times4\) matrix \(T_S\) by adding a directed edge from state \(u\) to state \((2u+c)\bmod4\) precisely when the triple \(2u+c\) is not in \(S\), for \(c\in\{0,1\}\). The matrix entries are zero or one. Every word of length \(n\ge2\) avoiding \(S\) is uniquely a two-symbol start state followed by \(n-2\) allowed edges, so its generating function is exactly
\[
G_S(z)=1+2z+z^2\,\mathbf1^{\mathsf T}(I_4-zT_S)^{-1}\mathbf1,
\]
where \(\mathbf1=(1,1,1,1)^{\mathsf T}\). Consequently
\[
\sum_{n\ge0}a_3(n)z^n=\sum_{\alpha\in\{0,1,2\}^4}\epsilon_\alpha G_{S_\alpha}(z).
\]
All inverses are formal-power-series inverses since their constant matrices are \(I_4\).

**Step 3: exact finite algebra.** Applying the adjugate-over-determinant identity to the 81 explicit \(4\times4\) matrices, collecting rational terms, and cancelling gives
\[
\sum_{\alpha}\epsilon_\alpha G_{S_\alpha}(z)=
\frac{1+z^2+z^3+z^4-4z^6-2z^7-2z^8}{(1-z)(1-z-z^3)}.
\]
The standalone `verify.py` computes this symbolic equality using exact integer-polynomial arithmetic, independently of any numerical generating-function fitting. The 81-term definition above, the four-state transition rule, and the adjugate algorithm completely specify a finite reproducible algebraic certificate.

**Step 4: recurrence and growth.** Rational-function division gives the exact identity
\[
\sum_{n\ge0}a_3(n)z^n=
\frac4{1-z}+\frac{2(1+z+z^2)}{1-z-z^3}
 -(5+6z+6z^2+4z^3+2z^4).
\]
The coefficients of \((1+z+z^2)/(1-z-z^3)\) satisfy \(b_0=1,b_1=2,b_2=3\) and \(b_n=b_{n-1}+b_{n-3}\) for \(n\ge3\). This proves the stated equality for \(n\ge5\).

The denominator \(1-z-z^3\) has one simple positive root \(r\in(0,1)\), with reciprocal \(\lambda>1\) satisfying the displayed cubic. Its other reciprocal roots are a complex-conjugate pair of modulus \(\lambda^{-1/2}<1\): the product of the three roots of \(x^3-x^2-1\) is one, and the two remaining roots have equal modulus. The residue at \(z=r\) gives coefficient \((1+r+r^2)/(r(1+3r^2))\) multiplying \(\lambda^n\). The two other roots contribute \(O(\lambda^{-n/2})\) and the \(4/(1-z)\) term contributes exactly four for sufficiently large \(n\). This proves the asymptotic statement.

**Step 5: the threshold.** A nonempty word avoiding complementary single letters must be constant, giving \(a_1(n)=2\) for \(n\ge1\). For \(\ell=2\), avoiding simultaneous \(01\) and \(10\) forces at most one transition; avoiding simultaneous \(00\) and \(11\) then forces one of its two nonempty runs to have length one. At length \(n\ge3\) there are exactly two constant words and four single-transition words, giving six. For \(n=1,2\) all binary words are admissible. Finally, if a word avoids complementary triples then it avoids complementary factors of every length \(\ell\ge3\), because any length-\(\ell\) complementary pair would have complementary length-three prefixes. Thus \(a_\ell(n)\ge a_3(n)\) for every \(\ell\ge3\), completing the threshold proof.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The program (i) carries out exact symbolic inclusion-exclusion over all 81 transfer matrices, (ii) independently counts admissible words by a seen-triple streaming automaton through length 64, (iii) brute-force enumerates all binary words through length 15, and (iv) verifies the rational partial-fraction identity. Its verified output ends in `ALL CHECKS PASSED`. The infinite theorem follows from the finite symbolic identity and the proof above, not from extrapolating the finite tests.

## Relationship to prior work

Currie, Dvořáková, Ochem, Opočenská, Rampersad and Shallit introduced and analyzed classes of infinite binary words that avoid complementary factors of fixed length. Their arXiv preprint dates from 20 September 2022, and their journal article appeared in 2025. Theorem 3 and Section 5 focus on critical exponents, infinite-word factor languages, and transitions from polynomial to exponential complexity under additional repetition restrictions. The present theorem addresses a different exact enumerative question: the number of **all finite labeled words of each length**, with no repetition restriction, avoiding simultaneous complementary length-three factors. The inspected paper does not give the rational generating function, its order-three recurrence, or its asymptotic leading constant.

The related paper by Baranwal and collaborators enumerates binary words avoiding contiguous **antisquares** of the form \(x\overline{x}\). Such local contiguous concatenations are different from a pair of complementary factors at arbitrary positions. Neither that growth result nor general transfer-matrix existence statements supply the rational function above without the explicit finite calculation.

## Limitations

No exact enumerator is claimed for complementary-factor lengths greater than three, and no classification of individual infinite sequences or repetition thresholds is claimed. Published literature may contain an unindexed equivalent finite enumeration; originality rests on the specified primary-text and indexed-record comparisons rather than an exhaustive theorem of uniqueness. The symbolic computation is a finite, completely specified algebraic identity; the separate brute-force tests cover only the stated finite ranges.

## References

1. J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598v1 (20 September 2022); Electronic Journal of Combinatorics **32**(4) (2025), #P4.24, DOI:10.37236/11555. Full text: https://arxiv.org/html/2209.09598v2.
2. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad and J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223v1 (19 September 2022), Discrete Mathematics & Theoretical Computer Science **25**(2) (2023), #11, DOI:10.46298/dmtcs.10063. Full text: https://arxiv.org/html/2209.09223v3.
