# Exact trace fibers of squarefree self-reciprocal polynomials over odd finite fields

## Finding
Let \(q=p^r\) be any odd prime power, \(n\ge1\), and \(c\in\mathbb F_q\). Let \(N_{q,n}(c)\) count monic self-reciprocal, squarefree \(F\in\mathbb F_q[X]\) of degree \(2n\) whose coefficient at \(X^{2n-1}\) equals \(c\). Define the integer
\[
S_{q,n}=[z^n]\frac{1-qz^2}{(1-qz)(1+z)^2}
\]
and let
\[
M_{p,n}(c)=\#\{j\in\{0,\ldots,n\}:\ c=-2n+4j\text{ in }\mathbb F_q\}.
\]
The exact fiber count is
\[
\boxed{N_{q,n}(c)=\frac{S_{q,n}-(-1)^n(n+1)}{q}+(-1)^nM_{p,n}(c).}
\]
The displayed fraction is an integer. If \(n+1=ap+b\) with \(0\le b<p\), then \(M_{p,n}\) equals \(a+1\) on exactly \(b\) elements of the prime subfield, equals \(a\) on the other \(p-b\) elements of that subfield, and vanishes on the other \(q-p\) elements. Consequently, *all fibers are uniform if and only if \(q=p\) and \(p\mid(n+1)\)*. For prime fields the fiber counts differ by at most one; in extension fields they are nonuniform for every \(n\ge1\).

## Assumptions and scope
The characteristic \(p\) is odd, the degree is positive and even, every polynomial is monic with constant term one, and the squarefree condition is over an algebraic closure. Self-reciprocity means \(X^{2n}F(1/X)=F(X)\). The first non-leading coefficient is the additive statistic in the theorem. The prime-subfield membership in the multiplicity histogram is literal; a coefficient not in \(\mathbb F_p\) has multiplicity zero. Every count includes all factorization types permitted by squarefreeness, not only irreducibles.

## Proof
**Reciprocal reduction and separability.** Every monic self-reciprocal \(F\) of degree \(2n\) uniquely has the form
\[
F(X)=X^n g(X+X^{-1}),
\]
where \(g\in\mathbb F_q[Y]\) is monic of degree \(n\). Uniqueness follows by descending powers or the basis of symmetric Laurent polynomials \(1,X+X^{-1},\ldots,X^j+X^{-j}\). The coefficient of \(X^{2n-1}\) in \(F\) equals the coefficient \(u(g)\) of \(Y^{n-1}\) in \(g\). At a root of \(g\) other than \(\pm2\), the map \(X\mapsto X+X^{-1}\) has two distinct simple inverse images because its derivative \(1-X^{-2}\) is nonzero. At \(Y=2\) or \(Y=-2\), the inverse image is \(X=1\) or \(X=-1\), respectively, with ramification of degree two. Thus \(F\) is squarefree exactly when \(g\) is squarefree and \(g(2)g(-2)\ne0\). No assumption about splitting of \(g\) is necessary.

**Additive characters and Euler product.** For any monic polynomial \(g\), set \(u(g)\) to its next-to-leading coefficient and set \(u(1)=0\). The identity \(u(gh)=u(g)+u(h)\) holds for all monic \(g,h\). Fix an additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). In the formal series ring, the unrestricted monic generating function is
\[
U_\psi(z)=\sum_{g\text{ monic}}\psi(u(g))z^{\deg g}
=\begin{cases}(1-qz)^{-1},&\psi=1,\\1,&\psi\ne1.\end{cases}
\]
Indeed, at each positive degree the second-leading coefficient is uniformly distributed. Removing the two monic linear factors \(Y-2\) and \(Y+2\) multiplies \(U_\psi\) by \((1-\psi(-2)z)(1-\psi(2)z)\). Let \(U_\psi^{\!*}(z)\) denote the resulting generating function for monic polynomials not divisible by either linear factor. Unique factorization gives the squarefree Euler product
\[
R_\psi(z)=\frac{U_\psi^{\!*}(z)}{U_{\psi^2}^{\!*}(z^2)},
\qquad \psi^2(v):=\psi(2v).
\]
This holds as an identity of formal power series, since for each allowed monic irreducible \(P\) the local quotient is \((1-\psi(u(P))^2z^{2\deg P})/(1-\psi(u(P))z^{\deg P})=1+\psi(u(P))z^{\deg P}\).

For the trivial character, simplification gives
\[
R_1(z)=\frac{1-qz^2}{(1-qz)(1+z)^2}.
\]
For nontrivial \(\psi\), odd characteristic ensures \(\psi^2\) is nontrivial. Writing \(\alpha=\psi(-2)\) and \(\beta=\psi(2)=\alpha^{-1}\), we obtain
\[
R_\psi(z)=\frac{(1-\alpha z)(1-\beta z)}{(1-\alpha^2z^2)(1-\beta^2z^2)}
=\frac1{(1+\alpha z)(1+\beta z)}.
\]
Therefore its degree-\(n\) coefficient is
\[
[z^n]R_\psi(z)=(-1)^n\sum_{j=0}^n\psi(-2n+4j).
\]
This identity is exact for every nontrivial additive character, including all extension-field characters.

**Fourier inversion.** The number with prescribed next-to-leading coefficient \(c\) is, by orthogonality of the \(q\) additive characters,
\[
N_{q,n}(c)=\frac1q\sum_\psi\psi(-c)[z^n]R_\psi(z).
\]
For each of the \(n+1\) summands from the nontrivial characters, the identity \(\sum_{\psi\ne1}\psi(a)=q\,\mathbf1_{a=0}-1\) yields
\[
N_{q,n}(c)=\frac{S_{q,n}-(-1)^n(n+1)}q+(-1)^nM_{p,n}(c).
\]
Modulo the integer \(q\), the expression for \(R_1\) reduces to \((1+z)^{-2}\), proving \(S_{q,n}\equiv(-1)^n(n+1)\pmod q\) and the divisibility assertion.

**Complete multiplicity and equality classification.** The list \(-2n+4j\) as \(j\) runs from zero through \(n\) lies in \(\mathbb F_p\). Because \(4\) is invertible modulo odd \(p\), it runs through the \(p\) prime-subfield elements in successive complete cycles. Exactly \(b\) values occur \(a+1\) times and \(p-b\) occur \(a\) times, with \(n+1=ap+b\). When \(q=p\), uniformity is equivalent to \(b=0\), or \(p\mid n+1\). When \(q>p\), \(M_{p,n}\) is positive somewhere in the prime subfield and zero outside it; hence uniformity is impossible. This also proves the claimed sharp prime-field discrepancy.

## Verification
The accompanying standalone script `verify.py` uses only Python 3 standard library. Run `python3 verify.py`. It checks the formula for every coefficient in 25 field/degree cases over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\), \(\mathbb F_9\), and \(\mathbb F_{25}\), and independently checks the reciprocal transformation against direct polynomial-squarefreeness for all degree parameters \(n\le3\) in those cases. The successful run reported `VERIFY_OK cases=25 fibers=215 polynomials=32915 direct_transform_checks=19150`. This is finite corroboration only; the universal result follows from the formal-series proof.

## Relationship to prior work
The reciprocal substitution \(F(X)=X^n g(X+X^{-1})\) and the enumerations of irreducible self-reciprocal polynomials are classical and are not claimed as new. Kim, Song and Ri (2013) analyze generalized self-reciprocity, factor structure and repeated factors, but their inspected theorems do not count squarefree monic reciprocal polynomials according to the prescribed coefficient \(c\). The Handbook of Finite Fields explains the classical transformation and irreducible counts, but does not supply this coefficient-refined squarefree formula. Garefalakis (2011), Mattarei and Pizzato (2016), and Gao (2021) analyze **irreducible** reciprocal polynomials with prescribed coefficients; their settings impose a stronger irreducibility restriction and do not yield the stated squarefree fiber census without further argument. Price and Thompson (2022) count polynomials having reciprocal factors, rather than squarefree reciprocal trace fibers. The added result is the explicit squarefree additive-character sieve and the exact prime-versus-extension-field uniformity dichotomy.

## Limitations
The characteristic must be odd. The theorem counts all squarefree self-reciprocal monic polynomials with constant coefficient one; it does not resolve the full distribution of factorization patterns, joint distributions of multiple initial coefficients, or even-characteristic analogues. Equivalent coverage in an unlocated broader generating-function theorem cannot be excluded by literature searches alone. Garefalakis's full text was unavailable at the time of review, so only the available abstract and bibliographic description informed that comparison. Independent mathematical validation has not been performed.

## References
1. R. Kim, O.-H. Song and H.-C. Ri, *Some Properties of Generalized Self-reciprocal Polynomials over Finite Fields* (2013), arXiv:1302.3051v1, https://arxiv.org/abs/1302.3051.
2. G. L. Mullen and D. Panario, editors, *Handbook of Finite Fields* (2013), Section 3.1.3, https://jackgiffin.com/main/pdfs/Handbook-of-Finite-Fields-Gary-L-Mullen.pdf.
3. S. Mattarei and M. Pizzato, *Generalizations of self-reciprocal polynomials*, arXiv:1609.07677v1 (2016), https://arxiv.org/abs/1609.07677.
4. T. Garefalakis, *Self-reciprocal irreducible polynomials with prescribed coefficients*, Finite Fields and Their Applications (2011), https://doi.org/10.1016/j.ffa.2010.11.004.
5. *Enumeration of self-reciprocal irreducible monic polynomials with prescribed leading coefficients over a finite field*, arXiv:2109.09006 (2021), https://arxiv.org/abs/2109.09006.
6. *Palindromic Polynomials over Finite Fields*, arXiv:2210.15703 (2022), https://arxiv.org/abs/2210.15703.
