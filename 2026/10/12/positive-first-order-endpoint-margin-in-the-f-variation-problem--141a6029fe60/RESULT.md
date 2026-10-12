# Positive first-order endpoint margin in the F-variation problem
## Finding
Fix an integer \(d\ge6\). For integers \(m\ge5\), let
\[
X_{d,m}\sim F(d,m)
\]
and define
\[
C_{d,m}
=
\Pr\!\left\{
\left|X_{d,m}-\mathbb E X_{d,m}\right|
\le
\sqrt{\operatorname{Var}(X_{d,m})}
\right\}.
\]
Let \(Y_d\sim\chi_d^2\), write \(f_d\) for its density, and put
\[
C_d^\chi
=
\Pr\!\left\{
|Y_d-d|\le\sqrt{2d}
\right\}.
\]
Then, as \(m\to\infty\) through integers,
\[
C_{d,m}
=
C_d^\chi
+
\frac{2\sqrt{2d}}{m}
\left[
f_d\!\left(d+\sqrt{2d}\right)
+
f_d\!\left(d-\sqrt{2d}\right)
\right]
+
O_d(m^{-2}).
\]
The first correction is strictly positive. Hence, for every fixed integer \(d\ge6\), there is a finite \(M_d\) such that
\[
C_{d,m}>C_d^\chi
\qquad\text{for every integer }m\ge M_d.
\]
The known Gamma/chi-square variation theorem gives \(C_d^\chi\ge \Pr\{|Z|\le1\}\) for a standard normal \(Z\). Thus the F-distribution variation conjecture holds for every fixed unresolved numerator degree \(d\ge6\) once the denominator degree is sufficiently large.

## Assumptions and scope
The numerator degree \(d\) is fixed while \(m\) tends to infinity through integers. The theorem is stated for \(d\ge6\), in the parameter range left after the motivating paper's cases \(d=1,2,3,4\) and a separate prior result for \(d=5\). The variance exists because \(m\ge5\).

The result is pointwise in \(d\). It gives neither a threshold uniform in \(d\), nor full monotonicity in \(m\), nor a proof for every \(m\ge5\).

## Proof
Let \(U\sim\chi_d^2\) and \(V\sim\chi_m^2\) be independent and write \(W=V/m\). Then
\[
X_{d,m}=\frac{U/d}{W}.
\]
The exact mean and variance are
\[
\mu_m=\frac{m}{m-2},
\qquad
s_m^2=
\frac{2m^2(d+m-2)}{d(m-2)^2(m-4)}.
\]
For fixed \(d\),
\[
\mu_m=1+\frac2m+O(m^{-2}),
\]
and
\[
s_m=
\sqrt{\frac2d}
\left(
1+\frac{d+6}{2m}+O_d(m^{-2})
\right).
\]
Put
\[
r=\sqrt{2d},
\qquad
t_\pm=d\pm r.
\]
Because \(d\ge6\), \(t_->0\). If
\[
t_{m,\pm}=d(\mu_m\pm s_m),
\]
then
\[
t_{m,\pm}
=
t_\pm+\frac{b_\pm}{m}+O_d(m^{-2}),
\qquad
b_\pm=2d\pm\frac{d+6}{2}r.
\]

Let \(H_d\) be the chi-square distribution function. Conditioning on \(W\) gives
\[
\Pr\{X_{d,m}\le x\}=\mathbb E\,H_d(dxW).
\]
For fixed positive \(t\), Taylor expansion about \(W=1\), together with
\[
\mathbb E(W-1)=0,\qquad
\mathbb E(W-1)^2=\frac2m,
\]
\[
\mathbb E(W-1)^3=\frac8{m^2},
\qquad
\mathbb E(W-1)^4=\frac{12}{m^2}+O(m^{-3}),
\]
gives
\[
\mathbb E H_d(tW)
=
H_d(t)+\frac{t^2f_d'(t)}{m}+O_d(m^{-2}).
\]
For the remainder, restrict first to \(|W-1|\le1/2\), where the required derivatives are bounded. The complementary normalized-chi-square tails are exponentially small, so they are \(O_d(m^{-2})\).

Substituting the moving endpoints,
\[
\Pr\{X_{d,m}\le\mu_m\pm s_m\}
=
H_d(t_\pm)
+
\frac{b_\pm f_d(t_\pm)+t_\pm^2 f_d'(t_\pm)}{m}
+
O_d(m^{-2}).
\]
Since
\[
f_d'(t)
=
f_d(t)
\left(
\frac{d/2-1}{t}-\frac12
\right),
\]
the endpoint coefficient simplifies exactly:
\[
b_\pm+
\left(\frac d2-1\right)t_\pm
-\frac{t_\pm^2}{2}
=
\pm2r.
\]
Thus
\[
\Pr\{X_{d,m}\le\mu_m+s_m\}
=
H_d(t_+)+\frac{2r f_d(t_+)}m+O_d(m^{-2}),
\]
while
\[
\Pr\{X_{d,m}\le\mu_m-s_m\}
=
H_d(t_-)-\frac{2r f_d(t_-)}m+O_d(m^{-2}).
\]
Subtracting gives the claim. Both endpoint densities are positive, so the leading correction is positive.

## Verification
The theorem is analytic. The standalone script `verify_f_endpoint.py` implements regularized beta and gamma functions using only the Python standard library. It checks the endpoint algebra and compares
\[
m(C_{d,m}-C_d^\chi)
\]
with the proved coefficient for \(d\in\{6,7,10,20,40\}\) and \(m\in\{2000,4000,8000\}\). Its successful output is `VERIFY_OK max_scaled_error=0.00483207616522`.

The finite calculations are regression checks only and do not prove the asymptotic theorem.

## Relationship to prior work
Sun, Hu, and Sun formulate the F-distribution variation conjecture and prove it for numerator degrees \(1,2,3,4\) and every denominator degree at least \(5\). Their paper also records the exact F moments and the independent chi-square ratio representation. Its final section explicitly discusses numerator degrees at least \(5\) as the remaining difficult range.

A separate prior result for numerator degree \(5\) proves the full denominator-degree comparison in that one case. The present claim excludes \(d=5\) and instead treats every fixed \(d\ge6\) only in the large-\(m\) regime, so neither statement subsumes the other.

The Gamma paper of Sun, Hu, and Sun establishes that the infimum of the one-standard-deviation central probability over the Gamma family equals the standard-normal central probability. Since chi-square laws are Gamma laws, this provides the benchmark used in the final consequence.

Targeted searches for F-to-chi-square one-standard-deviation asymptotics, moving central intervals, and the explicit endpoint-density coefficient did not locate a covering statement.

## Limitations
The threshold \(M_d\) is existential and can depend on \(d\). The theorem does not prove monotonicity in \(m\), does not cover the whole finite range \(m\ge5\), and does not treat joint growth of the two degrees. A residual literature risk is that a general asymptotic expansion for F distribution functions could imply the coefficient after a nontrivial specialization, although no such covering result was found.

## References
1. P. Sun, Z.-C. Hu, and W. Sun, *Variation comparison between the F-distribution and the normal distribution*, arXiv:2305.13615v1, first public version 2023-05-23. Primary listed MSC: \(60E15\).
2. P. Sun, Z.-C. Hu, and W. Sun, *The extreme values of two probability functions for the Gamma distribution*, arXiv:2303.17487v1, first public version 2023-03-30.
