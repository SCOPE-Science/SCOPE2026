# Exact two-landmark design for a cosine kernel: a noise-independent angle and a quarter-power collision law

## Finding

Let \(k_a(x,y)=a+\cos(x-y)\) on the circle \(\mathbb R/(2\pi\mathbb Z)\), where \(a>0\). Given two landmarks at angular distance \(\Delta\in[0,\pi]\), and a regularization or independent observation-noise variance \(t>0\), define the uniform integrated residual

\[
V_{a,t}(\Delta)=\frac{1}{2\pi}\int_0^{2\pi}\bigl[k_a(x,x)-k_a(x,Z)(K_a(Z,Z)+tI_2)^{-1}k_a(Z,x)\bigr]dx.
\]

Write \(u=\cos^2(\Delta/2)\). The following is the **complete global classification** of the two-landmark minimizer:

\[
V_{a,t}(u)=a+1-\frac{2a^2+u}{t+2a+2u}-\frac{1-u}{t+2-2u}.
\]

Set \(C=t+2a-4a^2\), and define

\[
a_c(t)=\frac{-t^2+4t+4+(t+2)\sqrt{17t^2+20t+4}}{4(t^2+5t+4)}.
\]

If \(a\ge a_c(t)\), the unique minimizing separation is antipodal: \(\Delta_*=\pi\), or \(u_*=0\). If \(0<a<a_c(t)\), the unique minimizer is at the strictly interior value

\[
u_*=\frac{(t+2)\sqrt C-(t+2a)\sqrt t}{2(\sqrt t+\sqrt C)},\qquad \Delta_*=2\arccos\sqrt{u_*}\in(0,\pi).
\]

In particular, **at \(a=1/2\), the optimal separation is exactly \(\Delta_*=2\pi/3\) for every \(t>0\)**. This angle is independent of the noise variance.

For every fixed \(0<a<1/2\), the minimizing separation has the sharp low-noise law

\[
\Delta_*\sim 2\sqrt{\frac{a+1}{\sqrt{2a(1-2a)}}}\,t^{1/4}\qquad(t\downarrow0).
\]

Thus the two landmarks approach one another with the fourth root of the noise variance, but never coincide when \(t>0\).

## Assumptions and scope

The design consists of exactly two locations, with repetitions permitted and charged as two independently noisy observations. The circle carries normalized uniform measure. Both kernel parameters and the positive ridge/noise variance are known. The objective is the integrated diagonal posterior covariance, equivalently the integrated diagonal residual of the ridge-regularized Nyström approximation. It is not the squared integrated kernel error, an operator-norm criterion, entropy, or a finite-data fitting score. Rotating both landmarks does not change the objective; uniqueness means uniqueness of their smaller angular separation, up to rotation and relabeling.

The kernel is positive semidefinite because \(k_a(x,y)=\phi_a(x)\cdot\phi_a(y)\) with \(\phi_a(x)=(\sqrt a,\cos x,\sin x)\). Its integral operator has rank three.

## Proof

**1. Exact reduction.** Rotate the landmarks to \(z_\pm=\pm\Delta/2\) and use the symmetric and antisymmetric unit vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\). The two eigenvalues of \(K_a(Z,Z)+tI_2\) are \(t+2a+2u\) and \(t+2-2u\), respectively. The associated squared coordinates of the kernel evaluation vector, averaged over the uniform circle, are \(2a^2+u\) and \(1-u\). Taking the trace of the integrated rank-two quadratic form proves the displayed exact formula for \(V_{a,t}(u)\). For \(t>0\), both denominators stay strictly positive throughout \(0\le u\le1\).

**2. One-dimensional derivative and phase boundary.** Differentiation gives

\[
\frac{dV_{a,t}}{du}=-\frac{C}{(t+2a+2u)^2}+\frac{t}{(t+2-2u)^2}.
\]

If \(C\le0\), this derivative is positive everywhere and \(u_*=0\). For \(C>0\), its sign is the sign of

\[
h(u)=\frac{\sqrt t}{t+2-2u}-\frac{\sqrt C}{t+2a+2u}.
\]

Both terms contribute a strictly positive derivative to \(h\), hence \(h\) is strictly increasing. At \(u=1\), the inequality \(h(1)>0\) follows from the exact positive identity

\[
(t+2a+2)^2-tC=2(2a^2t+2a^2+at+4a+2t+2)>0.
\]

At \(u=0\), the condition \(h(0)<0\) is equivalent to

\[
F(a,t):=(t+2)^2(t+2a-4a^2)-t(t+2a)^2>0.
\]

For each fixed \(t>0\), \(F(a,t)\) is a concave quadratic in \(a\), is positive at \(a=0\), and tends to negative infinity. It therefore has exactly one positive root. Solving this quadratic gives the displayed \(a_c(t)\). For \(a\ge a_c(t)\), the derivative is nonnegative and strictly positive away from at most \(u=0\); the minimum is uniquely \(u_*=0\). For \(a<a_c(t)\), strict increase of \(h\), with opposite endpoint signs, gives a unique interior zero. Solving \(h(u)=0\) gives the stated \(u_*\). The derivative changes sign from negative to positive there, proving the global minimum, without an unproved stationary-point assumption.

**3. Universal angle.** At \(a=1/2\), \(C=t\) and the expression for \(u_*\) simplifies exactly to \(1/4\). Since the threshold condition is strict at this parameter, the minimizer is unique. The relation \(u_*=\cos^2(\Delta_*/2)\) gives \(\Delta_*=2\pi/3\) for every positive \(t\).

**4. Singular small-noise limit.** Fix \(0<a<1/2\). Then \(C\to C_0=2a(1-2a)>0\) as \(t\downarrow0\), and a Taylor expansion of the exact stationary point yields

\[
1-u_*=\frac{a+1}{\sqrt{C_0}}\sqrt t+O(t).
\]

Since \(\Delta=2\arccos\sqrt u=2\sqrt{1-u}+O((1-u)^{3/2})\) near \(u=1\), the quarter-power law follows.

**5. Noiseless boundary and rank change.** At \(t=0\), for distinct landmarks \(0\le u<1\), the ordinary unregularized inverse exists and

\[
V_{a,0}(u)=\frac{a(2u+1)}{2(a+u)}.
\]

Its derivative has the sign of \(2a-1\). For \(a>1/2\), antipodal landmarks uniquely minimize it; for \(a=1/2\), every distinct pair gives the same value \(1/2\); for \(0<a<1/2\), the infimum \(3a/[2(a+1)]\) is approached as the two distinct landmarks collide but is not attained by a distinct pair. At exact collision the matrix has rank one, so the Moore–Penrose definition gives

\[
V^{\mathrm{coll}}_{a,0}=a+1-\frac{a^2+1/2}{a+1}
=\frac{2a+1/2}{a+1},
\]

which exceeds the distinct-pair limit by exactly \(1/2\). This rank-loss discontinuity explains why the positive-noise fourth-root law is a genuinely singular boundary effect rather than permission to place two noiseless points at the same location.

## Verification

The standalone \(\texttt{verify.py}\) uses two independent computations of integrated posterior variance: direct inversion of the original two-by-two Gram matrix followed by a uniform trigonometric integral, and the analytic symmetric/antisymmetric decomposition. It also exercises exact rational identities, checks the phase classification against a dense grid, and checks the universal angle, quarter-power asymptotic coefficient, and pseudoinverse collision jump. Run with \(\texttt{python3 verify.py}\). The verified package run reports **7,770 passed assertions**. The infinite-domain optimality and asymptotic claims are proved above, not inferred from these finite tests.

## Relationship to prior work

The 2023 work of Hayakawa, Oberhauser and Lyons studies Nyström approximation and integrated residuals under sampling and subspace selection, but its inspected results do not state the exact positive-ridge two-landmark cosine-kernel design. The 2015 preprint by Gorodetsky and Marzouk develops GP integrated-variance experimental design and includes periodic-kernel experiments with a different, infinite-rank kernel, but the inspected sections give a continuous numerical optimization framework rather than this finite-rank analytic phase classification. Xu and Shang's classical trigonometric-regression design work studies unregularized regression optimality criteria and could be adjacent; only its abstract was accessible, so specialized earlier coverage cannot be categorically excluded. The new mathematical content is the explicit phase boundary, the all-noise \(120^\circ\) identity, and the singular fourth-root limiting law for the specified positive-ridge problem.

## Limitations

The result does not optimize over three or more landmarks, unequal noise variances, nonuniform integration weights, adaptive schemes, or arbitrary periodic kernels. It asserts no numerical-conditioning guarantee as \(t\to0\); indeed, the noiseless colliding configuration is singular. Full-text comparison with the 2014 Xu–Shang article was unavailable, leaving a publication-priority risk. No independent scientific audit has been performed.

## References

1. S. Hayakawa, H. Oberhauser and T. Lyons, *Sampling-based Nyström Approximation and Kernel Quadrature*, first public arXiv posting 23 January 2023, https://arxiv.org/abs/2301.09517 ; ICML 2023, https://proceedings.mlr.press/v202/hayakawa23a.html .
2. A. A. Gorodetsky and Y. M. Marzouk, *Mercer Kernels and Integrated Variance Experimental Design: Connections Between Gaussian Process Regression and Polynomial Approximation*, first public posting 27 February 2015, https://arxiv.org/abs/1503.00021 ; SIAM/ASA J. Uncertainty Quantification 4 (2016), 796–828.
3. X. Xu and X. Shang, *Optimal and Robust Designs for Trigonometric Regression Models*, Metrika 77 (2014), 753–769, https://doi.org/10.1007/s00184-013-0463-7 (abstract available; full text not independently inspected).
4. H. Dette, V. Melas and P. Shpilev, *Optimal Designs for Trigonometric Regression Models*, https://doi.org/10.17877/DE290R-813 (2009); different classical coefficient-estimation criterion.
