# Degeneracy-order phase diagram for adaptive universal trust-region steps

## Finding

Let \(f_p(x)=|x|^p/p\), with \(p\ge3\), and consider the local, zero-tolerance update map obtained from the adaptive universal trust-region (UTR-Adaptive) subproblem and Strategy 4.1 of Jiang et al. Assume exact subproblem solutions and a sufficiently small nonzero starting point. Let \(\rho_{\min}>0\) be the parameter floor. The accepted parameter reaches \(\rho_{\min}\) after finitely many steps.

At cubic flatness, \(p=3\), the eventual recurrence is exactly

\[
 x_{k+1}=q_3(\rho_{\min})x_k,
 \qquad
 q_3(\rho)=\begin{cases}
 1/2,&0<\rho\le1,\\
 1-1/(2\rho),&1<\rho\le2,\\
 1-1/(4\rho),&\rho>2.
 \end{cases}
\]

For every \(p>3\), the trust-region boundary is eventually active and

\[
 |x_{k+1}|=|x_k|-\frac{|x_k|^{(p-1)/2}}{4\rho_{\min}},
 \qquad
 |x_k|\sim\left(\frac{8\rho_{\min}}{(p-3)k}\right)^{2/(p-3)}.
\]

Thus the branch ratio \(f_p''(x)/\sqrt{|f_p'(x)|}=(p-1)|x|^{(p-3)/2}\) separates an eventual linear regime at \(p=3\) from a boundary-limited polynomial tail for \(p>3\).

## Assumptions and scope

- The objective agrees with \(f_p(x)=|x|^p/p\) in a neighborhood of its minimizer \(x=0\). For \(p\ge3\), this local germ has a locally Lipschitz Hessian; a bounded-below global extension with Lipschitz Hessian can be made with a smooth cutoff without changing the local trajectory.
- The update is the exact one-dimensional UTR-Adaptive subproblem from Algorithm 3 and Strategy 4.1 of the cited source, with fixed \(\rho_{\min}>0\), \(\gamma_2>1\), and the source's admissible acceptance parameters, including \(\eta<1/32\) and \(1/4<\xi<1\).
- “Zero-tolerance” denotes the infinite local update map before the algorithm's finite-tolerance stopping test. For any positive stopping tolerance, the observed trajectory terminates; the asymptotic statement describes the pre-termination law as the tolerance is decreased.
- The claim is one-dimensional and local. It does not assert a multidimensional extension, a global rate, or a complexity lower bound.

## Proof

Write \(a=|x|\). For \(x\ne0\),

\[
 |f_p'(x)|=a^{p-1},\qquad f_p''(x)=(p-1)a^{p-2},\qquad \sqrt{|f_p'(x)|}=a^{(p-1)/2}.
\]

The branch selector in Strategy 4.1 compares \(f_p''(x)\) with \(\rho\sqrt{|f_p'(x)|}\), so their ratio is \((p-1)a^{(p-3)/2}\).

**Acceptance and parameter floor.** For \(p>3\), the ratio tends to zero, the middle branch is selected, and its boundary step has size \(a^{(p-1)/2}/(4\rho)\). Taylor expansion gives

\[
 \frac{\rho\,[f_p(x)-f_p(x+d)]}{|f_p'(x)|^{3/2}}\longrightarrow\frac14>\eta.
\]

Hence the first inner-loop trial is accepted for sufficiently small \(a\). For \(p=3\), the branch ratio is exactly \(2\). If \(0<\rho\le1\), the Newton step is feasible and the gradient ratio is exactly \(1/4<\xi\). If \(1<\rho\le2\), the decrease ratio is

\[
 \frac{\rho\,[f_3(x)-f_3(x+d)]}{|f_3'(x)|^{3/2}}
 =\frac12-\frac{1}{4\rho}+\frac{1}{24\rho^2}>\eta.
\]

If \(\rho>2\), it is

\[
 \frac{\rho\,[f_3(x)-f_3(x+d)]}{|f_3'(x)|^{3/2}}
 =\frac14-\frac{1}{16\rho}+\frac{1}{192\rho^2}>\eta.
\]

Thus, locally, the inner loop accepts its first trial. The update \(\rho_{k+1}=\max\{\rho_{\min},\rho_k/\gamma_2\}\) therefore reaches \(\rho_{\min}\) after finitely many steps.

**The case \(p=3\).** Here \(f_3''(x)=2|x|\) and \(\sqrt{|f_3'(x)|}=|x|\). For \(\rho\le2\), Strategy 4.1 sets \(\sigma=0\) and radius \(|x|/(2\rho)\). The unconstrained Newton step has size \(|x|/2\): it is feasible when \(\rho\le1\), and the boundary is active when \(1<\rho\le2\). For \(\rho>2\), the middle branch sets \(\sigma=\rho\) and radius \(|x|/(4\rho)\); its unconstrained step has size \(|x|/(\rho+2)\), which exceeds that radius. These three cases give the stated exact factor \(q_3(\rho_{\min})\).

**The case \(p>3\).** Since \((p-1)a^{(p-3)/2}\to0\), the middle branch is eventually selected. Its unconstrained step has magnitude

\[
 |d_{\rm unc}|=\frac{a^{p-1}}{(p-1)a^{p-2}+\rho_{\min}a^{(p-1)/2}},
\]

whereas the radius is \(a^{(p-1)/2}/(4\rho_{\min})\). The ratio of these magnitudes tends to \(4\), so the constraint is eventually active and the recurrence in the Finding section follows. Put \(s=(p-3)/2>0\) and \(c=1/(4\rho_{\min})\). Then

\[
 |x_{k+1}|=|x_k|(1-c|x_k|^s),\qquad
 |x_{k+1}|^{-s}-|x_k|^{-s}\longrightarrow sc.
\]

Summing yields \(|x_k|^{-s}\sim sc\,k=((p-3)/(8\rho_{\min}))k\), which is equivalent to the claimed asymptotic. The argument is analytic; the finite script below is only a numerical sanity check.

## Verification

The symbolic branch calculations above use the exact derivatives and exact solution of the scalar trust-region subproblem. The included standard-library script checks the exact \(p=3\) factors and compares finite-iterate values of \(|x_k|^{-(p-3)/2}/k\) with the predicted limit for \(p=4,5\). These finite checks are not used as proof of the infinite asymptotic. Reproduce them with `python3 verification.py`.

## Relationship to prior work

Jiang et al. introduce the UTR subproblem, the adaptive branch selector, and a quadratic local-convergence theorem for a non-degenerate local optimum. Their Theorem 4.3 uses a positive-definite Hessian at the limiting point; the power minima here satisfy \(f_p''(0)=0\), so that theorem does not imply the result. The present statement instead computes the exact branch behavior and asymptotic law for this degenerate family.

Gradient-regularized Newton methods of Mishchenko, and the Bregman-regularized Newton method of Doikov and Nesterov, use different update rules and state local superlinear behavior under strong-convexity assumptions. They are relevant neighboring methods, but those stated results do not imply this branch-dependent UTR recurrence. Semantic searches also returned analyses of other algorithms (including fixed-radius composite trust-region gradient descent and accelerated fixed-point methods), not this claim. Search failure is not proof of novelty; see the review record for the remaining risk.

## Limitations

The classification concerns the exact local update map on a one-dimensional power germ. It does not cover inexact subproblem solves, noisy derivatives, multidimensional flat minima, or arbitrary degenerate critical points. A positive tolerance truncates the trajectory, so the polynomial law is an asymptotic pre-termination statement. The literature search was targeted rather than exhaustive; an equivalent result in unqueried trust-region literature remains possible.

## References

1. Y. Jiang, C. He, C. Zhang, D. Ge, B. Jiang, and Y. Ye, “A Universal Trust-Region Method for Convex and Nonconvex Optimization,” arXiv:2311.11489v1, first public 2023-11-20; later published as “Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses,” *Journal of Scientific Computing* 106 (2026), DOI 10.1007/s10915-025-03154-y. See Algorithm 3, Strategy 4.1, and Theorem 4.3.
2. K. Mishchenko, “Regularized Newton Method with Global \(O(1/k^2)\) Convergence,” *SIAM Journal on Optimization* 33(3) (2023), 1440–1462, DOI 10.1137/22M1488752.
3. N. Doikov and Y. Nesterov, “Gradient Regularization of Newton Method with Bregman Distances,” *Mathematical Programming* 204 (2024), 1–25, DOI 10.1007/s10107-023-01943-7.
