# A sharp local ascent boundary for directional Gaussian smoothing on smooth strongly convex objectives

## Finding

Let \(d\ge2\), \(\sigma>0\), \(\delta>0\), and \(u\in\mathbb R^d\setminus\{0\}\). Let \(g\in C^2(\mathbb R)\) be even with bounded, nonnegative second derivative and \(g(0)=g''(0)=0\). Consider the globally smooth, \(\delta\)-strongly convex objective
\[
 f(z)=\frac{\delta}{2}\|z\|_2^2+g(u^{\mathsf T}z),\qquad z\in\mathbb R^d.
\]
Write \(Z\sim N(0,1)\). Its exact coordinate-direction Gaussian-smoothing (DGS) field at common smoothing radius \(\sigma\) is
\[
 F_i(z)=\mathbb E\big[\partial_i f(z+\sigma Z e_i)\big],\qquad i=1,\ldots,d.
\]
Define
\[
 c_i=\mathbb E\,g''(\sigma u_i Z),\qquad a_i=u_i c_i,
 \qquad \delta_*=\frac{\|u\|_2\|a\|_2-u^{\mathsf T}a}{2}.
\]
**Sharp local criterion.** The symmetric part of the Jacobian \(DF(0)\) has least eigenvalue exactly \(\delta-\delta_*\). If \(0<\delta<\delta_*\), one fixed nonzero vector \(v\) has the property that **for every fixed stepsize \(h>0\)**,
\[
 f(tv-hF(tv))>f(tv)\quad\text{for all sufficiently small }t>0.
\]
Thus exact DGS points strictly uphill, arbitrarily close to the unique minimizer, for a smooth strongly convex function; shrinking a fixed positive stepsize cannot ensure universal one-step objective descent. If \(\delta>\delta_*\), the field \(-F\) is instead a strict descent direction at every nonzero point in some neighborhood of the minimizer. Equality is a threshold for the quadratic local test, not a claimed full nonlinear classification.

An explicit analytic two-dimensional witness uses \(\sigma=1\), \(\delta=1/1000\), \(u=(1,10)^{\mathsf T}\), and the unique even function with \(g(0)=g'(0)=0\) and \(g''(s)=s^2e^{-s^2/2}\), namely
\[
 g(s)=\sqrt{\frac\pi2}\,s\,\operatorname{erf}(s/\sqrt2)+2(e^{-s^2/2}-1).
\]
Here
\[
 \delta_*=0.1569212492283318\ldots>\delta.
\]
The rational direction \(v=(-99/10,1)^{\mathsf T}\) is an exact witness.

## Assumptions and scope

The operator is the **exact** expected directional derivative, with the standard normal variance-one convention and the **same** smoothing radius in every coordinate. Each direction is one of the coordinate unit vectors. Smoothness and strong convexity are global: since \(0\le g''\le M<\infty\), the Hessian satisfies
\[
 \delta I\preceq\nabla^2 f(z)\preceq (\delta+M\|u\|_2^2)I.
\]
Evenness and \(g(0)=0\) imply \(g'(0)=0\) and \(g(s)\ge0\), so \(0\) is the unique minimizer. The condition \(g''(0)=0\) makes the objective locally isotropic to second order, while the finite-radius DGS field retains anisotropic information from the ridge.

## Proof

**1. The exact DGS Jacobian.** By differentiation under the Gaussian integral (bounded \(g''\) suffices),
\[
 F_i(z)=\delta z_i+u_i\mathbb E\,g'(u^{\mathsf T}z+\sigma u_i Z).
\]
The Gaussian term in the quadratic derivative has zero mean. Evenness makes \(g'\) odd; hence \(F(0)=0\). Differentiating at zero yields
\[
 DF(0)=J=\delta I+a u^{\mathsf T}.
\]
In general, \(J\) is not symmetric, even though \(\nabla^2 f(z)\) always is.

**2. Sharp spectral threshold.** For \(B=(a u^{\mathsf T}+u a^{\mathsf T})/2\), the eigenvalues on the span of \(u,a\) are
\[
 \lambda_{\pm}(B)=\frac{u^{\mathsf T}a\pm\|u\|_2\|a\|_2}{2};
\]
all remaining eigenvalues are zero. The formula follows by choosing an orthonormal basis beginning with \(u/\|u\|_2\): the resulting nontrivial symmetric block has trace \(u^{\mathsf T}a\) and eigenvalue separation \(\|u\|_2\|a\|_2\). Because \(d\ge2\), the least eigenvalue of \((J+J^{\mathsf T})/2=\delta I+B\) is \(\delta-\delta_*\). Cauchy–Schwarz gives \(\delta_*\ge0\), with strict inequality precisely when \(a\) and \(u\) are nonparallel. Since \(a_i=u_i c_i\) with \(c_i\ge0\), this means the active coordinate curvatures are unequal.

**3. Local objective-direction test.** For each fixed nonzero \(v\), continuity of \(g''\) and \(g''(0)=0\) give
\[
 \nabla f(tv)=\delta tv+o(t),\quad
 F(tv)=tJv+o(t),\quad
 f(tw)=\frac\delta2 t^2\|w\|_2^2+o(t^2)
\]
for any fixed \(w\). Consequently
\[
 \lim_{t\downarrow0}\frac{\nabla f(tv)^{\mathsf T}F(tv)}{\delta t^2}
 =v^{\mathsf T}Jv
 =\delta\|v\|_2^2+(u^{\mathsf T}v)(a^{\mathsf T}v).
\]
If \(\delta<\delta_*\), choose a unit eigenvector \(v\) of the negative least eigenvalue. Then \(v^{\mathsf T}Jv<0\). For any **fixed** \(h>0\), the stronger finite-step expansion is
\[
 \lim_{t\downarrow0}\frac{f(tv-hF(tv))-f(tv)}{\delta t^2}
 =-h\,v^{\mathsf T}Jv+\frac{h^2}{2}\|Jv\|_2^2>0.
\]
The same \(v\) works for all stepsizes (the required upper bound on \(t\) can depend on \(h\)). If \(\delta>\delta_*\), the symmetric part of \(J\) is positive definite, and the remainder in the directional test is uniform on the unit sphere; therefore \(\nabla f(z)^{\mathsf T}F(z)>0\) for all sufficiently small nonzero \(z\). This proves the stated strict local dichotomy away from equality.

**4. Explicit bounded-curvature witness.** The displayed \(g\) differentiates to
\[
 g'(s)=\sqrt{\frac\pi2}\,\operatorname{erf}(s/\sqrt2)-s e^{-s^2/2},
 \qquad g''(s)=s^2e^{-s^2/2}.
\]
Thus \(0\le g''(s)\le2/e\); the example is globally \(1/1000\)-strongly convex and its gradient is globally Lipschitz with constant at most \(1/1000+202/e\). The Gaussian identity
\[
 \mathbb E[(\tau Z)^2e^{-(\tau Z)^2/2}]=\frac{\tau^2}{(1+\tau^2)^{3/2}}
\]
gives
\[
 c_1=\frac{1}{2\sqrt2},\quad c_2=\frac{100}{101^{3/2}},\quad a=(c_1,10c_2)^{\mathsf T}.
\]
For \(v=(-99/10,1)^{\mathsf T}\), \(u^{\mathsf T}v=1/10\), hence
\[
 v^{\mathsf T}Jv=\frac{9901}{100000}-\frac{99}{100}c_1+c_2<0.
\]
Indeed \(c_1>1/3\) and \(c_2<1/10\) prove the strict inequality using only rational comparisons. The spectral formula evaluates to the displayed \(\delta_*\). This proves the explicit claim, including every fixed positive stepsize, without relying on floating-point experiments.

## Verification

Run `python3 verify_dgs.py` with Python 3 and only its standard library. The script independently integrates normal expectations by Simpson quadrature, verifies the analytic Gaussian formulas and the Jacobian, checks the sharp symmetric eigenvalue, and tests objective growth for several fixed stepsizes and scales. The recorded run passed 63 checks. These computations are corroboration; the theorem for all dimensions, all eligible ridge functions, all stepsizes and arbitrarily small initial points is proved above.

## Relationship to prior work

Zhang, Tran, Lu and Zhang introduced coordinate-direction Gaussian smoothing as a nonlocal search operator (arXiv:2002.03001, Section 3 and Appendix D). Tran and Zhang introduced an adaptive line-search variant (arXiv:2011.02009). Tran, Du and Zhang analyzed convergence to a controlled neighborhood under Lipschitz and strong-convexity assumptions (arXiv:2302.06404, Sections 2 and 4). Those results define the method and derive performance bounds; their inspected statements do not give the sharp local Jacobian threshold or a uniformly smooth strongly convex example for which **every** positive fixed step can raise the true objective arbitrarily near its unique minimizer. A neighborhood convergence estimate does not imply monotone objective decrease, so the present statement does not contradict it. Ordinary full-dimensional Gaussian convolution is a different operator: it is the gradient of one smoothed convex potential, while direction-by-direction assembly need not be conservative.

## Limitations

The theorem treats the exact DGS integral, a fixed coordinate frame and a common fixed radius. It gives a local, one-step obstruction, **not** global divergence or nonconvergence. The equality case \(\delta=\delta_*\) is classified only to quadratic order. It does not assess any finite Gauss–Hermite quadrature, Monte Carlo implementation, adaptive line search or higher-order update rule. No claim is made that the cited works assert monotone decrease.

## References

1. J. Zhang, H. Tran, D. Lu and G. Zhang, *A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization*, arXiv:2002.03001, first posted 2020-02-07, https://arxiv.org/abs/2002.03001.
2. H. Tran and G. Zhang, *AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient*, arXiv:2011.02009, first posted 2020-11-03, https://arxiv.org/abs/2011.02009.
3. H. Tran, Q. Du and G. Zhang, *Convergence analysis for a nonlocal gradient descent method via directional Gaussian smoothing*, arXiv:2302.06404, first posted 2023-02-13, https://arxiv.org/abs/2302.06404.
