# Exact trace–constant squarefree fibers over all binary finite fields

## Finding

Fix a finite field \(\mathbb F_q\), where \(q=2^r\) and \(r\ge1\). For an integer \(n\ge2\), \(t\in\mathbb F_q\), and \(c\in\mathbb F_q^\times\), let \(N_{n,q}(t,c)\) denote the number of squarefree monic polynomials
\[
f(X)=X^n+tX^{n-1}+a_2X^{n-2}+\cdots+a_{n-1}X+c
\]
over \(\mathbb F_q\). At \(n=2\), the string of middle coefficients is empty. A polynomial is squarefree if it has no repeated irreducible factor. Then
\[
\boxed{N_{n,q}(t,c)=\begin{cases}
\dfrac{q^{n-1}-q(-1)^n}{q+1},&t=0,\\[3pt]
\dfrac{q^{n-1}+(-1)^n}{q+1},&t\ne0.
\end{cases}}
\]
In particular the answer is independent of the chosen nonzero constant term, and depends on the trace coefficient only through its vanishing. The difference between the zero and nonzero trace fibers is exactly \((-1)^{n+1}\); all fibers are nonempty except the zero-trace degree-two case.

## Assumptions and scope

The field has characteristic two, its size is an arbitrary power \(q=2^r\), \(n\ge2\), and the prescribed constant \(c\) is nonzero. Here the coefficient of \(X^{n-1}\), rather than its negative, is called the trace coefficient; in characteristic two the two conventions coincide. No irreducibility restriction is imposed: squarefree reducible polynomials are included. The case \(n=1\) is excluded because the trace and constant constraints then describe the same coefficient. There is no assertion for odd-characteristic fields or zero constant term.

## Proof

For each monic polynomial \(f\) with nonzero constant term define \(b(f)\) to be its coefficient immediately below the leading coefficient; take \(b(1)=0\). Let \(c(f)=f(0)\), with \(c(1)=1\). The fundamental identities under multiplication are \(b(fg)=b(f)+b(g)\) and \(c(fg)=c(f)c(g)\).

For an additive character \(\psi\) of \(\mathbb F_q\) and a multiplicative character \(\chi\) of \(\mathbb F_q^\times\), form the formal series
\[
Z_{\psi,\chi}(u)=\sum_{f\text{ monic},\,c(f)\ne0}
 \psi(b(f))\chi(c(f))u^{\deg f}.
\]
Its degree-zero coefficient is \(1\). For every degree \(d\ge2\), the coefficient \(b(f)\) and the constant \(c(f)\) vary independently and freely, with \(q^{d-2}\) choices of remaining coefficients, so
\[
[u^d]Z_{\psi,\chi}=q^{d-2}
 \Big(\sum_{b\in\mathbb F_q}\psi(b)\Big)
 \Big(\sum_{c\in\mathbb F_q^\times}\chi(c)\Big).
\]
The degree-one contribution is \(\sum_{c\ne0}\psi(c)\chi(c)\). Consequently the four cases are
\[
Z_{1,1}(u)=\frac{1-u}{1-qu},\quad
Z_{\psi,1}(u)=1-u\;(\psi\ne1),\quad
Z_{1,\chi}(u)=1\;(\chi\ne1),\quad
Z_{\psi,\chi}(u)=1+G_{\psi,\chi}u\;(\psi,\chi\ne1).
\]
The final Gauss-sum coefficient need not be evaluated.

Every monic polynomial of nonzero constant term has a unique decomposition \(f=g h^2\) with \(g\) monic squarefree and \(h\) monic, both of nonzero constant term. Its character weight factors as \(\psi(b(g))\chi(c(g))\cdot\psi^2(b(h))\chi^2(c(h))\). Thus the squarefree series satisfies
\[
S_{\psi,\chi}(u)=\frac{Z_{\psi,\chi}(u)}{Z_{\psi^2,\chi^2}(u^2)}.
\]
Every additive character has order dividing two because the field is of characteristic two. Every nontrivial multiplicative character has nontrivial square because \(q-1\) is odd. Substituting the four expressions for \(Z\) yields
\[
S_{1,1}(u)=\frac{1-qu^2}{(1-qu)(1+u)},\qquad
S_{\psi,1}(u)=\frac{1-qu^2}{1+u}\quad(\psi\ne1),
\]
whereas for \(\chi\ne1\), the series \(S_{\psi,\chi}\) has degree at most one. In every degree \(n\ge2\), therefore,
\[
[u^n]S_{1,1}=\frac{(q-1)(q^n-(-1)^n)}{q+1}=T_n,\qquad
[u^n]S_{\psi,1}=(1-q)(-1)^n=A_n
\]
for every nontrivial additive \(\psi\), with zero contribution whenever \(\chi\ne1\).

Apply Fourier inversion on the finite abelian group \((\mathbb F_q,+)\times(\mathbb F_q^\times,\cdot)\). For a fixed \(t\) and any \(c\ne0\), the sum over nontrivial additive characters is \(q-1\) when \(t=0\) and \(-1\) otherwise. Hence
\[
N_{n,q}(t,c)=\frac{T_n+A_n(q\mathbf1_{t=0}-1)}{q(q-1)}.
\]
Substituting \(T_n\) and \(A_n\) gives the two claimed formulas. Their difference is \((-1)^{n+1}\), and the numerator is nonnegative, vanishing only at \(n=2,t=0\). This proves all assertions. \(\square\)

## Verification

The attached `VERIFY.py` independently performs exhaustive enumerations of monic nonzero-constant polynomials over binary fields of sizes \(2,4,8,16\). For each fixed degree, trace coefficient and nonzero constant it tests squarefreeness by the Euclidean gcd criterion between a polynomial and its formal derivative. Tested degree ranges are \(2\le n\le10\) over \(\mathbb F_2\), \(2\le n\le7\) over \(\mathbb F_4\), \(2\le n\le5\) over \(\mathbb F_8\), and \(2\le n\le4\) over \(\mathbb F_{16}\). The check covers 22 degree/field cases and all 1,034 trace/constant fibers therein, over 115,682 polynomials. These computations are finite corroboration, not proof for untested degrees or field sizes.

## Relationship to prior work

Ri, Myong, Kim and Rim (2013) count *irreducible* characteristic-two polynomials with prescribed trace and subtrace. This is a different condition from squarefreeness with jointly prescribed trace and nonzero constant. Almousa and Wood (2012) treat root multiplicity patterns and give the unrestricted squarefree total \(q^n-q^{n-1}\); their inspected work does not refine by both coefficients. Kuttner and Wang (2021) give a general factorization-pattern enumeration with prescribed *initial* coefficients, not jointly a leading trace coefficient and a constant coefficient. Oppenheim and Shusterman (2017) give existence results for constrained coefficients under sufficiently large field hypotheses, not these exact uniform formulas. Gao, Kuttner and Wang (2021) address trace and norm for irreducible polynomials and related objects using generating functions and exponential sums; a complete comparison with that article is unavailable and remains an originality risk. The present proof isolates a characteristic-two Fourier cancellation and evaluates the full squarefree fiber count.

## Limitations

Only finite fields of characteristic two, degrees at least two, and nonzero prescribed constants are classified. The argument does not give finer splitting-type counts among the squarefree polynomials, or analogous complete formulas in odd characteristic. A specialist trace/norm article could contain an equivalent formulation not excluded by the accessible abstract. No independent mathematical audit has been performed.

## References

- W.-H. Ri, G.-C. Myong, R. Kim and C.-I. Rim, *The Number of Irreducible Polynomials over Finite Fields of Characteristic 2 with Given Trace and Subtrace*, arXiv:1304.0521, first submitted 2013-04-02; https://arxiv.org/html/1304.0521v4 .
- A. Almousa and M. M. Wood, *Counting polynomials over finite fields with given root multiplicities*, arXiv:1210.0472, first submitted 2012-10-01; https://arxiv.org/abs/1210.0472 .
- S. Kuttner and Q. Wang, *On the enumeration of polynomials with prescribed factorization pattern*, arXiv:2105.07550, first submitted 2021-05-17; https://arxiv.org/html/2105.07550v1 .
- A. Oppenheim and M. Shusterman, *Squarefree polynomials with prescribed coefficients*, arXiv:1707.06528, first submitted 2017-07-20; https://arxiv.org/abs/1707.06528 .
- Z. Gao, S. Kuttner and Q. Wang, *On enumeration of irreducible polynomials and related objects over a finite field with respect to their trace and norm*, *Finite Fields and Their Applications* 69 (2021), article 101770, doi:10.1016/j.ffa.2020.101770; abstract inspected, full text not obtained.
