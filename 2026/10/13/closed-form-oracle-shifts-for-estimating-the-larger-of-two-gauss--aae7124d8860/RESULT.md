# Closed-form oracle shifts for estimating the larger of two Gaussian means
## Finding
Let
\[
X_1\sim N(\theta_1,\sigma^2),
\qquad
X_2\sim N(\theta_2,\sigma^2)
\]
be independent, with known \(\sigma>0\), and let
\[
\theta_{(2)}=\max(\theta_1,\theta_2).
\]
For the constant-shift estimators
\[
\delta_b=X_{(2)}-b,\qquad b\in\mathbb R,
\]
under squared-error loss, define
\[
\Delta=\frac{|\theta_1-\theta_2|}{\sigma}
\]
and
\[
h(\Delta)
=
\sqrt2\,\phi\!\left(\frac{\Delta}{\sqrt2}\right)
-
\Delta\,\Phi\!\left(-\frac{\Delta}{\sqrt2}\right),
\]
where \(\phi\) and \(\Phi\) are the standard-normal density and distribution function.

The unique pointwise risk-minimizing shift is
\[
b_\Delta=\sigma h(\Delta),
\]
and, for every real \(b\),
\[
R_\Delta(b)-R_\Delta(b_\Delta)
=
(b-b_\Delta)^2.
\tag{1}
\]
Furthermore,
\[
h'(\Delta)
=
-\Phi\!\left(-\frac{\Delta}{\sqrt2}\right)<0,
\]
so the oracle shift decreases continuously and bijectively from
\[
b_0=\frac{\sigma}{\sqrt\pi}
\]
at equal means to \(0\) as the standardized separation tends to infinity.

For the boundary estimator emphasized in the motivating paper,
\[
\delta_{b_0}=X_{(2)}-\frac{\sigma}{\sqrt\pi},
\]
and the usual estimator
\[
\delta_0=X_{(2)},
\]
the exact risk difference is
\[
R_\Delta(b_0)-R_\Delta(0)
=
\sigma^2\left[
\frac1\pi-\frac{2}{\sqrt\pi}h(\Delta)
\right].
\tag{2}
\]
It has exactly one zero,
\[
\Delta_*=0.699454801905019\ldots,
\]
characterized by
\[
h(\Delta_*)=\frac{1}{2\sqrt\pi}.
\]
Consequently,
\[
R_\Delta(b_0)<R_\Delta(0)
\quad\text{for }0\le\Delta<\Delta_*,
\]
the risks are equal at \(\Delta_*\), and
\[
R_\Delta(b_0)>R_\Delta(0)
\quad\text{for }\Delta>\Delta_*.
\]

## Assumptions and scope
The two observations are independent Gaussians with a common known variance. The target is the larger of the two unknown means. The loss is squared error.

Equation (1) concerns the full constant-shift class \(X_{(2)}-b\). It does not claim that a constant-shift estimator is optimal among all equivariant estimators. In fact, the motivating paper gives a Brewster–Zidek-type estimator that dominates its boundary constant-shift estimator.

The crossover in (2) is therefore a precise comparison of two canonical members of the source's class, not a global admissibility statement.

## Proof
By symmetry, assume
\[
\theta_2=\theta_{(2)}
\]
and put
\[
\Delta=\frac{\theta_2-\theta_1}{\sigma}\ge0.
\]
Let
\[
M=X_{(2)}.
\]
For any real \(b\),
\[
R_\Delta(b)
=
\mathbb E[(M-\theta_2-b)^2].
\]
Expanding the square gives
\[
R_\Delta(b)
=
R_\Delta(0)
-
2b\,\mathbb E[M-\theta_2]
+
b^2.
\tag{3}
\]
Thus the unique minimizing shift is
\[
b_\Delta=\mathbb E[M-\theta_2].
\tag{4}
\]

Since
\[
M-\theta_2
=
(X_2-\theta_2)+(X_1-X_2)_+,
\]
and \(\mathbb E[X_2-\theta_2]=0\),
\[
b_\Delta
=
\mathbb E[(X_1-X_2)_+].
\]
Now
\[
\frac{X_1-X_2}{\sigma}
\sim
N(-\Delta,2).
\]
For a normal variable \(Y\sim N(\mu,s^2)\),
\[
\mathbb E[Y_+]
=
s\,\phi(\mu/s)+\mu\,\Phi(\mu/s).
\]
Applying this with \(\mu=-\Delta\) and \(s=\sqrt2\) gives
\[
\frac{b_\Delta}{\sigma}
=
\sqrt2\,\phi\!\left(\frac{\Delta}{\sqrt2}\right)
-
\Delta\,\Phi\!\left(-\frac{\Delta}{\sqrt2}\right)
=
h(\Delta).
\tag{5}
\]

Substituting (4) into the quadratic expression (3) and completing the square proves
\[
R_\Delta(b)-R_\Delta(b_\Delta)
=
(b-b_\Delta)^2.
\]

Differentiating (5), the two density-derivative terms cancel and yield
\[
h'(\Delta)
=
-\Phi\!\left(-\frac{\Delta}{\sqrt2}\right)<0.
\]
Also,
\[
h(0)=\sqrt2\,\phi(0)=\frac1{\sqrt\pi},
\]
while \(h(\Delta)\to0\) as \(\Delta\to\infty\). This proves the asserted bijection between standardized separation and the oracle constant shift.

Finally set
\[
b_0=\frac{\sigma}{\sqrt\pi}.
\]
From (3),
\[
R_\Delta(b_0)-R_\Delta(0)
=
b_0^2-2b_0b_\Delta
=
\sigma^2\left[
\frac1\pi-\frac{2}{\sqrt\pi}h(\Delta)
\right].
\]
Because \(h\) is continuous and strictly decreasing from \(1/\sqrt\pi\) to \(0\), this risk difference is continuous and strictly increasing from
\[
-\frac{\sigma^2}{\pi}
\]
to
\[
\frac{\sigma^2}{\pi}.
\]
It therefore has exactly one zero, equivalently
\[
h(\Delta_*)=\frac1{2\sqrt\pi}.
\]
Numerical root evaluation gives the displayed value of \(\Delta_*\).

## Verification
The bundled script `verify.py` uses only the Python standard library. It solves the crossover equation by bisection, checks the strict sign pattern, numerically integrates the positive part of a \(N(-\Delta,2)\) variable against the closed form in (5), and checks the derivative formula by finite differences.

A successful run ends with
`VERIFY_OK delta_star=0.699454801905 h0=0.564189583548`.

The numerical calculation is only a reproducibility check. The oracle identity, monotonicity, and uniqueness of the crossover are proved analytically.

## Relationship to prior work
Garg, Patra, and Misra study the same problem of estimating the larger location parameter. For the normal model with common known variance and squared-error loss, their Example 5.1 identifies the usual estimator \(X_{(2)}\) and the boundary constant-shift estimator
\[
X_{(2)}-\frac{\sigma}{\sqrt\pi}.
\]
Their general Theorem 2.3 characterizes the admissible constant-shift interval through an abstract pointwise minimizer \(b_\theta\), but the inspected normal example does not give the explicit map (5).

The same paper reports simulation risk comparisons and states that its boundary estimator performs better for small and moderate mean separations whereas the usual estimator performs better for large separations. The exact crossover \(\Delta_*\) above turns that qualitative simulation pattern into a complete analytic phase boundary and simultaneously gives the full oracle map for the constant-shift class.

Blumenthal and Cohen's 1968 paper is a highly relevant earlier source on estimation of the larger of two normal means under squared-error loss, and the motivating paper says it studies several estimators for this problem. Bibliographic metadata and citation context were available, but full article text was unavailable through the checked lawful routes. Exact-expression searches did not locate (1), (2), or the numerical crossover, but possible prior appearance in that older literature remains a residual originality risk.

## Limitations
The result is specific to two independent normal observations with common known variance and squared-error loss. It does not compare the Brewster–Zidek estimator with the usual estimator, and it does not supersede the motivating paper's dominance result for the Brewster–Zidek estimator over the boundary constant shift.

The main bibliographic uncertainty is older literature on the larger of two normal means whose full text was not accessible in the checked routes.

## References
1. N. Garg, L. K. Patra, and N. Misra, “On improved estimation of the larger location parameter,” arXiv:2309.13878v1, 25 September 2023; *Statistical Papers* 65 (2024). DOI: 10.1007/s00362-024-01614-5.
2. S. Blumenthal and A. Cohen, “Estimation of the Larger of Two Normal Means,” *Journal of the American Statistical Association* 63 (1968), 861–876. DOI: 10.2307/2283879.
