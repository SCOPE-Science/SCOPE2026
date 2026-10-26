# The doubled nonordinary Hasse divisor of the bielliptic Picard family in every characteristic \(p\equiv1\pmod6\)

## Finding

Let \(p=6m+1\) be prime, \(m\ge1\). For the smooth one-parameter Picard family
\[
 C_a:\quad Y^3Z=X^4+aX^2Z^2+Z^4,\qquad a^2\ne4,
\]
over an algebraically closed field of characteristic \(p\), define
\[
 D(a)=a^2-4,\qquad Q_m(a)=[t^{3m}](t^2+at+1)^{2m}
 =\sum_{j=0}^{\lfloor m/2\rfloor}\frac{(2m)!}{(m+j)!(m-2j)!j!}a^{m-2j}.
\]
All factorials in this formula are evaluated as integers before reduction modulo \(p\). The polynomial \(Q_m\) has degree exactly \(m\), has \(m\) distinct geometric roots, and is coprime to \(D\). In the natural plane-quartic cohomology basis, the Hasse--Witt matrix is
\[
 H_a=K\,\operatorname{diag}\bigl(A D(a)^m,\ Q_m(a),\ B D(a)^m Q_m(a)\bigr),
\]
with nonzero constants in \(\mathbb F_p\)
\[
 K=\binom{6m}{2m},\quad A=\binom{4m}{2m},\quad
 B=\binom{4m}{m}\binom{2m}{m}^{-1}.
\]
Consequently, on \(\mathbb A^1_a\setminus V(D)\), the nonordinary Hasse divisor is exactly \(2V(Q_m)\): it consists of \(m\) distinct double points, length \(2m\). At each root, the Jacobian has geometric \(p\)-rank \(1\) and \(a\)-number \(2\); at every other smooth parameter the Jacobian is ordinary (rank \(3\), \(a\)-number \(0\)). There are no rank-zero or rank-two members in this family for these characteristics.

## Assumptions and scope

Here \(p\) ranges over **all** primes \(p\equiv1\pmod6\), with no upper bound; the base field is algebraically closed of characteristic \(p\). The curve is the entire smooth plane quartic, not merely the affine patch. Its plane model is smooth exactly when \(D(a)\ne0\): the unique point at infinity \([0:1:0]\) has nonzero \(Z\)-partial derivative, and on \(Z=1\) a singular point forces \(y=0\), \(4x^3+2ax=0\), and \(x^4+ax^2+1=0\), equivalent to \(a^2=4\). A smooth plane quartic has genus three. Multiplicities are on the *marked affine parameter line*, rather than on its moduli quotient (where \(a\) and \(-a\) may represent isomorphic curves).

## Proof

**1. The cohomological matrix.** Set \(F=Y^3Z-X^4-aX^2Z^2-Z^4\). From the exact sequence \(0\to\mathcal O_{\mathbb P^2}(-4)\xrightarrow{F}\mathcal O_{\mathbb P^2}\to\mathcal O_C\to0\), the standard Cech monomial basis of \(H^1(C,\mathcal O_C)\) corresponds to the degree-minus-four Laurent monomials
\[
 X^{-2}Y^{-1}Z^{-1},\quad X^{-1}Y^{-2}Z^{-1},\quad X^{-1}Y^{-1}Z^{-2}.
\]
The Frobenius matrix is obtained from coefficients of \(F^{p-1}\), with row \(i\), column \(j\) given by the monomial having exponent \(p(1+\delta_{ki})-(1+\delta_{kj})\) on variable \(k\). Off-diagonal coefficients vanish: all \(Y\)-exponents in \(F^{p-1}\) are divisible by three, while mixed \(X\)-to-\(Z\) exponents are odd and every monomial of \(F\) has even \(X\)-exponent. With
\[
 P_{r,s}(a)=[t^r](t^2+at+1)^s,
\]
the three diagonal coefficients, in the displayed order, are
\[
 K P_{6m,4m},\qquad K P_{3m,2m},\qquad K P_{3m,4m}.
\]
Indeed the \(Y^3Z\) factor occurs \(2m,4m,2m\) times respectively, and the remaining factors expand in powers of \(X^2/Z^2\). The overall signs are positive because their exponents \(4m,2m,4m\) are even.

**2. The first and third factorizations.** Write \(T=P_{6m,4m}\), \(R=P_{3m,4m}\), \(Q=P_{3m,2m}\), and \(D=a^2-4\). The polynomial \(T\) has degree \(2m\) with leading coefficient \(A=\binom{4m}{2m}\), nonzero modulo \(p\). For \(0\le j<m\), differentiation and evaluation at \(a=2\) give
\[
 T^{(j)}(2)=(4m)_j\binom{8m-2j}{6m-j} \equiv0\pmod p.
\]
The congruence follows from Lucas's theorem: the top has base-\(p\) digits \(1,2m-2j-1\), whereas the bottom \(6m-j<p\) exceeds the low digit. The same vanishing holds at \(a=-2\) because the underlying polynomial becomes \((t-1)^2\), with the corresponding sign. Thus \(D^m\) divides \(T\) modulo \(p\); comparing leading coefficients gives \(T=A D^m\).

The coefficient polynomial \(P_{r,s}\) satisfies, by direct binomial expansion and coefficient comparison, the identity
\[
 (a^2-4)P_{r,s}''+(1-2s)aP_{r,s}'+r(2s-r)P_{r,s}=0.
\]
In particular,
\[
 DQ''+(1-4m)aQ'+3m^2Q=0,\qquad
 DR''+(1-8m)aR'+15m^2R=0.
\]
Substituting \(D^mQ\) into the second differential operator and using the first gives \(-8m(6m+1)D^{m-1}Q=0\) modulo \(p\). The second equation has at most one polynomial solution of degree at most \(3m\) for each specified leading coefficient: its coefficient recurrence is
\[
 (n-3m)(n-5m)c_n=4(n+2)(n+1)c_{n+2},
 \quad0\le n<3m,
\]
with nonzero left multiplier modulo \(p=6m+1\). Both \(R\) and \(D^mQ\) have degree \(3m\), with leading coefficients \(\binom{4m}{m}\) and \(\binom{2m}{m}\) respectively. Therefore \(R=B D^mQ\). All three binomial constants \(K,A,B\) are nonzero because their factorial arguments are less than \(p\).

**3. Simple and interior roots.** The leading coefficient of \(Q\) is \(\binom{2m}{m}\ne0\), so its degree is \(m<p\). At \(a=2\), the coefficient definition gives \(Q(2)=\binom{4m}{3m}\ne0\), and at \(a=-2\) it differs only by the sign \((-1)^m\). If \(Q\) had a multiple root \(a_0\) away from \(D=0\), its differential equation would have a lowest-order nonzero term \(D(a_0)r(r-1)c(a-a_0)^{r-2}\), for multiplicity \(2\le r\le m<p\), a contradiction. Therefore all \(m\) roots are distinct and inside the smooth parameter locus.

**4. Scheme multiplicity and \(p\)-rank.** The determinant is
\[
 \det H=K^3AB D^{2m}Q^2.
\]
The factor \(D\) is a unit on the smooth parameter line, hence the Hasse section cuts out precisely the Cartier divisor \(V(Q^2)=2V(Q)\). The diagonal Frobenius action preserves three cohomology lines semilinearly, so its stable rank equals its matrix rank. At \(Q=0\) exactly one diagonal entry survives; otherwise all three survive. The \(p\)-rank is the stable Frobenius rank and the \(a\)-number is the dimension of the Cartier kernel, giving the announced strata.

## Verification

The bundled standalone Python program \(\texttt{CHECK.py}\) uses exact integer multinomial coefficients reduced modulo \(p\). It independently compares the three coefficient-polynomial identities, tests the two boundary values via polynomial greatest common divisors, and checks squarefreeness for twelve primes \(p=7,13,19,31,37,43,61,67,73,79,97,103\). It outputs \(\texttt{VERIFY\_OK}\). These finite tests provide reproducibility checks only; the preceding coefficient identities, polynomial ODE, and degree arguments prove the unlimited prime range.

For example, at \(p=7\), \(Q_1=2a\); at \(p=13\), \(Q_2=6a^2+4\); and at \(p=19\), \(Q_3=a^3-8a\), with coefficients read in the respective prime fields.

## Relationship to prior work

The bielliptic Picard family and its quaternionic Prym geometry are standard objects. Petkova--Shiga treat a Picard-family realization of the discriminant-six Shimura curve; their accessible description concerns complex uniformization rather than this positive-characteristic Hasse divisor. Kazemifard--Tafazolian classify Newton polygons for particular Fermat-related Picard curves, not this variable-parameter stratification. Takizawa's 2016 preprint gives finite-field hypergeometric formulas for Frobenius traces of a larger two-parameter Picard family, but does not state this exact diagonal Cartier matrix, uniform simple-root polynomial, or scheme-theoretic multiplicity. Laga--Shnidman analyze the same bielliptic family and its Prym surface, principally focusing on moduli, quaternionic multiplication, and rational arithmetic; the accessible complete text contains no corresponding Hasse-divisor classification. General Frobenius and modular-curve theories are relevant background but do not themselves constitute this explicit uniform formula without further derivation.

## Limitations

This is a statement only for prime characteristic \(p\equiv1\pmod6\) and the normalized affine family \(b=1\). It makes no claims for primes \(p\equiv5\pmod6\), for degenerate values \(a=\pm2\), for full Newton polygons or endomorphism rings of individual fibers, or for counting isomorphism classes of Picard curves. The historical possibility of equivalent formulas under a different Shimura-curve coordinate remains, especially because the complete Petkova--Shiga paper could not be inspected. Independent scholarly validation remains outstanding.

## References

1. M. Petkova and H. Shiga, *A new interpretation of the Shimura curve with discriminant 6 in terms of Picard modular forms*, Archiv der Mathematik 96 (2011), 335--348, DOI: 10.1007/s00013-011-0235-4.
2. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107--122, DOI: 10.1016/j.ffa.2014.12.002.
3. Y. Takizawa, *A Picard family of curves and hypergeometric functions over finite fields I*, arXiv:1608.07474 (first posted 2016-08-25), https://arxiv.org/abs/1608.07474.
4. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297, DOI: 10.1112/jlms.70347. Published online full text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70347.
