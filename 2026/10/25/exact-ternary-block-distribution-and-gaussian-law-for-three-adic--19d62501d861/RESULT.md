# Exact ternary-block distribution and Gaussian law for three-adic Catalan valuations

## Finding

Let \(C_n=\binom{2n}{n}/(n+1)\) be the Catalan number, and let \(\nu_3\) denote the exponent of \(3\) in a positive integer. For every integer \(L\geq 0\) define the finite distribution polynomial
\[
P_L(u)=\sum_{0\leq n<3^L}u^{\nu_3(C_n)}.
\]
Then the following **exact bivariate rational generating function** holds as a formal power series in \(z\), with polynomial coefficients in \(u\):
\[
\boxed{\sum_{L\geq0}P_L(u)z^L=\frac{1+(1-2u)z}{1-2(1+u)z+3uz^2}.}
\tag{1}
\]
Equivalently, \(P_0(u)=1\), \(P_1(u)=3\), and
\[
\boxed{P_L(u)=2(1+u)P_{L-1}(u)-3uP_{L-2}(u)\qquad(L\geq2).}
\tag{2}
\]
For every \(L\geq1\), the attained valuations are **exactly** \(0,1,\ldots,L-1\), and precisely \(3\cdot2^{L-1}\) indices in the block have valuation zero.

If \(N_L\) is uniformly distributed on the \(3^L\) integers \(0\leq n<3^L\), and \(X_L=\nu_3(C_{N_L})\), then for every integer \(L\geq0\)
\[
\boxed{\mathbb E X_L=\frac L2-\frac34+\frac{3}{4\cdot3^L},}\qquad
\boxed{\operatorname{Var}(X_L)=\frac{8L-15+24\cdot3^{-L}-9\cdot3^{-2L}}{16}.}
\tag{3}
\]
In addition, as \(L\to\infty\),
\[
\boxed{\frac{X_L-L/2}{\sqrt{L/2}}\ \Longrightarrow\ \mathcal N(0,1).}
\tag{4}
\]
For any fixed integer \(r\geq0\), the number of indices with valuation exactly \(r\) also satisfies
\[
[u^r]P_L(u)=\frac{3\cdot2^L}{2}\,\frac{L^r}{4^r r!}+O_r(2^L L^{r-1})
\quad (L\to\infty),
\tag{5}
\]
where for \(r=0\) the main term is exact.

## Assumptions and scope

The integer \(n=0\) is included, with \(C_0=1\). An empty power \(3^0=1\) gives the one-element block \(\{0\}\). The indeterminate \(u\) marks the **exact** nonnegative three-adic valuation, and \(z\) marks the block length \(L\); neither is a residue variable. The identities (1)--(3) are valid at all specified finite values, and (4)--(5) are asymptotic statements only as \(L\to\infty\).

## Proof

**Carry model.** By Kummer's theorem, the valuation of \(\binom{2n}{n}\) equals the total number of carries, counted including a final carry, in the base-three sum \(n+n\). Therefore
\[
\nu_3(C_n)=\#\{\text{base-three carries in }n+n\}-\nu_3(n+1).
\tag{6}
\]
Represent each \(n<3^L\) using exactly \(L\) ternary digits, least significant first. If the entire string consists of the digit \(2\), then \(n=3^L-1\), the addition produces \(L\) carries, and \(\nu_3(n+1)=L\); this string contributes the monomial \(1\) to \(P_L\).

For every other string let \(t\) be the number of initial (least significant) digits equal to \(2\), so \(0\leq t<L\). Those \(t\) digits contribute exactly \(t\) carries, canceled by \(\nu_3(n+1)=t\). The first non-\(2\) digit is \(0\) or \(1\). If \(t=0\), both choices have outgoing carry zero and combined weight \(2\). If \(t\geq1\), a carry enters that digit: choosing \(0\) yields outgoing carry zero and weight \(1\), whereas choosing \(1\) yields outgoing carry one and weight \(u\).

Subsequent digits are governed by the weighted carry-transition matrix (rows are incoming carries \(0,1\), columns outgoing carries \(0,1\))
\[
T(u)=\begin{pmatrix}2&u\\1&2u\end{pmatrix}.
\tag{7}
\]
Indeed for incoming carry \(c\) and digit \(d\in\{0,1,2\}\), the outgoing carry is \(\lfloor(2d+c)/3\rfloor\), and each outgoing carry contributes a factor \(u\). Put \(e_0=(1,0)\), \(e_1=(0,1)\), and \(\mathbf1=(1,1)^T\). The trailing-digit decomposition is exhaustive and disjoint; for every \(L\geq1\),
\[
P_L(u)=1+2e_0T(u)^{L-1}\mathbf1+(e_0+ue_1)\sum_{j=0}^{L-2}T(u)^j\mathbf1.
\tag{8}
\]
The sum is empty for \(L=1\).

**Rational generating function.** Let \(D(z,u)=1-2(1+u)z+3uz^2\). Direct inversion gives
\[
(I-zT(u))^{-1}\mathbf1=\frac{1}{D(z,u)}\begin{pmatrix}1-uz\\1-z\end{pmatrix}.
\tag{9}
\]
Multiply (8) by \(z^L\) and sum over \(L\geq1\), adding \(P_0=1\). Using (9), the contributions of the all-\(2\) string, the \(t=0\) strings, and the \(t\geq1\) strings are, respectively, \(z/(1-z)\), \(2z(1-uz)/D\), and \(z^2(1+u-2uz)/((1-z)D)\). Simplification gives (1). Multiplying by its denominator proves (2).

**Support and zero valuation.** Setting \(u=0\) in (1) gives \(\sum_{L\geq0}P_L(0)z^L=(1+z)/(1-2z)\), hence \(P_L(0)=3\cdot2^{L-1}\) for \(L\geq1\). Every valuation is at most \(L-1\) because for a non-all-\(2\) digit string at least its first non-\(2\) digit contributes no valuation when \(t=0\), and after removing the \(t\) canceled low carries there remain at most \(L-t\) digits, with the earliest available outgoing carry at a strictly later digit if \(t=0\). For the exact upper bound more directly, \(t=0\) has first outgoing carry zero, giving at most \(L-1\) later carries; \(t\geq1\) has at most \(L-t\leq L-1\) remaining carries. Every \(r\in\{0,\ldots,L-1\}\) occurs: \(r=0\) uses \(n=0\), and \(r\geq1\) uses the ternary string with units digit \(0\), next \(r\) digits equal to \(2\), and all higher digits zero. Its only carries are those \(r\) digits, while \(3\nmid n+1\).

**Moments.** Differentiating (1) with respect to \(u\) and setting \(u=1\) gives
\[
G(z,1)=\frac1{1-3z},\quad
G_u(z,1)=\frac{3z^2}{(1-z)(1-3z)^2},\quad
G_{uu}(z,1)=\frac{6z^3(2-3z)}{(1-z)^2(1-3z)^3}.
\tag{10}
\]
Because \(P_L(1)=3^L\), coefficient extraction from (10) yields the exact expectation and variance in (3), including \(L=0\).

**Normal law.** The two characteristic roots of (2) are
\[
\lambda_{\pm}(u)=1+u\pm\sqrt{1-u+u^2}.
\tag{11}
\]
In a complex neighborhood of \(u=1\), choose the analytic square-root branch positive at \(u=1\). Solving the initial-value problem gives \(P_L(u)=a(u)\lambda_+(u)^L+(1-a(u))\lambda_-(u)^L\), where \(a(u)=(3-\lambda_-(u))/(\lambda_+(u)-\lambda_-(u))\), so \(a(1)=1\). As \(|\lambda_-(1)|=1<3=\lambda_+(1)\), the second term is exponentially negligible uniformly nearby. Direct Taylor expansion for small real \(s\) gives
\[
\log\!\left(\lambda_+(e^s)/3\right)=s/2+s^2/4+O(s^3).
\tag{12}
\]
For each fixed real \(t\), insert \(s=t/\sqrt{L/2}\) into the moment generating function \(3^{-L}P_L(e^s)\), and center by \(L/2\). Its logarithm tends to \(t^2/2\), the logarithm of the standard-normal moment generating function. The moment-generating-function continuity theorem proves (4).

**Fixed-valuation tails.** In a neighborhood of \(u=0\), the analytic roots satisfy \(\lambda_+(u)=2+u/2+O(u^2)\), \(\lambda_-(u)=O(u)\), and \(a(0)=3/2\). For each fixed \(r\), extracting \([u^r]\) from \(a(u)\lambda_+(u)^L\) gives \((3/2)2^L L^r/(4^r r!)+O_r(2^L L^{r-1})\). The other root contributes nothing for \(L>r\), because \(\lambda_-(0)=0\). This proves (5).

## Verification

The standalone `verify.py` uses the independent Legendre factorial-valuation identity
\[
\nu_3(C_n)=\sum_{j\geq1}\left(\left\lfloor\frac{2n}{3^j}\right\rfloor-\left\lfloor\frac n{3^j}\right\rfloor-\left\lfloor\frac{n+1}{3^j}\right\rfloor\right).
\]
It exhaustively compares direct valuation histograms against (2) for \(0\leq L\leq9\), independently compares the digit-carry formula for \(0\leq n<10000\), and compares exact rational moments against (3). Its successful output is:

`VERIFY_OK: 29524 valuation-census instances through L=9; 10000 digit-carry comparisons; exact rational moments and polynomial normalization`

For example, \(P_4(u)=24+24u+21u^2+12u^3\). Finite computation is a reproducibility check, **not** the proof of the infinite formulas or limit theorem.

## Relationship to prior work

The individual three-adic valuation \(\nu_3(C_n)\) has long been studied. OEIS A067397 was published in January 2002 and records individual terms and a 2015 digit-block recurrence. Alter and Kubota (1973) investigated divisibility of Catalan numbers by prime powers. Deutsch and Sagan (2004) studied congruences of Catalan and related numbers, including mod-three criteria; Chen and Jiang (2013) studied Catalan congruences modulo prime powers. Li (2018) presents individual prime-adic digit algorithms and divisibility consequences. These inputs establish valuation methods and congruence information, not by themselves a displayed two-variable census at every ternary-block length with exact variance and a Gaussian limit. Formula (1) aggregates all valuation levels simultaneously, while (3)--(5) describe exact and asymptotic population statistics. An unavailable full text of Alter and Kubota remains a specific risk for earlier priority or stronger coverage.

## Limitations

This result concerns only prime \(3\) and blocks \(0\leq n<3^L\), not arbitrary real cutoffs or simultaneous valuations at several primes. Formula (4) describes the bulk distribution and does not assert uniform local limit bounds. The earliest work of Alter and Kubota could not be fully inspected; the literature comparison is not an exhaustive guarantee of priority. The mathematical proof above is self-contained apart from classical Kummer's theorem and routine analytic continuity of moment generating functions.

## References

1. Henry Bottomley et al., OEIS A067397, "Maximal power of 3 that divides n-th Catalan number," first entry Jan. 22, 2002, https://oeis.org/A067397 .
2. R. Alter and K. K. Kubota, "Prime and prime power divisibility of Catalan numbers," *Journal of Combinatorial Theory, Series A* **15** (1973), 243--256, DOI:10.1016/0097-3165(73)90072-1.
3. E. Deutsch and B. E. Sagan, "Congruences for Catalan and Motzkin numbers and related sequences," arXiv:math/0407326v1, July 19, 2004, https://arxiv.org/abs/math/0407326 .
4. Y.-G. Chen and W. Jiang, "Catalan numbers modulo a prime power," *Integers* **13** (2013), A36, https://math.colgate.edu/~integers/n36/n36.pdf .
5. Tsz Chung Li, "On the Divisibility of Catalan Numbers," 2018, https://hlma.hanglung.com/assets/2127BE7E-4FF5-4E68-8A75-4268DE5AEB8E/007.pdf .
