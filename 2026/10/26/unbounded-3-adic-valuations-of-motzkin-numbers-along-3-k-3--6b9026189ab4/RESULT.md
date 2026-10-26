# Unbounded \(3\)-adic valuations of Motzkin numbers along \(3^k-3\)

## Finding

Write \(M_n\) for the \(n\)-th Motzkin number, with generating series
\[
M(x)=\sum_{n\ge0}M_nx^n=\frac{1-x-\sqrt{(1+x)(1-3x)}}{2x^2}.
\]
For every integer \(k\ge2\),
\[
\boxed{M_{3^k-3}\equiv-3^{k-1}\pmod{3^k}},
\qquad
\boxed{\nu_3(M_{3^k-3})=k-1}.
\]
In particular, the sequence of \(3\)-adic valuations of the Motzkin numbers is unbounded. This settles the unboundedness part of Rowland and Yassawi's Open Question 3.15 [1].

## Assumptions and scope

\(M_0=1\), \(M_1=1\), and \(M_n\) counts lattice paths from \((0,0)\) to \((n,0)\) with steps \((1,1)\), \((1,0)\), \((1,-1)\), never passing below the horizontal axis. The \(3\)-adic valuation \(\nu_3(t)\) for nonzero integer \(t\) is the exponent of \(3\) dividing it. The theorem concerns the infinite subsequence \(3^k-3\), \(k\ge2\); it does not characterize all valuations or prove \(3\)-regularity.

## Proof

Fix \(k\ge2\), put \(N=3^k\) and \(m=N-1\) (which is even). Extracting the coefficient of \(x^{m}\) from the generating function yields
\[
M_{N-3}=-\frac12[x^m]\sqrt{(1+x)(1-3x)}
=-\frac12\sum_{j=0}^{m}\binom{1/2}{m-j}\binom{1/2}{j}(-3)^j. \tag{1}
\]
For integers \(t\ge1\),
\[
\binom{1/2}{t}=(-1)^{t-1}\frac{2C_{t-1}}{4^t},\qquad
C_s=\frac1{s+1}\binom{2s}{s}\in\mathbb Z, \tag{2}
\]
so every half-integral binomial coefficient in (1) is a \(3\)-adic integer. Consequently, terms with \(j\ge k\) vanish modulo \(3^k\).

For \(1\le j<k\), define \(s=N-j-2\), so that \(m-j=s+1\ge1\). We establish the key bound
\[
\nu_3(C_{N-j-2})\ge k-j. \tag{3}
\]
Recall Kummer's carry formula for Catalan numbers:
\[
\nu_3(C_s)=\bigl(\text{number of carries in the base-\(3\) sum }s+s\bigr)-\nu_3(s+1). \tag{4}
\]
For \(j=1\), the base-\(3\) expansion of \(s=N-3\) has \(k-1\) leading digits \(2\) and final digit \(0\). Its doubling creates exactly \(k-1\) carries, while \(3\nmid(s+1)\); hence (3) holds with equality.

For \(j=2\), available when \(k\ge3\), the last two base-\(3\) digits of \(s=N-4\) are \(12\) and all preceding digits are \(2\). Doubling produces \(k\) carries and \(\nu_3(s+1)=1\); thus \(\nu_3(C_s)=k-1\ge k-2\).

For \(j=3\), available when \(k\ge4\), the last two digits of \(s=N-5\) are \(11\) and all preceding digits are \(2\). Doubling produces exactly \(k-2\) carries, while \(3\nmid(s+1)\). Thus \(\nu_3(C_s)=k-2\ge k-3\).

For \(4\le j<k\), let \(r\) be the positive integer determined by \(3^{r-1}<j+2\le3^r\). Since \(j+2<N\), the top \(k-r\) base-\(3\) digits of \(s=N-(j+2)\) are all \(2\). Doubling therefore creates at least \(k-r\) carries. Moreover, \(s+1=N-(j+1)\) has \(\nu_3(s+1)=\nu_3(j+1)\le r-1\), because \(0<j+1<3^r\). Hence
\[
\nu_3(C_s)\ge k-2r+1\ge k-j,
\]
where the final inequality follows from \(2r\le j\) for all integers \(j\ge4\) satisfying \(3^{r-1}<j+2\le3^r\) (immediate for \(r=2\), and by \(3^{r-1}-1\ge2r\) for \(r\ge3\)). This proves (3) in all cases. By (2), every summand in (1) with \(1\le j<k\) is also divisible by \(3^k\) in the \(3\)-adic integers.

It remains to evaluate the term \(j=0\). Since \(m\) is even, (2) gives
\[
-\tfrac12\binom{1/2}{m}=\frac{C_{N-2}}{4^{N-1}}. \tag{5}
\]
The exact identity
\[
C_{N-2}=\frac{N}{4(2N-1)(2N-3)}\binom{2N}{N} \tag{6}
\]
shows that \(\nu_3(C_{N-2})=k-1\): indeed \(\nu_3(N)=k\), \(\nu_3(2N-3)=1\), \(2N-1\) is a \(3\)-adic unit, and Lucas's theorem gives \(\binom{2N}{N}\equiv2\pmod3\). More precisely,
\[
\frac{C_{N-2}}{3^{k-1}}
=\frac{3}{2N-3}\frac{\binom{2N}{N}}{4(2N-1)}
\equiv(-1)\cdot\frac{2}{-1}\equiv-1\pmod3. \tag{7}
\]
As \(4^{N-1}\equiv1\pmod3\), equation (5) is congruent to \(-3^{k-1}\) modulo \(3^k\). Together with the vanishing of all \(j\ge1\) terms in (1), this proves the asserted congruence and exact valuation. \(\square\)

## Verification

A standalone integer-arithmetic checker, `verify_motzkin.py`, independently computes the standard Motzkin recurrence through the indices \(3^k-3\) for \(2\le k\le7\), confirms exact valuations and residues, tests the Catalan identity (6), and checks the carry bounds used in the proof for small \(k\). Its successful output is `VERIFY_OK`. These finite checks corroborate but do not replace the infinite proof.

## Relationship to prior work

Rowland and Yassawi [1, Section 3.3, Open Question 3.15] explicitly ask whether the \(3\)-adic valuations of Motzkin numbers are unbounded, and, if so, whether the entire valuation sequence is \(3\)-regular. The displayed congruence answers the first question affirmatively, without addressing the second. Krattenthaler and Müller [2, Section 7] develop a method for Motzkin congruences modulo any *fixed* power of \(3\); their inspected results do not give an exact valuation growing with \(k\) on \(3^k-3\). Kohen [3] proves symmetry formulas for Motzkin numbers modulo a prime \(p\), not modulo unbounded powers of \(3\); this does not imply the present prime-power result. The related composite-index list OEIS A393215 [4] uses a different congruence and does not cover this valuation identity.

## Limitations

The theorem does not establish whether \((\nu_3(M_n))_{n\ge0}\) is \(3\)-regular or compute the valuation at arbitrary indices. While targeted literature and database comparisons did not find the exact theorem, incompleteness of indexing leaves a residual risk that an equivalent result exists elsewhere. The independent mathematical audit remains outstanding.

## References

[1] E. Rowland and R. Yassawi, “Automatic congruences for diagonals of rational functions,” *Journal de Théorie des Nombres de Bordeaux* 27 (2015), 245–288, Section 3.3, Open Question 3.15. First public preprint: arXiv:1310.8635v1 (2013-10-31). DOI: 10.5802/jtnb.901.

[2] C. Krattenthaler and T. W. Müller, “A method for determining the mod-\(3^k\) behaviour of recursive sequences,” arXiv:1308.2856 (2013), Section 7.

[3] N. Kohen, “Density and symmetry in the generalized Motzkin numbers modulo \(p\),” *Integers* 26 (2026), article A22; arXiv:2411.03681.

[4] OEIS A393215, “Odd composite numbers \(k\) such that \(M_{k-3}\equiv(-3)^{(k-3)/2}\pmod{k}\),” first created 2026.
