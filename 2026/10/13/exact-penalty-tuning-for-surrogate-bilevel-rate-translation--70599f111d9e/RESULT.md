# Exact penalty tuning for surrogate bilevel rate translation
## Finding

A recent surrogate construction for composite bilevel optimization introduces a penalty parameter
\[
\rho>0
\]
and proves a rate-translation estimate for the original real-valued outer function. At a fixed target iteration \(k\), suppose the surrogate rate bounds have the affine dependence stated in the source remark,
\[
\theta_\omega(k;\rho)=a_0+a_1\rho,
\qquad
\theta_\phi(k;\rho)=b_0+b_1\rho,
\]
where
\[
a_0,a_1,b_0,b_1\ge0.
\]
Assume additionally that one constant
\[
\ell>0
\]
is a valid Lipschitz bound for the outer function on every level set entering Proposition 1(iii) over the values of \(\rho\) being compared. This holds, for example, when the outer function is globally Lipschitz with constant \(\ell\).

Then the translated upper bound is
\[
U(\rho)
=
a_0+a_1\rho
+\ell\sqrt{2\left(b_1+\frac{b_0}{\rho}\right)},
\qquad \rho>0.
\]

If
\[
a_1>0
\qquad\text{and}\qquad
b_0>0,
\]
then \(U\) is strictly convex on \((0,\infty)\) and has a unique minimizer \(\rho_\star\). It is the unique positive solution of
\[
b_1\rho_\star^4+b_0\rho_\star^3
=
\frac{\ell^2b_0^2}{2a_1^2}.
\]
The minimum itself can be written without a square root as
\[
U(\rho_\star)
=
a_0+3a_1\rho_\star
+\frac{2a_1b_1}{b_0}\rho_\star^2.
\]

A particularly simple case is
\[
b_1=0,
\]
for which
\[
\rho_\star
=
\left(\frac{\ell^2b_0}{2a_1^2}\right)^{1/3}
\]
and
\[
U(\rho_\star)
=
a_0+3\left(\frac{a_1\ell^2b_0}{2}\right)^{1/3}.
\]

The degenerate cases form an exact phase diagram:

- if \(a_1=0<b_0\), then \(U\) is strictly decreasing and its infimum is approached only as \(\rho\to\infty\);
- if \(b_0=0<a_1\), then \(U\) is strictly increasing and its infimum is approached only as \(\rho\downarrow0\);
- if \(a_1=b_0=0\), then \(U\) is constant.

Thus the qualitative penalty trade-off identified in the motivating paper can be turned into a unique algebraic tuning rule exactly when both the linear smoothness cost and the inverse-penalty translation cost are present.

## Assumptions and scope

The theorem is a statement about the published translation bound at a fixed target horizon \(k\). A single value of \(\rho\) is chosen for the surrogate problem whose guarantee at that horizon is being compared; the theorem does not prescribe changing \(\rho\) during one run of an algorithm.

The affine dependence
\[
\theta_\tau(k;\rho)=\theta_\tau^0(k)+\theta_\tau^\rho(k)\rho,
\qquad
\tau\in\{\phi,\omega\},
\]
is exactly the form singled out in the source for its analyses after the surrogate smoothness constant changes to
\[
\widetilde L_2=L_2+2\rho.
\]
The symbols \(a_0,a_1,b_0,b_1\) are simply the four nonnegative coefficients at the chosen horizon.

The uniform-Lipschitz assumption is essential. In Proposition 1(iii), the Lipschitz constant is taken over a level set that can itself depend on the rate certificate and hence on \(\rho\). If only a \(\rho\)-dependent certificate \(\ell(\rho)\) is available, the objective to be minimized is instead
\[
a_0+a_1\rho+\ell(\rho)\sqrt{2\left(b_1+\frac{b_0}{\rho}\right)},
\]
and the algebraic rule proved here need not apply.

## Proof

Write
\[
S(\rho)=\sqrt{2\left(b_1+\frac{b_0}{\rho}\right)}.
\]
For \(b_0>0\), differentiation gives
\[
U'(\rho)
=
a_1-
\frac{\ell b_0}{\rho^2S(\rho)}.
\]
A second differentiation gives the explicit positive quantity
\[
U''(\rho)
=
\frac{\sqrt{2}\,\ell b_0\left(4b_1\rho+3b_0\right)}
{4\rho^{5/2}\left(b_1\rho+b_0\right)^{3/2}}
>0.
\]
Hence \(U\) is strictly convex whenever \(b_0>0\).

Assume now
\[
a_1>0
\qquad\text{and}\qquad
b_0>0.
\]
As \(\rho\downarrow0\), the negative term in \(U'(\rho)\) diverges in magnitude, so
\[
U'(\rho)\to-\infty.
\]
As \(\rho\to\infty\), that term vanishes, so
\[
U'(\rho)\to a_1>0.
\]
Strict convexity therefore gives exactly one stationary point, and it is the global minimizer.

At the stationary point,
\[
a_1
=
\frac{\ell b_0}{\rho_\star^2S(\rho_\star)}.
\]
Squaring and clearing the positive denominator yields
\[
2a_1^2\left(b_1\rho_\star^4+b_0\rho_\star^3\right)
=
\ell^2b_0^2,
\]
which is the asserted algebraic equation. Its left-hand side is strictly increasing for \(\rho>0\), giving another direct proof of uniqueness.

The stationary equation also implies
\[
\ell S(\rho_\star)
=
2a_1\rho_\star
+\frac{2a_1b_1}{b_0}\rho_\star^2.
\]
Substitution into \(U\) gives
\[
U(\rho_\star)
=
a_0+3a_1\rho_\star
+\frac{2a_1b_1}{b_0}\rho_\star^2.
\]
If \(b_1=0\), the algebraic equation reduces to
\[
\rho_\star^3
=
\frac{\ell^2b_0}{2a_1^2},
\]
which gives the displayed cube-root formula and its minimum value.

For the boundary cases, if \(a_1=0<b_0\), then
\[
U'(\rho)<0
\]
for every \(\rho>0\). If \(b_0=0<a_1\), then the square-root term is independent of \(\rho\) and
\[
U'(\rho)=a_1>0.
\]
If \(a_1=b_0=0\), every term is independent of \(\rho\). This proves the complete phase diagram.

## Verification

The bundled script `artifacts/verify_penalty_tuning.py` checks two exact parameter choices for which the algebraic optimizer is \(\rho_\star=1\), verifies the stationary polynomial with rational arithmetic, checks the derivative sign on both sides, and tests the three degenerate monotonicity regimes.

The script is supporting evidence only. The theorem is proved by the derivative and convexity calculation above.

## Relationship to prior work

Shtern and Taiwo introduce the split surrogate, prove the translation estimate in Proposition 1, and then state in Remark 2 that their rate certificates are affine in \(\rho\) through the modified smoothness constant \(\widetilde L_2=L_2+2\rho\). They explicitly note that, depending on the forms of the bounds, a value of \(\rho\in(0,\infty)\) may minimize the translated real-valued-function bound. They do not derive the optimizer, its uniqueness conditions, its minimum value, or the boundary regimes in which no finite optimizer exists.

Latafat, Themelis, Villa, and Patrinos discuss a related lifted reformulation for making separate proximal operators available. Their lifted model motivates the same kind of quadratic coupling, but the inspected lifting remark uses a fixed quadratic coupling and does not derive the rate-translation bound or optimize a penalty parameter against such a bound.

General quadratic-penalty analyses choose penalty schedules to guarantee convergence of constrained optimization methods. Those results address a different object: an algorithmic penalty sequence and optimization error, rather than the fixed-horizon minimization of the specific bilevel translation certificate above.

Targeted searches for the source title, the affine \(\rho\)-dependence, the translated square-root bound, equivalent penalty-tuning language, and the resulting quartic equation did not locate a statement implying this phase diagram.

## Limitations

The result optimizes an upper bound, not the unknown true error. A bound-optimal \(\rho\) need not minimize empirical error.

The theorem is horizon-wise: the coefficients may depend on \(k\), so a different target horizon can produce a different recommended fixed \(\rho\).

The uniform-Lipschitz certificate cannot be omitted. If the Lipschitz constant in Proposition 1(iii) changes materially with \(\rho\), that dependence must be incorporated before tuning.

No claim is made that the quartic root is the best parameter for bilevel methods outside the source surrogate construction.

## References

1. S. Shtern, A. Taiwo, *On the Convergence Rates of Iterative Regularization Algorithms for Composite Bi-Level Optimization*, arXiv:2506.16382v1, 2025; SIAM Journal on Optimization 36(2), 1043--1074, 2026. DOI: 10.1137/24M1703355.
2. P. Latafat, A. Themelis, S. Villa, P. Patrinos, *On the Convergence of Proximal Gradient Methods for Convex Simple Bilevel Optimization*, arXiv:2305.03559v3; Journal of Optimization Theory and Applications 204, 51, 2025. DOI: 10.1007/s10957-024-02564-6.
3. H. Li, C. Fang, Z. Lin, *Convergence Rates Analysis of the Quadratic Penalty Method and Its Applications to Decentralized Distributed Optimization*, arXiv:1711.10802, 2017.
