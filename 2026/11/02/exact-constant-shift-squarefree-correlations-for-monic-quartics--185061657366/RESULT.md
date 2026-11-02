# Exact constant-shift squarefree correlations for monic quartics over finite fields

## Finding
Let \(q\) be a prime power, let \(k=\mathbb F_q\), and fix \(c\in k^\times\). Among monic quartics \(f\in k[T]\), define \(B_q(c)\) as the number for which neither \(f\) nor \(f+c\) is squarefree, and \(C_q(c)\) as the number for which both are squarefree. Write \((k^\times)^j=\{t^j:t\in k^\times\}\).

The exact simultaneous non-squarefree spectrum is
\[
B_q(c)=\begin{cases}
q^2,&q\text{ even},\\
q(q-5),&q\equiv1\pmod8,\quad c\in(k^\times)^4,\\
q(q+3),&q\equiv1\pmod8,\quad c\in(k^\times)^2\setminus(k^\times)^4,\\
q(q-1),&\text{every other odd case}.
\end{cases}
\]
Moreover,
\[
C_q(c)=q^4-2q^3+B_q(c).
\]
For uniformly random monic \(f\), the covariance of the indicators of squarefreeness of \(f\) and \(f+c\) equals \((B_q(c)-q^2)/q^4\). These events are independent if and only if \(q\) is even. When \(q\equiv1\pmod8\), the three values of \(B_q(c)\) occur for exactly \((q-1)/4,(q-1)/4,(q-1)/2\) nonzero shifts respectively, in the order fourth powers, squares not fourth powers, and nonsquares.

## Assumptions and scope
Every prime power \(q\), including characteristic two and nonprime fields, is covered; the shift \(c\) is nonzero and constant, and \(f\) is monic of degree exactly four. Squarefree means no squared nonconstant irreducible polynomial factor, equivalently \(\gcd(f,f')=1\). The standard number of squarefree monic degree-four polynomials over \(k\) is \(q^4-q^3\).

## Proof
**Odd characteristic: rational repeated roots.** Let \(q\) be odd. Write \(R_j(s)=\#\{t\in k^\times:t^j=s\}\) and
\[
H(s)=\#\{t\in k^\times:t^2=s,\quad -t\notin(k^\times)^2\}.
\]
For each ordered pair of distinct \(x,y\in k\), the four conditions
\[
f(x)=f'(x)=0,\qquad f(y)=-c,\quad f'(y)=0
\]
uniquely determine one monic quartic. Indeed, the difference of two solutions has degree at most three but is divisible by \((T-x)^2(T-y)^2\); existence follows from the invertible two-point Hermite interpolation system. Thus there are exactly \(q(q-1)\) such triples \((f,x,y)\).

A quartic has at most two *distinct* repeated roots. If both \(f\) and \(f+c\) have two rational repeated roots, they are squares of monic quadratics, say \(f=g^2\) and \(f+c=h^2\). But \((h-g)(h+g)=c\) is impossible, because \(h+g\) has degree two in odd characteristic. Therefore the incidence count overcounts only when one polynomial has two rational repeated roots and the other has one.

If \(f=g^2\) with \(g=(T-x)(T-z)\), \(x\ne z\in k\), then \(f+c\) can have a repeated rational root only at \(y=(x+z)/2\), since its derivative is \(2gg'\) and its values at \(x,z\) are \(c\ne0\). Because \(f(y)=(x-z)^4/16\), this happens precisely if \((x-z)^4=-16c\). The number of unordered pairs \(\{x,z\}\) satisfying this condition is \(qR_4(-c)/2\), since multiplication by \(2\) bijectively rescales fourth roots. Similarly, the number of cases where \(f+c\) has two distinct rational repeated roots and \(f\) has one is \(qR_4(c)/2\). Hence the count with a rational repeated root in each polynomial is
\[
q(q-1)-\frac q2\bigl(R_4(c)+R_4(-c)\bigr).
\]

**Odd characteristic: nonrational repeated roots.** A non-squarefree monic quartic with no repeated root in \(k\) must equal \(g^2\), where \(g\) is monic irreducible of degree two. If \(f=g^2\), then \(f+c\) cannot also be a quadratic square: otherwise \((h-g)(h+g)=c\), impossible as above. Consequently, if \(f+c\) is non-squarefree it must have a repeated *rational* root \(y\). Write the unique critical-point parametrization
\[
g(T)=(T-y)^2+t.
\]
Since \(g\) is irreducible, \(-t\) is a nonsquare and \(t\ne0\). The condition \((f+c)(y)=0\) becomes \(t^2=-c\), giving exactly \(qH(-c)\) such quartics. The reverse case, where \(f+c\) is an irreducible-quadratic square and \(f\) has a rational repeated root, contributes \(qH(c)\). These classes are disjoint from the rational/rational cases. Thus, for all odd \(q\),
\[
B_q(c)=q(q-1)+q\left(H(c)+H(-c)-\frac{R_4(c)+R_4(-c)}2\right).\tag{1}
\]

**Character classes.** When \(q\equiv3\pmod4\), precisely one of \(c,-c\) is a square; for that value \(s\), \(R_4(s)=2\) and \(H(s)=1\). Formula (1) gives \(B_q(c)=q(q-1)\). When \(q\equiv1\pmod4\), \(c,-c\) have the same quadratic character. If both are nonsquares, the correction in (1) vanishes. For a square \(s\), if \(s\) is a fourth power, \((R_4(s),H(s))=(4,0)\); otherwise \((R_4(s),H(s))=(0,2)\). When \(q\equiv5\pmod8\), \(-1\) is a square but not a fourth power, so \(c,-c\) belong to opposite fourth-power classes and the corrections cancel. When \(q\equiv1\pmod8\), \(-1\) is a fourth power, and the corrections add to \(-4q\) for fourth-power \(c\) or \(+4q\) for square-non-fourth-power \(c\). This proves every odd-characteristic case.

**Characteristic two.** Write \(f=T^4+aT^3+bT^2+dT+e\). Then \(f'=aT^2+d\). If \(a=d=0\), both \(f\) and \(f+c\) have zero derivative and are nonsquarefree; there are \(q^2\) such monic quartics. If \(a=0,d\ne0\), both are squarefree. If \(a\ne0\), the derivative has exactly one root in \(k\), because squaring is a field automorphism, and \(f\) and \(f+c\) cannot both vanish there when \(c\ne0\). Thus \(B_q(c)=q^2\).

Finally, inclusion-exclusion gives \(C_q(c)=q^4-2q^3+B_q(c)\). The covariance and independence conclusions follow immediately, and multiplicative-group cyclicity yields the stated class frequencies.

## Verification
The included `verify.py` implements finite fields as polynomial quotients, and tests squarefreeness using an independent Euclidean polynomial-gcd algorithm, not the repeated-root incidence formulas. Run `python3 verify.py` in the extracted directory. It exhaustively enumerates all monic quartics and all nonzero shifts for field orders \(2,3,4,5,7,8,9,11,13,16,17\); it also enumerates all monic quartics for four selected nonzero shifts in order \(25\). The recorded result is `VERIFY_OK fields 12 shift_cases 88 quartics 596920`. These finite tests corroborate, but cannot establish, the universal formula.

## Relationship to prior work
Carmon and Rudnick's preprint (first publicly posted May 8, 2012, arXiv:1205.1599) proves a large-field Möbius autocorrelation bound, not an exact pair-squarefreeness count at fixed quartic degree. Keating and Rudnick (arXiv:1504.03444, Appendix A, Theorem A.2) study *the same pair-squarefreeness quantity* \(\sum_f\mu(f)^2\mu(f+J)^2\) for general polynomial shifts, but give a singular-series formula with an error term \(O(nq^{2n/3})\); at degree four the estimate does not yield the exact coefficient- and fourth-power-class dependence above. Carmon's characteristic-two extension (arXiv:1409.3694) treats Möbius correlations rather than this exact pair count. Almousa and Wood (arXiv:1210.0472) enumerate single-polynomial root-multiplicity types and do not incorporate a prescribed additive translation of the same polynomial. No assertion that the general study of squarefree pairs is new is made here.

## Limitations
The result is restricted to monic quartics and nonzero constant translations. It does not give higher-degree pair correlations or distributions for arbitrary nonconstant shifts. While the proof is complete and finite-field tests agree, unnoticed equivalent coverage in older discriminant, squarefree-tuple, or configuration-space literature cannot be ruled out. No independent mathematical audit has been performed.

## References
1. D. Carmon and Z. Rudnick, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599 (first posted 2012-05-08), https://arxiv.org/abs/1205.1599.
2. J. P. Keating and Z. Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444 (first posted 2015-04-14), Appendix A, https://arxiv.org/abs/1504.03444.
3. D. Carmon, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field in characteristic 2*, arXiv:1409.3694 (first posted 2014-09-12), https://arxiv.org/abs/1409.3694.
4. A. Almousa and M. Matchett Wood, *Counting polynomials over finite fields with given root multiplicities*, arXiv:1210.0472 (first posted 2012-10-01), https://arxiv.org/abs/1210.0472.
