# Sharp one-step p-adic lift for prime-power hook/core congruences
## Finding
For every prime \(p\), every integer \(a\ge 1\), and \(t=p^a\), define
\[
A(x)=\prod_{m\ge1}(1-x^m),\qquad
F_{t^2}(x)=A(x)^{t^2-1}=\sum_{n\ge0}a_t(n)x^n,
\]
and
\[
C_t(x)=\prod_{m\ge1}\frac{(1-x^{tm})^t}{1-x^m}=\sum_{n\ge0}b_t(n)x^n.
\]
Then
\[
a_t(n)\equiv b_t(n)\pmod{p^{a+1}}\qquad(n\ge0).
\]
Moreover this exponent is best possible: at \(n=p^{a-1}\),
\[
v_p\!\left(a_t(n)-b_t(n)\right)=a+1.
\]
Thus the largest power of \(p\) dividing every coefficient difference is exactly \(p^{a+1}\).

## Assumptions and scope
All identities are in the integral formal-power-series ring \(\mathbb Z[[x]]\). The parameter \(p\) is an arbitrary prime, including \(p=2\), and \(a\ge1\). No analytic convergence or modular-form input is required. The result concerns the p-adic strength of the coefficient congruence for prime-power \(t\); it does not address non-prime-power \(t\), for which the motivating work proves a different obstruction.

## Proof
Put
\[
B_j(x)=A\!\left(x^{p^j}\right),\qquad
R_j(x)=\frac{B_j(x)^p}{B_{j+1}(x)}.
\]
The Freshman's-dream congruence gives \(B_j(x)^p\equiv B_{j+1}(x)\pmod p\). Since \(B_{j+1}(0)=1\), division by \(B_{j+1}\) is legitimate in \(\mathbb Z[[x]]\), and hence
\[
R_j(x)\in 1+p\mathbb Z[[x]].
\]

We use the elementary lifting fact that if \(U\in1+p\mathbb Z[[x]]\), then for every integer \(r\ge0\),
\[
U^{p^r}\equiv1\pmod{p^{r+1}}.
\]
Indeed the case \(r=0\) is immediate. If \(U^{p^r}=1+p^{r+1}V\), the binomial expansion of \((1+p^{r+1}V)^p\) shows that every nonconstant term is divisible by \(p^{r+2}\). This also covers \(p=2\).

The ratios telescope exactly:
\[
\frac{A(x)^{p^{2a}}}{B_a(x)^{p^a}}
 =\prod_{j=0}^{a-1}R_j(x)^{p^{2a-j-1}}.
\]
For the factor indexed by \(j\), the lifting fact gives congruence to \(1\) modulo \(p^{2a-j}\). The weakest modulus occurs at \(j=a-1\), where it is \(p^{a+1}\). Therefore
\[
A(x)^{p^{2a}}\equiv B_a(x)^{p^a}\pmod{p^{a+1}}.
\]
Because \(A(0)=1\), division by \(A\) preserves this coefficientwise congruence, and
\[
F_{t^2}(x)=\frac{A(x)^{p^{2a}}}{A(x)}
\equiv
\frac{B_a(x)^{p^a}}{A(x)}=C_t(x)
\pmod{p^{a+1}}.
\]
This proves the uniform congruence.

For sharpness, write \(m=p^{a-1}\). Since \(A(x)=1-x+O(x^2)\),
\[
R_0(x)=\frac{A(x)^p}{A(x^p)}=1-px+O(x^2),
\]
so
\[
R_{a-1}(x)=R_0(x^m)=1-px^m+O(x^{2m}).
\]
Consequently the coefficient of \(x^m\) in \(R_{a-1}(x)^{p^a}\) is exactly \(-p^{a+1}\). Every earlier telescoping factor \(R_j^{p^{2a-j-1}}\), with \(j\le a-2\), is congruent to \(1\) modulo \(p^{a+2}\). Also \(B_a(x)^{p^a}\) has no positive term below degree \(p^a>m\). Hence the coefficient of \(x^m\) in
\[
A(x)^{p^{2a}}-B_a(x)^{p^a}
\]
is congruent to \(-p^{a+1}\) modulo \(p^{a+2}\), while all lower coefficients are divisible by \(p^{a+2}\). Multiplication by \(A(x)^{-1}\), whose constant coefficient is \(1\), therefore preserves that residue at degree \(m\). Thus
\[
v_p\!\left(a_t(p^{a-1})-b_t(p^{a-1})\right)=a+1.
\]

## Verification
The proof above is exact and does not depend on finite computation. A standalone integer-arithmetic script in `artifacts/verify.py` independently expands the two products through degree \(24\) for seven test pairs \((p,a)\), checks divisibility by \(p^{a+1}\) in every computed coefficient, and checks the claimed exact valuation at \(n=p^{a-1}\). Its replay output is:

`VERIFY_OK cases=7 sharp=[(2, 1, 1, -4, 2), (2, 2, 2, 88, 3), (2, 3, 4, 478480, 4), (3, 1, 1, -9, 2), (3, 2, 3, -75843, 3), (5, 1, 1, -25, 2), (7, 1, 1, -49, 2)]`

These finite checks are sanity tests only; the infinite statement follows from the formal-series proof.

## Relationship to prior work
Sharma's 2026 preprint proves that \(a_t(n)\equiv b_t(n)\pmod t\) for every \(n\) exactly when \(t\) is a prime power, and proves the stronger modulus \(p^2\) when \(t=p\) is prime. Its prime-power proposition records modulus \(p^a\) for \(t=p^a\), while its numerical section explicitly suggests that the prime-power case may admit a lift to higher p-adic orders. The result here supplies a uniform lift for every exponent \(a\) and identifies the exact universal p-adic modulus by an explicit sharp coefficient.

Han and Ono's earlier work compares the same two generating functions at \(t=3\) through the zero sets of their coefficients, using modular forms; it does not give the general prime-power coefficient congruence or its exact p-adic exponent.

## Limitations
The theorem determines only the common p-adic divisibility of the coefficient differences. It does not claim that \(p^{a+1}\) is the largest arbitrary integer modulus common to all differences, nor does it classify the valuations at coefficients other than the sharp witness \(n=p^{a-1}\). The finite verifier samples low degrees and is not a proof of the universal quantifiers.

## References
1. Meenu Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and t-Core Partitions*, arXiv:2610.01422v1, first submitted 2026-10-01.
2. Guo-Niu Han and Ken Ono, *Hook Lengths and 3-Cores*, Annals of Combinatorics 15 (2011), DOI 10.1007/s00026-011-0096-3.
