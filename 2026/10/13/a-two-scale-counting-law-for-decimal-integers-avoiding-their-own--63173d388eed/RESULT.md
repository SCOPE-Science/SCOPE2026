# A two-scale counting law for decimal integers avoiding their own divisor digits

## Finding
A positive integer is *patterned* if some positive one-digit divisor occurs as a digit of its usual decimal representation; otherwise it is *unpatterned*. Let \(U(k)\) count the unpatterned positive integers having exactly \(k\) digits. There is an absolute constant \(\rho\), with \(7\le\rho<8\), such that
\[
U(k)=\frac{96}{7}9^{k-2}+\frac{5}{32}8^k+O(\rho^k)\qquad(k\to\infty).
\]
In particular, the second term is strictly separated from the error and has a positive coefficient. The three sources of the second term are exactly the restrictions arising from one additional excluded prime digit \(2\), \(3\), or \(7\).

## Assumptions and scope
All numerals use ordinary base ten; leading zeroes are forbidden; the digit \(0\) never divides a number. A number is unpatterned precisely when each digit \(d\in\{1,\ldots,9\}\) that actually occurs in it fails to divide the number. This is the complement of Campbell's definition [1], and no probabilistic independence between digit content and divisibility is assumed.

Put \(A=\{0,2,3,4,5,6,7,8,9\}\), and for \(p\in\{2,3,7\}\) put \(A_p=A\setminus\{p\}\). For an alphabet \(B\subseteq\{0,\ldots,9\}\) and \(q\in\{21,63\}\), define the finite spectral radius
\[
\vartheta(B,q)=\max_{1\le t<q}\left|\sum_{d\in B}e^{2\pi itd/q}\right|.
\]
One may take
\[
\rho=\max\{7,\vartheta(A,21),\vartheta(A_2,21),\vartheta(A_3,63),\vartheta(A_7,21)\}.
\]
We prove below that \(\rho<8\).

## Proof
**Digit-restricted modular equidistribution.** If \(q\) is coprime to \(10\), consider integers obtained by appending \(j\) freely chosen digits from a fixed alphabet \(B\). The number of digit strings giving any specified residue modulo \(q\) is
\[
\frac{|B|^j}{q}+O_q(\vartheta(B,q)^j),
\]
uniformly over the initial residue and the terminal target. Indeed, Fourier inversion expresses the indicator of the target residue as \(q^{-1}\sum_{t=0}^{q-1}e^{2\pi it(n-r)/q}\). For nonzero \(t\), the digit product has factors \(\sum_{d\in B}e^{2\pi i(10^h t)d/q}\); because \(10\) is invertible modulo \(q\), every factor has absolute value at most \(\vartheta(B,q)\). A prescribed first digit, finitely many prescribed last digits, and a finite union of residue classes only change the fixed multiplicative constant.

For \(A_2,A_3,A_7\), the differences of alphabet digits have gcd one. Hence the triangle inequality is strict for every nonzero additive character, and \(\vartheta(A_p,q)<8\) for each indicated modulus. For \(A\), we need \(\vartheta(A,21)<8\), rather than merely \(<9\). If \(3\nmid t\), the phases of the digits \(0\) and \(7\) sum to a complex number of absolute value \(1\), and the remaining seven phases sum to absolute value at most \(7\). Equality at \(8\) is impossible because the phases for digits \(2\) and \(3\) differ. If \(3\mid t\) but \(21\nmid t\), one may choose \(d\in A\) so that \(td\equiv9\) or \(12\pmod{21}\), since \(A\) contains every residue class modulo \(7\). Then the phases of digits \(0,d\) sum to absolute value \(2\cos(3\pi/7)<1\), and the seven others contribute at most \(7\). Thus \(\vartheta(A,21)<8\) and \(\rho<8\).

**Disjoint main classes.** Any unpatterned number omits digit \(1\). Define four classes of \(k\)-digit integers:
\[
\begin{aligned}
E&=\{n:1\text{ is absent},\ \gcd(n,210)=1\},\\
F_2&=\{n:1,2\text{ are absent},\ \nu_2(n)=1,\ \gcd(n,105)=1\},\\
F_3&=\{n:1,3\text{ are absent},\ \nu_3(n)=1,\ \gcd(n,70)=1\},\\
F_7&=\{n:1,7\text{ are absent},\ 7\mid n,\ \gcd(n,30)=1\}.
\end{aligned}
\]
All four classes are unpatterned: each candidate divisor digit between \(2\) and \(9\) has a prime divisor in \(\{2,3,5,7\}\); when such a prime divides the number it is either absent as a digit, or no such prime divides it. The four classes are disjoint by their mutually exclusive prime-divisibility conditions.

For \(E\), the first digit has eight possibilities, the last digit must be \(3,7,9\), and the \(k-2\) unrestricted middle digits lie in \(A\). The residue modulo \(21\) must be coprime to \(21\), occupying a fraction \(12/21=4/7\). Therefore
\[
|E|=8\cdot3\cdot\frac47\,9^{k-2}+O(\rho^k)=\frac{96}{7}9^{k-2}+O(\rho^k).
\]
For \(F_2\), the leading digit has seven choices, the \(k-3\) middle digits eight choices, and there are exactly twelve permitted last-two-digit strings satisfying \(n\equiv2\pmod4\) and ending in a digit coprime to \(5\). Specifically, the units digit is \(4\) or \(8\) with odd tens digit, or \(6\) with even tens digit, all chosen from \(A_2\). The residue modulo \(21\) is coprime to \(21\) for a fraction \(4/7\), so
\[
|F_2|=7\cdot12\cdot\frac47\,8^{k-3}+O(\rho^k)=\frac{3}{32}8^k+O(\rho^k).
\]
For \(F_3\), there are seven leading digits, eight unrestricted middle digits, and two allowed final digits \(7,9\) (odd and coprime to \(5\)). The residue modulo \(63\) must lie in one of the two residue classes \(3,6\pmod9\), while being coprime to \(7\), a fraction \((2/9)(6/7)=4/21\) of all residues. Hence
\[
|F_3|=7\cdot2\cdot\frac4{21}\,8^{k-2}+O(\rho^k)=\frac1{24}8^k+O(\rho^k).
\]
For \(F_7\), again seven leading digits and eight choices for each middle digit; the last digit is \(3\) or \(9\), and the residue modulo \(21\) must be zero modulo \(7\) but nonzero modulo \(3\). This occupies \(2/21\) of the residues. Consequently
\[
|F_7|=7\cdot2\cdot\frac2{21}\,8^{k-2}+O(\rho^k)=\frac1{48}8^k+O(\rho^k).
\]

**Remainder.** Let \(n\) be unpatterned outside these four classes. Some prime \(p\in\{2,3,5,7\}\) divides \(n\), and the digit \(p\) must be absent. If \(5\mid n\), then digit \(5\) is absent, so \(n\) ends in \(0\), and \(2\mid n\) as well: digits \(2,5\) are both absent. Otherwise, if \(2\mid n\) and no other prime of \(\{3,5,7\}\) divides \(n\), exclusion from \(F_2\) forces \(4\mid n\), so digits \(2,4\) are absent. Similarly, if \(3\mid n\) and none of \(2,5,7\) divides \(n\), exclusion from \(F_3\) forces \(9\mid n\), so digits \(3,9\) are absent. Finally, if \(7\mid n\), exclusion from \(F_7\) forces an additional prime divisor among \(2,3,5\). Thus every residual \(n\) omits digit \(1\) and at least two distinct further digits from \(\{2,\ldots,9\}\). A union bound over the \(\binom82\) possible pairs gives at most \(\binom82\cdot7^k=O(7^k)\) integers, counting leading-zero strings harmlessly. Combining the four disjoint asymptotics and \(3/32+1/24+1/48=5/32\) proves the asserted formula.

## Verification
The accompanying `verify.py` independently enumerates the complement of the digit-divisor property for all two- through six-digit positive integers, separately counts the four disjoint classes, and checks their union and residual cardinalities against an exact output table. It also checks that the four indicated finite Fourier radii are strictly smaller than \(8\) numerically. These finite checks supplement, but do not replace, the analytic argument above.

## Relationship to prior work
Campbell [1] introduced the decimal digit-divisor property, gave a finite enumeration, and suggested further asymptotic investigation; the paper does not state a \(k\)-digit asymptotic, nor an \(8^k\) correction. Maynard [2] studies the considerably different counting question of *primes* avoiding a specified digit; that prime theorem does not directly yield this digit-divisor complementary count or the three-prime correction coefficient. The elementary Fourier argument here uses the standard restricted-digit modular equidistribution method. No claim is made that restricted-digit Fourier techniques themselves are new.

## Limitations
This proves a two-term asymptotic for *exactly* \(k\)-digit decimal integers only. It does not give a uniform sharp asymptotic at arbitrary decimal cutoffs, a closed exact formula for every \(U(k)\), or a prime-number analogue. The constant \(\rho\) is explicit as a maximum of finite spectral radii but is not claimed to be the optimal third exponential rate. The proof does not establish independent confirmation of novelty or a complete classification of all residual configurations.

## References
[1] J. T. M. Campbell, *Patterned Numbers: A Novel Number Classification with Structural and Quantum Algebraic Perspectives*, arXiv:2601.07846v1, first posted 6 January 2026, https://arxiv.org/html/2601.07846v1.

[2] J. Maynard, *Primes with restricted digits*, Inventiones Mathematicae **217** (2019), 127–218; first preprint arXiv:1604.01041v1, https://arxiv.org/abs/1604.01041.
