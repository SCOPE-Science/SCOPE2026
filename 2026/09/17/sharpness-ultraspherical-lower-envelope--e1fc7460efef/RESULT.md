# Sharpness of the nonnegative-parameter range for the ultraspherical lower envelope

## Result

For \(\alpha>-1\), write
\[
U_n^{(\alpha)}(x):=
\frac{P_n^{(\alpha,\alpha)}(x)}{P_n^{(\alpha,\alpha)}(1)},
\]
and put \(\xi_0=-1\). For \(n\ge 1\), let \(\xi_n\) denote the largest zero of
\[
R_n^{(\alpha+1,\alpha)}(x)
=
\frac{P_n^{(\alpha+1,\alpha)}(x)}
     {P_n^{(\alpha+1,\alpha)}(1)}.
\]

Castillo and Sadigova proved that for every \(\alpha\ge0\),
\[
U_k^{(\alpha)}(x)=\min_{n\ge0}U_n^{(\alpha)}(x),
\qquad
\xi_{k-1}\le x\le \xi_k,
\]
for every \(k\ge1\).

The parameter range \(\alpha\ge0\) is sharp inside the full Jacobi range
\(\alpha>-1\): the same interval-by-interval lower-envelope conclusion fails for
every \(-1<\alpha<0\).

More precisely, the failure has three regimes.

### 1. The range \(-\tfrac12<\alpha<0\): a degree-five obstruction at the first transition point

The first transition point is
\[
\xi_1=-\frac{1}{2\alpha+3}.
\]
At this point
\[
U_1^{(\alpha)}(\xi_1)=U_2^{(\alpha)}(\xi_1)=\xi_1,
\]
but
\[
\boxed{
U_5^{(\alpha)}(\xi_1)-U_1^{(\alpha)}(\xi_1)
=
\frac{4\alpha(\alpha+2)(2\alpha+1)(2\alpha+7)}
     {(2\alpha+3)^5}<0.
}
\]
Thus degree \(5\) already lies strictly below the degree-\(1\) polynomial at the
right endpoint of the first claimed cell.

At \(\alpha=0\) the displayed defect vanishes, so this same finite-degree test
detects the sharp boundary.

### 2. The endpoint \(\alpha=-\tfrac12\): Chebyshev failure inside the first cell

For \(\alpha=-\tfrac12\),
\[
U_n^{(-1/2)}(x)=T_n(x),
\]
the Chebyshev polynomial of the first kind, and
\[
\xi_1=-\frac12.
\]
Taking
\[
x=-\frac1{\sqrt2}\in[-1,-1/2]
\]
gives
\[
U_1^{(-1/2)}(x)=-\frac1{\sqrt2},
\qquad
U_4^{(-1/2)}(x)=T_4(x)=-1.
\]
Hence the degree-\(1\) member is not the lower envelope on the first cell.

### 3. The range \(-1<\alpha<-\tfrac12\): the family is unbounded below at \(x=0\)

For every \(m\ge0\),
\[
\boxed{
U_{2m}^{(\alpha)}(0)
=
(-1)^m
\frac{(2m)!}{4^m m!(\alpha+1)_m}
=
(-1)^m
\frac{\Gamma(\alpha+1)\Gamma(m+\tfrac12)}
     {\sqrt{\pi}\,\Gamma(m+\alpha+1)}.
}
\]
Consequently,
\[
|U_{2m}^{(\alpha)}(0)|
\sim
\frac{\Gamma(\alpha+1)}{\sqrt{\pi}}\,
m^{-\alpha-\frac12}.
\]
When \(-1<\alpha<-\tfrac12\), the exponent
\(-\alpha-\tfrac12\) is positive. The magnitudes therefore tend to infinity,
with alternating signs, and
\[
\boxed{\inf_{n\ge0}U_n^{(\alpha)}(0)=-\infty.}
\]
In this regime there is not even a finite pointwise lower envelope at the
origin.

Combining these counterexamples with the theorem of Castillo--Sadigova for
\(\alpha\ge0\) gives an exact parameter classification, within
\(\alpha>-1\), for their stated interval-by-interval minimum theorem:
\[
\boxed{\text{the theorem holds exactly for }\alpha\ge0.}
\]

## Proof

The first-degree Jacobi formula gives
\[
P_1^{(\alpha+1,\alpha)}(x)
=\frac12\bigl(1+(2\alpha+3)x\bigr),
\]
so its unique zero is
\[
\xi_1=-\frac1{2\alpha+3}.
\]

For the symmetric normalized family,
\[
U_1^{(\alpha)}(x)=x,
\qquad
U_2^{(\alpha)}(x)
=
\frac{(2\alpha+3)x^2-1}{2(\alpha+1)}.
\]
Substitution of \(x=\xi_1\) gives
\[
U_2^{(\alpha)}(\xi_1)=U_1^{(\alpha)}(\xi_1)=\xi_1.
\]

A direct degree-five Jacobi calculation gives
\[
U_5^{(\alpha)}(x)
=
\frac{x\left[(4\alpha^2+32\alpha+63)x^4
-(20\alpha+70)x^2+15\right]}
{4(\alpha+1)(\alpha+2)}.
\]
Substituting \(x=\xi_1\) and simplifying yields
\[
U_5^{(\alpha)}(\xi_1)-U_1^{(\alpha)}(\xi_1)
=
\frac{4\alpha(\alpha+2)(2\alpha+1)(2\alpha+7)}
{(2\alpha+3)^5}.
\]
For \(-\tfrac12<\alpha<0\), all factors except \(\alpha\) are positive, so
the expression is strictly negative.

At \(\alpha=-\tfrac12\), the normalized symmetric Jacobi polynomials are
exactly \(T_n\). Since
\[
T_4(-1/\sqrt2)=8(1/4)-8(1/2)+1=-1,
\]
the stated first-cell counterexample follows.

Finally, the standard symmetric Jacobi evaluation at the origin gives
\[
U_{2m}^{(\alpha)}(0)
=
(-1)^m\frac{(2m)!}{4^m m!(\alpha+1)_m}.
\]
Using the duplication formula,
\[
\frac{(2m)!}{4^m m!}
=
\frac{\Gamma(m+\tfrac12)}{\sqrt{\pi}},
\]
and
\[
(\alpha+1)_m
=
\frac{\Gamma(m+\alpha+1)}{\Gamma(\alpha+1)},
\]
gives the gamma-function form. The quotient asymptotic
\[
\frac{\Gamma(m+\tfrac12)}{\Gamma(m+\alpha+1)}
\sim m^{-\alpha-\frac12}
\]
then proves divergence in magnitude for \(-1<\alpha<-\tfrac12\), while the
factor \((-1)^m\) gives values tending to \(-\infty\) along odd \(m\).

## Context and significance

The recent Castillo--Sadigova theorem resolves the lower-envelope question in
the parameter range \(\alpha\ge0\). The calculation above shows that this is not
merely a convenient range for their proof: it is the maximal range in the
natural Jacobi domain \(\alpha>-1\) for the theorem as stated.

The obstruction immediately below zero is especially rigid. No large-degree
asymptotic construction is needed: at the first transition point, degree \(5\)
crosses below the proposed degree-\(1\) envelope for every
\(-\tfrac12<\alpha<0\), and the sign changes exactly at \(\alpha=0\).

The second threshold \(\alpha=-\tfrac12\) separates two qualitatively different
failure mechanisms. At the threshold the family becomes the bounded Chebyshev
family; below it, normalized even Jacobi values at the origin grow without
bound. This explains why attempts to continue the lower-envelope picture into
negative parameters encounter a more severe obstruction after crossing
\(-\tfrac12\).

## Limitations and originality boundary

The Jacobi identities, Chebyshev specialization, gamma quotient asymptotic, and
the growth of normalized ultraspherical values for negative parameters are
classical ingredients and are not claimed as new in isolation.

The originality claim is narrower: to the best of our knowledge, the exact
sharpness of the newly proved Castillo--Sadigova lower-envelope theorem across
the full Jacobi range \(\alpha>-1\), including the explicit universal
degree-\(5\) first-cell defect for \(-\tfrac12<\alpha<0\) and the three-regime
failure classification, has not previously been recorded.

The motivating question cited by Castillo--Sadigova was posed for
\(\alpha\ge0\), so these counterexamples do not alter the answer to that
originally stated problem. They instead determine the maximal natural parameter
range of the new theorem itself.

## References

1. K. Castillo and S. Sadigova, *The lower envelope of ultraspherical polynomials*, arXiv:2609.15473 (2026).
2. F. M. de Oliveira Filho, *New Bounds for Geometric Packing and Coloring via Harmonic Analysis and Optimization*, PhD thesis, 2009.
3. NIST Digital Library of Mathematical Functions, Chapter 18, classical orthogonal polynomials.
