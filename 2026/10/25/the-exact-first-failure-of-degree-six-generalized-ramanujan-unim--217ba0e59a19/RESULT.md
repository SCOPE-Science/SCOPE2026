# The exact first failure of degree-six generalized Ramanujan unimodularity

## Finding
For every integer \(2\le N<163\) and every nonprincipal real Dirichlet character \(\chi\) modulo \(N\), all nonzero zeros of the generalized Ramanujan polynomial \(S_6(X;\chi,\chi)\) lie on the unit circle. At \(N=163\), the unique nonprincipal real character is the Legendre character, and its degree-six polynomial has four nonzero zeros off the unit circle. Consequently, **163 is the exact least modulus of a degree-six failure**, with imprimitive as well as primitive real characters included in the lower-modulus exclusion.

The lower range has a sharp quantitative separation from failure. If \(\chi\) is odd, \(N\le162\), and \(B_{1,\chi}\neq0\), then
\[
\frac{5B_{3,\chi}^{2}}{3B_{1,\chi}B_{5,\chi}}
\le \frac{378006}{390241}<1.
\]
Equality occurs only for the nonprincipal character modulo \(67\). At that modulus,
\[
S_6(X;\chi,\chi)=\frac1{12}(390241X^4+756012X^2+390241).
\]
At modulus \(163\), the corresponding ratio is exactly \(32155350/21322561>1\) and the polynomial is
\[
S_6(X;\chi,\chi)=\frac1{12}(21322561X^4+64310700X^2+21322561).
\]
The latter polynomial and its non-unimodular roots were already given by Pathak; the new assertions are **least-modulus minimality including imprimitive characters** and the **unique sharp pre-failure boundary at modulus \(67\)**.

## Assumptions and scope
A real Dirichlet character modulo \(N\) is a completely multiplicative function \(\chi:\mathbb Z\to\{0,\pm1\}\), periodic modulo \(N\), vanishing exactly on nonunits. The principal character is excluded. The generalized Bernoulli numbers are defined by
\[
\sum_{a=1}^{N}\chi(a)\frac{t e^{at}}{e^{Nt}-1}=\sum_{j\ge0}B_{j,\chi}\frac{t^j}{j!}.
\]
We use the usual Berndt–Straub normalization
\[
S_6(X;\chi,\chi)=\sum_{s=0}^{6}\frac{B_{s,\chi}B_{6-s,\chi}}{s!(6-s)!}X^{5-s}.
\]
The extreme terms vanish for every nonprincipal character, so this expression is a polynomial. Zeros at \(X=0\) are not counted as failures. No assertion is made for degree greater than six or for moduli beyond \(163\).

## Proof
**Reduction to an exact Bernoulli inequality.** For nonprincipal \(\chi\), \(B_{0,\chi}=0\). Parity implies \(B_{j,\chi}=0\) when \(\chi(-1)\ne(-1)^j\). For even \(\chi\), therefore,
\[
S_6(X;\chi,\chi)=\frac{B_{2,\chi}B_{4,\chi}}{48}(X^3+X).
\]
If it is nonzero, its nonzero roots are \(\pm i\). For odd \(\chi\),
\[
S_6(X;\chi,\chi)=\frac{B_{1,\chi}B_{5,\chi}}{120}(X^4+1)
+\frac{B_{3,\chi}^2}{36}X^2.
\]
If \(B_{1,\chi}=0\), there are no nonzero roots unless the polynomial vanishes identically. In the remaining cases, \(B_{1,\chi}B_{5,\chi}>0\); this positivity follows from the character \(L\)-value formula (and is also explicitly checked in the finite range below). With \(Y=X^2\), the polynomial is a positive multiple of \(Y^2+cY+1\) where \(c>0\). All roots satisfy \(|X|=1\) precisely when \(c\le2\); the criterion is
\[
5B_{3,\chi}^2\le3B_{1,\chi}B_{5,\chi}.
\]
Strict reverse inequality gives four purely imaginary off-circle roots.

**Complete enumeration of real characters.** Write \(U_N=(\mathbb Z/N\mathbb Z)^\times\), and let \(H_N=\{u^2:u\in U_N\}\). Every real character of \(U_N\) is trivial on \(H_N\), hence factors uniquely through \(U_N/H_N\). This quotient has exponent two and is an \(\mathbb F_2\)-vector space. Conversely every linear functional from this quotient to \(\mathbb F_2\) gives a real Dirichlet character. The verifier constructs all cosets, extends an explicit vector-space basis one coset at a time, and evaluates every nonzero functional. Thus there are no unexamined real characters, including those of smaller conductor than the modulus.

**Exact generalized Bernoulli calculations.** Let \(s_j=\sum_{a\in U_N}\chi(a)a^j\). Expansion of the defining generating function using the Bernoulli polynomials gives
\[
B_{1,\chi}=\frac{s_1}{N},\quad
B_{3,\chi}=\frac{s_3}{N}-\frac32s_2+\frac N2s_1,\quad
B_{5,\chi}=\frac{s_5}{N}-\frac52s_4+\frac{5N}{3}s_3-\frac{N^3}{6}s_1.
\]
Every \(s_j\) is an integer; all comparisons use exact rational arithmetic. For even characters the verifier additionally computes \(B_{2,\chi}=s_2/N-s_1\) and \(B_{4,\chi}=s_4/N-2s_3+Ns_2\).

The complete computation for \(2\le N\le163\) covers **433 nonprincipal real characters**, of which **173 are even** and **260 odd**. Among the odd characters, **85 have \(B_{1,\chi}=0\)**; all the other **175** have \(B_{1,\chi}B_{5,\chi}>0\). Exactly **one** of those 175 has the strict reverse inequality: the unique nonprincipal character at \(N=163\), with
\[
(B_{1,\chi},B_{3,\chi},B_{5,\chi})=(-1,13890,-213225610).
\]
Among the other 174, the unique largest ratio is \(378006/390241\), for \(N=67\), where
\[
(B_{1,\chi},B_{3,\chi},B_{5,\chi})=(-1,1506,-3902410).
\]
The values give the two displayed polynomial identities. This establishes both the least modulus and the strict sharp pre-failure separation. \(\square\)

## Verification
The standalone file `verify_ramanujan_min.py` is an exhaustive pure-Python certificate using only integer arithmetic, `math.gcd`, and `fractions.Fraction`. It generates all nonprincipal real characters as the nonzero dual functionals of the square-class quotient for every modulus from \(2\) through \(163\), independently checks character multiplicativity, computes the exact Bernoulli values, and asserts the first failure and unique near miss.

A successful execution prints `CERTIFICATE_OK moduli=2..163 nonprincipal_real=433 even=173 odd=260`, the case counts \(85\) and \(175\), and the exact unique ratios \(378006/390241\) and \(32155350/21322561\). The calculation checks the entire **finite** domain in the theorem; it does not use a sample to infer behavior for arbitrarily large moduli.

## Relationship to prior work
Berndt and Straub introduced these polynomial families and conjectured unimodularity for nonprincipal real characters (2014 preprint, Conjecture 7.9). They reported numerical verification for moduli at most \(100\) and degrees at most \(50\), but not a least failure. Pathak (2026, Example following Theorem 1.2) disproved the conjecture by giving the explicit four-root counterexample at \(N=163\), and proved a general bound of four exceptional roots; **that example and its coefficients are not new here**. Neither inspected source gives the exhaustive theorem for every modulus below \(163\), including imprimitive real characters, or identifies the exact sharp near-boundary ratio at \(67\). The proof above supplies both missing finite statements.

## Limitations
This is an exact finite classification through modulus \(163\), not a general unimodularity theorem in larger moduli or higher degree. The quantitative \(67\) bound concerns only odd characters with nonzero first generalized Bernoulli number. The finite certificate relies on correctness of transparent arithmetic and character enumeration; its independently reproduced outputs are not an external audit. An implicit earlier enumeration, or an unpublished computational search underlying the example at \(163\), remains a potential originality risk.

## References
1. Siddhi Pathak, *On Berndt–Straub conjectures about zeros of generalized Ramanujan polynomials*, arXiv:2610.18065v1, first submitted 13 October 2026. https://arxiv.org/html/2610.18065v1
2. Bruce C. Berndt and Armin Straub, *On a secant Dirichlet series and Eichler integrals of Eisenstein series*, arXiv:1406.2273v1, Section 7, 9 June 2014. https://arxiv.org/html/1406.2273v1
