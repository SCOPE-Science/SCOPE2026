# Exact 103-adic valuations of the Tribonacci sequence

## Finding

For every integer \(n\ge1\), let \(T_0=0\), \(T_1=T_2=1\), and \(T_{n+3}=T_{n+2}+T_{n+1}+T_n\). Write \(\nu_{103}(u)\) for the 103-adic valuation of the positive integer \(u\). Then, for **every** \(n\ge1\),

\[
\nu_{103}(T_n)=\begin{cases}
2+\nu_{103}(n)+\nu_{103}(n+17),&n\equiv0\pmod{17},\\
1+\nu_{103}(n+4),&n\equiv13\pmod{17},\\
1+\nu_{103}(n+1),&n\equiv16\pmod{17},\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, the integer-center valuation conjecture of Marques–Lengyel holds at the formerly unresolved prime \(103\), with modulus \(17\). The exceptional residue \(0\) has two simultaneous integer centers and a baseline valuation of \(2\).

## Assumptions and scope

All congruences on indices are among integers. The valuation of zero may be set to \(+\infty\) when extending the identity to \(n=0\), but the theorem is stated for \(n\ge1\). The formulas are exact, not merely asymptotic or up to finitely many exceptions. The 103-adic analytic interpolation used in the proof is over \(\mathbb Z_{103}\), not a claim about ordinary real-variable interpolation.

## Proof

Define the companion matrix and initial state

\[
C=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix},\qquad v=(0,1,1)^{\mathsf T}.
\]

Its first coordinate in \(C^n v\) is \(T_n\), also for negative integers since \(\det C=1\). Direct seventeen-fold integer matrix multiplication gives

\[C^{17}\equiv46I\pmod{103},\qquad46^3\equiv1\pmod{103},\quad46\not\equiv1\pmod{103}.\]

Let \(\omega\in\mathbb Z_{103}\) be the unique cube root of unity congruent to \(46\) modulo \(103\) (Hensel lifting applies since the derivative \(3\omega^2\) is a unit). Thus \(U=\omega^{-1}C^{17}=I+103D\) for some matrix \(D\) with entries in \(\mathbb Z_{103}\). For each \(r\in\{0,\ldots,16\}\), set

\[
f_r(t)=e_1^{\mathsf T}C^rU^t v,
\qquad U^t=\sum_{j\ge0}\binom tj(103D)^j,
\qquad t\in\mathbb Z_{103}.
\]

The series converges uniformly and gives restricted analytic functions with integral coefficients: the coefficients of the monomials in \(t\) tend 103-adically to zero because \(\nu_{103}(103^j/j!)\to\infty\). For every nonnegative integer \(t\), \(T_{r+17t}=\omega^t f_r(t)\), and \(\omega\) is a unit, so the valuations agree.

Reduce modulo \(103\). The first component of \(C^r v\) is nonzero for \(r\notin\{0,13,16\}\). This finite check uses the recurrence for precisely the seventeen residues \(r=0,\ldots,16\), so \(f_r(t)\) is a unit throughout these fourteen classes, giving valuation \(0\).

For \(r=13,16\), the exact values \(T_{13}=927=9\cdot103\) and \(T_{16}=5768=56\cdot103\) show that \(f_r(t)\) is divisible by \(103\) as a restricted analytic function, and \(f_r(t)/103\) is affine modulo \(103\): all terms of degree at least two in the binomial expansion have coefficient divisible by \(103^2\). The negative-index identities \(T_{-4}=T_{-1}=0\), directly obtained by reversing the recurrence, imply respectively \(f_{13}(-1)=f_{16}(-1)=0\). Hence

\[
103^{-1}f_{13}(t)\equiv9(t+1)\pmod{103},\qquad
103^{-1}f_{16}(t)\equiv56(t+1)\pmod{103}.
\]

Both are nonzero constant multiples of \(t+1\). The elementary restricted-power-series factor theorem (division by the monic linear factor at an integral zero) therefore gives \(f_{13}(t)=103(t+1)h_{13}(t)\) and \(f_{16}(t)=103(t+1)h_{16}(t)\), where \(h_{13}\equiv9\) and \(h_{16}\equiv56\pmod{103}\) on all of \(\mathbb Z_{103}\). Thus both factors are units, so the two asserted valuation formulas follow because \(103\nmid17\) and \(n+4=17(t+1)\) or \(n+1=17(t+1)\) in the respective classes.

For \(r=0\), the exact identities \(T_0=0\), \(T_{17}=10609=103^2\), and \(T_{-17}=0\) give \(f_0(0)=f_0(-1)=0\). Modulo \(103^2\), the binomial series for \(f_0\) is \(T_0+t(\omega^{-1}T_{17}-T_0)\), which vanishes identically. Thus \(f_0/103^2\) is an integral restricted analytic function. Modulo \(103\), all terms indexed by \(j\ge3\) vanish, so this quotient is a polynomial of degree at most two. It vanishes at \(t=0\) and \(t=-1\), while at \(t=1\) it equals \(\omega^{-1}\) modulo \(103\). Therefore

\[
103^{-2}f_0(t)\equiv\frac{\omega^{-1}}2\,t(t+1)\pmod{103}.
\]

The same restricted-power-series factor theorem at both distinct integral zeros yields \(f_0(t)=103^2t(t+1)h_0(t)\), with \(h_0(t)\equiv\omega^{-1}/2\pmod{103}\), a unit for all integral \(t\). Consequently

\[
\nu_{103}(T_{17t})=2+\nu_{103}(t)+\nu_{103}(t+1)
=2+\nu_{103}(17t)+\nu_{103}(17t+17).
\]

Together these cases prove the theorem for all positive indices. The divisibility and unit statements above concern entire convergent functions, not just finitely many sampled integers.

## Verification

The bundled `verify.py` independently constructs the companion-matrix congruence and negative-index zeros, checks the finite residue computations, and tests the valuation formula at every \(1\le n<30000\) using arithmetic modulo \(103^8\). Those finite computations verify critical boundary arithmetic; the unrestricted conclusion rests on the restricted-analytic factorization proved above.

## Relationship to prior work

Bilu, Luca, Nieuwveld, Ouaknine, and Worrell (arXiv:2210.16959, Theorem 1.7 and its final proof section) explicitly leave \(p=103\) undecided for the integer-center conjecture, noting a degenerate first-order test. The present proof uses a **scalar 17-step companion matrix** and a nontrivial *quadratic* initial factor at residue \(0\), recovering an exact formula instead. The subsequent *On the p-adic Skolem Problem* (STACS 2026, Example 18) lists 103-adic zero branches but does not supply this exact valuation law or its exceptional quadratic multiplicity; the latter makes a zero-set statement alone insufficient to determine the exponents. The results here are not a claim to rediscover the already reported rational centers.

## Limitations

The argument concerns the Tribonacci normalization specified above, prime \(103\), and positive integer indices. It neither classifies all primes nor resolves the separate prime \(163\). Related 103-adic zeros had already been investigated in subsequent work; originality is confined to the exact all-index valuation formula and its multiplicity-two local factor. No independent expert audit has been performed.

## References

1. Y. Bilu, F. Luca, J. Nieuwveld, J. Ouaknine, J. Worrell, *On the p-adic zeros of the Tribonacci sequence*, arXiv:2210.16959, first publicly submitted 2022-10-30. https://arxiv.org/abs/2210.16959
2. *On the p-adic Skolem Problem*, STACS 2026, Example 18, on 103-adic zero branches. https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.8/LIPIcs.STACS.2026.8.html
3. Y. Bilu, F. Luca, J. Nieuwveld, J. Ouaknine, J. Worrell, *Twisted rational zeros of linear recurrence sequences*, Journal of the London Mathematical Society (2025), DOI 10.1112/jlms.70126. https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms.70126
