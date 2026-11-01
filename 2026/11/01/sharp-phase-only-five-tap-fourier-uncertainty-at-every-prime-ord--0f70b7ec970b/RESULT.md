# Sharp phase-only five-tap Fourier uncertainty at every prime order

## Finding
For every prime \(p\ge5\), set \(\zeta_p=e^{2\pi i/p}\). Among all polynomials
\[
P(z)=a_0+a_1z+a_2z^2+a_3z^3+a_4z^4,
\qquad |a_0|=\cdots=|a_4|=1,
\]
let \(Z_p(P)=\{k\in\{0,\ldots,p-1\}:P(\zeta_p^k)=0\}\). The **sharp phase-only Fourier-zero maximum** is
\[
\boxed{\max_{|a_j|=1}|Z_p(P)|=\begin{cases}4,&p=5,\\2,&p\ge7.\end{cases}}
\]
For every prime \(p\ge7\), an explicit five-tap polynomial has exactly the two zeros at \(\zeta_p\) and \(\zeta_p^{-1}\). In contrast, with unrestricted nonzero coefficients on the same five sites, the prime-cyclic uncertainty theorem permits four zeros at every prime \(p\ge5\).

## Assumptions and scope
The group is \(\mathbb Z/p\mathbb Z\), with prime \(p\ge5\). The five sites \(0,1,2,3,4\) are distinct. All five coefficient moduli are equal and nonzero; common scaling normalizes them to one. We use the Fourier convention \(\widehat f(k)=\sum_{j=0}^4f(j)e^{2\pi i kj/p}\) and identify it with \(P(\zeta_p^k)\). The opposite Fourier sign permutes the zero set and does not affect its cardinality. The theorem determines the **maximum number** of zeros, not all attainable Fourier-zero sets or counts. No statement is made for composite orders or nonconsecutive five-point supports.

## Proof
**Upper bound for primes above five.** Suppose \(p\ge7\) and a polynomial as above vanishes at three distinct \(p\)-th roots \(A,B,C\). Divide by its leading coefficient, preserving all coefficient moduli, and write its fourth root as \(u\). Put
\[
s=A+B+C,\qquad t=AB+AC+BC.\]
Since the constant and leading coefficients have equal absolute value, \(|ABC u|=1\), so \(|u|=1\). The first two elementary symmetric coefficients are \(e_1=s+u\) and \(e_2=t+us\); both have modulus one. Using \(\overline u=u^{-1}\), these two conditions give quadratic equations for \(u\):
\[
F(u)=\overline s\,u^2+s\overline s\,u+s=0,
\]
\[
G(u)=\overline t\,s\,u^2+(t\overline t+s\overline s-1)u+t\overline s=0.
\]
Every coefficient lies in the ring of cyclotomic integers \(R=\mathbb Z[\zeta_p]\). Since \(F\) and \(G\) have the common complex root \(u\), their Sylvester resultant vanishes **as an element of \(R\)**. Reduce this identity modulo the prime ideal \((1-\zeta_p)\); its residue field is \(\mathbb F_p\). All three chosen roots, their inverses, and their conjugates reduce to \(1\), so \(s,t,\overline s,\overline t\) reduce to \(3\). Consequently
\[
F(U)\equiv3U^2+9U+3,\qquad
G(U)\equiv9U^2+17U+9\pmod{1-\zeta_p}.
\]
Their resultant is the elementary integer determinant
\[
\det\begin{pmatrix}
3&9&3&0\\
0&3&9&3\\
9&17&9&0\\
0&9&17&9
\end{pmatrix}=900.
\]
Reduction of a vanishing resultant forces \(900\equiv0\pmod p\), impossible for any prime \(p\ge7\). Thus \(|Z_p(P)|\le2\).

**Sharpness for every prime above five.** Write \(c=\cos(2\pi/p)>0\) and \(v=c^2\). Define
\[
\alpha=\frac{16v^2-12v+3}{8c(1-2v)},\qquad
 a=\alpha+i\sqrt{1-\alpha^2},\qquad
 b=2-4v-2ca.
\]
We check that \(|\alpha|<1\) and \(v\ne1/2\). The exact identity
\[
1-\alpha^2=-\frac{(16v^2-28v+9)(16v^2-12v+1)}{64v(1-2v)^2}
\]
shows \(|\alpha|<1\) for
\[
\frac{3-\sqrt5}{8}<v<\frac{7-\sqrt{13}}8
\quad\text{or}\quad
\frac{3+\sqrt5}8<v<1.
\]
For \(p\ge11\), monotonicity of cosine gives \(c\ge\cos(2\pi/11)>\cos(\pi/5)=(1+\sqrt5)/4\); hence \(v>(3+\sqrt5)/8\). For \(p=7\), the number \(c=\cos(2\pi/7)\) is the unique positive root in \((3/5,5/8)\) of \(8c^3+4c^2-4c-1=0\), since the cubic is increasing there and has endpoint values \(-29/125\) and \(1/64\). Then \(9/25<v<25/64\), which lies inside \(((3-\sqrt5)/8,(7-\sqrt{13})/8)\). Thus \(a\) is well defined and \(|a|=1\). Also
\[
|b|^2=(2-4v)^2+4v-4c(2-4v)\alpha=1
\]
by the defining formula for \(\alpha\). The polynomial
\[
\begin{aligned}
P_p(z)&=(z^2-2cz+1)(z^2+(2c+a)z+1)\\
&=1+az+bz^2+az^3+z^4
\end{aligned}
\]
therefore has all five coefficient moduli equal to one, and vanishes at \(z=e^{\pm2\pi i/p}\). By the upper bound these are its only sampled zeros.

**The exceptional smallest prime.** At \(p=5\), the polynomial \(1+z+z^2+z^3+z^4\) has all four nontrivial fifth roots of unity as zeros; a nonzero quartic has at most four roots. This proves the displayed sharp classification.

## Verification
The self-contained standard-library Python program `artifacts/verify.py` recomputes the exact Sylvester determinant \(900\), checks the explicit coefficient moduli and both expected Fourier zeros for twenty-two primes from \(7\) through \(1009\), independently samples every Fourier frequency for these cases, and checks the exceptional fifth-order witness. It prints `FIVE_TAP_PHASE_ONLY_PRIME_FOURIER_OK` on success. Execute `python3 artifacts/verify.py` after extracting the file. The infinite result is established by the above exact resultant and inequalities; finite sampling is corroborative and does not prove the universal quantifiers.

## Relationship to prior work
Tao's sharp prime-cyclic uncertainty theorem gives \(|\operatorname{supp}f|+|\operatorname{supp}\widehat f|\ge p+1\), with every feasible support-cardinality pair attainable for arbitrary complex coefficients. For five supported sites it therefore allows four zeros but does **not** guarantee equal coefficient magnitudes. Krahmer, Pfander, and Rashkov discuss this theorem and finite-group short-time Fourier uncertainty without imposing the five-tap equal-modulus constraint.

Published phase-only classifications for three and four nonzero coefficients, and a classification for four consecutive coefficients at general cyclic orders, concern different support sizes and do not imply the five-coefficient conclusion. The known exact continuous fourth-moment optimum for a five-term phase-only polynomial is a different invariant; it neither counts zeros on a finite Fourier grid nor provides the present resultant obstruction. Lalín and Smyth study self-inversive polynomials and conditions for **all** their roots to lie on the unit circle, not the simultaneous requirement of unit coefficient moduli and **three prescribed prime-order roots**. The new obstruction is the reduction of two coefficient-modulus equations to a fixed nonzero cyclotomic resultant; the constructive half proves this is an exact maximum rather than just an exclusion.

## Limitations
The result does not classify all zero patterns or all phase choices, only the sharp maximum; and it does not extend automatically to arbitrary five-point supports or composite moduli. The originality review inspected the closely related complete publications and accessible mathematical records but cannot exclude a differently indexed old result in sequence design or cyclotomic-polynomial theory. There is no independent mathematical audit or validation.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, first public 2003-08-29, https://arxiv.org/abs/math/0308286.
2. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, first public 2006-11-16, https://arxiv.org/abs/math/0611493.
3. M. N. Lalín, C. J. Smyth, *Unimodularity of zeros of self-inversive polynomials*, arXiv:1201.0774v1, first public 2012-01-03, https://arxiv.org/abs/1201.0774.
