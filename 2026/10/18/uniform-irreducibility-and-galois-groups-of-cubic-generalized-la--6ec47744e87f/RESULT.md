# Uniform irreducibility and Galois groups of cubic generalized Laguerre polynomials

## Finding

For every integer \(a\geq 0\), the generalized Laguerre polynomial \(L_3^{(a)}(X)\) is irreducible over \(\mathbb Q\). Its splitting-field Galois group is cyclic of order three precisely for \(a=3k^2-2\) with an integer \(k\geq1\), and is \(S_3\) for every other integer \(a\geq0\). In particular, the number of cyclic specializations with \(0\leq a\leq B\), for any integer \(B\geq0\), is exactly \(\left\lfloor\sqrt{(B+2)/3}\right\rfloor\).

The discriminant condition in this statement is already present in the 2013 work of Banerjee--Filaseta--Finch--Leidy. The additional point proved here is the **uniform absence of linear factors for every nonnegative integral parameter**, which makes the discriminant condition an unconditional complete Galois-group classification for the cubic family.

## Assumptions and scope

Use the standard generalized Laguerre normalization
\[
L_n^{(a)}(X)=\sum_{j=0}^n(-1)^j\binom{n+a}{n-j}\frac{X^j}{j!},
\qquad n\geq0,\quad a\in\mathbb Z_{\geq0}.
\]
The assertion concerns degree \(n=3\) and **all** integral parameters \(a\geq0\), with Galois groups taken over \(\mathbb Q\). It does not assert irreducibility at higher degrees or for all negative or nonintegral parameters.

## Proof

Multiplying \(L_3^{(a)}(X)\) by \(-6\) produces the monic integral polynomial
\[
P_a(X)=X^3-3AX^2+3A(A-1)X-A(A-1)(A-2),\qquad A=a+3\geq3.
\]
The integral translation \(Y=X-A\) changes \(P_a\) to
\[
F_A(Y)=Y^3-3AY-2A.
\]
A reducible monic cubic over \(\mathbb Q\) has an integer root. If \(Y=y\in\mathbb Z\) were a root, then
\[
y^3=A(3y+2).\tag{1}
\]
For odd \(y\), \(\gcd(y,3y+2)=\gcd(y,2)=1\). Equation (1) forces \(3y+2\mid1\). The sole integral possibility is \(y=-1\), which yields \(A=1\), contradicting \(A\geq3\).

For even \(y=2k\), equation (1) becomes
\[
4k^3=A(3k+1).
\]
As \(\gcd(k,3k+1)=1\), we have \(3k+1\mid4\). Among the divisors \(\{\pm1,\pm2,\pm4\}\), those congruent to \(1\) modulo \(3\) are \(1,-2,4\), giving respectively \(k=0,-1,1\). The corresponding values of \(A=4k^3/(3k+1)\) are \(0,2,1\), again incompatible with \(A\geq3\). Thus no integral root exists, so \(P_a\), and hence \(L_3^{(a)}\), is irreducible for every \(a\geq0\).

The discriminant of the depressed cubic is
\[
\Delta_a=-4(-3A)^3-27(-2A)^2=108A^2(A-1)=[6(a+3)]^2\,3(a+2).
\]
This is nonzero. It is a rational square precisely when \(3(a+2)\) is a square integer, which is equivalent to \(a+2=3k^2\) for an integer \(k\geq1\). An irreducible separable cubic has transitive Galois group either \(A_3\cong C_3\) or \(S_3\), and the group lies in \(A_3\) exactly when its discriminant is a square. This gives the claimed dichotomy.

The cyclic parameters are \(a=3k^2-2\), one for each \(k\geq1\). Counting those at most \(B\) gives \(\lfloor\sqrt{(B+2)/3}\rfloor\). Both Galois groups occur infinitely often, since the cyclic set is infinite and its complement among nonnegative integers is infinite.

## Verification

The accompanying standalone `verify.py`, using exact integer arithmetic and symbolic algebra, verifies the normalization, translated cubic, and discriminant identity; checks irreducibility and the square-discriminant criterion independently for all \(0\leq a\leq512\); and checks 60 further cyclic parameters of the form \(3k^2-2\). `verification_output.txt` records a successful execution. These are finite consistency checks; the proof for arbitrarily large \(a\) is the preceding divisibility argument, not the computation.

Execute from the directory containing both artifacts with `python3 verify.py` (requires SymPy).

## Relationship to prior work

Das--Dutta--Laishram--Nair (arXiv:2610.10614v1, 7 October 2026), Theorem 1.1, establishes irreducibility for parameters \(0\leq a\leq1000\), with explicit exceptions in degrees two and four. Their Theorem 1.2(ii) gives necessary prime-power conditions **if** a cubic Laguerre polynomial has an integer root; it does not assert uniform cubic irreducibility at all nonnegative parameters. The present root-divisibility argument excludes all such roots without a parameter cutoff.

Banerjee--Filaseta--Finch--Leidy (2013), Schur's discriminant identity and list (xiv) in Section 2, already identify the degree-three square-discriminant locus \(a=3k^2-2\). Their published Galois-group classification for nonnegative \(a\) is stated for \(a\leq10\) in Theorem 2.4, not for all parameters. Here the discriminant formula is **not** claimed as new; uniform irreducibility upgrades the known square locus to a complete Galois classification across all \(a\geq0\).

Laishram (2014/2015), Theorem 1.1, concerns only specified fractional parameters \(\pm1/2,\pm1/3,\pm2/3,\pm1/4,\pm3/4\). The theorem of Filaseta--Lam (2002), as quoted in both later primary papers, holds for sufficiently large **degree** with each fixed rational parameter, a different quantifier order. No equivalent unrestricted cubic irreducibility statement was identified in the examined sources.

## Limitations

This is a degree-three theorem, not a proof of any general higher-degree conjecture. The Galois-group square-discriminant condition predates this work. A mathematically equivalent unrestricted cubic irreducibility proof might exist in older or unindexed literature; absence from searches is not a proof of priority. Independent audit has not been performed.

## References

1. D. T. Das, S. Dutta, S. Laishram and S. G. Nair, *Irreducibility of Generalised Laguerre Polynomials for Large Integer Parameters*, arXiv:2610.10614v1 (7 October 2026), https://arxiv.org/html/2610.10614v1.
2. P. Banerjee, M. Filaseta, C. E. Finch and J. R. Leidy, *On classifying Laguerre polynomials which have Galois group the alternating group*, Journal de théorie des nombres de Bordeaux 25 (2013), 1--30, doi:10.5802/jtnb.822, https://www.numdam.org/article/JTNB_2013__25_1_1_0.pdf.
3. S. Laishram, *On the Galois groups of generalized Laguerre Polynomials*, Hardy--Ramanujan Journal 37 (2014), 8--12, https://hrj.episciences.org/1317/pdf.
4. M. Filaseta and T.-Y. Lam, *On the irreducibility of generalized Laguerre polynomials*, Acta Arithmetica 105 (2002), 177--182.
