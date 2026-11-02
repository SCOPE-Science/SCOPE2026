# A complete modulo-nine Lucas lift for Fibonacci-binomial coefficients

## Finding

For every pair of integers \(n\geq0\) and \(0\leq k\leq n\), the Fibonomial coefficient \(\left\langle\begin{smallmatrix}n\\k\end{smallmatrix}\right\rangle_F\) has an explicit residue modulo \(9\), given below using only ordinary binomial coefficients, division by \(4\), and units modulo \(9\). This determines all residue classes, including the coefficients divisible by \(3\) but not \(9\).

Write uniquely
\[
n=4m+r,\qquad k=4a+s,\qquad n-k=4b+t,
\]
where \(m,a,b\geq0\) and \(r,s,t\in\{0,1,2,3\}\). Define the units \(R_h(j)\in(\mathbb Z/9\mathbb Z)^\times\), for \(h\geq0\), by
\[
R_h(0)=1,\quad R_h(1)=(-1)^h(1-6h),\quad R_h(2)=1-6h,\quad R_h(3)=2(-1)^h\pmod9.
\]
Put \(W=R_m(r)R_a(s)^{-1}R_b(t)^{-1}\) in \(\mathbb Z/9\mathbb Z\). Then
\[
\boxed{\displaystyle
\left\langle\begin{matrix}n\\k\end{matrix}\right\rangle_F\equiv
\begin{cases}
W\binom ma,&s+t=r,\\[2pt]
6W(b+1)\binom ma,&s+t=r+4
\end{cases}\pmod9.}
\]
These are the only two cases. In particular the formula is unconditional, with no coprimality assumption on the ordinary binomial coefficient.

## Assumptions and scope

The Fibonacci integers are \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and the Fibonomial is the integer
\[
\left\langle\begin{matrix}n\\k\end{matrix}\right\rangle_F=
\frac{\prod_{i=1}^n F_i}{\left(\prod_{i=1}^k F_i\right)\left(\prod_{i=1}^{n-k}F_i\right)}.
\]
Empty products equal \(1\). All congruences and displayed inverses are in the ring \(\mathbb Z/9\mathbb Z\) unless otherwise specified. The statement covers all nonnegative \(n\) and valid \(k\), including boundaries \(k=0,n\), and each of the three possible residues modulo \(3\) and nine possible residues modulo \(9\).

## Proof

**A lifting lemma.** Put \(Q=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\) and \(B=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\). Then \(Q^4=-I+3B\), \((Q^j)_{12}=F_j\), \((B^2)_{12}=3\), and \((B^3)_{12}=8\). For every integer \(u\geq1\), the binomial expansion gives the identity in the \(3\)-adic integers
\[
\frac{(-1)^{u+1}F_{4u}}{3u}
=\sum_{j=1}^u\frac{(-1)^{j+1}3^{j-1}}j
\binom{u-1}{j-1}(B^j)_{12}.
\]
The first term is \(1\); the second vanishes modulo \(9\) because \((B^2)_{12}=3\); the third is \(24\binom{u-1}{2}\equiv3(u-1)(u-2)\pmod9\). For \(j\geq4\), \(\nu_3(3^{j-1}/j)\geq2\), so the remaining terms vanish modulo \(9\). Hence
\[
\frac{F_{4u}}{3u(-1)^{u+1}}\equiv
1+3(u-1)(u-2)\equiv7^{[3\mid u]}\pmod9.
\]
The right-hand side is a unit, proving at the same time \(\nu_3(F_{4u})=1+\nu_3(u)\). For indices not divisible by \(4\), use \(Q^{4u+j}\equiv(-1)^u(I-3uB)Q^j\pmod9\) to obtain
\[
\begin{aligned}
F_{4u+1}&\equiv(-1)^u(1-6u),\\
F_{4u+2}&\equiv(-1)^u,\\
F_{4u+3}&\equiv(-1)^u(2-6u)\pmod9.
\end{aligned}
\]
Each is a unit modulo \(3\).

**Fibotorial unit factorization.** For a nonzero integer \(z\), let \(u_3(z)=z/3^{\nu_3(z)}\), a \(3\)-adic unit. Define \(U_N=\prod_{j=1}^N u_3(F_j)\) and \(u_3(m!)=m!/3^{\nu_3(m!)}\). The preceding formulas show that the \(3\)-adic unit product of the four Fibonacci terms indexed \(4u+1,\ldots,4u+4\) is
\[
2\,u_3(u+1)7^{[3\mid(u+1)]}\pmod9.
\]
Multiplying complete blocks and then the remaining \(r\) terms proves
\[
\boxed{U_{4m+r}\equiv2^m7^{\lfloor m/3\rfloor}
 u_3(m!)R_m(r)\pmod9.}
\]
The corresponding valuation identity is
\[
\nu_3\!\left(\prod_{j=1}^{4m+r}F_j\right)=m+\nu_3(m!).
\]
Thus this unit identity and the valuation identity together determine Fibotorial quotients modulo \(9\) without dividing by a nonunit.

**Cancellation and the two carry cases.** From the three quotient–remainder decompositions in the statement, \(\delta=m-a-b\) is \(0\) if \(s+t=r\), and \(1\) if \(s+t=r+4\). Set \(\eta=\lfloor m/3\rfloor-\lfloor a/3\rfloor-\lfloor b/3\rfloor\). The valuation and unit formulas, combined before reduction modulo \(9\), give
\[
\left\langle\begin{matrix}n\\k\end{matrix}\right\rangle_F
\equiv3^\delta 2^\delta 7^\eta W\frac{m!}{a!b!}\pmod9.
\]
The final quotient here is an integer: it is \(\binom ma\) for \(\delta=0\), and \((b+1)\binom ma\) for \(\delta=1\). In the second case the initial factor \(3^\delta 2^\delta=6\) makes \(7^\eta\equiv1\pmod3\) irrelevant, proving the second branch.

In the first case \(m=a+b\). The integer \(\eta\) is \(0\) or \(1\); if it is \(1\), the least significant ternary digits of \(a\) and \(b\) add with a carry. By Lucas's congruence, \(3\mid\binom ma\). Therefore \(7^\eta\binom ma\equiv\binom ma\pmod9\), giving the first branch. This also handles zero or higher valuations uniformly. Both cases are proved for arbitrary valid indices.

## Verification

The standalone script `verify_mod9.py` implements the predicted formula using modular inverses and directly constructs Fibonacci integers and complete Fibotorial integers. It compares **all \(13{,}041\) coefficient pairs** in rows \(0\) through \(160\) against exact integer division, independently tests the intermediate unit-product lemma for \(161\) indices, and checks the valuation/residue consistency. Running `python3 verify_mod9.py` yields `VERIFY_OK integer_pairs= 13041 rows= 161 unit_product_checks= 161 modulus= 9`. These finite checks corroborate but do not replace the preceding proof.

## Relationship to prior work

Chen–Sagan (2013, arXiv:1306.2377) establish fractal congruences modulo \(2\) and modulo \(3\). DeBellevue–Kryuchkova (2018, Theorem 4.6) give the exact signed Lucas-type congruence for Fibonomials **modulo an odd prime** under their apparition-rank hypothesis, in particular modulo \(3\). The present formula reduces to that known congruence modulo \(3\); the reduction is not claimed as new. Its new content is the full first prime-square lift modulo \(9\), including coefficients of valuation exactly one and the first-order unit corrections.

Southwick (2016) studies Fibonomial divisibility and modulo \(5\), not a full modulo-\(9\) unit formula. Chand (2025) gives universal matrix products for generating functions of \(p\)-adic **valuations**, which determine divisibility but not residues of the nonzero \(p\)-adic units modulo \(9\). An ordinary-binomial Lucas congruence does not itself determine the Fibonomial unit correction. No equivalent full all-indices modulo-\(9\) congruence was located in the checked literature, but this is not a guarantee of historical uniqueness.

## Limitations

The result is specific to classical Fibonacci numbers and modulus \(9\). It does not establish a congruence modulo \(27\), for other Lucas sequences, or for arbitrary prime-power moduli. The work has received self-review, not independent audit. The literature comparison cannot exclude unlocated earlier equivalent congruences.

## References

1. Xi Chen and Bruce E. Sagan, *The fractal nature of the Fibonomial triangle*, arXiv:1306.2377v1, first submitted 2013-06-10; *Integers* 14 (2014), A3.
2. Michael DeBellevue and Ekaterina Kryuchkova, *Fractal Behavior of the Fibonomial Triangle Modulo Prime \(p\), Where the Rank of Apparition of \(p\) Is \(p+1\)*, *Fibonacci Quarterly* 56 (2018), 113–120, Theorem 4.6, doi:10.1080/00150517.2018.12427704.
3. Jeremiah Southwick, *A Conjecture concerning the Fibonomial Triangle*, arXiv:1604.04775v1 (2016).
4. Arav Chand, *Universal Matrices for Counting Fibonomial and \(C\)-nomial Coefficients by their \(p\)-adic Valuations*, arXiv:2508.18461v1 (2025).
5. Donald E. Knuth and Herbert S. Wilf, *The power of a prime that divides a generalized binomial coefficient*, J. Reine Angew. Math. 396 (1989), 212–219.
