# Sharp objective-monotonicity frontier for Barzilai–Borwein interval steps

## Setting

Let
\[
f(x)=\frac12 x^\top A x-b^\top x,\qquad A=A^\top\succ0,
\]
with smallest and largest eigenvalues \(0<\mu\le L\) and condition number
\[
\kappa=\frac{L}{\mu}.
\]
Write \(x_\star=A^{-1}b\), \(e_k=x_k-x_\star\), \(g_k=Ae_k\), and
\[
F_k=f(x_k)-f(x_\star)=\frac12 e_k^\top A e_k.
\]

A scalar gradient step is
\[
x_{k+1}=x_k-\eta_k g_k.
\]
For a nonzero previous displacement \(s_{k-1}=x_k-x_{k-1}\), the two classical
Barzilai–Borwein steps on this quadratic are
\[
\eta_k^{\rm BB1}
 =\frac{s_{k-1}^\top s_{k-1}}{s_{k-1}^\top A s_{k-1}},
\qquad
\eta_k^{\rm BB2}
 =\frac{s_{k-1}^\top A s_{k-1}}{s_{k-1}^\top A^2 s_{k-1}}.
\]
We consider the full **BB interval class**
\[
\eta_k^{\rm BB2}\le \eta_k\le \eta_k^{\rm BB1}.
\]
It contains BB1, BB2, and every convex combination of the two steps, including the
spectral-gradient family studied by Dai, Huang and Liu.

## Theorem

For every finite-dimensional real SPD quadratic and every nonstationary step in the
BB interval class,
\[
\boxed{\frac{F_{k+1}}{F_k}\le(\kappa-1)^2.}
\]

The constant is sharp in the strongest uniform sense:
\[
\boxed{
\sup \frac{F_{k+1}}{F_k}=(\kappa-1)^2,
}
\]
where the supremum ranges over SPD quadratics of condition number \(\kappa\), valid
histories, and arbitrary choices of \(\eta_k\) inside the BB interval. The same
supremum remains sharp even if the history is required to begin with an exact
line-search (Cauchy) step.

Consequently,
\[
\boxed{\kappa\le2}
\]
is the exact condition-number frontier for **universal objective monotonicity** of
the entire BB interval class:

- if \(\kappa<2\), every such step satisfies
  \[
  F_{k+1}\le(\kappa-1)^2F_k<F_k;
  \]
- if \(\kappa=2\), every such step is nonincreasing;
- if \(\kappa>2\), there is a two-dimensional SPD quadratic and an exact-line-search
  warm-up for which, on the next step, **every** selector between BB2 and BB1
  increases the objective. Thus adaptive blending within the BB interval cannot
  restore a universal descent guarantee once \(\kappa>2\).

## Proof

### 1. Every BB-interval step lies between \(1/L\) and \(1/\mu\)

Rayleigh quotient bounds give
\[
\frac1L\le \eta_k^{\rm BB1}\le\frac1\mu,
\qquad
\frac1L\le \eta_k^{\rm BB2}\le\frac1\mu.
\]
Moreover, Cauchy–Schwarz yields
\[
(s^\top As)^2\le(s^\top s)(s^\top A^2s),
\]
so
\[
\eta_k^{\rm BB2}\le\eta_k^{\rm BB1}.
\]
Hence every interval selector satisfies
\[
\frac1L\le\eta_k\le\frac1\mu.
\]

### 2. Universal one-step amplification bound

Since
\[
e_{k+1}=(I-\eta_kA)e_k,
\]
diagonalizing \(A\) gives
\[
\frac{F_{k+1}}{F_k}
\le
\max_{\lambda\in[\mu,L]}|1-\eta_k\lambda|^2.
\]
Over
\[
\eta_k\in[1/L,1/\mu],
\]
the largest possible magnitude of \(1-\eta_k\lambda\) is
\[
\max\left\{1-\frac{\mu}{L},\frac{L}{\mu}-1\right\}
=\kappa-1.
\]
Therefore
\[
\frac{F_{k+1}}{F_k}\le(\kappa-1)^2.
\]

If \(\kappa\le2\), this immediately gives \(F_{k+1}\le F_k\), with strict
contraction whenever \(\kappa<2\) and \(F_k>0\).

### 3. Sharpness after an exact line-search warm-up

Scale \(\mu=1\) and take
\[
A=\operatorname{diag}(1,\kappa).
\]
For \(r>0\), choose the initial gradient
\[
g_0=(1,\sqrt r)^\top.
\]
Use an exact line-search first step:
\[
\eta_0
=\frac{g_0^\top g_0}{g_0^\top Ag_0}
=\frac{1+r}{1+\kappa r}.
\]
Then
\[
g_1=(I-\eta_0A)g_0
=\frac{\kappa-1}{1+\kappa r}
\begin{pmatrix}r\\-\sqrt r\end{pmatrix}.
\]

The next BB endpoints, computed from the first secant, are
\[
\eta_1^{\rm BB1}
=\frac{1+r}{1+\kappa r},
\qquad
\eta_1^{\rm BB2}
=\frac{1+\kappa r}{1+\kappa^2r}.
\]
Both tend to \(1=1/\mu\) as \(r\downarrow0\). Therefore any selector
\[
\eta_1(r)\in
[\eta_1^{\rm BB2},\eta_1^{\rm BB1}]
\]
also satisfies \(\eta_1(r)\to1\).

For an arbitrary such selector, direct substitution gives
\[
\frac{F_2}{F_1}
=
\frac{
 \kappa r(1-\eta_1)^2+(1-\kappa\eta_1)^2
}{
 1+\kappa r
}.
\]
Thus, uniformly over every choice inside the shrinking BB interval,
\[
\lim_{r\downarrow0}\frac{F_2}{F_1}
=(\kappa-1)^2.
\]
This proves sharpness of the global bound.

For the two endpoint rules separately, the ratios simplify to
\[
\frac{F_2^{\rm BB1}}{F_1}
=
(\kappa-1)^2
\frac{\kappa r^3+1}{(1+\kappa r)^3},
\]
and
\[
\frac{F_2^{\rm BB2}}{F_1}
=
(\kappa-1)^2
\frac{\kappa^2r^2-\kappa r+1}{(1+\kappa^2r)^2}.
\]

When \(\kappa>2\), the common limiting value is strictly larger than \(1\).
Hence for all sufficiently small positive \(r\), not merely BB1 and BB2 but every
step chosen between them increases the objective on that next iteration. This proves
necessity of \(\kappa\le2\) for a universal monotonicity guarantee.

## Interpretation

The classical fact that BB methods can be nonmonotone is stronger than the existence
of isolated bad steps. For SPD quadratics, the entire interval between the two
canonical BB spectral steps has a sharp condition-number phase transition:

- below condition number \(2\), no native BB1/BB2 blend can increase the quadratic
  objective;
- above \(2\), even an exact line-search warm-up cannot prevent a subsequent
  objective increase, and choosing adaptively anywhere between BB2 and BB1 does not
  remove the obstruction;
- the largest possible one-step objective amplification is exactly
  \((\kappa-1)^2\) in supremum.

The statement is one-step and worst-case. It is compatible with the established
global and asymptotic convergence of BB methods: a convergent nonmonotone trajectory
may contain large individual objective increases.

## Relation to prior literature

Barzilai and Borwein introduced the two spectral steps and analyzed the
two-dimensional quadratic dynamics. Raydan explicitly noted that the BB choice does
not guarantee descent and later coupled BB with a nonmonotone line search. Dai and
Liao proved \(R\)-linear convergence on strongly convex quadratics. Dai, Huang and
Liu introduced a family whose steps are convex combinations of BB1 and BB2.
Later surveys and harmonic-Rayleigh formulations document the ordering
\(\eta^{\rm BB2}\le\eta\le\eta^{\rm BB1}\) for that convex family and place BB in a
broader spectral-gradient framework. Recent 2026 work gives sharp asymptotic rates
and Lyapunov descriptions of nonmonotone quadratic BB dynamics.

The searches and accessible theorem statements inspected for these works did not
locate the exact universal frontier \(\kappa=2\), the sharp one-step amplification
\((\kappa-1)^2\), or the uniform obstruction for every selector in the BB interval.
The originality claim is therefore to the best of our knowledge, not an assertion
that all historical literature has been exhausted.

## Limitations

- The theorem is for finite-dimensional real SPD quadratics in exact arithmetic.
- It concerns objective-gap monotonicity, not monotonicity of the Euclidean gradient
  norm, iterate norm, or floating-point residuals.
- The interval class requires the step to lie between the contemporaneous BB2 and
  BB1 values formed from the same previous secant. It does not cover spectral rules
  deliberately choosing steps outside that interval, clipping rules, line searches,
  trust regions, or other globalization devices.
- The threshold is a uniform worst-case guarantee. Particular problems and
  trajectories can remain monotone when \(\kappa>2\).
- The result does not improve known asymptotic convergence rates or iteration
  complexity.
- Complete theorem-level text of some broad historical treatments, including the
  original 1988 article and Fletcher's 2005 chapter, was not inspected in full;
  an equivalent historical statement remains the principal originality risk.

## Reproducibility

`artifacts/verify_bb_monotonicity.py` checks the sharp upper bound on deterministic
random SPD examples, verifies the two-dimensional construction, tests selectors
throughout the BB interval, and reproduces the transition at \(\kappa=2\).
`artifacts/verification.txt` records its deterministic output.

## References

1. J. Barzilai and J. M. Borwein, “Two-Point Step Size Gradient Methods,”
   *IMA Journal of Numerical Analysis* 8 (1988), 141–148.
   https://doi.org/10.1093/imanum/8.1.141
2. M. Raydan, “On the Barzilai and Borwein choice of steplength for the gradient
   method,” *IMA Journal of Numerical Analysis* 13 (1993), 321–326.
   https://doi.org/10.1093/imanum/13.3.321
3. M. Raydan, “The Barzilai and Borwein Gradient Method for the Large Scale
   Unconstrained Minimization Problem,” *SIAM Journal on Optimization* 7 (1997),
   26–33. https://doi.org/10.1137/S1052623494266365
4. Y.-H. Dai and L.-Z. Liao, “R-linear convergence of the Barzilai and Borwein
   gradient method,” *IMA Journal of Numerical Analysis* 22 (2002), 1–10.
   https://doi.org/10.1093/imanum/22.1.1
5. Y.-H. Dai, Y. Huang and X.-W. Liu, “A family of spectral gradient methods for
   optimization,” *Computational Optimization and Applications* 74 (2019), 43–65.
   https://doi.org/10.1007/s10589-019-00107-8
6. Q. Zou and F. Magoulès, “Delayed Gradient Methods for Symmetric and Positive
   Definite Linear Systems,” *SIAM Review* 64 (2022), 517–553.
   https://doi.org/10.1137/20M1321140
7. G. Ferrandi, M. E. Hochstenbach and N. Krejić, “A harmonic framework for
   stepsize selection in gradient methods,” *Computational Optimization and
   Applications* 85 (2023), 75–106.
   https://doi.org/10.1007/s10589-023-00455-6
8. S. Yang and Y.-X. Yuan, “The Sharp Worst-Case Asymptotic Rate of the
   Barzilai--Borwein Method in R^d and Hilbert Spaces,” arXiv:2608.07839 (2026).
   https://arxiv.org/abs/2608.07839
9. S. Yang and Y.-X. Yuan, “Lyapunov Functions and R-Linear Convergence for
   Quadratic Barzilai-Borwein Dynamics,” arXiv:2609.12084 (2026).
   https://arxiv.org/abs/2609.12084
