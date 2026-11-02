# Exact derivative-root law for cubic Möbius correlations in binary fields

## Finding
For an odd positive integer \(m\), set \(q=2^m\) and \(K=\mathbb F_q\). For pairwise distinct constants \(c_1,\ldots,c_k\in K\) with \(1\le k\le q\), define
\[
P(Y)=\prod_{i=1}^{k}(Y+c_i),\qquad
C(c_1,\ldots,c_k)=\sum_{\substack{f\in K[T]\\ f\text{ monic},\ \deg f=3}}\prod_{i=1}^k\mu(f+c_i).
\]
Then
\[
\boxed{C(c_1,\ldots,c_k)=q^2\#\{y\in K:P'(y)=0\}.}
\]
Thus the exact correlation is nonnegative, divisible by \(q^2\), and bounded above by \(q^2\lfloor(k-1)/2\rfloor\). This is a complete formula for every admissible shift set and every binary field of odd extension degree. In particular, for distinct constants, the two-point correlation vanishes; the three-point correlation is always \(q^2\); and the four-point correlation is \(q^2\) when \(c_1+c_2+c_3+c_4\ne0\), and zero otherwise.

## Assumptions and scope
The polynomial Möbius function is \(\mu(F)=0\) if \(F\) is not squarefree; otherwise \(\mu(F)=(-1)^j\), where \(j\) is the number of distinct monic irreducible factors of \(F\). Every summand is interpreted as an integer. The polynomial derivative \(P'\) is the *formal* derivative in characteristic two; distinct shifts imply \(P\) is squarefree. The assumption that \(m\) is odd is essential for the cube map to be bijective; no claim is made for even \(m\).

## Proof
Write a general monic cubic as
\[
f(T)=T^3+aT^2+bT+c\quad (a,b,c\in K).
\]
The translation \(T\mapsto T+a\) puts it in the form
\[
f(T+a)=T^3+uT+d,\qquad u=a^2+b,\quad d=ab+c.
\]
For each fixed \(a\), this is a bijection from coefficient pairs \((b,c)\) to \((u,d)\). The derivative of \(T^3+uT+d\) is \(T^2+u\), whose unique root is \(\sqrt u\). Substituting this root into the cubic gives \(d\); hence the cubic is squarefree exactly when \(d\ne0\). More generally, \(f+c_i\) is squarefree exactly when \(d+c_i\ne0\).

For a squarefree depressed cubic \(g(T)=T^3+uT+v\), the characteristic-two Berlekamp discriminant is
\[
\operatorname{Berl}(g)=1+\frac{u^3}{v^2}.
\]
The characteristic-two Pellet formula is \(\mu(g)=-\psi(\operatorname{Berl}(g))\), where \(\psi(z)=(-1)^{\operatorname{Tr}_{K/\mathbb F_2}(z)}\). Both identities occur in Carmon [1, §§2.1, 2.3]. Since \(m\) is odd, \(\psi(1)=-1\), giving the particularly simple exact formula
\[
\mu(T^3+uT+v)=\psi(u^3/v^2)\qquad(v\ne0).
\]
No singular cubic contributes to the desired correlation.

Let \(D=K\setminus\{c_1,\ldots,c_k\}\) (signs coincide in characteristic two). For each \(d\in D\), multiply the preceding formulas to obtain
\[
\prod_{i=1}^{k}\mu(f+c_i)=
\psi\!\left(u^3\sum_{i=1}^{k}\frac1{(d+c_i)^2}\right)
=\psi\!\left(u^3\left(\sum_{i=1}^{k}\frac1{d+c_i}\right)^2\right).
\]
For every \(a\) there is exactly one \((b,c)\) realizing a given \((u,d)\). Thus, summing over all cubics and using the \(q\) choices of \(a\),
\[
C(c_1,\ldots,c_k)=q\sum_{d\in D}\sum_{u\in K}\psi\!\left(u^3\left(\frac{P'(d)}{P(d)}\right)^2\right).
\]
Because \(m\) is odd, \(\gcd(3,q-1)=1\), so \(u\mapsto u^3\) permutes \(K\). The sum of a nontrivial additive character over \(K\) is zero; hence the inner sum is \(q\) if \(P'(d)=0\) and is zero otherwise. As \(P\) is squarefree, \(P'(c_i)\ne0\) for each \(i\). Therefore every \(K\)-root of \(P'\) is already in \(D\), proving the boxed identity.

For the bound, \(P'\) is a nonzero polynomial whose exponents are all even, hence is the square of a polynomial over the perfect field \(K\); it has at most \(\lfloor(k-1)/2\rfloor\) distinct roots. For two distinct shifts \(P'=c_1+c_2\ne0\); for three it is of the form \(Y^2+s\) and has exactly one root. For four shifts, writing \(s_j\) for the elementary symmetric sums of the \(c_i\) gives \(P'=s_1Y^2+s_3\). If \(s_1\ne0\), squaring is bijective and there is exactly one root. If \(s_1=0\), squarefreeness forces \(s_3\ne0\), so there are no roots. This proves all stated corollaries.

## Verification
The standalone script `verify_cubic_mobius.py` independently evaluates each cubic's Möbius value from its roots and derivative, not from its Berlekamp discriminant. It tests all nonempty shift subsets over \(\mathbb F_8\), along with tests over \(\mathbb F_2\) and \(\mathbb F_{32}\). A negative control over \(\mathbb F_4\) demonstrates why the odd-degree extension hypothesis cannot simply be dropped. Execute `python3 verify_cubic_mobius.py`. The observed summary is: `VERIFY_OK shift_sets 268 cubic_terms 458264 sharp_even_degree_control 32`.

## Relationship to prior work
Carmon [1] proves characteristic-two Chowla-type asymptotic cancellation estimates for general polynomial Möbius correlations (Theorem 1.1), and gives the cubic Berlekamp-discriminant formula and the corresponding Pellet identity (Section 2). The derivative-root equality here uses those valid starting identities but performs a distinct exact summation in the cubic constant-shift regime, resolving the correlation for *every* shift set when the extension degree is odd. The general bound does not imply this exact integer value, its positivity, its divisibility by \(q^2\), or the four-shift dichotomy. Carmon–Rudnick [2] deals with odd characteristic, so its general correlation estimate does not cover these binary fields. In particular, analogous two- and three-shift formulas for odd-characteristic fields do not imply the present all-order characteristic-two theorem. A search of the relevant literature and mathematical research records found no equivalent statement; historical coverage remains possible and independent evaluation is still needed.

## Limitations
The result is for monic degree-three polynomials, constant pairwise distinct shifts, and binary fields \(\mathbb F_{2^m}\) with odd \(m\). It is not a formula for even \(m\), higher polynomial degrees, nonconstant shifts, or repeated shifts. In fact, for \(q=4\) and shifts \(0,1\), direct calculation gives a two-point cubic correlation of \(32\), while \(P'\) has no roots: the odd-\(m\) hypothesis is substantive. Finite enumerations verify examples, not the universal statement. No independent mathematical audit has been performed.

## References
[1] D. Carmon, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field in characteristic 2*, arXiv:1409.3694v1, publicly posted 2014-09-12. https://arxiv.org/html/1409.3694v1 and https://arxiv.org/abs/1409.3694.

[2] D. Carmon and Z. Rudnick, *The autocorrelation of the Mobius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599, publicly posted 2012-05-08. https://arxiv.org/abs/1205.1599.
