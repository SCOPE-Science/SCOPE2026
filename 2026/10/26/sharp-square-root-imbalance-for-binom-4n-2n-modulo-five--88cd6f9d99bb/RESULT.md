# Sharp square-root imbalance for \(\binom{4n}{2n}\) modulo five

## Finding
For each integer \(n\geq 0\), let \(w(n)\in\{-1,0,1\}\) be the signed representative of \(\binom{4n}{2n}\pmod 5\): residue \(1\) is represented by \(+1\), residue \(4\) by \(-1\), and residue \(0\) by \(0\). Only these three residues occur. Write
\[
D(X)=\sum_{0\leq n<X}w(n),\qquad
P(X)=\#\{0\leq n<X:w(n)=1\},\quad
Q(X)=\#\{0\leq n<X:w(n)=-1\}.
\]
Here \(X\geq1\) is an integer cutoff, and the summation is over integers. For every integer \(L\geq0\),
\[
P(5^L)+Q(5^L)=3^L,\qquad
D(5^L)=P(5^L)-Q(5^L)=\operatorname{Re}((1+i)(2+i)^L).
\]
Consequently
\[
P(5^L)=\tfrac12\bigl(3^L+\operatorname{Re}((1+i)(2+i)^L)\bigr),\quad
Q(5^L)=\tfrac12\bigl(3^L-\operatorname{Re}((1+i)(2+i)^L)\bigr).
\]
For every integer \(X\geq1\), the **global imbalance** obeys
\[
|D(X)|\leq\frac{8\sqrt5}{\sqrt5-1}\sqrt X.
\]
The exponent \(1/2\) is best possible, even on powers of five: the limit points of \(D(5^L)/5^{L/2}\), as \(L\to\infty\), fill the interval \([-\sqrt2,\sqrt2]\). In particular, the limsup of its absolute value is \(\sqrt2\). Thus the two nonzero residues are asymptotically balanced throughout arbitrary initial intervals, in the precise sense \(P(X)-Q(X)=O(\sqrt X)\).

## Assumptions and scope
All binomial coefficients are ordinary integer coefficients, with \(\binom00=1\). Base-five expansions may be padded with leading zero digits. The residue assertions concern precisely the sequence \(\binom{4n}{2n}\) modulo the prime \(5\); no claim is made for other moduli or other binomial families. The counts begin at \(n=0\), which is essential for the exact short-block identities.

## Proof
**Digit transducer.** Put \(m=2n\), so that \(\binom{4n}{2n}=\binom{2m}{m}\). Double the base-five digits of \(n\) from least significant to most significant. If the incoming carry is \(c\in\{0,1\}\) and the current digit is \(d\in\{0,1,2,3,4\}\), define \(e=(2d+c)\bmod5\) and outgoing carry \(c'=\lfloor(2d+c)/5\rfloor\). The produced digit \(e\) is a digit of \(m\). Lucas's congruence gives
\[
\binom{2m}{m}\equiv\prod_j\binom{2e_j}{e_j}\pmod5
\]
if every digit \(e_j\leq2\); if some digit exceeds \(2\), adding \(m\) to itself forces a carry in that position, so the coefficient vanishes modulo five. For permitted digits \(e=0,1,2\), the local factors are \(1,2,6\equiv1,2,1\pmod5\). The number \(h\) of digits equal to one is even, because \(m=2n\) is even and base five is odd: \(m\equiv\sum_j e_j\equiv h\pmod2\). Hence the nonzero product is \(2^h=i^h\in\{1,-1\}\) modulo five, where the real integer \(i^h\) is the chosen signed representative. This proves the three-residue restriction and permits complex weights \(1,i,1\) on produced digits \(0,1,2\), respectively, and weight zero otherwise.

For each input digit \(d\), define a two-state complex transition matrix \(A_d\), with row indexed by incoming carry and column by outgoing carry, whose sole possible nonzero row entry is the corresponding digit weight. An explicit list is
\[
A_0=\begin{pmatrix}1&0\\i&0\end{pmatrix},\quad
A_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
A_2=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
A_3=\begin{pmatrix}0&i\\0&1\end{pmatrix},\quad
A_4=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\]
The first row of \(A_1\) corresponds to produced digit two; the nonzero entries of \(A_2\) and \(A_3\) follow from the carry rule. Summation yields exactly
\[
M:=\sum_{d=0}^4A_d=\begin{pmatrix}2&i\\ i&2\end{pmatrix}.
\]
For a padded \(L\)-digit input with digits \(d_0,\ldots,d_{L-1}\), the final carry is an additional most significant digit of \(m\). It supplies terminal weights \(v=(1,i)^T\). Therefore, with \(u=(1,0)\),
\[
w(n)=u A_{d_0}A_{d_1}\cdots A_{d_{L-1}}v.
\]
This expression is real, as shown by the parity argument. Summing over all \(5^L\) inputs gives \(D(5^L)=uM^Lv\). Since \(M\) has eigenvalues \(2+i\) and \(2-i\), and \(v\) decomposes as \(\frac{1+i}{2}(1,1)^T+\frac{1-i}{2}(1,-1)^T\),
\[
uM^Lv=\tfrac12(1+i)(2+i)^L+\tfrac12(1-i)(2-i)^L
=\operatorname{Re}((1+i)(2+i)^L).
\]
Replacing every nonzero transition weight by one produces the matrix \(B=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), and terminal vector \((1,1)^T\). Since \(B(1,1)^T=3(1,1)^T\), the total number of nonzero terms is \(uB^L(1,1)^T=3^L\). This yields the exact signed counts.

**Arbitrary cutoffs.** Each fixed-digit matrix \(A_d\) has at most one nonzero entry of modulus one in each row. The same holds for any product of such matrices; therefore its operator norm is at most \(\sqrt2\). The matrix \(M\) is normal with both eigenvalues of modulus \(\sqrt5\), so \(\|M^j\|_2=5^{j/2}\). A complete block of \(5^j\) consecutive integers aligned at a multiple of \(5^j\) has freely varying low \(j\) digits and fixed high digits. Its signed sum has the form \(uM^jHv\), where \(H\) is a product of fixed-digit matrices. Its absolute value is at most \(2\cdot5^{j/2}\), since \(\|u\|_2=1\), \(\|H\|_2\leq\sqrt2\), and \(\|v\|_2=\sqrt2\).

If \(5^{L-1}<X<5^L\), the interval of integers \([0,X)\) is a disjoint union of at most four aligned complete blocks of length \(5^j\), for each \(0\leq j\leq L-1\). Consequently,
\[
|D(X)|\leq8\sum_{j=0}^{L-1}5^{j/2}
<\frac{8\cdot5^{L/2}}{\sqrt5-1}
\leq\frac{8\sqrt5}{\sqrt5-1}\sqrt X.
\]
For integral powers \(X=5^L\), the exact formula gives \(|D(X)|\leq\sqrt{2X}\), also within the stated bound. All cutoffs in this theorem are positive integers, so no boundary-rounding convention is required.

**Sharpness.** Write \(2+i=\sqrt5e^{i\theta}\), with \(\theta\in(0,\pi/2)\). If \(\theta/\pi\) were rational, \(\zeta=e^{2i\theta}=(3+4i)/5\) would be a root of unity. Yet \(\zeta+\zeta^{-1}=6/5\), a rational noninteger; this is impossible because the sum of roots of unity is an algebraic integer and every rational algebraic integer is integral. Hence \(\theta/\pi\) is irrational. The phases \(L\theta\pmod{2\pi}\) are dense on the circle, so
\[
D(5^L)/5^{L/2}=\operatorname{Re}((1+i)e^{iL\theta})
\]
has the full interval \([-\sqrt2,\sqrt2]\) as its limit-point set. The square-root exponent is therefore optimal.

## Verification
An independently implemented Lucas-digit computation of \(\binom{4n}{2n}\pmod5\) agrees with the two-state digit transducer for every \(0\leq n<5^7=78125\); the first 200 terms were also checked using ordinary exact integer binomial coefficients. For each \(1\leq L\leq7\), independent enumerations verify the two exact \(5^L\)-block counting identities, and all partial sums satisfy the asserted numerical square-root bound in this range. Run the standalone script with `python verify.py`; it uses only the Python standard library. These are finite consistency checks; the proof above supplies all infinite quantifiers.

## Relationship to prior work
The digit-carry obstruction \(\binom{4n}{2n}\pmod5\in\{0,1,4\}\) was reported in Yaqubi and Mirzavaziri (2017), Theorem 4.1, attributing it to Maxim Vsemirnov, as a counterexample to Guo and Krattenthaler's 2013 Conjecture 7.1. That residue **support restriction is not new**. Berend and Harmse (1998) establish distribution properties for the full middle-binomial sequence \(\binom{2m}{m}\) as \(m\) varies, not the even-index subsequence \(m=2n\). Barat and Grabner (2001) develop general digit-block distribution and spectral techniques for binomial coefficients across Pascal's triangle; those techniques are part of the classical context, but their full text does not state the particular signed finite-block identity or its sharp cancellation constant for this exceptional diagonal subsequence. The new assertion is precisely the exact imbalance formula, the optimal global square-root bound, and the sharp limit-point interval, not Lucas's theorem, the three-residue support, or a general digital-matrix method.

## Limitations
The theorem is specific to the modulus five, to central coefficients on even indices, and to the three-residue obstruction. No assertion is made about higher prime powers, other diagonal binomial families, or an explicit main term for nonzero counts at an arbitrary cutoff. A quantitatively equivalent statement might occur in unlocated literature, especially digital-sum specializations of general matrix methods. Independent mathematical validation has not been performed.

## References
- V. J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651 (first posted 2013-01-31), Conjecture 7.1, https://arxiv.org/abs/1301.7651 .
- S. Yaqubi and M. Mirzavaziri, *Some Divisibility Properties of Binomial Coefficients*, arXiv:1701.06217 (2017), Theorem 4.1 and its attribution to M. Vsemirnov, https://arxiv.org/pdf/1701.06217 .
- D. Berend and J. E. Harmse, *On some arithmetical properties of middle binomial coefficients*, Acta Arithmetica 84 (1998), 31–41, doi:10.4064/aa-84-1-31-41.
- G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society 64 (2001), 523–547, doi:10.1112/S0024610701002630, https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf .
