# UWG moment formula is invalid; the beta-one slice has an exact correction
## Finding
Let \(X\) have the unit-Weibull geometric (UWG) distribution with
\[
\alpha>0,\qquad \beta>0,\qquad 0<p<1,
\]
and cumulative distribution function
\[
F(x)
=
\frac{
e^{-\alpha(-\log x)^\beta}
}{
1-p+p e^{-\alpha(-\log x)^\beta}
},
\qquad 0<x<1.
\]
After the change of variable
\[
y=-\log x,
\]
the exact raw moment of every real order \(r>0\) is
\[
\boxed{
\mu_r'
=
(1-p)\alpha\beta
\int_0^\infty
\frac{
y^{\beta-1}e^{-r y-\alpha y^\beta}
}{
[1-p+p e^{-\alpha y^\beta}]^2
}\,dy.
}
\]

Equation (5.9) in the source is not equal to this integral in general. The source reaches the exact intermediate expression
\[
(1-p)\alpha\beta
\sum_{i=0}^\infty(i+1)p^i
\sum_{m=0}^i
\binom{i}{m}(-1)^{i-m}
\int_0^\infty
y^{\beta-1}
e^{-r y-\alpha(1+i-m)y^\beta}\,dy,
\]
but then replaces the remaining integral by a single gamma term. The factor
\[
e^{-r y}
\]
cannot disappear in this way. Expanding it produces an additional infinite series, and for general \(\beta\) the integral is not the gamma expression printed in Eq. (5.9).

There is an exact, decisive counterexample inside the model's parameter space. Set
\[
\alpha=\beta=1,\qquad p=\frac12,\qquad r=1.
\]
Then
\[
F(x)=\frac{x}{1-p+px},
\]
and direct integration gives
\[
\boxed{
\mathbb E[X]
=
2\log 2-1
=
0.3862943611198906\ldots .
}
\]
By contrast, the series printed as Eq. (5.9) sums to
\[
\boxed{
2\log 2
=
1.3862943611198906\ldots ,
}
\]
which is impossible for a random variable supported on \((0,1)\).

The full slice
\[
\beta=1
\]
admits a useful exact correction. In this case
\[
f(x)
=
\frac{(1-p)\alpha x^{\alpha-1}}
{(1-p+p x^\alpha)^2}.
\]
With \(u=x^\alpha\),
\[
\boxed{
\mu_r'
=
\frac{
{}_2F_1\!\left(
2,1+r/\alpha;
2+r/\alpha;
-p/(1-p)
\right)
}{
(1-p)(1+r/\alpha)
},
\qquad r>0.
}
\]
For
\[
\alpha=2,\qquad p=\frac12,\qquad r=1,
\]
this gives
\[
\boxed{
\mathbb E[X]
=
\frac{\pi}{2}-1
=
0.5707963267948966\ldots .
}
\]
The source's Table 2 reports \(0.5708\) for this parameter row. Thus the numerical table is compatible with the corrected moment and need not have been generated from Eq. (5.9).

Finally, Eq. (5.14) in the source is obtained by substituting Eq. (5.9) into the ordinary MGF expansion. That displayed closed-form representation is therefore invalid as written. The MGF itself exists for every real and complex argument because the distribution is supported in \((0,1)\); a correct integral representation is
\[
M_X(t)
=
(1-p)\alpha\beta
\int_0^\infty
\frac{
y^{\beta-1}
e^{-\alpha y^\beta}
e^{t e^{-y}}
}{
[1-p+p e^{-\alpha y^\beta}]^2
}\,dy.
\]

## Assumptions and scope
The finding concerns the UWG parameterization used by the source:
\[
\alpha,\beta>0,\qquad 0<p<1.
\]
The corrected integral is valid for every real \(r>0\). The hypergeometric closed form is asserted only on the slice
\[
\beta=1.
\]

The finding does not claim that the numerical values in Table 2 are wrong. One published row agrees with the corrected formula to four decimals, providing evidence that the table may have been produced by direct numerical integration or another correct computation.

The MGF criticism is similarly narrow. The general identity
\[
M_X(t)=\sum_{\ell=0}^\infty \frac{t^\ell}{\ell!}\mu_\ell'
\]
is valid. What fails is the subsequent displayed substitution of the incorrect moment formula.

## Proof
Starting from the published density,
\[
f(x)
=
\frac{
(1-p)\alpha\beta
(-\log x)^{\beta-1}
e^{-\alpha(-\log x)^\beta}
}{
x[1-p+p e^{-\alpha(-\log x)^\beta}]^2
},
\]
put
\[
y=-\log x.
\]
Then \(x=e^{-y}\) and \(dx=-e^{-y}dy\). Therefore
\[
x^r f(x)\,dx
=
-(1-p)\alpha\beta
\frac{
y^{\beta-1}
e^{-r y-\alpha y^\beta}
}{
[1-p+p e^{-\alpha y^\beta}]^2
}\,dy.
\]
Reversing the integration limits proves the exact moment integral.

To see the defect in Eq. (5.9), retain the source's own geometric-series and finite-binomial expansions. They lead to integrals of the form
\[
I=
\int_0^\infty
y^{\beta-1}
e^{-r y-cy^\beta}\,dy,
\qquad
c>0.
\]
The printed gamma term is what one obtains after removing the factor \(e^{-r y}\), not after integrating it. If one expands
\[
e^{-r y}
=
\sum_{j=0}^\infty
\frac{(-r)^j y^j}{j!},
\]
then each \(j\) produces a different gamma term. A single term cannot represent the general integral.

For the explicit counterexample, take
\[
\alpha=\beta=1.
\]
The exact density is
\[
f(x)
=
\frac{1-p}{(1-p+px)^2}.
\]
Thus
\[
\mathbb E[X]
=
(1-p)\int_0^1
\frac{x}{(1-p+px)^2}\,dx
=
\frac{1-p}{p^2}
[-\log(1-p)-p].
\]
At \(p=1/2\), this is \(2\log2-1\).

Now evaluate the source's printed Eq. (5.9) at the same parameter values. Its inner finite sum reduces to
\[
\sum_{j=0}^i
(-1)^j\binom{i}{j}\frac{1}{(j+1)^2}
=
\frac{H_{i+1}}{i+1},
\]
where \(H_n\) is the \(n\)-th harmonic number. Hence the printed expression becomes
\[
(1-p)
\sum_{i=0}^\infty p^i H_{i+1}
=
-\frac{\log(1-p)}{p}.
\]
At \(p=1/2\), this equals \(2\log2\).

For the corrected \(\beta=1\) formula, substitute \(u=x^\alpha\):
\[
\mu_r'
=
(1-p)
\int_0^1
\frac{u^{r/\alpha}}{(1-p+pu)^2}\,du.
\]
Factoring \((1-p)^2\) from the denominator and using Euler's hypergeometric integral gives
\[
\mu_r'
=
\frac{
{}_2F_1\!\left(
2,1+r/\alpha;
2+r/\alpha;
-p/(1-p)
\right)
}{
(1-p)(1+r/\alpha)
}.
\]
For \(\alpha=2\), \(p=1/2\), \(r=1\), elementary integration reduces this to \(\pi/2-1\).

## Verification
The accompanying checker performs four independent finite checks.

First, it numerically integrates the exact UWG density for
\[
\alpha=\beta=1,\qquad p=1/2,
\]
and reproduces
\[
2\log2-1.
\]

Second, it directly sums a long truncation of the source's Eq. (5.9) for the same parameters and verifies convergence to
\[
2\log2.
\]

Third, on the slice \(\beta=1\), it compares direct quadrature with the corrected hypergeometric expression for several values of \(\alpha\), \(p\), and \(r\).

Fourth, it verifies
\[
\alpha=2,\quad p=1/2,\quad r=1
\]
against the elementary value \(\pi/2-1\), which rounds to the source's Table 2 entry \(0.5708\).

These computations are consistency checks. The contradiction and corrected formulas are established analytically above.

## Relationship to prior work
Namsaw et al. introduce the UWG model and correctly derive its CDF and density. Their Section 5.2 reaches an exact integral representation for raw moments before giving Eq. (5.9). The error occurs in the final evaluation of the integral containing both
\[
e^{-r y}
\]
and
\[
e^{-c y^\beta}.
\]
Section 5.3 then propagates Eq. (5.9) into the displayed MGF representation.

The same article's Table 2 contains a useful internal check. At
\[
\alpha=2,\qquad\beta=1,\qquad p=1/2,
\]
its reported mean \(0.5708\) agrees with the corrected value \(\pi/2-1\) rather than with the value obtained from Eq. (5.9). The safest interpretation is therefore that the displayed analytic formula is wrong while at least some numerical summaries were computed by another route.

Focused searches using the exact DOI, the UWG name, raw-moment and MGF terminology, the \(\beta=1\) slice, and formula-correction aliases did not locate a published correction of Eq. (5.9) or Eq. (5.14).

## Limitations
The finding does not supply a one-line special-function reduction of the raw moment for arbitrary \(\beta\). The exact one-dimensional integral is the general correction, while a hypergeometric closed form is given only for \(\beta=1\).

No claim is made that every numerical moment in the article is incorrect. The verified Table 2 row shows that at least one tabulated mean is consistent with the correct distribution.

The finding does not reassess the source's identifiability, likelihood estimation, simulation consistency, or real-data fits.

## References
1. M. Namsaw, B. Das, M. S. Eliwa, and M. F. Abouelenein, “The unit-Weibull geometric distribution: Mathematical properties, identifiability, and asymptotic analysis with applications to data modeling,” AIMS Mathematics 11 (2026), 29488–29528. DOI: 10.3934/math.20261171.
