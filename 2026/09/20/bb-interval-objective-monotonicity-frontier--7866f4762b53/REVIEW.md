# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof has two independent parts.

First, Rayleigh quotient bounds imply
\[
1/L\le \eta^{\rm BB2}\le\eta^{\rm BB1}\le1/\mu.
\]
For any step in this interval, the quadratic error update is
\[
e^+=(I-\eta A)e.
\]
In the \(A\)-energy norm, the one-step factor is bounded by the squared spectral
radius of this symmetric polynomial in \(A\):
\[
\frac{F^+}{F}\le
\max_{\lambda\in[\mu,L]}|1-\eta\lambda|^2
\le(\kappa-1)^2.
\]
The endpoint comparison is exact.

Second, the two-dimensional construction
\[
A=\operatorname{diag}(1,\kappa),\qquad g_0=(1,\sqrt r)^\top
\]
uses an exact line-search warm-up. The resulting current gradient and both next BB
steps are explicit. BB1 and BB2 both approach \(1\) as \(r\downarrow0\), while the
current gradient becomes asymptotically supported on the \(\kappa\)-eigenspace.
For every selector between those two steps,
\[
\frac{F_2}{F_1}
=
\frac{\kappa r(1-\eta_1)^2+(1-\kappa\eta_1)^2}{1+\kappa r}
\longrightarrow(\kappa-1)^2.
\]
Thus the upper bound is sharp in supremum. If \(\kappa>2\), uniform convergence
over the shrinking BB interval gives objective increase for every selector when
\(r\) is sufficiently small. This proves the if-and-only-if frontier.

The standalone numerical artifact independently checks the matrix bound, the
closed-form construction, convex selectors across the BB interval, and values on
both sides of the threshold.

## Originality

**PASS, to the best of our knowledge.**

The literature check began from the classical BB papers and then followed later
convergence, spectral-family, survey, harmonic-Rayleigh, and recent sharp-rate work.

- Barzilai--Borwein (1988) introduces the two-point steps and analyzes the
  two-dimensional quadratic case.
- Raydan (1993) explicitly states that the BB choice does not guarantee objective
  descent while proving convergence for strictly convex quadratics.
- Raydan (1997) uses a nonmonotone line search to globalize BB.
- Dai--Liao (2002) establishes \(R\)-linear convergence for any-dimensional strongly
  convex quadratics.
- Dai--Huang--Liu (2019) studies convex combinations of the long and short BB steps.
- Zou--Magoulès (2022) surveys delayed-gradient and BB spectral behavior.
- Ferrandi--Hochstenbach--Krejić (2023) gives accessible formulas for BB1, BB2 and
  the convex-combination interval and develops a broader harmonic-Rayleigh framework.
- Recent Yang--Yuan work (2026) establishes sharp asymptotic rates and a Lyapunov
  description while explicitly retaining nonmonotone objective behavior.

Searches for exact and synonymous formulations involving BB objective monotonicity,
condition number, one-step amplification, BB1/BB2 blends, and the numerical
threshold \(2\) did not locate the theorem proved here. In particular, the checked
sources establish nonmonotonicity and asymptotic convergence but did not provide
the sharp uniform statement
\[
\kappa\le2
\quad\Longleftrightarrow\quad
\text{universal objective monotonicity over the BB interval class},
\]
nor the sharp one-step supremum \((\kappa-1)^2\).

Residual originality risk remains because complete theorem-level text of some broad
historical sources, especially the original 1988 article and Fletcher's 2005 BB
chapter, was not inspected in full. The originality assessment is therefore
explicitly limited to the best of our knowledge.

## Value

**PASS.**

The result converts the familiar qualitative statement “BB can be nonmonotone”
into an exact and reusable condition-number boundary. It also shows that the issue
is not specific to choosing the long or short BB step: the obstruction persists
uniformly for every adaptive selector lying between them, including the standard
convex-combination family. The exact-line-search warm-up construction rules out an
explanation based only on a poor arbitrary initialization.

The sharp amplification factor quantifies how large a single objective excursion
can be as a function of conditioning, while remaining fully compatible with the
known global and asymptotic convergence theory.

## Scientific limitations

- Finite-dimensional real SPD quadratics and exact arithmetic only.
- Objective-gap monotonicity only; other norms and floating-point quantities are
  not covered.
- The selector must remain inside the contemporaneous BB2--BB1 interval.
- Particular trajectories can remain monotone above the threshold.
- No new asymptotic rate, iteration complexity, or implementation-performance claim
  is made.
- Some historical sources were not inspected in complete theorem-level form, so
  hidden equivalent prior coverage cannot be excluded.
